---
HasBanner: false
draft: false
sidebar: true
title: Hoja de Ruta
type: page

---
{{<content-start >}}
# Hoja de Ruta
{{<roadmap >}}

{{<button class="is-primary1 is-rounded" link="https://qgis.org/schedule.ics" text="Subscribe to the roadmap iCalendar" >}}

Las versiones y el desarrollo de QGIS siguen un calendario basado en el tiempo (hoja de ruta).
- Versiones con números pares (2.18, 3.2, etc) son versiones liberadas.
- Versiones con números impares (2.99, 3.1, etc) son versiones de desarrollo.

Un nuevo lanzamiento ocurrirá cada cuatro meses. En los primeros tres meses, se está produciendo un nuevo desarrollo. En el último mes antes de un lanzamiento, se invoca una congelación de funciones y el último mes se usa para probar, corregir errores, traducir y preparar los lanzamientos. Cuando se produce la versión, se crea una rama con un número de versión par y la rama maestra avanza a la siguiente versión impar. Después del lanzamiento, se emite una solicitud de embalaje.

Cada tercer lanzamiento (empezando con el 2.8) es un lanzamiento con soporte a largo plazo (LTR) que será mantenido hasta que el próximo LTR ocurra.
## Fase de desarrollo
En la fase de desarrollo, los desarrolladores trabajan para agregar nuevas funcionalidades para la próxima versión. Los primeros usuarios pueden usar las compilaciones nocturnas que tenemos para todas las plataformas principales para ver el progreso del desarrollo, hacer pruebas preliminares y proporcionar informes de errores y sus pensamientos para ayudar con el desarrollo.
## Congelamiento de característica
In the feature freeze phase, new features are not allowed in anymore and the focus of everyone moves from enhancing QGIS to stabilizing it. This also turns the nightly builds effectively into [prereleases](#qgis-prereleases).

**Users** should start extensive testing of these prereleases in their environment to verify that there are no issues, they wouldn’t want to see in the upcoming release. All such issues should be reported (see [Bugs, Features and Issues]({{< ref "resources/support/bug-reporting" >}})). Everything that goes unnoticed, will also end up in the next release. Only in case of serious problems backports to a latest release will occur. Therefore testing of the prereleases and reporting issues is very important.

En el congelamiento de funciones, **los desarrolladores** monitorean el rastreador de errores y comienzan a trabajar para solucionar los problemas reportados y actualizan el **registro de cambios visual** con las funciones que agregaron.

Con el inicio de la función de congelación, los archivos de traducción se actualizarán para que los **traductores** puedan comenzar su trabajo. Tenga en cuenta que esto podría ser un proceso incremental ya que aunque las funciones están congeladas, las correcciones de errores aún pueden introducir cambios en la cadena de traducción.

Dos semanas antes del lanzamiento, se inicia una congelación dura después de la cual solo se solucionan los problemas graves y las regresiones introducidas después de que se permite la congelación de funciones.

El lider del lanzamiento anuncia esto en el congelamiento de funciones. 
## Lanzamiento
On major and minor release dates, the release branch is created and the release is tagged and tar balls are prepared. Point releases are just tagged and tar balls are created.

Se notifica a los empaquetadores que pueden comenzar con el empaquetamiento.

Una vez que los paquetes están disponibles el lanzamiento puede ser anunciado y el sitio Web se actualiza como corresponde.
## Cronograma de lanzamiento
El calendario está alineado para producir aproximadamente las mismas fechas para cada año, dadas nuestras cuatro publicaciones mensuales con LTR que entran en el repo de LTR a finales de febrero.

Beginning after 2.12 the development phase is always 12 weeks and the freeze phase is at least 5 weeks. Remainders are used to extend the freeze phase of LTR releases.

Point releases will happen every month on the latest release branch, if there are backports. Beginning with the 3.28 release, point releases are only done with new latest releases.

In the first four months after its release, a new LTR is also the current LR. In this phase, the new LTR doesn’t replace the previous LTR in the LTR repositories. This happens as soon as a new LR is released.

This schedule is also available as [“iCalendar”](https://qgis.org/schedule.ics).
### Cronograma
{{<csv-table file="csv/schedule.csv" >}}
### Leyenda de evento
| Abbreviation | Descripción |
| --- | --- |
| LLD | Lanzamiento de largo plazo, inicio de nueva fase de desarrollo |
| LR | Lanzamiento regular, inicio de nueva fase de desarrollo |
| FF | Congelamiento de característica, fin de la fase de desarrollo |
| PR | Punto de lanzamiento de la última versión y rama LLP |
| EPR | Punto extra de lanzamiento |
| :rm-current:current | :rm-current:currently supported releases: {{< param "ltrrelease" >}} and {{< param "release" >}} |
| :rm-next:next | :rm-next:next releases |

## Ubicación de prelanzamientos / construcciones nocturnas{#qgis-prereleases }
| Plataforma | Ubicación |
| --- | --- |
| Windows | [OSGeo4W]({{< ref "resources/installation-guide#online-osgeo4w-installer" >}}) |
| Linux | [Debian/Ubuntu]({{< ref "resources/installation-guide#repositories" >}}) |

{{<content-end >}}
