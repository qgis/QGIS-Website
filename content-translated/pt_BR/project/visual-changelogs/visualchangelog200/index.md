---
HasBanner: false
draft: false
releaseDate: '2013-09-09'
section: projeto
sidebar: true
title: Alterações no QGIS 2.0
type: visual-changelog

---
{{<content-start >}}
# Alterações no QGIS 2.0{#changelog20 }
Release date: 2013-09-09

{{<table-of-contents >}}
## Ferramentas de análise
### Novidade: Comando de processamento
Para um rápido acesso às funcionalidades de geoprocessamento, apenas pressione o atalho de processamento (Ctrl + Alt + M) e inicie digitando o nome da ferramenta que você está procurando. O comando mostrará as opções disponíveis e as iniciará para vocês. Sem mais pesquisas para achar as ferramentas. Elas estão agora na ponta dos seus dedos.

![image1](images/processing_commander_2.png)
### Novidade: Aprimoramentos para o Complemento do Mapa de Calor
O complemento de Mapa de calor teve inúmeros aprimoramentos e optimizações, resultando em criações mais rápidas destes tipos de mapas. Adicionalmente, você agora tem a escolha de qual função kernel é utilizada para criar os mapas de calor.

![image2](images/Selection_027.png)
### Novidade: Suporte de processamento
The SEXTANTE project has been ported to and incorporated into QGIS as core functionality. SEXTANTE has been renamed to \'Processing\' and introduces a new menu in QGIS from where you can access a rich toolbox of spatial analysis tools. The processing toolbox has incredibly rich functionality - with a python programming API allowing you to easily add new tools, and hooks to provide access to analysis capabilities of many popular open source tools such as GRASS, OTB, SAGA etc.

![image3](images/Selection_028.png)
### Novidade: Modelador do Processamento
Uma das grandes novidades do novo Processing é a capacidade de combinar as ferramentas graficamente. Usando o **modelador gráfico**, é possível construir uma análise complexa de uma série de pequenos módulos. Você pode salvar esses modelos e, em seguida, usá-los como tijolos para construir modelos mais complexos. Tudo isso é integrado diretamente no QGIS e muito fácil de usar!

![image4](images/Processing_modeler_029.png)
## Opções de aplicativo e projeto
### Novidade: Definir projeto de inicialização padrão e modelos de projeto
With QGIS 2.0 you can specify what QGIS should do when it starts: `New Project` (legacy behaviour, starts with a blank project), `Most recent` (when you start QGIS it will load the last project you worked on), `Specific` (always load a specific project when QGIS starts). You can use the project template directory to specify where your template projects should be stored. Any project that you store in that directory will be available for use as a template when invoking the `Project --> New from template` menu.

![image5](images/Screen_Shot_2013-09-12_at_11.23.02_PM.png)
### Novidade: Variáveis ​​de ambiente do sistema
Current system environment variables can now be viewed and many configured within the application Options dialog. Useful for platforms, such as Mac, where a GUI application does not necessarily inherit the user\'s shell environment. Also useful for setting/viewing environment variables for the external tool sets controlled by the processing toolbox, e.g. SAGA, GRASS; and, for turning on debugging output for specific sections of the source code.

![image6](images/changelog-2.0_sys-env-options.png)
### Novo: escalas de zoom definido
A listing of zoom scales can now be configured for the application and optionally overridden per project. The list will show up in the `Scale` popup combo box in the main window status bar, allowing for quick access to known scales for efficiently viewing and working with the current data sources. Defined scales can be exported to an XML file that can be imported into other projects or another QGIS application.

![image7](images/changelog-2.0_predefined-scales.png)
## Navegador
### Característica: Melhorias no painel do browser in-app
- Os diretórios podem ser filtrados por expressões curinga ou regex
- New `Project home` (parent directory of current project)
- View `Properties` of the selected directory in a dialog
- Choose which directories to `Fast scan`
- Choose to `Add a directory` directly to `Favourites` via filesystem browse dialog
- New `/Volumes` on Mac (hidden directory for access to external drives)
- New `OWS` group (collation of available map server connections)
- Open a second browser (`View -> Panels -> Browser (2)`) for drag-n-drop interactions between browser panels
- Agora os ícones estão classificados por tipo de grupos de cada item (sistema de arquivos, banco de dados, serviços de mapas)
- Layer `Properties` now have better visual layout

