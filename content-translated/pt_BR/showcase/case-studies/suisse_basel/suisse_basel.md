---
draft: 'true'

---
# QGIS \-\-- an interesting instrument for forestry planning concepts at local and regional level
Almost 35% of Switzerland\'s surface is covered by forests. Changing demands upon the forest and the poor financial situation of forest enterprises in Switzerland led to the development of a new forestry planning concept about fifteen years ago. This concept introduced a clear distinction between planning at the level of the authorities and planning at the level of the owners1. As a new forestry planning office, guaraci works primarily in the region of Basel (Switzerland) on both mentioned planning levels. This case study discusses the use of QGIS at the forest owner level. On this level, a simple, dynamic and compatible geographic information system is required for the establishment of a forest management plan. This plan covers about 1000 ha of forests, will be valid for about 20 years and is implemented by the local forest manager. The area is situated in the region of Basel (see google maps).
## Como o QGIS é usado
Dentro do planeamento de todo o processo, o QGIS foi utilizado para as seguintes quatro tarefas:
- Importação de dados existentes. Os dados incluem mapas de fundo geo-referenciados (\*.tif), juntamente com os arquivos do tipo polígono, linha e ponto. Para o gestor da floresta, a visualização de dados temáticos existentes (por exemplo, os recursos hídricos, solo e água potável, zonas de protecção da natureza) são importantes para o seu trabalho diário.
- Digitizing. The forestry measurements planned by the forest manager had been digitized. The QGIS digitizing tools with the advanced snapping options are very useful and user friendly. The „delimited text" plugin enabled the import of additional data tables.
- Análise. Foram calculadas as áreas das diferentes categorias de medição. A partir de certas características da linha, como trilhos de comboio ou estradas, as florestas de protecção foram determinadas com a ajuda de uma área envolvente dessas linhas.
- Impressão e exportação. O compositor de mapas suporta  criação de um layout para o mapa. O mapa foi exportado em ficheiro PDF e imagem.

![Extract of the forestry measurements map](./images/suisse_basel1.jpg){.align-right}
## Conclusão
QGIS is an interesting tool for small planning offices, such as guaraci, as well as for the forest managers and owners. It can be used in a professional context and the presented output result was appreciated by all parties involved. For the mentioned tasks the present QGIS version 1.4 "Enceladus" offers all necessary GIS tools. The most important qualities of QGIS are the intuitive user interface and the compatibility with different file formats. It is an ideal tool for projects that are on one hand based on existing geographic data and on the other hand require the acquisition of new data. The user-manual is helpful and easy to understand. Both from the technical as well as the financial perspective QGIS is an interesting alternative to other GIS software.
## Perspectiva
As tarefas principais do planeamento florestal podem ser trabalhadas com as ferramentas básicas SIG mencionadas. O Guaraci vai continuar a usar QGIS para o planeamento florestal, a nível do proprietário florestal. Com base nas experiências com o projecto apresentado, o QGIS também pode ser recomendado para conceitos florestais ao nível das autoridades locais. Projectos maiores e mais complexos, com requisitos de análise detalhadas poderiam ser tratadas com a combinação do QGIS com o servidor de base de dados espaciais Postgis. Novas zonas de madeira, bem como florestas reservadas e zonas de protecção podem ser facilmente digitalizadas. Felizmente, os proprietários e gestores florestais utilizarão cada vez mais o potencial do QGIS para seu planeamento anual, bem como a documentação das suas actividades florestais.
## Autor
![Raphael Häner](./images/suisse_baselaut.jpg){.align-left height="200px"}

This article was contributed in June 2010 by Raphael Häner. He is Dipl. Forst Ing. at ETH Zürich, Switzerland and founded his one-man company guaraci in 2009.
