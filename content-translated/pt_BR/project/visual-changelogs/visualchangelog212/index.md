---
HasBanner: false
draft: false
releaseDate: '2015-10-23'
section: projeto
sidebar: true
title: Alterações no QGIS 2.12
type: visual-changelog

---
{{<content-start >}}
# Alterações no QGIS 2.12{#changelog212 }
![image1](images/projects/3648539707d0789903fdfedac3705584f12fa6ac.png)

Release date: 2015-10-23

This is the change log for the next release of QGIS - version 2.12.0 \'Lyon\' - host city to our developer meet up in April 2012.

**New Features in QGIS 2.12 \'Lyon\'**

This is the next release in our 4-monthly release series. It gives you access to the new features we have been working on and represents the \'cutting edge\' of QGIS development.

QGIS \'Lyon\' is jam-packed with awesome new features. Special highlights are support for rule based labelling, rule based styling of attribute tables, and advanced geometry checker, support for digitising curve based geometries, better authentication management and much, much more! QGIS 2.12 also has many bug fixes and memory leaks addressed. The features provided in QGIS 2.12 will be included in the next LTR release (slated for release in 2016), so using this release provides you with an excellent opportunity to test new features that will make their way into the next LTR.

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org). If you are working in a production environment where you wish to be more conservative about rolling out new features to your users, we also provide a Long Term Release (LTR) version of QGIS. The current LTR is version 2.8.3 and is available at [download.qgis.org](http://download.qgis.org).

**Agradecimentos**

Gostaríamos de agradecer aos desenvolvedores, testadores e documentadores, todas as pessoas lá fora que oferecem seu tempo e esforço.

From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

Finalmente, gostaríamos de agradecer aos nossos patrocinadores oficiais pelo apoio financeiro de valor inestimável que prestam a este projeto:
- **GOLD Sponsor:** [Asia Air Survey, Japan](http://www.asiaairsurvey.com/)
- SILVER Sponsor: [AGH University of Science and Technology, Krakow, Poland](http://www.agh.edu.pl/en)
- SILVER Sponsor: [State of Vorarlberg, Austria](http://www.vorarlberg.at/)
- SILVER Sponsor: [Office of Public Works, Ireland, Ireland](http://www.opw.ie/)
- SILVER Sponsor: [Sourcepole AG, Switzerland](http://www.sourcepole.com/)
- BRONZE Sponsor: [Lutra Consulting, UK](http://www.lutraconsulting.co.uk/)
- BRONZE Sponsor: [WhereGroup GmbH & Co. KG, Germany](http://wheregroup.com/)
- BRONZE Sponsor: [Nicholas Pearson Associates, UK](http://www.npaconsult.co.uk/)
- BRONZE Sponsor: [QGIS Poland, Poland](http://qgis-polska.org/)
- BRONZE Sponsor: [www.terrelogiche.com, Italy](http://www.terrelogiche.com/)
- BRONZE Sponsor: [GeoSynergy, Australia](http://www.geosynergy.com.au/)
- BRONZE Sponsor: [Gaia3D, South Korea](http://www.gaia3d.com/)
- BRONZE Sponsor: [Royal Borough of Windsor and Maidenhead, UK](http://www.rbwm.gov.uk/)
- BRONZE Sponsor: [Chartwell Consultants Ltd, Canada](http://www.chartwell-consultants.com/)
- BRONZE Sponsor: [Trage Wegen vzw, Belgium](http://www.tragewegen.be/)
- BRONZE Sponsor: [GFI - Gesellschaft fr Informations technologie mbH, Germany](http://www.gfi-gis.de/)
- BRONZE Sponsor: [GKG Kassel,(Dr.-Ing. Claas Leiner), Germany](http://www.gkg-kassel.de/)
- BRONZE Sponsor: [GIS-Support, Poland](http://www.gis-support.com/)
- BRONZE Sponsor: [ADLARES GmbH, Germany](http://www.adlares.com/)
- BRONZE Sponsor: [www.molitec.it, Italy](http://www.molitec.it/)
- BRONZE Sponsor: [www.argusoft.de, Germany](http://www.argusoft.de)
- BRONZE Sponsor: [Customer Analytics, USA](http://www.customeranalytics.com/)
- BRONZE Sponsor: [Avioportolano Italia, Italy](http://www.avioportolano.it/)
- BRONZE Sponsor: [Faculty of Geology, Geophysics and Environmental Protection, AGH, University of Science and Technology, Poland](http://www.wggios.agh.edu.pl/en)
- BRONZE Sponsor: [Urbsol, Australia](http://www.urbsol.com.au/)
- BRONZE Sponsor: [MappingGIS, Spain](http://www.mappinggis.com/)
- BRONZE Sponsor: [GIS3W, italy](http://www.gis3w.it/)

A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become and official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts.

QGIS é um software livre e você não tem obrigação de pagar nada para usa-ló - de fato queremos encorajar pessoas de todo o lado para usá-lo independentemente do seu status financeiro ou social - acreditamos que capacitar as pessoas com ferramentas de tomada de decisão espacial resultará em uma sociedade melhor para toda a humanidade.

{{<table-of-contents >}}
## Geral
### Funcionalidade: Nova tela de boas-vindas
Em vez de simplesmente mostrar uma tela em branco, o QGIS irá a partir de agora mostrar-lhe uma lista de seus projetos mais recentes, juntamente com miniaturas, que tornarão o retorno ao trabalho mais rápido e fácil, onde você parou na sua última sessão.

**This feature was developed by:** Matthias Kuhn at [OPENGIS.ch](http://www.opengis.ch)

![image11](images/entries/30f2ab32f4ae0d135a26b6a6ddb6705f0f6dd74a.webp)
### Funcionalidade: Melhorias contínuas para a qualidade do código
Através do uso do endereço de higienizador de bibliotecas, centenas de fugas de memória têm sido identificados e corrigidas. Escaneamentos de código automatizado estão sendo usados digitalização está sendo regularmente utilizada para identificar possíveis problemas, e nossa densidade de defeitos Coverity agora é muito reduzida em apenas 0,02 defeitos por 1000 linhas de código. A biblioteca de testes de unidade automatizados também tem crescido significativamente durante a versão 2,12, resultando em mais regressões identificadas e corrigidas imediatamente. Na versão 2.12, nós também adicionamos o teste contínuo em OSX, de modo que cada commit é testado contra a suíte de testes de unidade em ambas as plataformas Linux e OSX.

![image12](images/entries/774d1839283f357009c64811bd000e2f8ad97c7a.webp)
### Funcionalidade: Editor de configurações avançadas
Um novo painel foi adicionado à caixa de diálogo de configurações que permite editar qualquer uma das opções já definidas em seu perfil. Este recurso é destinado a usuários avançados no QGIS, se você alterar essas configurações sem compreender totalmente o que você está fazendo, o QGIS pode ter um comportamento inesperado.

**This feature was developed by:** Matthias Kuhn at [OpenGIS](http://www.opengis.ch/)

![image13](images/entries/6d59988bf11726192579915cff18f2b81e3f9c8f.webp)
### Funcionalidade: Árvore de grupos de camadas mutuamente exclusivos
Com esse recurso, você pode criar grupos de camadas, onde apenas uma camada no grupo pode se visível a qualquer momento. O recurso pode ser alternado individualmente para grupos menu de contexto visão.

**This feature was developed by:** Martin Dobias at [Lutra Consulting](http://www.lutraconsulting.co.uk/) on subcontract to [Gis3W](http://www.gis3w.it/)

**Esse recurso foi desenvolvido por:** Tuscany Region (Italy) - SITA (CIG: 63526840AE)

![image14](images/entries/5c68a4deab4d6058d05d3129fec89c6f9abb8530.webp)
### Funcionalidade: Filtragem de valores de campo no Widget de expressão
Ao criar uma expressão que utiliza valores de um campo, agora você pode filtrar no painel de visualização de valores de campo.

**Esse recurso foi desenvolvido por:**  Salvatore Larosa

![image15](images/entries/5d41174bdf2a059d41824590520857002a70a056.webp)
### Funcionalidade: Suporte para tema de interface de usuários
QGIS 2.12 now supports user interface theming support which you can use to customise the appearance of window backgrounds, buttons etc. By default we ship with two themes: **Default** and **Night mapping**. The latter is a dark theme which some people may prefer if they find that light themes cause eye strain. If you know a little CSS you can create your own custom themes fairly easily too\...

Find out more about theming support by reading [Nathan Woodrow\'s blog article](http://nathanw.net/2015/08/29/ui-theme-support-now-core-in-qgis/).

**This feature was developed by:** [Nathan Woodrow](http://nathanw.net/)

![image16](images/entries/2ec302b12a3b0db8e7a66465afccb227bc543a3e.webp)
### Funcionalidade: Novas funções de expressão 2.12
A set of functions for \"fuzzy matching\" have been added. These include functions for finding the similarity of two strings and also for performing phonetic matching between strings, and allow you to perform filters for records which \"nearly match\" a specified string.

Funções com base em geometria foram adicionadas, incluindo:
- `num_points(geom)` for calculating the number of nodes in a geometry
- `area(geom)`, `length(geom)` and `perimeter(geom)`, for calculating the area, length and perimeter of any geometry object. Previously only calculation of the area, length and perimeter of the current feature\'s geometry was possible.
- `start_point(geom)`, `end_point(geom)`, `point_n(geom, n)`, for retrieving the first, last and numbered points from a geometry
- `make_point(x,y)`, for manual creation of a point geometry
- `x(geom)`, `y(geom)` functions which return the x and y coordinate for point geometries or the centroid x/y for non-point geometries

A new `project_color` function has been added, which allows you to retrieve a color from the project\'s color scheme by name. This lets you create \'linked colors\', where the color of symbol or labeling components can be bound to a color in the project\'s color scheme. Update the color in the scheme, and all the linked colors will be automatically refreshed to match!

Além disso, algumas expressões muito úteis foram portadas de expressões adicionais de plugin, incluindo:
- `color_part`: allows retreival of a specific color component (eg red, hue, alpha) from a color
- `set_color_part`: allows a specific color component to be overridden, eg alter the alpha value (opacity) of a color
- `day_of_week`: returns the day of week as a number from a date

Além disso, a ajuda de contexto para funções de expressão foi melhorada para melhor legibilidade.

![image17](images/entries/b56f529af78b2d970f057c2c25ba89b87a85ce85.webp)
### Funcionalidade: Variáveis em expressões
Agora você pode definir variáveis personalizadas para uso em expressões. As variáveis podem ser definidas no nível global, nível de projeto, nível de camada e nível de composição. Assim como as regras em cascata CSS, variáveis podem ser substituídas - por exemplo, uma variável de nível de projeto irá substituir quaisquer variáveis de outro nível indicado. Você pode usar essas variáveis para construir cadeias de texto ou outras expressões personalizadas. Por exemplo, no compositor criar uma etiqueta com este conteúdo:

`This map was made using QGIS [% @qgis_version %].` `The project file for this map is: [% @project_path %]`

A etiqueta será processada como esta:

`This map was made using QGIS 2.12.` `The project file for this map is: /gis/qgis-user-conference-2015.qgs`

You can manage global variables from the `Settings -> Options` menu, and project level variables from `Project properties` (including adding your own custom variables).

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image18](images/entries/19aca1d680543a4013c53ba80406bdd5ebff88c5.webp)
## Ferramentas de análise
### Funcionalidade: Foi adicionado a quantidade de vértices de campos derivados da ferramenta de identificação
Usando a ferramenta identificação em uma feição de linha, agora irá mostrar o número de vértices presentes na feição como um atributo adicional derivado.
### Funcionalidade: Ferramenta de alinhamento de Raster
This new tool in qgis_analysis library is able to take several rasters as input and:
- reprojetar ao mesmo CRS
- reamostrar para o mesmo tamanho de célula e compensar na grade
- cortar para uma região de interesse
- quando necessário, redimensionar os valores

**This feature was developed by:** Martin Dobias at [Lutra Consulting](http://www.lutraconsulting.co.uk/) on subcontract to [Kartoza](http://kartoza.com/)

**This feature was funded by:** [DFAT](http://dfat.gov.au) for the [InaSAFE project](http://inasafe.org/)

![image2](images/entries/c613bb210ba0e85eb3b479ab79cd895827c22602.webp)
### Funcionalidade: Plugin verificador de geometria e plugin de fisgagem de geometria
Dois novos plugins (que você precisa habilitar manualmente no gerenciador de plugins) estão disponíveis para validar e corrigir geometrias. O **plugin verificador de geometrias** (foto à direita) irá verificar e corrigir o seu conjunto de dados de vetor para uma quantidade de diferentes tipos de erros sistemáticos e tentar resolvê-los. Após a resolução de um erro, a lista de erros é automaticamente atualizada de modo a que se, por exemplo, que corrige um erro também resolve outros erros, todos os erros são removidos da lista de emissão de erros.

Com o **plugin Fisgar Geometria**, você pode alinhar as bordas e vértices de uma camada vetorial para as bordas e vértices de uma segunda camada usando uma tolerância definida.

**This feature was developed by:** Sandro Mani at [Sourcepole AG](http://www.sourcepole.ch/)

**This feature was funded by:** [Canton of Solothurn](http://www.sogis.so.ch/)

![image3](images/entries/319136e65a51c7a8d76adac7aef89806db170c2e.webp)
## Opções de aplicativo e projeto
### Funcionalidade: gerenciamento de senha criptografada
QGIS 2.12 introduces a new authentication system (see [PR 2330, QEP 14](https://github.com/dakcarto/QGIS-Enhancement-Proposals/blob/auth-system/qep-14-authentication-system.rst)). Here\'s what is included:
- Configurações de autenticação criptografada por senha são armazenadas em um banco de dados SQLite
- Plugin de arquitetura do método de autenticação (como provedores de dados)
- Plugin de método de autenticação básica 
- Plugin básico integrado com PostGIS e conexões de provedores de OWS
- Configuração de usuário/senha em linha é atual (ainda totalmente funcional)
- Configurações de conexão do servidor SSL (salvo exceções ou configurações personalizadas para erros de conexão SSL)

Autenticações PKI relacionados:
- Autoridades de importação adicionais de Certificados, emitentes de certificados intermediários e feixes de identidade pessoal
- Gerencie componentes de certificados como no Firefox
- Plugins de Método de autenticação para pacotes  PEM e PKCS#12 em disco e de identidades pessoais armazenados
- Integrado com conexões de provedores de OWS (PostGIS e outros bancos de dados vão demorar um pouco mais de trabalho)

Para cenários de projetos compartilhados, incluindo uma configuração de unidade de rede, você pode editar o ID de configuração de autenticação (authcfg) para algo que é compartilhado entre os usuários.

Since the authcfg ID is embedded in the project file, each user just needs to make an auth config that has their specific credentials for that resource, then edit the ID (upon creation of config or after) to the same ID in the project file. Then, when the resource loads, the same configuration will be queried on everyone\'s QGIS, just with their respective credentials for the authentication method used.

Para o diálogo Handle Bad Layers, os usuários podem adicionar/editar/remover configurações de autenticação dentro do diálogo e ter a fonte de dados URI atualizada para corresponder. Assim, no cenário de um projeto compartilhado, o usuário pode adicionar imediatamente uma configuração de autenticação nova e apropriada e ver exatamente o que compartilhou no authcfg (O ID deve ser utilizado após o carregamento do projeto).

Currently, the master password auto-set can be set via Python, or by way of a custom C++ plugin, on launch setups using a call to `QgsAuthManager::instance()->setMasterPassword( "mypassword", true )`, or by QGIS_AUTH_PASSWORD_FILE environment variable to set the path to a file with the master password.

**Note:** for Server, you can also use QGIS_AUTH_DB_DIR_PATH to set the path to a qgis-auth.db directory and QGIS_AUTH_PASSWORD_FILE to set the path to a file with the master password on the server.

PKI example docs: <https://github.com/dakcarto/QGIS-Enhancement-Proposals/blob/auth-system/extras/auth-system/pkiuser.rst>

**Este recurso foi desenvolvido por:** Larry Shaffer

**This feature was funded by:** [Boundless Spatial, Inc.](http://boundlessgeo.com/)

![image4](images/entries/d6c9305a8dcaea3a5a6c039dec40d50e0caf23ff.webp)
## Navegador
### Funcionalidade: Melhorias para conexões de PostGIS no navegador
O navegador do QGIS agora suporta a funcionalidade adicional para conexões de PostGIS, incluindo a capacidade de **criar, renomear e apagar esquemas**, **suporte para renomeação e trucamento de camadas** e **cópia da tabela de um esquema para outro** .

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

**Table copying by:** Jürgen Fischer at [norBIT GmbH](http://www.norbit.de/)

![image5](images/entries/00820dbcf67c97b61154e7e1f41af0397009b548.webp)
## Provedores de dados
### Funcionalidade: Melhorias no provedor PostGIS
As seguintes melhorias foram feitas para o provedor PostGIS:
- melhorias de desempenho para o processador de regras baseadas em camadas de PostGIS
- suporte adicional para chaves compostas em exibições

**Compound keys developed by:** Jürgen Fischer at [norBIT GmbH](http://www.norbit.de/)

![image6](images/entries/bc56564581d97034137956cd27e945b3d3ceb3df.webp)
## O gerenciamento de dados
### Funcionalidade: Melhorias no DBManager
Houve uma série de melhorias para a ferramenta DB Manger:
- No DB Manager, agora você pode exportar seus dados para qualquer formato de dados OGR suportado em vez da opção única de Shapefile que estava disponível na versão anterior.
- Oracle Spatial agora é suportado no DBManager
- Ao importar dados em uma tabela, você pode usar os novos recursos **importar apenas feições selecionadas**, opção para restringir o que será importado.
- Novas janelas de consulta estão criadas como guias para reduzir o número de caixas de diálogo

![image7](images/entries/daa22cc4517b58f2457d78781d4dbab12663ce9d.webp)
### Funcionalidade: Formatação condicional para células da tabela de atributos
This is a major improvement to QGIS\'s attribute table rendering support. You can now style table cells according to rules. For example you can colour all cells with a population of less than 50 000 in red. The option is enabled via a new icon on the table toolbar at the top right of the attribute table window. You can read more about this feature on [Nathan Woodrow\'s blog article](http://nathanw.net/2015/08/20/mixing-a-bit-of-excel-into-qgis-conditional-formatted-table-cells/).

**This feature was developed by:** [Nathan Woodrow](http://nathanw.net/)

![image8](images/entries/ae9afefda043d31ef7718528d506d98e90e7a1f7.webp)
### Funcionalidade: Suporte para caminhos relativos nos Widgets
Para os seguintes tipos de widget de edição:
- Nome do arquivo
- Foto
- Exibição da Web

Se o caminho selecionado com o navegador de arquivos está localizado no mesmo diretório que o arquivo de projeto .qgs ou abaixo dele, os caminhos são convertidos para caminhos relativos. Isso aumenta a portabilidade de um projeto do QGIS com informação multimídia em anexo.

**This feature was developed by:** Matthias Kuhn at [OpenGIS](http://www.opengis.ch/)

**This feature was funded by:** [Alta ehf](http://www.alta.is/)

![image9](images/entries/fcf703990b5cb743ffa5cc7778cb151022ff2d20.webp)
## Digitalização
### Funcinalidade: Melhorias de digitalização
In QGIS 2.10 we mentioned that there is a new geometry architecture for QGIS but that not all features were supported in the digitising tools. With QGIS 2.12 we now have editing support for the **creation of curves / \'circular strings\`**. Note again that you need to be using a data provider (e.g. PostGIS, GML or WFS) that supports curves. These improvements to the digitising tools were also added in QGIS 2.12:
- ferramenta para adicionar cadeias circulares com dois pontos e raio
- ferramenta para adicionar cadeias circulares com ponto de partida, ponto de curva e ponto final
- permitir o escape para cancelar desenho novas feições
- exibir uma tabela ao editar com a ferramenta de nó, permitindo que você insira manualmente as coordenadas x e y exatas para nós, assim como os valores de z e m (dependendo do tipo de camada)

Além disso, as ferramentas de edição de geometria e de modificação foram atualizadas para funcionar corretamente com camadas contendo dimensões z ou m.

**This feature was developed by:** Marco Hugentobler at [Sourcepole AG](http://www.sourcepole.ch/)

**This feature was funded by:** [Canton of Solothurn](http://www.sogis.so.ch/)

![image10](images/entries/215ead2dd5e43e394d47169a7fd82aa5cc08b6b6.webp)
## Rótulo
### Feature: Data defined quadrant when in \"around point\" mode
Agora é possível especificar um quadrante de dados definidos quando um rótulo de ponto está definido para o modo de posicionamento ao redor do ponto. Isso permite que você substitua manualmente a colocação do quadrante para um rótulo específico, permitindo que os rótulos restantes estejam volta para a colocação automática.

See [this article](http://nyalldawson.net/2015/07/recent-labelling-improvements-in-qgis-master/) for more details.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image19](images/entries/27a58b65cf449505c92cc6c8470a93d1f09893a1.webp)
### Funcionalidade: Desenha somente etiquetas que se encaixam dentro de polígonos
Uma opção foi adicionada para camadas de polígonos que desenha apenas rótulos que se encaixam completamente dentro dos limites do polígono.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image20](images/entries/5c8461abe3aa5483c3243c0f145940b0d5fd1310.webp)
### Funcionalidade: Controle de obstáculos em  rotulagem de feições
In 2.12 it\'s now possible to specify the priority for labeling obstacles. This allows you to make labels prefer to overlap features from certain layers rather than others. The priority can also be data defined so that certain features are more likely to be covered than others. You can also use data defined expressions or fields to control whether a specific feature in layer will act as an obstacle for labels.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image21](images/entries/f07a082bd4e62f059788c18a9de353107b8bdc44.webp)
### Funcionalidade: Novas opções para controlar como as camadas de polígonos devem agir como obstáculos
New options have been added to control how labels should be placed to avoid overlapping the features in polygon layers. The options are to either avoid placing labels over polygon interiors or avoid placing them over polygon boundaries. Avoiding placing labels over boundaries is useful for regional boundary layers, where the features cover an entire area. In this case it\'s impossible to avoid placing labels within these features and it looks much better to avoid placing them over the boundaries between features instead. The result is better cartographic placement of labels in this situation.

See [this article](http://nyalldawson.net/2015/07/recent-labelling-improvements-in-qgis-master/) for more details.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image22](images/entries/e37943c654080e33219acb5e519970cf748c87bf.webp)
### Funcionalidade: Dados definidos para controle da prioridade do rótulo
Este recurso, frequentemente-pedido, permite aos usuários definir a prioridade para etiquetas individuais. Nas versões anteriores, o QGIS permitiu define a prioridade da etiqueta para uma camada inteira, mas não havia nenhuma opção para controlar a prioridade de recursos dentro de uma camada. Agora, você pode usar uma expressão de dados ou campo de prioridade de rotulagem de certas feições em detrimento de outras dentro de uma camada!

See [this article](http://nyalldawson.net/2015/07/recent-labelling-improvements-in-qgis-master/) for more details

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image23](images/entries/bd185cde38420f50fb540d742d178768d28ac577.webp)
### Funcionalidade: Opção para camadas únicas de obstáculos
This allows users to set a layer as just an obstacle for other layer\'s labels without rendering any labels of its own. It means that a non-labelled layer can act as an obstacle for the labels in other layers, so they will be discouraged from drawing labels over the features in the obstacle layer, and allows for improved automatic label placement by preventing overlap of labels and features from other layers.

In the screenshot you can see that the Streets have the option \"Discourage other labels from covering features in this layer\" enabled. The red labels derived from polygon geometries are thus placed to avoid intersection with the street axis. You have to enable \"Horizontal\" or \"Free\" on the polygon layer in order to achieve proper results.

Note, that it is also possible to both label a layer, but also act as obstacle layer, by enabling the checkbox \"Discourage labels from covering features\" in the \"rendering\" tab of the label settings.

See [this article](http://nyalldawson.net/2015/07/recent-labelling-improvements-in-qgis-master/) for more details.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image24](images/entries/de1eae1359ce92045d51c6fa9bc3f014a3f3ae67.webp)
### Funcionalidade: Rotulagem baseado em regras
Etiquetas em feições podem ser decoradas usando as regras para adicionar ainda mais controle sobre o posicionamento e estilização de etiquetas. Assim como a regra baseada pela prestação cartográfica, regras de etiqueta podem ser aninhadas para permitir opções de estilo extremamente flexíveis. Por exemplo, você pode tornar os rótulos de forma diferente com base no tamanho da feição que terá prioridade (como ilustrado na imagem).

See [blogpost](http://www.lutraconsulting.co.uk/blog/2015/10/25/rule-based-labeling/) for more details

**This feature was developed by:** Martin Dobias at [Lutra Consulting](http://www.lutraconsulting.co.uk/) on subcontract to [Gis3W](http://www.gis3w.it/)

**Esse recurso foi desenvolvido por:** Tuscany Region (Italy) - SITA (CIG: 63526840AE)

![image25](images/entries/8846f57f0395e7f6b2543a92a5c55b67e8b19923.webp)
## Compositor de mapas
### Funcionalidade: melhorias na navegação do Atlas
You can now set a field or expression as the \"page name\" for atlas compositions. A page number combobox has been added to the atlas toolbar, which shows both a list of available page numbers and names. This allows you to jump directly to a specific page within your atlas.

O nome da página também pode ser usado dentro de expressões de simbologia e rotulagem para permitir estilização avançada de feições do atlas com base no seu nome da página.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image26](images/entries/bbf6147ef8be9d209fa188d6c524bce9d13d5ba8.webp)
### Funcionalidade: formato personalizado para anotações de grade
A grade no compositor de mapas agora pode ser formatada em formatos personalizados, que são avaliados usando o mecanismo de expressão. Agora você utiliza qualquer formato de numeração esotérica que seus mapas exigem!

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image27](images/entries/a6cd03594ca802015ef4a5bf7806cc1ce291214b.webp)
### Funionalidade: manipulação de texto de múltiplas linhas e disposição do texto automático em tabelas de atributos no compositor
Tabelas de atributos no compositor agora incluem suporte completo para sequências multilinha. O controle sobre o alinhamento vertical do texto dentro de uma célula também foi adicionado, junto com opções para moldar texto em determinados caracteres ou calculas automaticamente a quebra de texto, possibilitando ajustar o tamanho das colunas. Para impor a quebra de texto automática com alturas de linha automáticas, defina a largura da coluna para um tamanho fixo.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

**This feature was funded by:** [City of Uster](http://gis.uster.ch/)

![image28](images/entries/db66b56f79949779ea32126bd22f2f1c9d4b55e6.webp)
### Funcionalidade: Personalização avançada de cor de fundo da célula
Esta mudança permite aos usuários definir cores diferentes para linhas e colunas, a primeira ou última linha ou coluna e linha de cabeçalho, alternando dentro das tabelas de atributos no compositor.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

**This feature was funded by:** [Ville de Morges](http://www.morges.ch/)

![image29](images/entries/68266f6b11599dfa226952455ca150448a5d082a.webp)
### Funcionalidade: Foi adicionada uma opção de ajuste de tamanho de página ao conteúdo e opções para cortar as exportações pelos conteúdos
Uma nova opção foi adicionada no painel de composição para redimensionar uma composição para o seu conteúdo, com margens extras opcionais, se necessário.

Composer exports can also be cropped to their contents. If selected, this option will make the images output by composer include only the area of the composition with content. There\'s also an option for margins to add around the item bounds if required.

If the composition includes a single page, then the output will be sized to include EVERYTHING on the composition. If it\'s a multi-page composition, then each page will be cropped to only include the area of that page with items.

Foi adicionado um diálogo de opções de exportação para nova imagem, de forma a facilitar este processo, que também inclui atalhos úteis para substituir a resolução de impressão ou dimensões da imagem exportada.

**Sponsored by:** [NIWA](https://www.niwa.co.nz/)

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image30](images/entries/38572cf4aa662cc4463c2a29f3d5ca38aa382632.webp)
### Funcionalidade: forçar camadas vetoriais a serem renderizadas como imagens raster
A new option has been added under the layer properties, rendering tab to force a vector layer to render as a raster. Extremely detailed layers (eg polygon layers with a huge number of nodes) can cause composer exports in PDF/SVG format to be huge as all nodes are included in the exported file. This can also make the resultant file very slow to work with or open in external programs. Now, you can force these layers to be rasterised on a layer-by-layer basis, so that the exported files won\'t have to include all the nodes contained in these layers. The end result is smaller file sizes and PDFs/SVGs which are faster to open.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image31](images/entries/0127fe10ecae31dbcd133492c93f33b0d569dcba.webp)
### Funcionalidade: Definição de dados para controle de camadas de mapas e predefinições de estilo
Novos dados de controle foram adicionados para as camadas de mapas e predefinições de estilo para mostrar em um compositor de mapa. Os dados das camadas do mapa são definidos através de expressão que deve resultar em uma \| (pipe) lista de nomes de camadas que serão mostrados no mapa delimitado, ou os dados predefinidos de estilo são definidos em expressão e devem resultar no nome de uma  de estilo existente.

Using this control over map layers allows for \"layer-based\" atlases, where the map layers should change between atlas pages instead of or in combination with the map extent changing. An example could be an atlas looping over different administrative units and at the same time looping over several historic maps or aerial images.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

**This feature was funded by:** [City of Uster](http://gis.uster.ch/)

![image32](images/entries/a8dc3b35df4020897e39c81bd22a469ab5ea6225.webp)
### Funcionalidade: Opção para ocultar páginas da visualização/exportação
There\'s now an option to hide the display of pages while editing and exporting compositions. This option is useful for compositions which aren\'t intended for print and are not bound by any preset page sizes. You can hide the pages, then add and resize items in any way you desire without the visual distraction of page boundaries!

**Sponsored by:** [NIWA](https://www.niwa.co.nz/)

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)
## Complementos
### Funcionalidade: Atualização do plugin GRASS
O plugin GRASS foi atualizado para habilitar o suporte para o GRASS 7. camadas GRASS podem ser pesquisados e carregadas a partir do navegador ou do painel QGIS browser. Vetores de dados Grass podem ser editados diretamente no QGIS. O projeto contém os seguintes pacotes de trabalho:
- Atualização da biblioteca do Plugin e versão multi compilação
- O navegador QGIS está integrado no painel
- Suporte para MapSets, módulos e shell para permitir a análise de dados
- Edição vetorial

Para usuários de ambos os GRASS 6 e 7, você vai achar que a integração entre o GRASS e o QGIS é muito mais transparente. Você pode criar camadas no GRASS diretamente no painel do navegador QGIS, estilizar camadas vetoriais no GRASS  usando ferramentas do QGIS e usar as ferramentas do QGIS para digitalização e criação de novas geometrias vetoriais em um mapset GRASS.

See also [QGIS GRASS Plugin Upgrade project page](http://www.gissula.eu/qgis-grass-plugin-crowdfunding/) and [progress report](http://www.gissula.eu/qgis-grass-plugin-crowdfunding/progress.html)

**This feature was developed by:** [Radim Blazek](http://www.gissula.eu/)

**This feature was funded by:** Crowd funding, see [project page](http://www.gissula.eu/qgis-grass-plugin-crowdfunding/)

![image33](images/entries/fb9ac25e9ca6c5e4030167e289435e995f5af8f5.webp)
## Programabilidade
### Feature: Map tools moved from app-\>gui
Esta mudança permite a reutilização de ferramentas de mapas de dentro de scripts PyQGIS e plugins em Python.

**This feature was developed by:** Matthias Kuhn at [OpenGIS](http://www.opengis.ch/)

**This feature was funded by:** [SIGE](http://www.sige.ch/)
### Funcionalidade: Edição de camadas via \`with edit(layer):\`
Exemplo:

    from qgis.core import edit
    
    with edit(layer):
       f=layer.getFeatures().next()
       f[0]=5
       layer.updateFeature(f)
    
Isto irá automaticamente chamar commitChanges() no final. Se ocorrer qualquer exceção, ele vai rollback() todas as mudanças.

**This feature was developed by:** Matthias Kuhn at [OpenGIS](http://www.opengis.ch/)
### Funcionalidade: Nova API para o motor de rotulagem (QgsLabelingEngineV2)
A ideia é tornar o motor mais flexível em comparação com a implementação QgsPalLabeling:
> - Relacionar abstrações com rótulos de texto / diagramas do próprio motor
> - permitir vários tipos de rótulos por camada
> - Suportar rótulos customizados por fornecedores (ex: implementado por plugins)
> - fazer o motor de rotulagem independente do mapa motor de renderização
> - torna mais fácil de auto-testar o motor de rotulagem e de seus componentes

See [blogpost](http://www.lutraconsulting.co.uk/blog/2015/10/25/rule-based-labeling/) for more details

**This feature was developed by:** Martin Dobias at [Lutra Consulting](http://www.lutraconsulting.co.uk/) on subcontract to [Gis3W](http://www.gis3w.it/)

**Esse recurso foi desenvolvido por:** Tuscany Region (Italy) - SITA (CIG: 63526840AE)
### Funcionalidade: roteiros abertos no editor externo
Pythonistas se alegre - agora você pode abrir seus scripts em um editor externo usando o novo botão adicionado ao console.

**This feature was developed by:** [Nathan Woodrow](http://nathanw.net/)

![image34](images/entries/78acf0058f4306bf408a58df3762dff5986633a7.webp)
### Funcionalidade: Novas classes para programas PyQGIS
Uma nova classe QgsStringUtils foi adicionada e permite que os scripts PyQGIS utilizem os novos algoritmos de correspondência difusa adicionados na versão 2,12. Estes incluem funções para encontrar a distância de edição Levenshtein entre duas strings e para o cálculo da representação fonética soundex de uma string. Esses algoritmos têm sido altamente otimizados para desempenho, eles estão prontos para você começar a utilizar a correspondência difusa através de milhões de sequências!

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)
## QGIS Server
### Funcionalidade: QGIS Server API Python
QGIS Server é agora embalado como uma biblioteca com uma API inicial (mas crescente) e ligações Python. Com a nova API, temos um conjunto de testes Python para o principal componente do servidor e para os plugins do servidor. Invocar o servidor a partir do Python é agora tão fácil como:

    from qgis.server import QgsServer
    headers, body =  QgsServer().handleRequest(my_query_string)
    
For more information see [this article](http://www.itopen.it/qgis-server-binding-news/)

**This work has been developed and funded by**: Alessandro Pasotti at [ItOpen](http://www.itopen.it/)
### Funcionalidade: getMap em formato DXF
Agora é possível recuperar o resultado de um pedido GetMap WMS em formato DXF. Ele suporta os mesmos recursos e opções disponíveis no QGIS desktop. Com as mesmas limitações.

| Sample URL: | `http://yourserver.org/cgi-bin/qgismapserver.fcgi?` | `map=/path/to/your/projectfile.qgs&` | `SERVICE=WMS&` | `VERSION=1.3.0&` | `REQUEST=GetMAP&` | `FORMAT=application/dxf&` | `FORMAT_OPTIONS=SCALE:500;MODE:SYMBOLLAYERSYMBOLOGY&` | `FILE_NAME=youroutputfilename.dxf&` | `CRS=EPSG:EPSG:21781&` | `BBOX=695558.73070825,244430.77224034,697158.88528251,245722.25976142&` | `WIDTH=1042&` | `HEIGHT=841&` | `LAYERS=yourdxfexportlayers`

See also [QGIS as OGC data server](http://docs.qgis.org/2.18/en/docs/user_manual/working_with_ogc/ogc_server_support.html#dxf-export) for all the available options.

Na imagem você vê o Cliente QGIS Web na esquerda com a funcionalidade de exportação DXF (utilizando o servidor QGIS) e na mesma medida visto no Autodesk TrueView do lado direito.

**This feature was developed by:** Marco Hugentobler [Sourcepole AG](http://www.sourcepole.ch/)

**This feature was funded by:** [City of Uster](http://gis.uster.ch/)

![image35](images/entries/beb2e9c00102c67ae703eac097ffba8866379609.webp)
## Simbologia
### Funcionalidade: Exportar miniaturas do gerenciador de estilo
O gerente de estilo agora permite exportar miniaturas do estilo selecionado como SVG ou imagens PNG.

**This feature was developed by:** [Nathan Woodrow](http://nathanw.net/)

![image36](images/entries/8861a040751804f6c2691ee4d93d410efd6d99ac.webp)
### Funcionalidade: Nova opção para limitar o tamanho em mm ao usar tamanhos de unidade do mapa
Anteriormente, apenas a opção de limitar o tamanhos de alcance da escala do mapa de unidade estava disponível. Agora você também optar por limitar o tamanho processado correspondente em mm.

![image37](images/entries/b822235ddb09b4184b926bf2e0acc5c892147d0b.webp)
### Funcionalidade: Melhorias no renderizador de deslocamento
- Permitem tolerância em mm/pixels para o renderizador de deslocamento
- Permitir a definição de transparência para cores
- O modo de colocação de anéis concêntricos (permite a exibição mais compactada do que apenas com anéis)

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image38](images/entries/33b5f15429279a7ec75dd1f6a2e01b1a7df789ca.webp)
### Funcionalidade: Todas as rampas de cor podem agora ser editadas
In QGIS 2.12 \"edit\" buttons have been added next to every color ramp choice. This allows you to easily edit an existing color ramp without having to create a new ramp and overwrite the existing one.

![image39](images/entries/6ca1426e6e9bfd5500b08fb2185ae50a77258892.webp)
### Funcionalidade: Melhoria do tratamento dos contornos de marcadores SVG 
O QGIS 2.12 corrige uma série de questões relativas à manipulação de contornos e preenchimentos dentro de marcadores de símbolos SVG .

As versões anteriores do QGIS tornaria os contornos em um tamanho significativamente menor do que o conjunto, e SVGs com tamanhos de contorno em unidades do mapa seriam deformados.

These issues have been fixed in QGIS 2.12, but as a result you may need to update your project symbology if you\'ve previously set oversized outlines for your symbols to overcome these bugs. In the image you see QGIS 2.12 vs QGIS 2.10 SVG markers in the symbol layer dialogs.

![image40](images/entries/a678d22393345b4fcc07b5bd023babe383151b46.webp)
### Funcionalidade: Foi adicionado pixels como opção para todas as opções de unidade de tamanho de simbologia
For all size input widgets there is now a third option \"pixel\", next to \"mm\" and \"map units\". This concerns symbol sizes, stroke widths, dash sizes, offsets, etc. This may help, if you design for screens and not for print output.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image41](images/entries/cbc683061bcc06764361ab79874f1020ccfe8eb7.webp)

{{<content-end >}}
