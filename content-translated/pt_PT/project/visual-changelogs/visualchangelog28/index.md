---
HasBanner: false
draft: false
releaseDate: '2015-02-20'
section: projeto
sidebar: true
title: Ficheiro de alterações para o QGIS 2.8
type: visual-changelog

---
{{<content-start >}}
# Ficheiro de alterações para o QGIS 2.8{#changelog28 }
Release date: 2015-02-20

This is the change log for the next release of QGIS - version 2.8 \' Wien\'. Wien is German for \'Vienna\' - host city to our developer meet up in November 2009 and again in March 2014.

**Lançamento de Longo Prazo**

This is a special release since it is designated an \'LTR\' (Long Term Release). LTR releases will be supported with backported bug fixes for one year, and will be in permanent feature freeze (i.e. no new features will be added, only bug fixes and trivial updates).

O objetivo das versões LTR é fornecer uma plataforma estável e como alterações menos frequentes para empresas e organizações que não querem lidar com atualização das capacidades dos utilizadores, material de formação, etc. mais do que uma vez por ano. O sucesso da LTR depende de vós, nossos adorados utilizadores - precisamos do vosso apoio para ajudar a financiar a correção de erros e a garantir que, nos contratos de suporte técnico, quaisquer correção de erros feito em seu nome são aplicados tanto ao branch LTR como no nosso branch de desenvolvimento normal.

Se um LTR é importante para si, considere por favor suportar diretamente o projeto QGIS, ou encoraje o seu apoio técnico a usar o LTR como base para a solução empresarial de forma a que todos possa beneficiar de uma plataforma estável e em constante melhoria e refinamento. Note que, para utilizadores e organizações que gostam de trabalhar no fio da navalha, os lançamentos regulares a cada quatro meses continuarão.

**Novas Funcionalidades**

O QGIS 2.8 é também uma versão especial pelo facto de incluir novas funcionalidades fantásticas, otimizações e melhorias para tornar o mais popular SIG desktop livre ainda mais útil e funcional.

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

**Agradecimentos**

Gostaríamos de agradecer aos programadores, escritores de documentação, testers e todos aqueles que disponibilizaram o seu tempo e esforço (ou que financiaram quem o fizesse).

From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

