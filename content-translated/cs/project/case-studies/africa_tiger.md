---
HasBanner: false
archived: true
date: 2012-06-30
draft: false
featured: false
section: projekt
sidebar: true
thumbnail: images/africa_tiger1.jpg
title: 'Pozorovací a informační systém pro vodu: Umožnění využití dat z pozorování
  Země pro integrované řízení vodních zdrojů v Africe'
type: case-study

---
{{<content-start >}}
# Pozorovací a informační systém pro vodu: Umožnění využití dat z pozorování Země pro integrované řízení vodních zdrojů v Africe
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>June 30, 2012</span>
</p>

The Water Observation and Information System (WOIS) is an open source software tool for monitoring, assessing and inventorying water resources in a cost-effective manner using Earth Observation (EO) data. The WOIS has been developed under the TIGER-NET project, which is a major component of the TIGER initiative of the European Space Agency (ESA) and whose main goal is to support the African Earth observation capacity for water resource monitoring. TIGER-NET aims to support the satellite-based assessment and monitoring of water resources from watershed to cross-border basin levels through the provision of a free and powerful software package, with associated capacity building, to African authorities.
## Popis systému
The WOIS can be seen as a multipurpose system consisting of a spatial database, facilities for extracting and processing EO data, and integrative tools and models aimed at decision support e.g. hydrological modelling and GIS-embedded visualization and analysis tools. The WOIS is designed around QGIS, which acts as the front-end Graphical-User-Interface (GUI). QGIS was chosen as the central integrating platform, due to its clear and accessible GUI, strong development community, ease of implementing additional functionalities through Python plugins and its high level of interoperability with major GIS data formats through the use of the Geospatial Data Abstraction Library (GDAL/OGR) library.

Moreover, the integrated Processing Toolbox, formerly known as SEXTANTE, brings the ability to easily incorporate geoprocessing algorithms from various applications into QGIS. It acts as a joint repository for a wide range of algorithms, some native to QGIS and others imported from external applications, such as GRASS GIS or the Orfeo Toolbox. Support for algorithms from ESA's BEAM, NEST and Sentinel-1 Toolbox software and for setting up and executing SWAT based hydrological models was added to the Processing Toolbox during the WOIS development. The toolbox also allows for easy incorporation of custom R and Python scripts. The inputs and outputs of the Processing Toolbox algorithms can be evaluated with the QGIS capabilities of data I/O, rendering or map creation.

Klíčovou výhodou sady Processing Toolbox je možnost bezproblémového využití funkcí od různých poskytovatelů algoritmů pro zpracování a analýzu dat. Toho lze využít k vytváření automatických modelů zpracování a prostřednictvím zásuvného modulu QGIS vyvinutého v rámci projektu TIGER-NET k postupnému spojování algoritmů od různých poskytovatelů do zpracovatelských řetězců založených na průvodci. Tato funkce byla využita k vytvoření knihovny standardizovaných pracovních postupů (s návody) pro provádění běžných, ale složitých úloh souvisejících s analýzou dat EO v rámci řízení vodních zdrojů.

<figure>
<img src="../images/africa_tiger1.jpg" class="align-center" style="width:100.0%" alt="africa_tiger1.jpg" />
<figcaption>The WOIS graphical user interface, including the embedded workflow library (center) and wizard-based processing workflow (right)</figcaption>
</figure>

Provozní a praktické využití systému WOIS na podporu integrovaného řízení vodních zdrojů v Africe bylo demonstrováno na řadě demonstračních případů pro konkrétní uživatele, které se týkají široké škály témat a informačních produktů. Patří mezi ně: kvalita vody v jezerech, monitorování povodní, charakterizace degradace půdy a půdního pokryvu, mapování vodních útvarů a hydrologické modelování. Demonstrační případy mají několik fází. Nejprve jsou pro požadované produkty a aplikace vyvinuty přizpůsobené pracovní postupy komplexního zpracování. Tyto pracovní postupy jsou následně použity pro odvození produktů ve významných oblastech a časových obdobích podle požadavků uživatelů. V posledním kroku se v úzkém dialogu s uživateli vyhodnocují pracovní postupy (tj. jejich stabilita/výkonnost a snadnost použití) a také výsledky produktů.

