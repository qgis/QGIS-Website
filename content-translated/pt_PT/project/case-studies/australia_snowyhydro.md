---
HasBanner: false
archived: true
date: 2014-08-01
draft: false
featured: false
section: projeto
sidebar: true
thumbnail: images/australia_snowyhydro1.jpg
title: Utilização das Ferramentas de Processamento na automatização da avaliação de
  mantos de neve.
type: case-study

---
{{<content-start >}}
# Utilização das Ferramentas de Processamento na automatização da avaliação de mantos de neve.
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>August 01, 2014</span>
</p>

A Snowy Hydro Limited (SHL) é uma empresa de energia, especializada na produção de electricidade durante os períodos de elevado consumo, com sede nas Montanhas Nevadas, estado de Nova Gales do Sul, Austrália. Apesar de possuir uma variedade de outros recursos de geração de energia espalhados pelo país, a SHL é mais conhecida por tutelar uma parte icónica das infraestruturas australianas deste sector, designada por Plano Hidroeléctrico das Montanhas Nevadas.

O Plano Hidroeléctrico das Montanhas Nevadas só é possível graças à queda sazonal de neve na região alpina de Nova Gales do Sul. A água proveniente do degelo da primavera é utilizada na geração de electricidade para satisfação da procura sentida no mercado nacional de energia, ao mesmo tempo que é distribuída pelas regiões mais secas do interior do sudeste australiano, para fins de irrigação e agricultura.

A avaliação do manto de neve presente nos meses de inverno permite à SHL monitorizar o ciclo de vida das áreas cobertas, mantendo um registo histórico e fornecendo estatísticas às equipas dos serviços hidrográficos que lhes permitem elaborar previsões sobre o armazenamento e fornecimento de água.

<figure>
<img src="../images/australia_snowyhydro1.jpg" class="align-center" height="43400" alt="images/australia_snowyhydro1.jpg" />
<figcaption>Map 1.1 Snowy Water Catchment Map</figcaption>
</figure>

## Fundo
A cada ano, durante os meses de inverno (de 1 de Junho a 31 de Outubro), a SHL obtêm, a partir do sensor MODIS do satélite Terra (EOS AM-1), tantas imagens quantas a cobertura de nuvens lhe permite. Estas imagens alimentam um algoritmo conhecido como Índice de Neve de Diferença Normalizada (NDSI), utilizado na identificação das áreas onde se verifica a presença de neve. Apesar de este algoritmo não ser exclusivo de qualquer sensor em particular, o dispositivo MODIS foi escolhido em virtude da sua adequada resolução espacial e cobertura diária da área em estudo (Mapa 1.1 Bacia Hidrográfica das Nevosas).
## Objectivo
O objectivo deste projecto é automatizar o fluxo de trabalho do NDSI tornando-o num dos modelos das Ferramentas de Processamento do QGIS. Pretende-se obter um polígono que circunscreva o manto de neve sobre a bacia hidrográfica das Nevadas, juntamente com um atributo que represente a área total, calculada em Km².
## Método
O algoritmo NDSI é em si mesmo bastante simples (ver abaixo Fórmula 1.1 - Índice de Neve de Diferença Normalizada (NDSI)) e os passos subsequentes necessários à extracção do índice em formato vectorial encaixam perfeitamente num modelo das Ferramentas de Processamento.

<figure>
<img src="../images/australia_snowyhydro8.png" alt="australia_snowyhydro8.png" />
<figcaption>Formula 1.1 - Normalised Difference Snow Index (NDSI)</figcaption>
</figure>

O algoritmo NDSI devolverá valores compreendidos entre -1 e 1, sendo que valores superiores a 0.4 (limiar típico) são indicadores da presença de neve. Apresenta-se em baixo (Mapa 1.3 - Resultados NDSI)  um exemplo de resultado do NDSI, lado a lado com um imagem a cor natural (Mapa 1.2 - Cor verdadeira MODIS) para o dia 13 de Julho de 2014. As imagens mostram como é fiável o resultado do NDSI na distinção entre áreas cobertas de neve e áreas com outro tipo de cobertura inclusive nuvens. O algoritmo pode todavia enganar-se ao classificar grandes massas de água como neve, dadas as propriedades de absorção da água nas bandas espectrais próximas do infra-vermelho. Esta particularidade do NDSI revela a necessidade da introdução, nalguma fase do modelo,  de um filtro que permita a discriminação da água.