Finalmente, gostaríamos de agradecer aos nossos patrocinadores oficiais pelo suporte financeiro de valor inestimável que fornecem a este projeto:
- **GOLD Sponsor: Asia Air Survey, Japan** <http://www.asiaairsurvey.com/>
- SILVER Sponsor: [Sourcepole AG, Switzerland](http://www.sourcepole.com/)
- SILVER Sponsor: [State of Vorarlberg, Austria](http://www.vorarlberg.at/)
- SILVER Sponsor: [Office of Public Works, Ireland, Ireland](http://www.opw.ie/)
- BRONZE Sponsor: [GIS3W, Italy](http://www.gis3w.it/)
- BRONZE Sponsor: [www.molitec.it, Italy](http://www.molitec.it/)
- BRONZE Sponsor: [www.argusoft.de, Germany](http://www.argusoft.de)
- BRONZE Sponsor: [www.openrunner.com, France](http://www.openrunner.com)
- BRONZE Sponsor: [GKG Kassel,(Dr.-Ing. Claas Leiner), Germany](http://www.gkg-kassel.de/)
- BRONZE Sponsor: [Customer Analytics, USA](http://www.customeranalytics.com/)
- BRONZE Sponsor: [Urbsol, Australia](http://www.urbsol.com.au/)
- BRONZE Sponsor: [MappingGIS, Spain](http://www.mappinggis.com/)
- BRONZE Sponsor: [Lutra Consulting, UK](http://www.lutraconsulting.co.uk/)
- BRONZE Sponsor: [ADLARES GmbH, Germany](http://www.adlares.com/)
- BRONZE Sponsor: [Avioportolano Italia, Italy](http://www.avioportolano.it/)
- BRONZE Sponsor: [Faculty of Geology, Geophysics and Environmental Protection, AGH, ​University of Science and Technology, Poland](http://www.wggios.agh.edu.pl/en)

A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become an official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts.

If you enjoy using QGIS, please consider making a donation to support the project - either [financial](https://qgis.org/en/site/getinvolved/donations.html) or of [your time and skills](https://qgis.org/en/site/getinvolved/index.html)! Lastly we would like to also take a moment to encourage you to fund a [special campaign](http://blog.vitu.ch/10102014-1046/crowdfunding-initiative-automated-testing) by one of our QGIS developers to get a working test suite for QGIS so that we can improve out quality assurance process and deliver you the best possible releases.

O QGIS é um software livre e você não tem qualquer obrigação de pagar o que quer que seja para poder usá-lo - na verdade, queremos incentivar as pessoas de todo o mundo a usá-lo, independentemente do seu estatuto financeiro ou social - acreditamos que dotar as pessoas com ferramentas espaciais de apoio à decisão resultará numa sociedade melhor para toda a humanidade.

{{<table-of-contents >}}
## Geral
### Funcionalidade: Usar expressões em spin boxes
When editing attributes in the **attribute table or forms**, you can now enter expressions directly into spin boxes, e.g. `5 * 2.5` and they will be automatically evaluated.

![](images/entries/e094287244ee1fe161c8ca95951c2d11ca1e6cdd.webp)
### Funcionalidade: É possível importar/exportar marcadores
Agora é possível gravar / carregar os seus marcadores num ficheiro. O que torna simples partilhar de localizações guardadas, ou transferi-las entre computadores.

** Esta funcionalidade foi desenvolvida por:** Salvadore Larosa

![](images/entries/e3d35c32da659821bc0c657b8e7ba40587a1bfb2.webp)
### Funcionalidade: Melhorias nas expressões
- **Integer division produces a double when required**: Previously dividing two integers in an expression would always result in an integer value, i.e. `5 / 2 = 2`. Now the result will always be double when required, so `5 / 2 = 2.5`, which is much more expected for users. A new integer divide operator - `//` has been added to mimic the old behaviour, i.e. `5 // 2 = 2`.
- **New \'if()\' function**: There is now a new `if(cond, true, false)` expression
- **Lazy evaluation for expressions**
- **Added get and transform geometry**: These new keywords can be used with `getFeature` for some geometry tests like intersects, crosses, contains, etc.
- `geometry` - returns the feature\'s geometry
- `transform` - returns the transformed geometry

![](images/entries/ec56f9b8331e619ad1a44970fde655b68125f9d8.webp)
### Elemento: Teste contínuo da infraestrutura e melhorias QA
In our ongoing quest to improve the stability and quality of QGIS, every commit is now tested against a growing test suite to identify regressions automatically. In the image on the right you can see the list of incoming pull requests on our GitHub page are now automatically annotated with a check or cross based on whether our test suite successfully ran on [Travis.ci](https://travis-ci.org/qgis/QGIS) when the pull request is made or updated.

We are also now regularly performing Coverity scans of QGIS codebase. As a result of this, we have identified and fixed over 1000 flagged issues, including memory leaks and potential crashes. QGIS has a defect density of 0.01 wheras the average for programs of similar size is about 1.0.

![](images/entries/4ec86080ff150743f1bdc88d3ac7881a6cd405de.webp)
## Ferramentas de Análise
### Funcionalidade: Melhoria do diálogo de medição
A ferramenta de medição foi melhorada para que possa selecionar que unidades devem ser usadas no diálogo de medição. Existe também uma nova secção de informação no diálogo que mostra as configurações que são usadas durante os cálculos da medição.

![](images/entries/67a001d3d800feec8805de698ed364e91d00daab.webp)
## Navegador
### Navegador mais responsivo
In the QGIS Browser items are now expanded in their own threads, speeding up the load time of the browser and making the browser more responsive. Navigating PostGIS sources is now much faster in the browser. The animated snapshot to the right (click image to see the animation) shows the loading of two slow WMS servers in parallel . The browser\'s state (tree expansion) is restored on startup.

**Esta funcionalidade foi desenvolvida pelo:** Radim Blazek

![](images/entries/c8df646572084b8f12027fd54c1210f14c80c8e1.gif)
## Fornecedores de Dados
### Funcionalidade: Suporte para a legenda gráfica contextual do WMS
If your WMS server supports contextual legends, you can make use of them in QGIS now too. Contextual legends are getLegendGraphic requests which return only the relevant legend for your current view extent, and thus do not include legend items for things you can\'t see in the current map.

**This feature was funded by:** [Regione Toscana](http://www.regione.toscana.it/)

**This feature was developed by:** [Faunalia](http://www.faunalia.eu/)

![](images/entries/e516a25492b547113c487d00475cfe07bc7b131e.webp)
## Gestão de Dados
### Funcionalidade: prefixo personalizável para as uniões
You can now define a custom prefix in the joins manager in the layer properties dialog. When using a prefix, the attribute table in will show joined attribute names with your preferred prefix.

![](images/entries/372e6561a4db3ed3ca3d418c946f81bce0d0d134.webp)
### Funcionalidade: Suporte para a criação de camadas de memória temporárias
This release add support for creating new temporary scratch layers within QGIS core. Scratch layers can be created in the `Layer --> Create layer --> New Temporary Scratch Layer` menu option.

![](images/entries/bddbbd6cb55e9a19441ea564275dd480661e61de.webp)
### Funcionalidade: Suporte para os cálculos em linhas selecionadas
Na tabela de atributos pode agora fazer cálculos de linhas selecionadas graças ao novo botão adicionado ao campo da barra da calculadora de campos.

![](images/entries/1b7ead001901ed4242d26556abac055834e367b2.webp)
## Digitalização
### Funcionalidade: Ferramentas de digitalização avançada
If you ever wished you could digitise lines exactly parallel or at right angles, lock lines to specific angles and so on in QGIS, now you can! The advanced digitizing tools is a port of the CADinput plugin and adds a new panel to QGIS. The panel becomes active when capturing new geometries or geometry parts

![](images/entries/50f726e5899eb72dcec76e4bed1936bcf957e75f.webp)
### Funcionalidade: Melhoria na ferramenta de simplificação
A ferramenta de simplificação foi reformulada, adicionando:
- Suporte na reprojeção OTF
- o utilizador pode especificar a tolerância exata (não apenas para valores relativos)
- a tolerância pode ser especificada em unidades de mapa ou em unidades da camada ou em pixeis
- as configurações da tolerância são armazenadas nas configurações
- simplificar elementos múltiplos de uma só vez (em vez de um só clique, arraste o retângulo)
- suporte para elementos multiparte
- estatísticas sobre a redução do número de vértices

**This feature was funded by:** [Tracks for Africa](http://tracks4africa.com/)

**This feature was developed by:** [Lutra Consulting](http://www.lutraconsulting.co.uk/) in cooperation with [Kartoza](http://kartoza.com/)

![](images/entries/20b7f96ffc7d37b8c2ae09189d7957a929a716e5.webp)
### Funcionalidade: Melhorias no Snapping
There is a new snapping mode : **snap to all layers** which makes it quick to enable snapping between all layers. Also the underlying snapping architecture of QGIS has been overhauled making snapping much faster on large projects and improving the precision with which snapping takes place. ​There's also less confusion with snapping tolerances being to map units or layer units, so those anticipated 1 metre tolerances don't become 1 degree tolerances without you knowing.

**This feature was funded by:** [Ville de Vevey, SITNyon](http://www.vevey.ch/) and [QGIS Usergroup Switzerland](http://www.qgis.ch/)

**This feature was developed by:** [Lutra Consulting](http://www.lutraconsulting.co.uk/)

![](images/entries/8454af2743154585eb82325ab2694e50e7d9efcd.webp)
## Legenda da Camada
### Feature: Show rule-based renderer\'s legend as a tree
Advanced users who leverage QGIS\'s rule based renderer system will be pleased to see that the rules are now presented as a tree in the legend. Better still, each node in the **tree** can be **toggled on/off** individually providing for great flexibility in which sublayers get rendered in your map.

**This feature was funded by:** [SIGE](http://www.sige.ch/)

**This feature was developed by:** [Lutra Consulting](http://www.lutraconsulting.co.uk/) in cooperation with [Kartoza](http://kartoza.com/)

![](images/entries/0d39448aa0893d7a71c5241aa2181750535e62c3.webp)
## Compositor de Mapas
### Funcionalidade: Melhorias no GUI do compositor
- View menu option to **hide bounding boxes**. This allows users to hide the bounding boxes for selected items within a composition. It\'s a handy feature for allowing interaction with items while previewing exactly how they will look when the composition is exported, without large boxes blocking the view.
- **Modo de Ecrã inteiro para o compositor**
- Option to **toggle display of panels** in composer, available by both the `view menu`, using the shortcut `F10` and by pressing `Tab` when the composer canvas is selected. It\'s useful for maximising the space when planning a map layout.

![](images/entries/10677c6e1612a4392e8bca0a9cbe31126426becf.webp)
### Funcionalidade: Melhorias na Grelha
In the composer you now have finer control of frame and annotation display. Previously, for rotated maps or reprojected grids, the composer would draw all coordinates for every map side. This resulted in a mix of latitude/y and longitude/x coordinates showing on a side. Now you can control whether you want all coordinates, latitude only or longitude only for each map frame side. Similar options have also been added for controlling how a map grid frame is divided.

New vertical descending direction for annotations. This change adds a new descending vertical direction mode for map grid annotations. Previously only ascending text was supported for vertical annotations.

![](images/entries/288d533cbed1f6beeef17004897060c8639bbbb4.webp)
### Funcionalidade: margens do item Rótulo
- You can now control both horizontal and vertical **margins for label** items. Previously only a single margin setting would apply to both horizontal and vertical margins. This change allows users to specify different horizontal and vertical margins.
- You can now specify negative margins for label items, **allowing text to be drawn slightly outside of a label item\'s bounds**. This is desirable for aligning label items with other items while allowing for optical margin alignment for the label type.

![](images/entries/7f4905d74ca140ed369bea8866357b9d952ee212.webp)
## Plugins
### Funcionalidade: Melhorias na linha de comandos Python
You can now drag and drop python scripts into QGIS window and they will be executed automatically. We also added a toolbar icon to the plugins toolbar and a shortcut ( `Ctrl-Alt-P` ) for quick access to the python console.

![](images/entries/03be8f30ce341816bd3bcd1a58f3b913ddcea07c.webp)
## Processamento
### Funcionalidade: Novo tipo de parâmetro do atributo geométrico
With this new parameter type, used in **Select by location, Extract by location** and **Join attributes by location** algorithms, the user can select precisely the spatial operator to use.

**This feature was funded by:** [French Ministry of Ecology, Sustainable Development and Energy](http://www.developpement-durable.gouv.fr/)

**This feature was developed by:** [Camptocamp](http://www.camptocamp.com)

![](images/entries/cd198b98cf28e611f5c2e3be93bc5ec90dd0a5b4.webp)
### Funcionalidade: Novos algoritmos
Foi adicionado um número novo de algoritmos à infraestrutura do processamento:
- Algoritmo **Pontos regulares** (referido em #5953)
- Algoritmo **Diferença simétrica** (referido em #5953)
- Algoritmo **Divisão de vetor** (referido em #5953)
- Algoritmo **Grelha vetorial** (referido em #5953)
- Algoritmo de cálculo de **Curvas hipsométricas**
- **Dividir linhas com linhas**
- **Refactor fields** attributes manipulation algorithm

![](images/entries/b2403fae20cd24cfb1883d24e97de6fc51e40c88.webp)
## Programabilidade
### Funcionalidade: Adicionar comentários  de funcionalidade nas expressões
Comments can now be added to expressions using an SQL style `--` prefix.

![](images/entries/e1579eec6d8ab74330fb2f784c68ed16c83bb79d.webp)
### Funcionalidade: Expressões personalizadas no editor de funções
You can now define custom expression functions in the expression widget. See [this blog post](http://nathanw.net/2015/01/19/function-editor-for-qgis-expressions/) for more details.

![](images/entries/503dd9dadec4fb85ee5ab6335e4f03979a8e7d77.webp)
### Funcionalidade: Suporte para Qt5
O QGIS pode compilado usando bibliotecas Qt5. Tenha em atenção que atualmente a maioria dos binários irão ter por defeito o Qt4 .

![](images/entries/c702d89260cbab35323c052a15ab5c5728fc7115.webp)
### Funcionalidade: Volume de carregamento de índices espaciais
In the API we have added support for bulk loading of spatial index. This is much faster way of initializing a spatial index. From python it is as simple as:

`index = QgsSpatialIndex( layer.getFeatures() )`

Através de um simples teste com 50K pontos na camada de memória:

**bulk loading \~ 100 ms**

inserting features \~ 600 ms

A árvore do índex deve estar melhor em teoria e pode resultar em rápidas visualizações.

![](images/entries/80cea18c68b7885cb71c1682ca3777caa048ff9e.webp)
### Funcionalidade: Executa apenas partes selecionadas de uma consulta SQL
In the DB Manager SQL editor, it is now possible to highlight a portion of the SQL and only that portion will be executed when you press `F5` or click the `run` button

![](images/entries/0d1343e84aa0946becab1e37880a58ceeffbd491.webp)
## Servidor QGIS
### Funcionalidade:  Módulos python para Servidor
 suporte para módulos Python para o QGIS server trás o poder do python do lado do servidor, permitindo um desenvolvimento mais rápido e mais eficiente e desenvolvimento de novas funcionalidades.

**This feature was developed by:** [Alessandro Pasotti (ItOpen)](http://www.itopen.it/)
### Funcionalidade: Suporte para estilos de camada
- O QGIS Server agora suporta estilos de camada pré-definidas nos Pedidos GetMap
- O QGIS Server suporta agora múltiplos estilos no pedido GetStyles (veja em baixo a secção da simbologia)

### Funcionalidade: Adicionar o Método DescribeLayer ao WMS
**Styled Layer Descriptor profile of the Web Map Service : DescribeLayer**

<http://www.opengeospatial.org/standards/sld>

Defining a user-defined style requires information about the features being symbolized, or at least their feature/coverage type. Since user-defined styles can be applied to a named layer, there needs to be a mechanism by which a client can obtain feature/coverage-type information for a named layer. This is another example of bridging the gap between the WMS concepts of layers and styles and WFS/WCS concepts such as feature-type and coverage layer. To allow this, a WMS may optionally support the **DescribeLayer** request.

DescribeLayer method has been thought to be a better approach than overloading the WMS capabilities document even more.

For each named layer, the description should indicate if it is indeed based on feature data and if so it should indicate the WFS/WCS (by a URL prefix) and the feature/coverage types. Note that it is perfectly valid for a named layer not to be describable in this way.
## Simbologia
### Funcionalidade: Preenchimento com imagem raster
This new symbol layer type allows for filling polygons with a (tiled) raster image.

Options include (data defined) file name, opacity, image size (in pixels, mm or map units), coordinate mode (feature or view), and rotation.

![](images/entries/3c372b247f1f5583768532c2be96f169dcff1e8f.webp)
### Funcionalidade: Renderizador em tempo real de heatmap
O novo renderizador de camadas vetoriais permite ver em tempo real mapas térmicos (heatmaps) dinâmicos para camadas de pontos.

Options include specifying heatmap radius in pixels, mm or map units, choice of color ramp,weighting points by field, and a slider for selecting a tradeoff between render speed and quality.

![](images/entries/a13862e4cf8707ec70ddb37a8e3e824db6af883d.webp)
### Funcionalidade: Múltiplos estilos por camada
It is now possible to set multiple styles for a layer and then easily toggle between them. This functionality is available in the `legend context menu --> styles sub-menu` where it is possible to add/remove styles and quickly switch between them. Layer sets remember styles, and different styles can also be applied to individual composer map items. The multiple styles defined are also available when the project is served via QGIS Server as a WMS layer. For more information on this see also this [blog post](http://www.lutraconsulting.co.uk/blog/2015/02/19/towering-qgis-release/).

**This feature was funded by:** [Regione Toscana](http://www.regione.toscana.it/)

**This feature was developed by:** [Gis3W](http://www.gis3w.it/), [Lutra Consulting](http://www.lutraconsulting.co.uk/)

![](images/entries/e6d0058bbae51c52fb9fffc79d4cc459fbaf853b.webp)
### Funcionalidade: Mais configurações para simbologia definida por dados
The user interface for data defined symbology settings has been improved - moving the data defined option next to each data definable property (in keeping with other parts of QGIS such as the labeling properties). Also many new properties have been made data definable for symbology. This user interface improvement also provides a way to immediately see if a data defined override is defined as well as easier access to the data-defined settings.

![](images/entries/1af9b133ea80a4469e9be81107449b0e22df442b.webp)
### Funcionalidade: Exportação DXF: melhoria da exportação do símbolo do marcador
A funcionalidade de exportação para ficheiros DXF foi melhorada, com uma melhor fidelidade dos símbolos de marcadores exportados para a simbologia original do QGIS.
### Funcionalidade: Rotação do Mapa no enquadramento, melhoria da rotação no compositor
This release includes preliminary support for rotation in the map canvas. You can rotate the canvas using the new rotation widget in the status bar. Rotation support has been extended into the map composer too so that it correctly handles labelling and symbology, etc.

**This feature was funded by:** [Japan Space Imaging Corporation (JSI)](http://www.spaceimaging.co.jp/)

**This feature was developed by:** [Faunalia](http://www.faunalia.eu/)

![](images/entries/b655549a3336c2fb16eef87f6f30fe50f5abe9f9.webp)
## Interface de utilizador
### Funcionalidade: Melhoria/consistência na seleção de projeções
Todos os diálogos usam um widget de seleção de projeção consistente o que permite selecionar rapidamente os usados recentemente e as projeções padrão do projeto/QGIS.

![](images/entries/7a9b103d6b537f8fd6d2c53b81dc4f9a2e3f736c.webp)

.

{{<content-end >}}
