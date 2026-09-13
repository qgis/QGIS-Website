---
HasBanner: false
archived: true
date: 2015-10-30
draft: false
featured: false
section: proyecto
sidebar: true
thumbnail: images/italy_cesena1.png
title: QGIS para describir la Muralla de Cesena.
type: case-study

---
{{<content-start >}}
# QGIS to describe the Cesena\'s Wall
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>October 30, 2015</span>
</p>

La Universidad ECAMPUS fue creada como una Universidad online y reconocida por el MIUR (Ministerio Italiano de Educación, Universidad e Investigación) por el Decreto Ministerial del 30 de Enero de 2006. Fue formada con el objetivo de proporcionar acceso a la universidad mediante su plataforma de eLearning a la gente joven, profesoinales, empresarios, ejecutivos y actores culturales para contribuir al mercado laboral. La Sede, tambien conocida como Campus Internacional de Milan, o Campus de Novredate, está ubicado en el excentro de entrenaiento de IBM de Novedrate (Como, Italia), en un campus en la bastante verde Brianza.

La universidad tiene 5 facultades Virtuales: Ingeniería, Economicas, Psicología, Artes, Leyes. Los mapas históricos y el proyecto de QGIS The Citty Wall caracteriza la ciudad de Cesena. Su forma de escorpión separa el centro histórico de la zona nueva.

Los documentos cartográficos históricos describen su evolución y su destrucción. El programa QGIS permite comparar diferentes mapas históricos, porque permite transferir todos los mapas al mismo Sistema de Referencia, con el complemento de georreferenciado. Como referencias la capa abierta del Satélite de Google y la capa abierta de Open Street Map fueron usadas para referenciar todos los mapas históricos al Sistema de Referencia EPSG: 3857 (WEB Mercator o Pseudo Mercator).

QGIS ha sido una herramienta fundamental para elaborar, analizar, comparar esos mapas georreferenciados mediante capas vectoriales o shapefiles, en los cuales he guardado todos los elementos de los mapas, como carreteras, edificios, parques y jardines. City Wall, las antiguas torres fortificadas y las antiguas Puertas de la Ciudad. Usé capas de puntos, lineales y poligonales. Comparé estas capas mediante herramientas de análisis, investigación, geoprocesado, geometricas y administración de datos. (Fig. 1).

<figure>
<img src="../images/italy_cesena1.png" style="width:100.0%" alt="italy_cesena1.png" />
<figcaption>Fig. 1 Concept Map of the QGIS project</figcaption>
</figure>

Usando esta herramienta, obtuve información sobre:
- The precision of the Leonardo Da Vinci\'s topographic survey, realized in 1502, such as how many points of this survey are correct (Fig. 2);
- The Cesena Wall\'s Development from the Roman Age to the 15th Century;
- The Cesena Wall\'s Demolitions from the 19th Century to the Early 20th Century;
- Los cambios morfológicos de la Muralla de la Ciudad, así como los derrumbamientos de las antiguas torres fortificadas y las Puertas de su Ciudad;
- The Cesena\'s Urban Progress from the 16th Century to the Present;

<figure>
<img src="../images/italy_cesena2.png" style="width:100.0%" alt="italy_cesena2.png" />
<figcaption>Fig. 2: Openlayer Google Satellite overlapped by the informations recorded in different layers: the present City Wall in black, the Leonardo Da Vinci's topographic survey of the City Wall in orange, the Leonardo Da Vinci's points of survey in yellow and the present ancient City Gates in red.</figcaption>
</figure>

Hay numerosas herramientas de QGIS, y he empleado algunas para crear:
- links que conectan cada sección de la capa lineal de la Muralla de la Ciudad a fotografías, las cuales muestran el estado actual de conservación;
- Un mapa de Cesena en el Siglo 19 mediante el compositor de impresión;
- Un modelo 3D de Cesena con el complemento qgis2threejs (Fig. 3);

<figure>
<img src="../images/italy_cesena3.png" style="width:100.0%" alt="italy_cesena3.png" />
<figcaption>Fig. 3: The 3D model of the present City Wall and Cesena's buildings inside and outside the Wall. The ancient fortified towers and the ancient City Gates are indicated.</figcaption>
</figure>

## Conclusión
Los mapas históricos son documentos importantes incluso si su precisión no es comparable con la precisión de los documentos cartográficos actuales, y son representaciones muy comunicativas incluso para aquellos no especializados en representaciones geográficas. QGIS fue el único medio que me permitió usar el contenido numérico de los mapas históricos junto a una representación efectiva y significativa.
## Índice bibliográfico
Los mapas históricos han sido extraidos de:
- \"Costruzione, alterazione e recupero del centro storico di Cesena\", Ballardini, Cantori, Pezzi, Righetti, Tossani, Bruno Ghigi Editore, 1977
- \"La cinta muraria di Cesena\", Pino Montalti, Edizioni Panini, 1986

Las informaciones históricas han sido extraidas de:
- \"La cartografia in Italia: nuovi metodi e nuovi strumenti dal Settecento ad Oggi\", Andrea Cantile, IGM Firenze, 2007
- \"Lineamenti di storia della cartografia italiana, volume secondo, dal Seicento al Novecento\" Andrea Cantile, Geoweb, 2013
- \"I rilievi cartografici di Leonardo per Cesena ed Urbino contenuti nel manoscritto \'L\' dell\'Istituto di Francia\", Nando De Toni, G. Barbéra Editore, 1965
- \"La città da guerra\", Amelio Fara, Einaudi, 1993
- \"La cartografia dall\'antichità fino al XVIII secolo\", Carlo Monti, Maggioli Editore, 2011

## Autor
Camilla Fabbri has a bachelor\'s degree in Civil and Environmental Engineering. She has developed her dissertation on historical cartography of the Cesena Wall using the QGIS program with the Supervisor Alessandra Borghi, who is the University Teacher of Topography and Theoretical Mechanics of the bachelor\'s degree in Civil and Environmental Engineering in the eCampus University.

{{<content-end >}}
