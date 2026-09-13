---
HasBanner: false
archived: true
date: 2016-10-30
draft: false
featured: false
section: proyecto
sidebar: true
thumbnail: images/poland_ffth/toolbox.png
title: Uso de QGIS para la planificación de redes FTTH / GPON en consecuencia de la
  implementación de la Agenda Digital Europea.
type: case-study

---
{{<content-start >}}
# Uso de QGIS para la planificación de redes FTTH / GPON en consecuencia de la implementación de la Agenda Digital Europea.
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>October 30, 2016</span>
</p>

## Definición del problema.
Durante unos pocos años atrás muchos paises de Europa han lanzado programas operacionales para implementar la Agenda Digital Europea (EAC) desarrollada por la Comisión Europea en 2010. De acuerdo a sus directrices hasta 2020 todos los ciudadanos de la Unión Europea deben tener acceso a un ancho de banda de 30Mbps, y al menos la mitad de ellos deben tener acceso a un ancho de banda no menor a 100Mbps.

Polonia es uno de los paises en los cuales la Agenda se está implementando. Gracias a fondos de la Unión Europea muchos operadores locales pueden competir con los grandes proveedores de telecomunicaciones en cuanto a servicios de ancho de banda de alta velocidad. Desafortunadamente, la solicitud de financiación requiere una gran cantidad de trabajo necesario para elaborar la documentación adecuada, incluyendo, entre otras cosas, el desarrollo de mapas conceptuales de red FTTH (Fiber To The Home) planificados.

Además, actualmente no hay herramientas de TI basadas en SIG disponibles para ayudar a los potenciales beneficiarios con la preparación de la documentación. La complejidad del problema es aún mayor por el hecho de que dicho software debería permitir la creación de documentación de acuerdo con directrices específicas del programa (por ejemplo, la obligación de conectar las instituciones educativas).

Como tenemos una amplia experiencia en la industria de las telecomunicaciones, las entidades que solicitan fondos de la UE nos pidieron que creáramos un software que ayudara al desarrollo del mapa conceptual de la red FTTH. Los productos generados por el software desarrollado aceleraron significativamente el proceso de preparación de la aplicación.
## Descripción de la solución.
Debido a la gran popularidad, disponibilidad generalizada, la apertura del software y las inmensas capacidades funcionales, se vió natural seleccionar QGIS como la plataforma base para nuestra solución.

De acuerdo con las directrices del Consejo Europeo de FTTH , es crucial preparar primero un plan considerando tanto el aspecto técnico (colocación de cables, cierres de empalme, divisores) como el aspecto económico (demanda) basado en datos reales de puntos de dirección .La estructura de construcción y el desarrollo de la densidad de la construcción determinan la tecnología para el diseño de red GPON (Gigabit Passive Optical Network). Para tener la capacidad de planificar la topología de la red de manera eficiente, se requiere tener entre otras cosas: 
- Acceso a datos SI>G,
- automatización de procesamiento de datos SIG,
- aplicación de algoritmos de optimización de la red,
- Aplicación de las reglas de ingeniería de red GPON.

Todos estos elementos fueron conectados en la plataforma QGIS. Abajo hay una breve descripción de como realizamos el proyecto y que elementos funcionales fueron incorporados para crear una solución.

Para alcanzar nuestro objetivo, necesitábamos pocos componentes funcionales además de la plataforma GIS estándar:
- GRASS -  una colección de algoritmos de vectores y redes.
- Complementos de QGIS - OpenLayer. QuickOSM, Scipy Point Clustering, WorkContextTracer (nuestro plugin),
- QGIS modeler -- tool for graphical flow modelling,
- SpatiaLite - una base de datos local para almacenar datos entrantes y salientes.

The entire solution was based on the concept of so called wizards which realize the process of preparing the FTTx network technical concept step by step. Using \'geoprocessing\' modeller, we created models requiring only the necessary input data from operator. Algorithmic complexity was encapsulated within models in the form of designed flow, which use existing QGIS algorithms and calls dedicated scripts.

![](../images/poland_ffth/toolbox.png)

Para evitar que los resultados de análisis posteriores se mezclen, proporcionamos un complemento llamado WorkContextTracer que agrupa nuestro trabajo en los llamados contextos de trabajo.

![](../images/poland_ffth/workorder.png)

Los algoritmos de red basados en las funciones gráficas disponibles en GRASS se mejoraron agregando los scripts de telecomunicaciones. Introdujimos un concepto de agrupamiento de demanda que permite utilizar métodos K y medios jerárquicos para agregar puntos de demanda.

