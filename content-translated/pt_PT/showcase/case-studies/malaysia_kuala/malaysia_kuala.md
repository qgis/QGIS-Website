---
draft: 'true'

---
# QGIS no Departamento Federal de Planeamento Urbanístico, Malásia Peninsular
## Introdução
O Departamento Federal de Planeamento Urbanístico, da Malásia Peninsular (JPBD) é um agência federal que faz aconselhamento em questões de planeamento urbanístico. O âmbito desta administração para o departamento, porém, é limitado à península da Malásia porque Sabah e Sarawak na Malásia Oriental têm as suas respetivas agências de planeamento urbanístico. O Ordenamento do território está na lista atual da Legislação Federal, portanto, no nível federal, JPBD aconselha a Habitação e o Ministro do Governo local a partir do qual JPBD recebe o seu auxílio, bem como aconselha o Conselho Nacional de Planeamento Físico presidido pelo Primeiro-Ministro . No nível estadual, o diretor estadual informa o Comité de Planeamento do Estado presidido pelo ministro-chefe. No nível local, JPBD aconselha as autoridades de planeamento local em matéria de planeamento estando envolvido na preparação obrigatória de planos de desenvolvimento. Na sede, a Divisão Nacional de Plano Físico prepara o Plano obrigatório Nacional Físico enquanto quatro escritórios regionais de projetos auxiliam na elaboração de Planos de estrutura do Estado, os Planos Distritais Locais e os Planos de Área especial. Como os órgãos públicos eram tradicionalmente estabelecido de base em sua especialização, JPBD é o que guarda a informação do uso do solo.
## O Projeto
O QGIS foi introduzido pela primeira vez na comunidade de Código Aberto da Malásia como uma alternativa viável para o software SIG proprietário nos órgãos públicos pelo JPBD na Conferência de Código Aberto no Governo da Malásia (MyGOSSCON) em 2009 e para a comunidade SIG da Malásia na 4 ª Conferência Nacional de SIG e Exibição (NGIS) em 2010. JPBD tem sido, tradicionalmente, um utilizador de SIG proprietário, logo, a introdução do QGIS foi um abrir de olhos, não só do ponto de vista de Software de Código Aberto (OSS), mas também, OSS SIG. A filosofia Código Aberto era diferente assim como o usar o QGIS era estranho, inseguro e perigoso, e surpreendentemente a ideia de usar o QGIS não recebeu muito apoio internamente, de facto, enfrentou resistência em 2010, a partir da gestão de topo até ao grupo de apoio.

![MyGOSSCON, 2009](./images/malaysia_kuala1.png){.align-right}

On the opposite side, request for technical talks on QGIS came from other technical agencies which JPBD gave to the Ministry of Works and the Department of Irrigation and Drainage. Other works to promote QGIS from JPBD came in the form of newsletter articles on QGIS to the Open Source Competency Centre (OSCC) at the Prime Minister\'s Department and articles introducing QGIS to the Survey Department\'s GIS Bulletin and the Ministry of Natural Resource\'s Public Sector GeoSpatial Bulletin. In the meantime, JPBD researched on developing a slope analysis module for QGIS\'s Windows and Ubuntu version.

O estudo destacou prós e contras de personalizar um módulo e o alto nível de compromisso na gestão necessária para garantir o seu sucesso e adopção contínua. Em 2011, a JPBD começou a fazer mais pesquisas sobre o QGIS mais como uma ferramenta analítica invés de uma ferramenta de mapeamento, a fim de explorar novos módulos pioneiros ou encontrar novas abordagens para explorar o QGIS.

O departamento eventualmente promoveu o pacote QGIS-GRASS em vez do simplesmente QGIS como foi encontrado para ser mais poderoso e útil para fins de planeamento urbanístico, tais como a limpeza de erros de topologia e superar as limitações das entradas padrão. Isso foi apenas o começo.

![Northern Project Office get QGIS training](./images/malaysia_kuala2.png){.align-right}

In order to centralize and share findings in the use of QGIS for town planning purpose which could also be use in other fields dealing with spatial analysis, an unofficial blog established by the author called "QGIS MALAYSIA" at <http://www.qgismalaysia.blogspot.com> was made to generate a QGIS community in Malaysia. External agencies seem to have more interest in QGIS than JPBD itself and upon their request, JPBD gave QGIS training to the Fire and Safety Department as well as to the Ministry of Education whom later was convinced QGIS will be their de facto GIS tool.

Hearing this, JPBD\'s Research and Development Division took the initiative and requested for QGIS training and subsequently 12 persons were trained. Word of mouth (a godsend thing, though at times, extremely detrimental) spread that QGIS was indeed user-friendly, easy to use and at par with proprietary GIS in mapping task and could take on proprietary GIS when optimized with GRASS modules.

O interesse no QGIS aumentou e em 2012, com o apoio total dos diretores de projeto, um um esforço feito por todos na Divisão Nacional de Informação de Uso do Solo e espalharam a formação do QGIS para 4 gabinetes de projeto onde detinham o maior número de utilizadores SIG. No final de 2012, foi revelado que pelo menos 320 equipas no JPBD iriam usar QGIS e que contavam com aproximadamente 90% de utilizadores SIG do departamento. 

That is not all. States town planning departments have also requested QGIS training such as Perak including strong interest from poorer states like Perlis and Kelantan. If this catches on, it is anticipated that the use of QGIS may dominate states planning departments and even extend to local planning authorities, many of which are not wealthy. In the meantime, JPBD is seriously studying the use of the QGIS-PosgreSQL-PostGIS package for every planning office\'s client GIS-geodatabase server structure to serve as the foundation of JPBD\'s integrated landuse (iPLAN) network.
## Resultado do uso do QGIS
- Assumindo que por licença de um SIG proprietário ronda 10,000 RM, o uso de 320 instalação ajuda a poupar ao governo federal 3,200,000 RM;
- A total erradicação da pirataria nos SIG e aumento da confiança no uso do na generalidade dos OSS e especificamente os SIG OSS;
- A formação de QGIS é simples de gerir. Isto significa aprendizagem cruzada entre equipa, divisões, agências públicas e mesmo autoridades locais de planeamento que usam o QGIS mais eficazmente por ser usada de forma uniforme.
- O uso do QGIS ajuda a sinergia  do PostgreSQL, e das base de dados geográficos PostGIS que o departamento está a planear usar como base na sua base de dados geográfica de uso do solo para toda a península da Malásia.
- É mais rápido no processamento de verificação de dados e limpar erros de topologia.
- Os utilizadores ficam mais encorajados a começar a aventurar-se no Google Maps e outras fontes da internet para informação secundária;
- Sendo fácil de utilizar, o QGIS incentiva os utilizadores para serem mais aventureiros e para explorarem muitos dos módulos disponíveis, tornando-se uma vantagem e faz com que a sua tarefa seja mais fácil.
- SIG é uma ferramenta complexa que torna-se um amigo em vez de um obstáculo.

## Sobre o autor:
![Abbas Abdul Wahab](./images/malaysia_kualaaut.jpg){.align-left height="200px"}

This article was contributed in January 2012 by Abbas Abdul Wahab. Abbas graduated as a town planner from Gloucestershire College of Arts & Design, United Kingdom in 1980 and has a Masters of Science in GIS & Geomatic Engineering from Putra University Malaysia in 2002. He is currently the Head of the National Landuse Information Unit at the National Landuse Information Division of the Federal Department of Town & Country Planning, Peninsular Malaysia.
