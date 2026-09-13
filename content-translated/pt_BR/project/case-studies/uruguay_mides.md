---
HasBanner: false
archived: true
date: 2016-03-01
draft: false
featured: false
section: projeto
sidebar: true
thumbnail: images/uruguay_mides1.png
title: Uso do QGIS no Ministério do Desenvolvimento Social do Uruguai (MIDES)
type: case-study

---
{{<content-start >}}
# Uso do QGIS no Ministério do Desenvolvimento Social do Uruguai (MIDES)
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>March 01, 2016</span>
</p>

## Introdução
The Ministry of Social Development of Uruguay ([MIDES,](http://www.mides.gub.uy/innovaportal/v/4376/3/innova.front/mision) , for its acronym in Spanish) is responsible for the national social policies. MIDES is also accountable for the coordination -at both sectoral and territorial levels- articulation, monitoring, supervision and evaluation of plans, programs and projects, within the areas of its competence, aiming at the consolidation of a progressive redistributive social policy.

The National Division of Evaluation and Monitoring ([DINEM](http://dinem.mides.gub.uy/innovaportal/v/25948/11/innova.front/mision-y-cometidos) ) is a section of MIDES that oversees the monitoring and evaluation of plans, programs, actions, devices and social projects through the national territory. DINEM also produces and manages necessary information to improve their design and implementation.

The [Department of Geography of DINEM](http://dinem.mides.gub.uy/innovaportal/v/25507/11/innova.front/departamento-de-geografia) is responsible for the production, management and analysis of geographical information,
## QGIS no Departamento de Geografia do DINEM
Ever since the consolidation of the Department of Geography in 2012, we have tried to incorporate open source software to fulfill our duties. In particular, the management of an extensive field work, consisting in the annual implementation of approximately 40,000 visits to socially vulnerable households throughout the country. The objective was to conform a thorough georeferenced database of target households, in order to improve social policies implementation. Particularly, data was collected to enhance the scope of monetary transfer programs ([\"Asignaciones Familiares -- Plan de Equidad\"](https://www.bps.gub.uy/3540/plan-de-equidad.html) and [\"Tarjeta Uruguay Social\"](http://www.mides.gub.uy/innovaportal/v/55480/3/innova.front/tarjeta-uruguay-social-tus)). The survey form applied contemplates social, housing, and environmental aspects.

Logística para viabilizar tal trabalho de campo envolvendo o uso de pacotes estatísticos para gerenciar o banco de dados gerado, juntamente com um uso intensivo de GIS para organizar viagens de campo e georeferenciamento de dados aliviados.

<figure>
<img src="../images/uruguay_mides1.png" class="align-center" alt="uruguay_mides1.png" />
<figcaption>QGIS at work: identifying houses on informal settlements to implement fieldwork</figcaption>
</figure>

Embora o software proprietário tenha sido implementado quando o processo de trabalho foi iniciado, o desenvolvimento das próprias tarefas gradualmente exigiu que ele fosse convertido em software de código aberto. À medida que o processo como um todo se tornou mais computadorizado - incorporando um mecanismo de fluxo de trabalho e um banco de dados geoespacial PostGIS -, os requisitos de licença e os benefícios oferecidos pelas opções de software livre e de código aberto (FOSS) nos incentivaram a fazer a mudança. Dessa forma, como o projeto QGIS foi refinado (menos bugs e mais funcionalidades), conseguimos satisfazer nossas necessidades usando o QGIS. As ferramentas associadas ao PostGIS permitiram ao grupo de trabalho coordenar rapidamente as tarefas necessárias para viabilizar viagens de campo diárias, juntamente com as tarefas de análise subsequentes no mesmo campo de dados gerado, pouco depois de ter sido aliviado e digitalizado.

<figure>
<img src="../images/uruguay_mides2.png" class="align-center" alt="uruguay_mides2.png" />
<figcaption>QGIS at work: Montevideo, Uruguay’s capital and most populated city, overlayed with PostGIS layer showing to-do visits (mostly composed of socially vulnerable households, in the outskirts of the city)</figcaption>
</figure>

In addition to information management and field work implementation, we constantly use QGIS typical geospatial tools to produce tematic cartography, and in spatial analysis tasks. This last, as much about the data that the fieldwork generates, as with other ministry programs information, and frequently even to aid interinstitutional projects. With [\"qgis2web\"](https://plugins.qgis.org/plugins/qgis2web/) we were able to produce interactive maps, which have become the main way to communicate the results of such investigations. They allow human resources within other programs and agencies to easily and effectively manage higher amounts of information than with a collection of static maps, even when these resources are not used to reading spatial data.
## Conclusão
O QGIS tornou-se um software fundamental para o Departamento de Geografia do DINEM. Apresenta um excelente desempenho para trabalhar com arquivos pesados e interagir com o PostGIS e com o nosso mecanismo de fluxo de trabalho. Isso nos permite ter uma excelente gestão de dados geográficos, o que também contribui para a produção de mapas base e cartografias temáticas de qualidade superior.

At the same time, extra features that are incorporated through plugins are of great value to us. For instance, the possibility of exporting \"leaflet\" map viewers, as well as incorporating high resolution satellite imagery directly into the GIS work area through "OpenLayers" to manually vectorize information, among others.

This variety of options is precisely what has allowed us to develop the specific and at the same time very different technical solutions that programs and agencies have been needing through past years.As mentioned in this article, we can state that QGIS meets the necessary requirements to be used in public administration as desktop GIS software. Also it has been a cornerstone in helping this institution to set up a web map, offering general population much information about social issues ([SIG MIDES](https://mapas.mides.gub.uy/), OpenLayers based WEB GIS developed by the IT division).
## Autores
Guillermo D\'Angelo - Head of the Geography Department (DINEM-MIDES, Uruguay). Degree in Geography.

Richard Detomasi - Assessor da Seção de Análise Espacial do Departamento de Geografia (DINEM-MIDES, Uruguai). Ph.D. estudante em Ciências Sociais, Estudos da População. Magister em Estudos Contemporâneos da América Latina. Licenciatura em Ciências Antropológicas.

Martín Hahn - Assessor da Seção de Análise Espacial do Departamento de Geografia (DINEM-MIDES, Uruguai). Bach. atualmente cursando Geografia.

Apesar de o presente artigo ter sido escrito pelos três acima mencionados, há mais de cem pessoas envolvidas no processo descrito nele, então este trabalho pertence principalmente a eles.

Contact: <mapas@mides.gub.uy>

{{<content-end >}}
