---
HasBanner: false
draft: false
releaseDate: '2018-02-23'
section: projeto
sidebar: true
title: Registro de alterações para o QGIS 3.0
type: visual-changelog

---
{{<content-start >}}
# Registro de alterações para o QGIS 3.0{#changelog30 }
![image1](images/projects/8c7c6c5ded71fa7284d9e31144e2c0cdb02059ee.png)

Release date: 2018-02-23

The greatest QGIS release ever! QGIS 3.0 is a huge overhaul and cleanup of our beloved Open Source GIS. QGIS 3.0 brings a massive list of new changes - the highlights of which we will try to cover here. As always can we remind you that QGIS is an open source project and if you are able to, consider supporting our work through [donations](http://www.qgis.org/en/site/getinvolved/donations.html?highlight=donate), [sponsorship](http://www.qgis.org/en/site/getinvolved/governance/sponsorship/sponsorship.html) or contributions to the code documentation, web site and so on.

**Agradecimentos**

We would like to thank the developers, documenters, testers and all the many folks out there who volunteer their time and effort (or fund people to do so). From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

QGIS is supported by donors and sponsors. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become and official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

QGIS é um software livre e você não tem obrigação de pagar nada para usa-ló - de fato queremos encorajar pessoas de todo o lado para usá-lo independentemente do seu status financeiro ou social - acreditamos que capacitar as pessoas com ferramentas de tomada de decisão espacial resultará em uma sociedade melhor para toda a humanidade.

{{<table-of-contents >}}
## Sponsors for QGIS version 3.0
{{<fund type="changelog" relativeImgPath=true >}}
### Recurso: Remover o complemento de conversor dxf2shp
Esta funcionalidade está disponível em OGR e não há mais a necessidade de um complemento QGIS  para fazer esta tarefa
### Recurso: Remova o raster complemento oracle orfão 
### Recurso: Remover provedor TauDEM do núcleo de processamento 
O TauDEM é um conjunto de ferramentas bastante específico e requer a instalação de algumas ferramentas adicionais. Por isso, decidimos transformá-lo em um provedor separado, reduzindo o tamanho da base de código e os esforços para a sua manutenção.
### Funcionalidade: Mais ajuda e possibilidade de configurar a localização dos arquivos de ajuda do QGIS
Mais botões de Ajuda para algoritmos e diálogos são adicionados e direcionados para a Documentação on-line do QGIS.

A configuração permite acessar a ajuda armazenada on-line, na rede da organização ou no computador local. Também é possível combinar diferentes fontes de ajuda.

![image112](images/entries/7c17e43c0c6738c9588f3bef149ca7f3d8a13948.png.400x300_q85_crop.webp)

Esse recurso foi desenvolvido por Alexander Bruy 
### Recurso: Migrar fotos, WebView e arquivo por nome Anexo
![image113](images/entries/d2e949a9804de76d196af6e58996165d01350fec.jpeg.400x300_q85_crop.webp)
### Funcionalidade: Provedores otb e lidartools removidos do processamento
A nova lógica será o desenvolvimento de provedores de complementos capazes de acompanhar o ciclo de vida do software externo.
## Interfaçe de usuário
### Recurso: Ativas docas flutuante com abas 
For qt \> 5.6 builds, it is possible to drop several floating docks in the same floating window where they appear as tabs <https://woboq.com/blog/qdockwidget-changes-in-56.html>

![image66](images/entries/02137f3073c3f8a32bc505bd4916a8df751db79f.gif)
### Recurso: Adicionar suporte para zoom de roda de mouse de resolução fina
Alguns dispositivos de mouse / ponteiro (notadamente no Mac) têm resoluções mais refinadas. Eles enviam eventos de roda do mouse em alta freqüência, mas com valores delta menores. O zoom com esses dispositivos era inutilizável para ações rápidas de zoom. Isso foi corrigido no 3.0.

Esse recurso foi desenvolvido por Matthias Kuhn 
### Recurso: adicionar barra de pesquisa à caixa de diálogo Configurar atalhos
Suporte para pesquisa por nome de ação e por atalho

![image67](images/entries/5f9439417546fff26fe410b5a860a7680b07c53e.png.400x300_q85_crop.webp)

Esse recurso foi desenvolvido por Alexander Bruy 
### Recurso: Barra de localização 
A barra de localização é um recurso de pesquisa rápido, sempre pronto, genérico e conectável no canto inferior esquerdo do QGIS.

Atualmente ele é capaz de procurar algoritmos, ações e nomes de camadas, mas também para selecionar uma função na camada ativa atual, digitando um valor de atributo.

It is \'easy\' extendable, so everybody can create a QgsLocatorFilter for his/her national geocoding service or other search online or database search facility.

![image68](images/entries/c5eba5f5e5a6745d1a81df88eb55f01a68fcc1ad.gif)

Esta funcionalidade foi desenvolvida por Nyall Dawson
### Recurso: mais edição sem bloqueio online
- dimensionamento da unidade de mapa
- Rampa de edição de cores aleatória limitada
- Edição de cores em uma linha lista de cores no painel de estilo
- edição em linhas de cores e símbolos no compositor

agora mostrando em linha no painel de estilo
### Recurso: Adicionar uma opção para mostrar menus de cor para usuários 
Isso adiciona a capacidade dos usuários para definir se um esquema de cores do usuário criado deve aparecer no botão de cor menus drop-down.

It\'s accessed through the color picker dialog, on the lists tab. Just add a new color scheme, then from the scheme menu tick the new \"show in buttons\" option.

Isso é útil se você tiver conjuntos de paletas comuns e quer que eles sejam imediatamente disponíveis através do menu de cores.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Recurso: Configuração de cores para a decoração da seta norte da tela do mapa
A configuração de cor foi adicionada para toda a decoração da seta norte da tela do mapa.

![image69](images/entries/6a3fa6fb065a02defaa42440f301847e8fbbeb75.jpg.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Feature: Improved map canvas\' save as image
The map canvas\' save as image function has been expanded and now offers users the possibility to tweak the scale, resolution, and extent on-the-fly. Extents can be restricted to a height-width ratio. A save as PDF function was also added to quickly export the map canvas into a resolution-independent PDF.

![image70](images/entries/a2adf1e9930f23fa739e68a6e2c55e1b553867b9.png.400x300_q85_crop.webp)

Esse recurso foi financiado por Andreas Neumann (financiamento parcial)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Recurso: Alternar a visibilidade dos painéis abertos na janela principal
Accessible via: - View menu \> Toggle Panels Visibility - **Ctrl+Tab** keyboard shortcut

![image71](images/entries/68249b50c2813f4b204cb0305587b2850e7cd61e.gif)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Recurso: Melhor consistência na interface do usuário
This work sponsored by the QGIS grant program on \"adding consistency to UI controls\" is now complete and merged into master. The following tasks were done as part of this work:
- Toda a API referente a ** transparência / opacidade / alfa ** foi padronizada para ** setOpacity () ** e ** opacidade () **. Os métodos recebem um valor duplo entre 0 (transparente) e 1 (opaco), mantendo a consistência com a API do Qt.
- Um ** novo widget QgsOpacityWidget ** foi criado e agora é usado em todos os lugares por meio da interface do usuário em que a opacidade é configurada. Isso garante um comportamento consistente e procura controles de opacidade em todos os lugares.
- ** A rotação ** foi padronizada na API e na interface do usuário, portanto, a rotação é sempre aplicada no sentido horário. Todos os widgets de rotação foram atualizados para aceitar valores de -360 a 360.
- 2.x Os projetos com rotulagem usando rotação e rotação definida por dados são ** atualizados ** de forma transparente ao abrir em 3.0
- As APIs de escala foram feitas de forma consistente em toda a API do QGIS. ** A mistura confusa de denominadores de escala vs escalas reais foi removida **, com tudo agora operando em denominadores de escala. O comportamento de todas as chamadas de escala de escala é padronizado com um significado comum para escalas min / max (e documentação explícita de api referente a isto)
- Todos os controles de escala agora usam os widgets de escala padrão para consistência na interface do usuário
- Rotulagem agora utiliza a mesma definição para escala min / max como o resto da interface do usuário, e projetos existentes são atualizados de forma transparente na abertura em 3,0.
- Corrigidos os erros mais notáveis relacionados ao uso da escala, incluindo erros que quebram os limites de escala baseados em regras

Obrigado ao QGIS PSC e aos doadores do projeto por patrocinar este trabalho e permitir que ele continue!

Esse recurso foi financiado por patrocinadores e doadores do QGIS 

This feature was developed by [Nyall Dawson](https://north-road.com)
### Recurso: Abra camadas em um grupo único
Se você tentar abrir mais subcamadas, você pode agora abrir todos eles dentro de um grupo na legenda

![image72](images/entries/a64155774fee81370dfb5a786cf7386bffb7a089.png.400x300_q85_crop.webp)

This feature was funded by [Kartoza](http://www.kartoza.com)

This feature was developed by [Etienne Trimaille](https://github.com/Gustry)
## Feições 3D
### Feição: Vista do mapa 3D e geração de terreno
Temos uma nova visualização do mapa 3D nativa no QGIS! A visualização do mapa 3D exibe mapa 2D (renderizado a partir de camadas de projetos) no topo do terreno. Por padrão o terreno é uma superfície plana, mas isso é possível para usar camada raster com modelo de elevação digital como a fonte de dados de altura.

Use menu View \> New 3D Map View to add a 3D view of the project. This will create a new dock widget with 3D map canvas. The 3D view uses the same controls like 2D map views to browse the map using mouse (drag map to move it around, mouse wheel to zoom) or keyboard arrow keys. In addition there are camera controls specific to 3D views: it is possible to rotate and tilt camera by one of the following ways:
- arrastando o mouse com o botão do meio do mouse pressionado
- pressionando Shift e arrastando o mouse com o botão esquerdo do mouse pressionado
- pressionando Shift e usando as teclas para cima / baixo / esquerda / direita

![image121](images/entries/86e6303419d84812266eada5327e74dbc6d507a4.jpg.400x300_q85_crop.webp)

This feature was funded by [QGIS.ORG](https://qgis.org/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Recurso: renderizadores 3D para camadas de mapa
Na configuração padrão, as camadas do mapa são renderizadas em imagens de mapas 2D no topo do terreno. No entanto, é possível fazer melhor uso do mundo 3D configurando renderizadores 3D para algumas camadas do mapa. Com renderizadores 3D, os dados podem ser exibidos em vistas 3D como verdadeiros objetos 3D - isso é atualmente suportado por camadas vetoriais (todos os tipos de geometria - ponto, linha ou polígono). Isso permite uma visualização muito melhor, por exemplo:
- polígonos com bases de construção pode ser extrudida (possivelmente com altura definida-dados) para atingir 3D olhar
- pontos com localizações de pontos de árvores podem ser renderizados com símbolos 3D de árvores (formas geométricas simples ou modelos 3D existentes carregados de um formato de arquivo suportado)

Para configurar renderizadores 3D, use o widget de encaixe de estilo de camada ou a caixa de diálogo de propriedades da camada vetorial - há uma nova guia para configuração de renderizadores 3D.

![image122](images/entries/311f1b52d068ccca9ef74f9ea1dcba259c7ed674.png.400x300_q85_crop.webp)

This feature was funded by [QGIS.ORG](https://qgis.org/)

This feature was developed by [Martin Dobias, Peter Petrik (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
## Expressões
### Recurso: Novo expressão de variáveis
Adds `@project_crs` and `@project_crs_definition` variables for retrieving the current project CRS
### Feature: new global expression variable \@qgis_locale
Retorna a localidade atual usada pelo QGIS. Por padrão, essa é a localidade do sistema atual. Se a substituição de localidade ativada pelo usuário nas configurações do QGIS for substituída, o local será retornado.

![image63](images/entries/23e0bd2bc2cd560dad2d2a873e7d9ab98c532fb0.png.400x300_q85_crop.webp)

Esse recurso foi desenvolvido por Alexander Bruy 
### Recurso: Novas variáveis de expressão para configuração do mapa
    - map_crs, map_crs_definition: retrieves crs details for map
    - map_units: retrieves units for map (eg 'meters','degrees')
    
This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Expressões
**Atlas de expressões**
- **atlas_layerid** and **atlas_layername**: Returns layer ID and layer name of the current layer in the atlas.

**Expressões agregadas**
- **array_agg(expression, group_by, filter)**: Returns an array of aggregated values from a field or expression.

Expressões de matrizes

New group that contains expression functions for the creation and manipulation of arrays (also known as list data structures). The order of values within the array matters, in contrary to the \'map\' data structure, where the order of key-value pairs is irrelevant and values are identified by their keys.
- **array(value1, value2, ...)** : Returns an array containing all the values passed as parameter.
- **array_append(array, value)**: Returns an array with the given value added at the end.
- **array_cat(array1, array2, ...)**: Returns an array containing all the given arrays concatenated.
- **array_contains(array, value)**: Returns true if an array contains the given value.
- **array_distinct(array)**: Returns an array containing distinct values of the given array.
- **array_find(array, value)**: Returns the index (0 for the first one) of a value within an array. Returns -1 if the value is not found.
- **array_first(array)**: Returns the first value of an array.
- **array_get(array, index)**: Returns the Nth value (0 for the first one) of an array.
- **array_insert(array, pos, value)**: Returns an array with the given value added at the given position.
- **array_intersect(array1, array2)**: Returns true if any element of array1 exists in array2.
- **array_last(array)**: Returns the last value of an array.
- **array_length(array)**: Returns the number of elements of an array.
- **array_prepend(array, value)**: Returns an array with the given value added at the beginning.
- **array_remove_all(array, value)**: Returns an array with all the entries of the given value removed.
- **array_remove_at(array, pos)**: Returns an array with the given index removed.
- **array_reverse(array)**: Returns the given array with array values in reversed order.
- **array_slice(array, start_pos, end_pos)**: Returns a portion of the array. The slice is defined by the start_pos and end_pos arguments.
- **array_to_string(array, delimiter, empty_value)**: Concatenates array elements into a string separated by a delimiter using and optional string for empty values.
- **regexp_matches(string, regex, empty_value)**: Returns an array of all strings captured by capturing groups, in the order the groups themselves appear in the supplied regular expression against a string.
- **string_to_array(string, delimiter, empty_value)**: Splits string into an array using supplied delimiter and optional string for empty values.

**Expressões de cor**
- **create_ramp(map, discrete)**: Returns a gradient ramp from a map of color strings and steps.

**Dados e expressões temporais**
- ** epoch (date) **: Retorna o intervalo em milissegundos entre a época do unix e um determinado valor de data.

**Expressões gerais**
- ** env (name) **: Obtém uma variável de ambiente e retorna seu conteúdo como uma string. Se a variável não for encontrada, NULL será retornado.
- **raster_statistic(layer, band, property)**: Returns statistics from a raster layer. Properties: min/max/avg/range/stdev/sum
- **with_variable(name, value, node)**: This function sets a variable for any expression code that will be provided as 3rd argument. This is only useful for complicated expressions, where the same calculated value needs to be used in different places.

Expressões Geometria
- **extend(geometry, start_distance, end_distance)**: Extends linestrings by a specified amount at the start and end of the line
- **hausdorff_distance(geometry a, geometry b, densify_fraction)**: Returns the Hausdorff distance between two geometries. This is basically a measure of how similar or dissimilar 2 geometries are, with a lower distance indicating more similar geometries.
- **inclination(inclination(point_a, point_b)**: Returns the inclination measured from the zenith (0) to the nadir (180) on point_a to point_b.
- **make_circle(center, radius, segment)**: Creates a circular, segmentized, polygon.
- **make_ellipse(center, semi_major_axis, semi_minor_axis, azimuth, segment)**: Creates an elliptical, segmentized, polygon.
- **make_regular_polygon(center, radius, number_sides, circle)**: Creates a regular polygon.
- **make_triangle()**: help still missing
- **minimal_circle(geometry, segment)**: Returns the minimal enclosing circle of a geometry. It represents the minimum circle that encloses all geometries within the set.
- **offset_curve(geometry, distance, segments, join, miter_limit)**: Returns a geometry formed by offsetting a linestring geometry to the side. Distances are in the Spatial Reference System of this geometry.
- **oriented_bbox(geom)**: Returns a geometry which represents the minimal oriented bounding box of an input geometry.
- **pole_of_inaccessibility(geometry, tolerance)**: Calculates the approximate pole of inaccessibility for a surface, which is the most distant internal point from the boundary of the surface. This function uses the \'polylabel\' algorithm (Vladimir Agafonkin, 2016), which is an iterative approach guaranteed to find the true pole of inaccessibility within a specified tolerance.
- ** simplificar (geometria, tolerância) **: Simplifica uma geometria removendo nós usando um limite baseado em distância (isto é, o algoritmo de Douglas Peucker). O algoritmo preserva grandes desvios em geometrias e reduz o número de vértices em segmentos quase retos.
- **simplify_vw(geometry, tolerance)**: Simplifies a geometry by removing nodes using an area based threshold (the Visvalingam-Whyatt algorithm). The algorithm removes vertices which create small areas in geometries, e.g., narrow spikes or nearly straight segments.
- **smooth(geometry, iterations, offset, min_length, max_angle)**: Smooths a geometry by adding extra nodes which round off corners in the geometry.
- **single_sided_buffer(geometry, distance, segments, join, miter_limit)**: Returns a geometry formed by buffering out just one side of a linestring geometry. Distances are in the Spatial Reference System of this geometry.

** Propriedade de Camada **
- **crs_description** returns the CRS description of the layer.

**Mapa de expressões**

This group contains expression functions for the creation and manipulation of \'map\' data structures (also known as dictionary objects, key-value pairs, or associative arrays). One can assign values to given keys. The order of the key-value pairs in the map object is not relevant.
- **map(key1, value1, key2, value2, , ...)**: Returns a map containing all the keys and values passed as pair of parameters.
- **map_akeys(map)**: Returns all the keys of a map as an array.
- **map_avals(map)**: Returns all the values of a map as an array.
- **map_concat(map1, map2, ...)**: Returns a map containing all the entries of the given maps. If two maps contain the same key, the value of the second map is taken.
- **map_delete(map, key)**: Returns a map with the given key and its corresponding value deleted.
- **map_exist(map, key)**: Returns true if the given key exists in the map.
- **map_get(map, key)**: Returns the value of a map, given it\'s key.
- **map_insert(map, key, value)**: Returns a map with an added key/value.

**Camadas de mapa**

Novo grupo que contém uma lista de camadas de mapas disponíveis no projeto atual. Retorna os IDs da camada interna do mapa. Isso é usado em muitas outras funções de expressão que fazem referência às camadas do mapa.

**Expressões matemáticas**
- **inclination(point_a, point_b)**: Returns the inclination measured from the zenith (0) to the nadir (180) on point_a to point_b.

**Operadores**
- **\~:** Performs a regular expression match on a string value.

** Gravar e Atribuir Expressões **

renamed from just \"Record\"
- **get_feature_by_id(layer, feature_id)**: Returns the feature with an id on a layer.
- **is_selected(feature, layer)**: Returns if a feature is selected. If called with no parameters checks the current feature.
- **num_selected(layer)**: Returns the number of selected features on a given layer. By default works on the layer on which the expression is evaluated.
- **represent_value(value, fieldName)**: Returns the configured representafftion value for a field value. It depends on the configured widget type. Often, this is useful for \'Value Map\' widgets.
- ** uuid () **: Gera um Identificador Único Universal (UUID) para cada linha usando o método Qt QUuid :: criar o método Uuid. Cada UUID tem 38 caracteres.

**Relatórios**

New group listing all available table relations in a project. Useful for relation_aggregate functions.

**Desaprovado**
- **\$scale**: old variable to get current map scale. Replaced by **maps_scale**

**Alterar**
- Mudança na função **substr()** 
  - support negative start value (e.g. substr(\'hello\',-2) returns \'lo\')
  - support negative length value (e.g. substr(\'hello\',3,-1) returns \'ll\')
  - length parameter now optional, defaults to end of string (e.g. substr(\'hello world\',7) returns \'world\')
- ** strpos () ** agora depende de uma string simples dentro de uma pesquisa de string
- **regexp_match()** now returns pos of a matching regular expression

Este recurso foi desenvolvido por vários desenvolvedores
### Feature: Expose \@parent variable in aggregate functions
This makes it possible to access attributes and geometry from the parent feature when in the filter of the \"aggregate\" expression function. With this in place aggregates can be calculated per feature.

    E.g. max "measurement" for each point_station per polygon_research_area.
    
Ou um valor de atributo padrão ao digitalizar recursos:

`aggregate(layer:='countries', aggregate:='max', expression:=\"code\", filter:=intersects( $geometry, geometry(@parent) ) )`

![image64](images/entries/7666e6f1fd7a95ec3e099c27c6bf9ef6b145c956.jpeg.400x300_q85_crop.webp)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](https://opengis.ch)
### Feature: Item_variables expression function inside compositions
This adds a new item_variables expression function when expressions are used inside a composition context.

A função aceita um único argumento, o id de um item dentro da composição e retorna um mapa de nome de variável para o valor desse item. Isso permite que você faça coisas como inserir texto em uma etiqueta buscando propriedades de outro item na composição, por exemplo

Inserir escala do mapa em um marcador:

`map_get( item_variables( 'map'),'map_scale')`

Inserir coordenada x do centro do mapa em um rótulo:

`x(map_get( item_variables( 'map'),'map_extent_center'))`

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
## Documentação
### Recurso: Melhorias no processamento de algoritmos
Algoritmos de processamento foram revisados e documentados. Clicar no botão Ajuda abrirá o site do QGIS e mostrará a descrição do algoritmo com documentação e imagens aprimoradas.

![image65](images/entries/ca710bbcb3e67a83217d5894ccccfcb5103b1bf4.png.400x300_q85_crop.webp)

Esse recurso foi financiado por QGIS Grant Proposal

This feature was developed by [Matteo Ghetta (Faunalia), Alexander Bruy](http://www.faunalia.eu/)
## Simbologia
### Recurso: Visibilidade da camada de símbolo definida pelos dados
Adds a data defined override to control a symbol layer\'s visibility. Allows users to disable drawing certain symbol layers for matching features.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Recurso: salvar e restaurar a rampa de cores usada para renderização de falsar cor de banda única
Esse recurso foi desenvolvido por Alexander Bruy 
### Recurso: Adicionar Pontos e Polegadas às unidades de símbolos disponíveis
This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Recurso: Nova ferramenta de botão de rampa colorido
In QGIS 3.0, handling of color ramps has gotten much better via a newly introduced color ramp button widget. Improvements include: - custom color ramp settings are remembered when projects are re-opened - color ramp inversion is implemented within the widget, enabling this action across QGIS - quick access to \"favorite\" color ramps within the widget pop-up menu - interfacing with catalogs (cpt-city and ColorBrewer) is now much more pleasant

![image73](images/entries/547ffa26f79435ff28198820bb0d95dc495b4f13.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Recurso: Re-trabalho de gerenciamento de estilo e atualização
Style management has received a major upgrade. The improvements include:
- A new favorite grouping system was added, which the symbols list widget defaults to
- The selected tag / smartgroup in the symbols list widget now persists when switching layers (and across sessions)
- The symbols list widget will update the tag / smartgroup combo box when users add / rename / remove categories
- Users can now directly tag, as well as add to favorites, symbols while saving those to the style database
- To streamline style management, groups have been removed and fully replaced by tags
- Tags have been integrated into the import/export user interface

![image74](images/entries/bb43cc8a048018b0f54463674ebf2d11bb0abc21.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Recurso: Suporta a definição de cor e transparência em vários itens para renderizadores de raster.
It is now possible to change the color and transparency for multiple values at the same time for the singleband pseudocolor and the paletted renderers. Simply select values within the values\' list and right click to have a pop-up menu appear.

![image75](images/entries/dc60a3f5fdc3a6568e8f3b9bf635066fcde9926d.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Recurso: Mostrar um controle deslizante alfa no menu suspenso do botão de cor
Permite ajustes rápidos na cor alpha

![image76](images/entries/669437f416c6ef5c18dd87ecdfc52772e0b597c7.png.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Recurso: ações de barras de ferramentas de extensão de raster dão suporte a renderização falsa cor 
Esse recurso foi desenvolvido por Mathieu Pellerin
### Recurso: suporte a transparência para o renderizador de paleta
No QGIS 3.0, agora é possível alterar o valor de transparência para valores exclusivos para o renderizador da paleta.

![image77](images/entries/603b73fbf8ad7db9cdb43689641eb70326c11bbf.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Recurso: alongamento automático de varredura ao atualizar a tela
see <https://lists.osgeo.org/pipermail/qgis-developer/2016-September/044393.html> follow up to raster pseudocolor updated extent auto classification.

Este recurso foi desenvolvido pela Even Rouault
### Recurso: Controle sobre as margens do conteúdo da anotação
Permite definir margens esquerda / superior / direita / inferior para o conteúdo de uma anotação.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Recurso: as anotações podem ser estilizadas usando estilos de símbolo de preenchimento
This changes the rendering of annotation frames to use QGIS\' symbology engine, which means that all the existing fill styles can now be used to style annotation frames.

Também pinte os efeitos e os parâmetros de símbolo definidos pelos dados.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Recurso: Renderizador de cluster de pontos
Novo renderizador de símbolo que agrupa pontos próximos em um único símbolo de marcador renderizado. Opcionalmente, um rótulo exibe o número de recursos que foram agregados no único símbolo.

Além disso, algumas melhorias foram feitas no renderizador de deslocamento de ponto, especificamente:
- points are now assigned to the group which is \"nearest\" them, rather then just assigning them first group within the search distance. In some cases this was assigning features to a more distant cluster, resulting in less predictable cluster patterns
- pontos individuais agora são mostrados corretamente em seu próprio estado de seleção
- muita limpeza de código + documentação também.

Para desenvolvedores: QgsPointDisplacementRenderer foi dividido em uma nova classe base QgsPointDistanceRenderer virtual pura que lida com a detecção de grupo e agrupamento de pontos. O novo renderizador de grupo reutiliza essa classe base para evitar a duplicação de código.

See the crowd [funding programme](https://north-road.com/qgis-cluster-renderer-crowdfunding/) for more details.

![image78](images/entries/a9a26b2c7154f918f8b218c2e01f3b38f599436a.png.400x300_q85_crop.webp)

Este recurso foi financiado por Andreas Neumann, Qtibia Engineering (Tudor Barascu), Karl-Magnus Jönsson, Geonésia (Nicolas Ponzo) e numerosos patrocinadores anônimos adicionais cujas generosas contribuições também são altamente valorizadas!

This feature was developed by [Nyall Dawson](https://north-road.com/qgis-cluster-renderer-crowdfunding/)
### Matéria: NOVOS ALGORITMOS DE COLORAÇÃO DE MAPAS NO QGIS 3.0
see <http://nyalldawson.net/2017/02/new-map-coloring-algorithms-in-qgis-3-0/>

![image79](images/entries/1a507363f0c35065d8c2751e167531b96600d700.png.400x300_q85_crop.webp)

Esta funcionalidade foi desenvolvida por Nyall Dawson
### Feature: New \"preset\" colors color ramp option
Allows use of a color ramp consisting of a list of selected colors. Currently there\'s no way in QGIS to classify a renderer using some list of colors you\'ve previously selected. So you can modify the colors manually after classifying, but that\'s a pain if you\'re regularly using the same color scheme. Basically, it\'s like the color brewer color ramp options but allowing users to pick their own preset list of colors to use (Because Cynthia Brewer isn\'t the only cartographic color expert!)

![image80](images/entries/ea1e2fe7215ea888b9de00329e230f6b665610a6.png.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Recurso: Permitir que as camadas de símbolos sejam temporariamente desativadas
Adds a new checkbox at the bottom of each symbol layer\'s properties which allows you to control whether the layer is enabled or not. Disabled layers are not drawn, but are saved and can be enabled at a later stage. This makes it easier to tweak symbol appearance without having to totally delete a symbol layer.

![image81](images/entries/555204a38e13852e4717179a9981cb522244613a.png.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Recurso: estilo fácil de rasters discretos
In QGIS 3.0, the existing raster Paletted Renderer for rasters was adapted to allow for easy styling of discrete raster layers, such as landcover or boolean rasters. Now, users can select the renamed \"Paletted/Unique Values\" renderer and click the \"Add Unique Values\" button to load all unique raster values from the layer. These are automatically assigned a color using the selected color ramp.

O cálculo de valor exclusivo é executado em uma linha de segundo plano para manter a interface do usuário responsiva para camadas de varredura grandes (ou remotas). Além disso, os usuários podem adicionar manualmente novas classes conforme desejado e editar o valor de pixel associado para qualquer classe existente. Também é possível excluir várias classes de uma só vez, além de alterar a cor, a transparência e os rótulos de várias classes de uma só vez.

As paletas de cores podem ser carregadas a partir de um arquivo de texto, com suporte aos formatos de tabela de cores ESR clr / GDAL / GRASS. As paletas de cores podem ser salvas em um arquivo de texto clr para compartilhamento.

![image82](images/entries/536a7bce4d526e2d5fbeeb3189de6f60b2d79256.png.400x300_q85_crop.webp)

This feature was funded by Stéphane Henriod, Satelligence (<http://satelligence.com/>), Bird\'s Eye View (<https://www.birdseyeviewgis.com/>), other anonymous backers

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Rótulo
### Recurso: Permitir tamanho de letra do marcador em mm / pixels
This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Recurso: a barra de ferramentas de etiquetagem personalizada está agora sempre ativada
Thanks to the awesome **auxiliary data storage** and the editable joined table, the manual label customization is now always enabled. You do not need anymore to add dedicated fields in your datasource to change labels position, rotation, or any of the possible settings for labels to activate the toolbar. **No more copy of readonly datasources and so much faster labeling !** **Be warned**, labels are **only saved along with your project file** in a .qgd sqlite database, or inside the .qgz zipped project file if you chose that format. Don\'t forget to share that .qgd file if you want to share your project file.

And for power users, the old way of having data defined fields in your datasource is still there. Just define them in the layer\'s properties as before!

![image83](images/entries/546a77b230bf9b0b28bf61bb231b78cbb6bd5b5f.png.400x300_q85_crop.webp)

This feature was funded by [French ministry of Ecology and Sustainable Developpement](https://www.ecologique-solidaire.gouv.fr/)

This feature was developed by [OSLANDIA - Paul Blottiere](https://github.com/pblottiere)
## Diagramas
### Recurso: propriedades definíveis pelos dados
Adicione suporte para mais propriedades definíveis por dados em diagramas:
- Distância
- Prioridade
- ZIndex
- É um obstáculo
- exposição
- Sempre aparece
- Diagrama Inciar Ângulo

Este recurso foi financiado pelo Programa de Subsídio do QGIS

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
## Renderização
### Recurso: suporte a camada ao vivo
O QGIS 3.0 agora suporta camadas ao vivo. Essas camadas são renderizadas novamente em um intervalo de tempo determinado por você, de maneira limpa e sem tremores. As camadas ao vivo são ótimas para rastrear dados em constante mudança, como uma frota de carros, um bando de pássaros para os quais você tem dados de telemetria e assim por diante.

![image84](images/entries/5a9cd3df6f804b903fee30a08f7018887c1d8710.gif)

Este recurso foi desenvolvido pela Kartoza & North Road
### Recurso: Acionar ações de atualização ou camada de camada do sinal NOTIFY do PostgreSQL
Após os efeitos da camada ao vivo, isso permite desencadear ações ou atualização de camada no QGIS somente quando o banco de dados notifica o QGIS que deve fazer alguma coisa. Isso exigirá menos recursos do que a atualização no intervalo, e você pode até codificar um aplicativo de bate-papo no QGIS com isso :)

See <https://vimeo.com/236604742>

<http://oslandia.com/en/2017/10/07/refresh-your-maps-from-postgresql/>

This feature was funded by [QGIS.org Grant application](https://qgis.org)

This feature was developed by [OSLANDIA - Vincent Mora](https://github.com/vmora)
### Recurso: resultado de rotulagem de cache para evitar redesenhos desnecessários ao atualizar a tela
Essa alteração permite que os resultados da rotulagem sejam armazenados em cache em uma imagem após uma renderização do mapa. Se a imagem de resultado do rótulo em cache puder ser reutilizada para a próxima renderização, ela será evitada, evitando a necessidade de redesenhar todas as camadas que participam do problema de rotulagem e resolvendo a solução de rotulagem. Basicamente, isso significa que ** as atualizações da tela, como resultado de alterações em qualquer camada NON-LABELED, são muito mais rápidas **. (Alterar uma camada que faz parte da solução de rotulagem ainda requer que todas as camadas rotuladas sejam completamente redesenhadas)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Recurso: Representante de grade para deslocamento de pontos
renderizador de grade para pontos deslocados

![image85](images/entries/0247dfa555b6a80139f399b69071a2cc9bd278b3.png.400x300_q85_crop.webp)

This feature was developed by [Muhammad Yarjuna Rohmat (Kartoza)](http://www.kartoza.com)
## Digitalização
### Recurso: Seleção de vértice de intervalo na ferramenta de nó
Esse recurso torna possível selecionar um ** intervalo de vértice** a partir de um recurso. 

Ele pode ser ativado pressionando ** Shift + R ** - depois, é necessário clicar no ponto inicial e final dentro de um recurso - isso selecionará todos os vértices entre os dois.

A seleção do intervalo pode ser cancelada a qualquer momento clicando com o botão direito ou pressionando a tecla Esc.

For closed curves (polygons), it is possible to switch to the \"longer\" way around the ring by holding **Ctrl** while clicking the final point.

![image86](images/entries/b44524fe2864249a334cb7d21fd1a0c1d885ff15.gif)

This feature was funded by [French ministry in charge of ecology](https://www.ecologique-solidaire.gouv.fr/)

This feature was developed by [Martin Dobias (Lutra Consulting)](http://www.lutraconsulting.co.uk)
### Recurso: Adicionar opção de valor Z padrão
Criar Geopackages / Shapefiles: agora com a opção de ter valores Z

![image87](images/entries/80e8c78a1b38dfde5120144fac7354e800b9daff.png.400x300_q85_crop.webp)

Esse recurso foi desenvolvido por Alexander Lisovenko / Paul Blottiere
### Recurso: o recurso Mover agora se beneficia com a digitalização avançada
Just move a feature using the new \"click - click ergonomy\" and use the advanced digitizing panel and shortcut to constraint angles, distances, exact XY.

Esse recurso foi desenvolvido por Denis Rouzaud
### Feature: Added functionality to copy/move feature to move feature map tool
Isso permite duplicar o recurso e movê-los em um movimento a partir de um recurso selecionado

![image88](images/entries/eea327329365ad80c7fc3363ad0fb455fc9d4335.png.400x300_q85_crop.webp)

Esse recurso foi desenvolvido por Denis Rouzaud
### Recurso: rastreamento com deslocamento
Agora você pode usar a ferramenta de digitalização de traços com um deslocamento, conforme mostrado na imagem anexada.

![image89](images/entries/974604dc8908668c2d727e12975707560cffb493.gif)

This feature was funded by [d.b.g. Datenbankgesellschaft mbH](http://www.datenbankgesellschaft.de/)

This feature was developed by [Martin Dobias](http://www.lutraconsulting.co.uk)
### Recurso: revisão da ferramenta Vértice
A ferramenta Nó (agora renomeada para a ferramenta Vértice) sofreu um retrabalho completo para torná-la mais flexível. Algumas das mudanças mais importantes são:
1. Em vez de exigir que os usuários selecionem primeiro um recurso e, em seguida, editem seus vértices no segundo passo, a ferramenta agora é capaz de trabalhar com vários recursos ao mesmo tempo. Portanto, é fácil selecionar vértices de vários recursos e movê-los ou excluí-los de uma só vez. Se houver necessidade de restringir a seleção de vértices a apenas um recurso específico, é possível selecionar os recursos com a ferramenta de seleção primeiro - a ferramenta de vértices só funcionará com vértices do (s) recurso (s) selecionado (s) nesses casos.
2. Em vez de trabalhar apenas com a camada atualmente selecionada, a ferramenta agora pode trabalhar com todas as camadas que estão no modo de edição ao mesmo tempo. A movimentação de recursos que logicamente pertencem, mas estão localizados em diferentes camadas, ficou muito mais fácil. Ainda assim, a camada atual é respeitada se houver várias opções ao escolher vértices.
3. Os recursos e seus vértices são destacados quando o usuário move o ponteiro do mouse sobre eles, fornecendo um melhor feedback visual.
4. In QGIS 2.x the vertices would be moved by clicking a vertex, dragging it with the left mouse button still pressed and finally dropping them by releasing the mouse button. This behavior has been changed to \"click-click\" approach where user first clicks a vertex to pick it, then drag it without having any mouse buttons pressed and drop it by clicking again on the final destination. The arguments for this change were the following:
5. é mais fácil posicionar os nós com precisão (não ter que aplicar força ao botão do mouse o tempo todo)
6. Ninguém move os nós inadvertidamente
7. é possível cancelar a operação
8. permite deslocar o mapa pressionando a barra de espaço enquanto o nó está sendo movido

See <https://github.com/qgis/QGIS-Enhancement-Proposals/issues/69> for more information.

![image90](images/entries/c2761555d13be6b8a1893da2bd3240dd6343c9a6.gif)

This feature was funded by [QWAT](http://qwat.org/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Recurso: Ferramenta de vértice: marcadores de ponto médio para adicionar vértices
A ferramenta aprimorada de vértices agora também exibe marcadores extras no ponto médio de segmentos de linha de recursos. Clicar nesse marcador resulta em um novo vértice. A maneira existente de adicionar vértices clicando duas vezes nos segmentos foi mantida.

![image91](images/entries/b47f105d5ea3ecf5176a8296cc386c65bce21da7.gif)

This feature was funded by [QWAT](http://qwat.org/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Recurso: ferramenta de vértice: linha continua
Ao editar geometrias de segmento de reta com a ferramenta de vértice, mover o mouse em direção ao primeiro ou último vértice exibirá um marcador extra próximo ao ponto final. Clicar no marcador adicionará um vértice no final da geometria.

![image92](images/entries/b355e0701d6b395d25a965cc7d31b9f8acce49d7.gif)

This feature was funded by [QWAT](http://qwat.org/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Recurso: Ferramenta de vértices: suporte para painel digitalizador avançado
O avançado painel de digitalização agora funciona também com a ferramenta de vértices - é possível inserir coordenadas de vértices novos ou existentes no painel, como em outras ferramentas de mapeamento de digitalização.

![image93](images/entries/297f18356a626066332b4c28e13ce4c94bb70166.gif)

This feature was funded by [QWAT](http://qwat.org/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
## Gestão de dados
### Recurso: Pan de recurso atual em tabela de atributos
![image94](images/entries/2f488f086cb64fb0394d1848b4a41f28f80a2adf.gif)

Esse recurso foi desenvolvido por Marco Hugentobler
### Recurso: Mapa da extensão do CRS nas propriedades do projeto
![image95](images/entries/d56d5d68aff5b7f10999751041490769b79e619d.png.400x300_q85_crop.webp)
### Feature: Auxiliary Storage Support
Uma nova guia está disponível nas propriedades da camada vetorial para gerenciar o armazenamento auxiliar:

Uma nova ação * Armazenar dados no projeto * está disponível no menu de dados definidos, fornecendo uma maneira fácil de gerenciar dados auxiliares para uma propriedade:

Os dados auxiliares são armazenados em um banco de dados sqlite e gerenciados graças ao provedor de dados OGR (em vez do provedor de espaço geográfico) para manter o menor tamanho possível do arquivo de banco de dados. Este arquivo de banco de dados (com extensão * .qgd *) é salvo ao lado do arquivo de projeto ou diretamente embutido no novo formato * .qgz *.

See the original [pull request](https://github.com/qgis/QGIS/pull/5086) and this article [which explains more](http://oslandia.com/en/2017/10/17/auxiliary-storage-support-in-qgis-3/)

![image96](images/entries/f0fded6f5276d4b7e51b11834bad3d615e2b4f2d.png.400x300_q85_crop.webp)

This feature was developed by [Paul Blottiere / Oslandia](http://oslandia.com/)
### Recurso: revisão de metadado
O sistema de metadados no QGIS foi revisado. No QGIS 3.0, introduzimos nosso próprio esquema de metadados interno e formalizado, separado do formato de arquivo do projeto QGIS. Apresentamos novos recursos de API para leitura e gravação de metadados para camadas. Separamos a exibição de meta-dados da edição e adicionamos uma nova ferramenta de edição de metadados. Os metadados estão atualmente salvos no arquivo de projeto. Ele também pode ser salvo como um arquivo XML ao lado de camadas baseadas em arquivo ou em um banco de dados sqlite local para camadas remotas (por exemplo, PostGIS).

you can read more about the design considerations adopted in this work by referring to the QGIS Enhancement Proposal (QEP) - [QEP-92](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/91)

Please note this is the first phase in the development of a complete and standards compliant metadata infrastructure for QGIS. We are seeking further funding to implement a more complete implementation for the metadata system - see [this document](https://docs.google.com/document/d/1twE8J345Sz1rk1z34672eqlEiL2mJT4bZbuF5oRTCoM/edit?usp=sharing) for details of future planned work packages that need funding.

The specification for the QGIS metadata schema is [here](https://github.com/qgis/QGIS/blob/master/resources/qgis-resource-metadata.xsd).

The primary funder for this work was [The WorldBank/GFDRR](https://www.gfdrr.org) with supporting funding provided by [NINA](https://www.nina.no/english).

![image97](images/entries/a26adc99ea62733e65222769095537e3be3fb29a.png.400x300_q85_crop.webp)

This feature was funded by [WorldBank/GFDRR](http://gfdrr.org)

This feature was developed by [Kartoza and collaborators](http://kartoza.com)
### Recurso: diálogo do gerenciador de origem de dados unificado
Um único diálogo unificado para manipular o gerenciamento da origem de dados e o carregamento de camadas.

![image98](images/entries/3d6a40ee709ca4f18d8532291f3cbc97997f1932.gif)

Este recurso foi financiado pelo Boundless

This feature was developed by [Alessandro Pasotti](https://www.itopen.it)
### Recurso: Ferramenta OSM Downloader removida
We have removed the OSM downloader tool that was provided in 2.x releases of QGIS. We encourage you to rather use the QuickOSM plugin which has been ported to QGIS 3.0.
## Formulários e Widgets
### Recurso: Permitir rótulos de controle para ferramentas de edições individuais
No designer de arrastar e soltar, um clique duplo em um item permitirá controlar se o rótulo deve ser exibido para cada item individualmente.

Esse recurso foi desenvolvido por Matthias Kuhn 
### Recurso: Permitir a configuração de botões de recurso de link / desconexão no ferramenta do editor de relações
Esse recurso foi desenvolvido por Matthias Kuhn 
### Recurso: visibilidade condicional para guias e caixas de grupo
Isso adiciona uma nova opção de configuração para mostrar ou ocultar abas condicionais e grupos de caixas em arrastar e soltar formulários de designer. A configuração é feita através de um clique duplo na árvore de designer na interface de configuração dos campos. Uma expressão pode ser inserida para controlar a visibilidade.  A expressão  será reavaliado todos os valores na mudança de forma e a aba ou grupo de caixas mostrado / escondido em conformidade.

Esse recurso foi desenvolvido por Matthias Kuhn 
### Feição: Elemento de edição padrão mais inteligentes com plugins para selecioná-los
O novo elemento pode dar um ponto sobre quão bem eles poderíamos manipular o tipo de um campo. Lendo o melhor padrão widgets.

Adicionalmente, plugins podem ser adicionadas para escolher um tipo de widget em função de informação externa. Um deles usam uma tabela e PostgreSQL, permitindo para o tipo de elemento específico e configuração a ser usada para cada campo.

Automatically pick RelationReference widgets for foreign keys.

Esse recurso foi desenvolvido por Patrick Valsecchi
### Feature: Field constraints can be enforced or not
Non-enforced constraints just show a warning to the user, but do not prevent committing the feature. Enforced constraints block users from committing non compliant features. So we have soft warnings now! Any constraints detected by the provider are always enforced.

![image99](images/entries/da468dc209eb7e7da3696ee26850af6b9017312c.png.400x300_q85_crop.webp)

Esse recurso foi financiado por OpenGIS.ch

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: Add layer scoped actions
Within the attribute table, there is a new button to trigger actions which are not based on individual features but instead on the whole layer. Normally they will perform actions based on all features or the selection.

Esse recurso foi desenvolvido por Matthias Kuhn 
### Feature: Show field values in autocompleter in form filter mode
The autocompleter is nicely updated in the background so that the gui remains nice and responsive, even if there\'s millions of records in the associated table.

It\'s now used as a search widget for text fields, so can be seen in the browser window if you set the filter to a text field, or if you launch the form based select/filter by selecting a layer and pressing F3.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: Add zoom to features and flash features shortcuts in select by form dialog
Allows very quick navigation and identification of features which match the criteria in the form

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: Add between/not between to numerical fields in select by form
![image100](images/entries/4bfb34794edbff35e6336c165993278e9a515644.jpeg.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
## Camada legenda
### Feature: Hide Deselected Layers action
Allows you to quickly hide all deselected layers. This is very handy when you have a large project and want to quickly hide all except for a couple of layers

![image101](images/entries/a8419d6027de9351afa6f8a99700509b24cc7418.png.400x300_q85_crop.webp)

This feature was funded by [SMEC (Surbana Jurong)](http://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: Change of ergonomy of the visibility of layers inside groups
- Checking/unchecking a group doesn\'t change the check state of its children. A node is visible if and only if it is checked and all its parents too.
- There is no more a semi-checked state for a group
- **Ctrl-clic** on a unchecked group will check the group and all its descendants.
- Clic on a unchecked layer will check the lager and all its parents.
- Ctrl-clic on a checked group will uncheck the group and all its descendants.
- Ctrl-clic on a checked layer will uncheck the layer and all its parents.
- Those actions are available in contextual menu items in the tree view.
- Invisible layers because they or their parent(s) is unchecked are greyed out.

Este recurso foi desenvolvido pela Even Rouault
## Compositor de mapas
### Feature: Control over drawing of composer table grid horizontal & vertical lines
It is now possible to independently control horizontal and vertical line rendering of composer table items. This added flexibility expends the styling possibilities of this item directly within QGIS.

![image102](images/entries/ac1b2079c9e6c19747322d246d666df7e3c4ac0d.jpg.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Feature: Drag qpt to QGIS to create new composer from template
This feature was funded by [SMEC (Surbana Jurong)](http://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: Allow customization of line spacing for composer legend item labels
This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Feature: Allow choice of CRS for map items
This allows the CRS for map items to differ from the canvas/project CRS. It also allows different map items to have different CRS, eg an overview map can be set to a different CRS to the main map.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: Holding shift while drawing polyline/polygon constrains line angles
This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: More data definable controls
Item **frame** and **background colors** Data defined **svg colors and outline width for composer picture items** (Especially useful when the picture is showing a north arrow!) Data defined **legend titles and column count** Data defined **scalebar colors and line width**

Este recurso foi financiado pelo Programa de Subsídio do QGIS

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feição: Revisão do Compositor de Mapas
This is a major rework to how compositions are managed in the code of QGIS.

Destaques são:
- A new QgsLayoutManager class which is used for storage and serializing/deserializing of compositions. A QgsLayoutManager is attached to QgsProject. This allows core code to access the compositions attached to a project. All handling of compositions has been moved from app to core, making it easy for server (and other non-app based projects. QField/roam?) to access project compositions without resorting to fragile xml parsing.
- Composer windows are created on demand and destroyed on close. This avoids the heavy requirement of creating all composer windows and widgets for every single composer item when loading projects. **It was the main reason loading projects with compositions were so slow previously**. Now, composer windows are created only when the window is opened and destroyed when the window is closed. Composer item configuration widgets are also only created on demand (when an item is selected) instead of precreating all widgets.
- A side benefit of destroying composer windows on close is that **we now no longer suffer from a Qt bug** which blocked use of floating docks in composer windows. Now you can float the item/composition/etc panels! Much nicer for full screen working with compositions on multi-monitor setups.
- **Reworked API for working with composers through iface**. Since composer windows don\'t exist unless they are currently open, all the iface methods for interacting with composers have been redone to make it clear that they only apply to open windows. Additionally, a simple composer interface which provides a stable API for plugins and scripts to work with composer windows has been added. Very basic for now, but in future we can extend with more hooks to allow plugins to interact with composer windows.
- Muitas remoções e limpezas de códigos

More info at <https://north-road.com/qgis-layout-and-reporting-engine-campaign/>

![image103](images/entries/fa298be4fea348f58b9bd2f4bea30f2e7f1c2ee5.png.400x300_q85_crop.webp)

Este recurso foi financiado pelo The Swiss QGIS User Group e muito mais!

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Ferramenta de anáilise
### Feature: Raster unique values count for processing
<http://imhere-asia.com/blog/post/qgis-raster-layer-unique-values-count>

This feature was developed by <http://imhere-asia.com/>
## Processamento
### Feature: New algorithm for offsetting lines
This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: New algorithm for single sided buffers
This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Funcionalidade: Adicionar escolha do método de simplificação para simplificar
This change allows users to choose which method to use when running the simplify geometries algorithm, with choices of the existing distance based (Douglas Peucker) algorithm, area based (Visvalingam) algorithm and snap-to-grid.

Visvaligam in particular usually results in more cartographically pleasing simplification over the standard distance based methods.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: support for output geometry types in models
Model child algorithm inputs are now filtered to only those which generate applicable geometry types for the input to another child algorithm

Esse recurso foi desenvolvido por Alexander Bruy 
### Feature: Angle threshold for smooth algorithm
Add option to QgsGeometry::smooth to not smooth segments shorter than a certain threshold or sharp corners with an angle exceeding a threshold

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: Better support for Z/M dimensions and curved geometries
Many more algorithms now respect Z/M values and do not discard this information, and additionally many algorithms now correctly maintain curved geometries without forced segmentization of these geometries.
### Feature: Raster analysis algorithms added to Processing
The following algorithms were added to Processing from the Raster Analysis plugin:
- Aspecto
- Declividade
- Rugosidade
- Relevo sombreado
- Relevo

Now these algorithms can be used in scripts, models and for batch processing.

![image104](images/entries/f5980f4840b9c822e5a228ec03da59168cd9c5e9.png.400x300_q85_crop.webp)

Esse recurso foi desenvolvido por Alexander Bruy 
### Feature: New algorithm to extract specific nodes
This algorithm allows you to extract specific nodes from geometries. Eg you can extract the first or last node in the geometry.

The algorithm accepts a comma separated list of node indices to extract, eg 0 = first node, 1 = second node, etc. Negative indices can be used to extract nodes from the end of the geometry. Eg -1 = last node, -2 = second last node.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: Expose zonal statistics from Zonal statistics plugin in toolbox
Esse recurso foi desenvolvido por Alexander Bruy 
### Feature: Add a spatialite execute SQL algorithm
Esse recurso foi desenvolvido por Mathieu Pellerin
### Recurso: Novo algoritmo para estender linhas
Allows extending linestrings by a set distance at the start and end of the line

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Recurso: Novo extrato por algoritmo de expressão
Filters an input layer by expression

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: Add import into spatialite algorithm
Esse recurso foi desenvolvido por Mathieu Pellerin
### Recurso: Algoritmos de interpolação
Expose IDW and TIN interpolation from Interpolation plugin in toolbox

Interpolation plugin has been removed as a result

Esse recurso foi desenvolvido por Alexander Bruy 
### Feature: New algorithm to compute geometry by expression
This algorithm updates existing geometries (or creates new geometries) for input features by use of a QGIS expression. This allows complex geometry modifications which can utilise all the flexibility of the QGIS expression engine to manipulate and create geometries for output features.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: Snap geometries to layer algorithm
Port the Geometry Snapper plugin to processing

Snap geometries algorithm allows snapping to other layer types, supports point/line layers

Snap to layer algorithm accepts a mode parameter. With a new option to prefer to snap to closest point on geometry. The old behaviour was to prefer to snap to nodes, even if a node was further from the input geometry than a segment. The new option allows you to snap geometries to the closest point, regardless of whether it\'s a node or segment.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: New input type for expressions
This adds a new input type for expression inputs. Expression inputs can be linked to a parent layer so that the builder shows the correct fields and layer variables.

It\'s designed to be used when an algorithm specifically requires an expression, eg Select by Expression and Extract by Expression.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: SplitWithLines
Rename algorithm SplitLinesWithLines to SplitWithLines Accept polygon as input, too Use only selected lines to split with (if processing is set to use selection only) Issue log message if trying to split multi geometries Update help

Este recurso foi desenvolvido por Bernhard Ströbl
### Feature: Pole of inaccessibility algorithm
Implements a processing algorithm to calculate the pole of inaccessibility for a surface, which is the most distant internal point from the boundary of the surface. This function uses the \'polylabel\' algorithm (Vladimir Agafonkin, 2016), which is an iterative approach guaranteed to find the true pole of inaccessibility within a specified tolerance. More precise tolerances require more iterations and will take longer to calculate.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: Extract by attribute can extract for null/notnull values
Adds support for filtering where an attribute value is null or not null

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: Create attribute index algorithm
Allows creation of an index on an attribute in a layer for faster attribute based filtering

Support depends on the underlying data provider for the layer

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: New \'drop geometries\' algorithm
Simply removes any geometries from an input layer and returns the features with attributes only

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: New universal \'basic stats for field\' algorithm
Replaces the existing \'Basic Stats for Numeric Fields\' and \'Basic Stats for String Fields\' algorithms and adds support for date/time/datetime fields.

Having a single unified algorithm allows more flexible models where a field type may not be known in advance.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: Port heatmap plugin to processing algorithm
This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: New algorithm to orthagonalize geometries
Adds a new algorithm which tries to make angles in geometries either right angles or straight lines

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: Network analysis algorithms
add shortest path and service area algorithms to Processing

also allow calculating shortest path from a point to all points in a layer, or from all points in a layer to an end point. And creating service areas for all points in a layer.

Roadgraph plugin has been removed as a result.

Esse recurso foi desenvolvido por Alexander Bruy 
### Feature: Export processing models as PDF/SVG
In addition to exporting processing models as bitmap images, it is now possible to export processing models as resolution-independent PDFs and SVGs. This allows for high-resolution export of models which can be embedded into papers and books being published.

![image105](images/entries/0ad81df99f01b91d2421263ad35fdc4430c483e0.jpg.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Feature: New algorithm to truncate tables
Irretrievably deletes all features from a table\... use with caution!

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: Added 'invalid feature handling' option
Esse recurso foi desenvolvido por Victor Olaya
### Feature: Algorithm to fix invalid geometries using native makeValid() implementation
Esse recurso foi desenvolvido por Alexander Bruy 
### Feature: Add search to Get Scripts and Models dialog
Esse recurso foi desenvolvido por Alexander Bruy 
### Feature: Generic centroid algorithm
Reworked centroid algorithm which handles non-polygon layers

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: Improved Extract nodes algorithm
Extract nodes algorithm now saves node index, distance along line and angle at node

Este recurso foi financiado por  Andreas Neumann

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: New algorithm for translating (moving) points
Allows geometries to be shifted by a x/y displacement

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: Improved processing modeler window
The processing modeler window has received a lot of attention for this release. Improvements include: - zoom controls in the window\'s toolbar - customization of inputs and algorithms panels\' location - panels can now float above the processing window

![image106](images/entries/d7d74d9113516f51289380755f1862324c83feb5.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Feature: New raster unique values report algorithm
A new algorithm was added to processing which returns the count and area of each unique value within a given raster layer.

![image107](images/entries/096af77b050265c85d7ee203c2ab4d974b8be126.jpg.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Feature: Remove TauDEM provider from core Processing
Nós removemos o provedor TauDEM do processamento

![image108](images/entries/c48a25965a147b866502d10771bea3e831a4d28e.jpeg.400x300_q85_crop.webp)
### Recurso: baixar um arquivo do processamento
Download a file from Processing. Query a remote API to get a geojson

This feature was developed by [Etienne Trimaille](https://github.com/Gustry)
### Feature: Optimised points along geometry algorithm
Supports also polygon geometries, handles null geometries, and records the original line angle along with the distance for each point.

![image109](images/entries/9b24dc337e4896a8be9b0e651e32b3dc9cb11593.png.400x300_q85_crop.webp)

Este recurso foi financiado por  Andreas Neumann

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: Sort by expression algorithm
This feature was funded by [DFAT/DMI](http://dfat.gov.au/pages/default.aspx)

This feature was developed by [Etienne Trimaille (Kartoza)](http://www.kartoza.com)
## Opções de aplicativo e projeto
### Feature: New zipped project file format .qgz
A long time ago on the developper\'s mailing list, we discussed of a container storing the xml file and other ressources. This is now possible, though it remains optional. The auxiliary storage feature takes advantage of that by storing the associated .qgd sqlite database. We hope that in next versions land support for embedding other resources like SVG, color ramps, datasources, images, etc\...

![image110](images/entries/b954811defffce51a7375ae24c640e0d1dcf88da.png.400x300_q85_crop.webp)

This feature was funded by [French ministry of Ecology and Sustainable Developpement](https://www.ecologique-solidaire.gouv.fr/)

This feature was developed by [OSLANDIA - Paul Blottiere](https://github.com/pblottiere)
### Feature: Add support for user profiles
All user settings/plugins, etc are now loaded from the app data location for each platform and no longer .qgis3/2. Settings and plugins in each profile are now isolated from each other.

This allows for different runtime setups depending on what the user needs, e.g test, prod, demo, etc

Profile menu allows for switching between profiles or creating new ones.

![image111](images/entries/82d90b2a02b84584279b5e2b75774631a0cd4a44.jpeg.400x300_q85_crop.webp)

This feature was developed by [Nathan Woodrow](https://github.com/NathanW2)
## Navegador
### Feature: Drag\'n\'drop layers from layer tree view to browser dock
Makes it easy to e.g. store your temporary layers in PostGIS

Esta funcionalidade foi desenvolvida por Martin Dobias
### Feature: Standalone QGIS Browser application removed
We have removed the standalone QGIS Browser application that shipped with QGIS 2.x. This application had poor user uptake and represented a maintenance overhead that we do not wish to continue with in the 3.0 code base.
## Provedores de dados
### Feature: New unified \'add layer\' dialog
You can now use a single dialog to add a huge variety of data formats to QGIS.

![image114](images/entries/d81a5fba0df198b53ef60293ade556125499e5e8.png.400x300_q85_crop.webp)

This feature was developed by [Alessandro Pasotti](https://www.itopen.it)
### Feição: GeoPackage
- processing uses pkg by default
- save as uses pkg by default
- create new layer uses pkg by default
- browser drag and drop import layers

Este recurso foi desenvolvido por Alessandro Pasotti
### Feature: Support all GDAL writable raster formats for \'Save as\' dialog on raster layers
Esta funcionalidade foi desenvolvida por Nyall Dawson
### Feature: Support for Z/M geometries in gpkg, spatialite and memory layer provider
Support for Z dimension and M values was added to QGIS\' gpkg, spatialite and memory layer provider. the option to add Z and M dimensions has also been added to the \"create new layer\" dialogs

![image115](images/entries/63c518b689c749b106944c9d48826abba90887f0.jpg.400x300_q85_crop.webp)

This feature was funded by [QWAT group, http://www.imhere-asia.com/](http://www.qwat.org)

Este recurso foi desenvolvido por Mathieu Pellerin, Alexander Bury, Paul Blottiere
### Feature: Unique and not-null constraint handling
Automatic detection of provider-side unique and not-null constraints implemented for postgres, spatialite, ogr provider

Client side unique and not-null constraints can be set within QGIS.

Unique constraints are enforced in attribute form

Esse recurso foi financiado por OpenGIS.ch

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: GeoNode integration
[GeoNode](http://geonode.org) is an open source geospatial content management system that makes it easy to publish geospatial data on the web. QGIS 3.0 includes new functionality that will allow you to very easily add a GeoNode instance to the browser tree and add any layers from that site to your project as WMS, WFS or XYZ. There is no need to dig around trying to figure out WMS/WFS end points, QGIS will do everything for you. When using WMS and XYZ Tiled layers, the style of the published GeoNode layer will be used.

If the GeoNode instance uses the QGIS Server backend rather than a GeoServer backed, you can copy and paste styles from the server and apply them to your local layer so that your WFS layer renders exactly as it does on the server (as shown in the animated GIF here).

There are also python bindings so that you can add GeoServer layers to QGIS from your plugins. If you are interested in running your own GeoNode with QGIS Server backend please see [this site](https://github.com/kartoza/kartoza-rancher-catalogue/blob/master/README.md) for details on how you can do that using docker and rancher.

![image116](images/entries/8f23a63a25a4ad14c8a35ccf52029aa8f8c96379.gif)

This feature was funded by [WorldBank/GFDRR](https://www.gfdrr.org)

This feature was developed by [Kartoza](http://kartoza.com)
### Feature: Detect literal default values for spatialite provider
This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: Create attribute index support for spatialite provider
Allows creation of attribute indexes for spatialite layers

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Funcionalidade: Adicionar suporte para matrizes
Supported by postgres, spatialite

Esse recurso foi desenvolvido por Patrick Valsecchi
### Feature: Support for HStore in PostGIS data provider
### Feature: Add auto-discovery of relations for PostgresQL
Esse recurso foi desenvolvido por Patrick Valsecchi
### Funcionalidade: Dependências de dados entre camadas
This allows to declare data dependencies between layers. A data dependency occurs when a data modification in a layer, not by direct user manipulation may modify data of other layers. This is the case for instance when geometry of a layer is updated by a database trigger after modification of another layer\'s geometry.

Esta funcionalidade foi desenvolvida por Hugo Mercier
### Feature: dxf export: support reprojection
Esta funcionalidade foi desenvolvida por Juergen E. Fischer
### Feature: Load/save style in database for GPKG and Spatialite
Este recurso foi desenvolvido pela Even Rouault
### Feature: Improved handling of defaults
Improve handling of defaults (inc provider default clauses, literal defaults, and QGIS expression defaults) and automatically handle unique value constraints on layers

Any fields with unique value constraints will be guaranteed to have a value which is unique to the field.

Isso também significa que após determinadas operações de edição (por exemplo, copiar, colar, dividir feições, etc.), os atributos serão agora definidos para o seu valor padrão, se aplicável.

Esta funcionalidade foi financiada por Canton of Zug e pelo projeto QGEP

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
## QGIS Server
### Feature: QGIS Server overhaul
As you may know, QGIS is jumping to a new major version (yes!). Doing so was made necessary because of the need to switch to python 3, QT5, but also because we needed to break the QGIS API in several places. (<http://blog.qgis.org/2016/02/10/qgis-3-0-plans/>)

A year ago, a tiny troll from switzerland rang a bell about the strong need for love server code base required. Indeed, the API was locked by some old methods of QGIS server. In short, QGIS server was reparsing the qgs project file in his own way, and created dependencies to part of QGIS we needed to drop.

As outsourcing the server code base was not an option, so we had to refactor it. The involved parties decided to get engaged in a code sprint in the city of Lyon, France dedicated to sharing their vision, planning the work and finally making all the following happen:

Higher level refactoring

All services (WMS GetMap, WFS GetFeature, GetLegendGraphics, WCS, GetPrint etc..) have been rewritten. Some like WMS were entirely rewritten. Kudos to the devs!

Novas feições
- Multi-thread rendering like in the desktop
- A new option to trust layer metadata and thus speed up project loading
- WFS 1.1 support <https://github.com/qgis/QGIS/pull/5297>
- Ligações completas do Python para a API do servidor
- Serviços do servidor como complementos como provedores

Tarefas profundas, complexas e pouco recompensadoras
- Remover todas as chamadas únicas
- Cortar todas as dependências para o antigo analisador de arquivos do projeto QGIS
- Minimizar as dependências para a biblioteca GUI. Como as fontes são necessárias para renderizar mapas, não era viável removê-las totalmente.

Tarefas de infraestrutura
- Construa uma plataforma de conformidade OGC e integre-a a uma plataforma de integração contínua. Os relatórios de conformidade agora são enviados para tests.qgis.org
- Add unit tests \... and again more unit tests
- Stress QGIS server against security leaks (SQL injections and other malicious attacks)
- Start profiling and bench marking performances. This work still need some love - and funding - to be achieved

A presentation was given at FOSS4G-EU in July.

Esta funcionalidade foi financiada por doadores do QGIS.ORG
### Feição: Possibilidade de segmentar informações de geometria da feição em servidor
Many web clients can\'t display circular arcs in geometries. To allow such clients to still display a feature\'s geometry (e.g. for highlighting the feature), a new per project QGIS server option was introduced (Menu \"Project\" -\> \"Project Properties\" -\> \"QGIS Server\") to segmentize the geometry before sending it to the client in a GetFeatureInfo response.

![image117](images/entries/c6e36e36b5dc6fb0f5534ef11cb773781db4bf8c.png.400x300_q85_crop.webp)

This feature was funded by [Kanton of Zug](https://geo.zg.ch/)

This feature was developed by [Marco Hugentobler](https://www.sourcepole.ch/)
## Complementos
### Feature: Remove trusted status from Plugin Manager
<https://github.com/qgis/QGIS/pull/5272>
### Feature: Offline editing: Add flag to only copy selected features
This extends the offline editing possibilities to only work on subset of large layers

Esta funcionalidade foi financiada por DB Fahrwegdienste GmbH

Esse recurso foi desenvolvido por Matthias Kuhn 
### Funcionalidade: GDALTools foi movido para Processamento
O complemento GDALTools foi removido.

All functions previously available through the GDALTools plugin were moved to the QGIS Processing framework, allowing to use these tools in scripts, models and execute them in batch processes. Additionaly we updated the algorithms with new parameters, introduced in latest GDAL versions and improved overall UI/UX by exposing some advanced parameters like creation options, NODATA value settings etc.

![image118](images/entries/ee1c51737225b6dac80a044f272319534fee2832.png.400x300_q85_crop.webp)

Esse recurso foi desenvolvido por Alexander Bruy 
### Funcionalidade: permitir a instalação de complementos a partir de pacotes ZIP locais
Agora é mais fácil instalar complementos manualmente sem ter que descompactá-los manualmente no diretório do perfil do usuário.

![image119](images/entries/b0311613cf73564f4dc104772abfab551c391dad.jpg.400x300_q85_crop.webp)

Esse recurso foi desenvolvido por Alexander Bruy 
### Feature: Plugins can provide a custom help in Expression window
Plugins which are providing expressions can add a custom help made with HTML strings.

![image120](images/entries/ef610ef1efd507e9bf0ee905d8f8d24a40c753e5.png.400x300_q85_crop.webp)

This feature was funded by [DFAT/DMI](http://dfat.gov.au)

This feature was developed by [Etienne Trimaille (Kartoza)](http://www.kartoza.com)
## Programabilidade
### Recurso: Atualização de classe de geometria
There has been a major overhaul of the geometry classes in QGIS. The old classes have been renamed (as per the table below). New geometry classes will properly preserve Z and M attributes if present.

References [https://github.com/qgis/qgis3.0\\\_api/issues/11](https://github.com/qgis/qgis3.0\_api/issues/11)

This finally brings back a consistent state in naming within the geometry API
### Renomear
| QGIS 2 | QGIS 3 |
| --- | --- |
| QgsPolygon | QgsPolygonXY |
| QgsMultiPoint | QgsMultiPointXY |
| QgsMultiPolyline | QgsMultiPolylineXY |
| QgsMultiPolygon | QgsMultiPolygonXY |
| QgsPolygonV2 | QgsPolygon |
| QgsMultiPointV2 | QgsMultiPoint |
| QgsMultiPolylineV2 | QgsMultiPolyline |
| QgsMultiPolygonV2 | QgsMultiPolygon |

See also <https://github.com/qgis/QGIS/pull/5491>

Esse recurso foi desenvolvido por Matthias, Nyall e outros
### Recurso: Gerenciador de tarefas
Introduces a framework for creating background tasks, which are interacted with through a centralised manager

Adds new classes: - QgsTask. An interface for long-running background tasks - QgsTaskManager. Handles groups of tasks - also available as a QgsApplication member for tracking application wide tasks

Add simple python method QgsTask.fromFunction for creation of tasks from a function without having to create a QgsTask subclass

Suporte para tarefas pendentes

O cancelamento de  uma tarefa da qual os outros dependem conduz que todas essas outras tarefas também sejam canceladas.

Adicionar manipulação de camadas dependentes do gerenciador de tarefas

Se uma tarefa tiver camadas dependentes que estão prestes serem removidas, a tarefa será automaticamente cancelada

QgsTasks pode ter subtarefas

Agora, um QgsTask pode ter subtarefas QgsTasks chamado por conjunto QgsTask::addSubTask. Subtarefas podem ter seus próprios conjuntos de tarefas dependentes,

As subtarefas não são visíveis para os usuários e os usuários só vêem o progresso geral e o status da tarefa principal.

Isso permite a criação de tarefas que são construídas com muitas tarefas de componente menores. O gerenciador de tarefas ainda vai lidar de disparar e programar as subtarefas, portanto, por exemplo, as subtarefas podem ser executadas em paralelo (se suas dependências permitirem isso).

As subtarefas podem em si ter subtarefas.

Esse alteração foi designada para permitir que conceito de processamento de algorítimos e algorítimos de modelador seja traduzido diretamente para a arquitetura do gerenciador de tarefas.

Este recurso foi financiado pelo Programa de Subsídio do QGIS

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: API to allow drag\'n\'drop of custom browser items
QgsDataItem implementations may provide hasDragEnabled(), mimeUri() and QgsCustomDropHandler implementation to deal with drop of custom items.

Esta funcionalidade foi desenvolvida por Martin Dobias

{{<content-end >}}
