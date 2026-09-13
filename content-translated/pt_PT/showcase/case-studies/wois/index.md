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
## Descrição do Sistema
The WOIS can be seen as a multipurpose system consisting of a spatial database, facilities for extracting and processing EO data, and integrative tools and models aimed at decision support e.g. hydrological modelling and GIS-embedded visualization and analysis tools. The WOIS is designed around QGIS, which acts as the front-end Graphical-User-Interface (GUI). QGIS was chosen as the central integrating platform, due to its clear and accessible GUI, strong development community, ease of implementing additional functionalities through Python plugins and its high level of interoperability with major GIS data formats through the use of the Geospatial Data Abstraction Library (GDAL/OGR) library.

Moreover, the integrated Processing Toolbox, formerly known as SEXTANTE, brings the ability to easily incorporate geoprocessing algorithms from various applications into QGIS. It acts as a joint repository for a wide range of algorithms, some native to QGIS and others imported from external applications, such as GRASS GIS or the Orfeo Toolbox. Support for algorithms from ESA's BEAM, NEST and Sentinel-1 Toolbox software and for setting up and executing SWAT based hydrological models was added to the Processing Toolbox during the WOIS development. The toolbox also allows for easy incorporation of custom R and Python scripts. The inputs and outputs of the Processing Toolbox algorithms can be evaluated with the QGIS capabilities of data I/O, rendering or map creation.

Uma das principais vantagens da Caixa de Ferramentas do Processamento é a capacidade de usar facilmente funcionalidades de diferentes fornecedores de algoritmos para processamento e análise de dados. Isso pode ser usado para a criação modelos de processamento automático e, através de um plugin QGIS desenvolvido durante o projeto TIGER-NET, para combinar sequencialmente algoritmos dos diferentes provedores em cadeias de processamento baseadas em assistentes. Esta funcionalidade foi usada para criar uma biblioteca de fluxos de trabalho padronizados (com instruções) para executar tarefas comuns, porém complexas, relacionadas à análise de dados EO na gestão de recursos hídricos.

![The WOIS graphical user interface, including the embedded workflow library (center) and wizard-based processing workflow (right)](africa_tiger1.jpg)

O uso operacional e prático do WOIS para apoiar a gestão integrada dos recursos hídricos na África foi demonstrado através de uma série de casos de demonstração específicos do utilizador cobrindo uma ampla gama de temas e produtos de informação. Estes incluem: qualidade da água do lago; monitorização de inundação; degradação do solo e caracterização da cobertura do solo; mapeamento de corpos d'água e modeção hidrológica. Os casos de demonstração têm várias etapas. Primeiro, fluxos de trabalho de processamento de ponta a ponta personalizados são desenvolvidos para os produtos e aplicações solicitadas. Esses fluxos de trabalho são usados subsequentemente para derivação de produtos em áreas e períodos de tempo significativos, conforme solicitado pelos utilizadores. Na etapa final, os fluxos de trabalho (ou seja, sua estabilidade / desempenho e facilidade de uso), bem como os resultados do produto, são avaliados num diálogo próximo com os utilizadores.

![Sentinel-1 flood monitoring of Caprivi flood plain, Namibia.](africa_tiger2.jpg)
## Conclusões
O desenvolvimento do WOIS representa um exemplo bem-sucedido de um modelo de desenvolvimento colaborativo e orientado para o utilizador, onde as funcionalidades foram projetadas, desenvolvidas e avaliadas por meio de casos designados pelo utilizador para demonstrar o real impacto do sistema na melhoria da gestão da água e planos de gestão integrados de recursos hídricos. O WOIS já está implementado nas principais autoridades africanasque gerem bacias hidrográficas, em vários ministérios e agências africanas, bem como em organizações de pesquisa e humanitárias. Por conseguinte, continuará a desenvolver-se em resposta a requisitos contínuos do utilizador para novas funcionalidades e melhorias funcionais e devido a melhorias gerais de software, algoritmo e metodologia.

O foco particular será garantir o suporte e a implementação da capacidade de processamento do novo sistema de satélites Sentinel, integrando as caixas de ferramentas da ESA Sentinel no WOIS e desenvolvendo fluxos de trabalho de produção dedicados. A próxima versão do WOIS (prevista para a segunda quinzena de abril de 2015) já incorporará o Sentinel-1 Toolbox e vários fluxos de trabalho utilizando este novo conjunto de dados de radar para monitorização de inundação, mapeamento de corpos de água etc. Isto transformará o WOIS em totalmente sistema de monitorização operacional. Através da provisão deste sistema livre de licenças, poderoso e extensível, e através de contínuos esforços de capacitação e formação, o projecto prospera para construir a base para uma extensão, isto é, implantação para outros países e regiões de África e além.
## Referências
- Bauer-Gottwein, P., Jensen, I. H., Guzinski, R., Bredtoft, G. K. T., Hansen, S., & Michailovsky, C. I. (2015). Operational river discharge forecasting in poorly gauged basins: the Kavango River basin case study. Hydrology and Earth System Sciences, 19(3), 1469-1485.
- Guzinski, R.; Kass, S.; Huber, S.; Bauer-Gottwein, P.; Jensen, I.H.; Naeimi, V.; Doubkova, M.; Walli, A.; Tottrup, C. Enabling the Use of Earth Observation Data for Integrated Water Resource Management in Africa with the Water Observation and Information System. Remote Sens. 2014, 6, 7819-7839.
- Walli, A., Tottrup, C., Naeimi, V., Bauer-Gottwein, P., Bila, M., Mufeti, P., Tumbulto, J.W., Rajah, C., Moloele, L.S. & Koetz, B. "TIGER-NET---Enabling an earth observation capacity for integrated water resource management in Africa," presented at the ESA Living Planet Symp., Edinburgh, U.K., Sep. 11--13, 2013.

## Hiperligações
- More information about the WOIS software and the TIGER-NET project can be found on the project's website: www.tiger-net.org
- More information about ESA's TIGER initiative can be found on the initiative's website: <http://www.tiger.esa.int/> WOIS is available for download (after registration) from the TIGER website (<http://www.tiger.esa.int/page_eoservices_wois.php>) with source code of the developed plugins, scripts, models and workflows available from the project's GitHub page (<https://github.com/TIGER-NET>)
- More information about the new Sentinel satellites can be found on ESA's website: <http://www.esa.int/Our_Activities/Observing_the_Earth/Copernicus/Overview4>

### Sobre o autor:
This article was contributed by Radoslaw Guzinski (WOIS software developer) with contributions from the TIGER-NET technical teams at DHI-GRAS (www.dhi-gras.com), GeoVille (www.geoville.com), the technical universities in Vienna (<http://rs.geo.tuwien.ac.at/>) and Copenhagen (<http://www.env.dtu.dk/>) as well as the European Space Agency ( www.esa.int).

{{<content-end >}}
