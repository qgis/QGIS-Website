---
HasBanner: false
archived: true
date: 2012-06-30
draft: false
featured: false
section: projektą
sidebar: true
thumbnail: images/africa_tiger1.jpg
title: 'Vandens stebėjimo informacijos sistema: žemės stebėjimo duomenų naudojimas
  integruotame vandens resursų valdyme afrikoje'
type: case-study

---
{{<content-start >}}
# Vandens stebėjimo informacijos sistema: žemės stebėjimo duomenų naudojimas integruotame vandens resursų valdyme afrikoje
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>June 30, 2012</span>
</p>

The Water Observation and Information System (WOIS) is an open source software tool for monitoring, assessing and inventorying water resources in a cost-effective manner using Earth Observation (EO) data. The WOIS has been developed under the TIGER-NET project, which is a major component of the TIGER initiative of the European Space Agency (ESA) and whose main goal is to support the African Earth observation capacity for water resource monitoring. TIGER-NET aims to support the satellite-based assessment and monitoring of water resources from watershed to cross-border basin levels through the provision of a free and powerful software package, with associated capacity building, to African authorities.
## Sistemos aprašymas
The WOIS can be seen as a multipurpose system consisting of a spatial database, facilities for extracting and processing EO data, and integrative tools and models aimed at decision support e.g. hydrological modelling and GIS-embedded visualization and analysis tools. The WOIS is designed around QGIS, which acts as the front-end Graphical-User-Interface (GUI). QGIS was chosen as the central integrating platform, due to its clear and accessible GUI, strong development community, ease of implementing additional functionalities through Python plugins and its high level of interoperability with major GIS data formats through the use of the Geospatial Data Abstraction Library (GDAL/OGR) library.

Moreover, the integrated Processing Toolbox, formerly known as SEXTANTE, brings the ability to easily incorporate geoprocessing algorithms from various applications into QGIS. It acts as a joint repository for a wide range of algorithms, some native to QGIS and others imported from external applications, such as GRASS GIS or the Orfeo Toolbox. Support for algorithms from ESA's BEAM, NEST and Sentinel-1 Toolbox software and for setting up and executing SWAT based hydrological models was added to the Processing Toolbox during the WOIS development. The toolbox also allows for easy incorporation of custom R and Python scripts. The inputs and outputs of the Processing Toolbox algorithms can be evaluated with the QGIS capabilities of data I/O, rendering or map creation.

Pagrindinis apdorojimo įrankinės pranašumas yra galimybė be papildomų sunkumų naudoti skirtingų algoritmų tiekėjų funkcionalumą duomenų apdorojimui ir analizei. Tai gali būti panaudota kuriant automatinius apdorojimo modelius ir per QGIS priedą, sukurtą TIGER-NET projekte, kombinuoti algoritmus iš skirtingų tiekėjų į vedlio tipo apdorojimo sekas. Šis funkcionalumas buvo panaudotas kuriant standartizuotų darbo eigų biblioteką (su instrukcijomis), skirtą vykdyti bendras bet sudėtingas užduotis, susijusias su EO duomenų analizę vandens resursų valdyme.

<figure>
<img src="../images/africa_tiger1.jpg" class="align-center" style="width:100.0%" alt="africa_tiger1.jpg" />
<figcaption>The WOIS graphical user interface, including the embedded workflow library (center) and wizard-based processing workflow (right)</figcaption>
</figure>

Veiklos ir praktinis WOIS naudojimas integruotam vandens resursų valdymui Afrikoje buvo pademonstruotas eilėje konkrečių naudotojų demonstracijomis su įvairiomis temomis ir informaciniais produktais. Tarp jų: ežerų vandens kokybės, potvynių stebėjimo, žemės degradacijos ir žemėnaudos charakteristikos, vandens telkinių žymėjimas ir hidrologinis modeliavimas. Demonstracijos turi kelis etapus. Visų pirma reikiamiems produktams ir aplikacijoms sukuriamos savos nuo-iki apdorojimo darbų sekos. Šios sekos vėliau naudojamos produkto išvedimui į didelius ploto ir laiko periodus pagal naudotojų užklausas. Paskutiniame žingsnyje darbų eigos (pvz. jų stabilumo/našumo ir naudojimo paprastumo) ir produkto rezultatai įvertinami artimo dialogo su naudotojais metu.