<figure>
<img src="../images/australia_snowyhydro2.jpg" class="align-left" width="300" alt="australia_snowyhydro2.jpg" />
<figcaption>Map 1.2 - MODIS true colour</figcaption>
</figure>

<figure>
<img src="../images/australia_snowyhydro3.jpg" class="align-center" width="300" alt="australia_snowyhydro3.jpg" />
<figcaption>Map 1.3 - NDSI output</figcaption>
</figure>

<figure>
<img src="../images/australia_snowyhydro4.jpg" class="align-left" width="300" alt="australia_snowyhydro4.jpg" />
<figcaption>Map 1.4 - Recoded "Snow" vs "Non snow"</figcaption>
</figure>

The NDSI output is created with some very simple band map by using the GRASS module \"r.mapcalculator\". Once the NDSI grid was available the NDSI threshold of 0.4 needed to be applied and this would result in a boolean grid depicting \"Snow\" and \"Non snow\" areas. To get that classification another GRASS module \"r.recode\" was used and produced the result shown above in Map 1.4 Recoded 'Snow' vs 'Non Snow'.

The recoded grid was then converted to a vector polygon dataset and the snow covered areas were extracted (shown below, Map 1.5 - Extracted snow). The snow covered areas were then clipped to the Snowy Water Catchment (shown below, Map - 1.6 Snow inside the SWC), then the large water bodies are masked out (shown below, Map 1.7 - Final snow covered area), and finally the area statistics for the snow covered area is generated.

<figure>
<img src="../images/australia_snowyhydro5.jpg" class="align-left" width="300" alt="australia_snowyhydro5.jpg" />
<figcaption>Map 1.5 - Extracted Snow</figcaption>
</figure>

<figure>
<img src="../images/australia_snowyhydro6.jpg" class="align-center" width="300" alt="australia_snowyhydro6.jpg" />
<figcaption>Map 1.6 - Snow inside the SWC</figcaption>
</figure>

<figure>
<img src="../images/australia_snowyhydro7.jpg" class="align-left" width="300" alt="australia_snowyhydro7.jpg" />
<figcaption>Map 1.7 - Final snow covered area</figcaption>
</figure>

The output from the model is a vector polygon showing the snow covered area within the Snowy Water Catchment. The attributes of the polygon include the area covered by the snow and the percentage of the catchment that is covered. The model in its entirety can be seen below in \"Image 1.1 - Normalised Difference Snow Index (NDSI) QGIS processing toolbox model\".

<figure>
<img src="../images/australia_snowyhydro.png" class="align-center" width="600" alt="australia_snowyhydro.png" />
<figcaption>Image 1.1 - Normalised Difference Snow Index (NDSI) QGIS processing toolbox model</figcaption>
</figure>

## Resultados/Conclusão
As Ferramentas de Processamento do QGIS constituem um poderoso recurso de automatização de fluxos de trabalho (tarefas de dependência hierarquizada), como o da avaliação de mantos de neve. O modelo acima apresentado automatiza eficazmente o processo de avaliação da presença de neve e fornece um conjunto de dados de informação geográfica apropriados a representação gráfica bem como posterior utilização em aplicações estatísticas. É bem sucedido na remoção de erros subjectivos associados a outros métodos anteriormente utilizados na SHL, impondo-se como uma ferramenta de avaliação com características de consistência e reprodutibilidade.
### Sobre o autor:
Andrew Jeffrey é analista SIG na empresa Snowy Hydro Limited sediada em Cooma, estado de Nova Gales do Sul, Austrália. Terminou a sua licenciatura (Bsc) em 2004, na Universidade Charles Sturt de Wagga Wagga, com uma especialização em Sistemas de Informação Espacial. Na SHL, ao mesmo tempo que desempenha as comuns tarefas diárias, também proporciona informação geográfica de suporte a projectos entusiasmantes como o da Chuva Artificial.

{{<content-end >}}
