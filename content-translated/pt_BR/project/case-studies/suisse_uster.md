---
HasBanner: false
archived: true
date: 2011-04-01
draft: false
featured: false
section: projeto
sidebar: true
thumbnail: images/suisse_uster1.png
title: O uso do QGIS na Infraestrutra de Geoinformação na Cidade de Uster
type: case-study

---
{{<content-start >}}
# O uso do QGIS na Infraestrutra de Geoinformação na Cidade de Uster
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>April 01, 2011</span>
</p>

A cidade de Uster tem vindo a usar o QGIS desde 2007. Encorajados pela decisão do Cantão de Solothurn em usar o QGIS como um substituto SIG Desktop para ArcView, a cidade de Uster decidiu também dar-lhe uma tentativa. A cidade juntou-se no esforço para o desenvolvimento do software QGIS, sugerindo e testando novos recursos e apoiando financeiramente o seu desenvolvimento. Em troca Uster recebe uma evolução rápida e independente de plataforma SIG Desktop e a solução WebSIG apoiado por uma comunidade de usuários e desenvolvimento em todo o mundo.

![](../images/suisse_uster1.png)

O Postgis/PostgreSQL é usado como um armazém central de geoinformação. Outras base de dados e fontes de dados são reproduzidos no PostgreSQL num intervalo regular, usando as ferramentas como o OGR r FME. No início o QGIS era apenas um visualizador. O primeiro usuários do QGIS foi um agricultor que tinha a tarefa de supervisionar as declarações feitas pelos agricultores locais para receberem os subsídios agrícolas. Mais tarde, o QGIS também introduziu um editor de informação e uma plataforma de publicação de mapas, juntamente com melhoramentos nas ferramentas de edição e no compositor de mapas. Juntos como outros usuários QGIS suíços (Solothurn, Thun e CDE (Universidade de Berne)) nós coordenamos e patrocinamos os melhoramentos para essas ferramentas, juntamente como algumas melhorias na informação orientada para a simbolização, rotulagem automática, manuseamento de atributos e formulários.

![](../images/suisse_uster2.png)

A administração da cidade também usa um software SIG comercial: Autodesk Topobase, para recolher e editar informação cadastral e de infraestrutra de desperdício de água, e GE Smallworld para a gestão de redes do gás, água e  electricidade. Contudo, estes são sistemas especialistas usados por pessoal especialmente formado. Todos os outros projectos de SIG e visualização de todos os dados é tratado pelo QGIS.

In the second half of 2010, first tests with QGIS server were carried out. In 2011 we introduced a new WebGIS system based on the QGIS WMS server and GeoExt/OpenLayers as the web client. The main reasons for the decision to use QGIS server were the considerable time savings made possible by re-using the existing QGIS desktop project configurations, rather than having to manage parallel Web project configurations. Additional advantages are the rich set of symbolization and labeling options and the consistent map rendering between the Desktop GIS application and the Web-GIS. The QGIS webclient can be tested and used at <http://gis.uster.ch/>

![](../images/suisse_uster3.png)

Actualmente, o QGIS é usado para os seguintes projectos SIG:
- visualização de informação de desperdício de água, integração de bases de dados adicionais e acesso directo a vídeos de canais e protocolos de inspecção
- visualização e edição para a monitorização do planeamento urbano e ambiental dos desperdícios de água e sistemas de hidrologia. (alemão:  Genereller Entwässerungsplan)
- visualização de dados cadastrais subterrâneos (desperdício de água, água, redes de electricidade e gás, e por fim telecomunicações) (alemão: Leitungskataster)
- visualização de dados cadastrais e levantamentos
- visualização e edição de inventários de baldios e sítios naturais de protecção
- visualização e edição da informação do planeamento regional e urbano
- visualização e edição da informação da infraestrutura de rede viária
- visualização de estatísticas geradas directamente da base de dados dos residentes actuais e do passado
- Planejamento e visualização do planejamento para a energia (regiões de fornecimento de gás, calor usado do desperdício de água, energia geotermal à superfície, estações de blocos de aquecimento, etc.)

Projetos adicionais estão atualmente em desenvolvimento.

![](../images/suisse_uster4.png)

Em 2007 não foi totalmente claro em que ritmo o QGIS seria desenvolvido e como a comunidade e o apoio comercial iriam evoluir. Hoje pode-se afirmar que a velocidade do desenvolvimento e as melhorias feitas pela comunidade QGIS superou as nossas expectativas. A comunidade e o suporte comercial das empresas Sourcepole e Norbit é excelente. Há uma comunicação directa com os programadores sem ser blindados pela gestão de produto ou equipa de vendas. Os programadores das duas empresas são também programadores líderes do projecto QGIS e têm um excelente conhecimento do código base.

Os erros são muitas vezes fixados em horas ou dias após a notificação e as novos desenvolvimentos são implementados num curto espaço de tempo. As novas funcionalidades podem ser testados imediatamente após o desenvolvimento e distribuído para os usuários, sempre que a qualidade é boa e suficiente para o usuário final. Não há necessidade de esperar por lançamentos oficiais de software. Nós apreciamos a liberdade de ser capaz de influenciar o projeto e instalar o software em quantos computadores que gostamos, sem ter que lidar com a gestão de licenciamento. Estamos a olhar para a frente para uma futura colaboração com a comunidade QGIS e os nossos apoiantes comerciais para o avanço do projeto QGIS.
## Autor
<figure>
<img src="../images/suisse_usteraut.jpg" class="align-left" height="200" alt="suisse_usteraut.jpg" />
<figcaption>Andreas Neumann</figcaption>
</figure>

Este artigo foi contribuído em Abril de 2011 pelo Dr. Andreas Neumann, Ele é coordenador SIG na Cidade de Uster, Suíça.

{{<content-end >}}