<figure>
<img src="../images/africa_tiger2.jpg" class="align-center" style="width:100.0%" alt="africa_tiger2.jpg" />
<figcaption>Sentinel-1 flood monitoring of Caprivi flood plain, Namibia.</figcaption>
</figure>

## Išvada
WOIS kūrimas - puikus naudotojų valdomo bendradarbiavimo modelio pavyzdys, kur funkcionalumas buvo suprojektuotas, sukurtas ir įvertintas naudojant naudotojų sukurtus naudojimo atvejus, kad būtų galima parodyti tikrą sistemos įtaką gerinant vandens valdymo ir integruotų vandens resursų valdymo planus. WOIS jau įdiegta pagrindinių Afrikos vandens baseinų valdžios įstaigose, keliose Afrikos ministerijose ir agentūrose, o taipogi ir tyrimo ir humanitarinėse organizacijose. Todėl sistema ir toliau bus vystoma atsižvelgiant į naudotojų naujo funkcionalumo pridėjimo ir esamo tobulinimo poreikius ir siekiant bendro programinės įrangos, algoritmų ir metodų gerinimo.

Ypatingas dėmesys bus skiriamas užtikrinant naujo Sentinel palydovo sistemos apdorojimo galimybių diegimui ir palaikymui integruojant ESA Sentinel įrankines į WOIS ir kuriant tam skirtas gamybos darbo sekas. Kita WOIS laida (turi pasirodyti 2015 balandžio antroje pusėje) jau turės įdiegtą Sentinel-1 įrankinę ir eilę darbo sekų, naudojančių naują radaro duomenų rinkinį potvynių stebėjimui, vandens telkinių žymėjimui ir pan. Tai pavers WOIS į pilnai veikiančią stebėjimo sistemą. Teikiant šią laisvą, galingą ir plečiamą sistemą ir pastoviai didinant galimybes bei skiriant didelį dėmesį mokymams, projektas gyvuoja tam, kad sukurtų dar didesnio plėtimosi bazę, pavyzdžiui diegimui į kitas šalis ir regionus, Afrikoje ir už jos ribų.
## Šaltiniai
- Bauer-Gottwein, P., Jensen, I. H., Guzinski, R., Bredtoft, G. K. T., Hansen, S., & Michailovsky, C. I. (2015). Operational river discharge forecasting in poorly gauged basins: the Kavango River basin case study. Hydrology and Earth System Sciences, 19(3), 1469-1485.
- Guzinski, R.; Kass, S.; Huber, S.; Bauer-Gottwein, P.; Jensen, I.H.; Naeimi, V.; Doubkova, M.; Walli, A.; Tottrup, C. Enabling the Use of Earth Observation Data for Integrated Water Resource Management in Africa with the Water Observation and Information System. Remote Sens. 2014, 6, 7819-7839.
- Walli, A., Tottrup, C., Naeimi, V., Bauer-Gottwein, P., Bila, M., Mufeti, P., Tumbulto, J.W., Rajah, C., Moloele, L.S. & Koetz, B. "TIGER-NET---Enabling an earth observation capacity for integrated water resource management in Africa," presented at the ESA Living Planet Symp., Edinburgh, U.K., Sep. 11--13, 2013.

## Nuorodos
- More information about the WOIS software and the TIGER-NET project can be found on the project's website: www.tiger-net.org
- More information about ESA's TIGER initiative can be found on the initiative's website: <http://www.tiger.esa.int/> WOIS is available for download (after registration) from the TIGER website (<http://www.tiger.esa.int/page_eoservices_wois.php>) with source code of the developed plugins, scripts, models and workflows available from the project's GitHub page (<https://github.com/TIGER-NET>)
- More information about the new Sentinel satellites can be found on ESA's website: <http://www.esa.int/Our_Activities/Observing_the_Earth/Copernicus/Overview4>

### Autorius
This article was contributed by Radoslaw Guzinski (WOIS software developer) with contributions from the TIGER-NET technical teams at DHI-GRAS (www.dhi-gras.com), GeoVille (www.geoville.com), the technical universities in Vienna (<http://rs.geo.tuwien.ac.at/>) and Copenhagen (<http://www.env.dtu.dk/>) as well as the European Space Agency ( www.esa.int).

{{<content-end >}}
