---
HasBanner: false
draft: false
releaseDate: '2018-06-22'
section: projeto
sidebar: true
title: Alterar registro para QGIS 3.2
type: visual-changelog

---
{{<content-start >}}
# Alterar registro para QGIS 3.2{#changelog32 }
![image1](images/projects/8f04d904f903b8bff930e6c968fe46928e6cc012.png)

Release date: 2018-06-22

The greatest QGIS release ever! QGIS 3.2 brings a massive list of new changes - the highlights of which we will try to cover here. As always can we remind you that QGIS is an open source project and if you are able to, consider supporting our work through [donations]({{< ref "/funding/donate.md" >}}), [sustaining memberships]({{< ref "/funding/membership.md" >}}) or contributions to the code documentation, web site and so on.

**Agradecimentos**

We would like to thank the developers, documenters, testers and all the many folks out there who volunteer their time and effort (or fund people to do so). From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

QGIS is supported by donors and sustaining members. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list]({{< ref "/funding/donate.md" >}}). If you would like to become an official sustaining member, please visit [our sustaining members page]({{< ref "/funding/membership.md" >}}) for details. Supporting QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts. A complete list of current sustaining members is provided below - our very great thank you to all of our supporters!

QGIS é um software livre e você não tem obrigação de pagar nada para usa-ló - de fato queremos encorajar pessoas de todo o lado para usá-lo independentemente do seu status financeiro ou social - acreditamos que capacitar as pessoas com ferramentas de tomada de decisão espacial resultará em uma sociedade melhor para toda a humanidade.

{{<table-of-contents >}}
## Patrocinadores para a versão 3.2 do QGIS
A special thanks to all our [sustaining members, sponsors and donors]({{< ref "/funding/membership.md" >}}) for helping us to make this release possible!
## Geral
### Funcionalidade: O novo formato de arquivo de projeto compactado .qgz agora é o formato padrão
QGZ foi adicionado como um formato opcional no 3.0. Ter esse formato como o formato padrão facilitará muito o caminho para ir para um contêiner capaz de incorporar recursos como SVG, dados offline no GPKG, rampas de cores, plug-ins ou scripts.

![image29](images/entries/15e0d291ccc9722a61ed5d2611d3ac4c0eef3685.png.400x300_q85_crop.webp)

