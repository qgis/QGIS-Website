---
HasBanner: false
draft: false
releaseDate: '2014-10-31'
section: projeto
sidebar: true
title: Alterações no QGIS 2.6
type: visual-changelog

---
{{<content-start >}}
# Alterações no QGIS 2.6{#changelog26 }
Release date: 2014-10-31

O registro de alterações para o próximo lançamento do QGIS 2.6.0. Nós adicionamos novas funcionalidades e melhorias para tornar este SIG Desktop Gratuito mais cheio de funcionalidades e mais útil.

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

Gostaríamos de agradecer aos desenvolvedores, testadores e documentadores, todas as pessoas lá fora que oferecem seu tempo e esforço.

From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

Finalmente, gostaríamos de agradecer aos nossos patrocinadores oficiais pelo apoio financeiro de valor inestimável que prestam a este projeto:
- **GOLD Sponsor: Asia Air Survey, Japan** <http://www.asiaairsurvey.com/>
- SILVER Sponsor: [Sourcepole AG, Switzerland](http://www.sourcepole.com/)
- SILVER Sponsor: [State of Vorarlberg, Austria](http://www.vorarlberg.at/)
- BRONZE Sponsor: [Lutra Consulting, UK](http://www.lutraconsulting.co.uk/)
- BRONZE Sponsor: [www.molitec.it, Italy](http://www.molitec.it/)
- BRONZE Sponsor: [www.argusoft.de, Germany](http://www.argusoft.de)
- BRONZE Sponsor: [www.openrunner.com, France](http://www.openrunner.com)
- BRONZE Sponsor: [GKG Kassel,(Dr.-Ing. Claas Leiner), Germany](http://www.eschenlaub.de/)

A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become an official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts.

If you enjoy using QGIS, please consider making a donation to support the project - either [financial](https://qgis.org/en/site/getinvolved/donations.html) or of [your time and skills](https://qgis.org/en/site/getinvolved/index.html)! Lastly we would like to also take a moment to encourage you to fund a [special campaign](http://blog.vitu.ch/10102014-1046/crowdfunding-initiative-automated-testing) by one of our QGIS developers to get a working test suite for QGIS so that we can improve out quality assurance process and deliver you the best possible releases.

QGIS é um software livre e você não tem obrigação de pagar nada para usa-ló - de fato queremos encorajar pessoas de todo o lado para usá-lo independentemente do seu status financeiro ou social - acreditamos que capacitar as pessoas com ferramentas de tomada de decisão espacial resultará em uma sociedade melhor para toda a humanidade.

{{<table-of-contents >}}
## Geral
### Funcionalidade: Nome do ficheiro do projecto nas propriedades
Pode agora ver o caminho completo para o ficheiro do projecto QGIS no dialógo de propriedades do projecto.

![](images/entries/8662dc4a69298f603dd9038d1199ab16fd25f786.webp)
### Funcionalidade: Permissão para remover o último ponto na medição através da tecla del/backspace
Agora quando mede áreas e distâncias, pode remover vértices indesejados a partir da linha da sua medição usando as teclas delete ou backspace.

![](images/entries/ed471908937cb068e2f004e7b3311f2bdf307042.webp)
### Funcionalidade: selecciona um elemento relacionado no enquadramento a partir do widget da relação de referência
### Funcionalidade: Widgets Editor
Fizemos numerosas melhorias nos editores de widgets:
- novo editor de widget para data/tempo capaz de definir datas nulas
- edição do filtro na linha
- Correcta manipulação em valores NULOS para widgets de edição
- O widget fotografia preserva o valor NULO
- O widget Web preservam o valor NULO
- A tabela de atributos conseguem distinguir entre 0 e NULO
- Adicionado o sufixo ao widget de intervalo

![](images/entries/78fd27b2cf736f37bdf97694a5018f29c609c6cb.webp)
### Funcionalidade: Opcionalmente use um subconjunto de campos numa junção de camada
Agora você pode usar apenas um subconjunto de campos relacionados ao criar uma união vetorial.

![](images/entries/14023cf2ee768960d9c4a43da6e2a1624d10b3c3.webp)
### Funcionalidade: Campo expressão (campos virtuais)
Sometimes you want to have an attribute that is calculated and that is always \'fresh\' - reflecting the current state of the feature properties. Now you can add virtual fields to your table which are based on an expression.

![](images/entries/5fe53ad54b8d0cf8b7a22b90e733a421bb929506.webp)
### Funcionalidade: As acções podem agora ter um ícone associado
Quando cria uma acção personalizado para uma camada vectorial, pode agora definir um ícone para essa acção.

![](images/entries/e7bd5b306e3a72cc111a81f86a053b42679aa2f8.webp)
### Funcionalidade: tipos de expressões e opções adicionais
- Allow using `+` for string concatenation.
- New keyword: `attribute( feature, attribute_name )` - gets the specified attribute from a feature.
- New keyword: `$currentfeature` - returns the current feature.
- New keyword: `$atlasfeature` - returns the atlas feature.
- New keyword: `getFeature` - gets a matching feature from a layer.

![](images/entries/e2e079bec87be65ccc97055251fc2544be91aaab.webp)
### Funcionalidade: Classes dentro dos renderizadores graduados e categorizados podem ser activados
Pode agora escolher que classes desactivar nos renderizadores graduados e por categorias sem remover nenhum.

![](images/entries/84d11c6d978775d92f6a1902092795735d1f32b3.webp)
### Funcionalidade: Melhorias na legenda
A revisão da segunda fase da legenda / tabela de conteúdo  foi concluída. Isso inclui:
- Limpeza da API (para programadores)
- Grupos de visibilidade das camadas do mapa na árvore de camadas. Este novo botão da barra de ferramentas permite mudanças rápidas entre os grupos de camadas que devem ser visíveis.
- Capacidade de gerir grupos de camadas a partir da barra de ferramentas da legenda
- A nova opção de filtro de legenda localizado na barra de ferramentas da legenda irá remover itens da legenda para as classes que não estão atualmente na vista do mapa. Essa é uma melhoria impressionante, pois garante que a legenda do seu mapa não contenha entradas para os itens que não estão atualmente na visualização do mapa. Ele está disponível na principal legenda do mapa, no mapa compositor e para as camadas WMS.
- As legendas do renderizador baseadas em regras agora podem ser exibidas em uma pseudo-árvore

![](images/entries/363048a7d08ac76d35463abbef514c65031922e7.webp)
## Provedores de dados
### Funcionalidade: Melhorias na exportação de DXF
- vista da árvore e selecção do atributo para atribuição da camada no diálogo
- suportar o preenchimento de polígonos/HATCH
- representa textos como MTEXT em vez de TEXT (incluindo fonte, inclinação e peso)
- support for RGB colors when there\'s no exact color match
- use o AutoCAD 2000 DXF (R15) em vez do R12
- remove os métodos testes R18

![](images/entries/4f615505e3fd6ec0b619278e42ecc5a3e79ac827.webp)
## Compositor de mapas
### Funcionalidade: Controlo sobre itens de compositor de impressão escondidos a partir de impressões/exportações
Nós adicionamos uma caixa de seleção e um botão de dados definido para controlar se um item é excluído do compositor exportações / impressões. Se o item for desmarcado será visível n o composição de impressão uma única vez.

![](images/entries/f334447d13ee49a6c4c5cb4322e3f12824643416.webp)
### Funcionalidade: Controlo sobre a impressão de página para molduras vazias do compositor
Para tabelas ou molduras HTML, uma caixa de verificação agora controla como a página continda deve ser exportada quando a moldura está vazia.

![](images/entries/1500ba6abdf5b314c760ebfc63e460731dcc5110.webp)
### Funcionalidade: Item painel de árvore
A aba item, localizada no painel do compositor de mapas permite selecionar itens, habilitar ou desabilitar sua visualização, alterar status, e, a partir de clique duplo alterar a nomenclatura do mesmo. É possível também arrastando os mesmos ordenar conforme a necessidade.

![](images/entries/52b70bdf87d21a13c00798458bab6347dddd7910.webp)
### Funcionalidade: Mais controlo sobre a aparência dos itens linha/seta do compositor
- As linhas podem ser estilizadas usando símbolo de linha de diálogo estilo
- Paleta de Cores de contorno e preenchimento podem ser definidos pelo usuário
- Largura do contorno da cabeça da seta pode ser definida pelo usuário

![](images/entries/49757b3cc09839edb8af38f1cb1317458f279110.webp)
### Funcionalidade: Controle de Dados definidos de composição de itens
Muitas propriedades dos itens do compositor podem agora ser controladas com a sincronização de dados. O que incluem: 
- Transparência e modo de mesclagem.
- Rotação de item.
- Escala do mapa, extensões e rotação.
- Margem de feição do Atlas.
- Tamanho e posição do item.
- Tamanho da página, orientação e números de páginas.

![](images/entries/9f321489cd9c90eb4d66e577680fc5467756e58e.webp)
### Funcionalidade: Imagens do compositor podem ser especificadas por URLs remotos
Itens de imagens a serem adicionados no compositor de impressão agora possuem também o suporte de urls remotas como fonte.  Esta fonte pode ser também um dado definido.

![](images/entries/05cd7008c231df3b3af874753b840669a605cb0f.webp)
### Funcionalidade: Melhorias na Tabela do Compositor
- Agora pode definir o cabeçalho da tabela e as cores do conteúdo,
- Tabelas agora podem ser divididas através de múltiplas janelas, permitindo que seu conteúdo seja distribuído entre colunas ou entre diferentes páginas.
- Adicionado opção mostrar cabeçalhos no primeiro quadro, todos os quadros, ou sem quadros.
- Permite o controlo manual da largura da coluna.
- Novas opções para a origem da tabela, incluindo o recurso do atlas atual e os recursos filho de uma relação.
- A opção de comportamento para tabelas vazias inclui ocultar a tabela inteira, mostrar células vazias ou exibir uma mensagem definida no corpo da tabela.
- Adicionada uma caixa de seleção para filtrar as feiões da tabela para aqueles que cruzam o recurso do atlas atual.
- Caixa de seleção adicionada para remover linhas duplicadas da tabela.

Observe que as tabelas em projetos existentes não são atualizadas automaticamente para o novo formato de tabela que suporta esses recursos, e as tabelas devem ser lidas para uma composição para que as novas configurações apareçam.

![](images/entries/9ccb75b2110daf0c95a3fba31ac18144c1345f0e.webp)
### Funcionalidade: Melhorias no compositor
O compositor de mapas (usado para a preparação de mapas para impressão) recebeu uma série de melhorias no QGIS 2.6.
- Você pode agora mudar a cor secundária de preenchimento para a barra de escalas
- O deslocamento de espera ao desenhar itens de linha/seta restringe o desenho para ângulos horizontais, verticais ou de 45 graus
- Manter SHIFT enquanto desenha outros novos itens os restringe a quadrados, segurar ALT faz com que o item seja desenhado a partir do centro
- Clicar com o botão direito não bloqueia/desbloqueia mais os itens, isso agora é tratado pelo novo painel de itens. Os itens bloqueados não podem mais ser selecionados na tela do compositor, permitindo interação com itens abaixo deles.
- Segurar ALT enquanto pressiona as teclas do cursor resulta em um movimento de 1px para itens
- Removed the destructive \'Load from template\' menu item, replace with a new non-destructive \'Add items from template\' action

![](images/entries/a7267ed637121bc9be70c5fa0afd2a63f9790bc7.webp)
### Recurso: aprimoramento de encaixe de item
Os limites de captura agora são definidos em pixels, permitindo movimentos e redimensionamentos mais precisos dos itens quando ampliados para uma composição. Os itens dentro de um grupo não são mais usados para aderir linhas automáticas.

![](images/entries/8e43479380c28942345f3d9500dd956bd13f43e8.webp)
### Recurso: várias visões gerais de um item do mapa
Sometimes it is useful to be able to show more than one overview frame for a map frame. For example if you want to show where your map is in local, regional and global context, using multiple overview maps can help you to achieve this. As of QGIS 2.6 you can now achieve this by assigning as many maps as you like to the \'overview\' role in your composition.

![](images/entries/88b55cc5f5e7cfb62486fe3b4867b7133ae66953.webp)
### Funcionalidade: melhorias do item HTML
Existe um conjunto de novas opções para o item HTML do compositor:
- Opção para entrada manual da fonte HTML
- Expressões QGIS com a fonte HTML podem ser avaliadas depois da renderização do conteúdo HTML
- Dados definidos por um URL para uma fonte HTML
- Permite criar uma folha de estilos do usuário para rescrever os estilos HTML

![](images/entries/7ed388f0c775b738648b2bd6eb6be0a75fa5816a.webp)
### FuncionalidadE: Melhorias na grelha de mapa do Compositor
- Agora podem ter múltiplas grelhas com diferentes propriedades.
- Pode misturar grelhas reprojectadas e grelhas Lat/Long.
- Pode usar simbologias QGIS padrão para linhas, etc.
- Há um novo estilo de grade somente de quadros/anotações. Selecionar este estilo faz com que apenas o quadro e as anotações sejam desenhados, sem linhas de grade ou outras marcações sobre o mapa.
- Agora há opções para controlar em qual lado de um item do mapa a moldura é desenhada. 
- Existem novos estilos de vistos para quadros, com vistos internos, vistos externos e opções de visto interno e externo.
- Fizemos melhorias nas anotações de grade, incluindo muitos novos formatos de anotações.
- As anotações de grade agora usam os símbolos principal e duplo primos tipograficamente corretos para as anotações de grade.

![](images/entries/eeb61d7da3d3f95283b1bb47545cbdff9cc334ae.webp)
## Processamento
### Funcionalidade: Colecção online de modelos e scripts
Modelos e scripts podem ser baixados da coleção on-line e instalados diretamente da interface de processamento. A coleção será expandida com novos scripts e modelos fornecidos pelos usuários do processamento.

![](images/entries/23e357ca0e559a33a7872206b306c0b1fbdb4b7d.webp)
### Funcionalidade: Implementação do novo Modelador
O modelador foi reescrito e agora fornece funcionalidade extra, como permitir modelos aninhados sem limite de profundidade. Os modelos agora são armazenados como arquivos JSON. A compatibilidade com versões anteriores é mantida, portanto, todos os modelos ainda podem ser usados. Você também pode arrastar e soltar itens das entradas e algoritmos no gráfico do modelador.

![](images/entries/72bb8beaf97133424d1e68da67ae6fe79ea6faf6.webp)
## Programabilidade
### Funcionalidade: Alterações da API para os widgets QGIS
In order to normalise the naming of QGIS widgets, some minor API changes have been made. Almost all edit widgets were renamed by adding \"Wrapper\" at the end of their names. In particular this concerns:
- QgsCheckboxWidget -\> QgsCheckboxWidgetWrapper
- QgsClassificationWidget -\> QgsClassificationWidgetWrapper
- QgsColorWidget -\> QgsColorWidgetWrapper
- QgsEnumerationWidget -\> QgsEnumerationWidgetWrapper
- QgsFilenameWidget -\> QgsFilenameWidgetWrapper
- QgsHiddenWidget -\> QgsHiddenWidgetWrapper
- QgsPhotoWidget -\> QgsPhotoWidgetWrapper
- QgsRangeWidget -\> QgsRangeWidgetWrapper
- QgsTexteditWidget -\> QgsTexteditWrapper
- QgsUniquevalueWidget -\> QgsUniquevalueWidgetWrapper
- QgsUuidWidget -\> QgsUuidWidgetWrapper
- QgsValuemapWidget -\> QgsValuemapWidgetWrapper
- QgsValuerelationWidget -\> QgsValuerelationWidgetWrapper
- QgsWebviewWidget -\> QgsWebviewWidgetWrapper

## QGIS Server
### Funcionalidade: Melhorias na pesquisa com o pedido GetFeatureInfo
<https://github.com/qgis/QGIS/commit/8888c5f0c0e0ffdf23453a20addf6abaf125845d>
### Funcionalidade: Adição de uma configuração de precisão para os atributos de geometria para o GetFeatureInfo
## Simbologia
### Funcionalidade: Melhor escolha nas cores aleatórias
Melhoramos o algoritmo de cores aleatórias para o renderizador classificado, para que as cores geradas sejam visualmente mais distintas umas das outras.

![](images/entries/ec29c9d6eb23d01b4dbbae32a6e20fe0b1f48198.webp)
### Novidade: melhorias na interface de usuário da simbologia
- Quando possível, as propriedades do símbolo da camada são mantidas quando muda-se o tipo de símbolo.
- Adicionado um botão de edição para shapeburst e gradiente de rampas de cores.
- Atualização automática dos limites de rótulos e faixas vizinhas.
- Classes são automaticamente convertidas a partir de categorização ou classes graduadas quando troca-se para renderização baseada em regra.
- Adicionado unidades e número de casas decimais para rótulos de renderizador graduados.
- Maior capacidade de resposta às mudanças no gradiente de cores, gradiente de cores invertidas e outras opções na GUI.
- Reter o símbolo ao alternar entre renderizadores simples, graduados, categorizados e outros.
- Rotulagem aprimorada do modo de cálculo StdDev.

![](images/entries/08305d5131c28c45b400662267ff0d174ef9c8ce.webp)
## Interfaçe de usuário
### Recurso: Editor de código de destaque da sintaxe
Para editores de scripts python, construtor de expressões, janela de filtragem, compositor de HTML e editores de CSS

![](images/entries/54b470a064d65d6d65aa66a8feece43ba8cbf6c4.webp)
### Funcionalidade: Paletas de cores
Você agora pode definir suas próprias paletas de cores personalizadas para uso no QGIS.
- Paleta de cores global do usuário personalizada (na caixa de diálogo de opções).
- Paleta de cores por projeto (no diálogo de propriedades do projeto).
- As cores são exibidas nos menus de botões coloridos e na nova caixa de diálogo de seleção de cores.
- Você pode importar/exportar cores para um arquivo de paleta GPL.

![](images/entries/a156f408d7a87fc930095c8fd68e9fba0fc0a817.webp)
### Funcionalidade: Nova caixa de diálogo de seleção de cores
Existe uma nova caixa de diálogo de seleção de cores QGIS personalizada. As características incluem:
: - Sliders para matiz, saturação, valor, vermelho, verde, componentes de cor azul.
  - Controle deslizante alfa.
  - Opção de copiar/colar códigos de cores html (numa variedade de formatos).
  - Antes/depois da pré-visualização de cores, com pré-visualização alfa.
  - Widget de rampa de cor 2D interativo.
  - Hue wheel/triangle widget.
  - Paletas de cores editáveis, incluindo a capacidade de criar novas paletas e importar/exportar cores para um arquivo de paleta GPL.
  - Amostrador de cores ao vivo com a opção de amostragem sobre um raio definido (dependente do suporte ao sistema operacional).
  - Suporta interação com outros aplicativos através de arrastar e soltar cores (dependente do suporte ao SO).
  - Opção para desabilitar a caixa de diálogo e usar a caixa de diálogo do selecionador nativo.

![](images/entries/7189c0fe2d1ff3fdc63c531a02f74b5d32b70bfd.webp)
### Recurso: Ferramenta de seleção de recurso único mesclada em selecão por retângulo
Nós mesclamos a ferramenta de seleção única na ferramenta de retângulo. Se você quiser selecionar um único recurso, simplesmente ative a ferramenta retângulo e, em seguida, clique uma vez em (em vez de arrastar um retângulo) um recurso.

![](images/entries/f8a68fcdfcaa59e6162185acb5c92edb9145c881.webp)
### Funcionalidade: Adicionar camada para mapear o comportamento da tela
In many of QGIS\' dialogs that generate a new layer, the \'Add layer to map canvas\' checkbox is now checked by default so that the new layer automatically gets added to the map.

![](images/entries/f36f5912d2422a439d67b1a743fe81588e709dfb.webp)
### Funcionalidade: Adição do ícone de tamanho 48 e 64
Para aqueles que usam o QGIS em dispositivos tácteis (ou se deseja icones grandes), pode agora definir os ícones até ao tamanho de 64 x 64 pixeis.

![](images/entries/3be3f51da2f54a8395f054f757f9fae1948a6103.webp)
### Funcionalidade: Novos botões de cores
This is probably one of the most useful new features in QGIS 2.6 -especially if you are involved a lot in cartography work. The colour button used everywhere in QGIS has been enhanced, with drop down menus, colour swatches, default colours, etc. Click on the drop down item to the right of the colour button to see the quick options. Click on the button to the left of the colour widget to see a standard colour chooser dialog.

![](images/entries/54c211513bc86d00a5bce01a17476481937e0fbe.webp)
### Funcionalidade: Menu de contexto para a ferramenta de identificação
Ao usar a ferramenta de identificação, agora você pode clicar com o botão direito do mouse na tela para usar a ferramenta de identificação no modo de contexto. No menu que aparece, você pode definir quais tipos de recurso você deseja identificar (todos, se quiser).

![](images/entries/c395c2ce4964826458a721a8a3f89cb7dc2853b5.webp)

{{<content-end >}}
