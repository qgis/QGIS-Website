---
HasBanner: false
draft: false
releaseDate: '2015-06-26'
section: projeto
sidebar: true
title: Alterações no QGIS 2.10
type: visual-changelog

---
{{<content-start >}}
# Alterações no QGIS 2.10{#changelog210 }
Release date: 2015-06-26

This is the change log for the next release of QGIS - version 2.10.0 \' Pisa\' - host city to our developer meet up in March 2010.

**Última versão**

This is the next release in our 4-monthly release series. It gives you early access to the new features we have been working on and represents the \'cutting edge\' of QGIS development. If you are working in a production environment where you wish to be more conservative about rolling out new features to your users, we also provide a Long Term Release (LTR) version of QGIS. The current LTR is version 2.8.2 and is available at [download.qgis.org](http://download.qgis.org). LTR releases will be supported with backported bug fixes for one year, and will be in permanent feature freeze (i.e. no new features will be added, only bug fixes and trivial updates). The features provided in QGIS 2.10 \'Pisa\' will be included in the next LTR release (slated for release in 2016), so using this release provides you with an excellent opportunity to test new features that will make their way into the next LTR.

**New Features in QGIS 2.10 \'Pisa\'**

QGIS 2.10.0 includes many great new features, tweaks and enhancements to make the most popular Free desktop GIS even more feature filled and useful. Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

**Agradecimentos**

Gostaríamos de agradecer aos desenvolvedores, testadores e documentadores, todas as pessoas lá fora que oferecem seu tempo e esforço.

From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