![image8](images/changelog-2.0_browser.png)
## Provedores de dados
### Novidade: Fornecedor de dados  raster revisado
The raster data provider system has been completely overhauled. One of the best new features stemming from this work is the ability to \'Layer -\> Save As\...\' to save any raster layer as a new layer. In the process you can clip, resample, and reproject the layer to a new Coordinate Reference System. You can also save a raster layer as a rendered image so if you for example have single band raster that you have applied a colour palette to, you can save the rendered layer out to a georeferenced RGB layer.

![image9](images/Selection_017.png)
### Uma das grandes novidades do novo Processing é a capacidade de combinar as ferramentas graficamente. Usando o gráfico ** ** modelador, é possível construir uma análise complexa de uma série de pequenos módulos. Você pode salvar esses modelos e, em seguida, usá-los como tijolos para construir modelos mais complexos. Tudo isso é integrado diretamente no QGIS e muito fácil de usar!
QGIS 2.0 agora inclui suporte Oracle Spatial.

![image10](images/oracle.png)
### Novidade: Provedor Web Coverage Service adicionado
QGIS agora oferece suporte nativo para as camadas de cobertura do serviço da Web - o processo de adição de WCS é semelhante a adicionar uma camada WMS ou camada WFS.
### Novidade: Raster corte de 2% acumulada por padrão
Muitos produtos de imagens de varredura têm um grande número de valores extremos, que resultam em imagens que têm uma aparência desbotada. QGIS 2.0 apresenta controle de grão muito mais detalhado sobre o comportamento de processamento de rasters, incluindo o uso de 2% - 98% por cento corte cumulativo, por padrão, ao determinar o espaço de cor para a imagem. A imagem aqui mostra QGIS 1.8 (esquerda) versus QGIS 2.0 (à direita) ao renderizar a mesma imagem com as configurações padrão.

![image11](images/Selection_023.png)
### Novidade: Identificador para o formato WMS
Agora é possível utilizar a ferramenta identificar para camadas WMS se vários formatos conhecidos são suportados pelo servidor. Os formatos suportados são HTML, feição (GML) e textos simples. Se o formato de feição (GML) estiver selecionado, o resultado estará da mesma forma das camadas vetoriais, a geometria poderá ser destacada e a feição, incluindo atributos e geometria podem ser copiados para a área de transferência e colado e alguma outra camada.

![image12](images/wms-identify.png)
### Novidade: Suporte WMTS
O cliente WMS no QGIS suporta agora WMTS (Web Mapping Serviço Tile), incluindo a seleção de sub-conjuntos de dados, tais como fatias de tempo. Ao adicionar uma camada WMS de um servidor compatível, você será solicitado a selecionar o intervalo de tempo para exibir.

![image13](images/Selection_035.png)
## Geral
### Feature: Quantum GIS is now known only as \'QGIS\'
The \'Quantum\' in \'Quantum GIS\' never had any particular significance and the duality of referring to our project as both `Quantum GIS` and `QGIS` caused some confusion. We are streamlining our project and as part of that process we are officially dropping the use of the word `Quantum` - henceforth we will be known only as `QGIS` (spelled with all letters in upper case). We will be updating all our code and publicity material to reflect this.

![image14](images/qgis.png)
## Rótulo
### Novidade: Novo sistema de rotulagem
The labelling system has been totally overhauled - it now includes many new features such as drop shadows, \'highway shields\', many more data bound options, and various performance enhancements. We are slowly doing away with the \'old labels\' system, although you will still find that functionality available for this release, you should expect that it will disappear in a follow up release.

