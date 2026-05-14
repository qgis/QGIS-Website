---
draft: 'true'

---
# QGIS e GRASS per la mappatura del pericolo di incendi boschivi
## Introduzione
Il Southern Downs Regional Council (SDRC) è un piccolo-medio governo locale nel sud-est del Queensland, in Australia. La regione del Consiglio, principalmente la parte meridionale, soffre di grandi incendi boschivi, Gli incendi boschivi sono una preoccupazione reale e presente per i residenti e i proprietari terrieri nella regione dei Southern Downs e hanno provocato la perdita di vite umane e proprietà.

Questo progetto permetterà al Consiglio e alla popolazione della regione di essere più consapevoli del rischio e di consentire un migliore processo decisionale in futuro.

![](./images/australia_queens1.jpg){.align-right}
## Il Progetto
As bushfire is not only a problem for SDRC but also for the whole of Queensland, the state government requires that each local government identifies the bushfire hazard in their area via the State Planning Policy 1/03 Mitigating the Adverse Impacts of Flood, Bushfire and Landslide \[1\]. This kind of job would normally be done using consultants but was instead done by the council itself using a combination of QGIS and GRASS.

La parte GIS del progetto è stato suddivisa in 6 fasi principali
- Valutazione e mappatura della pendenza
- Valutazione e mappatura dell'esposizione
- Valutazione e mappatura della vegetazione
- Combinazione di punteggi per identificare la gravità del pericolo incendio boschivo
- Verifica sul campo e valutazione qualitativa
- Mappe finali

## L'uso di QGIS e GRASS
![](./images/australia_queens2.jpg){.align-right}

QGIS, using the GRASS plugin, was selected as it provided the tools needed to complete the job and the interaction between QGIS and GRASS made it easy to process the raster maps and present them in a meaningful way to users. SDRC uses MapInfo for its main GIS system, however MapInfo's addons were not as powerful as GRASS GIS for raster processing.

Il plug-in QGIS GRASS è stato utilizzato per importare i contour a 5 metri dell'intera regione in GRASS, che sono stati poi convertiti in una mappa raster di countour utilizzando r.surf.contour. Una mappa di pendenza ed esposizione sono state quindi generate utilizzando r.slope.aspect partendo dalla mappa raster del contour. Le categorie sono state assegnate ai diversi intervalli di pendenza ed esposizione a cui è stata assegnata una classe di pericolosità. Anche alle aree di vegetazione sono stati assegnati punteggi di rischio diversi. Tutte le mappe raster risultanti sono state quindi combinate utilizzando mapcalc e hanno ottenuto un punteggio finale di rischio. I punteggi di rischio sono stati quindi divisi in tre categorie principali: alto; medio; e basso.

La parte finale del processo è stata la verifica sul campo tramite il servizio dei vigili del fuoco rurali. Dopo il processo di revisione, QGIS è stato utilizzato per stampare le mappe finali per la presentazione.

Poiché tutti i comandi di GRASS possono essere eseguiti dalla riga di comando, sono stati registrati tutti i comandi necessari per generare le mappe di pericolo di incendi boschivi, a scopo di documentazione e se le mappe dovessero essere rigenerate in futuro.
## Conclusione
Nel complesso QGIS, insieme al plug-in GRASS, ha fornito un'ottima esperienza e un ottimo risultato finale per il Comune che ha eseguito la propria mappatura del rischio di incendi boschivi. Il plugin GRASS fornisce un'interfaccia molto facile da usare per GRASS tramite QGIS. Poiché QGIS è in grado di aprire il formato raster GRASS in modo nativo, l'integrazione è molto semplice e le mappe possono essere create con facilità.

The project won an encouragement award at the Queensland Planning Institute of Australia state planning awards in 2010 \[2\]
## Riferimenti
- \[1\] <http://www.emergency.qld.gov.au/publications/spp/>
- \[2\] <http://digital.crowtherblayne.com.au/default.aspx?xml=crowther_pia.xml>

## Autore
![Nathan Woodrow](./images/australia_queensaut.jpg){.align-left height="200px"}

Questo articolo è stato scritto nel mese di gennaio del 2011 da Nathan Woodrow. Nathan è un operatore GIS presso il Consiglio regionale del Southern Downs e sta studiando Spatial Science presso la University of Souther Queensland
