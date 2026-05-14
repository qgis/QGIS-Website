---
HasBanner: false
archived: true
date: 2015-02-01
draft: false
featured: false
section: progetto
sidebar: true
thumbnail: images/europe_lynx1.png
title: Analisi dell'habitat della lince nei Carpazi meridionali
type: case-study

---
{{<content-start >}}
# Analisi dell'habitat della lince nei Carpazi meridionali
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>February 01, 2015</span>
</p>

Un caso di studio per promuovere la comprensione di base della modellazione dell'habitat della fauna selvatica per gli studenti sulla base di dati open source.
## Introduzione
Challenged with the task of GIS based modeling for the first time, a working group of undergraduate forestry students of the University for Sustainable Development Eberswalde (HNEE) conducted literature research for habitat suitability and behavior of the Eurasian Lynx (*Lynx lynx*). In the module 'Applied GIS in Natural Resource Management', under the guidance of Prof. Mund, the students quickly discovered the subject's complexity, especially within regard to the adaptability of species to changing environments. With limited research published in English about lynx habitat on the Romanian side, we continued the project based on only freely available data sets and open-source software, aiming to establish conceptual knowledge of habitat modeling, strengthening skills on widely applied QGIS tools and to create a **basic expert model** in the process.
## Metodologia
Tutti i dati raccolti sono stati elaborati con QGIS 2.6 e 2.8, proiettati in ETRS89 / ETRS-LAEA e memorizzati secondo la direttiva INSPIRE per soddisfare gli standard UE. È stato definito e applicato a tutti i dati di input un **indice discreto dei pesi** globale.

<figure>
<img src="../images/europe_lynx1.png" alt="europe_lynx1.png" />
<figcaption>Figure 1: Workflow - Lynx habitat expert model</figcaption>
</figure>

**Descrizione del flusso di lavoro**
- Area of Interest \[Step I -- II\]: Based on selected national park areas and adding a 10 kilometer buffer, a minimum bounding box \[α\] was created and clipped with the outline of the river Danube (derived from Corine Land Cover 2006). Further clipping tools \[β\] were applied to all additional data as an initial preparation step (Figure 2)
- Land Cover Suitability Model \[Step IX\]: \[γ\] Input III and IV were transformed into shape files using the inbuilt #Polygonize function. Corine Landcover (2006) data was reclassified using the field calculator to group land use classes and assign respective index values. Similar processing was applied to Hansen Forestcover data (2000), extracting only areas of cover equal or higher 75 %. Sub-model IX was produced by using the functions #Merge Shapes to combine III with IV and #Rasterize

*Nota: le classi di copertura del suolo sono state raggruppate per possibile presenza di lince e attività umana. Sebbene tecnicamente di origine più antica, le informazioni relative ai valori di copertura forestale sono state integrate per indicare il miglioramento degli habitat e come esempio generale di aggregazione di set di dati spaziali*.
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
*Nota: il modello di accessibilità per i cacciatori indica la diminuzione della probabilità che i cacciatori accedano all'area a maggiore distanza dalle strade e pendenza crescente*.

<figure>
<img src="../images/europe_lynx2.png" alt="europe_lynx2.png" />
<figcaption>Figure 2, 3 and 4</figcaption>
</figure>

## Conclusione
Guardando al risultato finale (Figura 3), una prima analisi del potenziale habitat è sembrata avere successo, ma, cosa ancora più importante, la stessa modellazione di base si è rivelata meno difficile di quanto inizialmente previsto. La nostra scelta di aggiungere un sottomodello per l'accessibilità per i cacciatori ci ha permesso di implementare un'altra dimensione in termini di valutazione del rischio dell'habitat, che può essere semplicemente annidata nello scenario già esistente e utilizzata per determinare le necessità di protezione sotto aspetti, ad esempio, dello sviluppo delle infrastrutture. Tuttavia, alcune informazioni cruciali sugli habitat, come la struttura forestale (la nostra massima idoneità dell'habitat) non possono essere ricavate dai dati disponibili e, in combinazione con il complesso comportamento delle specie, il risultato deve quindi essere inteso come base e incompleto. Ulteriori fattori non implementati in questa fase sono la mortalità stradale, la rugosità del terreno e la presenza di prede dettagliata.

Oltre al suo carattere open source e disponibile gratuitamente, il software QGIS è stato oggetto di importanti sviluppi negli ultimi anni. Abbiamo fatto un'esperienza molto positiva con l'integrazione del tool box, permettendo l'utilizzo di vari strumenti GRASS e SAGA, anche per utenti inesperti. Non si sono verificati problemi di compatibilità nonostante i frequenti cambiamenti tra le diverse versioni, e la generale assenza di restrizioni amministrative può essere un potente vantaggio quando si lavora intuitivamente con i set di dati. Siamo ansiosi di vedere ulteriori miglioramenti, soprattutto per quanto riguarda il model builder integrato.
## Riferimenti
- Kaczensky, P., Chapron, G.,von Avrx, M., Huber, D., Andrén, H. & Linnell, J. (December 2012): Status, management and distribution of large carnivores in Europe. Document European Commission.
- Schadt, S., Revilla, E., Wiegand, T., Knauer, F., Kaczensky, P., Breitenmoser, U., Bufka, L., Cerveny, J., Koubek, P., Huber, T., Stanisa, C. & Trepl, L. (2002): Assessing the suitability of central European landscapes for the reintroduction of Eurasian lynx. Article Journal of Applied Ecology.
- Salvatori, V. (2004): Conservation areas for large carnivores in the Carpathian Mountains. PhD Thesis.
- Podgórski, T., Schmidt, K., Kowalczyk, R. & Gulczyñska, A. (2008): Microhabitat selection by Eurasian lynx and its implications for species conservation. Acta Theriologica 53: 97--110.
- Boutros, D. (March 2002): Characterization and assessment of suitability of Eurasian lynx (Lynx lynx) den sites. KORA Report No. 12e, Diploma thesis.

### Autori
Angela Dichte, Luca Ehrminger, Silvana Garcia Travesi Reyes, Tobias Hoppe e David Winger sono studenti del quarto semestre del programma di studio International Forest Ecosystem Management B.Sc., Anne Gnilke e Henri Hiltunen è uno studente di scambio della Mikkeli University of Applied Sciences, Finlandia. Il Prof. Mund è docente di GIS e telerilevamento presso la HNE Eberswalde dal 2010 e ha fornito guida e supporto tecnico al progetto.

Contatta Luca.Ehrminger(at)hnee.de, David.Winger(at)hnee.de, o il Prof.Dr.Jan-Peter Mund: Jan-Peter.Mund(at)hnee.de per ulteriori informazioni.

{{<content-end >}}
