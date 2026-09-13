---
draft: 'true'

---
# Usando o QGIS para planejamento de rede FTTH / GPON devido à Agenda Digital Europeia
## Definição do problema
Nos últimos anos, muitos países da UE lançaram programas operacionais para implementar a Agenda Digital Europeia (EAC) desenvolvida pela Comissão Europeia em 2010. De acordo com as suas diretrizes até 2020, todos os cidadãos da União Europeia devem ter acesso a largura de banda de Internet de 30 Mbps e menos da metade deles terá acesso a largura de banda não inferior a 100 Mbps.

A Polônia é um dos países em que a Agenda está sendo implementada. Graças aos fundos da União Europeia, muitos operadores locais podem competir com os grandes fornecedores de telecomunicações no que diz respeito aos serviços de banda larga de alta velocidade. Infelizmente, a solicitação de financiamento requer um grande trabalho necessário para elaborar a documentação apropriada, incluindo, entre outras coisas, o desenvolvimento de mapas conceituais da rede FTTH (Fiber To The Home) planejados.

Além disso, atualmente não há ferramentas de TI baseadas em SIG disponíveis para apoiar os possíveis beneficiários com a preparação da documentação. The complexity of the problem is even more complicated by the fact tht such a software should enable a creation of documentation in accordance with specific program guidelines (e.g. the obligation to connect educational institutions).

Como temos uma vasta experiência no setor de telecomunicações, as entidades que solicitam fundos da UE nos pediram para criar software de apoio ao desenvolvimento do mapa conceitual da rede FTTH. Os produtos gerados pelo software desenvolvido foram para acelerar significativamente o processo de preparação da aplicação.
## Descrição da solução
Devido à alta popularidade, ampla disponibilidade, abertura do software e imensas habilidades funcionais, pareceu natural selecionar o QGIS como plataforma para servir como base para nossa solução.

De acordo com as diretrizes do FTTH Council Europe, é crucial primeiro preparar um plano considerando tanto o aspecto técnico (colocação de cabos, fechamento de splice, divisores) quanto o aspecto econômico (demanda) baseado em dados reais de pontos de endereçamento. A estrutura do edifício e a densidade do desenvolvimento do edifício determinam a tecnologia do projeto de rede GPON (Gigabit Passive Optical Network). Para ter a capacidade de planejar a topologia de rede com eficiência, é necessário ter entre outras coisas:
- acesso a dados SIG,
- automação de processamento de dados SIG,
- aplicação de algoritmos de otimização de rede,
- aplicação de regras de engenharia de rede GPON.

Todos esses itens foram conectados na plataforma QGIS. Abaixo, há uma breve descrição de como percebemos o projeto e quais itens funcionais foram incorporados para criar uma solução.

Para atingir nosso objetivo, precisávamos de poucos componentes funcionais além da plataforma SIG padrão:
- GRASS - uma coleção de algoritmos vetoriais e de rede,
- Complementos QGIS - OpenLayer, QuickOSM, Clustering Scipy Point, WorkContextTracer (nosso complemento),
- QGIS modeler -- tool for graphical flow modelling,
- SpatiaLite - um banco de dados local para armazenar dados de entrada e saída.

The entire solution was based on the concept of so called wizards which realize the process of preparing the FTTx network technical concept step by step. Using \'geoprocessing\' modeller, we created models requiring only the necessary input data from operator. Algorithmic complexity was encapsulated within models in the form of designed flow, which use existing QGIS algorithms and calls dedicated scripts.

![](./images/poland_ffth/toolbox.png){.align-left}

Para evitar que os resultados das análises subsequentes se misturassem, fornecemos um complemento chamado WorkContextTracer, que agrupa nosso trabalho nos chamados contextos de trabalho.

![](./images/poland_ffth/workorder.png){.align-left}

Algoritmos de rede baseados nas funções gráficas disponíveis no GRASS foram enriquecidos pela adição de scripts de telecomunicação. Introduzimos um conceito de agrupamento de demanda que permite usar métodos K-means e hierárquicos para agregar pontos de demanda.

Geoprocessing scripts with usage of cable routing layer and Djikstra algorithm develops a cable route proposal with optical fiber nodes\' locations.

