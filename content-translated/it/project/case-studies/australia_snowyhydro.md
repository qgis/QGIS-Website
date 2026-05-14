---
HasBanner: false
archived: true
date: 2014-08-01
draft: false
featured: false
section: progetto
sidebar: true
thumbnail: images/australia_snowyhydro1.jpg
title: Utilizzo della processing toolbox per automatizzare la classificazione della
  neve
type: case-study

---
{{<content-start >}}
# Utilizzo della processing toolbox per automatizzare la classificazione della neve
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>August 01, 2014</span>
</p>

Snowy Hydro Limited (SHL) è un generatore di energia elettrica di picco con sede nelle Snowy Mountains del New South Wales, Australia. Nonostante possieda una varietà di impianti di generazione in tutto il paese, Snowy Hydro Limited è conosciuta soprattutto per la custodia di un pezzo iconico dell'infrastruttura australiana, lo Snowy Mountains Hydro Electric Scheme.

Lo Snowy Mountains Hydro Electric Scheme, è reso possibile dalle nevicate stagionali nella regione alpina del New South Wales. L'acqua proveniente dallo scioglimento delle nevi primaverili viene utilizzata per generare elettricità per far fronte ai picchi di domanda nel mercato elettrico nazionale, deviando nel contempo l'acqua verso le aree interne più asciutte del Sud Est australiano per l'irrigazione e l'agricoltura.

La classificazione della copertura nevosa nei mesi invernali consente a SHL di monitorare il ciclo dell'area innevata, di archiviare le aree di copertura per i dati storici e di fornire statistiche di copertura al team dei servizi idrografici per le previsioni sulla resa idrica e di stoccaggio.

<figure>
<img src="../images/australia_snowyhydro1.jpg" class="align-center" height="43400" alt="images/australia_snowyhydro1.jpg" />
<figcaption>Map 1.1 Snowy Water Catchment Map</figcaption>
</figure>

## Sfondo
Ogni anno durante i mesi invernali (dal 1° giugno al 31 ottobre) la SHL ottiene dal satellite MODIS Terra (EOS AM) il maggior numero possibile di immagini senza nuvole. Queste immagini vengono poi inserite in un algoritmo noto come Normalised Difference Snow Index (NDSI), che viene utilizzato per indicare le aree in cui è presente la neve. Anche se questo algoritmo non è univoco per un particolare sensore, lo strumento MODIS è stato scelto per la sua adeguata risoluzione spaziale e la copertura giornaliera dell'area di progetto (Mappa 1.1 Bacino nevoso).
## Obiettivo
L'obiettivo di questo progetto è quello di automatizzare il flusso di lavoro NDSI come modello nel toolbox di elaborazione QGIS. L'output richiesto è un poligono vettoriale che mostra l'estensione coperta di neve all'interno del bacino idrografico dello Snowy Water Catchment, insieme all'attribuzione che descrive l'area totale coperta in chilometri quadrati.
## Metodo
L'algoritmo NDSI è abbastanza semplice (vedi sotto in Formula 1.1 - Normalised Difference Snow Index (NDSI)) e i successivi passaggi necessari per estrarre il manto nevoso in formato vettoriale si prestano bene anche ad un modello di toolbox di elaborazione.

<figure>
<img src="../images/australia_snowyhydro8.png" alt="australia_snowyhydro8.png" />
<figcaption>Formula 1.1 - Normalised Difference Snow Index (NDSI)</figcaption>
</figure>

Questo algoritmo NDSI restituisce risultati compresi tra -1 e 1, con una soglia per la neve tipicamente superiore a 0,4. Un esempio dell'output NDSI è mostrato di seguito (Mappa 1.3 - output NDSI), accanto ad un'immagine a colori naturali (Mappa 1.2 - MODIS true color) per il 13 luglio 2014. Come si vede da queste immagini, l'output NDSI è molto buono nel discriminare le aree innevate da altri tipi di copertura del suolo e dalle nuvole. Può tuttavia classificare erroneamente come neve porzioni di grandi masse d'acqua, causate da acqua con caratteristiche di assorbimento nella parte dello spettro del vicino infrarosso. Questa caratteristica dell'NDSI indica la necessità di incorporare nel modello una maschera dell'acqua ad un certo punto.

