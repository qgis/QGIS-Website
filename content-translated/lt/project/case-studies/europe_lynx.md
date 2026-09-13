---
HasBanner: false
archived: true
date: 2015-02-01
draft: false
featured: false
section: projektą
sidebar: true
thumbnail: images/europe_lynx1.png
title: Lūšių buveinių analizė Pietų Karpatuose
type: case-study

---
{{<content-start >}}
# Lūšių buveinių analizė Pietų Karpatuose
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>February 01, 2015</span>
</p>

Atvejo analizė, siekiant skatinti bendrą studentų supratimą apie laukinės gamtos buveinių modeliavimą naudojant atvirus duomenis.
## Įvadas
Challenged with the task of GIS based modeling for the first time, a working group of undergraduate forestry students of the University for Sustainable Development Eberswalde (HNEE) conducted literature research for habitat suitability and behavior of the Eurasian Lynx (*Lynx lynx*). In the module 'Applied GIS in Natural Resource Management', under the guidance of Prof. Mund, the students quickly discovered the subject's complexity, especially within regard to the adaptability of species to changing environments. With limited research published in English about lynx habitat on the Romanian side, we continued the project based on only freely available data sets and open-source software, aiming to establish conceptual knowledge of habitat modeling, strengthening skills on widely applied QGIS tools and to create a **basic expert model** in the process.
## Metodologija
Visi surinkti duomenys buvo apdoroti su QGIS 2.6 ir 2.8, projektuoti į ETRS89 / ETRS-LAEA ir saugomi pagal INSPIRE direktyvą atitinkant ES standartus. Buvo apibrėžtas **diskretus svorių indeksas**, kuris buvo pritaikytas visiems įvesties duomenims.

<figure>
<img src="../images/europe_lynx1.png" alt="europe_lynx1.png" />
<figcaption>Figure 1: Workflow - Lynx habitat expert model</figcaption>
</figure>

**Darbo eigos aprašymas**
- Area of Interest \[Step I -- II\]: Based on selected national park areas and adding a 10 kilometer buffer, a minimum bounding box \[α\] was created and clipped with the outline of the river Danube (derived from Corine Land Cover 2006). Further clipping tools \[β\] were applied to all additional data as an initial preparation step (Figure 2)
- Land Cover Suitability Model \[Step IX\]: \[γ\] Input III and IV were transformed into shape files using the inbuilt #Polygonize function. Corine Landcover (2006) data was reclassified using the field calculator to group land use classes and assign respective index values. Similar processing was applied to Hansen Forestcover data (2000), extracting only areas of cover equal or higher 75 %. Sub-model IX was produced by using the functions #Merge Shapes to combine III with IV and #Rasterize

*Pastaba: Žemės dangos klasės buvo grupuojamos pagal galimą lūšių pasirodymą ir žmogaus veiklą. Nors techniškai ir senesnės kilmės, miško dangos reikšmių informacija buvo integruota, kad rodytų buveinių judėjimą ir kaip bendras erdvinių duomenų aibių jungimo pavyzdys*
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
*Pastaba: Medžiotojų prieinamumo modelis turėtų indikuoti mažėjančią tikimybę, kad medžiotojai prieis prie vietos dėl didesnio atstumo iki kelių ir didėjančio nuolydžio*

<figure>
<img src="../images/europe_lynx2.png" alt="europe_lynx2.png" />
<figcaption>Figure 2, 3 and 4</figcaption>
</figure>

## Išvada
Žiūrint į galutinį rezultatą (Paveikslas 3), tikėtina pirma potenciali buveinė atrodo sėkminga, bet svarbiausia, pats bazinis modeliavimas pasirodė daug paprastesnis nei buvo tikėtasi. Mūsų pasirinkimas pridėti medžiotojų prieinamumo sub-modelį leido įgyvendinti kitą buveinės rizikos įvertinimo dimensiją, kuri gali būti paprastai įtraukta į jau esamą scenarijų ir naudojama apsaugos būtinybių nustatymui pagal tarkim infrastruktūros vystymo aspektus. Kaip bebūtų, kai kuri kritinė buveinės informacija, tokia kaip miško struktūra (mūsų aukščiausias buveinės tinkamumas) negali būti išvesta iš prieinamų duomenų rinkinių kartu su sudėtinga rūšių elgsena, todėl rezultatas turi būti suprantamas kaip bazinis ir negalutinis. Šiame etape neįgyvendinti papildomi faktoriai, tokie kaip mirtingumas keliuose, paviršiaus grubumas ir detalus grobio paplitimas.

Be to, kad QGIS programinė įranga yra atviro kodo, laisvai prieinama, paskutiniais metais ji buvo labai stipriai vystoma. Mums paliko labai teigiamą įspūdį įrankinės integracija, leidžianti net nepatyrusiems naudotojams naudoti įvairius GRASS ir SAGA įrankius. Nebuvo jokių suderinamumo problemų net keičiant versijas. Administracinių apribojimų nebuvimas gali būti didelis privalumas dirbant su duomenų rinkiniais intuityviai. Mes laukiame tolimesnių patobulinimų, ypač su integruotu modelio kūrėju.
## Šaltiniai
- Kaczensky, P., Chapron, G.,von Avrx, M., Huber, D., Andrén, H. & Linnell, J. (2012 Gruodis): Status, management and distribution of large carnivores in Europe. Document European Commission.
- Schadt, S., Revilla, E., Wiegand, T., Knauer, F., Kaczensky, P., Breitenmoser, U., Bufka, L., Cerveny, J., Koubek, P., Huber, T., Stanisa, C. & Trepl, L. (2002): Assessing the suitability of central European landscapes for the reintroduction of Eurasian lynx. Article Journal of Applied Ecology.
- Salvatori, V. (2004): Conservation areas for large carnivores in the Carpathian Mountains. PhD Thesis.
- Podgórski, T., Schmidt, K., Kowalczyk, R. & Gulczyñska, A. (2008): Microhabitat selection by Eurasian lynx and its implications for species conservation. Acta Theriologica 53: 97--110.
- Boutros, D. (March 2002): Characterization and assessment of suitability of Eurasian lynx (Lynx lynx) den sites. KORA Report No. 12e, Diploma thesis.

### Autoriai
Angela Dichte, Luca Ehrminger, Silvana Garcia Travesi Reyes, Tobias Hoppe and David Winger are fourth semester students of the study program International Forest Ecosystem Management B.Sc., Anne Gnilke respectively German Forestry and Henri Hiltunen is an exchange student from Mikkeli University of Applied Sciences, Finland. Prof. Mund is lecturing GIS and Remote Sensing at HNE Eberswalde since 2010 and provided guidance and technical support to the project.

Jei norite daugiau informacijos, prašome susisiekti su Luca.Ehrminger(at)hnee.de, David.Winger(at)hnee.de, or Prof.Dr.Jan-Peter Mund: Jan-Peter.Mund(at)hnee.de.

{{<content-end >}}