Geoprocessing scripts with usage of cable routing layer and Djikstra algorithm develops a cable route proposal with optical fiber nodes\' locations.

Los operadores también necesitaban una asociación entre los nodos de red creados y los puntos de dirección para estimar el costo individual de cada rama de la red. Para completar esta tarea, creamos scripts que realizan esta operación almacenando resultados en la base de datos local de SpatiaLite. Los datos debían ser exportables a una hoja de cálculo, por lo que utilizamos una biblioteca de software libre para cumplir con este requisito.
## Cómo utilizaron los usuarios la herramienta para crear el plan de red FTTH / GPON
El usuario comenzó a trabajar abriendo un nuevo contexto de trabajo y especificando una capa de entrada de puntos de dirección a analizar. Usando la interfaz estándar QGIS, el usuario podría establecer un conjunto de demandas en los puntos de dirección y finalmente proporcionar los parámetros necesarios para los pasos adicionales del algoritmo.

![](../images/poland_ffth/step1_inputlayer.png)

Sin tener información sobre la infraestructura civil existente, se utilizó una red de carreteras de OpenStreet correctamente filtrada como capa de enrutamiento. Algoritmos Scipy alimentados con parámetros de entrada, se agruparon los puntos de dirección en agregados de demanda marcándolos con un color distintos que indican su asignación a un grupo particular.

![](../images/poland_ffth/step1.png)

Con todos los puntos de dirección agrupados, el usuario inició los pasos de la planificación de red de alto nivel proporcionando capas preparadas en los pasos anteriores y una capa con el punto de inicio de la red GPON.

![](../images/poland_ffth/step1-2_result.png)

Upon the completion of the algorithm, in QGIS there are geometry objects representing planned cables and splice closure locations. Basing on demand data and network topology, an additional information is stored in database such as the length of the cable, its profile, node's serving areas.

![](../images/poland_ffth/step4_results.png)

En esta etapa, el usuario ya tenía toda la información para desarrollar un concepto técnico de la red FTTx de alto nivel. La parte final fue la generación de la hoja de cálculo con el informe de datos que muestra todos los datos calculados desde varias perspectivas diferentes.

![](../images/poland_ffth/report_generated.png)

![](../images/poland_ffth/report_generated_and_tranformed.png)
## Conclusión
Gracias al uso de la plataforma QGIS, así como a sus capacidades de extensión, logramos desarrollar una solución gratuita de código abierto que permite a los operadores de telecomunicaciones preparar los documentos necesarios para presentar la solicitud de cofinanciación en el programa de la UE que implementa la Agenda Digital Europea.

Al combinar algoritmos vectoriales flexibles con los scripts de ingeniería de telecomunicaciones, permitimos el uso práctico de algoritmos matemáticos para resolver problemas reales relacionados con la planificación de redes de telecomunicaciones. El usuario opera en un alcance de datos comprensible (municipio, edificio, carretera) mientras que la transformación de esta información en un modelo matemático queda oculta para el usuario.

El usuario obtuvo muchos beneficios útiles:
- Desarrollo automático del plan de red GPON a partir de datos disponibles públicamente y reglas de ingeniería de tecnología GPON.
- Posibilidad de personalizar la herramienta con directrices específicas del programa de la UE en un país determinado.
- Gran precisión de los resultados correspondientes a las dimensiones reales.
- Generación de datos necesarios para solicitar fondos de la UE: mapa conceptual de red, informe de cierre de cable y empalme con asignación de áreas de servicio.
- Posibilidad de determinar con precisión los costos de construcción y depreciación de cada parte de la red con el cálculo del costo de conexión de cada punto de dirección.
- Posibilidad de priorizar puntos de dirección de los más rentables a los no rentables.
- Posibilidad de evaluar indicadores económicos básicos como ROI, NPV.

## Enlaces útiles y bibliografía
- <http://europa.eu/rapid/press-release_MEMO-10-200_en.htm> - information on European Digital Agenda
- <http://www.ftthcouncil.eu/> - FTTH Council Europe website
- <https://www.scipy.org/> - SciPy project website
- <https://ksavinetworkinventory.com/en/download-geospatial-network-inventory-free/>
  - tool download webpage.

## Autores
La solución es una herramienta de código abierto completamente gratuita. Es parte de un proyecto más grande basado en plataformas QGIS y FreeCAD que tiene la intención utilizarse en la industria de las telecomunicaciones.

The author of this QGIS based solution is Softelnet (<https://www.softelnet.com>), a company manufacturing and integrating software for the telecommunications industry for over 15 years.

{{<content-end >}}
