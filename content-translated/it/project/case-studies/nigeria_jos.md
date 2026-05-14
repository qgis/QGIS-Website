---
HasBanner: false
archived: true
date: 2011-12-31
draft: false
featured: false
section: progetto
sidebar: true
thumbnail: images/nigeria_jos1.jpg
title: Riserva forestale Amurum e mappatura dell'avifauna con QGIS in Nigeria
type: case-study

---
{{<content-start >}}
# Riserva forestale Amurum e mappatura dell'avifauna con QGIS in Nigeria
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>December 31, 2011</span>
</p>

La riserva forestale Amurum si trova vicino alla città di Jos, Stato di Plateau, in Nigeria.  È stata istituita in concomitanza con l'avvio della AP Leventis Ornitologico Research Institute (APLORI) ai fini della conservazione, l'istruzione e la ricerca della natura. APLORI è ospitato dal Dipartimento di Zoologia presso l'Università di Jos. Ogni anno un gruppo di circa otto studenti altamente motivati, ​provenienti da tutta la Nigeria, fanno una formazione sulla biologia della conservazione, sulla statistica (con R), e dal 2011 anche su GIS. Nel corso di due settimane in dicembre 2011 abbiamo studiato i concetti GIS di base e applicata con QGIS per gli studi sulla conservazione. In questo articolo descriviamo il modo in cui abbiamo usato QGIS per mappare gli habitat e i suoi determinanti della riserva Amurum e come le mappe di base dell'habitat sono state utilizzate per ottenere strati al fine di determinare in modo efficiente la distribuzione spaziale della avifauna tra cui la biodiversità.

<figure>
<img src="../images/nigeria_jos1.jpg" class="align-right" alt="nigeria_jos1.jpg" />
<figcaption>Training Group</figcaption>
</figure>

## Mappatura dell'elevazione, sfumatura del terreno, pendenza e habitat
1) Mapping elevation and groundtruthing: We downloaded (free) elevation data originating from the NASA Shuttle Radar Topographic Mission (SRTM) for the area in which Amurum is located. (Information about the global elevation data set can be found here: <http://www.cgiar-csi.org/data/elevation/item/45-srtm-90m-digital-elevation-database-v41>).
2) I GdalTools sono stati usati per fondere set di dati originali e per ritagliare una piccola area che contiene la riserva in modo che i dati raster siano ritagliati in quella zona. Per mezzo di GPS abbiamo raccolto elevazioni, in varie zone della riserva.
3) Nel complesso, le elevazioni del set di dati SRTM corrispondevano bene alle elevazioni raccolte con gps. I Modelli di terreno in GdalTools sono stati usati per calcolare le colline e piste per la zona. Queste variabili sono importanti da un punto di vista ecologico, perché sono fortemente associati con il tipo di habitat.

<figure>
<img src="../images/nigeria_jos2.jpg" class="align-right" alt="nigeria_jos2.jpg" />
<figcaption>QGIS screenshot</figcaption>
</figure>

4) Dal momento che abbiamo intenzione di sviluppare una bella mappa, abbiamo interpolato l'originale (ritagliato) elevazione della mappa per ottenere una risoluzione più elevata mappa. Abbiamo usato lo strumento altera in GdalTools. Mediante lo strumento di contorno abbiamo ottenuto linee di contorno lisce.
5) Le coordinate del confine della riserva sono state ottenuti camminando lungo i confini della riserva con un GPS. I punti d'interesse e le tracce memorizzate in GPS sono state importate utilizzando gli strumenti GPS, per costruire un shapefile di tipo poligono. I sentieri all'interno della riserva sono stati mappati in modo simile.
6) Siamo stati in grado di costruire rapidamente e con precisione una mappa dell'habitat di Amurum utilizzando un'immagine satellitare di Google che abbiamo ottenuto con il plugin Openlayers. La riserva ha tre tipi di habitat distinti: Savannah, Gallery forest e Rocky outcrop. Sulla base dell'immagine satellite abbiamo usato l'editor per disegnare i poligoni che delimitano i tre habitat. Le impostazioni delle opzioni di snap hanno permesso di costruire correttamente poligoni non sovrapposti.

## Mappatura della distribuzione degli uccelli e diversità
Le mappe degli habitat sono state usate per generare posizioni casuali. L'area dei vari tipi di habitat sono stati usati per generare un numero di posizioni proporzionale alla superficie di ciascun tipo di habitat (stratificazione).

<figure>
<img src="../images/nigeria_jos3.jpg" class="align-right" alt="nigeria_jos3.jpg" />
<figcaption>Training Group</figcaption>
</figure>

The random points in fTools were used for this purpose. All the locations were visited during two mornings by four groups of students (2 per group) giving a total of 38 random locations dispersed throughout the reserve. The observation data were entered in a spreadsheet and analyzed using R. In addition, the Shannon-Wiener diversity index was calculated using R. After merging the location file with the resulting observation data it was exported as a csv file which was loaded into QGIS using the "Add delimited text layer" tool. On the basis of the above mentioned layers a map was constructed presenting some of the most important landscape features and avian diversity of the Amurum reserve.
## Conclusione
Overall, the course was a great success. We - a group of students with no previous GIS experience —— enjoyed working with QGIS a lot. Within just two weeks time we were able to develop an extremely useful map of the reserve. Amongst others, the extents of the various habitats were determined which allows for stratification and thus for better estimates of abundances of various kinds of organisms. Basically we are now able to do better ecological research using QGIS as an open source platform.

<figure>
<img src="../images/nigeria_jos4.png" class="align-right" alt="nigeria_jos4.png" />
<figcaption>QGIS map: Diversity of Amurum Forest Reserve</figcaption>
</figure>

## Autori
Abengowe Elmond Chiadikaobi, Adeyanju Temidayo Esther, Akiemen Nerioya, Albert Malangale Tauje, Azi Abok Joel, Echude Daniel, Eelke Folmer, Nwaogu Chima Josiah, Onoja Joseph Daniel, Yadok Biplang Godwill

{{<content-end >}}
