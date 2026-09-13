---
HasBanner: false
draft: false
releaseDate: '2016-02-26'
section: projeto
sidebar: true
title: Alterações no QGIS 2.14
type: visual-changelog

---
{{<content-start >}}
# Alterações no QGIS 2.14{#changelog214 }
![image1](images/projects/596e7e353771d2802f065352548e512b8d902d83.png)

Release date: 2016-02-26

This is the changelog for the next release of QGIS - version 2.14 \'Essen\'. Essen was the host city to our developer meet ups in October 2012 and 2014.

**Lançamento de longa duração**

This is a special release since it is designated an \'LTR\' (Long Term Release). LTR releases will be supported with backported bug fixes for **one year**, and will be in permanent feature freeze (i.e. no new features will be added, only bug fixes and trivial updates). Note that we are in discussion to extend the term of our LTR releases to two years, but for technical reasons we will not do this until QGIS 3.2.

O objetivo da LTR é fornecer uma plataforma estável e menos frequentemente alterada para empresas e organizações que não querem lidar com atualização das habilidades do usuário, materiais de treinamento, etc. mais de uma vez por ano. O sucesso da LTR é muito baixo para vocês, nossos queridos usuários - precisamos do seu apoio para ajudar nas correções de bugs e financiamento, certificando-se em seus contratos de suporte com provedores de suporte para especificar que quaisquer correções de erros feitas em seu nome são aplicadas ao ramo LTR bem como o nosso ramo de desenvolvimento normal.

Se uma LTR for importante para você, considere também dar suporte diretamente ao projeto QGIS ou incentive seu provedor comercial a usar o LTR como base para sua solução corporativa, de modo que todos possam se beneficiar de uma plataforma estável que está sendo aprimorada e aprimorada continuamente. Observe que, para usuários e organizações que gostam de viver na fronteira, nossos lançamentos regulares de quatro meses continuarão sem interrupção.

**New Features in QGIS 2.14 \'Essen\'**

If you are upgrading from QGIS 2.8 (our previous LTR version) you will find a great many new features in this release. We encourage you to peruse the changelogs for the intermediate non LTR [2.10](../visualchangelog210/) and [2.12](../visualchangelog212/) releases as this QGIS 2.14 includes all features published in those releases too. Note that 2.14 first enters the regular package repositories and will not immediately replace 2.8 in the LTR package repositories. That will happen when 2.16 is released.

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

**Agradecimentos**

We would like to thank the developers, documenters, testers and all the many folks out there who volunteer their time and effort (or fund people to do so). From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

QGIS is supported by donors and sponsors. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become an official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six-monthly developer meetings, maintain project infrastructure and fund bug fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