<figure>
<img src="../images/africa_tiger2.jpg" class="align-center" style="width:100.0%" alt="africa_tiger2.jpg" />
<figcaption>Sentinel-1 flood monitoring of Caprivi flood plain, Namibia.</figcaption>
</figure>

## Závěr
Vývoj systému WOIS představuje úspěšný příklad modelu vývoje založeného na spolupráci a řízeného uživateli, kdy byly funkce navrženy, vyvinuty a vyhodnoceny na základě případů určených uživateli s cílem prokázat skutečný dopad systému na zlepšení vodního hospodářství a integrovaných plánů hospodaření s vodními zdroji. Systém WOIS je již implementován v hlavních afrických povodí, na několika afrických ministerstvech a agenturách a také ve výzkumných a humanitárních organizacích. Bude se proto nadále vyvíjet v reakci na neustálé požadavky uživatelů na nové funkce a funkční vylepšení a díky obecným vylepšením softwaru, algoritmů a metod.

Zvláštní pozornost bude věnována zajištění podpory a implementaci zpracovatelské kapacity pro nový družicový systém Sentinel prostřednictvím integrace sad nástrojů ESA Sentinel do systému WOIS a vývoje specializovaných výrobních pracovních postupů. Příští verze systému WOIS (která má být vydána v druhé polovině dubna 2015) již bude obsahovat sadu nástrojů Sentinel-1 a řadu pracovních postupů využívajících tuto novou radarovou datovou sadu pro monitorování povodní, mapování vodních ploch atd. Tím se systém WOIS stane plně funkčním monitorovacím systémem. Poskytnutím tohoto bezlicenčního, výkonného a rozšiřitelného systému a díky pokračujícímu úsilí o budování kapacit a školení se projektu daří budovat základ pro rozšíření, tj. rozšíření do dalších zemí a regionů v Africe i mimo ni.
## Reference
- Bauer-Gottwein, P., Jensen, I. H., Guzinski, R., Bredtoft, G. K. T., Hansen, S., & Michailovsky, C. I. (2015). Operativní předpověď říčního odtoku ve špatně měřených povodích: případová studie povodí řeky Kavango. Hydrology and Earth System Sciences, 19(3), 1469-1485.
- Guzinski, R.; Kass, S.; Huber, S.; Bauer-Gottwein, P.; Jensen, I.H.; Naeimi, V.; Doubkova, M.; Walli, A.; Tottrup, C. Enabling the Use of Earth Observation Data for Integrated Water Resource Management in Africa with the Water Observation and Information System. Remote Sens. 2014, 6, 7819-7839.
- Walli, A., Tottrup, C., Naeimi, V., Bauer-Gottwein, P., Bila, M., Mufeti, P., Tumbulto, J.W., Rajah, C., Moloele, L.S. & Koetz, B. "TIGER-NET---Enabling an earth observation capacity for integrated water resource management in Africa," presented at the ESA Living Planet Symp., Edinburgh, U.K., Sep. 11--13, 2013.

## Odkazy
- More information about the WOIS software and the TIGER-NET project can be found on the project's website: www.tiger-net.org
- More information about ESA's TIGER initiative can be found on the initiative's website: <http://www.tiger.esa.int/> WOIS is available for download (after registration) from the TIGER website (<http://www.tiger.esa.int/page_eoservices_wois.php>) with source code of the developed plugins, scripts, models and workflows available from the project's GitHub page (<https://github.com/TIGER-NET>)
- More information about the new Sentinel satellites can be found on ESA's website: <http://www.esa.int/Our_Activities/Observing_the_Earth/Copernicus/Overview4>

### Autor
This article was contributed by Radoslaw Guzinski (WOIS software developer) with contributions from the TIGER-NET technical teams at DHI-GRAS (www.dhi-gras.com), GeoVille (www.geoville.com), the technical universities in Vienna (<http://rs.geo.tuwien.ac.at/>) and Copenhagen (<http://www.env.dtu.dk/>) as well as the European Space Agency ( www.esa.int).

{{<content-end >}}
