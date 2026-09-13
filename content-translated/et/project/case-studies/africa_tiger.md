---
HasBanner: false
archived: true
date: 2012-06-30
draft: false
featured: false
section: projekt
sidebar: true
thumbnail: images/africa_tiger1.jpg
title: 'Water Observation and Information System: Maa jälgimise andmete kasutuselevõtt
  Aafrika integreeritud veeressursside haldamiseks'
type: case-study

---
{{<content-start >}}
# Water Observation and Information System: Maa jälgimise andmete kasutuselevõtt Aafrika integreeritud veeressursside haldamiseks
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>June 30, 2012</span>
</p>

The Water Observation and Information System (WOIS) is an open source software tool for monitoring, assessing and inventorying water resources in a cost-effective manner using Earth Observation (EO) data. The WOIS has been developed under the TIGER-NET project, which is a major component of the TIGER initiative of the European Space Agency (ESA) and whose main goal is to support the African Earth observation capacity for water resource monitoring. TIGER-NET aims to support the satellite-based assessment and monitoring of water resources from watershed to cross-border basin levels through the provision of a free and powerful software package, with associated capacity building, to African authorities.
## Süsteemi kirjeldus
The WOIS can be seen as a multipurpose system consisting of a spatial database, facilities for extracting and processing EO data, and integrative tools and models aimed at decision support e.g. hydrological modelling and GIS-embedded visualization and analysis tools. The WOIS is designed around QGIS, which acts as the front-end Graphical-User-Interface (GUI). QGIS was chosen as the central integrating platform, due to its clear and accessible GUI, strong development community, ease of implementing additional functionalities through Python plugins and its high level of interoperability with major GIS data formats through the use of the Geospatial Data Abstraction Library (GDAL/OGR) library.

Moreover, the integrated Processing Toolbox, formerly known as SEXTANTE, brings the ability to easily incorporate geoprocessing algorithms from various applications into QGIS. It acts as a joint repository for a wide range of algorithms, some native to QGIS and others imported from external applications, such as GRASS GIS or the Orfeo Toolbox. Support for algorithms from ESA's BEAM, NEST and Sentinel-1 Toolbox software and for setting up and executing SWAT based hydrological models was added to the Processing Toolbox during the WOIS development. The toolbox also allows for easy incorporation of custom R and Python scripts. The inputs and outputs of the Processing Toolbox algorithms can be evaluated with the QGIS capabilities of data I/O, rendering or map creation.

Töötlustööriistakasti oluline eelis on võime kasutada sujuvalt erinevate algoritmi pakkujate funktsionaalsusi andmete töötlemise ja analüüsi jaoks. Seda saab kasutada automaatsete töötlemismudelite loomiseks ning läbi TIGER-NET projekti arendatud QGIS-i pistikprogrammi, et järjestikuliselt ühendada erinevate pakkujate algoritmid võlukepil põhinevates töötlusahelates. Seda funktsionaalsust kasutati standardiseeritud töövoogude (koos juhistega) loomiseks, mis võimaldavad teha tavalisi, kuid keerulisi ülesandeid seoses Maa jälgimise andmete analüüsiga veeressursside haldamises.

<figure>
<img src="../images/africa_tiger1.jpg" class="align-center" style="width:100.0%" alt="africa_tiger1.jpg" />
<figcaption>The WOIS graphical user interface, including the embedded workflow library (center) and wizard-based processing workflow (right)</figcaption>
</figure>

WOIS-i operatiivne ja praktiline kasutamine Aafrika integreeritud veeressursside haldamise toetamiseks on demonstreeritud mitme kasutajaspetsiifilise näidiste kaudu, mis hõlmavad laia teemavalikut ja infotooteid. Nende hulka kuuluvad järve vee kvaliteet, üleujutuste jälgimine, maade degradatsioon ja maa katte iseloomustamine, veekogude kaardistamine ning hüdroloogiline modelleerimine. Demonstratsiooninäidistel on mitu etappi. Esimesena arendatakse kohandatud algusest lõpuni töötlevad töövood soovitud toodete ja rakenduste jaoks. Neid töövooge kasutatakse seejärel toodete tuletamiseks märkimisväärsetes piirkondades ja ajaperioodides vastavalt kasutajate soovile. Viimases etapis hinnatakse töövoogude stabiilsust/töökindlust, kasutusmugavust ja toodangu tulemusi tihedas dialoogis kasutajatega.

