---
HasBanner: false
archived: true
date: 2015-10-30
draft: false
featured: false
section: projeto
sidebar: true
thumbnail: images/italy_cesena1.png
title: Utilização do QGIS na Caracterização da Muralha de Cesena
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

A eCAMPUS UNIVERSITY foi constituída como universidade de ensino à distância e reconhecida pelo Ministério Italiano da Educação, Universidade e Investigação (MIUR) através de Decreto Ministerial de 30 de Janeiro de 2006. Foi criada com o propósito de facilitar a jovens, profissionais, empreendedores, executivos e agentes comerciais ou culturais, o acesso à universidade através de uma plataforma e-learning. A sede, também conhecida por Campus Internacional de Milão ou Campus de Novedrate, localiza-se nas instalações do antigo centro de formação da IBM em Novedrate (Como, Itália), na verdejante e tranquila região da Brianza.

A Universidade possui 5 faculdades virtuais: Engenharia, Economia, Psicologia, Artes e Direito.
A associação de MAPAS HISTÓRICOS com recurso ao PROJETO QGIS permitiu caracterizar a emblemática muralha da cidade de Cesena [25Km a noroeste de San Marino], cuja forma, semelhante à de um escorpião, separa o centro histórico da zona de construção mais recente.

A evolução e sucessivas destruições desta muralha estão descritas em documentos cartográficos antigos. O software QGIS permite comparar diferentes mapas históricos ao reprojetá-los para um Sistema de Referência comum através do módulo Georeferencer [GDAL]. Para esse efeito, o Sistema de Referência escolhido foi o EPSG: 3857 (WGS 84 Web Mercator ou WGS84/Pseudo Mercator), também utilizado pelas camadas raster Google Satellite e OpenStreetMap.

O QGIS foi uma ferramenta fundamental na elaboração, análise, georreferenciação e comparação destes mapas [raster]. Na vetorização (formato shapefile) de elementos tais como estradas, edifícios, parques e jardins, muralha, antigas portas e torres fortificadas, foram utilizadas camadas do tipo ponto, linha e polígono. O recurso às ferramentas de análise, pesquisa, geoprocessamento e gestão de dados permitiu a comparação daquelas camadas (Fig. 1). 

<figure>
<img src="../images/italy_cesena1.png" style="width:100.0%" alt="italy_cesena1.png" />
<figcaption>Fig. 1 Concept Map of the QGIS project</figcaption>
</figure>

A utilização destas ferramentas permitiu obter informações sobre:
- The precision of the Leonardo Da Vinci\'s topographic survey, realized in 1502, such as how many points of this survey are correct (Fig. 2);
- The Cesena Wall\'s Development from the Roman Age to the 15th Century;
- The Cesena Wall\'s Demolitions from the 19th Century to the Early 20th Century;
- Alterações ao traçado da Muralha, tais como demolições das suas antigas portas e torres fortificadas;
- The Cesena\'s Urban Progress from the 16th Century to the Present;

<figure>
<img src="../images/italy_cesena2.png" style="width:100.0%" alt="italy_cesena2.png" />
<figcaption>Fig. 2: Openlayer Google Satellite overlapped by the informations recorded in different layers: the present City Wall in black, the Leonardo Da Vinci's topographic survey of the City Wall in orange, the Leonardo Da Vinci's points of survey in yellow and the present ancient City Gates in red.</figcaption>
</figure>

As várias ferramentas disponibilizadas pelo QGIS foram utilizadas na criação de:
- Associação entre cada troço (entidade linear vetorial) da camada que representa a atual muralha e respetiva fotografia ilustrativa do seu estado de conservação. 
- Planta da Cesena do séc. XIX, formatada com recurso ao Compositor de Impressão;
- Modelo Tridimensional (3D) de Cesena com o módulo qgis2threejs (Figura 3);

<figure>
<img src="../images/italy_cesena3.png" style="width:100.0%" alt="italy_cesena3.png" />
<figcaption>Fig. 3: The 3D model of the present City Wall and Cesena's buildings inside and outside the Wall. The ancient fortified towers and the ancient City Gates are indicated.</figcaption>
</figure>

## Conclusões
Os mapas históricos são documentos importantes mesmo que a sua precisão não se possa comparar à da cartografia contemporânea. A sua apresentação é bastante apelativa até para quem não é especialista em representações geográficas. O QGIS foi a única ferramenta a permitir ao autor criar uma representação digital significativa da cartografia histórica em apreço. 
## Bibliografia
A cartografia histórica foi obtida em:
- \"Costruzione, alterazione e recupero del centro storico di Cesena\", Ballardini, Cantori, Pezzi, Righetti, Tossani, Bruno Ghigi Editore, 1977
- \"La cinta muraria di Cesena\", Pino Montalti, Edizioni Panini, 1986

Outra informação histórica:
- \"La cartografia in Italia: nuovi metodi e nuovi strumenti dal Settecento ad Oggi\", Andrea Cantile, IGM Firenze, 2007
- \"Lineamenti di storia della cartografia italiana, volume secondo, dal Seicento al Novecento\" Andrea Cantile, Geoweb, 2013
- \"I rilievi cartografici di Leonardo per Cesena ed Urbino contenuti nel manoscritto \'L\' dell\'Istituto di Francia\", Nando De Toni, G. Barbéra Editore, 1965
- \"La città da guerra\", Amelio Fara, Einaudi, 1993
- \"La cartografia dall\'antichità fino al XVIII secolo\", Carlo Monti, Maggioli Editore, 2011

## Sobre o autor:
Camilla Fabbri has a bachelor\'s degree in Civil and Environmental Engineering. She has developed her dissertation on historical cartography of the Cesena Wall using the QGIS program with the Supervisor Alessandra Borghi, who is the University Teacher of Topography and Theoretical Mechanics of the bachelor\'s degree in Civil and Environmental Engineering in the eCampus University.

{{<content-end >}}
