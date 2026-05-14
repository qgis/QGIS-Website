---
author: Radoslaw Guzinski
categories:
- Case studies
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
## Sistem Açıklaması
The WOIS can be seen as a multipurpose system consisting of a spatial database, facilities for extracting and processing EO data, and integrative tools and models aimed at decision support e.g. hydrological modelling and GIS-embedded visualization and analysis tools. The WOIS is designed around QGIS, which acts as the front-end Graphical-User-Interface (GUI). QGIS was chosen as the central integrating platform, due to its clear and accessible GUI, strong development community, ease of implementing additional functionalities through Python plugins and its high level of interoperability with major GIS data formats through the use of the Geospatial Data Abstraction Library (GDAL/OGR) library.

Moreover, the integrated Processing Toolbox, formerly known as SEXTANTE, brings the ability to easily incorporate geoprocessing algorithms from various applications into QGIS. It acts as a joint repository for a wide range of algorithms, some native to QGIS and others imported from external applications, such as GRASS GIS or the Orfeo Toolbox. Support for algorithms from ESA's BEAM, NEST and Sentinel-1 Toolbox software and for setting up and executing SWAT based hydrological models was added to the Processing Toolbox during the WOIS development. The toolbox also allows for easy incorporation of custom R and Python scripts. The inputs and outputs of the Processing Toolbox algorithms can be evaluated with the QGIS capabilities of data I/O, rendering or map creation.

İşleme Alet Kutusunun en önemli avantajı, veri işleme ve analizi için farklı algoritma sağlayıcılarının işlevlerini sorunsuz bir şekilde kullanma becerisidir. Bu, otomatik işleme modelleri oluşturmak ve TIGER-NET projesi sırasında geliştirilen bir QGIS eklentisi aracılığıyla, farklı sağlayıcılardan gelen algoritmaları sihirbaz tabanlı işleme zincirlerine sırayla birleştirmek için kullanılabilir. Bu işlevsellik, su kaynakları yönetimi içinde EO veri analizi ile ilgili ortak ama karmaşık görevleri yerine getirmek için standart talimatların (talimatlarla birlikte) bir kütüphanesini oluşturmak için kullanılmıştır.

![The WOIS graphical user interface, including the embedded workflow library (center) and wizard-based processing workflow (right)](africa_tiger1.jpg)

SGBS nin Afrikada ki birleşik su kaynağı yönetimi işlevsel ve pratik kullanımı 

![Sentinel-1 flood monitoring of Caprivi flood plain, Namibia.](africa_tiger2.jpg)
## Sonuç
SGBS nin geliştirilmesi kullanıcı-destekli ve fonksiyonelliği su yönetimi artırımında sistemin gerçek etkisini kullanıcı-tasarımlı durumlar işbirliği geliştirme modeli nin başarılı bir örneğini temsil eder.

Özellikle, ESA Sentinel araç kutularını WOIS'ye entegre ederek ve özel üretim iş akışları geliştirerek yeni Sentinel uydu sistemi için işlem kapasitesinin desteklenmesini ve uygulanmasını sağlamaya odaklanacağız. WOIS'in bir sonraki sürümü (Nisan 2015'ün ikinci yarısında), Sentinel-1 Toolbox'ı ve bu yeni radar veri setini kullanarak taşkın izleme, su vücut haritalama vb. Için bir takım iş akışlarını zaten içerecektir. Bu, WOIS'yi, Operasyonel izleme sistemi. Bu lisanssız, güçlü ve genişletilebilir sistemin sağlanması ve devam eden kapasite geliştirme ve eğitim çabaları sayesinde proje, Afrika'daki ve sonrasında diğer ülkelere ve bölgelere yayılma için bir temel oluşturmak için gelişir.
## Referanslar
- Bauer-Gottwein, P., Jensen, I. H., Guzinski, R., Bredtoft, G. K. T., Hansen, S., & Michailovsky, C. I. (2015).Yetersiz hacimli havzalarda işlevsel nehir boşaltım tahmini: the Kavango River basin case study. Hydrology and Earth System Sciences, 19(3), 1469-1485.
-  Guzinski, R.; Kass, S.; Huber, S.; Bauer-Gottwein, P.; Jensen, I.H.; Naeimi, V.; Doubkova, M.; Walli, A.; Tottrup, C. Afrikadaki Birleştirilmiş Su Kaynakları Yönetimi için Yer Gözlem Verisi Kullanımını Etkinleştirme. Remote Sens. 2014, 6, 7819-7839.
- Walli, A., Tottrup, C., Naeimi, V., Bauer-Gottwein, P., Bila, M., Mufeti, P., Tumbulto, J.W., Rajah, C., Moloele, L.S. & Koetz, B. "TIGER-NET---Enabling an earth observation capacity for integrated water resource management in Africa," presented at the ESA Living Planet Symp., Edinburgh, U.K., Sep. 11--13, 2013.

## Bağlantılar
- More information about the WOIS software and the TIGER-NET project can be found on the project's website: www.tiger-net.org
- More information about ESA's TIGER initiative can be found on the initiative's website: <http://www.tiger.esa.int/> WOIS is available for download (after registration) from the TIGER website (<http://www.tiger.esa.int/page_eoservices_wois.php>) with source code of the developed plugins, scripts, models and workflows available from the project's GitHub page (<https://github.com/TIGER-NET>)
- More information about the new Sentinel satellites can be found on ESA's website: <http://www.esa.int/Our_Activities/Observing_the_Earth/Copernicus/Overview4>

### Yazar
This article was contributed by Radoslaw Guzinski (WOIS software developer) with contributions from the TIGER-NET technical teams at DHI-GRAS (www.dhi-gras.com), GeoVille (www.geoville.com), the technical universities in Vienna (<http://rs.geo.tuwien.ac.at/>) and Copenhagen (<http://www.env.dtu.dk/>) as well as the European Space Agency ( www.esa.int).

{{<content-end >}}
