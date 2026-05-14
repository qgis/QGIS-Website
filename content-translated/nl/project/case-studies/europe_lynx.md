---
HasBanner: false
archived: true
date: 2015-02-01
draft: false
featured: false
section: project
sidebar: true
thumbnail: images/europe_lynx1.png
title: Analyse voor woonomgeving van Lynx in de zuidelijke Karpaten
type: case-study

---
{{<content-start >}}
# Analyse voor woonomgeving van Lynx in de zuidelijke Karpaten
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>February 01, 2015</span>
</p>

Een praktijkvoorbeeld om het basisbegrip te promoten voor het modelleren van woonomgevingen voor wilde dieren, voor studenten, gebaseerd op gegevens van open source.
## Introductie
Challenged with the task of GIS based modeling for the first time, a working group of undergraduate forestry students of the University for Sustainable Development Eberswalde (HNEE) conducted literature research for habitat suitability and behavior of the Eurasian Lynx (*Lynx lynx*). In the module 'Applied GIS in Natural Resource Management', under the guidance of Prof. Mund, the students quickly discovered the subject's complexity, especially within regard to the adaptability of species to changing environments. With limited research published in English about lynx habitat on the Romanian side, we continued the project based on only freely available data sets and open-source software, aiming to establish conceptual knowledge of habitat modeling, strengthening skills on widely applied QGIS tools and to create a **basic expert model** in the process.
## Methodologie
Alle verzamelde gegevens werden verwerkt met QGIS 2.6 en 2.8, geprojecteerd in ETRS89 / ETRS-LAEA en opgeslagen conform de richtlijn van INSPIRE om te voldoen aan de standaarden van de EU. Een overall **discrete index of weights** werd gedefinieerd en toegepast op alle ingevoerde gegevens.

<figure>
<img src="../images/europe_lynx1.png" alt="europe_lynx1.png" />
<figcaption>Figure 1: Workflow - Lynx habitat expert model</figcaption>
</figure>

**Beschrijving werkstroom**
- Area of Interest \[Step I -- II\]: Based on selected national park areas and adding a 10 kilometer buffer, a minimum bounding box \[α\] was created and clipped with the outline of the river Danube (derived from Corine Land Cover 2006). Further clipping tools \[β\] were applied to all additional data as an initial preparation step (Figure 2)
- Land Cover Suitability Model \[Step IX\]: \[γ\] Input III and IV were transformed into shape files using the inbuilt #Polygonize function. Corine Landcover (2006) data was reclassified using the field calculator to group land use classes and assign respective index values. Similar processing was applied to Hansen Forestcover data (2000), extracting only areas of cover equal or higher 75 %. Sub-model IX was produced by using the functions #Merge Shapes to combine III with IV and #Rasterize

*Opmerking: Klassen van landbedekking werden gegroepeerd op mogelijk voorkomen van de lynx en menselijke activiteiten. Hoewel technisch van oudere herkomst, werd informatie, gerelateerd om waarden van bosbedekking, geïntegreerd om de verbetering in de habitat aan te kunnen geven en als een algemeen voorbeeld voor het samenvoegen van ruimtelijke gegevenssets*
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
*Opmerking: De Hunter Accessibility Model zal de afnemende waarschijnlijkheid aangeven dat jagers het gebied betreden bij toenemende afstand tot wegen en steilere hellingen*

<figure>
<img src="../images/europe_lynx2.png" alt="europe_lynx2.png" />
<figcaption>Figure 2, 3 and 4</figcaption>
</figure>

## Conclusie
Kijkend naar de uiteindelijke uitvoer (Afbeelding 3),leek een eerste potentiële analyse van de habitat succesvol te zijn, maar meer belangrijk, het basis modelleren zelf bleek achteraf minder moeilijk dan initieel werd ver3wacht. Onze keuze om een sub-model voor toegankelijkheid voor jagers toe te voegen stelde ons in staat een andere dimensie te implementeren in termen van beoordeling van risico's voor de habitat, die eenvoudig kan worden genest binnen het reeds bestaande scenario en kan worden gebruikt om benodigde beschermingsmaatregelen te bepalen onder aspecten van bijv. infrastructurele ontwikkeling. Echter, enige cruciale informatie over de habitat, zoals bosstructuur (onze hoogste geschiktheid voor de habitat) kan niet worden afgeleid uit beschikbare gegevenssets en in combinatie met het complexe gedrag van de soort, moet het resultaat daarom worden begrepen als basis en niet volledig. Op dit moment nog niet geïmplementeerde aanvullende factoren zijn sterftecijfers op wegen, ruwheid van het terrein en gedetailleerd voorkomen van prooi.

Naast de open source, gratis beschikbare tekens, is QGIS software onderwerp geweest van belangrijke ontwikkelingen in de afgelopen jaren. We hebben een erg positieve ervaring gehad met de integratie van de Toolbox, wat het ons mogelijk maakte gebruik te maken van de verscheidene gereedschappen van GRASS en SAGA, zelfs voor onervaren gebruikers. Er traden geen compatibilteitsproblemen op ondanks het frequent gebruiken van de verschillende versies en de algemene afwezigheid van administratieve beperkingen kan een krachtig voordeel zijn bij het intuïtief werken met gegevenssets. Wij zien uit naar verdere verbeteringen, speciaal met betrekking tot de geïntegreerde modelbouwer.
## Verwijzingen
- Kaczensky, P., Chapron, G.,von Avrx, M., Huber, D., Andrén, H. & Linnell, J. (December 2012): Status, management and distribution of large carnivores in Europe. Document Europese Commissie.
- Schadt, S., Revilla, E., Wiegand, T., Knauer, F., Kaczensky, P., Breitenmoser, U., Bufka, L., Cerveny, J., Koubek, P., Huber, T., Stanisa, C. & Trepl, L. (2002): Assessing the suitability of central European landscapes for the reintroduction of Eurasian lynx. Article Journal of Applied Ecology.
- Salvatori, V. (2004): Conservation areas for large carnivores in the Carpathian Mountains. PhD Thesis.
- Podgórski, T., Schmidt, K., Kowalczyk, R. & Gulczyñska, A. (2008): Microhabitat selection by Eurasian lynx and its implications for species conservation. Acta Theriologica 53: 97--110.
- Boutros, D. (March 2002): Characterization and assessment of suitability of Eurasian lynx (Lynx lynx) den sites. KORA Report No. 12e, Diploma thesis.

### Auteurs
Angela Dichte, Luca Ehrminger, Silvana Garcia Travesi Reyes, Tobias Hoppe en David Winger zijn studenten in het vierde semester van het studieprogramma International Forest Ecosystem Management B.Sc., Anne Gnilke respectievelijk German Forestry en Henri Hiltunen is een uitwisselingsstudent van de Mikkeli University of Applied Sciences, Finland. Prof. Mund is lector in GIS en Remote Sensing aan de HNE Eberswalde sinds 2010 en verschafte begeleiding en technische ondersteuning aan het project.

Neem, voor meer informatie, contact op met Luca.Ehrminger(at)hnee.de, David.Winger(at)hnee.de, of Prof.Dr.Jan-Peter Mund: Jan-Peter.Mund(at)hnee.de.

{{<content-end >}}