Finalmente, gostaríamos de agradecer aos nossos patrocinadores oficiais pelo apoio financeiro de valor inestimável que prestam a este projeto:
- **GOLD Sponsor:** [Asia Air Survey, Japan,](http://www.asiaairsurvey.com/)
- SILVER Sponsor: [Sourcepole AG, Switzerland](http://www.sourcepole.com/)
- SILVER Sponsor: [State of Vorarlberg, Austria](http://www.vorarlberg.at/)
- SILVER Sponsor: [Office of Public Works, Ireland, Ireland](http://www.opw.ie/)
- SILVER Sponsor: [AGH University of Science and Technology, Krakow, Poland](http://www.agh.edu.pl/en)
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
- BRONZE Sponsor: [GeoSynergy, Australia](http://www.geosynergy.com.au/)
- BRONZE Sponsor: [Gaia3D, South Korea](http://www.gaia3d.com/)
- BRONZE Sponsor: [Royal Borough of Windsor and Maidenhead, UK](http://www.rbwm.gov.uk/)
- BRONZE Sponsor: [Chartwell Consultants Ltd, Canada](http://www.chartwell-consultants.com/)
- BRONZE Sponsor: [Trage Wegen vzw, Belgium](http://www.tragewegen.be/)
- BRONZE Sponsor: [GIS-Support, Poland](http://www.gis-support.com/)
- BRONZE Sponsor: [GIS3W, italy](http://www.gis3w.it/)
- BRONZE Sponsor: [GFI - Gesellschaft fr Informations technologie mbH, Germany](http://www.gfi-gis.de/)
- BRONZE Sponsor: [Faculty of Geology, Geophysics and Environmental Protection, AGH, University of Science and Technology, Poland](http://www.wggios.agh.edu.pl/en)

A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become and official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts.

QGIS é um software livre e você não tem obrigação de pagar nada para usa-ló - de fato queremos encorajar pessoas de todo o lado para usá-lo independentemente do seu status financeiro ou social - acreditamos que capacitar as pessoas com ferramentas de tomada de decisão espacial resultará em uma sociedade melhor para toda a humanidade.

{{<table-of-contents >}}
## Geral
### Funcionalidade: Junção por parâmetros podem agora ser editados
Agora é possível editar junção parâmetros (como inserir prefixo ou colunas para se juntar) após uma junção criada. Antes dessa mudança era preciso apagar e recriar para juntar ao todo.

![image14](images/entries/bb09241b7b997dfa07942ee5172ad466ebb777f7.webp)
### Funcionalidade: Camadas com associações podem agora ser filtradas
Prior to version 2.10 a layer couldn\'t be filtered if it had at least one join. Now it is still filterable, but only using columns of the original master table.

![image15](images/entries/a2a93d4e621c1a2cfd976f3b0ec9673739aafda3.webp)
### Funcionalidade: Melhorias gerais
Assim como os numerosos itens listados abaixo, as seguintes melhorias foram realizadas: 
- Suporte para camadas de nuvens de pontos em PostGIS
- Barras de ícones e ícones em widgets acoplados foram melhoradas para ocupar menos espaço na tela e para melhorar a aparência OSX
- Melhorias para o plugin GRASS
- Suporte para scripts não-latinos para rótulos curvos
- Calculadora raster melhorada e mais robusta e ferramentas do georeferencidador
- Melhoria da interface do usuário e fluxo de trabalho para as janela de propriedades de rótulagem de dados

![image16](images/entries/db0cb94196fd524d93236131418f6e5f3bbf6f25.webp)
### Funcionalidade: Melhoria no tratamento das substituições de arquivos do projeto
O QGIS 2.10 não irá avisá-lo ao tentar salvar o seu projeto se dados desde a última modificação de um projeto carregado mudou. Isso é útil se mais de um usuário ou sessão tem o mesmo arquivo de projeto aberto e estão ambos a tentar salvar as edições no arquivo de projeto.

**This feature was developed by:** [Jürgen Fischer (norBIT)](http://www.norbit.de/)

![image17](images/entries/c30c07afc9123db564b766339daefe53af3cd348.webp)
### Funcionalidade: Novo motor de geometria
QGIS 2.10 has a new geometry engine. In general you won\'t see many differences on the user interface yet, but this lays the foundation for a much richer set of geospatial capabilities that we will be able to support in the future. The new implementation supports curved geometry types (so for example you can represent a traffic roundabout as a circle rather than a segmented polygon made to look like a circle) and has backend support for z/m values in geometries. To use curves in QGIS you will need to use PostGIS or a similar datastore that is able to express curvilinear geometries. If you want to have a play you can try a simple exercise like this in your PostGIS database:

    -- Table: curves DROP TABLE curves;
    CREATE TABLE curves (
       id bigserial NOT NULL,
       geometry geometry(CURVEPOLYGON, 4326),
       name text,
       CONSTRAINT p_key PRIMARY KEY (id)
       );
    
    INSERT INTO curves VALUES ( 1, st_geomfromtext(
       'CURVEPOLYGON(CIRCULARSTRING(1 1,1 2, 2 2, 2 1, 1 1))', 4326), 'test');
    
Then add the layer `curves` to your project.

**This feature was developed by:** [Marco Hugentobler (Sourcepole AG)](http://www.sourcepole.ch/)

**This feature was funded by:** [KantonSolothurn, Switzerland](http://www.sogis.ch/)

![image18](images/entries/4f070e4075b4703edb40d8cb91d5fb527d1d3a93.webp)
## Ferramentas de análise
### Funcionalidade: Novo Widget com resumo estatístico
Can display summary statistics (e.g. mean, standard deviation, \...) for a field or expression from a vector layer or selection. This is provided by means of a new dock panel that you can activate from the `View -> Panels -> Statistics` menu. Please note that you will only be able to generate statistics on **vector layers** that have a **numeric column**.

![image1](images/entries/7d52fdffac5546ea3f39ee4dac5dbe19f961703a.webp)
### Funcionalidade: Use as funções logarítmicas na calculadora raster
The raster calculator (`Raster -> Raster Calculator` in the QGIS menu) is a tool that allows you to perform matrix operations on one or more raster layers. With QGIS 2.10 you can now use `LN` and `LOG10` functions in the raster calculator.

![image2](images/entries/13c65100ab57ed8f97fa23b08704ca726a7c33da.webp)
### Funcionalidade: Novos recursos de estatísticas zonais
Estatísticas zonais fornecem uma maneira de extrair valores agregados para os pixels subjacentes de um polígono. Os seguintes novos recursos foram adicionados à nossa ferramenta de estatística zonal:
- você agora pode selecionar quais estatísticas calcular. 
- Estatísticas extras foram adicionadas (mediana, min, max, gama, minoria, maioria e variedade)
- capacidade de selecionar a banda raster a ser usado para extração de estatísticas

Note that zonal stats is a \'core plugin\' (a plugin that ships with your QGIS installer), but is disabled by default. You need to enable it in the plugin manager and then a menu entry for zonal statistics will appear in the `Raster` menu.

![image3](images/entries/d86b8eb8a72d26a0fcb0bf043c9189e14a4ae125.webp)
## Navegador
### Funcionalidade: Novo navegador de propriedades do widget
When using the QGIS Browser dock panels (`View -> Panels -> Browser`), you and now enable a properties widget at the bottom of the file system tree. Any data source that you click on will have its properties shown in this panel. This makes it quick and convenient to see basic information about the dataset you have selected. To toggle the properties view, you should use the `i` icon at the top of the browser panel.

![image4](images/entries/2f3fed9a32d761418704da2a7da378ba172164da.webp)
### Funcionalidade: Novo ícone do navegador
O navegador QGIS é um aplicativo separado, autônomo que permite navegar e visualizar os conjuntos de dados disponíveis para você (a partir do seu sistema de arquivos, conexões de banco de dados, conexões de serviço web etc.) Nas versões anteriores do QGIS foi utilizado um ícone muito semelhante ao QGIS em si, que tem sido a fonte de confusão para muitos usuários. A fim de reduzir a probabilidade de abrir a aplicação errada, nós criamos um novo ícone para navegador do QGIS.

![image5](images/entries/e76e98dffc99404f3cad540c42baebb434a696fe.webp)
## Provedores de dados
### Funcionalidade: Melhorias no exportador DXF 
A exportação DXF foi melhorada continuamente nas últimas três versões do QGIS. Esta versão introduz uma SVG melhorada ou marcador simples de conversão bloco DXF, corrige alguns bugs e problemas que resultaram em arquivos DXF ilegíveis. Na imagem você pode ver a exibição original no QGIS à esquerda e à prestação do arquivo DXF exportado no Autodesk TrueView do lado direito.

See also [this article on qgis.ch](http://www.qgis.ch/en/projects/dxf-export) explaining what is supported and what not.

**This feature was developed by:** [Jürgen Fischer (norBIT)](http://www.norbit.de/)

**Este recurso foi financiado por:** Communities of Morges, Uster, Vevey e SIGE

![image6](images/entries/b5ee8bd7a3412e429782a5e56954dabee05c36ff.webp)
### Funcionalidade: provedor de filtros PostGIS de expressões laterais
No QGIS 2.10 agora é possível filtrar recursos no lado do servidor de banco de dados. Apenas expressões suportados serão enviadas para o banco de dados. Expressões usando operadores ou funções não suportadas vai para a avaliação local.

To make use of this feature you need to enable it in `Settings -> Options -> data sources`. If your filter expression is PostgreSQL compliant it will automatically be run on the server side. You can also make use of this feature when using the python API for example when using these calls.

`QgsFeatureRequest().setFilterExpression( expression )`

ou

`QgsVectorLayer::getFeatures( expression )`

![image7](images/entries/4d4076579ecc0b5aace30fa2743f616a9b691a02.webp)
## O gerenciamento de dados
### Funcionalidade: campos virtuais não são atualizáveis
Prior to version 2.8 you had to delete and recreate virtual fields if you wanted to change the expression for calculating the virtual field. In 2.10 you can now go to the `Fields` tab and press the small `Expression` button to open the expression editor and update the expression used for the virtual field.

**This feature was developed by:** [Matthias Kuhn (OpenGIS)](http://www.opengis.ch/)

**This feature was funded by:** [City of Uster, Switzerland](http://gis.uster.ch/)

![image8](images/entries/f45d5a4447f28d96a2c5c4cc6c27b84285096a02.webp)
### Funcionalidade: editor de linha com autocomplete de valores do widget de edição
The value relation edit widget for vector layers (`Layer -> Properties -> Fields -> Edit Widget -> Value Relation`) can now be set to autocomplete as you start typing in the input box it creates on the feature form.

![image9](images/entries/4610dc0ab64a85ae020aeb22b4cbfcc8d45d0df3.webp)
### Funcionalidade: Melhorias para o gerenciador de BD
Há dois novos recursos no gerenciador de BD:

**Consulta por camada não precisa mais de uma coluna inteira exclusiva**

Uma coluna com número inteiro único não é mais necessário para carregar uma consulta SQL em uma camada no QGIS. Um valor incrementado-magnético vai ser utilizado no seu lugar.

**Integração de um construtor de consulta SQL**

Uma nova janela no gerenciador BD ajuda na criação de consultas SQL por meio de widgets, onde os nomes de tabela, nomes e funções de colunas podem ser selecionados pelo usuário. Ele foi transportado do plugin SpatiaLite e trabalha por PostGIS e prestadores SpatiaLite.

**Esses recursos foram financiados por**: MEDDE (Ministério do Desenvolvimento Sustentável francês)

**Esses recursos foram desenvolvidos por**: Hugo Mercier / Oslandia

![image10](images/entries/f5ad9f81ac37ff4dcfa754f83d23c2700ad4c9f8.webp)
### Funcionalidade: Filtro de encadeamento relativo para o widget de referência
To select linked entries from other tables one can use the relation reference widgets. One can either select elements graphically by selecting them in the map, if the linked feature has a geometry attached or choose an element by the linked id. To facilitate the non-spatial selection it is now possible to narrow the available options with filters (chained or unchained). If the filters are unchained their choices are combined with \"AND\" to define the available options. If chained is checked, a drill-down mode for the filters is activated so each filter only shows the entries which correspond to the previous filter. This is useful for selecting from hierarchical data like City -\> Street -\> Number.

**This feature was developed by:** [Matthias Kuhn (OpenGIS)](http://www.opengis.ch/)

**This feature was funded by:** [SIGE](http://www.sige.ch/)

![image11](images/entries/fd0d2e726135033e8e5a61b8a718535074a2ac0c.webp)
## Diagramas
### Funcionalidade: Melhorias nos diagramas
A funcionalidade diagrama no QGIS permite sobrepor pequenos gráficos circulares ou histogramas sobre as feições do mapa. Nesta versão fizemos as seguintes melhorias para suporte diagramação:
- Diagramas podem ser desativados sem perder as configurações.
- Adicionar caixa de seleção para sempre mostrar diagramas para uma camada
- A interface  de usuário dos diagramas foi atualizada para simplificar o diálogo e torná-lo mais amigável
- Diagram classes are now shown in the layer\'s legend

![image12](images/entries/cc5753de0538c89e3231f18c7ce62c7bc0afa5e8.webp)
## Digitalização
### Funcionalidade: Melhoria da ferramenta de rotação geometria
The geometry rotation tool is an advanced digitising tool that allows you to arbitrarily rotate a feature\'s geometry. The following improvements have been made to the rotation tool:
- agora você pode usar entrada numérica em rotação ferramenta de mapa
- você pode usar uma caixa de combinação para definir os ângulos
- added support for snapping to angles (directly enabled when `using`shift + click\`\`)
- rotation anchor is defined on `CTRL+click` and not on mouse move

![image13](images/entries/7ff32dd8c7ead358f9ffab4576dff33503154eb2.webp)
## Rótulo
### Feature: \"Follow point\" alignment for multiline labels
When set to this mode, text alignment for labels are dependent on the final placement of the label relative to the point. Eg, if the label is placed to the left of the point then the label will be right aligned, and if it is placed to the right of the point then the label will be left aligned. This greatly improves the appearance of multiline labels for point layers.

![image19](images/entries/851e7234a9509e2452dee69939d9de933a8bb90a.webp)
## Compositor de mapas
### Funcionalidade: Adicione o modo de dimensionamento da barra de escala para ajustar-se a uma largura de barra de escala desejada
In previous QGISversions it was hard to use graphical scalebars when the range of potential scales was big. The scalebar would either be quickly too wide or too narrow and one had to manually adapt the segment sizes (units per segment) after each scale change. It also meant that graphical scalebars couldn\'t be really used in Atlas serial printing or with QGISserver when the final map scale was unknown. With QGIS2.10 one can now set min/max sizes for one segment length in mm and QGISwould automatically adapt the units per segment while still keeping round values.

Don\'t forget to also set the alignment of the scalebar, esp. if you want it to be centered or right-aligned!

**This feature was developed by:** [Sandro Mani (Sourcepole AG)](http://www.sourcepole.ch/)

**This feature was funded by:** [Kanton Glarus, Switzerland](http://geo.gl.ch/)

![image20](images/entries/d435d4f94cf3d70a97c8d373aa08c28f8685defd.webp)
## Programabilidade
### Funcionalidade: Melhorias para programadores
Realizamos uma série de mudanças e melhorias que serão de interesse a desenvolvedores: 
- Aumentamos o requisito mínimo para o Qt4 para a versão 4.8. O Qt4 é um dos principais kits de ferramentas / bibliotecas C ++ que usamos para criar o QGIS.
- New `QgsStatisticalSummary` class for calculating statistics from a list of numbers.
- Permite a mudança da fonte de dados da camada vetor.
- Implicit sharing of classes : `QgsField`, `QgsFields`, `QgsDataDefined`, `QgsFeature`, `QgsGeometry`.
- Plugins can now create their own entries in the browser widget with two new classes : `QgsDataItemProvider` and `QgsDataItemProviderRegistry`.

![image21](images/entries/c702d89260cbab35323c052a15ab5c5728fc7115.webp)
## QGIS Server
### Recurso: Suporte para o parâmetro de tolerância em solicitações do WMS GetFeatureInfo
Ao usar as camadas WMS atendidas pelo QGIS Server, você pode especificar a tolerância de quanto os pedidos GetFeatureInfo de origem de clique devem ser considerados. Isso é importante para dispositivos móveis, onde é mais difícil apontar exatamente para os recursos. Antes desse novo recurso, era praticamente impossível identificar recursos de ponto ou linha em um dispositivo móvel com o servidor QGIS. Você pode adicionar os seguintes parâmetros aos seus pedidos GetFeatureInfo:

FI_POINT_TOLERANCE=16&FI_LINE_TOLERANCE=8&FI_POLYGON_TOLERANCE=4

e mudar os valores de tolerância (em pixels) para atender às suas necessidades.

**This feature was developed by:** [Marco Hugentobler (Sourcepole AG)](http://www.sourcepole.ch/)

**This feature was funded by:** [City of Uster, Switzerland](http://gis.uster.ch/)

![image22](images/entries/29470cc51906dffe3a96d3e17a7e8c83b4504a18.webp)
## Simbologia
### Funcionalidade: Combina categorias com estilos existentes 
Adicione opções no menu avançado do renderizador categorizado para definir categorias para símbolos com um nome correspondente da biblioteca de estilos ou um arquivo de estilo XML.

![image23](images/entries/c3fe0d0389c267271cbd47b8c44f52ac079961d7.webp)
### Funcionalidade: Variação do tamanho do símbolo utilizando renderização graduada
Os renderizadores são o subsistema do QGIS que permite criar representações cartográficas ricas de seus dados. Um renderizador graduado varia a simbologia com base em um valor que muda continuamente em uma camada vetorial. Nas versões anteriores do QGIS, você só podia variar a cor (por exemplo, usando uma cor ao longo de uma rampa de cores). No QGIS 2.10, o renderizador de símbolo graduado agora permite que você varie o tamanho * ou * a cor. Para camadas de pontos, você pode variar o tamanho do ponto, para linhas você pode variar a largura da linha. As camadas de polígonos retêm apenas a capacidade de variar por cor, mas a largura da linha ainda não é suportada.

**This feature was developed by:** [Vincent Mora (Oslandia)](http://www.oslandia.com/)

**This feature was funded by:** [Agence de l\'eau Adour-Garonne](http://www.eau-adour-garonne.fr/)

![image24](images/entries/1d170efe9ca0c76e971cfe0f1d0adb7c4e14f08f.webp)
### Recurso: Nova opção para impedir o recorte automático de recursos para a extensão do mapa
This option (located under the symbol advanced menu) disables the automatic clipping of lines/polygons to the canvas extent. In some cases this clipping results in unfavourable symbology (eg centroid fills where the centroid must always be the actual feature\'s centroid).

![image25](images/entries/ecd30b6893fd93d65c95df8f069cc3c3e0fff7be.webp)
### Recurso: a escala e a rotação do tamanho foram removidas do menu avançado
We have removed `SizeScale` and `Rotation` from `` `Layer -> Properties -> Symbology tab -> Advanced Menu ``. You should rather set rotation on a *per-symbol layer basis* using an expression or field. The expressions used in old projects are converted to symbol level **data defined size and angle** properties.

**This feature was developed by:** [Vincent Mora (Oslandia)](http://www.oslandia.com/)

**This feature was funded by:** [Agence de l\'eau Adour-Garonne](http://www.eau-adour-garonne.fr/)

![image26](images/entries/2e02fb11f0f967b1ea17331d9af3d5a22a63fed1.webp)
### Recurso: Propriedades definidas pelos dados para marcador de fonte
A maioria das propriedades do marcador de fonte pode agora ser definida por dados, incluindo tamanho do marcador, rotação e caractere.

![image27](images/entries/9ffd9d3284adcc85d6434f0b97f2db8974a7f647.webp)
### Funcionalidade: Visualize e modifique o renderizador graduado usando um histograma
Uma nova guia de histograma foi adicionada ao renderizador graduado, que mostra um histograma interativo dos valores do campo ou da expressão designada. Quebras de classe podem ser movidas ou adicionadas usando o histograma.

**This feature was funded by:** [ADUGA](http://www.aduga.org)

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image28](images/entries/b519e61b5b50de563203adf8ef35a7c037536332.webp)
### Funcionalidade: Expressões de tamanho, rotação e largura do traço no nível do symbollist
Tamanho e Rotação podem ser definidos por uma expressão para todos os níveis de símbolos que compõem um marcador. Largura pode ser definida por uma expressão para todos os símbolos que compõem uma linha.

Para símbolos, uma legenda é gerada para tamanhos variados. Isso permite uma legenda de análise multivariada no caso de cores classificadas / graduadas.

Um assistente, com pré-visualização, é acessível através do botão de dados definidos para ajudar o usuário a definir a expressão de tamanho. Três métodos estão disponíveis: Flannery, Area e Radius.

**This feature was developed by:** [Vincent Mora (Oslandia)](http://www.oslandia.com/)

**This feature was funded by:** [Agence de l\'eau Adour-Garonne](http://www.eau-adour-garonne.fr/)

![image29](images/entries/30f4392583400a0ed2fbdae3468265b91f39e675.webp)
### Funcionalidade: Efeitos da camada ao vivo para camadas e camadas de símbolos
Os efeitos da camada ao vivo aumentam os já extensos recursos cartográficos do QGIS, adicionando a capacidade de adicionar vários efeitos de renderização à cadeia de renderização. Com os efeitos ao vivo, você pode fazer coisas como colocar sombras sob o seu símbolo, inclinando e cortando o símbolo renderizado. Você também pode sobrepor esses efeitos um sobre o outro e definir se o efeito deve ser progressivo (ou seja, aplicar-se ao estado renderizado até o momento) ou discreto (reinjetando novamente a geometria de origem na cadeia de renderização).

** Nota **: Esta é uma funcionalidade para usuários avançados e devemos observar que o uso excessivo desse recurso pode diminuir significativamente os tempos de renderização, portanto, convém considerar ter diferentes perfis de simbologia para sua camada - um para gerar mapas de qualidade de produção e um para o modo de rascunho.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

**This feature was funded by:** [a crowd-funding initiative](https://www.kickstarter.com/projects/41633306/a-christmas-gift-for-qgis-live-layer-effects-for-q)

![image30](images/entries/2ce331bd884c14764989c1bc5e3c4d1f80ec588c.webp)

{{<content-end >}}