<figure>
<img src="../images/australia_snowyhydro2.jpg" class="align-left" width="300" alt="australia_snowyhydro2.jpg" />
<figcaption>Map 1.2 - MODIS true colour</figcaption>
</figure>

<figure>
<img src="../images/australia_snowyhydro3.jpg" class="align-center" width="300" alt="australia_snowyhydro3.jpg" />
<figcaption>Map 1.3 - NDSI output</figcaption>
</figure>

<figure>
<img src="../images/australia_snowyhydro4.jpg" class="align-left" width="300" alt="australia_snowyhydro4.jpg" />
<figcaption>Map 1.4 - Recoded "Snow" vs "Non snow"</figcaption>
</figure>

The NDSI output is created with some very simple band map by using the GRASS module \"r.mapcalculator\". Once the NDSI grid was available the NDSI threshold of 0.4 needed to be applied and this would result in a boolean grid depicting \"Snow\" and \"Non snow\" areas. To get that classification another GRASS module \"r.recode\" was used and produced the result shown above in Map 1.4 Recoded 'Snow' vs 'Non Snow'.

The recoded grid was then converted to a vector polygon dataset and the snow covered areas were extracted (shown below, Map 1.5 - Extracted snow). The snow covered areas were then clipped to the Snowy Water Catchment (shown below, Map - 1.6 Snow inside the SWC), then the large water bodies are masked out (shown below, Map 1.7 - Final snow covered area), and finally the area statistics for the snow covered area is generated.

<figure>
<img src="../images/australia_snowyhydro5.jpg" class="align-left" width="300" alt="australia_snowyhydro5.jpg" />
<figcaption>Map 1.5 - Extracted Snow</figcaption>
</figure>

<figure>
<img src="../images/australia_snowyhydro6.jpg" class="align-center" width="300" alt="australia_snowyhydro6.jpg" />
<figcaption>Map 1.6 - Snow inside the SWC</figcaption>
</figure>

<figure>
<img src="../images/australia_snowyhydro7.jpg" class="align-left" width="300" alt="australia_snowyhydro7.jpg" />
<figcaption>Map 1.7 - Final snow covered area</figcaption>
</figure>

The output from the model is a vector polygon showing the snow covered area within the Snowy Water Catchment. The attributes of the polygon include the area covered by the snow and the percentage of the catchment that is covered. The model in its entirety can be seen below in \"Image 1.1 - Normalised Difference Snow Index (NDSI) QGIS processing toolbox model\".

<figure>
<img src="../images/australia_snowyhydro.png" class="align-center" width="600" alt="australia_snowyhydro.png" />
<figcaption>Image 1.1 - Normalised Difference Snow Index (NDSI) QGIS processing toolbox model</figcaption>
</figure>

## Risultati / Conclusione
Il toolbox di elaborazione QGIS è un modo potente per automatizzare un flusso di lavoro come questa classificazione della neve. Il modello mostrato sopra automatizza con successo il processo di classificazione della neve e fornisce un set di dati GIS che può essere utilizzato per la visualizzazione e l'inserimento in ulteriori applicazioni statistiche. Rimuove con successo gli errori soggettivi dell'utente associati ai metodi precedentemente utilizzati da SHL, fornendo al contempo uno strumento di classificazione ripetibile e coerente. Alcuni risultati stagionali possono essere visualizzati qui.
### Autore
Andrew Jeffrey è un analista GIS con Snowy Hydro Limited con sede a Cooma NSW, Australia. Si è laureato presso la Charles Sturt University a Wagga Wagga con una laurea in Sistemi Informativi Territoriali nel 2004. In Snowy Hydro Limited è stato in grado di fornire supporto spaziale a progetti interessanti come l'esperimento Cloud Seeding e le operazioni quotidiane all'interno dell'organizzazione.

{{<content-end >}}
