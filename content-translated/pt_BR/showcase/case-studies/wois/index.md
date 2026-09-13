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

Uma das principais vantagens da caixa de ferramentas de processamento é a habilidade de usar perfeitamente funcionalidades de diferentes provedores de algoritmos de processamento e análise de dados. Isso pode ser usado para criar modelos automáticos para processamento e, através de um plugin QGIS desenvolvido durante o projeto TIGER-NET, para combinar sequencialmente algoritmos de diferentes fornecedores em cadeias de processamento baseadas em assistentes. Esta funcionalidade foi usada para criar uma biblioteca de fluxos de trabalho padronizados (com instruções) para executar tarefas comuns, mas complexas, relacionados à análise de dados EO dentro do gerenciamento de recursos hídricos.

![The WOIS graphical user interface, including the embedded workflow library (center) and wizard-based processing workflow (right)](africa_tiger1.jpg)

O uso operacional e prático do WOIS para apoiar o gerenciamento integrado dos recursos hídricos na África tem sido demonstrada através de uma série de casos de demonstração específica de usuários, abrangendo uma vasta gama de temas e produtos de informação. Estes incluem: a qualidade da água do lago; monitoramento de inundações; degradação da terra e caracterização da cobertura da terra; mapeamento dos corpos de água e modelagem hidrológica. Os casos de demonstração tem várias etapas. Em primeiro lugar, fluxos de trabalho de processamento end-to-end personalizados são desenvolvidos para os produtos e aplicações solicitados. Esses fluxos de trabalho são posteriormente utilizados para a derivação de produtos em áreas significativas e períodos de tempo, tal como solicitado pelos usuários. Na etapa final, os fluxos de trabalho (ou seja, sua estabilidade / desempenho e facilidade de uso), bem como os resultados de produtos estão sendo avaliadas num diálogo estreito com os usuários.

![Sentinel-1 flood monitoring of Caprivi flood plain, Namibia.](africa_tiger2.jpg)
## Conclusão
O desenvolvimento do WOIS representa um exemplo bem-sucedido de um modelo orientado para o usuário e de desenvolvimento colaborativo, onde funcionalidades foram concebidas, desenvolvidas e avaliadas através de casos designados pelo usuário, a fim de demonstrar o real impacto do sistema na melhoria do gerenciamento da água e os planos de gerenciamento dos recursos hídricos integrados. O WOIS já está implementado em principais autoridades das bacias hidrográficas Africana, vários ministérios e agências africanas, bem como em pesquisa e organizações humanitárias. Portanto, continuará o desenvolvimento em razão da necessidade contínua dos usuários para novas funcionalidades e melhorias funcionais e devido a melhorias gerais de software, algoritmos e métodos.

Um foco particular será garantir o apoio e implementação da capacidade de processamento para o novo sistema de satélites Sentinela, integrando as ESA Sentinel toolboxes em WOIS e desenvolvimento de fluxos de trabalho de produção dedicados. A próxima versão do WOIS (feito na segunda quinzena de abril de 2015) já irá incorporar o Sentinel-1 Toolbox e uma série de fluxos de trabalho utilizando este novo conjunto de dados de radar para monitoramento de inundação, mapemanento corpo d'água, etc. Isso vai transformar WOIS em um sistema completo de monitorização operacional. Através disposição deste sistema de licença livre, poderoso e extensível,  por meio de capacitação contínua e esforços de treinamento, o sucesso do projeto se desenvolve na construção básica de uma extensão, ou seja, roll-out para outros países e regiões da África e muito mais.
## Referências
- Bauer-Gottwein, P., Jensen, IH, Guzinski, R., Bredtoft, GKT, Hansen, S., & Michailovsky, CI (2015). Previsão Operacional de vazão do riol nas bacias mal calibrados: estudo de caso da bacia do rio Kavango. Sistema de Ciência da Terra e Hidrologiacia, 19 (3), 1469-1485.
- Guzinski, R .; Kass, S .; Huber, S .; Bauer-Gottwein, P .; Jensen, I.H .; Naeimi, V .; Doubkova, M .; Walli, A .; Tottrup, C. Permitindo o Uso de Dados de Observação da Terra para o Gerenciamento Integrado dos Recursos Hídricos na África com a observação de Água e Sistema de Informação. Remote Sens. 2014, 6, 7819-7839.
- Walli, A., Tottrup, C., Naeimi, V., Bauer-Gottwein, P., Bila, M., Mufeti, P., Tumbulto, J.W., Rajah, C., Moloele, L.S. & Koetz, B. "TIGER-NET---Enabling an earth observation capacity for integrated water resource management in Africa," presented at the ESA Living Planet Symp., Edinburgh, U.K., Sep. 11--13, 2013.

## Links
- More information about the WOIS software and the TIGER-NET project can be found on the project's website: www.tiger-net.org
- More information about ESA's TIGER initiative can be found on the initiative's website: <http://www.tiger.esa.int/> WOIS is available for download (after registration) from the TIGER website (<http://www.tiger.esa.int/page_eoservices_wois.php>) with source code of the developed plugins, scripts, models and workflows available from the project's GitHub page (<https://github.com/TIGER-NET>)
- More information about the new Sentinel satellites can be found on ESA's website: <http://www.esa.int/Our_Activities/Observing_the_Earth/Copernicus/Overview4>

### Autor
This article was contributed by Radoslaw Guzinski (WOIS software developer) with contributions from the TIGER-NET technical teams at DHI-GRAS (www.dhi-gras.com), GeoVille (www.geoville.com), the technical universities in Vienna (<http://rs.geo.tuwien.ac.at/>) and Copenhagen (<http://www.env.dtu.dk/>) as well as the European Space Agency ( www.esa.int).

{{<content-end >}}
