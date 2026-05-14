---
draft: 'true'

---
# QGIS e GRASS no Mapeamento do Perigo de Incêndios Florestais no Governo Local
## Introdução
O Conselho Reginal de Southern Downs (RCSD) é um pequeno a médio governo local no sudeste de Queenslanda, Austrália. A região concelhia, situada principalmente na parte sul, sofre de grandes incêndios florestais. Os incêndios são reais e presentes na preocupação dos residentes e proprietários do Sul da Região de Southern Downs, e tem resultado na perda de vidas e propriedades. 

Este projeto irá permitir ao concelho e às pessoas da região estarem mais atentas ao risco e permitir uma melhor tomada de decisão do futuro.

![](./images/australia_queens1.jpg){.align-right}
## O Projeto
As bushfire is not only a problem for SDRC but also for the whole of Queensland, the state government requires that each local government identifies the bushfire hazard in their area via the State Planning Policy 1/03 Mitigating the Adverse Impacts of Flood, Bushfire and Landslide \[1\]. This kind of job would normally be done using consultants but was instead done by the council itself using a combination of QGIS and GRASS.

A componente SIG do projeto está dividida em 6 etapas principais
- Avaliação do Declive e o seu mapeamento
- Avaliação da Exposição e o seu mapeamento
- Avaliação da vegetação e o seu mapeamento
- Combinação de resultados para identificar a severidade do perigo de incêndio florestal
- Verificação no campo e avaliação qualitativa
- Mapas Finais

## O uso do QGIS e GRASS
![](./images/australia_queens2.jpg){.align-right}

QGIS, using the GRASS plugin, was selected as it provided the tools needed to complete the job and the interaction between QGIS and GRASS made it easy to process the raster maps and present them in a meaningful way to users. SDRC uses MapInfo for its main GIS system, however MapInfo's addons were not as powerful as GRASS GIS for raster processing.

A extensão GRASS do QGIS foi usado para importar curvas de nível com intervalos de 5 metros de toda a região para o GRASS que foram então convertidas num superfície raster usando r.surf.contour. O declive e a exposição foram geradas usando o r.slope.aspect do mapa de superfície raster. Foram atribuídas Categorias a diferentes intervalos de declive e exposição e valores de risco diferentes tendo em conta o perigo. As áreas de vegetações também receberam diferentes valores de risco. Todos os mapas raster resultantes foram então combinados usando mapcalc e foi atribuída uma avaliação final de perigo e risco. Os valores de risco são, então, divididos em três categorias principais: alta, média e baixa.

A parte final do processo foi a verificação no campo através do serviço de incêndio rural. Após o processo de revisão, o QGIS foi usado para imprimir os mapas finais para apresentação.

Como todos os comandos do GRASS podem ser executados a partir da linha de comando, todos os comandos que foram necessários para gerar os mapas de risco incêndios florestais foram registados, para fins de documentação e se for necessário para uma futura geração dos mapas.
## Conclusões
No Geral, o QGIS juntamente com a extensão GRASS, proporcionou uma grande experiência e um grande resultado final para o conselho para fazer o seu próprio mapeamento de risco de incêndios florestais. A extensão GRASS oferece uma interface fácil de usar através QGIS. Como QGIS é capaz de abrir o formato raster do GRASS nativamente, a integração é muito transparente e os mapas podem ser feitas com facilidade. 

The project won an encouragement award at the Queensland Planning Institute of Australia state planning awards in 2010 \[2\]
## Referências
- \[1\] <http://www.emergency.qld.gov.au/publications/spp/>
- \[2\] <http://digital.crowtherblayne.com.au/default.aspx?xml=crowther_pia.xml>

## Sobre o autor:
![Nathan Woodrow](./images/australia_queensaut.jpg){.align-left height="200px"}

A contribuição deste artigo foi feita pelo Nathan Woodrow em Janeiro de 2011. O Nathan é Técnico SIG no Concelho Regional do Sothern Downs e está a estudar uma licenciatura associada à Ciência Espacial na Universidade de Queensland Sul