This feature was developed by [OSLANDIA - Paul Blottiere](https://github.com/pblottiere)
### Recurso: Filtrando por valores de campo no Construtor de Consultas
Ao criar um novo filtro de expressão no construtor de consultas, agora você pode filtrar o painel de visualização de valores de campo.

![image30](images/entries/731d930d07ca6d35f6bff727ef94a6322fcf21d0.gif.400x300_q85_crop.webp)

This feature was developed by [Salvatore Larosa](https://github.com/slarosa)
### Característica: Tela FULL Mapa via Ctrl-Shift-Tab
Além de Ctrl-Tab, agora você pode usar Ctrl-Shift-Tab, que mostrará o Mapa e APENAS o Mapa, sem mais barras de ferramentas ou botões (ou mesmo sem Título da Janela, em combinação com F11). Ótimo para projeção de mapa de tela cheia via Beamer ou em grandes telas. Você ainda pode ampliar e deslocar! (Baseado no trabalho de Mathieu Pellerin)

![image31](images/entries/e05bfa8d423465a0ec6697fac1d21dfeee177aea.png.400x300_q85_crop.webp)

Este recurso foi desenvolvido por Richard Duivenvoorde
## Ferramentas de mapa
### Funcionalidade: simplificar ferramenta de mapa agora também pode suavizar recursos
The Simplify Features map tool has been renamed to \"Simplify/Smooth Features\", and now supports interactive smoothing of features.

![image2](images/entries/eca7851f8710661b929a99722afd28707f5926b3.png.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Funcionalidade: Identify Tool com opções extras
Com as novas melhorias, o usuário agora pode usar ferramentas semelhantes à Seleção para identificar vários recursos.

Este recurso foi financiado pelo Conselho do Condado de Leicestershire e pelo Conselho Distrital de East Hampshire

This feature was developed by [Martin Dobias and Viktor Sklencar](https://www.lutraconsulting.co.uk)
### feição: Armazene também o estado expandido / recolhido dos nós no mapa Temas
Cada tema de mapa também registrará quais camadas, grupos e itens de legenda serão expandidos. Assim, quando um tema de mapa é selecionado, os estados expandidos / recolhidos são aplicados na árvore de camadas.

![image3](images/entries/0cfc7d80448436d67a4b1e92773e66eda5900a57.PNG.400x300_q85_crop.webp)

This feature was funded by [Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) within ERIKUS project](https://www.arpa.piemonte.it/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk) and [Faunalia](https://www.faunalia.eu)
### Feature: Auto \"Zoom to Selection\" mode for new map views
Uma nova vista de mapa pode ser configurada para ampliar automaticamente a seleção atual. Poderia ser combinado com diferentes temas de mapas, como neste exemplo.

![image4](images/entries/17848d809ce5a999115619ace229b6f07dba272a.PNG.400x300_q85_crop.webp)

This feature was funded by [Technology One](https://www.technologyonecorp.com/)

This feature was developed by [Nathan Woodrow](https://nathanw.net/)
### feição: Escolha do método de simplificação para simplificar a ferramenta de mapa
This allows different techniques to be used for simplification in the interactive simplify map tool, including the more cartographically pleasing \"Visvalingam\" simplification algorithm.

![image5](images/entries/085ad891fdc2b416a89603a6962544d165f2cef1.PNG.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### feição: add zoom to related feature in forms
Um novo botão aparece no subformulário do atributo do recurso quando um ou mais registros são selecionados em uma tabela relacionada. O botão aproxima o mapa desses recursos se eles tiverem geometrias.

![image6](images/entries/697d671bf6227445e10f9c899c0740b4225c1e7f.PNG.400x300_q85_crop.webp)

Este recurso foi desenvolvido por Jürgen Fischer
### Característica: Áreas / comprimentos / perímetros cartesianos em identificar resultados
No QGIS 3.2, mostramos as áreas elipsoidais e cartesianas, comprimentos e perímetros separadamente no painel de identificação de resultados. Ver as duas medições distintas oferece aos usuários uma melhor compreensão de possíveis problemas em cálculos de área ou distância causados por projeções incorretas ou escolhas elipsoides.

![image7](images/entries/28e185f928be7d08fd2971828a1daed53c224394.png.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## Expressões
### Expressões
- color_grayscale_average()
- color_mix_rgb()
- flip_coordinates()
- wedge_buffer()
- tapered_buffer()
- buffer_by_m()

Nova variáveis:
- \@project_home
- \@project_author
- \@project_abstract
- \@project_creation_date
- \@project_identifier
- \@project_keywords

Este recurso foi desenvolvido por Mathieu Pellerin, Nyall Dawson
### expressão:  Construtor de expressões mais útil
O construtor de expressões agora facilita a criação de expressões dentro do QGIS!
- O construtor agora mostra a descrição dos valores definidos pelos dados, incluindo o intervalo de valores esperados da expressão
- Ctrl + clicar em um nome de função na expressão atual abrirá automaticamente a ajuda para essa função
- Agora mostra indicadores para partes de expressões com erros
- Mostra uma lista completa de mensagens de erro obtidas a partir da análise da expressão

![image8](images/entries/a296b411a0950f6bbd9af3c3cffec90b509b6e78.png.400x300_q85_crop.webp)

This feature was funded by [Technology One](https://www.technologyonecorp.com/)

This feature was developed by [Nathan Woodrow](https://nathanw.net/)
## Interfaçe de usuário
### Funcionalidade: painel Camadas: indicadores para camadas de mapa filtradas
The main window\'s layer tree view (ToC) gets support for indicators that are shown when a vector layer has a filter applied. This makes it easier for users to understand that they are looking at a subset of all data. Clicking the indicator\'s icon brings up query builder.

Isso adiciona um mini-framework para exibição de ícones extras nas exibições de árvore de camadas ao lado de nomes de camadas e grupos. O texto da dica de ferramenta pode ser associado a indicadores para fornecer um contexto extra aos indicadores. Além disso, um sinal é emitido quando o usuário clica em indicadores e ações personalizadas podem ser definidas. A ideia é que os indicadores possam ser usados no futuro para um relatório sutil de vários bits de informação, por exemplo:
- camada de mapa com geometrias inválidas
- camada de mapa com exceções de reprojeção on-the-fly
- camada de mapa tem fonte de dados em falta
- camada de mapa com CRS inválido

![image9](images/entries/ff2206aa7147ca68357ea4e3a1354bc231fb49cc.png.400x300_q85_crop.webp)

This feature was funded by [Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) within ERIKUS project](https://www.arpa.piemonte.it/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk) and [Faunalia](https://www.faunalia.eu)
### Funcionalidade: Permitir a personalização do prefixo de filtros de localização
Prefixes of locator filters can now be customized under the application settings in the \"Locator\" tab

![image10](images/entries/d45b0ff62c8013eed8171c3bc42c9cdacc7dac10.png.400x300_q85_crop.webp)

This feature was funded by [QGIS User Group Switzerland](https://qgis.ch)

This feature was developed by [Denis Rouzaud, OPENGIS.ch](https://opengis.ch)
### Funcionalidade: Abertura de vetor e rasterização armazenada em serviços HTTP (S), FTP ou na nuvem
In 3.2, the data source manager\'s vector and raster panels have been updated to simplify opening of vector and raster datasets stored on HTTP(S), FTP, or cloud services. Basic HTTP(S) authentication support included.

![image11](images/entries/06e06201fb4db385ae14d6932353ce0b0b035e83.jpg.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Funcionalidade: calculadora rápida na barra de pesquisa do localizador
QGIS 3.2 allows evaluation of simple expressions (well, actually ANY QGIS expression\... so you could use aggregates and the like if you really wanted!) by entering \"= \" followed by an expression into the locator bar. If a valid expression is entered, users are given an option to copy the result to the clipboard.

E.g. entering \"= 10/3\" shows a locator entry \"Copy \'3.3333333\' to clipboard\".

![image12](images/entries/873ea8846c5f2f2cea56e8d4602bb41ac0567d7d.png.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Recurso: atalhos para painéis de alternância
Ctrl + {no} atalho

This feature was funded by [Technology One](https://www.technologyonecorp.com/)

This feature was developed by [Nathan Woodrow](https://nathanw.net/)
### Recurso: Marcador de pesquisa no localizador
Permite procurar marcadores espaciais. Clicar duas vezes em um resultado da pesquisa aumentará o zoom do marcador.

Short video: <https://www.youtube.com/watch?v=ymW4TU8QWy4>

The new filter presents itself with a prefix of \"b\" and with tr( \"Spatial bookmarks\" ) as displayname.

Este recurso foi desenvolvido por Klavs Pihlkjær
### Recurso: fechar e reverter ações do projeto
Two new actions have been added to the \"Project\" menu
- \"Close\": Closes the active project, returning the QGIS window to the \"Recent Projects\" list
- \"Revert\": Restores the active project to the last saved state, discarding all unsaved changes

![image13](images/entries/3801ee06f51aa6517fd1c4a5de5eafffd4114f71.png.400x300_q85_crop.webp)

Este recurso foi desenvolvido por Nathan Woodrow, Nyall Dawson
### Funcionalidade: indicador de alterações não guardadas na barra de título
QGIS 3.2 now follows the standard UI approach of indicating that the current project has unsaved changes by adding a \"\*\" prefix to the project name in the application title bar. This makes it easy to see if you have unsaved changes at a single glance!

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Recurso: atraso de dicas de mapa configurável
Este recurso foi desenvolvido por jdugge
### Funcionalidade: Mover camada ou grupo para o painel superior da camada
Move a (s) camada (s) ou grupo (s) selecionado (s) para o topo do painel da camada.

Este recurso foi desenvolvido por Mie Winstrup
### Recurso: copiar o conteúdo do painel de estatísticas para o botão da área de transferência
It is now possible to copy the statistics panel\'s output table into the clipboard.

![image14](images/entries/0d1f4be90052251c05a1fc351dd099aaa92c65f7.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Funcionalidade: páginas Definições de Pesquisa, Opções e Propriedades do Projeto do localizador
Short video: <https://www.youtube.com/watch?v=duB2YekUmV0>

The new filter presents itself with a prefix of \"s\" and with tr( \"Settings\" ) as displayname.

Este recurso foi desenvolvido por Klavs Pihlkjær
### Recurso: Indicadores para camadas e grupos incorporados
Embedded project layers and groups are now flagged by a handy \"embedded\" indicator, making it immediately clear to users which layers and groups have been embedded inside a project.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## Simbologia
### Característica: cores mais agradáveis para novas camadas
The \"random\" colors assigned to new map layers are no longer \"random\" but instead randomly selected from a preset palette of \"visually pleasing\" colors. Say goodbye to ugly baby puke green layers!

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## Renderização
### Recurso: Decoração melhorada dos direitos autorais do mapa
- Suporte de expressão para o texto de copyright.
- Opções aprimoradas de formatação de texto, incluindo sombras, contornos, planos de fundo, etc.

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Recurso: O tamanho da fonte da barra de escala da janela principal e a família podem ser personalizados
This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Recurso: Caminho e tamanho SVG personalizados para a decoração da seta norte
This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
## Gestão de dados
### Recurso: Atualizar uma visão materializada
A partir do navegador, com um clique direito em uma visão materializada, você pode atualizá-lo.

![image15](images/entries/125ee6837700d992fb8b6452ab1b346ba96c5cce.png.400x300_q85_crop.webp)

This feature was developed by [Etienne Trimaille](https://github.com/Gustry)
### Recurso: suporte Z e M para edição off-line
A edição offline agora também suporta camadas com coordenadas Z e M.

This feature was funded by [Oester Messtechnik](https://messtechnik.ch/)

This feature was developed by [Matthias Kuhn, OPENGIS.ch](https://opengis.ch)
### Matéria: Metadados para projetos do QGIS
Continuando o trabalho de metadados iniciado no QGIS 3.0, o 3.2 agora suporta metadados para projetos do QGIS. Isso permite que metadados detalhados sejam definidos nas propriedades do projeto, incluindo resumos, palavras-chave, detalhes de contato, links, etc.

![image16](images/entries/eb1394b46bf05e8a9b6be480cac4382c2f22a865.png.400x300_q85_crop.webp)

Este recurso foi financiado por Arpa Piemonte (Departamento de Geologia e Medo) dentro do projeto ERIKUS

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com) and [Faunalia](https://www.faunalia.eu)
## Formulários e Widgets
### Recurso: Layout de várias colunas para o widget de relação de valor de seleção múltipla
O widget de relação de valor com seleção múltipla ativada agora suporta várias colunas. Isso permite melhor uso do espaço da tela horizontal.

![image17](images/entries/5fb9e551ed835b45161f3a2e9a94320dc50d5b97.gif.400x300_q85_crop.webp)

This feature was funded by [Grundbuch- und Vermessungsamt des Kanton Zug](https://www.zg.ch/behoerden/direktion-des-innern/grundbuch-und-vermessungsamt/gis-fachstelle)

This feature was developed by [David Signer, OPENGIS.ch](https://opengis.ch)
### Funcionalidade: Permitir usar uma URL para formulários de atributos personalizados (arquivo da interface do usuário)
O arquivo da interface do usuário será baixado em todas as sessões no primeiro uso. Isso torna possível distribuir facilmente os arquivos atualizados da interface do usuário para os clientes.

This feature was funded by [SIRS](http://www.sirs-fr.com)

This feature was developed by [Denis Rouzaud, OPENGIS.ch](https://opengis.ch)
### Recurso: formulários de detalhamento (em cascata)
QGIS 3.2 introduces drill-down (cascading) form support, where the values available in one field depend on the values of other fields. This feature allows users to create "value-relation" expressions based on the current value of another field in the same form. When the user modifies a field's value, the choices available in all related fields are filtered to match the new value -- allowing a hierarchical filtering strategy (drill-down, or cascading) inside a form.

![image18](images/entries/5990ff168d5b6b41176de4fa487964b97c32fafc.gif.400x300_q85_crop.webp)

Este recurso foi financiado por Grant Boxer, NaturalGIS, Tudor Bărăscu, NotioGIS, République e cantão de Neuchâtel, Arpa Piemonte, Nelson Silva, Grupo de Usuários Dinamarqueses QGIS, Bo Victor Thomsen e Lene Fischer, North River Geographic

This feature was developed by [Alessandro Pasotti (North Road)](https://north-road.com)
## Camada legenda
### feição: Texto opcional em cima de símbolos para camadas vetoriais
Esse recurso permite que os usuários adicionem informações extras aos símbolos da legenda.

![image19](images/entries/2e1e6a3c4b154c35642096a4c2235c2b2d706200.png.400x300_q85_crop.webp)

This feature was funded by [Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) within ERIKUS project](https://www.arpa.piemonte.it/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk) and [Faunalia](https://www.faunalia.eu)
### Funcionalidade: Copiar e Colar Grupo / Camadas de um projeto QGIS para outro.
Permitindo copiar e colar grupos ou camadas entre projetos e perfis.

This feature was developed by [Salvatore Larosa](https://github.com/slarosa)
## Compositor de mapas
### feição: Fonte de tabela definida por dados para itens da tabela de atributos
When an attribute table is set to a \"Layer features\" source, this new feature allows the underlying vector layer from which to source features to be data defined.

(Todos os atributos de tabela existentes (configurações de coluna) são deixados intactos, portanto, a configuração de uma tabela de dados definida em uma camada com campos diferentes resultará em colunas vazias na tabela.)

This feature was funded by [Kartoza/InaSAFE](http://kartoza.com/en/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Funcionalidade: metadados do projeto incorporados em exportações de layout
Salvar um layout de impressão em SVG, PDF ou imagens agora incorporará todos os metadados do projeto no arquivo criado. O suporte para diferentes elementos de metadados depende do formato de exportação individual.

Este recurso foi financiado por Arpa Piemonte (Departamento de Geologia e Medo) dentro do projeto ERIKUS

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Funcionalidade: Melhor formatação do texto da barra de ferramentas
O QGIS 3.2 permite que toda a gama de opções de formatação de texto seja usada no texto da barra de ferramentas, por ex. buffers, sombras e formas de fundo.

O texto da barra de escala ilegível é coisa do passado!

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## Processamento
### Feature: Improved \'Join by attribute table\' algorithm
The \'Join by attribute table\' algorithm has been upgraded to support one-to-many joins (i.e. create separate features for each matching feature) as well as an option to discard records which could not be joined. Additionally, an optional prefix for joined fields can now be specified.

![image20](images/entries/93dd2a52ae3ed2b7a3842f6379d033fabc7932fe.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin, Nyall Dawson](http://www.imhere-asia.com/)
### Recurso: Carregar script do modelo
Nova opção para carregar scripts de processamento de um modelo personalizado

![image21](images/entries/fce801da5d7b82a1038f19d603d64046e6a399a0.gif.400x300_q85_crop.webp)

This feature was developed by [Matteo Ghetta (Faunalia)](http://www.faunalia.eu/)
### Recurso: Algoritmo de Filtro de Recurso para Modelos de Processamento
Adicione um novo algoritmo de filtro de recurso para o modelador de processamento. Permite filtrar recursos de uma fonte com base em expressões e enviar recursos correspondentes para saídas diferentes como produtos finais ou pipeline de algoritmo diferente para processamento adicional.

Read this [blog post for more information](http://www.opengis.ch/2018/05/28/how-to-filter-features-in-qgis-using-the-graphical-processing-modeler/).

![image22](images/entries/3b1e5e0d5b1874d2e3f0cbb8070eb82dedd89a4e.png.400x300_q85_crop.webp)

This feature was funded by [QGIS User Group Switzerland](https://qgis.ch)

This feature was developed by [Matthias Kuhn, OPENGIS.ch](https://opengis.ch)
### Recurso: histograma zonal
Esse novo algoritmo acrescenta campos que representam contagens de cada valor exclusivo de uma camada de raster contida em zonas definidas como polígonos.

![image23](images/entries/577c3ed7ed7875d51e968a135bfd532f97d692c8.jpg.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Funcionalidade: Algoritmos de Port Union, Difference e Intersection para C ++
Os algoritmos de geoprocessamento nativos do QGIS foram portados do Python para o C ++. Além do aumento de desempenho, vários bugs foram resolvidos com esta atualização.

This feature was funded by [InaSAFE DFAT](https://www.dfat.gov.au/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk)
### Feature: \'Project points (cartesian)\' algorithm
Este novo algoritmo de Processamento projeta pontos de uma camada de ponto de entrada por uma distância especificada e por um rolamento (azimute). Suporta parâmetros dinâmicos para a distância e o rumo, de modo que a distância e o rumo possam ser obtidos de valores ou expressões de campo.

This feature was funded by [Nyall Dawson (North Road)](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Funcionalidade: valores de parâmetros dinâmicos para mais algoritmos
QGIS 3.2 extends the work begun in 3.0 to allow \"dynamic\" parameters for selected Processing algorithms. Dynamic parameters allow users to use expressions or field values to specify the value of a parameter while the algorithm executes, so e.g. the buffer size can be dynamically calculated for each individual feature buffered.

Em 3.2, os seguintes algoritmos suportam parâmetros dinâmicos:
- Excluir orifícios
- Remover Vértices Duplicados
- Simplificar
- suavizar
- Aderir à grade
- Subdidivir
- Transecto de shapes
- Traduzir

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Funcionalidade: Algoritmo de buffer multi-anel (distância constante)
This new algorithm computes multi-ring (\'donuts\') buffer for all the features in an input layer, using a fixed or dynamic distance and rings number.

Este recurso foi desenvolvido por Alex Bruy
### Feature: New \"segmentize\" algorithms
No QGIS 3.2, dois novos algoritmos para segmentar geometrias curvas foram adicionados ao Processing.

\"Segmentize by maximum distance\": The segmentization is performed by specifying the maximum allowed offset distance between the original curve and the segmentized representation.

\"Segmentize by maximum angle\": The segmentization is performed by specifying the maximum allowed radius angle between vertices on the straightened geometry (e.g the angle of the arc created from the original arc center to consective output vertices on the linearized geometry).

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Funcionalidade: Opção para criar pontos em todas as partes do polígono
The \"Centroid\" and \"Point on surface\" algorithms have a new option to create points for every individual part of input geometries.

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Recurso: algoritmo de recursos de rotação
This new algorithm allows rotation of features by a set angle. The rotation can occur around a preset point or each individual feature\'s centroid.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Line sinuosity in \"Add Geometry Attributes\"
The \"Add Geometry Attributes\" algorithm now calculates line sinuosity and straight distance for line layers.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Recurso: importar fotos georreferenciadas
In QGIS 3.2 a new \"Import geotagged photos\" algorithm has been added to Processing. It allows selection of a folder which it will scan for jpg files which have been geotagged and creates a PointZ layer with the result, with attributes for photo path, altitude, direction and timestamp.

Opcionalmente, a varredura pode ser recursiva e você pode criar uma tabela opcional de fotos que não puderam ser lidas ou com geotags ausentes.

O algoritmo define automaticamente a tabela de saída para usar um widget de recursos externo para exibir as fotos vinculadas no formulário de atributo.

![image24](images/entries/399ace1f3d437044b9fb478afb820372195b79d8.png.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Funcionalidade: Trocar algoritmo de valores de coordenadas x / y
Esse algoritmo troca os valores das coordenadas X e Y nas geometrias de entrada. Ele pode ser usado para reparar geometrias que acidentalmente tiveram seus valores de latitude e longitude invertidos.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Sort order option for \"Add Incremental Field\"
Essa alteração permite que os usuários configurem, opcionalmente, uma ordem de classificação para usar ao atribuir valores no algoritmo Add Incremental Field. Anteriormente, os valores eram sempre adicionados usando a ordem original dos recursos. Com essa mudança, os usuários podem controlar a ordem na qual os recursos são atribuídos a valores.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Característica: Indicador para unidades de parâmetros de distância
When an algorithm uses a \"distance\" type parameter, the units will now be shown next to the parameter. This avoids the confusion when running algorithms which use distances where the unit depends on a layer or CRS parameter - e.g. the distance parameter in the buffer algorithm gives the distance in layer units\... so now in QGIS 3.2 we show those units directly within the dialog. Hopefully this leads to less user confusion and accidental \"1000 degree buffers\"!

Além disso - se a unidade estiver em graus, um pequeno ícone de aviso será exibido ao lado do parâmetro. A dica de ferramenta para este ícone aconselha os usuários a reprojetarem dados em um sistema de coordenadas local projetado e adequado.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Funcionalidade: o log do algoritmo pode ser salvo / limpo / copiado
Na caixa de diálogo de execução do algoritmo, novos botões foram adicionados para permitir que os usuários salvem o log atual (em arquivos de texto ou HTML), copiem o conteúdo do log para a área de transferência e limpem o log.

Este recurso foi financiado pela SMEC / SJ

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Recurso: algoritmo de buffer de cunha
Este novo algoritmo cria buffers em forma de cunha a partir de pontos de entrada.

O parâmetro azimute fornece o ângulo (em graus) para o meio da cunha para apontar. A largura do buffer (em graus) é especificada pelo parâmetro width. Observe que a cunha se estenderá até a metade da largura angular de cada lado da direção do azimute. O raio externo do buffer é especificado pelo raio externo e, opcionalmente, um raio interno também pode ser especificado.

O algoritmo suporta parâmetros dinâmicos para azimute, largura e raio.

A saída nativa desse algoritmo é de geometrias CurvePolygon, mas elas podem ser automaticamente segmentadas para polígonos, dependendo do formato de saída.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Recurso: buffers de largura variável
Novos algoritmos de Processamento foram adicionados para criar buffers de largura variável, incluindo buffers afilados (com um diâmetro de início e fim especificado) e buffers de largura variável a partir de valores de string de linha m.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Recurso: Reclassificar algoritmos de varredura
Dois novos algoritmos de reclassificação de rasterização QGIS nativos foram adicionados ao Processing. Estes são simples de usar, mas rápidos e estáveis, e funcionam para QUALQUER tipo de camada de varredura suportada pelo QGIS!
- Reclassificar por camada: reclassifica uma imagem usando os intervalos especificados por meio de campos min / max / value de uma tabela de vetores
- Reclassificar por tabela: reclassifica uma imagem usando uma tabela fixa inserida por usuários na caixa de diálogo do algoritmo

Este recurso foi financiado pela SMEC / SJ

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Funcionalidade: Algoritmo de união com uma única camada
The union algorithm can be now run with just a single input layer in order to resolve any overlaps among the layer\'s features. For example, if an area is covered by three features, that area will be cut out from those features and three new features will be added, copying attributes of the original features.

![image25](images/entries/a32fa9ccc63bd3f91e6696ee8f9aef32f61b4691.png.400x300_q85_crop.webp)

This feature was funded by [InaSAFE DFAT](https://www.dfat.gov.au/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
## Opções de aplicativo e projeto
### Recurso: camadas obrigatórias no projeto
As camadas necessárias não podem ser removidas do projeto. Isso adiciona segurança extra para proteger os usuários do projeto da remoção de camadas que possam achar desnecessárias (por exemplo, usados em junções, relações, expressões).

![image26](images/entries/b65c47d1a41ab4a7ad545696b4985ebd7edb9f75.png.400x300_q85_crop.webp)

This feature was funded by [Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) within ERIKUS project](https://www.arpa.piemonte.it/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk) and [Faunalia](https://www.faunalia.eu)
### Funcionalidade: Salvando e carregando projetos no banco de dados PostgreSQL
Users can now save their projects within a PostgreSQL database. Project can be saved in menu **Projects \> Save To \> PostgreSQL** and loaded using menu **Projects \> Load From \> PostgreSQL**. Projects saved in database can be loaded also through the browser dock (projects show up under the schema where they were saved, together with other layers).

Saving/loading QGIS projects must be explicitly enabled in PostgreSQL connection settings: there is a new option \"Allow saving/loading QGIS projects in the database\" which is disabled by default.

New API has been introduced that allows creation of custom project storage implementations (may be used by plugins). Related QEP: <https://github.com/qgis/QGIS-Enhancement-Proposals/issues/118>

This feature was funded by [Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) within ERIKUS project](https://www.arpa.piemonte.it/)

This feature was developed by [Martin Dobias, Peter Petrik (Lutra Consulting)](https://www.lutraconsulting.co.uk) and [Faunalia](https://www.faunalia.eu)
## Navegador
### Recurso: Salvar / carregar conexões para ladrilhos XYZ
No painel Navegador, as entradas de XYZ Tiles podem ser exportadas / importadas para / de um arquivo XML.

![image27](images/entries/678a1f4686de353f4a04fc83877e27c18d2fca7d.png.400x300_q85_crop.webp)

This feature was developed by [Salvatore Larosa](https://github.com/slarosa)
### Funcionalidade: o caminho inicial do projeto pode ser definido manualmente
This new feature in QGIS 3.2 allows the project home path (which is used by the browser to create the \'Project Home\' item) to be set by users for a project, instead of always matching the location where the project is saved.

This allows users to set the project home to a folder which contains data and other content, and is especially useful for organisations where QGIS projects are not stored in the root folder of a organisational \'project\'.

Os caminhos iniciais do projeto também podem ser definidos para caminhos relativos, em cujo caso eles serão relativos ao local salvo do projeto.

The path can be set through the Project Properties dialog, or by right-clicking on the Project Home browser item and selecting \'Set Project Home\'.

![image28](images/entries/db297eb148a7d62dd58aab40dca32ee91d148831.png.400x300_q85_crop.webp)

Este recurso foi financiado pela SMEC / SJ

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## Provedores de dados
### Funcionalidade: Suporte para estilos de camadas
O trabalho inicial foi feito para introduzir camadas de malha que suportam a exibição de dados em malhas estruturadas ou não estruturadas (grades), além de camadas raster e vetoriais. Este ainda é um trabalho em andamento, esperado para estar totalmente pronto no QGIS 3.4. O trabalho até o momento levou à criação de uma nova biblioteca MDAL para manipulação de diferentes formatos de dados baseados em malha e há novas APIs introduzidas sob o capô, no entanto, a interface do usuário ainda não está implementada.

Para mais informações, veja:

<https://github.com/qgis/QGIS-Enhancement-Proposals/issues/119>

e

<https://github.com/lutraconsulting/MDAL>

![image32](images/entries/91c7bf725bc4afecc9efbeaedc8e98ad153b73b4.png.400x300_q85_crop.webp)

This feature was developed by [Peter Petrik and Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk)
### Funcionalidade: Definir automaticamente o estilo padrão para camadas para camadas do ArcG Feature Server
Quando as camadas de um Feature Server são carregadas no QGIS 3.2, elas terão automaticamente o mesmo estilo aplicado conforme foi especificado para aquela camada no servidor, correspondendo a aparência da camada quando ela é carregada no ArcGIS.

Este recurso foi financiado pela SMEC / SJ

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Recurso: consultas Oracle mais rápidas
Certas operações são muito aceleradas para camadas do Oracle, por exemplo valor insensível a maiúsculas corresponde a recursos.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Funcionalidade: Restringir lista de tabelas para uma conexão de banco de dados Oracle com um esquema predefinido
Essa alteração permite que um esquema seja configurado nas propriedades de conexão para uma conexão de banco de dados Oracle. Se definido, apenas as tabelas nesse esquema serão verificadas e listadas para a conexão.

Previously the option existed to restrict the scan to tables which belong to the user, but this option does not support the use case where a connection must access tables from a different user, and the default \"scan everything\" setting is too expensive (since it often takes multiple minutes to perform, especially when geometryless tables are shown).

This feature was funded by [Open Spatial](http://www.openspatial.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Recurso: suporte somente leitura para geometrias Oracle curvas
Anteriormente, essas geometrias eram descartadas silenciosamente.

This feature was funded by [Open Spatial](http://www.openspatial.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## Complementos
### Funcionalidade: Adicionar histórico de consultas no DB Manager
No 3.2, é possível armazenar consultas SQL. O histórico de consultas está disponível na guia Janela da SQL do plug-in do DB Manager.

![image33](images/entries/9c6074aaf1e989c460833535788d0b396a677e34.png.400x300_q85_crop.webp)

This feature was developed by [Salvatore Larosa](https://github.com/slarosa)
### Funcionalidade: Execução SQL do DB Manager em segundo plano
Este recurso foi desenvolvido por Paul Blottiere
## Feições 3D
### Recurso: Polígonos 3D: Opcionalmente, gerar faces traseiras
Às vezes, os conjuntos de dados com polígonos 3D não têm ordenação consistente de vértices (no sentido horário versus anti-horário) e causam resultados sub-ótimos na visualização 3D: alguns polígonos (paredes) parecem estar ausentes se o preenchimento de face traseira estiver ativado ou alguns polígonos são sombreados incorretamente se o abatimento de face traseira estiver desabilitado. Com a nova opção ** Adicionar faces de retorno ** ativada, o tessellator gerará triângulos em ambas as direções (frente e verso), o que melhora bastante a qualidade de renderização de tais conjuntos de dados.

The only downside when using this option is that more graphical memory is used (double amount of vertex data). Make sure to set culling mode to \"Back\" when using this option, otherwise there would be no visible difference as the scene would still render polygons with incorrect shading.

A imagem contém um conjunto de dados de prédios 3D Praga disponível gratuitamente.

![image34](images/entries/875e423e7a857a509812da6f46d468486fb7fd99.png.400x300_q85_crop.webp)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)

{{<content-end >}}
