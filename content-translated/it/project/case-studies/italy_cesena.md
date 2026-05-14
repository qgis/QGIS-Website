---
HasBanner: false
archived: true
date: 2015-10-30
draft: false
featured: false
section: progetto
sidebar: true
thumbnail: images/italy_cesena1.png
title: QGIS per descrivere le Mura di Cesena
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

L'UNIVERSITÀ ECAMPUS venne creata come un'Università online e riconosciuta dal MIUR (Ministero Italiano per l'Istruzione, l'Università e la Ricerca) tramite il Decreto Ministeriale del 30 gennaio 2006. Venne fondata con lo scopo di fornire accesso all'università attraverso la sua piattaforma eLearning ai giovani, professionisti, imprenditori, dirigenti e agli attori imprenditoriali e culturali con lo scopo di contribuire al mercato del lavoro. La sede principale, nota anche come Campus Internazionale di Milano, o Campus di Novedrate, si trova nell'ex centro IBM di Novedrate (Como, Italia), in un campus nella ridente Brianza.

L'Università ha 5 facoltà virtuali: Ingegneria, Economia, Psicologia, Arte, Giurisprudenza. LE MAPPE STORICHE E IL PROGETTO QGIS La cinta muraria caratterizza la città di Cesena. La sua forma a scorpione divide il centro storico dalla zona più recente costruzione.

I documenti cartografici storici descrivono la sua evoluzione e la sua distruzione. QGIS consente di confrontare diverse mappe storiche perché permette di trasferire tutte le mappe nello stesso Sistema di Riferimento, tramite il plugin di georeferenziazione. Ad esempio, il layer aperto Google Satellite e il layer aperto Open Street Map sono stati usati per riferire tutte le mappe storiche al Sistema di Riferimento EPSG: 3857 (Web Mercatore o Pseudo Mercatore).

QGIS si è rivelato uno strumento fondamentale per elaborare, analizzare e confrontare queste mappe georeferenziate attraverso i layer vettoriali o shapefile, nei quali ho memorizzato tutti gli elementi delle mappe, come strade, edifici, parchi e giardini, le Mura della Città, le antiche torri fortificate e le antiche Porte della Città. Ho usato layer puntuali, lineari e poligonali. Ho comparato questi layer attraverso gli strumenti di analisi, ricerca, geoprocessamento, geometria e di gestione dei dati (Fig. 1).

<figure>
<img src="../images/italy_cesena1.png" style="width:100.0%" alt="italy_cesena1.png" />
<figcaption>Fig. 1 Concept Map of the QGIS project</figcaption>
</figure>

Utilizzando questi strumenti, ho ottenuto informazioni su:
- The precision of the Leonardo Da Vinci\'s topographic survey, realized in 1502, such as how many points of this survey are correct (Fig. 2);
- The Cesena Wall\'s Development from the Roman Age to the 15th Century;
- The Cesena Wall\'s Demolitions from the 19th Century to the Early 20th Century;
- I cambiamenti morfologici delle Mura della Città, ad esempio le demolizioni delle sue antiche torri fortificati e delle antiche Porte della Città;
- The Cesena\'s Urban Progress from the 16th Century to the Present;

<figure>
<img src="../images/italy_cesena2.png" style="width:100.0%" alt="italy_cesena2.png" />
<figcaption>Fig. 2: Openlayer Google Satellite overlapped by the informations recorded in different layers: the present City Wall in black, the Leonardo Da Vinci's topographic survey of the City Wall in orange, the Leonardo Da Vinci's points of survey in yellow and the present ancient City Gates in red.</figcaption>
</figure>

Esistono moltissimi strumenti di QGIS, e ne ho utilizzati alcuni per creare:
- Link per connettere ogni sezione del layer lineare delle attuali Mura della Città a fotografie, che rappresentano l'attuale stato di conservazione;
- Una mappa di Cesena nel 19esimo secolo attraverso il compositore di stampe;
- Un modello 3D di Cesena con il plugin qgis2threejs (Fig. 3);

<figure>
<img src="../images/italy_cesena3.png" style="width:100.0%" alt="italy_cesena3.png" />
<figcaption>Fig. 3: The 3D model of the present City Wall and Cesena's buildings inside and outside the Wall. The ancient fortified towers and the ancient City Gates are indicated.</figcaption>
</figure>

## Conclusione
Le mappe storiche sono documenti importanti anche se la loro precisione non può essere comparata con quella dei documenti cartografici attuali, e sono inoltre rappresentazioni molto comunicative anche per persone non esperte di rappresentazioni geografiche. QGIS è stato l'unica strumento che mi ha permesso di usare il contenuto numerico delle mappe storiche mediante una rappresentazione efficace e significativa.
## Riferimenti Bibliografici
Le mappe storiche sono state estratte da:
- \"Costruzione, alterazione e recupero del centro storico di Cesena\", Ballardini, Cantori, Pezzi, Righetti, Tossani, Bruno Ghigi Editore, 1977
- \"La cinta muraria di Cesena\", Pino Montalti, Edizioni Panini, 1986

Le informazioni storiche sono state estratte da:
- \"La cartografia in Italia: nuovi metodi e nuovi strumenti dal Settecento ad Oggi\", Andrea Cantile, IGM Firenze, 2007
- \"Lineamenti di storia della cartografia italiana, volume secondo, dal Seicento al Novecento\" Andrea Cantile, Geoweb, 2013
- \"I rilievi cartografici di Leonardo per Cesena ed Urbino contenuti nel manoscritto \'L\' dell\'Istituto di Francia\", Nando De Toni, G. Barbéra Editore, 1965
- \"La città da guerra\", Amelio Fara, Einaudi, 1993
- \"La cartografia dall\'antichità fino al XVIII secolo\", Carlo Monti, Maggioli Editore, 2011

## Autore
Camilla Fabbri has a bachelor\'s degree in Civil and Environmental Engineering. She has developed her dissertation on historical cartography of the Cesena Wall using the QGIS program with the Supervisor Alessandra Borghi, who is the University Teacher of Topography and Theoretical Mechanics of the bachelor\'s degree in Civil and Environmental Engineering in the eCampus University.

{{<content-end >}}