Os operadores também precisavam de uma associação entre nós da rede criados e pontos de endereço para estimar o custo individual de cada ramificação da rede. Para completar esta tarefa, criamos scripts que realizam esta operação armazenando os resultados no banco de dados SpatiaLite local. Os dados precisavam ser exportados para a planilha, então usamos a biblioteca de software livre para atender a esse requisito.
## Como os usuários usaram ferramentas para criar o plano de rede FTTH / GPON
O usuário iniciou o trabalho abrindo um novo contexto de trabalho e especificando uma camada de entrada de pontos de endereço a ser analisada. Usando a interface QGIS padrão, o usuário poderia estabelecer um conjunto de demandas nos pontos de endereço e, finalmente, fornecer os parâmetros necessários para etapas adicionais do algoritmo.

![](./images/poland_ffth/step1_inputlayer.png){.align-left}

Sem ter informações sobre a infra-estrutura civil existente, uma rede rodoviária da OpenStreet devidamente filtrada era usada como uma camada de roteamento. Os algoritmos do Scipy alimentados com parâmetros de entrada agrupavam os pontos de endereço em agregados de demanda, marcando-os com cores separadas, indicando sua atribuição a determinado grupo.

![](./images/poland_ffth/step1.png){.align-left}

Tendo todos os pontos de endereço agrupados, o usuário iniciou as etapas do planejamento de rede de alto nível, fornecendo camadas preparadas nas etapas anteriores e uma camada com o ponto inicial da rede GPON.

![](./images/poland_ffth/step1-2_result.png){.align-left}

Upon the completion of the algorithm, in QGIS there are geometry objects representing planned cables and splice closure locations. Basing on demand data and network topology, an additional information is stored in database such as the length of the cable, its profile, node's serving areas.

![](./images/poland_ffth/step4_results.png){.align-left}

Nesta fase, o usuário já tinha todas as partes da informação para desenvolver um conceito técnico de rede FTTx de alto nível. A parte final foi a geração da planilha de relatório de dados mostrando todos os dados calculados de várias perspectivas diferentes.

![](./images/poland_ffth/report_generated.png){.align-left}

![](./images/poland_ffth/report_generated_and_tranformed.png){.align-left}
## Conclusão
Graças à utilização da plataforma QGIS, bem como às suas capacidades de extensão, conseguimos desenvolver uma solução de código aberto gratuito que permite aos operadores de telecomunicações prepararem os documentos necessários para apresentar pedidos de co-financiamento no programa da UE que implementa a Agenda Digital Europeia.

Combinando algoritmos flexíveis de vetores com os scripts de engenharia de telecomunicações, permitimos o uso prático de algoritmos matemáticos na solução de problemas reais relacionados ao planejamento de redes de telecomunicações. O usuário opera em um escopo de dados compreensível (município, prédio, rodovia), enquanto a transformação dessas informações em um modelo matemático é ocultada do usuário.

O usuário tem muitos benefícios úteis:
- Desenvolvimento automático do plano de rede GPON com base em dados publicamente disponíveis e regras de engenharia de tecnologia GPON.
- Capacidade de personalizar ferramentas com diretrizes específicas do programa da UE em um determinado país.
- A grande precisão dos resultados correspondentes às dimensões reais.
- Geração de dados necessários para solicitar fundos da UE: mapa conceitual da rede, relatório de fechamento de cabo e emenda com atribuição de áreas de serviço.
- Possibilidade de determinar com precisão os custos de construção e depreciação de cada parte da rede com o cálculo do custo de conexão de cada ponto de endereço
- Possibilidade de priorizar pontos de endereço dos mais lucrativos para os não lucrativos.
- Possibilidade de avaliar indicadores econômicos básicos como ROI, NPV.

## Links úteis e bibliografia
- <http://europa.eu/rapid/press-release_MEMO-10-200_en.htm> - information on European Digital Agenda
- <http://www.ftthcouncil.eu/> - FTTH Council Europe website
- <https://www.scipy.org/> - SciPy project website
- <https://ksavinetworkinventory.com/en/download-geospatial-network-inventory-free/>
  - tool download webpage.

## Autores
A solução é uma ferramenta de código aberto totalmente gratuita. Faz parte de um projeto maior baseado em plataformas QGIS e FreeCAD que tem a intenção de ser usado no setor de telecomunicações.

The author of this QGIS based solution is Softelnet (<https://www.softelnet.com>), a company manufacturing and integrating software for the telecommunications industry for over 15 years.