![image15](images/Layer_labeling_settings_003_1.png)
### Novidade: Expressão baseada propriedades de rótulo
The full power of normal label and rule expressions can now be used for label properties. Nearly every property can be defined with an expression or field value giving you more control over the label result. Expressions can refer to a field (e.g. set the font size to the value of the field \'font\') or can include more complex logic.

Exemplo:
- Fonte
- Tamanho
- Estilo
- Tamanho do buffer

![image16](images/2013-09-05_09_44_59-qgis-dev-bin.png)
### Novidade: Antigo motor de rotulagem obseleto.
Use of the older labelling engine available in QGIS \<= 1.8 is now discouraged (i.e. deprecated), but has not been removed. This is to allow users to migrate existing projects from the old to new labelling engine.

As diretrizes a seguir para trabalhar com o motor mais velho em QGIS 2.0 se por:
- Deprecated labelling tab is removed from vector layer properties dialog for new projects or older opened projects that don\'t use that labelling engine.
- As guias depreciadas permanecem ativas para projetos antigos abertos, se houver camada usa-los, e não vai embora, mesmo que salvar o projeto sem camadas com o motor de rotulagem mais velhos habilitado.

Guia de rotulagem depreciadas pode ser ativado / desativado para o projeto atual, através de comandos de console Python, por exemplo:

    >>> QgsProject.instance().writeEntry('DeprecatedLabels', '/Enabled', True | False)
    # or
    >>> QgsProject.instance().removeEntry('DeprecatedLabels', '/')
    
**NOTE**: Há uma  *probabilidade muito elevada* o motor rotulagem depreciado será completamente removido antes da próxima versão estável do QGIS. Por favor migrar projetos mais antigos.

![image17](images/changelog-2.0_labels-deprecated.png)
## Camada legenda
### Novidade: Legenda e opções visuais
- Contagem total por feições de camadas, bem como por símbolo
- Camadas vetoriais em modo de edição agora têm um lápis vermelho para indicar edições inconclusas (não salvas)
- Camadas ativas são agora sublinhadas para indicar se estão em uma seleção multi-camadas ou quando não há seleção
- Clicando em um espaço vazio limpa a seleção
- `Right-clicks` are now treated as `left-clicks` prior to showing the contextual menu, allowing for one click instead of two
- Grupos e camadas podem, opcionalmente, estar com estilo de fonte em negrito
- Ícones de visualização para camadas matriciais agora podem ser desabilitados para projetos nos quais a renderização pode ser lenta

![image18](images/changelog-2.0_visual-options.png)
### Novidade: Duplicar camada de mapa existente
Duplicar camadas selecionadas vetoriais e raster na legenda camada do mapa. Semelhante ao importar a mesma fonte de dados novamente, como uma camada separada, em seguida, copiar os atributos / estilo colar e simbologia.

![image19](images/changelog-2.0_dup-layer_1.png)
### Novidade: Multi-camada de comandos de edição de alternância
O usuário agora pode selecionar várias camadas e, se qualquer uma dessas operadoras estão em modo de edição, escolher salvar ou cancelar as alterações não salvas. O usuário também pode optar por aplicar essas medidas a partir de todos os níveis, independentemente da seleção.

![image20](images/changelog-2.0_current-edits.png)
## Compositor de mapas
### Novidade: Itens HTML nos Mapas
Agora você pode colocar elementos em HTML nos mapas.

![image21](images/Composer_1_006.png)
### Novidade: Suporte multi página
A janela de composição única agora pode conter mais de uma página.

![image22](images/2013-09-08_22_31_33-Composer_1.png)
### Novidade: Expressões no compositor de rótulos
The composer label item in 1.8 was quite limited and only allowed a single token \$CURRENT_DATE to be used. In 2.0 full expression support has been added too greater power and control of the final labels.

Uma etiqueta com uma expressão como:

    This was printed on: [% format_date( $now, 'dd.MM.yyyy')%]
    
será avaliada no momento da impressão (e tempo de exibição) para gerar:

    This was printed on: 06.09.2013
    
When atlas generation is enabled the currently active features\' attribute values will also be accessible in the expressions allowing such things as:

    Asset ID [% "ID" %] and the Tree Type is [% "TreeType" %]
    
![image23](images/2013-09-06_09_53_30-Composer_1.png)
### Novidade: Linhas de auto-ajuste
Ter um bom alinhamento dos itens do mapa é fundamental para obter bons mapas. As linhas de auto-ajuste têm sido adicionadas para permitir mais facilidade ao alinhamento de objetos apenas arrastando-os para próximos de outros.

![image24](images/2013-09-05_10_05_01-Composer_1.png)
### Novidade: Linhas de ajuste manual
Em determinados momentos é necessário alinhar objetos que estão a curta distância um do outro no compositor. Com a nova linha de ajuste manual, você é capaz de adicionar linhas que permitirão um melhor alinhamento entre os objetos. Apenas arraste na régua, na porção superior ou lateral, para criar uma nova linha guia.

![image25](images/2013-09-05_10_09_41-Composer_1.png)
### Novidade: Geração de séries de mapas
Nunca precisou gerar uma série de mapas? Claro que sim. O compositor agora inclui a geração de séries de mapas usando a ferramenta Atlas. As camadas cobertas podem ser de pontos, linhas, polígonos e o atual atributo da feição está disponível nos rótulos para substituição do valor real.

![image26](images/Picture1.png)
### Novidade: Suporte automático de visão geral no mapa
Agora você pode mostrar a área atual do mapa principal numa pequena janela de visão geral. O quadro do mapa agora contém a funcionalidade para visualizar as extensões de outro e ele será atualizado quando movido. Utilizando isto com a ferramenta de geração de atlas nativo no compositor permite mais agilidade na criação de mapas. O estilo da visão geral é a mesma utilizada nos objetos do tipo polígono, por isso sua criatividade nunca será restringida.

![image27](images/Picture1_1.png)
### Novidade: camada de mistura
Layer blending makes it possible to combine layers in new and exciting ways. While in older versions, all you could do was to make the layer transparent, you can now choose between much more advanced options such as \"multiply\", \"darken only\", and many more.

Blending can be used in the normal map view as well as in print composer. For a short tutorial on how to use blending in print composer to make the most out of background images, see [\"Vintage map design using QGIS\"](http://anitagraser.com/2013/07/29/vintage-map-design-using-qgis/).

![image28](images/printcomposer_blending_1.png)
### Novidade: Suporte para rótulo HTML
Suporte para HTLM tem sido acrescentado como item de rótulo do compositor de mapa para dar-lhes ainda mais controle sobre os mapas finais. Rótulos em HTML suportam planilhas completas em estilo css, html, e até mesmo javascript, se assim for o caso.

![image29](images/html.png)
### Novidade: Criação de legendas em multicolunas
A criação de legendas agora suportam colunas múltiplas. Dividindo um única camada com muitas classes em múltiplas colunas é opcional. Camadas com símbolos únicos são adicionadas por padrão item de linha simples. Três diferentes estilos podem ser atribuídos ao título da camada/grupo: Grupo, Subgrupo ou Oculto. Os estilos dos títulos permitem um agrupamento visual dos itens. Por exemplo, um camada de símbolo único pode ser exibida como um item de linha simples ou com o título da camada (como no 1.8), símbolos de múltipilas camadas em sequência podem ser agrupadas em um único grupo (ocultando os títulos), etc. A contagem de feições pode ser adicionadas aos rótulos.

![image30](images/multicolumn-legend.png)
### Novidade: Atualizações para a gerenciamento do compositor de mapas
Os seguintes aperfeiçoamentos foram introduzidos para o gerenciamento do compositor:
- O nome do compositor pode agora ser definido após a criação, opcionalmente escolhendo iniciar um a partir de outros já criados
- Compositores podem agora ser duplicados
- `New from Template` and from `Specific` (in Composer Manager) creates a composer from a template located anywhere on the filesystem
- Projetos podem agora ser salvos diretamente do espaço de trabalho do compositor
- Todas as ações do Gerenciador do compositor agora estão acessíveis diretamente do espaço de trabalho do compositor

![image31](images/changelog-2.0_composer-mngmnt.png)
## Complementos
### Novidade: Gerenciador de plugins renovado
No QGIS gestão plugins 1.x foi um pouco "confuso com duas interfaces - uma para lidar com o plugin instalado e um plugin python para a recuperação de um único repositório. No QGIS 2.0 introduzimos um novo unificado, gerente, plugin que fornece um local para o download, ativação / desativação e, geralmente, para a gestão de plugins.

![image32](images/Plugin_Manager_024.png)
## Programabilidade
### Novidade: Novo console Python
O novo console da Python lhe dá ainda mais poder. Agora apoiar autocompletar, destaque de sintaxe, configurações de fonte ajustável. O código do lado do editor permite a escrita de grandes blocos de código mais fácil com a capacidade de abrir e executar qualquer arquivo Python em sessão QGIS.

![image33](images/pyconsole.png)
### Novidade: novas funções para expressões
Com o motor de expressão cada vez mais utilizado, para permitir operações como etiquetas com base na expressão e símbolo, muitas outras funcionalidades foram adicionadas à expressão construtor e são acessíveis com o Expression Builder. Todas as funções são acompanhadas de suporte e manuais de usuário.

![image34](images/2013-09-06_09_10_49-Expression_based_label.png)
### Novidade: Funções de expressão personalizada
If the expression engine doesn\'t have the function that you need. Not to worry. New functions can be added via a plugin using a simple Python API.

![image35](images/2013-09-06_09_14_58-untitled__routing_-_Sublime_Text_UNREGISTERED.png)
### Novidade: Nova API Pyton
A API do Python foi renovado para permitir uma programação mais organizada e limpa. A API QGIS 2.0 utiliza SIP V2 que elimina a toString confuso (), Toint () que eram necessários quando se trabalha com valores. Os tipos agora são convertidos para tipos Python nativas. Os atributos podem agora ser acessados ​​usando uma chave de busca simples, não mais do que o índice de pesquisa e mapas de atributos.

    >>> feature['mycolumn'] = 10
    >>> feature['mycolumn']
    10
    
Melhoria da leitura da geometria de uma camada, a fim de permitir multithreading no futuro.

    for feature in layer.getFeatures():
           print feature['mycolumn']
    
![image36](images/2013-09-06_09_28_08-untitled__routing_-_Sublime_Text_UNREGISTERED.png)
### Novidade: Código de compatibilidade com os lançamentos de versões 1.x
As this is a major release, it is not completely API compatible with previous 1.x releases. In most cases porting your code should be fairly straightforward - you can use [this guide](https://github.com/qgis/QGIS/wiki/Python_plugin_API_changes_from_18_to_20) to get started. Please use the developer mailing list if you need further help.

![image37](images/Selection_021.png)
### Novidade: macros Python neste projeto
Um módulo Python, salvo em um arquivo project.qgs, podem ser carregados e têm funções específicas executadas nos seguintes eventos do projeto:
- `openProject()`
- `saveProject()`
- `closeProject()`

Se as macros são executadas pode ser configurado nas opções de aplicação.

![image38](images/changelog-2.0_project-macros_w-setttings.png)
## Simbologia
### Novidade: Propriedades definidas para dados 
Com as novas propriedades de dados definidos, é possível controlar o tipo, tamanho, cor, rotação e muitas outras propriedades dos símbolos através dos atributos das feições.

![image39](images/datadefinedproperties2.png)
### Novidade: Aperfeiçoamento da gestão da simbologia
A nova visão geral da simbologia das camadas utiliza um modelo limpo e estruturado em árvoce que permite acesso rápido e fácil a todos as opções de simbologia.

![image40](images/symbollayertree.png)
### Novidade: O suporte para a transparência na definição de cores
In most places where you select colours, QGIS now allows you to specify the alpha channel (which determins how transparent the colour should be). This allows you to create great looking maps and to hide data easily that you don\'t want users to see.

![image41](images/Layer_Properties_-_nat_026_1.png)
### Novidade: Controle de cores para camadas raster
QGIS 2.0 allows you to precisely control exactly how you\'d like raster layers to appear. You now have complete control over the brightness, contrast and saturation of raster layers. There\'s even options to allow display of rasters in grayscale or by colorising with a specified color.

![image42](images/Layer_Properties_-_blue_marble_032.png)
### Novidade: Cópia de simbologia entre camadas
Its now super easy to copy symbology from one layer to another layer. If you are working with several similar layer, you can simply `right-click` on one layer, choose `Copy Style` from the context menu and then `right-click` on another layer and choose `Paste-Style`.

![image43](images/Selection_034.png)
### Novidade: Salvar estilos no seu banco de dados
Se você está armazenando os dados em um banco de dados vetoriais, você pode fornecer as definições de estilo diretamente no banco de dados. Isto facilita o compartilhamento dos estilos das camadas numa organização ou num ambiente multi-usuário.

![image44](images/Selection_037.png)
### Novidade: Suporte a Rampa de cores
Colour ramps are now available in many places in QGIS symbology settings and QGIS ships with a rich, extensible set of colour ramps. You can also design your own and many [cpt-city](http://soliton.vm.bytemark.co.uk/pub/cpt-city/) themes are included in QGIS now \'out of the box\'. Color ramps even have full support for transparency!

![image45](images/Selection_038.png)
### Novidade: Definir estilos padrão personalizados para todos os tipos de camada
Now QGIS lets you control how new layers will be drawn when they do not have an existing `.qml` style defined. You can also set the default transparency level for new layers and whether symbols should have random colours assigned to them.

![image46](images/Screen_Shot_2013-09-12_at_11.18.52_PM.png)
## Interfaçe de usuário
### Novidade: Novo tema de ícones 
We have updated out icon theme to use the \'GIS\' theme which introduces an improved level of consistency and professionalism to the QGIS user interface.

![image47](images/Selection_001_1.png)
### Novidade: Abas laterais, grupos retraíveis
Nós padronizamos o layout das abas e introduzimos caixas de grupos retraíveis em vários de nossos diálogos para facilitar a navegação e aprimorar o uso.

![image48](images/Selection_005.png)
### Novidade: ligeiras modificações
In many cases we want to tell you something, but we don\'t want to stop your work or get in your way. With the new notification system QGIS can let you know about important information via a yellow message bar that appears at the top of the map canvas but doesn\'t force you to deal with it if you are busy doing something else. Programmers can create these notification (e.g. from a plugin) too using our python API.

![image49](images/Selection_030.png)
### Novidade: fonte padrão para o aplicativo e QT estilo
The system font used for the application\'s user interface can now be set. Any C++ or Python plugin that is a child of the QGIS GUI application or has copied/applied the application\'s GUI stylesheet can inherit its styling, which is useful for GUI fixes across platforms and when using custom QGIS Qt widgets, like `QgsCollapsibleGroupBox`.

O QGIS folha de estilo personalizado está disponível após a conclusão (dentro PyQGIS) ::

    qgis.utils.iface.mainWindow().styleSheet()
    
![image50](images/changelog-2.0_app-font.png)
### Novidade: diálogos do seletor de cores
Every color chooser button throughout the interface has been updated to give visual feedback on whether the current color has a transparent, or \'alpha,\' component. The color chooser opened by the new color buttons will now always be the default for the operating system. If the user has `Use live-updating color chooser dialogs` checked under `Options -> General -> Application`, any change in the color chooser will immediately be shown in the color button and for any item currently being edited, where applicable.

![image51](images/changelog-2.0_live-color-dlgs.png)
### Novidade: Anotações SVG
Com QGIS 2.0 agora é possível adicionar anotações ao SVG mapa - está preso a um lugar específico ou em uma posição relativa no mapa.

![image52](images/Screen_Shot_2013-09-14_at_9.39.11_AM.png)
### Novidade: Arraste e forma de gota construtor
QGIS 2.0 suporta um novo sistema para a criação de formas de entrada de dados. Com o designer do formulário para arrastar e soltar você pode criar formulários inteligentes com guias para agrupar campos comuns juntos. Agora é muito mais fácil de controlar a experiência de entrada de dados para os usuários.

![image53](images/Screen_Shot_2013-09-14_at_2.17.27_PM.png)
### Novidade: Ferramenta de ação padrão
Se você é um usuário de ações camada vetorial (pequenas tarefas que podem ser executados quando você clica em um recurso), você vai adorar a nova ferramenta de ação na barra de ferramentas. Com ele você pode selecionar uma ação ativa e, em seguida, clique em seus recursos para chamar essa ação.

![image54](images/Screen_Shot_2013-09-14_at_2.27.03_PM.png)

{{<content-end >}}
