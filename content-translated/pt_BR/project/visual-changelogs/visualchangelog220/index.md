---
HasBanner: false
draft: false
releaseDate: '2014-02-22'
section: projeto
sidebar: true
title: Alterações no QGIS 2.2
type: visual-changelog

---
{{<content-start >}}
# Alterações no QGIS 2.2{#changelog22 }
Release date: 2014-02-22

Registro de alterações para a próxima versão do QGIS 2.2.0. A ênfase deste lançamento foi dada essencialmente no aperfeiçoamento e no desempenho – adicionamos várias novas funções, pormenores e melhorias de modo a tornar a interface mais congruente e visualmente mais profissional (esperamos que de mais fácil uso também). O Editor (usado na criação de mapas prontos a imprimir) foi um dos pontos mais focados para torná-lo numa plataforma mais viável na criação de cartografia de qualidade superior. 

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

Gostaríamos de agradecer aos desenvolvedores, testadores e documentadores, todas as pessoas lá fora que oferecem seu tempo e esforço.

From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

Finalmente, gostaríamos de agradecer aos nossos patrocinadores oficiais pelo apoio financeiro de valor inestimável que prestam a este projeto:
- GOLD Sponsor: [Asia Air Survey, Japan](http://www.asiaairsurvey.com/)
- SILVER Sponsor: [G.A.I.A. mbH, Germany](http://www.gaia-mbh.de/)
- SILVER Sponsor: [State of Vorarlberg, Austria](http://www.vorarlberg.at/)
- BRONZE Sponsor: [www.molitec.it, Italy](http://www.molitec.it/)
- BRONZE Sponsor: [www.argusoft.de, Germany](http://www.argusoft.de)

A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors).

If you would like to make a donation or sponsor our project, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. QGIS is Free software and you are under no obligation to do so. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts.

{{<table-of-contents >}}
## Opções de aplicativo e projeto
### Novidade: Suporte para medidas em milhas naúticas
For you seafaring folks out there, you can now measure distances using nautical miles. To enable this, use the `Settings -> Options -> Map Tools` option panel.

![image1](images/entries/e1115ca7d43ec24fceaee93f976848583148724f.webp)
## Provedores de dados
### Novidade: Criando uma ou mais relações
This release sports the ability to define 1:n relations. The relations are defined in the project properties dialog. Once relations exist for a layer, a new user interface element in the form view (e.g. when identifying a feature and opening its form) will list the related entities. This provides a powerful way to express e.g. the inspection history on a length of pipeline or road segment. You can find out more about relations support [here](http://blog.vitu.ch/10112013-1201/qgis-relations).

![image2](images/entries/0e5e0d1b9dfafe9d64dd5b79866877980f03d099.webp)
### Novidade: Ferramenta para exportar DXF:
A new tool for exporting DXF\'s has been added to the `Project` menu

![image3](images/entries/452e7692b5b8d2704b4d31067265eb71986d969f.webp)
### Novidade: Colar como uma nova camada vetorial
It is a common activity in a GIS to create a sub-selection and then to create a new layer from the selection. In QGIS you can already do `save selection as` to save a layer from your selection, and now offers functionality that allows you to create a new file or memory layer from whatever is in your clipboard. Simply select some features, copy them to your clipboard and then do `Edit -> Paste features as` and choose either `New vector layer` or `New memory layer` from the submenu. The best part of this new feature is that if you have some Well Known Text (WKT) features in your clipboard from another app, you can simply paste them into QGIS as a new layer now.

![image4](images/entries/636db14446809f9e284013113a7b881868591ed3.webp)
### Novidade: Legenda de WMS na lista de camadas e no compositor
Prior to QGIS 2.2 the WMS data provider was not able to display a legend in the table of contents\' layer list. Similarly no legend could be displayed in the map composer. QGIS 2.2 addresses both of these issues.

Clicking on the layer\'s legend will open a frame with the legend at full resolution. The legend will display contextual information based on your current scale. The WMS legend will be shown only if the WMS server has GetLegendGraphic capability. Legend resolution can be modified changing Canvas & Legend options.

![image5](images/entries/6e7cd4849824a802558c0e029f605145d5c885aa.webp)
## Digitalização
### Novidade: Ferramenta de preenchimento de anel
This new tool is used to cut holes in polygons and automatically fill them with new features. If you hold down `Ctrl` when finalising the feature, the attributes will be taken from parent feature.

![image6](images/entries/a8c671765578b660cb5d33cca51efa66ecdb17a4.webp)
## Geral
### Novidade: Memorização de expressões recentes
O criador de expressões permitirá salvar as últimas 20 expressões utilizadas.

![image7](images/entries/90a6b4d181fb2dc7699402d17c1f31522c4f3409.webp)
### Novidade: Colar WKT da área de transferência
QGIS can now paste and create a new feature based on WKT that is found in the clipboard. Simply copy some WKT and paste into a editable layer. You can also create a new layer by selecting `Edit -> Paste As -> New Memory Layer`
## Compositor de mapas
### Novidade: Melhorias na borda do mapa estilo zebra
You can now set the colours of the `Zebra` border on the map element in the map composer.

![image8](images/entries/682c36e3ac96b491e2e0a99a7ff9d94b9e0dc4e5.webp)
### Novidade: Suporte para rotação de elementos
Todo tipo de elementos no compositor pode ser rotacionado, incluindo barras de escala, tabelas e legendas. Por exemplo, você pode rotacionar um rótulo na composição para ajustá-lo melhor ao modelo do mapa (como ilustrado). O redimensionamento de elementos rotacionados também foi melhorado.

![image9](images/entries/700e0999552bc2e2bb2cef86ed14240b05f1da4e.webp)
### Novidade: Melhorias na escala e régua no compositor
The appearance of rulers has been improved by adjusting the scale logic and by adding smaller ruler divisions, and by making vertical rulers use rotated text. There is also a new composer action for hiding/showing rulers. You can now quickly zoom to 100% page scale using the new `Zoom to 100%` tool on the toolbar. The composer window now lets you quickly switch the page scaling via a new scale combobox in the status bar. In addition a new indicator has been added to show you the precise pixel position of your cursor. The `Close` and `Help` buttons have been removed from the bottom of the composer window to give you the maximum amount of screen space for working with your compositions.

![image10](images/entries/8b148acf4ef24204b42f14ee7cec43d57c87911a.webp)
### Novidade: Geração de arquivos World
In the composer you can now create georefenced maps! Simply ensure that you choose the correct map element in the `Composition tab` and then export your map as a PNG file. An accompanying world file will be written, allowing you to load your exported composition in QGIS as a raster layer.

![image11](images/entries/d5887511afbe8379f9e240c3763f6b68766cac88.webp)
### Novidade: Trabalhando com múltiplos itens
Support has been added for moving and resizing multiple items simultaneously. You can now hold shift while resizing to maintain an item\'s ratio while resizing, or hold control to resize from the item\'s centre. Shortcut key also apply to moving items, so holding shift while moving an item constrains the movement to horizontal or vertical movement, and holding control temporarily disables item snapping. You can also hold shift while pressing a cursor key to shift all selected items by a larger amount.
### Novidade: Melhorias no Atlas
You can now preview the individual pages of the map atlas that will be generated in composer. While in atlas preview mode you can output the current page without outputting the entire atlas. You can also tweak the map extent or scale for each feature while previewing the atlas page. Atlas map settings have been moved from the atlas panel to the map properties panel, so now more than one map can be controlled by the atlas generation. There\'s a new option to automatically centre an overview map, which comes in handy when creating atlas based maps. More context information is now available so that you can adjust your symbology based on whether the feature is the current atlas feature or not. See [this article for more info](http://nathanw.net/2013/12/02/waiting-for-qgis-22-highlighting-current-atlas-feature/).

![image12](images/entries/fe668e5f257efec81db855a91fc7d6febc221261.webp)
### Novidade: Aperfeiçoado a seleção de item
You can now select more then one item by clicking and dragging a box to select them, and there\'s shortcuts for adding to a selection (holding shift while dragging), subtracting from a selection (hold control while dragging) and switching to \"within\" selection mode (hold alt while dragging). Shift clicking an already selected item will remove it from the selection. There\'s also shortcuts and menu items for selecting all items, clearing a selection, and inverting a selection. It\'s also possible now to select items which are hidden below other items by control-clicking an item, or by using \"Select next item above/below\" in the new composer Edit menu.
### Novidade: Melhor navegação de composições
QGIS 2.2 includes many improvements to help you navigate your compositions. You can now zoom in or out from a composition by using the mouse scroll wheel. A dedicated pan tool has been added which allows you to drag the composition around, and you can also switch immediately to pan mode by holding the space bar or the by holding the mouse scroll wheel. There\'s also a new zoom tool which allows you to precisely zoom to a specific area of your composition. You can also switch to zoom mode at any time by pressing and holding control-space and drawing a zoom region on the composition.
### Novidade: Melhoramento no estilo de páginas e formas
You can now control the style of the composition background using the full range of QGIS\' symbology options. It\'s now possible to export compositions with a transparent (or semi-transparent) background. Shape items (rectangles, triangles and ellipses) can also be styled using the same options as polygon map layers. You can even style the page background or shapes by using data defined settings based on the current atlas feature! There\'s also a new option for rounding the corners of rectangle shapes.
## QGIS Server
### Novidade: Adicionado suporte WCS ao QGIS Server
O QGIS Server suporta vários padrões, incluindo Web Map Service (WMS versão 1.3.0 e 1.1.1), Web Feature Service (WFS versão 1.0.0) and Web Feature Service Transacional (WFS-T). Nesta nova versão, você poderá fornecer serviços de camadas matriciais utilizando o padrão Web Coverage Service (WCS versão 1.0.0)) padrão.

![image13](images/entries/b93abbe00e7a32ffb06144ac839619ab50521e5c.webp)
## Simbologia
### Novidade: Suporte para preenchimento em gradiente
A nova funcionalidade de preenchimento em gradiente permite criar melhores mapas do que antes. Esta funcionalidade tem numerosas opções provendo com grande flexibilidade a forma de aplicar os gradientes às suas feições. Estas incluem:
- Preenchimento em duas cores ou em rampa de cores
- Tela- ou origem baseado em objetos e seus gradientes
- Gradientes originados a partir do centróide de uma feição
- Tipos de gradientes cônico, linear e radial
- Opções de dados definidos (ex. usar uma expressão ou uma coluna da tabela) para todas as propriedades de gradientes.

Read more about how to use gradient fills [here](http://nyalldawson.net/2014/01/waiting-for-qgis-2-2-gradient-fills/).

![image14](images/entries/7c4cb6c7ce981ca88b27cd2ae55bc4e503a1234f.webp)
### Novidade: Suporte de rótulo para paleta em raster
Rasters que utilizam uma paleta de cores fixas (para instâncias, um mapa de cobertura) podem ter categorias de rótulos nomeadas com o que será mostrado na legenda do mapa e na legenda do compositor.

![image15](images/entries/232d60f2aa3accb19eb4da3a08b75ad4c15d068a.webp)
### Novidade: Rampa de cores pode ser invertida
Uma nova opção que foi acrescentada às opções de simbologias relacionada às rampas de cores é que permite inverter a rampa após criada

![image16](images/entries/3b1e65705f751bb468cc6495267633d613edbe34.webp)
### Novidade: Copiar e colar um estilo baseado em regra
No renderizador baseado em regra, você pode em um clique com o botão direito do mouse numa regra, copiá-la e colá-la como uma nova regra.

![image17](images/entries/8e69ef57ed6ae838e813d798312d7d1e39913749.webp)
### Novidade:Recurso de generalização on-the-fly
O QGIS 2.2 introduz o recurso de generalização para o on-the-fly. Isto pode melhorar o tempo de renderização enquanto se desenha inúmeras feições complexas em escala pequena. Este recurso pode ser habilitado ou desabilitado nas propriedades da camada. Existe também uma nova opção geral que habilita a generalização por padrão para novas camadas adicionadas. **Nota:** O recurso de generalização pode apresentar artefatos no resultado da renderização em alguns casos. Isto pode incluir linhas entre polígonos e uma renderização inexata quando utilizado simbologia com offset.

![image18](images/entries/baa801841f58883d93d0ea6ecb5363da963e4ee2.webp)
### Novidade: Pontos âncoras podem ser ajustados para marcadores
When defining symbology with marker layers (e.g. a point layer symbolized with SVG markers) you can now specify what part of the image should correspond to the \'anchor point\'. For example you can indicate that the bottom-left corner of the image should coincide with the position of the feature. You can also use the `data defined properties` to have this property set at render time based on an attribute in the data table for that layer (or an arbitrary expression).

![image19](images/entries/ecac63dad2e0da0702b2fe5bc361d68f0c0c6a0f.webp)
### Novidade: Mapas temáticos baseados em expressões
Mapas temáticos categorizados ou graduados podem ser criados utilizando como resultado uma expressão. No diálogo de propriedades de uma camada vetorial, o atributo adotado tem sido aumentado com um criador de expressões. Agora, não é necessário escrever a classificação do atributo em uma nova coluna na tabela de atributos se você quer que a classificação do atributo seja composta de múltiplos campos ou um qualquer tipo de fórmula.

![image20](images/entries/cc5cad88da77d1868e394a115606f4b1e6ee8c29.webp)
### Novidade: Suporte para expressões nos diagramas de símbolos para tamanho e atributos:
You can now use an expression to define the size and attributes when using the diagramming capabilities of QGIS. For more info see the Pull Request here [Pull 1039](https://github.com/qgis/QGIS/pull/1039)

![image21](images/entries/547b5058efeca906c00ee65ee2504f2669ff52f9.webp)
### Novidade: Regra Else em estilos baseados em regra
O estilo baseado em regra suporta a regra ELSE que rodará se nenhuma outra regra corresponder neste nível. Regras Else podem ser aninhadas, assim como quaisquer outras regras.

Um exemplo pode ser:

| `type = 'water' (style grey)` | `ELSE (style red)`

![image22](images/entries/4c38bdd63e64274d22e6a57a6541920ed47bc4be.webp)
### Função: Apoio de traçado interno para polígonos:
Foi adicionado suporte para o traçado de polígonos a serem limitados no interior do polígono (para não transbordar para um polígono vizinho).

More information on this feature can be found on the [second part of this article](http://nyalldawson.net/2014/01/qgis-two-neat-features-in-2-2/).

![image23](images/entries/81597f0bc2b848fe39e078a2684c57d44fbda79d.webp)
## Interfaçe de usuário
### Novidade: Melhorias no diálogo de propriedades
Todas as propriedades diálogos tiveram seus menus atualizados para que eles se pareçam mais lisos, com uma barra lateral de cor inversa. Isto é puramente comético, mas deve facilitar as atividades neste diálogo.

![image24](images/entries/9d817847f89a3ea7836f86ddff3317040543a78f.webp)
### Novidade:Melhorias no diálogo de expressões
We have made some tweaks to the expression dialog - power users can now hide the operator buttons. There are also now splitters between the function list and function help areas, and between the expression and function list area. See the [original pull request](https://github.com/qgis/QGIS/pull/1073) for details.

![image25](images/entries/150ae30a6d905e008131c28e4befe862f1bf8ed6.webp)
### Novidade: Novas combinações de teclas:
Nós atualizamos os atalhos no QGIS para fazê-lo mais eficiente em tarefas repetitivas.
- `ctrl-d` - Remove selected layers in table of contents
- `>` - Select next vertex when using the node tool
- `<` - Select previous vertex when using the node tool
- `Delete` or `Backspace` - delete the selected features (you can undo these actions), or a node when using the nodetool.
- `F5` updates the canvas (instead of ctrl-r)

See also [Issue 9094](http://hub.qgis.org/issues/9094) and [Pull Request 1010](https://github.com/qgis/QGIS/pull/1010) for more details.

![image26](images/entries/e8766bfccf2da60b09acde28f5d766eb3d76cec9.webp)

{{<content-end >}}
