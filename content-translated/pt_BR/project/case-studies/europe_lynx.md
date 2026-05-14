---
HasBanner: false
archived: true
date: 2015-02-01
draft: false
featured: false
section: projeto
sidebar: true
thumbnail: images/europe_lynx1.png
title: Análise de habitat do lince nos Cárpatos do Sul
type: case-study

---
{{<content-start >}}
# Análise de habitat do lince nos Cárpatos do Sul
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>February 01, 2015</span>
</p>

Um estudo de caso para promover a compreensão básica da modelagem de habitat de animais selvagens para estudantes com base em dados abertos.
## Introdução
Challenged with the task of GIS based modeling for the first time, a working group of undergraduate forestry students of the University for Sustainable Development Eberswalde (HNEE) conducted literature research for habitat suitability and behavior of the Eurasian Lynx (*Lynx lynx*). In the module 'Applied GIS in Natural Resource Management', under the guidance of Prof. Mund, the students quickly discovered the subject's complexity, especially within regard to the adaptability of species to changing environments. With limited research published in English about lynx habitat on the Romanian side, we continued the project based on only freely available data sets and open-source software, aiming to establish conceptual knowledge of habitat modeling, strengthening skills on widely applied QGIS tools and to create a **basic expert model** in the process.
## Metodologia
Todos os dados coletados foram processados no QGIS 2.6 e 2.8, projetados em ETRS89 / ETRS-LAEA e armazenados de acordo com as diretivas do INSPIRE para atender aos padrões da UE. E no geral foi definido um **índice discreto de pesos** que foi aplicado a todos os dados de entrada.

<figure>
<img src="../images/europe_lynx1.png" alt="europe_lynx1.png" />
<figcaption>Figure 1: Workflow - Lynx habitat expert model</figcaption>
</figure>

**Descrição do fluxo de trabalho**
- Area of Interest \[Step I -- II\]: Based on selected national park areas and adding a 10 kilometer buffer, a minimum bounding box \[α\] was created and clipped with the outline of the river Danube (derived from Corine Land Cover 2006). Further clipping tools \[β\] were applied to all additional data as an initial preparation step (Figure 2)
- Land Cover Suitability Model \[Step IX\]: \[γ\] Input III and IV were transformed into shape files using the inbuilt #Polygonize function. Corine Landcover (2006) data was reclassified using the field calculator to group land use classes and assign respective index values. Similar processing was applied to Hansen Forestcover data (2000), extracting only areas of cover equal or higher 75 %. Sub-model IX was produced by using the functions #Merge Shapes to combine III with IV and #Rasterize

*Nota: as classes de cobertura do solo foram agrupadas pela possível ocorrência de lince e atividades humanas. Embora tecnicamente de origem antiga, a informação relacionada aos valores de cobertura florestal foram integradas na ordem de indicar a melhoria do habitat e formar um exemplo de junção de um conjunto de dados espaciais*
- Habitat Suitability Model \[Step X\]: \[δ\] An Elevation Suitability Index was derived from the AsterDEM 2.0 \[VI\] and together with a Population Density Index \[V\] was integrated into the final habitat suitability model (Figure 3) by using the #Raster calculator

```
    Cover Suitability Model * Population Density Index * Elevation Suitability Index
```
*Note:Defining forest (\>= 75 % cover) as best suitable and using the elevation data to reduce index values above assumed tree line is conceptually related to habitat of deer as the main prey*
- Potential Hunter Accessibility Model \[Step XI\]: Applying the #Terrain analysis tool \[ε\], a slope layer was extracted from the DEM data and combined \[η\] with a road distance layer, which was produced by processing rasterized OSM road data within the #Proximity function and index values assigned using #Reclassify grid values

```
                          Slopelayer
    Road distance * ( 1 + ----------- )
                             100
```
- Conservation Value Model \[Step XII\]: Is the result of the #Raster calculator function: (Figure 4)

