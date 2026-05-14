---
HasBanner: false
draft: false
releaseDate: '2014-06-27'
section: projeto
sidebar: true
title: Ficheiro de alterações para o QGIS 2.4
type: visual-changelog

---
{{<content-start >}}
# Ficheiro de alterações para o QGIS 2.4{#changelog24 }
Release date: 2014-06-27

Registo de alterações para o próximo lançamento do QGIS 2.4.0. A ênfase deste lançamento foi dada essencialmente no aperfeiçoamento e no desempenho - adicionámos várias novas funções, pormenores e melhorias de modo a tornar o interface mais congruente e visualmente mais profissional (esperamos que de mais fácil uso também). O Editor (usado na criação de mapas prontos a imprimir) foi um dos pontos mais focados para torná-lo numa plataforma mais viável na criação de cartografia de qualidade superior.

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

Gostaríamos de agradecer aos programadores, escritores de documentação, testers e todos aqueles que disponibilizaram o seu tempo e esforço (ou que financiaram quem o fizesse).

From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

Finalmente, gostaríamos de agradecer aos nossos patrocinadores oficiais pelo suporte financeiro de valor inestimável que fornecem a este projeto:
- GOLD Sponsor: [Asia Air Survey, Japan](http://www.asiaairsurvey.com/)
- SILVER Sponsor: [G.A.I.A. mbH, Germany](http://www.gaia-mbh.de/)
- SILVER Sponsor: [State of Vorarlberg, Austria](http://www.vorarlberg.at/)
- BRONZE Sponsor: [www.molitec.it, Italy](http://www.molitec.it/)
- BRONZE Sponsor: [www.argusoft.de, Germany](http://www.argusoft.de)
- BRONZE Sponsor: [www.openrunner.com, France](http://www.openrunner.com)
- BRONZE Sponsor: [www.eschenlaub.de, Germany](http://www.eschenlaub.de)

A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors).

If you would like to make a donation or sponsor our project, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. QGIS is Free software and you are under no obligation to do so. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts.

{{<table-of-contents >}}
## Geral
### Feature: Generate band name with NetCDF EXTRA_DIM
O NetCDF fornece informação extra dimensional. Esta informação fornece metadados de cada banda. Esses metadados podem ser usados para explicar o nome de cada banda. Por exemplo, as bandas do ficheiro NetCDF representam a temperatura numa dada profundidade. Para o utilizador, é mais fácil selecionar com informação de profundidade, em vez de apenas o número da banda.

![image1](images/entries/becafd815f152b53503b33048beb8bc95cdfdaf6.webp)
### Funcionalidade: Aplicação de escala e afastamento a dados raster
Em algumas fontes de dados raster, os dados são armazenados como inteiro com uma escala e um afastamento nos metadados. A escala e o afastamento podem ser usados para obter os dados corretos. O QGIS aplica-os nos dados raster e fornece aos utilizadores  a informação correta da legenda, histograma e identificação.

![image2](images/entries/9ec1681e4318f92a886405cf8215ec98068cf8ba.webp)
### Funcionalidade: Barra de calculo rápido de campo na tabela de atributos
Temos uma nova funcionalidade para aqueles que trabalhos com campos calculados na tabela de atributos de vetores. A nova barra de cálculo rápido permite-lhe atualizar os valores de uma coluna na tabela de atributos de forma rápida e simples.

![image3](images/entries/386f372e4b7be45426a62005813c8d58a9a2cb43.webp)
### Funcionalidade: Modos de pré-visualização de cores no compositor e no enquadramento do mapa
A really innovative feature that has been added to 2.4 is support for grayscale and colour blindness previews. This allows you to visualise how people with colour blindness will perceive your cartography and map layout, or how your map will look if it\'s printed in grayscale. You can read more about this new feature [here](http://nyalldawson.net/2014/05/colour-blindness-and-grayscale-previews-in-qgis-2-4/).

![image4](images/entries/d3d6193f1a37c8201c9be786ef798c5419eb4c79.webp)
### Funcionalidade: Ficheiros de Camada QGIS QLR
Added support for QGIS Layer Definition files or simply QLR (see <http://nathanw.net/2014/03/12/qgis-qlr/>). QLR file is a file that points to the data, contains all the styling, and other information. You can then just add this file and it will do all the other magic for you. QLR makes it easy to add same layer to multiple map documents, inheriting all of the properties which have been set and works with any layer supported in QGIS, expect special plugin layers.
### Funcionalidade: Novas funções de expressão
Temos algumas novas funções disponíveis no construtor de expressões.
- caixa delimitadora (limites)
- bounding box width & height (bounds_width/bounds_height)
- coordenadas min/máx x/y (xmin/xmax/ymin/ymax)
- nova função de wordwrap que retorna uma string envolvida para um número máximo/mínimo de caracteres

![image5](images/entries/b8f4b0adf2c8f7ba8303f5aa6df8d2294a0b4c7b.webp)
### Funcionalidade: Copiar, colar e arrastar e soltar cores
You can now copy, paste, drag and drop colours between any colour input widget in QGIS. See this [article](http://nyalldawson.net/2014/05/colour-shortcuts-in-qgis-2-4/) for more information on how this new feature works. Hex color codes and rgb strings can also be pasted on to colour buttons to allow importing colours from outside of QGIS.

![image6](images/entries/d2e1cdce5ed643c88f1630fa36b667e53ec8e4de.webp)
### Funcionalidade: Renderização  Multi-threaded
This is one feature we simply cannot do justice to with a screenshot -QGIS now supports multi-threaded rendering! What this means is that when drawing the map, QGIS will split the drawing work between all of the cores in your CPU, making the process more efficient and responsive. By **responsive** we mean that you no longer need to wait for the map view to update before you can pan or zoom again. Also the map display updates incrementally allowing you to see if the map is positioned correctly early on in the drawing process. Take a look at [this article](http://www.lutraconsulting.co.uk/casestudies/qgis-multi-threaded-rendering) for a more detailed overview of the multi-threaded rendering system. You will find some options in the QGIS settings dialog that allow you to manage the behaviour of multi-threaded rendering.

![image7](images/entries/ebcacf7c2623f7ea3e87c929d77bfe4113c75549.webp)
## Etiquetagem
### Funcionalidade: Repetição múltipla do rótulo dos elementos
Long lines (such as contour lines or roads) can now be repeatedly labeled at regular intervals. One can choose between mm and map units for specifying the repetition interval. At the time of the release there is still an issue with \"merge connected lines to avoid duplicate\" setting.

![image8](images/entries/4b996cdf33f0d18a5266e6b6053ab88d4dca9372.webp)
## Compositor de Mapas
### Funcionalidade: Melhoramento nos itens de imagem do compositor
The image item in composer is now \'atlas friendly\' - you can use an **expression to define which image** should be shown for each atlas page. You can also now set the **resize mode** (zoom, clip, stretch etc.) for the image in relation to its frame size and dimensions. You can also specify the placement of the image relative to its frame using the new **placement** item property.

![image9](images/entries/59c029be33ba4cbdf7fb48879350e699cf5f9897.webp)
### Funcionalidade: Modos de escalas pré-definidas para mapas do atlas
When working with atlas map items, you can now specify a predefined scale mode for the map. It will use the best fitting option from the list of predefined scales in you your project properties settings (see Project -\> Project Properties -\> General -\> Project Scales to configure these predefined scales).

![image10](images/entries/45aa708b7c1ba7dd42bd71e3ee293349262853f7.webp)
### Funcionalidade: Melhorias nas tabelas de atributos no compositor
Fizemos um conjunto de melhorias na forma de exibir as tabelas nos seus layouts de composição:
- Foi adicionado suporte para a reordenação das colunas dentro de uma tabela
- Adicionado suporte para expressões baseadas em colunas
- You can now set the alignment of individual table columns, and also specify the alignment for the table\'s header cells
- Conteúdos da tabela podem ser filtrados por uma expressão

![image11](images/entries/e39937a4b6533c14856b12d4a1064425eac52a31.webp)
### Funcionalidade: Melhorias no compositor
Existem um número de adições ao compositor de mapas para tornar a vida mais fácil enquanto trabalha com o modo de composição de mapas:
- Adicionado botão para ver o item a extensão do mapa atual no enquadramento principal do mapa
- Possibilidade de exportar imagens SVG do compositor com camadas
- Definir junção da linha e estilo de junção para as escalas gráficas
- Suporte para configuração do estilo da linha de junção para o item de molduras

![image12](images/entries/cff24f3259e286e405ca13c94fcf5e19dbe98c64.webp)
### Funcionalidade: Melhorias nas molduras HTML
As molduras HTML no compositor foram melhoradas. Existe um novo botão *adicionar moldura** que pode ser usado para criar manualmente múltiplas molduras interligadas. Também melhorámos a nova forma de dividir as páginas possibilitando a correta distribuição do texto.

![image13](images/entries/792d6c3cfc682d2132caec8b6be0ce30c855e39f.webp)
## Plugins
### Funcionalidade: Módulo de Cliente de Catálogos MetaSearch
O Metasearch é um módulo QGIS para interagir com os serviços de catálogos com metadados, suportando a norma do Serviço de Catálogos OGC para a Web (CSW). O módulo fornece uma abordagem intuitiva e amigável para pesquisar os catálogos de metadados com o QGIS e agora vem por defeito como parte integrante do QGIS.

![image14](images/entries/a80155cfd652a9e83c5f2564e371357a92ae115f.webp)
## Simbologia
### Feature: Estilo de preenchimento Shapeburst
We have a great new render in QGIS 2.4. The shapeburst renderer will allow you to fill polygons with a gradient extending from the line edge towards the polygon interior. You can read more about **shapeburst** [here](http://nyalldawson.net/2014/06/shapeburst-fill-styles-in-qgis-2-4/?utm_source=rss&utm_medium=rss&utm_campaign=shapeburst-fill-styles-in-qgis-2-4).

![image15](images/entries/1d85daf70119e7a58d5ef18ae5a0ac2daf18ff4f.webp)
### Funcionalidade: Opção para trocar o marcador de posicionamento da linha
When using a marker line along a line or polygon edge, you can now specify an **offset** so that the marker line starts a set distance from the beginning of the line. If a marker line is set to \"first vertex\" or \"last vertex\" mode, than this offset will control how far along the line from the vertex the marker is placed.

![image16](images/entries/884f1735cee30abc7024f6fc21756b8609770173.webp)
### Funcionalidade: Novo renderizador de Polígonos Invertidos
Um novo renderizador foi adicionado para os elementos do polígono, permitindo-lhe estilizar tudo **fora** dos seus polígonos. Isto pode ser útil para destacar áreas, ou para criar máscaras cartográficas. Quando usada com o novo estilo shapeburst, pode agora produzir mapas como é exibido na imagem desta entrada.

**Nota:** a nova versão do módulo de máscara ajuda de forma fácil a criar camadas de máscara a partir da seleção atual, rótulos de elementos dessas áreas, e gerar uma máscara automaticamente na geração de mapas de Atlas.

![image17](images/entries/b58dd06d363524d112de7a40748f599730c4276e.webp)
### Funcionalidade: Guardar e recuperar estilos com camadas Spatialite
In the previous version was possible to save style with postgres layers, now will be possible for Spatialite layers too. This functions allow to embed different styles inside a spatialite container simplifying sharing data and their presentation. A video tutorial of this funcionality can be found here <http://pvanb.wordpress.com/2014/05/15/saving-layer-styles-to-your-spatialite-database/>

![image18](images/entries/b52c9d3fab8a6281c0e8869702328521a2445994.webp)

{{<content-end >}}
