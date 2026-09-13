---
author: Radoslaw Guzinski
categories:
- Studii de Caz
date: '2015-04-01'
description: Enabling the Use of Earth Observation Data for Integrated Water Resource
  Management in Africa
draft: 'true'
heroImage: ''
tags:
- water
- case-study
- showcase
thumbnail: wois.png
title: Water Observation and Information System
type: showcase/case-studies

---
{{<content-start classes="notification is-light" >}}

The Water Observation and Information System (WOIS) is an open source software tool for monitoring, assessing and inventorying water resources in a cost-effective manner using Earth Observation (EO) data. The WOIS has been developed under the TIGER-NET project, which is a major component of the TIGER initiative of the European Space Agency (ESA) and whose main goal is to support the African Earth observation capacity for water resource monitoring. TIGER-NET aims to support the satellite-based assessment and monitoring of water resources from watershed to cross-border basin levels through the provision of a free and powerful software package, with associated capacity building, to African authorities.
## Descrierea Sistemului
The WOIS can be seen as a multipurpose system consisting of a spatial database, facilities for extracting and processing EO data, and integrative tools and models aimed at decision support e.g. hydrological modelling and GIS-embedded visualization and analysis tools. The WOIS is designed around QGIS, which acts as the front-end Graphical-User-Interface (GUI). QGIS was chosen as the central integrating platform, due to its clear and accessible GUI, strong development community, ease of implementing additional functionalities through Python plugins and its high level of interoperability with major GIS data formats through the use of the Geospatial Data Abstraction Library (GDAL/OGR) library.

Moreover, the integrated Processing Toolbox, formerly known as SEXTANTE, brings the ability to easily incorporate geoprocessing algorithms from various applications into QGIS. It acts as a joint repository for a wide range of algorithms, some native to QGIS and others imported from external applications, such as GRASS GIS or the Orfeo Toolbox. Support for algorithms from ESA's BEAM, NEST and Sentinel-1 Toolbox software and for setting up and executing SWAT based hydrological models was added to the Processing Toolbox during the WOIS development. The toolbox also allows for easy incorporation of custom R and Python scripts. The inputs and outputs of the Processing Toolbox algorithms can be evaluated with the QGIS capabilities of data I/O, rendering or map creation.

Un avantaj cheie al instrumentelor Processing este capacitatea de a folosi fără probleme funcționalități de la diferiți furnizori de algoritmi de prelucrare și analiză a datelor. Acest lucru poate fi util pentru a crea modele de automate de prelucrare și, printr-un plugin QGIS dezvoltat în cadrul proiectului TIGER-NET, pentru a combina secvențial algoritmi de la diverși furnizori în lanțurile de prelucrare asistată de calculator. Această funcționalitate a fost folosită pentru a crea o bibliotecă de fluxuri de lucru standardizate (cu instrucțiuni) pentru îndeplinirea unor sarcini comune, dar complexe, legate de analiza datelor EO în managementul resurselor de apă.

![The WOIS graphical user interface, including the embedded workflow library (center) and wizard-based processing workflow (right)](africa_tiger1.jpg)

Utilizarea operațională și practică a WOIS la sprijinirea gestionării integrate a resurselor de apă în Africa a fost demonstrată printr-o serie de cazuri demonstrative de utilizare specifice, care acoperă o gamă largă de teme și produse informative. Acestea includ: calitatea apei lacului; monitorizarea riscului de inundații; caracterizarea degradării și acoperirii terenului; cartografierea și modelarea hidrologică a cursurilor de apă. Cazurile demonstrative au mai multe etape. În primul rând, sunt dezvoltate fluxurile de lucru end-to-end, de procesare personalizată, pentru produsele și aplicațiile solicitate. Aceste fluxuri de lucru sunt ulterior utilizate pentru derivarea produselor asupra unor zone semnificative și pe perioadele solicitate de utilizatori. În etapa finală, fluxurile de lucru (cum ar fi stabilitatea/performanța și ușurința în utilizare a acestora), precum și rezultatele produselor sunt evaluate în dialog strâns cu utilizatorii.