```
    (Habitat Suitability Model * Hunter Accessibility Model)
    --------------------------------------------------------
                           2
```
*Nota: O Modelo de Acessibilidade Hunter deve indicar a diminuição da probabilidade dos hunters acessarem a área pela maior distância das estradas e aumento da declividade.

<figure>
<img src="../images/europe_lynx2.png" alt="europe_lynx2.png" />
<figcaption>Figure 2, 3 and 4</figcaption>
</figure>

## Conclusão
Com o resultado final (Figura 3), a primeira análise plausível do habitat potencial parece ser bem sucedida. Ainda mais importante, a modelagem básica em si se mostrou menos difícil do que inicialmente esperado. Nossa escolha de adicionar um submodelo de acessibilidade hunter nos permitiu implementar outra dimensão em termos da avaliação de riscos do habitat, na qual pode ser simplesmente aninhada no cenário existente e usada para determinar necessidades de proteção de aspectos, por exemplo, no desenvolvimento da infraestrutura. No entanto, algumas informações cruciais sobre o habitat, tais como estrutura da floresta (nossa mais alta adequação ao habitat), não podem ser derivadas de um conjunto de dados disponíveis e nem na combinação de comportamentos de espécies complexas, em que o resultado deve ser entendido como básico ou incompleto. Fatores adicionais não implementados nesse estágio são de mortalidade nas rodovias, sobre a rugosidade do terreno e ocorrência de detalhadas presas.

Além de ser código aberto, livre de caracteres disponíveis, o QGIS têm sido objeto de grande desenvolvimento nos últimos anos. Nós fizemos uma experiência positiva com a integração da caixa de ferramentas, permitindo o uso de variadas ferramentas do GRASS e SAGA GIS, mesmo para usuários inexperientes. Nenhum problema de compatibilidade ocorreu, apesar de frequentes alterações entre diferentes versões e ausência geral de restrições administrativas, no que pode ser uma grande vantagem quando trabalhando intuitivamente com conjuntos de dados. Nós estamos ansiosos para ver melhorias adicionais, especialmente na construção de um modelo integrado.
## Referências
- Kaczensky, P., Chapron, G.,von Avrx, M., Huber, D., Andrén, H. & Linnell, J. (December 2012): Status, management and distribution of large carnivores in Europe. Document European Commission.
- Schadt, S., Revilla, E., Wiegand, T., Knauer, F., Kaczensky, P., Breitenmoser, U., Bufka, L., Cerveny, J., Koubek, P., Huber, T., Stanisa, C. & Trepl, L. (2002): Assessing the suitability of central European landscapes for the reintroduction of Eurasian lynx. Article Journal of Applied Ecology.
- Salvatori, V. (2004): Conservation areas for large carnivores in the Carpathian Mountains. PhD Thesis.
- Podgórski, T., Schmidt, K., Kowalczyk, R. & Gulczyñska, A. (2008): Microhabitat selection by Eurasian lynx and its implications for species conservation. Acta Theriologica 53: 97--110.
- Boutros, D. (March 2002): Characterization and assessment of suitability of Eurasian lynx (Lynx lynx) den sites. KORA Report No. 12e, Diploma thesis.

### Autores
Angela Dichte, Luca Ehrminger, Silvana Garcia Travesi Reyes, Tobias Hoppe e David Winger são estudantes do 4º semestre do Programa de Estudos de Gestão de Florestas e Ecosistemas Internacionais; respectivamente, Anne Gnilke é silvicultor alemão e Henri Hiltunen é estudante de intercâmbio da Universidade de Mikkeli de Ciências Aplicadas, Finlândia. O prof. Mund está dando palestras de SIG e Sensoriamento Remoto na HNE Eberswalde desde 2010 e fornece guias e suporte técnico ao projeto. 

Por favor, entre em contato com Luca.Ehrminger(at)hnee.de, David.Winger(at)hnee.de, ou Prof.Dr.Jan-Peter Mund: Jan-Peter.Mund(at)hnee.de para mais informações.

{{<content-end >}}
