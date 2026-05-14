---
HasBanner: false
archived: false
date: 2016-04-01
draft: false
featured: true
section: projeto
sidebar: true
thumbnail: images/ft_europe_migration_balkan-route.png
title: Uso de GIS na equipe gráfica do Financial Times
type: case-study

---
{{<content-start >}}
# Uso de GIS na equipe gráfica do Financial Times
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>April 01, 2016</span>
</p>

## Entrevista com Steven Bernard (Editor de Design Interativo)
Steven is an Interactive Design Editor at Financial Times. You can find him on [Twitter](https://twitter.com/sdbernard). He also publishes useful [HOWTO Videos on Youtube](https://t.co/6aTE6G8h0T) for certain cartographic tasks in QGIS.

**QGIS**: Steven, qual o nome da equipe na qual você trabalha no FT? Você poderia nos dar um panorama sobre o que a sua equipe no FT está fazendo?

**Steve**: Nossa equipe está em um período de transição no momento, nós temos um novo editor de visualização de dados, Alan Smith OBE (antigamente da ONS), que está revolucionando as coisas e criando uma equipa gráfica única. Tradicionalmente nós tínhamos uma equipe gráfica web e uma equipe gráfica impressa. A equipe gráfica impressa seria a responsável por toda a arte gráfica do jornal, assim como pela criação de versões amigáveis para web dos mesmos. Minha equipe era responsável por todo o conteúdo exclusiva paro web, bem como trabalhar de perto com os produtores/desenvolvedores interativos no desenho de artes gráficas interativas.

A recém-formada equipe permitirá uma maior troca de habilidades entre as diferentes mídias.

Alan introduziu um fluxo de trabalho digital único para nossa equipe, incluindo utilizar d3 para auxiliar a criação de um vocabulário gráfico maior e reduzir o tempo que o mesmo leva para criar os visuais.

![](../images/ft_europe_migration_balkan-route.png)

*Exemplo: Fluxos migratórios. Rota das Balcãs Ocidentais.*

**QGIS**: Há quantos colegas de trabalho na sua equipe?

**Steven**: Incluindo todos os designers, desenvolvedores, produtores e estatísticos nós temos uma equipe de 24

**QGIS**: What\'s your specific role within the team?

**Steven**: We are a multi-disciplinary department so I don't have a specific role as such. My role includes producing responsive designs for interactive graphics as well as doing the front-end development on the less complicated interactives (e.g. [Inside Isis Inc: The journey of a barrel of oil](http://ig.ft.com/sites/2015/isis-oil/)). I also produce the standard news related charts and maps on a daily basis. Over the past two years I have been concentrating on developing our cartographic offerings at the FT. QGIS has been instrumental in changing how we produce maps, and in conjunction with other tools such Blender have helped me to be more creative with how we approach maps.

![](../images/ft_nigeria-migration_animation.gif)

*Example: Animation of Dora\'s journey from Nigeria to Sicily - one of thousands by trafficked women each year.*

**QGIS**: Can you tell us a bit about yourself? What\'s your educational background? What did you do before joining the data visualization team at FT?

![](../images/ft_gotthard-tunnel.png)

*Exemplo: túnel ferroviário e rodoviário de Gotthard nos Alpes suíços.*

**Steven**: I am traditionally trained as scientific illustrator. What's that I hear you ask? It involves producing illustrations for medical journals, natural history publications anything where you are trying to convey information visually where a photograph can't. Think of diagrams showing the human circulatory system, or showing a procedure to fix a broken bone. Sadly there wasn't much call for that kind of work when I left university and I basically fell into the job at the FT. I have always been good at maths, which I think is important when working with data visualisations, it has certainly helped me with my coding as well.

**QGIS**: Como você descobriu o QGIS?

**Steven**: I came across QGIS in 2013 when we were working on a [project mapping the ethnicity of the Middle East](http://ig.ft.com/features/2013-07-19_middleeast_religion_map/dist/index.html)

We used it to georeference maps that were created by a professor at Columbia University. At first I found it really tricky using the add feature drawing tool, probably because it was unlike anything I'd used in Adobe Illustrator for 17 years prior! I also found it frustrating that you had to save things twice, once when done editing the shapefile, then again to save the project. However, this was just down to inexperience with the program and in the end it did exactly what we needed, which was to produce shapefiles that we could add to a Mapbox base map.

**QGIS**: What\'s the role of QGIS within your usual workflows?

**Steven**: QGIS is now an integral part of our mapping workflow. I don't use any other GIS tool to create our maps. Although a few members of our team also use Map Publisher as they feel more comfortable staying within Adobe Illustrator. I would say 80% of our maps are now produced in QGIS.

![](../images/ft_blm-federal-land-map.png)

*Exemplo: Terras públicas no Brasil.*

**QGIS**: Que outras ferramentas você usa além do QGIS e como você combina eles?

**Steven**: Se for apenas um mapa simples, 95% do trabalho é feito no QGIS, com o polimento final feito no Adobe Illustrator.

Se estou fazendo um mapa de relevo, o processo é muito mais complexo. Recuperarei arquivos DEM do Nasa Earth Explorer e os trarei para o QGIS para cortar o tamanho. Então, levarei o DEM recortado para o Blender para criar uma renderização 3D. Se eu estiver usando uma sobreposição de satélite no hillshading, baixarei uma imagem BlueMarble da Nasa e levarei isso para o Blender também. A renderização exportada do Blender é então trazida de volta para o QGIS para ser usada como uma camada de background. Eu posso ajustá-lo no Photoshop antes, se necessário.

For responsive maps like those in the [Isis oil story](http://ig.ft.com/sites/2015/isis-oil/), I used all of the above tools but the final step is to use an open source Adobe Illustrator script developed by the New York Times' Archie Tse. This allows me to create responsive versions of my maps that work on all devices.

Outra ferramenta útil é o Meus Mapas Google, que permite que repórteres ao redor do mundo marquem locais no mapa e então podemos baixar como um arquivo kmz e importar diretamente para o QGIS.

A ferramenta final que uso é o Adobe After Effects, pois recentemente comecei a animar meus mapas para levar o usuário em uma jornada. Como usado na série Land Rush recentemente:
- [Land Rush Ethiopia](https://ig.ft.com/sites/land-rush-investment/ethiopia/)
- [Land Rush Myanmar](https://ig.ft.com/sites/land-rush-investment/myanmar/)
- [Land Rush Indonesia](https://ig.ft.com/sites/land-rush-investment/indonesia/)

**QGIS**: Você utiliza outras ferramentas espaciais ou SIG além do QGIS, e se sim, quais?

**Steven**: QGIS todo o caminho para mim, mas como mencionado acima, alguns dos meus colegas também usam o Map Publisher.

![](../images/ft_isis-air-strikes_febupdate.png)

*Exemplo: Greves na Síria em Fevereiro de 2016.*

**QGIS**: Você pode descrever os prós e os contras do QGIS baseado nas tarefas que você tem que realizar? 

**Steven**: When I first used QGIS I saw it as a specialist tool, fit for only dealing with specific tasks. I really didn't see it a production tool. In late 2014 two of my colleagues went on a QGIS course held by Alasdair Rae at Sheffield University. They both enthused about how good QGIS was, so I took it upon myself to evaluate it as a tool that could be used to produce all our maps.

Dentro de duas semanas, estava convencido de que seria viável. O principal ponto de venda foi a capacidade de configurar guias de estilo para tudo, incluindo estilo de nível de zoom para mapas de ruas.

Eu tenho um sistema configurado onde temos conjuntos de folhas do Google com colunas para nome, lat, long, ícone de marcador, peso da fonte, tamanho da fonte e se você deseja que o marcador seja visível ou não.

O ícone do marcador é um menu suspenso conectado a uma tabela vLookUp que preenche todos os detalhes desse marcador.

Então tudo o que tenho a fazer é baixar o csv, importá-lo para o QGIS, aplicar um estilo e tenho um mapa que está 95% pronto para ser usado.

To be perfectly honest I can't think of any weaknesses, there are a couple of things that I would like to see or be able to do but, I don't see that as a weakness, just a missing feature.

![](../images/ft_chinaMigration.png)

*Exemplo: Atração Urbana e Migração na China.*

**QGIS**: Quais são os conceitos ou recursos que você mais gosta no QGIS?

**Steven**: Existem inúmeros recursos que eu classificaria como salva-vidas! Mas principalmente o Quick OSM e o Georreferenciador me pouparam muito tempo, isso é absolutamente essencial quando os prazos estão apertados. O que, quando se trabalha para uma organização de notícias, geralmente é 90% do tempo.

![](../images/ft_china_henanGuangdong.png)

*Exemplo: Atração Urbana e Migração na China. Visualizações de detalhes.*

**QGIS**: Quais funcionalidades do QGIS que você sente falta? Você tem uma lista de funcionalidades ausentes que ajudariam muito se fossem implementadas?

**Steven**: A couple of things I would like to see in future versions are\...

Bezier curve support, this would be particularly useful in conjunction with Georeferencer. I know there is a spline plugin but it doesn't give you the full control a bezier curve would.

Ser capaz de salvar como imagem em tamanhos de arquivo maiores. Atualmente esta é a única maneira que eu posso criar uma cultura georreferenciada de um arquivo DEM para levar para o Blender. Mas é limitado ao tamanho da sua tela. Se eu tivesse um arquivo DEM de 8.000 pixels carregado no QGIS, gostaria de poder exportar a cultura em tamanho maior do que a minha tela para uso em vídeo HD, por exemplo.

**QGIS**: Se você perder alguns recursos do QGIS que o ajudariam - você consideraria melhorar o QGIS sozinho (com codificação no núcleo QGIS ou plug-ins do Python) ou consideraria contratar um desenvolvedor QGIS para implementar o recurso ausente? você? Ou você procuraria outras ferramentas para preencher essa lacuna?

**Steven**: I certainly don't have the necessary skills to do the coding myself, I'm fairly proficient in Javascript but would struggle with Python. I would love to hire a developer to get features implemented but unfortunately I'm not in control of any budgets, so I use other tools to get around this.

![](../images/ft_us_broadband_internet_subscription.png)

*Exemplo: Porcentagem de domicílios com assinatura de internet banda larga nos EUA.*

**QGIS**: Let\'s talk about user experience - the QGIS team is aware that there are various places in the UI (dialogs, panels, etc) that could be improved a lot. Can you tell us a little bit where in the UI you see the biggest potential for a UI overhaul?

**Steven**: I think the main tools are fine as they are, once you are familiar with them they're pretty obvious. However, one thing I do find a little frustrating is trying to hunt down a plugin once it's been installed. They either create their own menu (MMQGIS), live under one of the menus (Georeferencer) or create their own icon (threejs). It would be handy to have a plugin window that has all installed plugins in it. Again this isn't a deal breaker but would make it easier than hunting in several different locations.

**QGIS**: Obrigada por seu tempo e pelo trabalho que você realiza promovendo e documentando fluxos de trabalho no QGIS! 

![](../images/ft_potrait_steve_bernard.jpg)

*Retrato de Steve Bernard. Editor de Design Interativo no Financial Times.*

**Steven**: A pleasure, I'm almost evangelical about QGIS! Hence the [31 video tutorials](https://t.co/6aTE6G8h0T) and always happy to spread the word.

Entrevista por A. Neumann e T. Sutton. Abril, 2016.

{{<content-end >}}