![Sentinel-1 flood monitoring of Caprivi flood plain, Namibia.](africa_tiger2.jpg)
## Concluzii
Dezvoltarea WOIS reprezintă un exemplu de succes al unui model de dezvoltare colaborațional, condus de utilizator, în care funcționalitățile au fost proiectate, dezvoltate și evaluate prin cazuri stabilite de către utilizator, pentru a demonstra impactul real al sistemului la îmbunătățirea gestionării apei și a planurilor integrate de gestionare a resurselor de apă. WOIS se află deja în implementare la autoritățile din importante bazine hidrografice din Africa, la mai multe ministere și agenții din Africa, și la organizațiile umanitare și de cercetare. Prin urmare, va continua să se dezvolte, ca răspuns la cerințele continue ale utilizatorilor pentru noi funcționalități și îmbunătățiri și datorită îmbunătățirilor generale ale softurilor, algoritmilor și metodelor.

Un accent deosebit va fi pus pe asigurarea suportului și punerea în aplicare a capacității de procesare pentru noul sistem de satelit Sentinel, prin integrarea instrumentelor SEC Sentinel în WOIS și dezvoltarea fluxurilor de lucru dedicate producției. Următoara versiune de WOIS (programată în a doua jumătate a lunii aprilie 2015) va include deja Sentinel-1 Toolbox și un număr de fluxuri de lucru, folosind acest nou set de date radar pentru monitorizarea inundațiilor, cartografierea cursurilor de apă, etc. Acest lucru va transforma WOIS  într-un  sistem de monitorizare complet operațional. Prin furnizarea acestui sistem puternic și extensibil fără licență, și prin eforturile de formare continuă, proiectul prosperă, stând la baza extinderii în alte țări și regiuni din Africa și dincolo.
## Referințe
- Bauer-Gottwein, P., Jensen, I. H., Guzinski, R., Bredtoft, G. K. T., Hansen, S., & Michailovsky, C. I. (2015). Prognoză operațională de descărcare a râurilor în bazinele cu volum redus: studiu de caz pentru bazinul râului Kavango. Știința Sistemului Hidrologic și a Pământului, 19(3), 1469-1485.
- Guzinski, R.; Kass, S.; Huber, S.; Bauer-Gottwein, P.; Jensen, I.H.; Naeimi, V.; Doubkova, M.; Walli, A.; Tottrup, C. Utilizarea datelor de observare a Pământului pentru Managementul Integrat al Resurselor de Apă din Africa cu ajutorul Sistemului de Informații și Observare a Apei. Remote Sens. 2014, 6, 7819-7839.
- Walli, A., Tottrup, C., Naeimi, V., Bauer-Gottwein, P., Bila, M., Mufeti, P., Tumbulto, J.W., Rajah, C., Moloele, L.S. & Koetz, B. "TIGER-NET---Enabling an earth observation capacity for integrated water resource management in Africa," presented at the ESA Living Planet Symp., Edinburgh, U.K., Sep. 11--13, 2013.

## Legături
- More information about the WOIS software and the TIGER-NET project can be found on the project's website: www.tiger-net.org
- More information about ESA's TIGER initiative can be found on the initiative's website: <http://www.tiger.esa.int/> WOIS is available for download (after registration) from the TIGER website (<http://www.tiger.esa.int/page_eoservices_wois.php>) with source code of the developed plugins, scripts, models and workflows available from the project's GitHub page (<https://github.com/TIGER-NET>)
- More information about the new Sentinel satellites can be found on ESA's website: <http://www.esa.int/Our_Activities/Observing_the_Earth/Copernicus/Overview4>

### Autor
This article was contributed by Radoslaw Guzinski (WOIS software developer) with contributions from the TIGER-NET technical teams at DHI-GRAS (www.dhi-gras.com), GeoVille (www.geoville.com), the technical universities in Vienna (<http://rs.geo.tuwien.ac.at/>) and Copenhagen (<http://www.env.dtu.dk/>) as well as the European Space Agency ( www.esa.int).

{{<content-end >}}
