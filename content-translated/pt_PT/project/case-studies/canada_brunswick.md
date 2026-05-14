---
HasBanner: false
archived: true
date: 2013-01-01
draft: false
featured: false
section: projeto
sidebar: true
thumbnail: images/canada_brunswick1.jpg
title: Criando o Mapa de Trilhos do Fundy Footpath com QGIS
type: case-study

---
{{<content-start >}}
# Criando o Mapa de Trilhos do Fundy Footpath com QGIS
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>January 01, 2013</span>
</p>

![](../images/canada_brunswick1.jpg)

The Fundy Footpath is a wilderness hiking trail located along the Fundy coast of New Brunswick, Canada. It is a charter member of the [UNESCO Fundy Biosphere Reserve](http://fundy-biosphere.ca/en/about-us/the-reserve) and affiliated with the [NB Trails Council Inc.](http://www.sentiernbtrail.com/) and the Trans Canada Trail. The Footpath takes hikers through the coastal Acadian Forest, home to the world's highest tides, old growth forests, and several rare and unique types of flora and fauna.

O trilho foi criado, e é mantido e promovido por um grupo de voluntários conhecido como a Associação Fundy de Trilhos e Caminhadas Inc. (AFTC) (1975). Como uma organização sem fins lucrativos AFTC recolhe os seus fundos para as atividades através da venda de guias que incluem um mapa do trilho. Em 2011, eu abordei a AFTC para me voluntariar na atualização do mapa oficial do trilho. Como voluntário criar um mapa para uma organização sem fins lucrativos como o QGIS foi ideal tanto como uma ferramenta de edição de dados e como para a produção final do mapa. Através dos meus esforços e dos membros da AFTC o novo mapa oficial do Trilho de Fundy foi criado do início ao fim com QGIS e incluído com o guia.

<figure>
<img src="../images/canada_brunswick2.jpg" class="align-right" alt="canada_brunswick2.jpg" />
<figcaption>QGIS GPS Tools Plugin for data collection</figcaption>
</figure>

## O Projeto
O processo de criação do novo mapa do Fundy Footpath com o QGIS pode ser dividido em três diferentes partes:
- Recolha de dados.
- Preparação e edição de dados.
- Produção do mapa.

Data was collected both with handheld GPS units and from various free data sources. Trail data (e.g. trail centerline, campsite locations, and tidal crossings) was collected with a Garmin GPSMap 60CSX. This data was then transferred from the GPS and to shapefile format in QGIS using the GPS plugin. Free data in vector formats was then obtained from the [Natural Resources Canada (NRCan) CanVec](http://geogratis.cgdi.gc.ca/geogratis/en/product/search.do?id=5460AA9D-54CD-8349-C95E-1A4D03172FDF) website and from [Service New Brunswick (SNB) online](http://www.snb.ca/gdam-igec/e/2900e_1.asp).

<figure>
<img src="../images/canada_brunswick3.jpg" class="align-right" alt="canada_brunswick3.jpg" />
<figcaption>Creation of the footpath map in QGIS</figcaption>
</figure>

Para preparar os dados na versão final do mapa as seguintes ferramentas do QGIS foram usadas para alcançar as tarefas específicas:
- Os dados recolhidos com o GPS foram corrigidos usando a barra de ferramentas de edição.
- A informação vetorial através do NRCan e SNB foi junta, interrogada e cortada para o mapa final da área usando ferramentas vetoriais.
- O ficheiro separado por vírgulas obtido do SNB foi importado para o QGIS como uma camada de pontos usando a extensão Adicionar Camadada Delimitada por Texto, a extensão de Interpolação foi usada para criar um raster de elevação que foi usado para criar um raster de sombreamento e para criar a camada de curvas de nível  com a extensão de ferramentas raster do GDAL.

<figure>
<img src="../images/canada_brunswick4.jpg" class="align-right" alt="canada_brunswick4.jpg" />
<figcaption>Footpath map in the Print Composer</figcaption>
</figure>

Once the data required to create the map was assembled and in a usable format the creation of the final map was started. To create the hiking map data was symbolized and labeled with the symbolization properties dialog and labeled with QGIS's very functional label engine. Once labels and symbolization were in place the map composer tool was run to create the layout. It was very easy to add useful map elements such as a custom north arrow and elevation profile in the print composer. Two layouts were created since it was to be a double-sided map. Once both layouts were created they were exported as PDF files and sent to the printers.
## Conclusões
The hiking map was printed on heavy-duty waterproof paper, folded and inserted in the back of the new edition of the Fundy Footpath Hiker's Guide Book. QGIS was the best and most functional choice for the creation of this map. Being free software the price was right for a volunteer creating a map for a non-profit organization. But the real advantage of QGIS was that it had all of the functionality and tools required to create a highly useful and detailed hiking map from start to finish. I would highly recommend QGIS to both experienced and beginning GIS users alike.

<figure>
<img src="../images/canada_brunswick5.jpg" class="align-right" alt="canada_brunswick5.jpg" />
<figcaption>The final Fundy Footpath map with accompanying guidebook</figcaption>
</figure>

## Hiperligações
- <http://fundy-biosphere.ca/en/about-us/the-reserve>
- <http://www.sentiernbtrail.com>
- <http://www.snb.ca/gdam-igec/e/2900e_1.asp>

## Sobre o autor:
<figure>
<img src="../images/canada_brunswickaut.jpg" class="align-left" height="200" alt="canada_brunswickaut.jpg" />
<figcaption>Jarrett Totton</figcaption>
</figure>

A contribuição deste artigo foi feita por Jarrett Totton em Janeiro de 2013. O Jarrett é Técnico SIG que vive em Alberta, Canadá.

{{<content-end >}}
