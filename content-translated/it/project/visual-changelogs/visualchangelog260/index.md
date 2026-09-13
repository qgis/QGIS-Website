---
HasBanner: false
draft: false
releaseDate: '2014-10-31'
section: progetto
sidebar: true
title: Elenco cambiamenti per QGIS 2.6
type: visual-changelog

---
{{<content-start >}}
# Elenco cambiamenti per QGIS 2.6{#changelog26 }
Data di rilascio: 2014-10-31

Lista dei cambiamenti per QGIS 2.6.0.  Sono state aggiunte molte nuove funzioni, modifiche e miglioramenti per rendere il più popolare software GIS per il desktop ancora più ricco di funzioni ed utile.  

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

Vogliamo ringraziare gli sviluppatori, i documentatori, i tester e tutti quelli che hanno dedicato il proprio tempo per migliorare QGIS.

From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

Infine vorremmo ringraziare i nostri sponsor ufficiali per il loro prezioso supporto finanziario:
- **GOLD Sponsor: Asia Air Survey, Japan** <http://www.asiaairsurvey.com/>
- SILVER Sponsor: [Sourcepole AG, Switzerland](http://www.sourcepole.com/)
- SILVER Sponsor: [State of Vorarlberg, Austria](http://www.vorarlberg.at/)
- BRONZE Sponsor: [Lutra Consulting, UK](http://www.lutraconsulting.co.uk/)
- BRONZE Sponsor: [www.molitec.it, Italy](http://www.molitec.it/)
- BRONZE Sponsor: [www.argusoft.de, Germany](http://www.argusoft.de)
- BRONZE Sponsor: [www.openrunner.com, France](http://www.openrunner.com)
- BRONZE Sponsor: [GKG Kassel,(Dr.-Ing. Claas Leiner), Germany](http://www.eschenlaub.de/)

A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become an official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts.

If you enjoy using QGIS, please consider making a donation to support the project - either [financial](https://qgis.org/en/site/getinvolved/donations.html) or of [your time and skills](https://qgis.org/en/site/getinvolved/index.html)! Lastly we would like to also take a moment to encourage you to fund a [special campaign](http://blog.vitu.ch/10102014-1046/crowdfunding-initiative-automated-testing) by one of our QGIS developers to get a working test suite for QGIS so that we can improve out quality assurance process and deliver you the best possible releases.

QGIS è un Software Libero e non c'è alcun obbligo di pagare nulla per utilizzarlo - vogliamo infatti incoraggiare le persone di ogni parte del mondo ad usarlo, indipendentemente dalla propria situazione finanziaria o sociale - crediamo che mettere tutti nella condizione di utilizzare gli strumenti decisionali spaziali produrrà una società migliore per tutta l'umanità.

{{<table-of-contents >}}
## Generale
### Funzionalità: Nome del file di progetto nelle proprietà
Ora potete vedere il percorso completo del file di progetto di QGIS nella finestra di dialogo relativa alle proprietà del progetto

![](images/entries/8662dc4a69298f603dd9038d1199ab16fd25f786.webp)
### Funzionalità: Consenti la rimozione dell'ultimo punto durante la misura mediante i tasti Del / Backspace
Ora mentre misurate aree e distanze potete rimuovere i vertici indesiderati dalla linea di misura utilizzando i tasti delete o backspace.

![](images/entries/ed471908937cb068e2f004e7b3311f2bdf307042.webp)
### Funzionalità: seleziona sulla mappa la geometria collegata dal widget relativo al riferimento della relazione 
### Funzionalità: Widget per le modifiche
Abbiamo apportato numerosi miglioramenti ai widget per le modifiche
- nuovo widget per la modifica di data/ora capace di impostare date nulle
- modifica il contenuto del filtro
- Corretta gestione dei valori NULL per i widget di modifica
- Il widget di controllo della fotografia mantiene i valori NULL
- Il widget di controllo del web mantiene i valori NULL
- La tabella degli attributi può distinguere tra 0 e NULL
- Aggiungi il supporto del suffisso per il widget di intervallo

![](images/entries/78fd27b2cf736f37bdf97694a5018f29c609c6cb.webp)
### Funzionalità: Utilizzo facoltativo di un solo sottoinsieme di campi dal layer unito
E' ora possibile utilizzare solo un sottoinsieme di campi correlati durante la creazione di un vettore da unire. 

![](images/entries/14023cf2ee768960d9c4a43da6e2a1624d10b3c3.webp)
### Funzionalità: Campo espressione (campi virtuali)
Sometimes you want to have an attribute that is calculated and that is always \'fresh\' - reflecting the current state of the feature properties. Now you can add virtual fields to your table which are based on an expression.

![](images/entries/5fe53ad54b8d0cf8b7a22b90e733a421bb929506.webp)
### Funzionalità: Ora le azioni possono avere un'icona associata
Durante la creazione di un'azione personalizzata per un layer vettoriale, ora è anche possibile definire un'icona da utilizzare per l'azione.

![](images/entries/e7bd5b306e3a72cc111a81f86a053b42679aa2f8.webp)
### Funzionalità: Ulteriori tipi di espressioni ed opzioni
- Allow using `+` for string concatenation.
- New keyword: `attribute( feature, attribute_name )` - gets the specified attribute from a feature.
- New keyword: `$currentfeature` - returns the current feature.
- New keyword: `$atlasfeature` - returns the atlas feature.
- New keyword: `getFeature` - gets a matching feature from a layer.

![](images/entries/e2e079bec87be65ccc97055251fc2544be91aaab.webp)
### Funzionalità: le classi all'interno dei tipi di visualizzazione graduati e categorizzati possono essere abilitate
Ora si può scegliere di disabilitare alcune classi nei tipi di visualizzazione graduati e categorizzati senza rimuoverle.

![](images/entries/84d11c6d978775d92f6a1902092795735d1f32b3.webp)
### Funzionalità: Miglioramenti della legenda
E' stata completata la seconda fase di revisione della legenda / indice. Questo comprende: 
- Pulizia della API (per sviluppatori)
- Visibilità dei gruppi di layers nell'albero dei layers. Questo nuovo pulsante della barra degli strumenti consente rapidi cambiamenti tra i gruppi di layers che dovrebbero essere visibili.
- Capacità di gestire i gruppi di layer nella barra degli strumenti legenda
- La nuova opzione di filtraggio nella barra degli strumenti legenda rimuoverà gli argomenti della legenda per tutte le classi che non sono  attualmente comprese nell'estensione della vista. Questo è un grande miglioramento dato che assicura che la legenda della vostra mappa non contenga inserimenti di argomenti non presenti nella vista attuale della mappa. L'opzione è disponibile nella legenda principale della mappa, nel compositore di stampe e per i layers WMS.
- Le legende degli stili di rappresentazione tramite regole ora possono essere visualizzate in un pseudo-albero

![](images/entries/363048a7d08ac76d35463abbef514c65031922e7.webp)
## Sorgenti Dati
### Funzionalità: miglioramenti dell'esportazione in DXF
- vista ad albero e selezione degli attributi per l'assegnazione al layer nella finestra di dialogo
- supporto riempimento poligoni/HATCH
- rappresentare i testi come MTEXT invece di TEXT (compresi carattere, inclinazione e peso)
- support for RGB colors when there\'s no exact color match
- utilizzo di AutoCAD 2000 DXF (R15) al posto di R12
- rimozione dei metodi di test R18

![](images/entries/4f615505e3fd6ec0b619278e42ecc5a3e79ac827.webp)
## Compositore di Mappe
### Funzionalità: Controllo della scomparsa di elementi del compositore di stampe dalle mappe/esportazioni 
Abbiamo aggiunto una casella di controllo e un pulsante definito in funzione dei dati per controllare se un oggetto è escluso dalle esportazioni/stampe del compositore di stampe. Se l'oggetto è deselezionato sarà visibile solo durante la progettazione della composizione. 

![](images/entries/f334447d13ee49a6c4c5cb4322e3f12824643416.webp)
### Funzionalità: Controllo sulla stampa di pagine per cornici vuote del compositore di stampe
Per quanto riguarda le tabelle o i quadri HTML una checkbox controlla ora se la pagina contenente debba essere esportata quando la cornice è vuota

![](images/entries/1500ba6abdf5b314c760ebfc63e460731dcc5110.webp)
### Funzionalità: pannello ad albero degli oggetti
Il pannello ad albero degli oggetti nel compositore di stampe permette la selezione degli oggetti, l'occultamento/visualizzazione degli oggetti, l'abilitazione dello stato di blocco degli oggetti e la modifica dell'id degli oggetti mediante doppio click. Si può anche utilizzare il trascinamento per riordinare gli oggetti. 

![](images/entries/52b70bdf87d21a13c00798458bab6347dddd7910.webp)
### Funzionalità: Più controllo sull'aspetto degli oggetti freccia/linea nel compositore di stampe
- Le linee possono essere disegnate utilizzando la finestra di dialogo stile simbolo di linea
- I colori di riempimento e bordo della testa delle frecce possono essere definiti dall'utente
- Lo spessore del bordo della testa delle frecce può essere definito dall'utente

![](images/entries/49757b3cc09839edb8af38f1cb1317458f279110.webp)
### Funzionalità: Controllo definito dai dati degli oggetti del compositore di stampe
Molte proprietà degli oggetti del compositore di stampe ora possono essere controllati mediante l'associazione dei dati. Queste includono:
- Trasparenza e metodo di fusione
- Rotazione dell'oggetto
- Scala della mappa, estensione e rotazione.
- Geometria dei margini dell'atlante.
- Dimensione e posizione dell'oggetto
- Dimensione della pagina, orientamento e numero di pagine.

![](images/entries/9f321489cd9c90eb4d66e577680fc5467756e58e.webp)
### Funzionalità: Le immagini del compositore di stampe possono essere specificate come URLS remote
Gli oggetti immagine nel compositore di stampe ora supportano le urls remote come sorgente dell'immagine. Questa sorgente può anche essere definita dai dati.

![](images/entries/05cd7008c231df3b3af874753b840669a605cb0f.webp)
### Funzionalità: Miglioramenti della tabella del compositore di stampe
- È ora possibile impostare l'intestazione della tabella e il colore del carattere.
- È ora possibile dividere le tabelle in strutture multiple, permettendo così di distribuire il loro contenuto su più colonne o in pagine differenti.
- Aggiunta l'opzione di visualizzazione delle intestazioni sul primo modulo, tutti i moduli o nessun modulo.
- Permette il controllo manuale della larghezza delle colonne.
- Nuove opzioni per l'origine della tabella, comprese l'attuale geometria dell'atlante e le geometrie figlie in una relazione.
- Scelta del comportamento delle tabelle vuote, inclusi l'occultamento dell'intera tabella, la visualizzazione delle celle vuote o di un messaggio preimpostato nel corpo della tabella.
- Aggiunta una casella di controllo per filtrare le geometrie della tabella a quelle che intersecano l'attuale geometria dell'atlante.
- Aggiunta una casella di controllo per rimuovere le righe duplicate in una tabella.

Si noti che le tabelle nei progetti esistenti non vengono aggiornate automaticamente al nuovo formato di tabella che supporta queste caratteristiche e devono pertanto essere reinserite in una composizione affinchè le nuove impostazioni appaiano.

![](images/entries/9ccb75b2110daf0c95a3fba31ac18144c1345f0e.webp)
### Funzionalità: Miglioramenti del compositore di stampe
Il compositore di stampe (utilizzato per preparare mappe stampabili) ha ricevuto numerosi miglioramenti in QGIS 2.6.
- E' ora possibile cambiare il colore di riempimento secondario per le scale grafiche
- Mantenendo premuto il tasto Shift mentre si disegnano oggetti linea / freccia si forza il disegno in orizzontale, verticale o per angoli di 45 gradi
- Mantenendo premuto il tasto Shift mentre si disegnano altri nuovi oggetti li si forza a quadrati, mantenendo premuto il tasto Alt si ottiene che vengano disegnati dal centro
- Il click con il tasto destro non blocca/sblocca più gli oggetti, questo ora viene gestito con il nuovo pannello oggetti. Gli oggetti bloccati non possono più essere selezionati dalla mappa nel compositore di stampe, consentendo l'interazione con gli oggetti sottostanti.
- La pressione del tasto Alt contemporaneamente ai tasti cursore comporta un movimento di 1px per gli oggetti
- Removed the destructive \'Load from template\' menu item, replace with a new non-destructive \'Add items from template\' action

![](images/entries/a7267ed637121bc9be70c5fa0afd2a63f9790bc7.webp)
### Funzionalità: migliorato lo snapping agli oggetti
Ora le soglie di snapping sono impostate in pixels, permettendo così movimenti più fini ed il ridimensionamento degli oggetti utilizzando lo zoom in una composizione. Gli oggetti all'interno di un gruppo non vengono più utilizzati per lo snap automatico delle linee.

![](images/entries/8e43479380c28942345f3d9500dd956bd13f43e8.webp)
### Funzionalità: Panoramiche multiple per un oggetto della mappa
Sometimes it is useful to be able to show more than one overview frame for a map frame. For example if you want to show where your map is in local, regional and global context, using multiple overview maps can help you to achieve this. As of QGIS 2.6 you can now achieve this by assigning as many maps as you like to the \'overview\' role in your composition.

![](images/entries/88b55cc5f5e7cfb62486fe3b4867b7133ae66953.webp)
### Funzionalità: Miglioramento deglli oggetti HTML
Ci sono molte nuove utili opzioni per gli oggetti HTML del compositore di stampe: 
- Opzione per l'inserimento manuale del file HTML sorgente
- Le espressioni QGIS in HTML possono essere valutate prima della visualizzazione del contenuto HTML 
- URL per il file sorgente HTML definito dai dati
- Possibilità di creare un foglio di stile utente che ignora gli stili HTML

![](images/entries/7ed388f0c775b738648b2bd6eb6be0a75fa5816a.webp)
### Funzionalità: Miglioramenti del reticolo del compositore di stampe
- E' ora possibile avere reticoli multipli con proprietà differenti.
- E' possibile mettere insieme reticoli riproiettati e reticoli Lat/Long.
- E' possibile utilizzare la simbologia QGIS standard per reticolo, linee, ecc.
- C'è un nuovo stile 'solo riquadro/annotazioni' per il reticolo. Selezionando questo stile verranno disegnati solo il riquadro e le annotazioni, senza linee del reticolo o altri simboli sulla mappa.
- Sono disponibili opzioni per controllare quale parte di un elemento della mappa è disegnato nel riquadro.
- Sono disponibili nuovi stili per le tacche dei riquadri, con opzioni per tacche interne, esterne o entrambe.
- Sono stati apportati miglioramenti alle annotazioni del reticolo, compresi molti nuovi formati.
- Nelle annotazioni del reticolo ora vengono utilizzati i simboli tipograficamente corretti 'primo' e 'doppio primo'.

![](images/entries/eeb61d7da3d3f95283b1bb47545cbdff9cc334ae.webp)
## Processing
### Funzionalità: Reperimento on-line di modelli e scripts
I modelli e gli script possono essere scaricati dalla collezione online e installati direttamente dall'interfaccia di Processing. La collezione sarà ampliata con nuovi script e modelli forniti dagli utenti.

![](images/entries/23e357ca0e559a33a7872206b306c0b1fbdb4b7d.webp)
### Funzionalità: Implementazione del nuovo modellatore
Il modellatore è stato riscritto ed ora fornisce funzionalità extra, come consentire modelli annidati senza limite di profondità. I modelli ora sono immagazzinati come files JSON. La retrocompatibilità è stata mantenuta, quindi possono ancora essere utilizzati tutti i modelli. Ora è possibile anche trascinare oggetti da inputs e algoritmi sul modellatore grafico.

![](images/entries/72bb8beaf97133424d1e68da67ae6fe79ea6faf6.webp)
## Programmabilità
### Funzionalità: Cambiamenti della API per i widget QGIS
In order to normalise the naming of QGIS widgets, some minor API changes have been made. Almost all edit widgets were renamed by adding \"Wrapper\" at the end of their names. In particular this concerns:
- QgsCheckboxWidget -\> QgsCheckboxWidgetWrapper
- QgsClassificationWidget -\> QgsClassificationWidgetWrapper
- QgsColorWidget -\> QgsColorWidgetWrapper
- QgsEnumerationWidget -\> QgsEnumerationWidgetWrapper
- QgsFilenameWidget -\> QgsFilenameWidgetWrapper
- QgsHiddenWidget -\> QgsHiddenWidgetWrapper
- QgsPhotoWidget -\> QgsPhotoWidgetWrapper
- QgsRangeWidget -\> QgsRangeWidgetWrapper
- QgsTexteditWidget -\> QgsTexteditWrapper
- QgsUniquevalueWidget -\> QgsUniquevalueWidgetWrapper
- QgsUuidWidget -\> QgsUuidWidgetWrapper
- QgsValuemapWidget -\> QgsValuemapWidgetWrapper
- QgsValuerelationWidget -\> QgsValuerelationWidgetWrapper
- QgsWebviewWidget -\> QgsWebviewWidgetWrapper

## QGIS Server
### Funzionalità: Miglioramento della funzionalità di ricerca con la richiesta GetFeatureInfo
<https://github.com/qgis/QGIS/commit/8888c5f0c0e0ffdf23453a20addf6abaf125845d>
### Funzionalità: Aggiunto un controllo della precisione per gli attributi delle geometrie GetFeatureInfo
## Simbologia
### Funzionalità: Migliore scelta casuale dei colori
Abbiamo migliorato l'algoritmo di colorazione casuale per le visualizzazioni classificate affinchè i colori generati siano maggiormente distinti uno dall'altro dal punto di vista visivo.

![](images/entries/ec29c9d6eb23d01b4dbbae32a6e20fe0b1f48198.webp)
### Funzionalità: Miglioramenti della simbologia dell'interfaccia utente
- Ove possibile, le proprietà dei simboli del layer vengono mantenute cambiando il tipo di simboli.
- Aggiunto un pulsante di modifica per la scala di colori di sfumature e gradienti.
- Aggiornamento automatico dell'etichetta e degli intervalli di vicinanza
- Le classi vengono automaticamente convertite da categorizzate e graduate passando alla visualizzazione tramite regole
- Aggiunti unità e numero di cifre decimali alle etichette del visualizzatore graduato.
- Migliorata la reattività ai cambiamenti nella scala dei colori, la scala inversa dei colori e altre opzioni nella GUI
- Quando si passa da semplice a graduata, categorizzata e altre rappresentazioni i simboli vengono mantenuti.
- Migliorata l'etichettatura della modalità di calcolo della StdDev.

![](images/entries/08305d5131c28c45b400662267ff0d174ef9c8ce.webp)
## Interfaccia Utente
### Funzionalità: Editor del codice di evidenziazione della sintassi
Per gli editor di script python, il generatore di espressioni, la finestra del filtro, il compositore HTML e gli editor CSS

![](images/entries/54b470a064d65d6d65aa66a8feece43ba8cbf6c4.webp)
### Funzionalità: Tavolozza dei colori
E' ora possibile definire la propria tavolozza di colori personalizzata da utilizzare in QGIS.
- Tavolozza dei colori globale personalizzata dell'utente (nella finestra di dialogo opzioni).
- Tavolozza dei colori per progetto (nella finestra di dialogo proprietà del progetto).
- I colori sono mostrati nei menu dei pulsanti colore e nella nuova finestra di dialogo di selezione dei colori.
- E' possibile importare/esportare i colori in un file della tavolozza GPL.

![](images/entries/a156f408d7a87fc930095c8fd68e9fba0fc0a817.webp)
### Funzionalità: Nuova finestra di dialogo di selezione dei colori.
E' disponibile una nuova finestra di dialogo QGIS di selezione dei colori personalizzata.
: - Cursori per tonalità, saturazione, valore, componenti dei colori rosso, verde, blu
  - Cursore alfa
  - Opzione per copiare/incollare i codici di colore html (in una varietà di formati).
  - Anteprima del colore prima/dopo, con anteprima alfa.
  - Controllo interattivo del gradiente di colore 2D.
  - Controllo rotella/triangolo della tonalità.
  - Tavolozza dei colori editabile, con la capacità di creare nuove tavolozze e importare/esportare i colori su un file di tavolozza GPL.
  - Campionatore del colore in tempo reale con la possibilità di campionare in un raggio preimpostato (dipende dal sistema operativo)
  - Supporta l'interazione con altre applicazioni tramite drag and drop dei colori (dipende dal sistema operativo)
  - Opzione per disabilitare la finestra di dialogo ed utilizzare invece la finestra di dialogo di selezione dei colori nativa

![](images/entries/7189c0fe2d1ff3fdc63c531a02f74b5d32b70bfd.webp)
### Funzionalità: Strumento di selezione singola della geometria incorporato nella selezione di rettangolo
Abbiamo incorporato lo strumento di selezione singola nello strumento rettangolo. Se volete selezionare una geometria singola, semplicemente abilitate lo strumento rettangolo e cliccate una volta (piuttosto che trascinare con l'ottenimento di un rettangolo) una geometria.

![](images/entries/f8a68fcdfcaa59e6162185acb5c92edb9145c881.webp)
### Funzionalità: Comportamento del comando 'aggiungi layer alla mappa'
In many of QGIS\' dialogs that generate a new layer, the \'Add layer to map canvas\' checkbox is now checked by default so that the new layer automatically gets added to the map.

![](images/entries/f36f5912d2422a439d67b1a743fe81588e709dfb.webp)
### Funzionalità: Aggiunta di icone di dimensioni 48 e 64
Per coloro che utilizzano QGIS su dispositivi touch (o solo se vi piacciono icone grandi e grosse), ora si possono impostare le icone fino a una dimensione di 64 x 64 pixels. 

![](images/entries/3be3f51da2f54a8395f054f757f9fae1948a6103.webp)
### Funzionalità: Nuovi pulsanti colore
This is probably one of the most useful new features in QGIS 2.6 -especially if you are involved a lot in cartography work. The colour button used everywhere in QGIS has been enhanced, with drop down menus, colour swatches, default colours, etc. Click on the drop down item to the right of the colour button to see the quick options. Click on the button to the left of the colour widget to see a standard colour chooser dialog.

![](images/entries/54c211513bc86d00a5bce01a17476481937e0fbe.webp)
### Funzionalità: Menu contestuale per lo strumento di identificazione
Quando si utilizza lo strumento di identificazione è ora possibile cliccare con il tasto destro sulla mappa per utilizzare lo strumento di identificazione in modalità contestuale. Nel menu che appare è possibile definire che tipo di geometria si vuole identificare (o tutte, se si vuole).

![](images/entries/c395c2ce4964826458a721a8a3f89cb7dc2853b5.webp)

{{<content-end >}}
