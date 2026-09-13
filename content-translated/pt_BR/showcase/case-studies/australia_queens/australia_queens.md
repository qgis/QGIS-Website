---
draft: 'true'

---
# QGIS e GRASS no Mapeamento do perigo de incêndios florestais pelo Governo Local
## Introdução
O Conselho Regional Centro Sul (SDRC) é um governo local de pequeno-a-médio porte no sudeste de Queenland, Austrália. O conselho regional principalmente na parte sul, sofre de grandes incêndios florestais. Incêndio florestal é uma preocupação real e presente para os moradores e proprietários de terra na Região Centro Sul, e já resultou na perda de vidas e bens.

Este projeto irá permitir que o Conselho e as pessoas da região a serem mais conscientes do risco e permitir uma melhor tomada de decisão no futuro.

![](./images/australia_queens1.jpg){.align-right}
## O Projeto
As bushfire is not only a problem for SDRC but also for the whole of Queensland, the state government requires that each local government identifies the bushfire hazard in their area via the State Planning Policy 1/03 Mitigating the Adverse Impacts of Flood, Bushfire and Landslide \[1\]. This kind of job would normally be done using consultants but was instead done by the council itself using a combination of QGIS and GRASS.

A componente SIG do projeto está dividida em 6 etapas principais
- Avaliação da declividade e o seu mapeamento
- Avaliação da exposição e o seu mapeamento
- Avaliação da vegetação e o seu mapeamento
- Combinação de resultados para identificar a severidade do perigo de incêndio florestal
- Verificação no campo e avaliação qualitativa
- Mapas Finais

## O uso do QGIS e GRASS
![](./images/australia_queens2.jpg){.align-right}

QGIS, using the GRASS plugin, was selected as it provided the tools needed to complete the job and the interaction between QGIS and GRASS made it easy to process the raster maps and present them in a meaningful way to users. SDRC uses MapInfo for its main GIS system, however MapInfo's addons were not as powerful as GRASS GIS for raster processing.

O plugin QGIS GRASS foi usado para importar 5 metros de contornos de toda a região para o GRASS, que foram então convertidos em um mapa de contorno raster usando r.surf.contour. Uma inclinação e o aspecto do mapa foram então gerados utilizando r.slope.aspect do mapa de contorno raster. Categorias foram atribuídas a diferentes faixas de declividade e aspecto e tendo em conta um risco de perigo. Áreas de vegetação foram também dadas diferentes pontuações de risco. Todos os mapas raster resultantes foram então combinados utilizando mapcalc e dado uma pontuação final de risco. As pontuações de risco são divididas em três categorias principais: alta; média; e baixa.

A parte final do processo era a verificação em campo através do serviço de incêndio rural. Após o processo de revisão, QGIS foi usado para imprimir os mapas finais para a apresentação.

Como todos os comandos GRASS podem ser executados a partir da linha de comando, todos os comandos que foram necessários para gerar os mapas de risco de incêndio foram guardados, para fins de documentação e se for necessário regerar os mapas em algum momento no futuro.
## Conclusão
Em geral QGIS, juntamente com o plugin GRASS, cria uma grande experiência e um grande resultado final para o Conselho a fazer o seu próprio mapeamento de risco de incêndios florestais. O plugin GRASS fornece uma interface muito fácil de usar para GRASS através QGIS. Como QGIS é capaz de abrir o formato GRASS raster nativamente, a integração é muito transparente e mapas podem ser feitos com facilidade.

The project won an encouragement award at the Queensland Planning Institute of Australia state planning awards in 2010 \[2\]
## Referências
- \[1\] <http://www.emergency.qld.gov.au/publications/spp/>
- \[2\] <http://digital.crowtherblayne.com.au/default.aspx?xml=crowther_pia.xml>

## Autor
![Nathan Woodrow](./images/australia_queensaut.jpg){.align-left height="200px"}

A submissão deste artigo foi feita por Nathan Woodrow em Janeiro de 2011. O Nathan é Técnico SIG no Concelho Regional do Sothern Downs e está cursando uma licenciatura associada à Ciência Espacial na Universidade de Queensland Sul