QGIS is Free software and you are under no obligation to pay anything to use it - in fact we want to encourage people far and wide to use it regardless of what your financial or social status is - we believe empowering people with spatial decision making tools will result in a better society for all of humanity. If you are able to support QGIS, you can [![donate here](https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif)](https://qgis.org/en/site/getinvolved/donations.html)

{{<table-of-contents >}}
## Patrocinadores QGIS atuais
{{<fund type="changelog" >}}
## Geral
### Funcionalidade: Mudou o comportamento da função strpos
The strpos function behaviour has been altered, so that no match now results in a \"0\" value and a non-zero value means a match at the specified character position. In older QGIS versions, a \"-1\" value would mean no-match and other return values represented the character position - 1.

Arquivos de projeto de versões anteriores do QGIS terão de ser atualizados para refletir essa mudança.

![image47](images/entries/74ddb567a30e840405ca83656e76dd6476d00226.png.400x300_q85_crop.webp)

Este recurso foi desenvolvido por Jürgen Fischer
### Funcionalidade: Zoom para a feição com clique com o botão direito na tabela de atributos
Agora você pode aumentar o zoom para uma feição de dentro de tabela de atributos (sem ter que selecioná-la primeiro) clicando com o botão direito e selecionando zoom para a feição.

![image48](images/entries/7a400f577a7d554f309297f8a1af05a61e448a27.png.400x300_q85_crop.webp)
### Funcionalidade: melhorias de velocidade e memória
- **Salvar um conjunto de feições selecionadas** de uma camada grande é agora muito mais rápido
- Atualizar feições selecionadas usando a **calculadora campo** é mais rápido
- **Zoom mais rápido** para feições selecionadas em camadas grandes
- Much faster `get_feature` expression function (especially when an indexed column in the referenced layer is used)
- `SelectByAttribute` and `ExtractByAttribute` processing algorithms are orders of magnitude faster, and can take advantage of database indices created on an attribute
- `PointsInPolygon` processing algorithm is many magnitudes faster
- **Filtrando as categorias em um renderizador categorizado** (por exemplo, mostrando apenas algumas categorias e desmarcando outras) é muito mais rápido, como agora apenas as feições correspondentes são obtidas a partir do provedor de dados
- **Redução significativa na memória** necessário para abertura de grandes camadas vetoriais

### Funcionalidade: Mais variáveis de expressão
Durante a renderização, novas variáveis estarão disponíveis:
- `@geometry_part_count`: The part count of the currently rendered geometry (interesting for multi-part features)
- `@geometry_part_num`: 1-based index of the currently rendered geometry part

Estes são úteis para aplicar estilos diferentes para diferentes partes do feições de várias partes:
- `@map_extent_width`: The width of the currently rendered map in map units
- `@map_extent_height`: The height of the currently rendered map in map units
- `@map_extent_center`: The center point of the currently rendered map in map units

Também foram acrescentadas variáveis relativas ao ambiente do sistema operacional:
- `@qgis_os_name`: eg \'Linux\',\'Windows\' or \'OSX\'
- `@qgis_platform`: eg \'Desktop\' or \'Server\'
- `@user_account_name`: current user\'s operating system account name
- `@user_full_name`: current user\'s name from operating system account (if available)

![image49](images/entries/b2e29d9df21795416961b8b548f98078386eeecf.png.400x300_q85_crop.webp)

Este recurso foi financiada por Andreas Neumann (o sistema operacional e as variáveis relacionadas ao usuário)

Este recurso foi desenvolvido por Nyall Dawson, Matthias Kuhn
### Funcionalidade: Melhor controle sobre a colocação de elementos do mapa
O QGIS 2.14 ganhou um melhor controle sobre a colocação de setas de norte, barras de escala e avisos de direitos autorais, visite a página de tela do mapa. Agora você pode definir precisamente a posição desses elementos usando uma variedade de unidades (incluindo milímetros, pixels e por cento).

![image50](images/entries/e2390ce8f4bc93ebf00228e1545b192315d2cb57.png.400x300_q85_crop.webp)
### Funcionalidade: Programa pago de correção de bugs
Antes de cada lançamento, temos um programa de correção de bugs pago onde financiar desenvolvedores para limpar o máximo de erros possível. Decidimos começar incluindo um relatório de volta ao programa de correção de bugs pagos como parte do nosso relatório de registro de alterações. Note que esta lista é **não exaustiva**.
- Sandro Santilli: [Postgis Connection freeze if you press \"Set filter\" during loading of data](http://hub.qgis.org/issues/13141)
- Sandro Santilli: [db_manager is unable to load rasters from connections with no dbname specified](http://hub.qgis.org/issues/10600)
- Sandro Santilli: [Plugin layers do not work correctly with rotation](http://hub.qgis.org/issues/11900)
- Sandro Santilli: Crash in QgsGeomColumnTypeThread stopping connection scan [#14140](http://hub.qgis.org/issues/14140) [#13806](http://hub.qgis.org/issues/13806)
- Sandro Santilli: [Crash after bulk change of attribute value in shapefile](http://hub.qgis.org/issues/11422)
- Sandro Santilli: [KMZ causes QGIS application crash (Mac)](http://hub.qgis.org/issues/13865)
- Sandro Santilli: [QGIS 2.8.1 crash opening FileGDB (openGDB-Driver)](http://hub.qgis.org/issues/12416)
- Sandro Santilli: [QGIS crashes when removing vertex of a multipart geometry](http://hub.qgis.org/issues/14188)
- Sandro Santilli: [test -V -R qgis_analyzertest segfaults](http://hub.qgis.org/issues/14176)
- Sandro Santilli: [output/bin/qgis_diagramtest segfaults](http://hub.qgis.org/issues/14212)
- Sandro Santilli: Overflow on primary key with negative values; crashes QGIS when editing [#13958](http://hub.qgis.org/issues/13958) [#14262](http://hub.qgis.org/issues/14262)
- Sandro Santilli: [PyQgsPostgresProvider test hangs in absence of test database](http://hub.qgis.org/issues/14269)
- Sandro Santilli: [TestVectorLayerJoinBuffer hangs if database is not available](http://hub.qgis.org/issues/14308)
- Nyall Dawson: [BLOCKER: Crash when opening layer properties dialog for geometryless vector layer](http://hub.qgis.org/issues/14116)
- Nyall Dawson: Broken server side filtering for OGR, Oracle and Spatialite layers
- Nyall Dawson: [BLOCKER: Bad polygon digitizing in master](http://hub.qgis.org/issues/14117)
- Nyall Dawson: [BLOCKER: Heatmap with expression triggers segfault](http://hub.qgis.org/issues/14127)
- Nyall Dawson: [BLOCKER: unchecking one sub-layer of a categorized symbology leads to no features being drawn](http://hub.qgis.org/issues/14118)
- Nyall Dawson: [HIGH: A Multiband image(e.g. landsat5,7,8) cannot be displayed in windows8](http://hub.qgis.org/issues/13155)
- Nyall Dawson: [BLOCKER: CurvePolygons not drawn](http://hub.qgis.org/issues/14028)
- Nyall Dawson: [BLOCKER: \"Merge Attributes\" tool doesn\'t change values when they are typed](http://hub.qgis.org/issues/14146)
- Nyall Dawson: [HIGH: Filter legend by content is broken when renderer contains duplicate symbols](http://hub.qgis.org/issues/14131)
- Nyall Dawson: Fix issues with conversion of renderers to rule based renderer resulting in broken renderer
- Nyall Dawson: Fix categorised renderer does not store changes to the source symbol
- Nyall Dawson: [HIGH: Avoid crash with raster calculator and huge raster inputs](http://hub.qgis.org/issues/13336)
- Nyall Dawson: [HIGH: \@value variable of simple symbol fill color wrongly gets modified in data-defined expression](http://hub.qgis.org/issues/14148)
- Nyall Dawson: [HIGH: Editing Composer legend while filtered does not work](http://hub.qgis.org/issues/11459)
- Nyall Dawson: [NORMAL: Deleting nodes - inconsistent behaviour](http://hub.qgis.org/issues/14168)
- Nyall Dawson: Fix handling of time value in attributes
- Nyall Dawson: Dialog tab order fixes
- Nyall Dawson: [BLOCKER: crash when adding multiple files from browser panel](http://hub.qgis.org/issues/14223)
- Nyall Dawson: [HIGH: Merge selected features tool corrupts data when columns are defined as \"hidden\"](http://hub.qgis.org/issues/14235)
- Nyall Dawson: Correctly handle LongLong fields in merge attribute dialog
- Nyall Dawson: Fix misleading display of calculation details in measure tool dialog (was misleading and inaccurate for many CRS/unit combinations)
- Nyall Dawson: [NORMAL: max value for option \"increase size of small diagrams\" not sufficient](http://hub.qgis.org/issues/14282)
- Nyall Dawson: [BLOCKER: Area not calculated correctly with OTF on](http://hub.qgis.org/issues/13209)
- Nyall Dawson: [NORMAL: Incoherent lat/lon coordinates in a projected coordinate system project](http://hub.qgis.org/issues/9730)
- Nyall Dawson: NORMAL: make the field calculator compute areas and lengths in units other than map units [#12939](http://hub.qgis.org/issues/12939) [#2402](http://hub.qgis.org/issues/2402) [#4857](http://hub.qgis.org/issues/4857)
- Nyall Dawson: [NORMAL: different built-in tools calculate inconsistent polygon areas](http://hub.qgis.org/issues/4252)
- Nyall Dawson: [NORMAL: In virtual fields \$area function computes always values using \"None/planimetric\" ellipsoid](http://hub.qgis.org/issues/12622)
- Martin Dobias: raster layer drawn as garbage
- Martin Dobias: HIGH: Multi-threaded rendering and OTF reprojection issues [#11441](http://hub.qgis.org/issues/11441) [#11746](http://hub.qgis.org/issues/11746)
- Martin Dobias: [BLOCKER: Regression in \"save as\" dialog for shapefiles](http://hub.qgis.org/issues/14158)
- Martin Dobias: Slow loading of attribute table in debug mode
- Martin Dobias: [BLOCKER: Crash when changing renderer type](http://hub.qgis.org/issues/14164)
- Martin Dobias: [HIGH: Custom python renderer issues #1](http://hub.qgis.org/issues/14025)
- Martin Dobias: [HIGH: Custom python renderer issues #2](http://hub.qgis.org/issues/13973)
- Martin Dobias: 2.5d renderer fixes
- Martin Dobias: [HIGH: Long freeze when initializing snapping](http://hub.qgis.org/issues/12578)
- Martin Dobias: [NORMAL: Loading of data-defined from xml](http://hub.qgis.org/issues/14177)
- Martin Dobias: Fix DB manager to work with SpatiaLite \< 4.2
- Martin Dobias: [NORMAL: Crash while rendering in debug mode](http://hub.qgis.org/issues/14369)
- Martin Dobias: BLOCKER: Fix selection / identification in spatialite views [#14232](http://hub.qgis.org/issues/14232) [#14233](http://hub.qgis.org/issues/14233)
- Martin Dobias: [BLOCKER: Fix drag&drop of spatialite tables](http://hub.qgis.org/issues/14237)
- Jürgen Fischer:[Zoom to layer works incorrectly while layer editing](http://hub.qgis.org/issues/3155)
- Jürgen Fischer:[Help viewer process running in the background with no help viewer (or even QGIS) open](http://hub.qgis.org/issues/8305)
- Jürgen Fischer:[Spatialindex include path missing in some components](http://hub.qgis.org/issues/13197)
- Jürgen Fischer:[compile fails attempting to generate qgsversion.h](http://hub.qgis.org/issues/13680)
- Jürgen Fischer:[Edit widget configuration is stored twice](http://hub.qgis.org/issues/13960)
- Jürgen Fischer:[Extra space in \"IS NOT\" operator makes the expression return wrong selection](http://hub.qgis.org/issues/13938)
- Jürgen Fischer:[QGIS greadily allocates memory and crashes when editing moderately large shapefiles with the node tool](http://hub.qgis.org/issues/13963)
- Jürgen Fischer:[French reprojection use ntf_r93.gsb (IGNF:LAMBE etc ..)](http://hub.qgis.org/issues/14101)
- Jürgen Fischer:[Digitizing: \"Reuse last entered attribute values\" should not overwrite primary key column](http://hub.qgis.org/issues/14154)
- Jürgen Fischer:[Issues in Case expression description](http://hub.qgis.org/issues/14189)
- Jürgen Fischer:[shapefile vector writer: datetime field saved as date resulting in data loss of time](http://hub.qgis.org/issues/14190)
- Jürgen Fischer:[Add help for some variable functions](http://hub.qgis.org/issues/14259)
- Jürgen Fischer:[Virtual layers not working in Processing](http://hub.qgis.org/issues/14313)
- Jürgen Fischer:[layer definition file load error](http://hub.qgis.org/issues/14340)
- Jürgen Fischer:[QgsGeometry::fromWkb fails if WKB is different endian representation](http://hub.qgis.org/issues/14204)
- Jürgen Fischer:[Debian build failure.](http://hub.qgis.org/issues/14248)
- Jürgen Fischer:[PyQgsPostgresProvider test hangs in absence of test database](http://hub.qgis.org/issues/14269)
- Jürgen Fischer:[wkb access out of bounds](http://hub.qgis.org/issues/14315)
- Jürgen Fischer:[QGIS under Windows netCDF import reverses Y axis, Linux doesn\'t](http://hub.qgis.org/issues/14316) [OSGeo4W #483](https://trac.osgeo.org/osgeo4w/ticket/483)
- Jürgen Fischer:[OSGEO4W: Running offline install crashes installer](https://trac.osgeo.org/osgeo4w/ticket/105)
- Jürgen Fischer:[OSGEO4W: Dependencies are not tracking on Windows Server 2003 x64](https://trac.osgeo.org/osgeo4w/ticket/117)
- Jürgen Fischer:[OSGEO4W: installation from local package don\'t check the dependencies](https://trac.osgeo.org/osgeo4w/ticket/151)
- Jürgen Fischer:[OSGEO4W: Setup starts downloading and installing packages before showing you a list to choose from](https://trac.osgeo.org/osgeo4w/ticket/262)
- Jürgen Fischer:[OSGEO4W: Using -a for Advanced selects two options (command line install)](https://trac.osgeo.org/osgeo4w/ticket/351)
- Jürgen Fischer:[OSGEO4W: Infinite license download during quite installation of szip](https://trac.osgeo.org/osgeo4w/ticket/486)
- Jürgen Fischer:Oracle provider deadlock
- Jürgen Fischer:fix saga path setting

### Feature: Field calculator can be used to update feature\'s geometry
A calculadora de campo agora pode ser usada para atualizar geometrias de recursos usando o resultado de uma expressão geométrica. Este é um atalho prático para fazer operações como aplicar um buffer a um grupo de recursos selecionados e, junto com todas as funções de geometria adicionadas recentemente em 2.14, é uma maneira muito prática de manipular suas geometrias!

![image51](images/entries/ba37e2e778a2349c7099e09fcf648238090d8af4.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Funcionalidade: Novas funções de expressão no QGIS 2.14
Lotes de novas funções de expressão foram adicionados para a versão 2.14:
- `relate`: performs a DE-9IM geometry relation by either returning the DE-9IM representation of the relationship between two geometries, or by testing whether the DE-9IM relationship matches a specified pattern.
- the `make_point` function now accepts optional z and m values, and a new `make_point_m` function has been added for creation of PointM geometries.
- `m` and `z` functions for retrieving the m and z values from a point geometry
- new `make_line` and `make_polygon` functions, for creation of line and polygon geometries from a set of points
- `reverse`, for reversing linestrings
- `eval` function, which can evaluate a string as though it is an expression of its own
- `translate` function, for translating geometries by an x/y offset
- `darker` and `lighter` functions, which take a color argument and make it darker or lighter by a specified amount
- `radians` and `degrees`: for converting angles between radians and degrees
- `point_on_surface`: returns a point on the surface of a geometry
- `exterior_ring`: returns the exterior ring for a polygon geometry
- `is_closed`: returns true if a linestring is closed
- new geometry accessor functions: `geometry_n` (returns a specific geometry from within a collection), `interior_ring_n` (returns an interior ring from within a polygon)
- `num_geometries`: returns number of geometries inside a collection
- `num_rings`: returns number of rings in a polygon geometry object
- `num_interior_rings`: returns number of interior rings in a polygon
- `nodes_to_points`, for converting every node in a geometry to a multipoint geometry
- `segments_to_lines`, for converting every segment in a geometry to a multiline geometry
- `closest_point`: returns closest point in a geometry to a second geometry
- `shortest_line`: returns the shortest possible line joining two geometries

`nodes_to_points` and `segments_to_lines` are intended for use with geometry generator symbology, eg to allow use of m and z values for nodes/lines with data defined symbology.

Outras melhorias:
- geometries and features can now be used in conditional functions. For instance, this allows expressions like `case when $geometry then ... else ...` and `case when get_feature(...) then ... else ...`

![image52](images/entries/98616590f44281e09aa24f6c30d7f668c8665c31.png.400x300_q85_crop.webp)
## Ferramentas de análise
### Funcionalidade: Mais ferramentas estatísticas disponíveis para mesclar atributos
Ao usar a ferramenta de atributo de mesclagem de valores de mesclagem ou de mesclagem, há estatísticas de resumo adicionais disponíveis que podem ser usadas para definir os valores de atributo resultantes. Estes incluem Q1, Q3, intervalos interquartil, valores majoritários e minoritários e número de valores únicos, entre outros.

![image27](images/entries/3820507f3bffdaab2bafe7285a8c51791f0b1fdb.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Funcionalidade: valores z/m são mostrados ao usar a ferramenta identificar
A ferramenta de identificação agora é capaz de mostrar qualquer valor z ou m presente nas feições identificadas. Se a feição é uma linha ou polígono, a ferramenta mostrará o número de vértices e x/y/z/m para o vértice mais próximo do ponto identificado. A ferramenta identificar também mostra o número de partes e o número de partes para coleções.

![image28](images/entries/c9813d351340f46e28e6a0cb576a4b2ca72466a9.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Funcionalidade: movimentação das unidades de distância e área e formatos de coordenadas unificados
No QGIS 2,14 a manipulação de várias opções sobre unidades de distância, unidades de área e de apresentação de coordenadas foram unificadas, simplificadas, e mudou-se para as propriedades do projeto. Esta mudança traz inúmeros benefícios, incluindo:
- O formato de coordenadas especificado nas propriedades do projeto é constantemente usado sempre que uma coordenada é exibida para o usuário, incluindo os resultados da ferramenta identificar e a exibição na barra de status.
- The setting for distance and area units in Project Properties is respected for all distance and area calculations, including the measure tool, identify results, and use of the `$area`, `$length` and `$perimeter` functions.
- Unidades de área adicionais foram adicionadas, incluindo metros quadrados, acres, hectares e muito mais.
- Unidades angulares adicionais foram adicionadas à ferramenta de medição do ângulo, incluindo rotações, minutos de arco e segundos de arco.
- It\'s now possible to show the coordinates in latitude and longitude in the status bar even when using a projected CRS.

![image29](images/entries/b086f236720ecb5cac0aa8bb7383275799affff4.png.400x300_q85_crop.webp)

Este recurso foi financiado pelo programa QGIS de patrocínio de correção de bugs

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
## Navegador
### Funcionalidade: Melhorias no navegador
O Navegador QGIS é um painel de sistema de arquivos, OGC Web Services e conexão com banco de dados que permite facilmente arrastar e soltar qualquer camada a partir das fontes acima mencionadas em seu mapa na tela (ou na janela do Gerenciador do banco de dados). Duas novas melhorias úteis foram adicionadas para esta versão:
- **Os caminhos podem ser seletivamente escondidos no painel do browser** - isto é útil para reduzir sua lista de fontes e se concentrar apenas em diretórios relevantes.
- **Projetos carregam diretamente a partir do navegador** - agora você pode arrastar e soltar todo um projeto para o mapa na tela do QGIS e ele será carregado.

![image30](images/entries/8479ec7c4077c9602d6eacdb11d518bd55922074.png.400x300_q85_crop.webp)

Este recurso foi desenvolvido por Nathan Woodrow
## Provedores de dados
### Funcionalidade: capacidades de cache WMS 
QGIS will now cache WMS `GetCapabilities` requests so that on subsequent use response times will be quicker when using that service. By default the cache period is 24 hours, but you can adjust this in the `Network` tab of the QGIS Settings dialog.

![image31](images/entries/743840449ddf09f45251e9710e9666cf4da86081.png.400x300_q85_crop.webp)

Este recurso foi desenvolvido por Jürgen Fischer
### Funcionalidade: apoio a geometria curva expandida
The delimited text provider now supports curved WKT strings, and the memory provider (eg \"temporary scratch\" layers) has gained full support for curved geometries. Additionally, if QGIS has been built using GDAL versions 2.0 and up then QGIS will fully support curved geometries in supported file types (eg GML files).

![image32](images/entries/79f4b8256ab3507b192277c4f14d3bb04423dc52.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Funcionalidade: Melhor manipulação de campos de hora e data e hora
O QGIS 2,14 melhorou a manipulação de tempo e de campo de data e hora, incluindo:
- campos timestamp PostgreSQL são tratados corretamente
- O mecanismo de expressão agora tem suporte completo para campos de tempo
- O construtor de expressão agora mostra os resultados do cálculo de pré-visualização para a data, hora,  e cálculos de intervalo
- Os campos de hora são totalmente suportados por camadas de arquivos vetoriais (dependendo do formato do ficheiro), PostgreSQL, MS SQL Server e camadas temporárias de scratch
- Salvando camadas para arquivos vetoriais serão preservados os campos de tempo se forem suportados pelo formato de camada vetorial (por exemplo, arquivos MapInfo .tab )

![image33](images/entries/2511118cd31ca53892ef5764cf8e80d9491d131a.png.400x300_q85_crop.webp)

Este recurso foi desenvolvido por Jürgen Fischer, Nyall Dawson
### Funcionalidade: suporte Z/M no provedor de texto delimitado
The delimited text provider has gained support for WKT strings containing Z and M coordinates. For example you can express a point with z and measure elements like this : `POINT ZM (1 1 5 60)`.

![image34](images/entries/41d5c223ac43b4f8f392894109414e9d053c9136.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Funcionalidade: grupos de transação para edição de postgres 
Uma nova opção foi introduzida para permitir a edição transacional.

Quando esta opção está habilitada
- Todas as camadas do mesmo banco de dados são colocadas em um grupo de transações
- Quando a primeira camada de um grupo é colocada em modo de edição, todas as outras também são colocadas em modo de edição automaticamente
- Quando uma camada é editada, as alterações são enviadas para o banco de dados imediatamente, permitindo que os gatilhos e restrições a serem aplicadas imediatamente
- Quando uma camada em um grupo de transações é confirmada, todas as camadas são confirmadas (transação de banco de dados)
- Quando uma camada em um grupo de transações é revertida, todas as camadas são revertidas (transação de banco de dados)

This feature is currently **Experimental**. If you find any problems, please [report them](https://www.qgis.org/en/site/getinvolved/development/bugreporting.html).

Isso só é implementado para bancos de dados PostgreSQL no momento.

![image35](images/entries/bb8a03f09c9675985409cf4360308509830d38d4.png.400x300_q85_crop.webp)

This feature was funded by [SIGE](http://www.sige.ch/)

This feature was developed by [Matthias Kuhn, OPENGIS.ch, based on work by Sourcepole](https://opengis.ch)
### Funcionalidade: provedor postgres de autenticação PKI 
A capacidade de usar o gerenciador de autenticação do QGIS introduzido na versão 2,12 foi estendida para o provedor PostGIS. Isso permite a conexão com Postgres usando autenticação básica ou PKI, com as credenciais armazenadas na configuração do QGIS. A nova autenticação do fornecedor de Postgres também pode ser usada no gestor de DB.

![image36](images/entries/6e8f65042bd5981e585812ce2d957d0c6055ba3f.jpg.400x300_q85_crop.webp)

This feature was funded by [Boundless Spatial](http://boundlessgeo.com)

Este recurso foi desenvolvido por Luigi Pirelli
### Funcionalidade: Camadas virtuais
consultas SQL dinâmicas agora podem ser usadas em qualquer tipo de camadas vetoriais que o QGIS é capaz de carregar, mesmo que o formato de camada em si não tem suporte para consultas SQL!

A new kind of vector layer called \"virtual layer\" is now available for that purpose. These allow you to create a virtual layer by defining a query (including support for aggregates and joins) from other layers in your project. The resultant layer will be a live, dynamic view of the query result, so any changes to the source layers will be automatically and immediately reflected in the virtual layer!

O dialeto SQL suportado é SQLite com funções SpatiaLite. As funções QGIS de expressão também podem ser utilizadas em procedimentos. Qualquer tipo de camada vetoriais pode ser acessado na consulta, incluindo várias camadas de diferentes provedores de dados.

Support for virtual layers has also been added to DB Manager as well as to the Processing toolbox where a new \'Execute SQL\' tool is available.

![image37](images/entries/58bc1a2fea31fe8d6ab70ff33c763c9ddac40ade.png.400x300_q85_crop.webp)

This feature was funded by [MEDDE (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr)

This feature was developed by [Hugo Mercier / Oslandia](http://oslandia.com)
### Funcionalidade: Mais extensões de arquivo para osprovedores GDAL e OGR
Para arquivos vetoriais e raster, o QGIS conta com a biblioteca GDAL / OGR. Isso significa que praticamente qualquer formato de arquivo que possa ser aberto pelo GDAL ou OGR pode ser aberto diretamente no QGIS. Até agora, algumas extensões de arquivo não foram adicionadas no seletor de arquivos GDAL ou OGR, resultando em usuários que acreditavam que o QGIS não podia abrir ou manipular esses formatos de arquivo. Para minimizar esse problema, algumas novas extensões foram adicionadas aos filtros do seletor de arquivos GDAL e OGR:

**Para arquivos vetoriais:**
- .thf para o formato EDIGEO de cadastro Francês
- .ods para formato de planilhas OpenDocument LibreOffice
- .xls para o formato Microsoft Excel
- .xlsx para o formato Microsoft Excel OpenXML
- .xml para o formato NAS - Alkis
- .map para o formato WAsP
- .pic para o formato PCIDSK
- .gts e .gtm para o formato GPS TrackMaker
- .vfk para o formato VFK
- .osm e .pbf para o formato OpenStreetMap
- .sua para o formato SUA
- .txt para o formato OpenAir
- .xml para o formato de tabela Planetary Data Systems
- .htf para o formato de Transferência Hidrográfica 
- .svg para o formato SVG
- .gen para ARCGEN
- .sxf para o formato de armazenamento e eXchange
- .pdf para o formato de vetor Geospatial PDF
- .sgy e .segy para o formato SEG-Y
- .seg, .seg1, .sp1, .ukog, .ukooa para o formato SEGD UKOOA
- .ovf para o formato de arquivo vetorial VRT
- .kmz para o formato KML compactado (KMZ)
- .db3, .s3db, .sqlite3, .db3, .s3db, .sqlite3 para o formato SQLite/SpatiaLite
- .sl3 para o formato SQLite Espaciais (FDO) 
- CouchDB Espaciais (via URL)

**Para arquivos raster:**
- .ovr para o formato de arquivo vrt raster

![image38](images/entries/7a628a66f2f63454bd65fbedda309ff5a7d25f1e.png.400x300_q85_crop.webp)

This feature was developed by [Médéric Ribreux](https://medspx.fr)
### Feature: Use ST_RemoveRepeatedPoints for server-side simplification with PostGIS 2.2 (or newer) layers
When using a PostGIS 2.2 instance, QGIS now uses the ST_RemoveRepeatedPoints function instead of the ST_SnapToGrid function to process server-side simplification, as described by [Paul Ramsey](http://blog.cartodb.com/smaller-faster/).

Este método irá diminuir o número de vértices das geometrias que o QGIS precisa fazer o download a partir do servidor, o que aumentará a velocidade de renderização e salvar largura de banda entre o QGIS e o servidor PostgreSQL.

![image39](images/entries/bea701efeedd257314f507dfb2689fbf95403095.png.400x300_q85_crop.webp)

This feature was developed by [Michaël Douchin \@kimaidou](http://3liz.com)
## O gerenciamento de dados
### Funcionalidade: A remoção do plug-in SPIT
The \"SPIT\" plugin is no longer bundled with QGIS, as the plugin was unmaintained and has been surpassed by DB Manager and the processing database import algorithms.

![image40](images/entries/b496fc25b098575ece2a38ea5a601caf75bb51dc.png.400x300_q85_crop.webp)

Este recurso foi desenvolvido por Nathan Woodrow
### Funcionalidade: exportação DXF: opção de usar o título em vez do nome como nome da camada DXF na aplicação e servidor
![image41](images/entries/e09652676e15a883821ca9b269c03ab0239aacb3.png.400x300_q85_crop.webp)

This feature was funded by [City of Uster](http://gis.uster.ch/)

Este recurso foi desenvolvido por Jürgen Fischer
### Funcionalidade: Tipos de geometrias podem ser substituídos na janela vetoriral Salvar como
Isso torna possível fazer coisas como salvar uma tabela geometryless com um tipo de geometria, de modo que as geometrias podem ser adicionadas manualmente para linhas. Anteriormente isso só era possível fazer noQGIS recorrendo a junção ou outras soluções.

Além disso, foram adicionadas opções para forçar o arquivo de saída para ser multi tipo, ou incluir uma dimensão z.

![image42](images/entries/886630cb835b72865c5442a73a79b46cc5a7b60f.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Funcionalidade: Associações vetoriais agora são guardadas dentro da camada de definição-em arquivos QLR
### Funcionalidade: Widget de recursos externos
A new form widget is now available. It is named \"External resource\" and it allows a more complete handling of attributes assigned to file paths storing. Here is a complete summary of the widget features:
- You can set an **extension filter** to force the storing of fixed file formats. If a filter is set, the file selector will only show file names that are relevant to the filter (it is still possible to select any file by using \'\*\' character in the search field). Filter syntax is the same than [Qt widget QFileDialog::getOpenFileName](https://doc.qt.io/qt-4.8/qfiledialog.html#getOpenFileName).
- You can set a **default path**. Each time a user triggers the widget, a file selector will open at the default path (if set). If no default path has been set, the file selector will use the last path selected from an \"External resource\" widget. If the widget has never been used, the file selector defaults to opening on the project path.
- Você pode definir e definir **o caminho relativo de armazenamento**. O armazenamento de caminho relativo permitirá que você salve apenas a parte do caminho que está após o caminho padrão (se o caminho padrão estiver definido) ou o caminho do projeto atual. Isso é particularmente útil quando você deseja salvar caminhos longos em atributos de tamanho limitado (como atributos de texto para Shapefiles que são limitados a 254 caracteres) ou para criar arquivos de projeto e arquivo de dados autocontidos para distribuição.
- Outro novo recurso para fazer o widget mais fácil de usar é que **caminhos de arquivos agora podem ser exibidos como hiperlinks**. Ao clicar no link irá abrir diretamente o arquivo vinculado ao QGIS. Você pode configurar essa opção para exibir o caminho completo do arquivo, ou apenas seu nome de arquivo. O arquivo será aberto usando o manipulador padrão para esse formato de arquivo de seu sistema operacional.
- Você também pode **usar uma URL em vez de um caminho de arquivo**. O widget irá interpretá-lo como um URL e você será capaz de abrir a página web ligada diretamente no seu navegador web padrão.
- Você pode optar por **caminhos de diretório de loja em vez de caminhos de arquivo**.
- Há um **visualizador de documentos integrado** neste widget. Você pode usá-lo para exibir imagens ou páginas da web diretamente no QGIS. O seletor de arquivos para o visualizador integrado irá beneficiar de todas as opções acima mencionadas.

Para mais informações sobre as opções de configuração, você pode usar as dicas de ferramentas da caixa de configuração.

The main aim of this new widget is to fix and improve the two existing \'File name\' and \'Photo\' widgets, and replace them with a single unified widget. For the moment, you can still use the old widgets but they will be deprecated and removed for QGIS 3.0. We recommend to switch your projects to use the new \'External Resource\' widget now.

**Este recurso foi desenvolvido por**:
- [Denis Rouzaud](https://github.com/3nids)
- Matthias Kuhn at [OPENGIS.ch](https://opengis.ch)
- [Médéric Ribreux](https://medspx.fr)

![image43](images/entries/d20edab2103d774f548a55552ca2dbe20ac39e67.png.400x300_q85_crop.webp)
### Funcionalidade: edição de relação N:M
Isso adiciona a possibilidade de gerenciar dados em um banco de dados relacional normalizado em N: M (muitas para muitas) relações. No editor de relação, as ferramentas para adicionar, excluir, vincular e desvincular também trabalham na tabela de ligação, se a relação é visualizada como uma relação N:M.

A configuração é feita através da guia campos onde a relação em uma segunda relação pode ser escolhida (se há uma relação adequada em termos de uma segunda relação de ligação na tabela).

**Limitações:**

O QGIS não é um sistema de gerenciamento de banco de dados.

Ela é baseado em suposições sobre o sistema de banco de dados subjacente. Em particular:
sugere uma edição
- it expects an `ON DELETE CASCADE` or similar measure on the second relation
- it does not take care of setting the primary key when adding features. Either users need to be instructed to set them manually or - if it\'s a database derived value - the layers need to be in transaction mode

![image44](images/entries/9f033883617b01432aae23c35be54070c1a9f5b3.png.400x300_q85_crop.webp)

Este recurso foi financiado por République et canton de Neuchâtel, Ville de Pully, Ville de Vevey

This feature was developed by [Matthias Kuhn](http://opengis.ch)
## Digitalização
### Funcionalidade: cor de banda da borracha configurável 
Agora você pode definir a largura da borracha e a cor utilizada para a digitalização.

![image45](images/entries/40ef6c2f93c7697133ebede324fe9dafe40f42f0.png.400x300_q85_crop.webp)
### Funcionalidade: ferramenta de digitalização de Traço
A nova ferramenta de rastreamento de digitalização é uma ferramenta de digitalização avançada, que lhe permite digitalizar feições em uma camada por recursos de rastreamento em outra camada.

A ferramenta de rastreamento:
- uses Dijkstra's shortest path algorithm to find traceable routes
- pode traçar rotas de múltiplas feições distintas
- pode ser usado com ferramentas avançadas de digitalização (reformulação por exemplo)
- pode ser ativada e desativada pressionando **T** no teclado enquanto digitalização
- é fácil e rápida de usar

You can read more about this feature [here](http://www.lutraconsulting.co.uk/blog/2016/02/16/qgis-trace-digitising/) and with [this tutorial](http://www.lutraconsulting.co.uk/products/autotrace/TraceDigitising).

Este recurso foi financiado por: The Royal Borough of Windsor and Maidenhead, Neath Port Talbot County Borough Council, Ujaval Gandhi, Surrey Heath Borough Council, Matias Arnold, Northumberland National Park Authority, Buccleuch Estates Limited, Countryscape

![image46](images/entries/357ff84cf7685a2686a019ebe42f0012b495f79a.png.400x300_q85_crop.webp)

This feature was developed by [Lutra Consulting](http://www.lutraconsulting.co.uk)
## Rótulo
### Feature: \"Cartographic\" placement mode for point labels
Nesse modo de veiculação, os candidatos a marcadores de ponto são gerados seguindo as regras de posicionamento cartográfico ideais, por exemplo, as veiculações de rótulo são priorizadas na ordem:
- superior direito
- superior esquerdo
- inferior direito
- inferior esquerdo
- meio direito
- meio esquerdo
- superior, levemente à direita
- inferior, levemente à esquerda

(respeitando as orientações do Krygier e Wood (2011) e outras obras-primas cartográficas)

Prioridade de colocação também pode ser definida para uma feição individual usando uma lista definida de dados de posições priorizadas. Isso também permite que apenas determinados canais serem utilizados, assim, por exemplo, para as feições costeiras você poderia evitar que as etiquetas fossem colocadas sobre a terra.

![image53](images/entries/23cdbb38f45b05ea930fbeec8ad461e2616ef2a9.png.400x300_q85_crop.webp)

Este recurso foi financiado por  Andreas Neumann

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Funcionalidade: Aplicando rótulo por distância de limites do símbolo
Quando essa configuração está ativa, a distância do rótulo aplica-se a partir dos limites do símbolo rendida por um ponto, em vez de o próprio ponto. É especialmente útil quando o tamanho do símbolo não é fixo, por exemplo, se ele é definido por um tamanho definido de dados ou quando utilizar símbolos diferentes em um renderizador categorizados.

Note que esta definição só está disponível com o novo modo de colocação de rótulo de ponto cartográfico.

![image54](images/entries/9469a985c317ec310e8506e27da5148cedbb93c0.png.400x300_q85_crop.webp)

Este recurso foi financiado por  Andreas Neumann

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Funcionalidade: controle sobre a ordem de renderização rótulo
A new control for setting a label\'s \"z-index\" has been added to the labeling properties dialog. This control (which also accepts data-defined overrides for individual features) determines the order in which labels are rendered. Label layers with a higher z-index are rendered on top of labels from a layer with a lower z-index.

Além disso, a lógica foi ajustada de modo que se 2 rótulos têm correspondência z-índices, então:
- Se eles são da mesma camada, um rótulo mais pequeno irá sempre ser retirada acima de um rótulo maior
- se eles são de diferentes camadas, os rótulos serão desenhados na mesma ordem como as próprias camadas (ou seja, respeitando a ordem definida na legenda)

Os diagramas também podem ter o seu índice z ajustado (mas não de dados definidos) de modo que a ordem de rotulagem e diagramas pode ser controlada.

Note que este *NÃO* permitir que os rótulos sejam traçados abaixo as feições de outras camadas, ele só controla a ordem em que os rótulos são desenhados em cima de seu mapa.

![image55](images/entries/52f3e941b047714fbaf81adc7a226e4808a82d09.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Funcionalidade: símbolo real agora é considerado como um obstáculo para os rótulos de feições de ponto
Anteriormente, apenas o recurso próprio de ponto era tratado como um obstáculo para os rótulos. Se um símbolo grande fosse utilizado para o ponto, em seguida, as etiquetas foram autorizadas a se sobrepor a este símbolo sem incorrer no custo de obstáculo.

Agora, o tamanho real e deslocamento do símbolo prestados são considerados quando detectar se um rótulo colide com uma feição de ponto. O resultado é que o QGIS agora evita rótulos sobre símbolos de pontos em mais circunstâncias.

![image56](images/entries/7d4d3117427f938ec3a5a4a1ed013e8e4445db60.png.400x300_q85_crop.webp)

Este recurso foi financiado por City of Uster

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
## Camada legenda
### Funcionalidade: Cole um estilo para várias camadas selecionadas ou todas as camadas em um grupo na legenda
Esse recurso adiciona a possibilidade de colar o estilo de uma camada para a camada ou grupo de camadas selecionadas.

![image57](images/entries/63fd1bfff18a108796c400edf127367f30f93c4b.png.400x300_q85_crop.webp)

Esta funcionalidade foi desenvolvida por Salvatore Larosa
### Funcionalidade: Filtro de legenda por expressão
Agora é possível filtrar elementos da legenda por uma expressão. Ele foi projetado com a filtragem da simbologia ou categorização baseado em regras.

A filtragem de legenda está disponível na legenda do aplicativo principal, bem como para componentes de legenda do compositor do QGIS.

![image59](images/entries/8c957ae820bc98f0a23a7d660abd40264af6e31d.png.400x300_q85_crop.webp)

This feature was funded by [Agence de l\'Eau Adour-Garonne (Adour-Garonne Water Agency)](http://www.eau-adour-garonne.fr)

This feature was developed by [Hugo Mercier / Oslandia](http://oslandia.com)
## Compositor de mapas
### Funcionalidade: Novas opções para elementos de filtragem de legenda
Este apresenta duas novas opções para filtrar elementos de legenda.

O primeiro, filtrar por expressão, permite aos usuários definir uma expressão para filtragem que devem ser mostrados na legenda. Somente símbolos com uma feição de correspondência serão mostrados na legenda.

A segunda opção de filtro permite que uma legenda do compositor seja filtrada para incluir somente itens que estão contidos dentro do polígono do atlas atual.

![image58](images/entries/cf32cc889370df205de51af684c4e683c3ec2dc4.png.400x300_q85_crop.webp)

This feature was developed by [Hugo Mercier (Oslandia)](http://oslandia.com/)
### Funcionalidade: caminhos adicionais para modelos do compositor
You can now define custom paths that should be used for QGIS to find composer templates. This means that you can for example put a bunch of templates in a network share and give your users access to that folder in addition to the local ones that exist on their own system. To manage the composer template search paths, look in `Settings -> Options -> Composer`

![image60](images/entries/bd36891d76ee01ee79e516b0167f403a89fa49de.png.400x300_q85_crop.webp)

Este recurso foi desenvolvido por Nathan Woodrow
### Funcionalidade: Seleção múltipla de composições no gerenciador
O Gerenciador do compositor ganhou suporte para o gerenciamento de várias composições, ao mesmo tempo. Agora você pode abrir ou excluir várias composições de uma só vez usando a tecla Ctrl e selecionando várias composições da lista.

![image61](images/entries/2603b37c6a6ccec10f56f37951d9494cb44c8d0a.png.400x300_q85_crop.webp)

This feature was developed by [Médéric Ribreux](https://medspx.fr)
## Complementos
### Funcionalidade: suporte do sistema de autenticação para o gerenciador de complementos
Suporte para o novo sistema de autenticação foi adicionado ao gerenciador de complementos. Isto permite aos usuários aplicar configurações de autenticação para ligações a repositórios de complementos, e administradores de sistema para criar o acesso autenticado a repositórios de plugins e/ou os pacotes de download de complementos.

![image62](images/entries/7b66e68eb37b27b0ecabcab7d0656985e222e8c0.png.400x300_q85_crop.webp)

This feature was funded by [Boundless Spatial](http://boundlessgeo.com)

Esta funcionalidade foi desenvolvida por Larry Shaffer
## Processamento
### Funcionalidade: Novos algorítimos no QGIS 2.14
#### Geoalgorítimos QGIS
- Suave: para alisar camadas de linha ou polígono.
- Inverter direção de linha.

#### geoalgoritimos GDAL/OGR:
- gdal2tiles: constrói um diretório com mosaicos TMS, PMSL e telespectadores web simples.
- gdal_retile: retiles a set of tiles and/or build tiled pyramid levels.

### Funcionalidade: testes de unidade Q/A
Para garantir a estabilidade a longo prazo do módulo de processamento, foi introduzida uma nova estrutura de teste.

Processamento de geo-algoritmos são executados após cada mudança que atinge o código-fonte do QGIS e o resultado é comparado com um conjunto de dados de controle para garantir o comportamento correto. Isto dá um feedback imediato sobre possíveis regressões.

It is possible - and desired - that more tests are added. You can read more about [how to participate](https://www.opengis.ch/2016/02/04/increasing-the-stability-of-processing-algorithms/).

![image63](images/entries/4121e58bd51cfe5c8b2c0cd14d1420eaeb1f4473.png.400x300_q85_crop.webp)

This feature was funded by [The QGIS Project](https://www.qgis.org)

This feature was developed by [Matthias Kuhn, OPENGIS.ch](https://opengis.ch)
### Funcionalidade: Melhoria da caixa de ferramentas
A interface simplificada foi removida e um novo e mais amigável sistema de gerenciamento de provedores foi adicionado. A funcionalidade de pesquisa de algoritmo agora também pesquisa em provedores que não estão ativos e sugere ativá-los.

![image64](images/entries/2a135d5384f592e77938c59c0563cc2d0f6c3ebf.jpg.400x300_q85_crop.webp)

This feature was funded by [Boundless Spatial](http://boundlessgeo.com/)

Este recurso foi desenvolvido por Víctor Olaya
### Funcionalidade: processos de lote podem ser salvos e mais tarde recuperados a partir da interface de processamento em lote
![image65](images/entries/f8dec7fbc9e74dc3f4078f9710984d44b26c4fa3.jpg.400x300_q85_crop.webp)
### Funcionalidade: janelas de algoritmo mais informativas
Uma breve descrição agora é mostrada junto com os parâmetros do algoritmo, tornando fácil de entender o propósito do algoritmo.

Also, batch processes can be now started from the algorithm dialog, using the "Run as batch process..." button

![image66](images/entries/c4039a87ddc906921e5e3ce47f8c7aadc7ab2263.jpg.400x300_q85_crop.webp)
### Funcionalidade: módulos GRASS7 v.net
QGIS 2.14 Processing now incorporates v.net GRASS modules (only for GRASS7). Those modules are a set of algorithms that perform on graph line vector layers (networks). [A graph](https://en.wikipedia.org/wiki/Graph_theory#Graph) is a set of vertices (or nodes or points) linked together with a set of edges (or arcs or lines). The set of edges is often called a network.

Thanks to v.net modules, you can easily calculate the shortest path between a set of nodes on the network or even compute the [isochrone map](https://en.wikipedia.org/wiki/Isochrone_map) from a set of central points. you can also easily solve [the complex travelling salesman problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem) from a network and a set of travel nodes.

algoritmos v.net muitas vezes usam uma camada de vetor de linha (para a rede) e uma camada de pontos que representar os nós que pretende utilizar para o cálculo. Certifique-se de usar uma camada de vetor de linha do gráfico verdade para a camada da rede (arestas precisam ser conectadas em vértices sem interseção entre bordas) para evitar problemas. Você também pode usar qualquer atributo da camada da rede para o cálculo de custos (o conteúdo do atributo é usado para calcular o custo de viagem da borda).

Aqui está um rápido resumo dos diferentes algoritmos que foram incluídos no processamento:
- v.net.alloc: Aloca sub-redes dos centros mais próximos.
- v.net.allpairs: Calcula o caminho mais curto entre todos os pares de nós na rede.
- v.net.arcs: Cria arcos de um arquivo de pontos.
- v.net.articulation: Computes the [articulation points](https://en.wikipedia.org/wiki/Biconnected_component) in the network.
- v.net.bridge: Computes [bridges](https://en.wikipedia.org/wiki/Bridge_%28graph_theory%29) of the network.
- v.net.centrality: Calcula grau, centralidade, betweenness, proximidade e eigenvector centralidade de cada nó da rede.
- v.net.components: Calcula componentes fortemente e fracamente ligados em rede.
- v.net.connect: Conecta pontos (nós) aos arcos mais próximos da rede (e adiciona bordas, se necessário).
- v.net.connectivity: Calcula conectividade de vértices entre dois conjuntos de nós na rede.
- v.net.distance: Calcula o caminho mais curto através da rede entre dois conjuntos de nós.
- v.net.flow: Calcula o fluxo máximo entre dois conjuntos de nós na rede.
- v.net.iso: Calcula o mapa isochrone da rede a partir de um conjunto de nós.
- v.net.nodes: Extrai nós de uma camada de rede/gráfico.
- v.net.nreports: Relata informações sobre os nós.
- v.net.path: Localiza o caminho mais curto na rede entre dois nós.
- v.net.report: Relata informações sobre as bordas da rede.
- v.net.salesman: Computes the [travelling salesman path](https://en.wikipedia.org/wiki/Travelling_salesman_problem) from a set of nodes on the network.
- v.net.spanningtree: Computes the [Spanning tree](https://en.wikipedia.org/wiki/Spanning_tree) of the network.
- v.net.steiner: Creates [a Steiner tree](https://en.wikipedia.org/wiki/Steiner_tree_problem) for the network and given nodes.
- v.net.visibility: Executa a construção do gráfico de visibilidade.

Use the \"Help\" tab on each of the v.net Processing algorithm to read [the official GRASS7 documentation](https://grass.osgeo.org/grass70/manuals/topic_network.html) directly for more information.

![image67](images/entries/655bbfccc4997a5a3e3d1f5c709da5277eef6000.png.400x300_q85_crop.webp)

This feature was developed by [Médéric Ribreux](https://medspx.fr)
## Programabilidade
### Funcionalidade: editor de função de expressão remodelado
Com autosalvamento

![image68](images/entries/b42e959476310932713777f75f5eced4826df20a.png.400x300_q85_crop.webp)
### Funcionalidade: Armazenamentno de código python de inicialização para o projeto
Adds an option and code editor to store python form init code into the project (and the DB, since it\'s in the style section)

![image69](images/entries/67bad1306d40aa9b32b64f4d025b77649ae2f775.png.400x300_q85_crop.webp)
### Funcionalidade: Novas opções de filtragem e ordenação para solicitação QgsFeature
QgsFeatureRequest agora suporta a configuração de um limite máximo para o número de recursos retornados. Em muitos casos, esse limite é passado para o provedor, resultando em ganhos significativos de desempenho quando apenas um número definido de recursos é necessário.

Additionally, QgsFeatureRequest now supports setting ordering for returned features. Again, in many cases this ordering is delegated to the provider so that it is performed \"server side\" for optimal performance.

![image70](images/entries/6e136c8a4bdf4361b9307f88175369b62d4648d6.png.400x300_q85_crop.webp)
### Funcionalidade: formulário de opções de personalizadas de feições do código Python 
Este recurso adiciona mais opções para o código de recurso de formulário personalizado do Python:
- Carregamento de arquivo (com widget de arquivo picker)
- Carregamento no ambiente (ou seja, um plug-in ou uma função Python init)
- entrar diretamente no código em um widget de entrada (opção nova)

As opções de configuração, incluindo o código Python personalizado inserido na janela são armazenados no projeto, bem como nas definições QML e podem ser exportados/restaurados a partir de um banco de dados.

![image71](images/entries/65e82ab529ee1287c631712127e1ac75f78d05c6.png.400x300_q85_crop.webp)

This feature was funded by [ARPA Piemonte](http://www.arpa.piemonte.gov.it/)

This feature was developed by [Alessandro Pasotti (ItOpen)](http://www.itopen.it)
### Funcionalidade: Novas classes PyQGIS no QGIS 2,14
### Novas classes do núcleo
- [QgsAttributeEditorElement](https://qgis.org/api/classQgsAttributeEditorElement.html)
  - abstract base class for any elements of a drag and drop form
- [QgsAttributeEditorContainer](https://qgis.org/api/classQgsAttributeEditorContainer.html)
  
  \- container for attribute editors, used to group them visually in an attribute form
- [QgsAttributeEditorField](https://qgis.org/api/classQgsAttributeEditorField.html)
  - element for loading a field\'s widget onto a form
- [QgsAttributeEditorRelation](https://qgis.org/api/classQgsAttributeEditorRelation.html)
  - element for loading a relation editor widget onto a form
- [QgsEditFormConfig](https://qgis.org/api/classQgsEditFormConfig.html)
  - stores and sets configuration parameters for attribute editor forms
- [QgsFeatureFilterProvider](https://qgis.org/api/classQgsFeatureFilterProvider.html)
  
  \- provides an interface for modifying a QgsFeatureRequest in place to apply additional filters to the request
- [QgsTracer](https://qgis.org/api/classQgsTracer.html) - provides graph creation and shortest path search for vector layers
- [QgsTransactionGroup](https://qgis.org/api/classQgsTransactionGroup.html)
  - interface for grouping layers into single edit transactions
- [QgsUnitTypes](https://qgis.org/api/classQgsUnitTypes.html) -helper functions for various unit types and conversions between units (eg distance and area units)
- [QgsVirtualLayerDefinition](https://qgis.org/api/classQgsVirtualLayerDefinition.html)
  - class for manipulating the definitions of virtual layers
- [QgsVirtualLayerDefinitionUtils](https://qgis.org/api/classQgsVirtualLayerDefinitionUtils.html)
  - helper utilities for working with QgsVirtualLayerDefinition objects
- [Qgs25DRenderer](https://qgis.org/api/classQgs25DRenderer.html) -2.5D symbol renderer
- [QgsGeometryGeneratorSymbolLayerV2](https://qgis.org/api/classQgsGeometryGeneratorSymbolLayerV2.html)
  - geometry generator symbol layer
- [QgsFeatureRequest.OrderByClause](https://qgis.org/api/classQgsFeatureRequest_1_1OrderByClause.html)
  - class for specifying a field sort order for feature requests
- [QgsFeatureRequest.OrderBy](https://qgis.org/api/classQgsFeatureRequest_1_1OrderBy.html)
  - a prioritized list of order by clauses for sorting

### Novas classes da GUI
#### Widgets reutilizáveis:
- [QgsExternalResourceWidget](https://qgis.org/api/classQgsExternalResourceWidget.html)
  
  \- widget for displaying a file path with a push button for an \"open file\" dialog, and optional display of pictures or HTML files
- [QgsFileWidget](https://qgis.org/api/classQgsFileWidget.html) -widget for selecting a file or a folder
- [QgsLegendFilterButton](https://qgis.org/api/classQgsLegendFilterButton.html)
  
  \- tool button widget that allows enabling or disabling legend filter by contents of the map
- [QgsMapCanvasTracer](https://qgis.org/api/classQgsMapCanvasTracer.html)
  
  \- an extension of QgsTracer that provides extra functionality for interacting with map canvases
- [Qgs25DRendererWidget](https://qgis.org/api/classQgs25DRendererWidget.html)
  - widget for setting properties for a 2.5D renderer
- [QgsColorWidgetAction](https://qgis.org/api/classQgsColorWidgetAction.html)
  - widget action for embedding a color picker inside a menu

#### Janelas reutilizáveis:
- [QgsStyleV2GroupSelectionDialog](https://qgis.org/api/classQgsStyleV2GroupSelectionDialog.html)
  - dialog for grouping selections in a style
- [QgsGroupWMSDataDialog](https://qgis.org/api/classQgsGroupWMSDataDialog.html)
  - dialog for setting properties for a WMS group
- [QgsOrderByDialog](https://qgis.org/api/classQgsOrderByDialog.html)
  - dialog for specifying sort ordering of fields

## QGIS Server
### Funcionalidade: Solicitações de parâmetros STARTINDEX em WFS GetFeature
`` `STARTINDEX `` is standard in WFS 2.0, but it\'s an extension for WFS 1.0 implemented in QGIS Server.

`STARTINDEX` can be used to skip some features in the result set and in combination with `MAXFEATURES` provides for the ability to use WFS GetFeature to page through results. Note that `STARTINDEX=0` means start with the first feature, skipping none.

This feature was developed by [3Liz](http://3liz.com)
### Funcionalidade: showFeatureCount em GetLegendGraphic
Add non-standard parameter **showFeatureCount** to add feature count in the legend. To activate it,**showFeatureCount** can be set to *TRUE* or *1*.

Esse recurso precisa de um servidor X falso.

![image72](images/entries/95f13aa3a1f4cb4ca8cbf7ce30e6bb278e6b9cd8.png.400x300_q85_crop.webp)

This feature was developed by [3Liz](http://3liz.com)
### Funcionalidade: Opção para evitar artefatos nas bordas de mosaicos
![image73](images/entries/1ded32aa2bb962fde1b9f00b891b2a04406be621.png.400x300_q85_crop.webp)
### Funcionalidade: verificador de configuração nas propriedades do projeto
Para ajudar com a configuração de um projeto para o servidor QGIS, um novo verificador de configuração foi adicionada às propriedades do projeto.

Os testes de verificador por erros como:
- nomes duplicar ou nomes abreviados usados como nomes OWS
- nomes OWS inválidos
- faltando codificações em camada vetorial

![image74](images/entries/c548fc562785f400d3000e7ae1f61705c333026c.png.400x300_q85_crop.webp)

This feature was funded by [Ifremer](http://wwz.ifremer.fr/institut_eng/)

This feature was developed by [3Liz](http://3liz.com)
### Funcionalidade: Capacidades WMS INSPIRE
Nas propriedades do projeto o usuário pode:
- ativar capacidades INSPIRE
- selecionar o idioma para o serviço, a partir de 24 línguas oficiais da UE + 5 idiomas regionais
- escolher o cenário para metadados de serviço e especificar seus parâmetros

As capacidades WMS 1.3.0 refletem a configuração INSPIRE.

![image75](images/entries/4ee445bcb5e9eab3fb9bf2eda8f9b1b81bbe21c0.png.400x300_q85_crop.webp)

This feature was developed by [3Liz](http://3liz.com)
### Funcionalidade: Adicionar nome curto para camadas, grupos e projeto
Um certo número de elementos tem um **Nome** e **Título**. O nome é uma cadeia de texto utilizada para comunicação de máquina-a-máquina, enquanto o título é para o benefício dos seres humanos. Por exemplo, um conjunto de dados pode ter o título descritivo *Temperatura Máxima atmosférica* e ser solicitado usando o nome abreviado *Tmáx*.

Os usuários já podem definir um título para camadas e projeto. Serviços da Web OpenGeospatial, OWS (WMS, WFS, WCS), o nome é baseado no nome usado na árvore de camadas. Este nome é mais um rótulo para humanos do que um nome para comunicação máquina-a-máquina.

Para adicionar a capacidade para os usuários definirem o Nome como uma cadeia de texto para comunicação máquina-a-máquina, esse recurso adiciona:
- Edição de nome curto para propriedades da camada
- Janelas de dados WMS para a árvore do grupo camada (nome abreviado, título, resumo)
- short name line edits to project properties
- add a regexp validator \"\^\[A-Za-z\]\[A-Za-z0-9.\_-\]\*\" to short name line edit accessible through a static method
- adicionar um elemento Treename nas configurações do projeto completo

De um nome curto foi definido para camadas, grupos e projeto é usado pelo Servidor QGIS como o nome da camada.

![image76](images/entries/e2345455bda9f0ed3da5e1c2750d6e2239ab8a86.png.400x300_q85_crop.webp)

This feature was developed by [3Liz](http://3liz.com)
## Simbologia
### Funcionaldiade: assistente de tamanho de largura variável de linha
![image77](images/entries/1d891425b0e1b9927ced6aab3e0353aed92608de.png.400x300_q85_crop.webp)
### Funcionalidade: Suporte de transparência em parâmetros de cor SVG
SVGs não empacotados para adicionar:

`fill-opacity="param(fill-opacity)"`

e

`stroke-opacity="param(outline-opacity)"`

para ativar o suporte a transparência.

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Funcionalidade: a duplicação fácil símbolos de camadas 
A new \"duplicate\" button has been added to the symbol properties dialog, which allows symbol layers to be easily duplicated.

![image78](images/entries/a6e2ad682852a2fb8b635395ec75f83ef584621d.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Funcionalidade: Rendererisador 2.5D
Isso adiciona uma interface de configuração e renderização que o torna fácil de colocar todas as partes juntas que são necessárias para obter um efeito 2.5D.

Ele permite configurar alguns dos estilos e destinir se deve criar uma instalação fácil de usar.

Since every part of the system is built around QGIS\' internal rendering and symbology engine, there is much to fine tune. To get all the possibilities, just change the renderer to a graduated, categorized or single symbol renderer upon creation and you will find full access to improve the style to your needs.

**Este recurso foi desenvolvido por**:
- Matthias Kuhn at [OPENGIS.ch](https://opengis.ch)

**Este recurso foi financiado por**:
- Regional Council of Picardy
- ADUGA
- Ville de Nyon
- Wetu GIT cc

![image79](images/entries/8d66f8838011e7bc8fae540d56bf9ef6db20db68.jpg.400x300_q85_crop.webp)
### Funcionalidade: Permitir definição de ordem de renderização para feições
Quando feições necessitam ser renderizadas em uma ordem particular, este recurso pode ser especificado, usando uma expressão arbitrária.

This can be configured in the layer\'s symbology configuration dialog and can be a simple field or a complex expression.

Fornece controle sobre ordem crescente ou decrescente, bem como se nulos são primeiro ou último.

Se possível, o pedido será enviado para o banco de dados (isso depende da complexidade da expressão, bem como do fornecedor da camada). Se não for possível enviar a solicitação para o banco de dados, o pedido será realizado na máquina local.

This is used by the 2.5D renderer to render features based on their distance from the \"camera\".

Isto também está disponível para complementos:

    layer.getFeatures( QgsFeatureRequest().setOrderBy( 'name' ) ) -- alphabetical by name
    
**This feature was developed by**: Matthias Kuhn at [OPENGIS.ch](https://opengis.ch) **This feature was funded by**: Regional Council of Picardy, ADUGA, Ville de Nyon, Wetu GIT cc

![image80](images/entries/e06cf21a35e070a28ce5b3b98c92f2fb1c1b881d.png.400x300_q85_crop.webp)

This feature was developed by [Matthias Kuhn, OPENGIS.ch](https://opengis.ch)
### Funcionalidade: gerador de geometrias de símbolos 
O gerador de símbolos de geometria permitir o uso do mecanismo de expressão para modificar a geometria antes de processar ou mesmo a criação de novas geometrias durante a prestação com base em atributos de feições.

Isso pode usar todos os tipos de operadores espaciais como buffer, translate, intersect ou extrude com parâmetros baseados em atributos apenas para a renderização sem realmente modificar os dados na origem.
### Exemplos
#### Traduzindo uma geometria
Usado pelo o renderizador de mosaicos 2.5D

    translate( $geometry, 10, 10 )
    
#### Estilo de preenchimento para polígono
Isto gera um polígono que representa o contorno do polígono inicial (Exemplo na imagem)

    difference( buffer( $geometry , 250 ), buffer( $geometry, -250 ) )
    
camadas com símbolos diferente podem conter geradores de geometria diferentes, isto permite que apresentam diferentes versões de uma geometria, ao mesmo tempo. O representante 2.5D serve como um exemplo.

![image81](images/entries/b06b6bc93644c051c13de162b45d9486b7af769a.png.400x300_q85_crop.webp)

Este recurso foi financiado por Regional Council of Picardy, ADUGA, Ville de Nyon, Wetu GIT cc

This feature was developed by [Matthias Kuhn, OPENGIS.ch](https://opengis.ch)
## Interfaçe de usuário
### Funcionalidade: tabela de atributos podem ser atualizadas
Uma opção para recarregar atributos dentro da tabela de atributo já está disponível.

![image82](images/entries/4623399cb1f63e2c6fa80c72a6aea17b6c63bb3e.png.400x300_q85_crop.webp)
### Funcionalidade: Renderizador diretamente definido e símbolo de classe de cores do menu de contexto na legenda
Mostra um widget de paleta de cores no menu, o que permite que você edite a cor de um símbolo de forma interativa, sem ter que abrir uma única caixa de diálogo!

![image83](images/entries/3159457a414ea61f8f40659af5c9561882a44fe1.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Funcionalidade: Editar símbolos da legenda diretamente na árvore de camadas
This adds a new \"edit symbol\" item to the right-click menu for a renderer child legend item (eg categories for the categorised renderer). Selecting it opens a symbol editor dialog which allows for directly editing the class\'s symbol. It\'s much faster than opening the layer properties and going through the style tab. You can also double-click on a child item to open the symbol editor immediately.

![image84](images/entries/e7b2447e329507f0b27e855111ffa038b1ccc353.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Funcionalidade: Mostrar/ocultar todos os itens de legenda através do menu de contexto
Allows toggling on/off all the symbol items for categorized/graduated/rule-based layers via the right click menu on an item. Previously you\'d have to toggle each item manually one-by-one.

![image85](images/entries/c526cf9c28c92dde193490a2707c1fe2e0a58ea6.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)

{{<content-end >}}
