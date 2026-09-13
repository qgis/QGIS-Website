---
HasBanner: false
archived: true
date: 2015-10-30
draft: false
featured: false
section: projeto
sidebar: true
thumbnail: images/italy_cesena1.png
title: QGIS na descrição do Muro de Cesena
type: case-study

---
{{<content-start >}}
# QGIS to describe the Cesena\'s Wall
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>October 30, 2015</span>
</p>

A ECAMPUS UNIVERSITY foi criada como uma universidade online e foi reconhecida pelo MIUR (Ministério Italiano de Educação, Universidade e Pesquisa) por meio do Decreto Ministerial de 30 de Janeiro de 2006. Foi concebida com o intuito de prover acesso à universidade, através de sua plataforma de ensino online, para a população mais jovem, profissionais, empresários, executivos e atuantes no mundo dos negócios e na cultura, com a intenção de contribuir para o mercado de trabalho. A sede, também conhecida como Campus Internacional de Milão, ou Campus de Novedrate, está localizado no antigo centro de treinamento da IBM de Novedrate (Como, Itália), em um campus na quieta e verde Brianza.

A universidade possui 5 faculdades virtuais: Engenharia, Economia, Psicologia, Artes, Direito. OS MAPAS HISTÓRICOS E O PROJETO QGIS O Muro da Cidade caracteriza a cidade a cidade de Cesena. A forma de escorpião divide o centro histórico da zona mais jovem.

Os documentos cartográficos históricos descrevem sua evolução e suas destruições. O programa QGIS permitiu que eu comparasse diferentes mapas históricos, já que ele permite transferir todos os mapas para um mesmo Sistema de Referência, com o complemento de georreferenciamento. Como referência foram usadas a camada livres do Google Satellite e a camada livre do Open Street Map para vincular todos os mapas históricos ao mesmo Sistema de Referência EPSG: 3857 (Mercator Web ou Pseudo Mercator).

O QGIS tem sido uma ferramenta fundamental para elaborar, analisar, comparar estes mapas georreferenciados através de camadas vetoriais ou shapefiles, nos quais eu inclui todos os elementos dos maps, como estradas, edifícios, parques e jardins, o Muro da Cidade, as antigas torres fortificadas e os antigos Portões da Cidade. Eu usei camadas de pontos, linhas e polígonos. Eu comparei estas camadas através da análise, pesquisa, geoprocessamento, geometria e ferramentas de gerenciamento de dados (Fig. 1).

<figure>
<img src="../images/italy_cesena1.png" style="width:100.0%" alt="italy_cesena1.png" />
<figcaption>Fig. 1 Concept Map of the QGIS project</figcaption>
</figure>

Usando estas ferramentas, eu coletei informações sobre:
- The precision of the Leonardo Da Vinci\'s topographic survey, realized in 1502, such as how many points of this survey are correct (Fig. 2);
- The Cesena Wall\'s Development from the Roman Age to the 15th Century;
- The Cesena Wall\'s Demolitions from the 19th Century to the Early 20th Century;
- As mudanças morfológicas do Muro da Cidade, além das demolições de suas antigas torres fortificadas e seus antigos Portões da Cidade;
- The Cesena\'s Urban Progress from the 16th Century to the Present;

<figure>
<img src="../images/italy_cesena2.png" style="width:100.0%" alt="italy_cesena2.png" />
<figcaption>Fig. 2: Openlayer Google Satellite overlapped by the informations recorded in different layers: the present City Wall in black, the Leonardo Da Vinci's topographic survey of the City Wall in orange, the Leonardo Da Vinci's points of survey in yellow and the present ancient City Gates in red.</figcaption>
</figure>

Existem inúmeras ferramentas QGIS, e eu usei algumas delas para criar:
- Links que conectavam cada seção da camada linear do atual Muro da Cidade às fotos, que representam o atual estado de conservação;
- Um mapa de Cesena no século 19 utilizando o compositor de impressão;
- Um modelo 3D de Cesena com o plugin qgis2threejs (Fig. 3);

<figure>
<img src="../images/italy_cesena3.png" style="width:100.0%" alt="italy_cesena3.png" />
<figcaption>Fig. 3: The 3D model of the present City Wall and Cesena's buildings inside and outside the Wall. The ancient fortified towers and the ancient City Gates are indicated.</figcaption>
</figure>

## Conclusão
Os mapas históricos são documentos importantes mesmo se sua precisão não possa ser comparada com a precisão de documentos cartográficos atuais, e eles são representações muito comunicativas também para aqueles que não são especialistas em representações geográficas. O QGIS foi o único meio que me permitiu utilizar o conteúdo numérico dos mapas históricos em conjunto com uma representação efetiva e significativa.
## Índice Bibliográfico
Os mapas históricos foram extraídos de:
- \"Costruzione, alterazione e recupero del centro storico di Cesena\", Ballardini, Cantori, Pezzi, Righetti, Tossani, Bruno Ghigi Editore, 1977
- \"La cinta muraria di Cesena\", Pino Montalti, Edizioni Panini, 1986

As informações históricas foram extraídas de:
- \"La cartografia in Italia: nuovi metodi e nuovi strumenti dal Settecento ad Oggi\", Andrea Cantile, IGM Firenze, 2007
- \"Lineamenti di storia della cartografia italiana, volume secondo, dal Seicento al Novecento\" Andrea Cantile, Geoweb, 2013
- \"I rilievi cartografici di Leonardo per Cesena ed Urbino contenuti nel manoscritto \'L\' dell\'Istituto di Francia\", Nando De Toni, G. Barbéra Editore, 1965
- \"La città da guerra\", Amelio Fara, Einaudi, 1993
- \"La cartografia dall\'antichità fino al XVIII secolo\", Carlo Monti, Maggioli Editore, 2011

## Autor
Camilla Fabbri has a bachelor\'s degree in Civil and Environmental Engineering. She has developed her dissertation on historical cartography of the Cesena Wall using the QGIS program with the Supervisor Alessandra Borghi, who is the University Teacher of Topography and Theoretical Mechanics of the bachelor\'s degree in Civil and Environmental Engineering in the eCampus University.

{{<content-end >}}
