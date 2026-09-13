---
draft: 'true'

---
# Mapeamento com o QGIS do habitat e avifauna da Reserva Florestal de Amurum na Nigéria
A reserva florestal Amurum está localizada perto da cidade de Jos, estado de Plateau, Nigéria. Foi estabelecido conjuntamente com a iniciação do A.P Instituto de Investigação Ornitológica Leventis (APIIOL) com o propósito da conservação natural, educação e investigação. APIIOL está sediada no Departamento de Zoologia da Universidade de Jos. Anualmente um grupo de cerca de oito alunos altamente motivados de toda a Nigéria obtêm formação em biologia de conservação, estatística (com R) e a partir de 2011 também nos SIG. Durante duas semanas em dezembro de 2011 foram estudados os conceitos básicos dos SIG e aplicados com recurso ao QGIS para diversos fins de conservação. Neste artigo vamos descrever a maneira pela qual usamos QGIS para mapear os habitats e seus objectivos na reserva Amurum e como os mapas básicos de habitat foram usados para obter extractos com a finalidade de determinar de forma eficiente a distribuição espacial da avifauna, incluindo a biodiversidade.

![Training Group](./images/nigeria_jos1.jpg){.align-right}
## Mapeamento da elevação, sombreamento, declive e habitats
1) Mapping elevation and groundtruthing: We downloaded (free) elevation data originating from the NASA Shuttle Radar Topographic Mission (SRTM) for the area in which Amurum is located. (Information about the global elevation data set can be found here: <http://www.cgiar-csi.org/data/elevation/item/45-srtm-90m-digital-elevation-database-v41>).
2) As Ferramentas Gdal foram usadas para juntar os conjunto de dados originais e cortar uma área menor contendo a reserva para que os conjuntos de dados raster ficassem relativamente pequenos. Com o GPS recolhemos elevações em várias localizações da reserva.
3) No geral, as elevações do conjunto de dados SRTM corresponderam bem às elevações recolhidas pelo gps. Os Modelos de terreno no GdalTools foram utilizados para calcular o ensombramento e declives para a área. Essas variáveis ​​são importantes do ponto de vista ecológico, porque eles estão fortemente associados com o tipo de habitat.

![QGIS screenshot](./images/nigeria_jos2.jpg){.align-right}
4) Uma vez que a intenção será desenvolver um mapa de boa aparência, nós interpolámos o mapa de elevação original (cortado) para obter um mapa de alta resolução. Nós usamos a ferramenta warp no GdalTools. Pela ferramenta de contorno obtivémos linhas de contorno suaves.
5) As coordenadas do limite da reserva foram obtidos a pé ao longo dos limites da reserva, com um GPS. Os pontos de passagem e trilhos armazenadas no GPS foram facilmente importados usando as ferramentas de GPS. Os pontos de passagem e trilhos importados foram usados para construir uma shapefile do tipo polígono. Os trilhos dentro da reserva foram mapeados numa forma semelhante.
6) Fomos capazes de construir com rapidez e precisão um mapa habitat de Amurum usando uma imagem de satélite do Google que temos na área de trabalho com o módulo OpenLayers. A reserva tem três tipos de habitat distintos: savana, floresta de galeria e afloramento rochoso. Com base na imagem de satélite foi utilizado o editor para desenhar polígonos que delimitam os três habitats. Definiu-se as opções de atracção correctamente que permitiu a construção dos polígonos sem sobreposição.

## Mapeamento da distribuição dos pássaros e a sua diversidade
Os mapas de habitats foram usados para gerar localizações aleatórias. A área de vários tipos de habitats foram usados para gerar um número de localizações proporcionais à superfície para cada tipo de habitat (estratificação).

![Training Group](./images/nigeria_jos3.jpg){.align-right}

The random points in fTools were used for this purpose. All the locations were visited during two mornings by four groups of students (2 per group) giving a total of 38 random locations dispersed throughout the reserve. The observation data were entered in a spreadsheet and analyzed using R. In addition, the Shannon-Wiener diversity index was calculated using R. After merging the location file with the resulting observation data it was exported as a csv file which was loaded into QGIS using the "Add delimited text layer" tool. On the basis of the above mentioned layers a map was constructed presenting some of the most important landscape features and avian diversity of the Amurum reserve.
## Conclusão
Overall, the course was a great success. We - a group of students with no previous GIS experience \-\-- enjoyed working with QGIS a lot. Within just two weeks time we were able to develop an extremely useful map of the reserve. Amongst others, the extents of the various habitats were determined which allows for stratification and thus for better estimates of abundances of various kinds of organisms. Basically we are now able to do better ecological research using QGIS as an open source platform.

![QGIS map: Diversity of Amurum Forest Reserve](./images/nigeria_jos4.png){.align-right}
## Autores
Abengowe Elmond Chiadikaobi, Adeyanju Temidayo Esther, Akiemen Nerioya, Albert Malangale Tauje, Azi Abok Joel, Echude Daniel, Eelke Folmer, Nwaogu Chima Josiah, Onoja Joseph Daniel, Yadok Biplang Godwill
