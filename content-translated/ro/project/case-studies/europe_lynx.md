---
HasBanner: false
archived: true
date: 2015-02-01
draft: false
featured: false
section: proiect
sidebar: true
thumbnail: images/europe_lynx1.png
title: Analiza habitatului pentru Lynxul din Carpații Meridionali
type: case-study

---
{{<content-start >}}
# Analiza habitatului pentru Lynxul din Carpații Meridionali
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>February 01, 2015</span>
</p>

Un studiu de caz pentru studenți, cu scopul de a promova înțelegerea de bază a modelării habitatului pentru fauna sălbatică, cu ajutorul surselor de date deschise.
## Introducere
Challenged with the task of GIS based modeling for the first time, a working group of undergraduate forestry students of the University for Sustainable Development Eberswalde (HNEE) conducted literature research for habitat suitability and behavior of the Eurasian Lynx (*Lynx lynx*). In the module 'Applied GIS in Natural Resource Management', under the guidance of Prof. Mund, the students quickly discovered the subject's complexity, especially within regard to the adaptability of species to changing environments. With limited research published in English about lynx habitat on the Romanian side, we continued the project based on only freely available data sets and open-source software, aiming to establish conceptual knowledge of habitat modeling, strengthening skills on widely applied QGIS tools and to create a **basic expert model** in the process.
## Metodologia
Toate datele colectate au fost prelucrate cu aplicațiile QGIS 2.6 și 2.8, proiectate în ETRS89 / ETRS-LAEA și depozitate în conformitate cu Directiva INSPIRE, pentru a îndeplini standardele UE. A fost definit și aplicat tuturor datelor de intrare un **indice discret al ponderilor**.

<figure>
<img src="../images/europe_lynx1.png" alt="europe_lynx1.png" />
<figcaption>Figure 1: Workflow - Lynx habitat expert model</figcaption>
</figure>

**Descrierea fluxului de lucru**
- Area of Interest \[Step I -- II\]: Based on selected national park areas and adding a 10 kilometer buffer, a minimum bounding box \[α\] was created and clipped with the outline of the river Danube (derived from Corine Land Cover 2006). Further clipping tools \[β\] were applied to all additional data as an initial preparation step (Figure 2)
- Land Cover Suitability Model \[Step IX\]: \[γ\] Input III and IV were transformed into shape files using the inbuilt #Polygonize function. Corine Landcover (2006) data was reclassified using the field calculator to group land use classes and assign respective index values. Similar processing was applied to Hansen Forestcover data (2000), extracting only areas of cover equal or higher 75 %. Sub-model IX was produced by using the functions #Merge Shapes to combine III with IV and #Rasterize

*Notă: Clase de acoperire a terenurilor au fost grupate în funcție de posibila prezență a lynxului și de activitatea umană. Deși vechi din punct de vedere tehnic,  informațiile referitoare la valorile suprafețelor împădurite au fost integrate, în ideea de a indica îmbunătățirea habitatelor, și ca un exemplu general de îmbinare a seturilor de date spațiale*
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
*Notă: Modelul de Accesibilitate al Prădătorului Potențial indică probabilitatea, în scădere, ca prădătorii să acceseze zona îndepărtate de drumuri și pantele mari*

<figure>
<img src="../images/europe_lynx2.png" alt="europe_lynx2.png" />
<figcaption>Figure 2, 3 and 4</figcaption>
</figure>

## Concluzii
Privind la rezultatul final (figura 3), o primă analiză a habitatului potențial plauzibil pare să se fi desfășurat cu succes, dar mai important, modelarea de bază s-a dovedit a fi mai puțin dificilă decât se aștepta inițial. Alegerea noastră, de a adăuga un sub-model de accesibilitate a prădătorului ne-a permis să implementăm o altă dimensiune în termeni de evaluare a riscului de habitat, care poate fi pur și simplu imbricată în scenariul deja existent și folosită pentru a determina necesitățile de protecție în conformitate cu, de exemplu, aspectele de dezvoltare a infrastructurii. Cu toate acestea, unele informații cruciale despre habitat, cum ar fi structura pădurii (habitatul cel mai adecvat), nu pot fi derivate din seturile de date disponibile, și prin urmare, ținând cont de comportamentul complex al speciilor, trebuie să înțelegem că rezultatul este orientativ și incomplet. Alți factori neimplementați în această etapă sunt mortalitatea rutieră, rugozitatea terenului și detaliile despre prezența prăzii.

În afară de sursa deschisă și de disponibilitatea sa gratuită, aplicația QGIS a fost subiectul unor evoluții importante în ultimii ani. Am avut experiențe foarte pozitive la integrarea trusei de instrumente, care permite utilizarea diverselor funcțiuni din GRASS și SAGA, chiar și de către utilizatorii neexperimentați. Nu au apărut probleme de compatibilitate. în ciuda schimbării frecvente a diverselor versiuni, iar absența generală a restricțiilor administrative constituie un avantaj puternic, atunci când se lucrează în mod intuitiv cu seturile de date. Așteptăm cu nerăbdare să vedem îmbunătățiri suplimentare, în special în ceea ce privește constructorul de modele integrat.
## Referințe
- Kaczensky, P., Chapron, G.,von Avrx, M., Huber, D., Andrén, H. & Linnell, J. (Decembrie 2012): Starea, gestionarea și distribuția carnivorelor mari din Europa. Document al Comisiei Europene.
- Schadt, S., Revilla, E., Wiegand, T., Knauer, F., Kaczensky, P., Breitenmoser, U., Bufka, L., Cerveny, J., Koubek, P., Huber, T., Stanisa, C. & Trepl, L. (2002): Evaluarea caracterului adecvat al peisajelor din Europa Centrală, pentru reintroducerea Lynxului eurasiatic. Articolul din Jurnalul de Ecologie Aplicată.
- Salvatori, V. (2004): Zone de conservare pentru carnivorele mari din Munții Carpați. Teză de doctorat.
- Podgórski, T., Schmidt, K., Kowalczyk, R. & Gulczyñska, A. (2008): Microhabitat selection by Eurasian lynx and its implications for species conservation. Acta Theriologica 53: 97--110.
- Boutros, D. (Martie 2002): Caracterizarea și evaluarea adecvării râsului eurasiatic (Lynx lynx). KORA Raport nr 12e, Lucrare de diplomă.

### Autori
Angela Dichte, Luca Ehrminger, Silvana Garcia Travesi Reyes, Tobias Hoppe și David Winger sunt studenți în semestrul al patrulea la programul de Management International al Ecosistemelor Silvice, Anne Gnilke este la Silvicultură Germană iar Henri Hiltunen este student la Universitatea de Științe Aplicate Mikkeli din Finlanda. Prof. Mund predă din 2010 cursuri de GIS și Teledetecție la HNE Eberswalde, și a oferit îndrumare și sprijin tehnic acestui proiect.

Contactați-i pe Luca.Ehrminger(at)hnee.de, David.Winger(at)hnee.de sau Prof.Dr.Jan-Peter Mund: Jan-Peter.Mund(at)hnee.de pentru informații suplimentare.

{{<content-end >}}
