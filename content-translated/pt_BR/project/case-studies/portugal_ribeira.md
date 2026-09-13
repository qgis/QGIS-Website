---
HasBanner: false
archived: true
date: 2012-07-01
draft: false
featured: false
section: projeto
sidebar: true
thumbnail: images/portugal_ribeira1.png
title: O uso do QGIS e GRASS para modelação de corredores ecológicos para lobos no
  Norte de Portugal
type: case-study

---
{{<content-start >}}
# O uso do QGIS e GRASS para modelação de corredores ecológicos para lobos no Norte de Portugal
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>July 01, 2012</span>
</p>

The Iberian wolf is a sub-species of the gray wolf that exists only in north of Portugal and Spain, with small isolated groups in the south of Douro river. During the last century, it suffered a high regression, being a "vulnerable" species in Spain and "endangered" in Portugal. Nowadays, there are only around 300 wolves in Portugal, due to the high persecution, destruction and fragmentation of the habitat.

<figure>
<img src="../images/portugal_ribeira1.png" class="align-right" alt="portugal_ribeira1.png" />
<figcaption>Study area in Portugal</figcaption>
</figure>

Ribeira de Pena é um Concelho que pertence ao Distrito de Vila Real, no Norte de Portugal. É um Município rural, caracterizado pela agricultura, pastoreio, floresta, montanhas, vales e a mais diversa fauna, juntamente com baixa densidade humana, o que em conjunto providenciam abrigo e comida para os lobos. Localizada entre as zonas montanhosas de Trás-os-Montes e o verde Minho, Ribeira de Pena é um dos Concelhos que pode funcionar como corredor ecológico entre as áreas com maiores densidades de lobo a Norte e as áreas com menor concentração a Sul. 

Eu comecei a utilizar softwares SIG durante o meu curso de biologia, aprofundando conhecimentos durante o mestrado. Na altura utilizei maioritariamente programas proprietários, cujo acesso perdi após ter terminado o mestrado. 

Entretanto tive o meu primeiro contacto com os sistemas operativos Linux. E logo depois fui contactada para ajudar uns investigadores na modelação de corredores ecológicos para lobos em Ribeira de Pena, utilizando SIG. O meu primeiro problema prendeu-se com a escolha do programa a utilizar, visto que já tinha substituído o sistema operativo para Linux. Foi na altura em que ouvi falar no QGIS e decidi experimentar, sendo que me parecia um programa muito simplista e incompleto, quando comparado ao que eu já conhecia. Depressa percebi que estava errada, e fiquei bastante entusiasmada com as capacidades analíticas que o QGIS oferecia, especialmente quando integrado com o GRASS.

Para modelar os corredores ecológicos, usámos o QGIS com o módulo GRASS. Usámos muita informação geográfica juntamente com dados de avistamentos de espécies para modelar os corredores ecológicos. Aqui estão algumas funções do QGIS e GRASS que usámos neste caso, apenas nomeando alguns:
- módulo de Interpolação no QGIS: para criar o Modelo Digital do Terreno
- r.watershed no GRASS: para criar as linhas de água do MDT
- r.grow.distance no GRASS: gera um mapa raster de distância para os elementos da camada de entrada
- r.reclass no GRASS: para reclassificar as camadas do mapa
- r.slope.aspect.slope no GRASS: para calcular o declive a partir do MDT
- r.mapcalculator no GRASS: para calcular alguma algebra simples de mapas
- r.cost.coord no GRASS: crua um mapa raster exibindo o custo cumulativo de mudanças entre diferentes localizações geográficas no mapa raster de entrada onde os valores das suas células representam o custo
- r.drain in GRASS: Traces a flow through an elevation model on a raster map — the one used to create the corridors

Com este trabalho obtivemos um mapa com zonas potenciais a corredores ecológicos para lobos no município da Ribeira da Pena. Estas áreas deverão ser consideras pela técnicos municipais aquando do planeamento de medidas de conservação para estas espécies. estes corredores são de extrema importância porque podem ligar as frágeis alcateias de lobos do sul com o norte de Vila Real, que são contínuos com os que vêm da Peneda-Gerês e Espanha onde são mais estáveis. É de extrema importância estes corredores que cruzam áreas sociais, como pequenas aldeias, cidades e rede viária. Estas áreas devem ser consideradas críticas para conservação do lobo, e aplicar medidas para reduzir o impacto humano nestas espécies.

<figure>
<img src="../images/portugal_ribeira2.png" class="align-right" style="width:100.0%" alt="portugal_ribeira2.png" />
<figcaption>Ecological corridors and critical conservation areas for wolves in northern Portugal.</figcaption>
</figure>

## Conclusão
Both QGIS and plugin GRASS are very intuitive with user-friendly interface, with all essential functions to perform most analysis. For what I could see, QGIS and GRASS perform equally as well as the proprietary programs I was most familiar with from college days, with the big advantage of free open-source software, usable in every computer or notebook without licenses, constant upgrades and the ultimate advantage to contribute to it\'s improvement and/or tip the developers about some essential function.

Changing to Linux and then to QGIS and GRASS was one of my best calls, and although there can be some missing issues, easily resolved in the future with the developers, I don\'t regret my decision and advise everyone to use them.
## Autor
<figure>
<img src="../images/portugal_ribeiraaut.png" class="align-left" height="200" alt="portugal_ribeiraaut.png" />
<figcaption>Monica Almeida</figcaption>
</figure>

Este artigo foi contribuído em Julho de 2012 pela Mónica Almeida. Ela é uma bióloga de conservação que trabalha numa organização não governamental de preservação do lobo em Portugal.

{{<content-end >}}