<figure>
<img src="../images/africa_tiger2.jpg" class="align-center" style="width:100.0%" alt="africa_tiger2.jpg" />
<figcaption>Sentinel-1 flood monitoring of Caprivi flood plain, Namibia.</figcaption>
</figure>

## Järeldus
WOIS-i arendamine esindab edukat näidet kasutajakesksest ja koostööl põhinevast arendusmudelist, kus funktsionaalsused on kavandatud, arendatud ja hinnatud kasutajate poolt määratud juhtumianalüüside kaudu, et näidata süsteemi tegelikku mõju veemajanduse ja integreeritud veeressursside haldamise kavade täiustamisel. WOIS on juba rakendatud olulistes Aafrika jõgede valgalade ametiasutustes, mitmetes Aafrika ministeeriumides ja agentuurides ning samuti teadus- ja humanitaarorganisatsioonides. Seetõttu jätkub selle arendamine vastusena kasutajate pidevatele nõuetele uute funktsionaalsuste ja funktsionaalsete täiustuste ning üldiste tarkvara-, algoritmi- ja meetoditõhustuste jaoks.

Erilist tähelepanu pööratakse uue Sentinel satelliidisüsteemi töötlusvõime toetamisele ja rakendamisele, integreerides ESA Sentineli tööriistakastid WOIS-i ning arendades selleks spetsiaalseid tootmistöövooge. Järgmine WOIS-i versioon (oodatavalt aprilli teise poole 2015. aastal) sisaldab juba Sentinel-1 tööriistakasti ja mitmeid töövooge, mis kasutavad seda uut radarandmestikku üleujutuste jälgimiseks, veekogude kaardistamiseks jne. See muudab WOIS-i täielikult toimivaks jälgimissüsteemiks. Pakkudes selle litsentsivaba, võimsat ja laiendatavat süsteemi ning jätkates võimekuse loomise ja koolitustegevustega, püüab projekt luua aluse selle laiendamiseks, st selle rakendamiseks teistesse Aafrika riikidesse ja piirkondadesse ning kaugemale.
## Viited
- Bauer-Gottwein, P., Jensen, I. H., Guzinski, R., Bredtoft, G. K. T., Hansen, S., & Michailovsky, C. I. (2015). Operational river discharge forecasting in poorly gauged basins: the Kavango River basin case study. Hydrology and Earth System Sciences, 19(3), 1469-1485.
- Guzinski, R.; Kass, S.; Huber, S.; Bauer-Gottwein, P.; Jensen, I.H.; Naeimi, V.; Doubkova, M.; Walli, A.; Tottrup, C. Enabling the Use of Earth Observation Data for Integrated Water Resource Management in Africa with the Water Observation and Information System. Remote Sens. 2014, 6, 7819-7839.
- Walli, A., Tottrup, C., Naeimi, V., Bauer-Gottwein, P., Bila, M., Mufeti, P., Tumbulto, J.W., Rajah, C., Moloele, L.S. & Koetz, B. "TIGER-NET---Enabling an earth observation capacity for integrated water resource management in Africa," presented at the ESA Living Planet Symp., Edinburgh, U.K., Sep. 11--13, 2013.

## Lingid
- More information about the WOIS software and the TIGER-NET project can be found on the project's website: www.tiger-net.org
- More information about ESA's TIGER initiative can be found on the initiative's website: <http://www.tiger.esa.int/> WOIS is available for download (after registration) from the TIGER website (<http://www.tiger.esa.int/page_eoservices_wois.php>) with source code of the developed plugins, scripts, models and workflows available from the project's GitHub page (<https://github.com/TIGER-NET>)
- More information about the new Sentinel satellites can be found on ESA's website: <http://www.esa.int/Our_Activities/Observing_the_Earth/Copernicus/Overview4>

### Autor
This article was contributed by Radoslaw Guzinski (WOIS software developer) with contributions from the TIGER-NET technical teams at DHI-GRAS (www.dhi-gras.com), GeoVille (www.geoville.com), the technical universities in Vienna (<http://rs.geo.tuwien.ac.at/>) and Copenhagen (<http://www.env.dtu.dk/>) as well as the European Space Agency ( www.esa.int).

{{<content-end >}}
