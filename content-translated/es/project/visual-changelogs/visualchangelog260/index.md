---
HasBanner: false
draft: false
releaseDate: '2014-10-31'
section: proyecto
sidebar: true
title: Registro de cambios para QGIS 2.6
type: visual-changelog

---
{{<content-start >}}
# Registro de cambios para QGIS 2.6{#changelog26 }
Fecha de lanzamiento: 2014-10-31

Registo de cambio para el siguiente lanzamiento de QGIS 2.6.0. Hemos adicionado muchas características nuevas, ajustes y mejoras para que el SIG Libre de escritorio más popular esté aún más lleno de característica y utilidad.

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

Nos gustaría agradecer a los desarrolladores, documentadores, probadores y a las muchas personas que ofrecen su tiempo y esfuerzo voluntario (o financian a personas que lo hacen).

From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

Finalmente nos gustaría agradecer a nuestros patrocinadores oficiales por el soporte financiero invalorable que proveen a este proyecto:
- **GOLD Sponsor: Asia Air Survey, Japan** <http://www.asiaairsurvey.com/>
- SILVER Sponsor: [Sourcepole AG, Switzerland](http://www.sourcepole.com/)
- SILVER Sponsor: [State of Vorarlberg, Austria](http://www.vorarlberg.at/)
- BRONZE Sponsor: [Lutra Consulting, UK](http://www.lutraconsulting.co.uk/)
- BRONZE Sponsor: [www.molitec.it, Italy](http://www.molitec.it/)
- BRONZE Sponsor: [www.argusoft.de, Germany](http://www.argusoft.de)
- BRONZE Sponsor: [www.openrunner.com, France](http://www.openrunner.com)
- BRONZE Sponsor: [GKG Kassel,(Dr.-Ing. Claas Leiner), Germany](http://www.eschenlaub.de/)

A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become an official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts.

If you enjoy using QGIS, please consider making a donation to support the project - either [financial](https://qgis.org/en/site/getinvolved/donations.html) or of [your time and skills](https://qgis.org/en/site/getinvolved/index.html)! Lastly we would like to also take a moment to encourage you to fund a [special campaign](http://blog.vitu.ch/10102014-1046/crowdfunding-initiative-automated-testing) by one of our QGIS developers to get a working test suite for QGIS so that we can improve out quality assurance process and deliver you the best possible releases.

QGIS es software gratuito y no tiene la obligación de pagar nada por usarlo; de hecho, queremos alentar a las personas a utilizarlo independientemente de su estado financiero o social, creemos que empoderar a las personas con herramientas de toma de decisiones espaciales dar como resultado una sociedad mejor para toda la humanidad.

{{<table-of-contents >}}
## General
### Característica: Nombre de archivo de proyecto en propiedades
Ahora puede ver la ruta completa para el archivo proyecto QGIS en el diálogo de propiedades del proyecto.

![](images/entries/8662dc4a69298f603dd9038d1199ab16fd25f786.webp)
### Prestación: Permitir eliminar el último punto mientras se mide a través de las teclas del/retroceso
Ahora cuando mides áreas y distancias, puedes eliminar vértices no deseados de tu línea de medición usando las teclas borrar o borrar hacia atrás.

![](images/entries/ed471908937cb068e2f004e7b3311f2bdf307042.webp)
### Prestación: seleccione la entidad relacionada en el lienzo desde el widget de referencia de relación
### Característica: Widgets de editor
Hemos hecho varias mejoras a los widgets del editor:
- nuevo widget de edición para fecha/hora capaz de establecer fechas nulas
- filtrar edición de línea
- Manejo propio de valores NULL para controles gráficos (widgets) de edición
- Widget foto preserva valor NULO
- Widget web preserva valor NULO
- Tabla de atributo puede distinguir entre 0 y NULO
- Adiciona soporte de sufijo para widget rango

![](images/entries/78fd27b2cf736f37bdf97694a5018f29c609c6cb.webp)
### Característica: Opcionalmente use solamente un subconjunto de campos de la capa unida (join)
Ahora puede usar un subconjunto de campos relacionados cuando crea una unión vector.

![](images/entries/14023cf2ee768960d9c4a43da6e2a1624d10b3c3.webp)
### Característica: campo Expresión (campos virtuales)
Sometimes you want to have an attribute that is calculated and that is always \'fresh\' - reflecting the current state of the feature properties. Now you can add virtual fields to your table which are based on an expression.

![](images/entries/5fe53ad54b8d0cf8b7a22b90e733a421bb929506.webp)
### Característica: Ahora las acciones pueden tener un ícono asociado
Cuando cree una acción personalizada para una capa vector, ahora puede definir un ícono a ser usado también por la acción.

![](images/entries/e7bd5b306e3a72cc111a81f86a053b42679aa2f8.webp)
### Característica: Tipos y opciones adicionales de expresiones
- Allow using `+` for string concatenation.
- New keyword: `attribute( feature, attribute_name )` - gets the specified attribute from a feature.
- New keyword: `$currentfeature` - returns the current feature.
- New keyword: `$atlasfeature` - returns the atlas feature.
- New keyword: `getFeature` - gets a matching feature from a layer.

![](images/entries/e2e079bec87be65ccc97055251fc2544be91aaab.webp)
### Prestación: las clases en representaciones graduadas y categorizadas se pueden alternar
Ahora puede optar por deshabilitar ciertas clases en representaciones graduadas y categorizadas sin eliminarlas realmente.

![](images/entries/84d11c6d978775d92f6a1902092795735d1f32b3.webp)
### Característica: Mejoras de leyenda
La segunda fase de la revisión de la leyenda / tabla de contenidos se ha completado. Esto incluye:
- Limpieza de API (para desarrolladores)
- Grupos de visibilidad de las capas del mapa en el árbol de capas. Este nuevo botón de la barra de herramientas permite cambios rápidos entre los grupos de capas que deberían estar visibles.
- Abilidad para manejar grupos de capas desde la barra de herramientas de la leyenda
- La nueva opción de filtro de leyenda en la barra de herramientas de leyenda eliminará los elementos de leyenda para cualquier clase que no esté actualmente en la extensión de la vista. Esta es una mejora impresionante, ya que garantiza que la leyenda del mapa no contenga entradas para elementos que no están actualmente en la vista del mapa. Está disponible en la leyenda del mapa principal y en el compositor de mapas y para las capas WMS.
- Las leyendas basadas en reglas del renderizador pueden ahora desplegarse en un pseudo-árbol

![](images/entries/363048a7d08ac76d35463abbef514c65031922e7.webp)
## Proveedores de datos
### Prestación: Mejoras en exportación DXF
- vista árbol y selección de atributo para asignación de capa en diálogo
- apoyo de llenado a polígonos/HATCH
- representar textos como MTEXT en vez de TEXT (incluyendo tipo de letra, inclinación y peso)
- support for RGB colors when there\'s no exact color match
- use AutoCAD 2000 DXF (R15) en vez de R12
- elimine los métodos de prueba R18

![](images/entries/4f615505e3fd6ec0b619278e42ecc5a3e79ac827.webp)
## Compositor de Mapa
### Característica: Control sobre ocultar elementos del diseñador de impresión de impresiones/exportaciones
Hemos agregado una casilla de verificación y un botón de datos definidos para controlar si un artículo está excluido de las exportaciones/impresiones del compositor. Si el elemento no está marcado, será visible solo en el momento del diseño de la composición.

![](images/entries/f334447d13ee49a6c4c5cb4322e3f12824643416.webp)
### Característica: Control sobre la impresión de página para los marcos vacíos del diseñador
Para marcos de tabla o HTML, una casilla de verificación ahora controla si la página que los contiene debería ser exportada cuando el marco está vacío.

![](images/entries/1500ba6abdf5b314c760ebfc63e460731dcc5110.webp)
### Característica: Panel de árbol de elementos
El panel del árbol de elementos en el compositor de mapas permite la selección de elementos, ocultar/mostrar elementos, alternar el estado de bloqueo de los elementos y hacer doble clic para editar la identificación del elemento. También puede usar arrastrar y soltar para reordenar elementos.

![](images/entries/52b70bdf87d21a13c00798458bab6347dddd7910.webp)
### Característica: Más control sobre la apariencia de elementos flecha/línea del diseñador
- Las líneas pueden recibir estilo usando el díalogo de estilo del símbolo de línea
- Los colores de relleno y borde de la punta de lanza pueden ser definidos por el usuario 
- El ancho del contorno de la cabeza de flecha puede ser definido por el usuario

![](images/entries/49757b3cc09839edb8af38f1cb1317458f279110.webp)
### Característica: Control de elementos del diseñador definido por datos
Muchas propiedades de elementos del diseñador pueden ahora ser controladas usando enlace de datos. Estas incluyen:
- Modo transparencia y mezcla.
- Rotación de elemento.
- Escala, extensiones y rotación de mapa.
- Margen de la entidad atlas.
- Tamaño y posición de elemento.
- Tamaño y orientación de página y número de páginas.

![](images/entries/9f321489cd9c90eb4d66e577680fc5467756e58e.webp)
### Característica: Imágenes del diseñador pueden ser especificadas como URLs remotos
Los elementos de imagen en el compositor de mapas ahora admiten URL remotas como fuente de imagen. Esta fuente también puede ser datos definidos.

![](images/entries/05cd7008c231df3b3af874753b840669a605cb0f.webp)
### Característica: Mejoras en tabla del diseñador
- Ahora puede definir un encabezado de tabla y colores de fuente del contenido.
- Las tablas ahora pueden partirse en múltiples marcos, permitiendo que su contenido sea distribuido a lo largo de columnas o a lo largo de diferentes páginas.
- Opción adicionada muestra encabezados en primer marco, todos los marcos, o ningún marco.
- Permite el control manual del ancho de columnas.
- Nuevas opciones para el origen de la tabla, incluida la entidad de atlas actual y las entidades secundarias de una relación.
- La elección del comportamiento para tablas vacías, incluye ocultar toda la tabla, mostrar celdas vacías o mostrar un mensaje establecido en el cuerpo de la tabla.
- Se agregó una casilla de verificación para filtrar las características de la tabla a aquellas que se cruzan con la entidad del atlas actual.
- Adicionada caja de confirmación (checkbox) para eliminar filas duplicada de tabla

Tenga en cuenta que las tablas en proyectos existentes no se actualizan automáticamente al nuevo formato de tabla que admite estas características, y las tablas deben leerse en una composición para que aparezcan las nuevas configuraciones.

![](images/entries/9ccb75b2110daf0c95a3fba31ac18144c1345f0e.webp)
### Característica: Mejoras del Diseñador
El diseñador de mapa (usado para preparar composiciones imprimibles de mapa) ha recibido varias mejoras en QGIS 2.6.
- Ahora puede cambiar el color de relleno secundario para las barras de escala
- Mantener presionada la tecla <kbd>Shift</kbd> mientras dibuja elementos de línea/flecha restringe el dibujo a ángulos horizontales, verticales o de 45 grados
- Mantiendo presionada la tecla shift mientras se dibujan otros elementos nuevos los restringen a cuadrados, manteniendo presionada alt causa que el elemento sea dibujado desde el centro
- El clic derecho ya no bloquea/desbloquea elementos, esto ahora lo maneja el nuevo panel de elementos. Los elementos bloqueados ya no se pueden seleccionar desde el lienzo del compositor, lo que permite la interacción con los elementos debajo de ellos.
- Manteniendo presionado alt mientras se presiona las teclas de cursos resulta en un movimiento de 1px para los elementos
- Removed the destructive \'Load from template\' menu item, replace with a new non-destructive \'Add items from template\' action

![](images/entries/a7267ed637121bc9be70c5fa0afd2a63f9790bc7.webp)
### Característica: Ajuste mejorado de elemento
Los umbrales de ajuste ahora se establecen en píxeles, lo que permite un movimiento más fino y cambiar el tamaño de los elementos cuando se acerca a una composición. Los elementos dentro de un grupo ya no se usan para líneas automáticas.

![](images/entries/8e43479380c28942345f3d9500dd956bd13f43e8.webp)
### Característica: Múltiples sobrevistas para un elemento de mapa
Sometimes it is useful to be able to show more than one overview frame for a map frame. For example if you want to show where your map is in local, regional and global context, using multiple overview maps can help you to achieve this. As of QGIS 2.6 you can now achieve this by assigning as many maps as you like to the \'overview\' role in your composition.

![](images/entries/88b55cc5f5e7cfb62486fe3b4867b7133ae66953.webp)
### Característica: Mejoras elemento HTML
Exsite un cantidad de nuevas opciones útiles para el elemento HTML del diseñador:
- Opción para el ingreso manual de código HTML
- expresiones QGIS dentro de fuente HTML pueden ser evaluadas antes de la visualización de contenido HTML
- URL definido por datos para fuente HTML
- Permite la creación de una stylesheet de usuario para ignorar estilos HTML

![](images/entries/7ed388f0c775b738648b2bd6eb6be0a75fa5816a.webp)
### Característica: Mejoras en cuadrícula de diseñador de mapa
- Ahora puede tener múltiples cuadrículas con diferentes propiedades.
- Puede mezclar cuadrículas reproyectadas y cuadrículas Lat/Long.
- Puede usar simbología de líneas de cuadrícula estándar de QGIS etc.
- Hay un nuevo marco/anotaciones estilo de solo cuadrícula. Al seleccionar este estilo, solo se dibujan el marco y las anotaciones, sin líneas de cuadrícula u otras marcas sobre el mapa.
- Ahora existen opciones para controlar en cuál lado de un elemento de mapa  se dibuja el marco.
- Hay nuevos estilos de tick para marcos, con ticks internos, ticks externos y opciones de ticks internos y externos.
- Hemos hecho mejoras a anotaciones de cuadrícula, incluyendo muchos formatos nuevos de anotaciones.
- Las anotaciones de cuadrícula ahora usan los símbolos primo y doble primo tipográficamente correctos para las anotaciones de cuadrícula.

![](images/entries/eeb61d7da3d3f95283b1bb47545cbdff9cc334ae.webp)
## Procesado
### Característica: Colección en-línea de modelos y scripts
Los modelos y scripts se pueden descargar de la colección en línea e instalar directamente desde la interfaz de procesamiento. La colección se ampliará con nuevos scripts y modelos proporcionados por los usuarios de Processing.

![](images/entries/23e357ca0e559a33a7872206b306c0b1fbdb4b7d.webp)
### Característica: Nueva implementación del modelador
El modelador se ha reescrito y ahora proporciona una funcionalidad adicional, como permitir modelos anidados sin límite de profundidad. Los modelos ahora se almacenan como archivos JSON. Se mantiene la compatibilidad con versiones anteriores, por lo que todos los modelos se pueden seguir utilizando. Ahora también puede arrastrar y soltar elementos de las entradas y algoritmos en el gráfico del modelador.

![](images/entries/72bb8beaf97133424d1e68da67ae6fe79ea6faf6.webp)
## Programabilidad
### Característica: Cambios API para widgets QGIS
In order to normalise the naming of QGIS widgets, some minor API changes have been made. Almost all edit widgets were renamed by adding \"Wrapper\" at the end of their names. In particular this concerns:
- QgsCheckboxWidget -\> QgsCheckboxWidgetWrapper
- QgsClassificationWidget -\> QgsClassificationWidgetWrapper
- QgsColorWidget -\> QgsColorWidgetWrapper
- QgsEnumerationWidget -\> QgsEnumerationWidgetWrapper
- QgsFilenameWidget -\> QgsFilenameWidgetWrapper
- QgsHiddenWidget -\> QgsHiddenWidgetWrapper
- QgsPhotoWidget -\> QgsPhotoWidgetWrapper
- QgsRangeWidget -\> QgsRangeWidgetWrapper
- QgsTexteditWidget -\> QgsTexteditWrapper
- QgsUniquevalueWidget -\> QgsUniquevalueWidgetWrapper
- QgsUuidWidget -\> QgsUuidWidgetWrapper
- QgsValuemapWidget -\> QgsValuemapWidgetWrapper
- QgsValuerelationWidget -\> QgsValuerelationWidgetWrapper
- QgsWebviewWidget -\> QgsWebviewWidgetWrapper

## Servidor de QGIS
### Característica: Mejoras para buscar con el pedido GetFeatureInfo
<https://github.com/qgis/QGIS/commit/8888c5f0c0e0ffdf23453a20addf6abaf125845d>
### Característica: Adiciona configuración de precisión para atributos de geometría GetFeatureInfo
## Simbología
### Característica: Mejor elección de color aleatorio
Hemos mejorado el algoritmo de color aleatorio para el renderizador clasificado para que los colores generados sean visualmente más distintos entre sí.

![](images/entries/ec29c9d6eb23d01b4dbbae32a6e20fe0b1f48198.webp)
### Característica: Mejoras en interfaz de usuario de simbología
- Cuando es posible, las propiedades de la capa símbolo son mantenidas cuando se cambia el tipo de capa símbolo.
- Se agregó un botón de edición para rampas de color de degradado y forma
- Actualización automática de etiquetas y límites de rangos vecinos.
- Las clases se convierten automáticamente de clases categorizadas y graduadas cuando se cambia al renderizador basado en reglas.
- Se adicionaron unidades y número de lugares decimales a etiquetas del visualizador graduado.
- Mayor capacidad de respuesta a los cambios en la rampa de color, la rampa de color invertida y otras opciones en la GUI.
- Mantener símbolo cuando cambien entre simple, graduado, categorizado, y otros visualizadores.
- Etiquetado mejorado del modo de cálculo de desviación estándar.

![](images/entries/08305d5131c28c45b400662267ff0d174ef9c8ce.webp)
## Interfaz de usuario
### Característica: Editor de código con resaltado de sintaxis
Para python editores script, constructor de expresión, ventana filtro, compositor HTML y editores CSS

![](images/entries/54b470a064d65d6d65aa66a8feece43ba8cbf6c4.webp)
### Característica: Paletas de color
Ahora puede definir sus propias paletas personalizadas para usarse en QGIS.
- Paleta de color global del usuario personalizada (en díalogo de opciones).
- Paleta de color por proyecto (en el diálogo de propiedades de proyecto).
- Los colores son mostrados en menus botón color y nuevo diálogo seleccionador de color.
- Puede importar/exportar colores a un archivo paleta GPL.

![](images/entries/a156f408d7a87fc930095c8fd68e9fba0fc0a817.webp)
### Característica: Nuevo díalogo para escoger color
Existe un nuevo diálogo personalizado que selecciona color QGIS. Las características incluyen:
: - Desplazador para componentes color matiz, saturación, valor, rojo, verde.
  - Deslizador Alfa.
  - Opción para copiar/pegar códigos color html (en una variedad de formatos).
  - Antes/después de previsión de color, con previsión alfa.
  - Widget interactivo para rampa de color 2D.
  - Widget rueda/triángulo de matiz.
  - Paletas de colores editables, incluida la capacidad de crear nuevas paletas e importar/exportar colores a un archivo de paleta GPL.
  - Muestra de color en vivo con opción para muestrear en un radio establecido (depende del soporte del sistema operativo).
  - Admite la interacción con otras aplicaciones mediante arrastrar y soltar colores (depende del soporte del sistema operativo).
  - Opción para desabilitar el diálogo y en vez usar el diálogo nativo de selección.

![](images/entries/7189c0fe2d1ff3fdc63c531a02f74b5d32b70bfd.webp)
### Característica: Herramienta de selección de rasgos fusionada en seleccionar con rectángulo
Hemos fusionado la herramienta de selección única en la herramienta de rectángulo. Si desea seleccionar una característica única, simplemente habilite la herramienta de rectángulo y luego haga clic en una entidad (en lugar de arrastrar un rectángulo).

![](images/entries/f8a68fcdfcaa59e6162185acb5c92edb9145c881.webp)
### Característica: Adicionar capa a comportamiento de tela de mapa 
In many of QGIS\' dialogs that generate a new layer, the \'Add layer to map canvas\' checkbox is now checked by default so that the new layer automatically gets added to the map.

![](images/entries/f36f5912d2422a439d67b1a743fe81588e709dfb.webp)
### Característica: Adicionar ícono tamaño 48 y 64
Para aquellos que usan QGIS en dispositivos táctiles (o si simplemente les gustan los iconos grandes y gruesos), ahora pueden configurar los iconos con un tamaño de hasta 64 x 64 píxeles.

![](images/entries/3be3f51da2f54a8395f054f757f9fae1948a6103.webp)
### Característica: Nuevos botones de color
This is probably one of the most useful new features in QGIS 2.6 -especially if you are involved a lot in cartography work. The colour button used everywhere in QGIS has been enhanced, with drop down menus, colour swatches, default colours, etc. Click on the drop down item to the right of the colour button to see the quick options. Click on the button to the left of the colour widget to see a standard colour chooser dialog.

![](images/entries/54c211513bc86d00a5bce01a17476481937e0fbe.webp)
### Característica: Menú de contexto para la herramienta identificar
Al usar la herramienta de identificación, ahora puede hacer clic derecho en el lienzo para usar la herramienta de identificación en modo contextual. En el menú que aparece, puede definir qué tipos de características desea identificar (todas, si lo desea).

![](images/entries/c395c2ce4964826458a721a8a3f89cb7dc2853b5.webp)

{{<content-end >}}
