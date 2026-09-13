---
draft: 'true'

---
# Usando a caixa de ferramentas para automatizar o processamento de classificação de neve
Snowy Hidro Limited (SHL) é um gerador de eletricidade de pico com base nas montanhas nevadas de New South Wales, Austrália. Apesar de possuir uma variedade de ativos de geração em todo o país, a Hydro Snowy Limited é o mais conhecido para a custódia de uma peça icónica de infra-estrutura australiano, o Snowy Mountains Hydro Electric Scheme.

O Snowy Mountains Hydro Electric Scheme, é possível graças a neve sazonal que cai na região alpina de New South Wales. A água do degelo da neve da primavera é usada para gerar eletricidade endereçando o pico de demanda no mercado nacional de energia, ao mesmo tempo, desviando a água para as zonas mais secas do interior do sul da Austrália oriental para irrigação e agricultura.

Classificando a cobertura de neve durante os meses de inverno permite SHL para monitorar o ciclo de vida de uma área coberta de neve, do arquivo de registros históricos das áreas cobertas, e fornecer estatísticas de cobertura para a equipe de serviços hidrográficos para previsões de rendimento e armazenamento de água.

![Map 1.1 Snowy Water Catchment Map](images/australia_snowyhydro1.jpg){.align-center height="43400px"}
## Fundo
Cada ano, durante os meses de inverno (1 de Junho a 31 de Outubro) SHL obtém o maior número de imagens livres de nuvens quanto possível do satélite MODIS Terra (EOS AM). Estas imagens são então ingerida em um algoritmo conhecido como a diferença normalizada de Índice de neve  (NDSI), que é usado para indicar as áreas onde a neve está presente. Embora este algoritmo não é único para qualquer sensor particular, o instrumento MODIS foi escolhido devido à sua adequada resolução espacial e cobertura diária da área do projeto (Mapa 1.1 Represa de Água da Neve).
## Objetivo
O objetivo deste projeto é automatizar o fluxo de trabalho NDSI como um modelo na caixa de ferramentas de processamento de QGIS. A saída necessária é um vetor polígono que mostra a extensão coberta de neve dentro da Represa de Água da Neve, juntamente com a atribuição descrevendo a área total coberta em quilômetros quadrados.
## Método
O algoritmo NDSI em si é bastante simples (mostrado abaixo na Fórmula 1.1 - Diferença Normalizada Índice de Neve (NDSI)) e os passos subsequentes necessários para extrair a cobertura de neve em um formato vetorial também se presta muito bem para um modelo de processamento da caixa de ferramentas.

![Formula 1.1 - Normalised Difference Snow Index (NDSI)](./images/australia_snowyhydro8.png)

Este algoritmo NDSI rá retornar resultados entre -1 e 1, com o limiar para a neve sendo tipicamente valores superiores a 0,4. Um exemplo da saída NDSI é mostrado abaixo (Mapa 1.3 - saída NDSI), uma imagem a cores naturais (Mapa 1.2 - cores naturais MODIS) para o 13 de julho de 2014. Como pode ser visto a partir dessas imagens a saída NDSI é muito boa em discriminar áreas cobertas de neve de outros tipos de cobertura da terra e nuvens. No entanto, pode classificar erroneamente porções de grandes massas de água como a neve, causadas por água com características de absorção na parte de infravermelho próximo do espectro. Esta característica do NDSI indica a necessidade de incorporar uma máscara de água em algum estágio no modelo.

![Map 1.2 - MODIS true colour](./images/australia_snowyhydro2.jpg){.align-left width="300px"}

![Map 1.3 - NDSI output](./images/australia_snowyhydro3.jpg){.align-center width="300px"}

![Map 1.4 - Recoded \"Snow\" vs \"Non snow\"](./images/australia_snowyhydro4.jpg){.align-left width="300px"}

The NDSI output is created with some very simple band map by using the GRASS module \"r.mapcalculator\". Once the NDSI grid was available the NDSI threshold of 0.4 needed to be applied and this would result in a boolean grid depicting \"Snow\" and \"Non snow\" areas. To get that classification another GRASS module \"r.recode\" was used and produced the result shown above in Map 1.4 Recoded 'Snow' vs 'Non Snow'.

The recoded grid was then converted to a vector polygon dataset and the snow covered areas were extracted (shown below, Map 1.5 - Extracted snow). The snow covered areas were then clipped to the Snowy Water Catchment (shown below, Map - 1.6 Snow inside the SWC), then the large water bodies are masked out (shown below, Map 1.7 - Final snow covered area), and finally the area statistics for the snow covered area is generated.

![Map 1.5 - Extracted Snow](./images/australia_snowyhydro5.jpg){.align-left width="300px"}

![Map 1.6 - Snow inside the SWC](./images/australia_snowyhydro6.jpg){.align-center width="300px"}

![Map 1.7 - Final snow covered area](./images/australia_snowyhydro7.jpg){.align-left width="300px"}

The output from the model is a vector polygon showing the snow covered area within the Snowy Water Catchment. The attributes of the polygon include the area covered by the snow and the percentage of the catchment that is covered. The model in its entirety can be seen below in \"Image 1.1 - Normalised Difference Snow Index (NDSI) QGIS processing toolbox model\".

![Image 1.1 - Normalised Difference Snow Index (NDSI) QGIS processing toolbox model](./images/australia_snowyhydro.png){.align-center width="600px"}
## Resultados/Conclusão
A caixa de ferramentas de processamento de QGIS é uma maneira poderosa para automatizar o fluxo de trabalho, como essa classificação de neve. O modelo mostrado acima automatiza com sucesso o processo de classificação da neve, e oferece um conjunto de dados SIG que podem ser utilizados para a visualização e de entrada em outras aplicações estatísticas. Ele remove com sucesso erro subjetivo do usuário associado a métodos anteriores usados pelo SHL, enquanto fornece uma ferramenta de classificação repetitível e consistente. Alguns resultados sazonais pode ser vistos aqui.
### Autor
Andrew Jeffrey é um Analista SIG da Snowy Hydro Limited com sede em Cooma NSW, na Austrália. Ele se formou na Universidade Charles Sturt em Wagga Wagga em Bacharel de Ciência (BSC) com especialização em sistemas de informação espacial em 2004. Enquanto em Snowy Hidro Limited ele tem sido capaz de fornecer apoio espacial para projetos emocionantes, como o experimento de semeação de nuvens, e as operações do dia a dia dentro da organização.
