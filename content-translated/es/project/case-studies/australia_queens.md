---
HasBanner: false
archived: true
date: 2011-01-01
draft: false
featured: false
section: proyecto
sidebar: true
thumbnail: images/australia_queens1.jpg
title: QGIS y GRASS en Mapeo de riesgo por incendio forestal en Gobierno Local
type: case-study

---
{{<content-start >}}
# QGIS y GRASS en Mapeo de riesgo por incendio forestal en Gobierno Local
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>January 01, 2011</span>
</p>

## Introducción
El Consejo Regional de Southern Downs (CRSD) es un gobierno local de tamaño pequeño/mediano en el sureste de Queensland, Australia. La región del consejo, sobre todo la parte sur, sufre de grandes incendios forestales. Los incendios forestales son una preocupación importante para los residentes y propietarios de tierras en la región de las llanuras del sur que se ha traducido en la pérdida de vidas y bienes.

Este proyecto permitirá al Consejo y al pueblo de la región ser más conscientes del riesgo y permitir una mejor toma de decisiones en el futuro.

![](../images/australia_queens1.jpg)
## El Proyecto
As bushfire is not only a problem for SDRC but also for the whole of Queensland, the state government requires that each local government identifies the bushfire hazard in their area via the State Planning Policy 1/03 Mitigating the Adverse Impacts of Flood, Bushfire and Landslide \[1\]. This kind of job would normally be done using consultants but was instead done by the council itself using a combination of QGIS and GRASS.

El componente SIG del proyecto fue dividido en 6 pasos principales
- Cálculo y mapeo de pendientes
- Evalucaión de aspecto y cartografía
- Cálculo y mapeo de vegetación
- Combinación de puntajes para identificar la intensidad del riesgo de incendio forestal
- Verificación de campo y evaluación cualitativa
- Mapas finales

## El uso de QGIS y GRASS
![](../images/australia_queens2.jpg)

QGIS, using the GRASS plugin, was selected as it provided the tools needed to complete the job and the interaction between QGIS and GRASS made it easy to process the raster maps and present them in a meaningful way to users. SDRC uses MapInfo for its main GIS system, however MapInfo's addons were not as powerful as GRASS GIS for raster processing.

El plugin GRASS para QGIS se utilizó para importar contornos de 5 metros de toda la región a GRASS que fueron convertidos en un mapa de contornos raster usando r.surf.contour. Luego se generaron un mapa de pendientes y formas usando r.slope.aspect a partir del mapa de contornos raster. Se asignaron categorías a diferentes rangos de pendiente y orientación y se les asigno un valor de riesgo de desastres. A las áreas de vegetación también se les asignaron diferentes escalas de riesgo. Todos los mapas raster resultantes se combinaron luego usando MapCalc y proporcionaron una puntuación final de riesgo. Las puntuaciones de riesgo se dividieron en tres categorías principales: alta; media; y baja.

La parte final del proceso consistió en la verificación en campo a través de los servicios rurales de bomberos. Después del proceso de revisión, QGIS se utilizó para imprimir los mapas finales para su presentación.

Como todos los comandos de GRASS se pueden ejecutar desde la línea de comandos, todos los comandos necesarios para generar el mapa de riesgo de incendio forestal fueron almacenadors con fines de documentación y así poder regenerar los mapas algún momento en el futuro.
## Conclusión
En general, QGIS junto con el complemento de GRASS, proporcionaron una gran experiencia y un gran resultado final para el Consejo al elaborar sus propios mapas de riesgo de incendios forestales. El complemento de GRASS proporciona una interfaz muy sencilla de usar a través de QGIS. Dado que QGIS es capaz de abrir el formato ráster de forma nativa, la integración es muy transparente y los mapas se puede hacer con facilidad.

The project won an encouragement award at the Queensland Planning Institute of Australia state planning awards in 2010 \[2\]
## Referencias
- \[1\] <http://www.emergency.qld.gov.au/publications/spp/>
- \[2\] <http://digital.crowtherblayne.com.au/default.aspx?xml=crowther_pia.xml>

## Autor
<figure>
<img src="../images/australia_queensaut.jpg" class="align-left" height="200" alt="australia_queensaut.jpg" />
<figcaption>Nathan Woodrow</figcaption>
</figure>

Este artículo fue aportado en enero de 2011 por Nathan Woodrow. Nathan es un oficial de SIG en el Consejo Regional de Southern Downs y está estudiando un grado asociado en Ciencia Espacial en la Universidad de Queenslad Souther

{{<content-end >}}
