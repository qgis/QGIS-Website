---
HasBanner: false
draft: false
releaseDate: '2013-09-09'
section: progetto
sidebar: true
title: Elenco cambiamenti per QGIS 2.0
type: visual-changelog

---
{{<content-start >}}
# Elenco cambiamenti per QGIS 2.0{#changelog20 }
Data di rilascio: 2013-09-09

{{<table-of-contents >}}
## Strumenti di Analisi
### Novità: Linea di comando
Per un veloce accesso agli strumenti di geoprocessing, è sufficiente eseguire la Linea di comando (CTRL + ALT+  M) e iniziare a scrivere il nome dello strumento che vuoi eseguire. La Linea di comando mostrerà le opzioni disponibili e le eseguirà. Non servirà più cercare strumenti attraverso il menu.

![image1](images/processing_commander_2.png)
### Novità: miglioramenti al plugin Mappa di concentrazione
Il plugin Mappa di concentrazione è stato migliorato e ottimizzato, permettendo di creare mappe di concentrazione più velocemente. In più, ora c'è la possibilità di scegliere con quale funzione creare la mappa.

![image2](images/Selection_027.png)
### Novità: supporto al processing
The SEXTANTE project has been ported to and incorporated into QGIS as core functionality. SEXTANTE has been renamed to \'Processing\' and introduces a new menu in QGIS from where you can access a rich toolbox of spatial analysis tools. The processing toolbox has incredibly rich functionality - with a python programming API allowing you to easily add new tools, and hooks to provide access to analysis capabilities of many popular open source tools such as GRASS, OTB, SAGA etc.

![image3](images/Selection_028.png)
### Novità: Modellatore grafico
Una delle grandi novità riguardanti il nuovo Processing è la possibilità di combinare gli strumenti graficamente. Utilizzando il **Modellatore grafico** , è possibile costruire analisi complesse da una serie di piccoli moduli. È possibile salvare questi modelli e poi utilizzarli come mattoni per costruire anche modelli più complessi. Tutto questo integrato direttamente in QGIS e molto semplice da usare!

![image4](images/Processing_modeler_029.png)
## Applicazioni e Opzioni del progetto
### Novità: opzioni per l'avvio di QGIS e template dei progetti
With QGIS 2.0 you can specify what QGIS should do when it starts: `New Project` (legacy behaviour, starts with a blank project), `Most recent` (when you start QGIS it will load the last project you worked on), `Specific` (always load a specific project when QGIS starts). You can use the project template directory to specify where your template projects should be stored. Any project that you store in that directory will be available for use as a template when invoking the `Project --> New from template` menu.

![image5](images/Screen_Shot_2013-09-12_at_11.23.02_PM.png)
### Novità: variabili d'ambiente di sistema
Current system environment variables can now be viewed and many configured within the application Options dialog. Useful for platforms, such as Mac, where a GUI application does not necessarily inherit the user\'s shell environment. Also useful for setting/viewing environment variables for the external tool sets controlled by the processing toolbox, e.g. SAGA, GRASS; and, for turning on debugging output for specific sections of the source code.

![image6](images/changelog-2.0_sys-env-options.png)
### Novità: scale di zoom definite dall'utente
A listing of zoom scales can now be configured for the application and optionally overridden per project. The list will show up in the `Scale` popup combo box in the main window status bar, allowing for quick access to known scales for efficiently viewing and working with the current data sources. Defined scales can be exported to an XML file that can be imported into other projects or another QGIS application.

![image7](images/changelog-2.0_predefined-scales.png)
## Browser
### Novità: miglioramenti nel panello del browser
- Le directory possono venir filtrate da caratteri jolly o da espressioni regolari
- New `Project home` (parent directory of current project)
- View `Properties` of the selected directory in a dialog
- Choose which directories to `Fast scan`
- Choose to `Add a directory` directly to `Favourites` via filesystem browse dialog
- New `/Volumes` on Mac (hidden directory for access to external drives)
- New `OWS` group (collation of available map server connections)
- Open a second browser (`View -> Panels -> Browser (2)`) for drag-n-drop interactions between browser panels
- Icone ora ordinati per tipo gruppo (file system, database, server di mappe)
- Layer `Properties` now have better visual layout

![image8](images/changelog-2.0_browser.png)
## Sorgenti Dati
### Caratteristica: revisione fornitore dati raster
The raster data provider system has been completely overhauled. One of the best new features stemming from this work is the ability to \'Layer -\> Save As\...\' to save any raster layer as a new layer. In the process you can clip, resample, and reproject the layer to a new Coordinate Reference System. You can also save a raster layer as a rendered image so if you for example have single band raster that you have applied a colour palette to, you can save the rendered layer out to a georeferenced RGB layer.

![image9](images/Selection_017.png)
### Caratteristica: supporto a Oracle Spatial
QGIS 2.0 adesso include il supporto a Oracle Spatial.

![image10](images/oracle.png)
### Novità: Web Coverage Service
QGIS offre ora il supporto nativo per il Web Coverage Service - il processo per l'aggiunta WCS è simile all'aggiunta di un layer WMS o WFS.
### Novità: 2% di riduzione cumulativa per i raster
Molti  raster hanno un gran numero di valori anomali che si traducono in immagini che hanno un aspetto slavato. QGIS 2.0 intoduce molto più controllo a grana fine sul comportamento rendering di raster, tra cui l'uso di un 2% - il 98% per cento di riduzione cumulativa di default per determinare lo spazio colore per l'immagine. L'immagine qui mostra QGIS 1.8 (a sinistra) rispetto a QGIS 2.0 (a destra) durante il rendering della stessa immagine con le impostazioni predefinite.

![image11](images/Selection_023.png)
### Feature: formato WMS per l'identificazione
è possibile selezionare il formato di identificazione dei risultati per layer WMS se il server supporta formati multipli. I formati supportati sono HTML, feature (GML) e plain text. Se è stato selezionato il formato feature (GML), il risultato è uguale a quello di un vettore, la geometria può essere evidenziata e sia la geometria che gli attributi possono essere copiati e incollati su un altro layer.

![image12](images/wms-identify.png)
### Novità: supporto WMTS 
Il client WMS in QGIS ora supporta WMTS (Web Mapping Tile Service) compresa la selezione dei sub-set di dati quali intervalli di tempo. Quando si aggiunge un layer WMS da un server compatibile, vi verrà chiesto di selezionare l'intervallo di tempo da visualizzare.

![image13](images/Selection_035.png)
## Generale
### Feature: Quantum GIS is now known only as \'QGIS\'
The \'Quantum\' in \'Quantum GIS\' never had any particular significance and the duality of referring to our project as both `Quantum GIS` and `QGIS` caused some confusion. We are streamlining our project and as part of that process we are officially dropping the use of the word `Quantum` - henceforth we will be known only as `QGIS` (spelled with all letters in upper case). We will be updating all our code and publicity material to reflect this.

![image14](images/qgis.png)
## Etichettatura
### Novità: nuovo sistema di etichettatura
The labelling system has been totally overhauled - it now includes many new features such as drop shadows, \'highway shields\', many more data bound options, and various performance enhancements. We are slowly doing away with the \'old labels\' system, although you will still find that functionality available for this release, you should expect that it will disappear in a follow up release.

![image15](images/Layer_labeling_settings_003_1.png)
### Novità: Espressioni in base alle proprietà delle etichette
The full power of normal label and rule expressions can now be used for label properties. Nearly every property can be defined with an expression or field value giving you more control over the label result. Expressions can refer to a field (e.g. set the font size to the value of the field \'font\') or can include more complex logic.

Esempi:
- Carattere
- Dimensione
- Stile
- Dimensione contorno

![image16](images/2013-09-05_09_44_59-qgis-dev-bin.png)
### Caratteristica: il vecchio motore per etichettare è deprecato
Use of the older labelling engine available in QGIS \<= 1.8 is now discouraged (i.e. deprecated), but has not been removed. This is to allow users to migrate existing projects from the old to new labelling engine.

Le seguenti linee guida per lavorare con il motore più vecchio in QGIS 2.0 sono:
- Deprecated labelling tab is removed from vector layer properties dialog for new projects or older opened projects that don\'t use that labelling engine.
- La scheda deprecata rimane attiva per i progetti più vecchi.

La scheda etichettatura deprecata può essere abilitata/disabilitata per il progetto corrente, tramite comandi della console Python, ad esempio:

    >>> QgsProject.instance().writeEntry('DeprecatedLabels', '/Enabled', True | False)
    # or
    >>> QgsProject.instance().removeEntry('DeprecatedLabels', '/')
    
**NOTA**: C'è una probabilità molto elevata che il motore di etichettatura deprecato sarà completamente rimosso prima della prossima versione stabile di QGIS. Si prega di migrare i vecchi progetti.

![image17](images/changelog-2.0_labels-deprecated.png)
## Legenda Layer
### Novità per la legenda e opzioni
- Numero totale di geometrie in un vettore e per simbolo
- I vettori in modalità modifica abilitata ora hanno una penna rossa per indicare modifiche (non salvate).
- Il vettore attivo è ora sottolineato, nel caso di selezioni multi vettore o quando non c'è nessuna selezione.
- Facendo clic in uno spazio vuoto ora cancella la selezione
- `Right-clicks` are now treated as `left-clicks` prior to showing the contextual menu, allowing for one click instead of two
- I gruppi e i layer possono essere opzionalmente scritti in un carattere grassetto
- Le icone di anteprima per i raster possono essere disabilitate, per migliorare le prestazioni.

![image18](images/changelog-2.0_visual-options.png)
### Novità: duplica una mappa esistente
È possibile duplicare vettori e raster selezionati nella legenda. È come importare di nuovo la stessa origine dati, come un layer separato, e copiare gli attributi ed incollare stile e simbologia.

![image19](images/changelog-2.0_dup-layer_1.png)
### Novità: editing multi layer
L'utente può ora selezionare più layer e, se qualcuno di questi sono vettori in modalità di modifica, scegliere di salvarli o annullare eventuali modifiche non salvate. L'utente può anche scegliere di applicare tali azioni attraverso tutti i livelli, indipendentemente dalla selezione.

![image20](images/changelog-2.0_current-edits.png)
## Compositore di Mappe
### Novità: oggetti mappa HTML
ora puoi aggiungere elementi HTML nella tua mappa.

![image21](images/Composer_1_006.png)
### Novità: supporto multi pagina
Una singola finestra di compositore può contenere più di una pagina.

![image22](images/2013-09-08_22_31_33-Composer_1.png)
### Novità: espressioni nelle etichette del compositore
The composer label item in 1.8 was quite limited and only allowed a single token \$CURRENT_DATE to be used. In 2.0 full expression support has been added too greater power and control of the final labels.

Un'etichetta con un'espressione come:

    This was printed on: [% format_date( $now, 'dd.MM.yyyy')%]
    
sarà valutata al momento della stampa per generare:

    This was printed on: 06.09.2013
    
When atlas generation is enabled the currently active features\' attribute values will also be accessible in the expressions allowing such things as:

    Asset ID [% "ID" %] and the Tree Type is [% "TreeType" %]
    
![image23](images/2013-09-06_09_53_30-Composer_1.png)
### Novità: snapping automatico delle linee
L'allineamento degli oggetti è fondamentale per la creazione di mappe. Lo snap automatico delle linee è stato aggiunto per facilitare l'allineamento di oggetti, semplicemente trascinando e rilasciando.

![image24](images/2013-09-05_10_05_01-Composer_1.png)
### Novità: linee di snapping manuali
Qualche volta si ha bisogno di allineare oggetti su una certa distanza nel compositore. Con le nuove linee di snapping puoi aggiungere queste linee con le quali puoi allineare gli oggetti utilizzando una distanza comune.

![image25](images/2013-09-05_10_09_41-Composer_1.png)
### Novità: stampa in serie di mappe
Il compositore ora include la stampa in serie di mappe, mediante l'atlante.

![image26](images/Picture1.png)
### Novità: panoramica automatica nella cornice della mappa
Necessità di mostrare l'attuale area della mappa principale in una piccola finestra di panoramica? Ora è possibile. La cornice  contiene ora la possibilità di mostrare l'estensione della mappa e si aggiornerà quando viene spostata.

![image27](images/Picture1_1.png)
### Novità: modalità fusione layer
Layer blending makes it possible to combine layers in new and exciting ways. While in older versions, all you could do was to make the layer transparent, you can now choose between much more advanced options such as \"multiply\", \"darken only\", and many more.

Blending can be used in the normal map view as well as in print composer. For a short tutorial on how to use blending in print composer to make the most out of background images, see [\"Vintage map design using QGIS\"](http://anitagraser.com/2013/07/29/vintage-map-design-using-qgis/).

![image28](images/printcomposer_blending_1.png)
### Novità: supporto alle etichette HTML
Il supporto HTML è stato aggiunto al compositore di stampe per dare ancora maggiore controllo sulle mappe finali. Le etichette HTML hanno pieno supporto stili CSS fogli, html, javascript.

![image29](images/html.png)
### Novità: legenda del compositore multi colonna
La legenda del compositore ora supporta più colonne. Ad esempio, un singolo strato di simbolo può essere visualizzata come singola voce o con titolo di livello (come in 1.8), i simboli da più layer successivi possono essere raggruppati in un unico gruppo (titoli nascosti) ecc conteggi delle funzioni possono essere aggiunti alle etichette.

![image30](images/multicolumn-legend.png)
### Novità: aggiornamenti alla gestione del compositore di stampa 
I miglioramenti alla gestione sono:
- Il nome del compositore può ora essere definita al momento della creazione, eventualmente scegliendo di partire da altri nomi di compositori
- I compositori ora possono essere duplicati
- `New from Template` and from `Specific` (in Composer Manager) creates a composer from a template located anywhere on the filesystem
- Il progetto principale ora può essere salvato direttamente dallo spazio di lavoro del compositore
- Tutte le azioni di gestione compositore ora accessibili direttamente dallo spazio di lavoro

![image31](images/changelog-2.0_composer-mngmnt.png)
## Plugin
### Novità: gestore plugin migliorato
In QGIS 1.x gestione plugins era un po' confuso con due interfacce - uno per gestire i plugin già installati e uno per il recupero plugin python da un unico repository. In QGIS 2.0 introduciamo un nuovo, unificato, gestore dei plugin che fornisce un punto per il download, attivazione/disattivazione e generalmente per la gestione dei plugin.

![image32](images/Plugin_Manager_024.png)
## Programmabilità
### Novità: nuova console python
La nuova console di Python vi dà ancora più potenza. Ora il supporto all'autocompletamento, evidenziazione della sintassi, le impostazioni dei font regolabili. L'editor di codice lato consente una più facile scrivere grossi blocchi di codice con la possibilità di aprire ed eseguire qualsiasi file Python nella sessione QGIS.

![image33](images/pyconsole.png)
### Novità: nuove funzioni per le espressioni
Con il motore di espressione utilizzato sempre di più, per consentire operazioni come le etichette a base di espressione e simbolo, molte altre funzioni sono state aggiunte al costruttore espressione e sono tutti accessibili anche con il generatore di espressioni. Tutte le funzioni sono corredate di aiuto e di guide per l'uso.

![image34](images/2013-09-06_09_10_49-Expression_based_label.png)
### Novità: funzioni di espressioni personalizzate
If the expression engine doesn\'t have the function that you need. Not to worry. New functions can be added via a plugin using a simple Python API.

![image35](images/2013-09-06_09_14_58-untitled__routing_-_Sublime_Text_UNREGISTERED.png)
### Novità: nuova API python più pulita
L'API Python è stata rinnovata per consentire un'esperienza più ordinata, pulita di programmazione. L'API QGIS 2.0 utilizza SIP V2 che elimina il disordinato toString(), toint() che erano necessarie quando si lavora con i valori. I tipi sono ora trasformati in tipi Python nativi. Gli attributi sono ora accessibili utilizzando una semplice chiave di ricerca, non più l'indice di ricerca e attributi mappe.

    >>> feature['mycolumn'] = 10
    >>> feature['mycolumn']
    10
    
È stata migliorata la lettura delle geometrie da un layer per poter abilitare il multithreading in futuro.

    for feature in layer.getFeatures():
           print feature['mycolumn']
    
![image36](images/2013-09-06_09_28_08-untitled__routing_-_Sublime_Text_UNREGISTERED.png)
### Novità: compatibilità del codice con la versione 1.x
As this is a major release, it is not completely API compatible with previous 1.x releases. In most cases porting your code should be fairly straightforward - you can use [this guide](https://github.com/qgis/QGIS/wiki/Python_plugin_API_changes_from_18_to_20) to get started. Please use the developer mailing list if you need further help.

![image37](images/Selection_021.png)
### Novità: macro del progetto Python
Un modulo Python, salvato in un file project.qgs, può essere caricato e hanno funzioni specifiche eseguite sui seguenti eventi del progetto:
- `openProject()`
- `saveProject()`
- `closeProject()`

Le macro possono essere configurate nelle opzioni dell'applicazione.

![image38](images/changelog-2.0_project-macros_w-setttings.png)
## Simbologia
### Novità: Proprietà definite dai dati
La tipologia, dimensione, colore, rotazione e molte altre proprietà del simbolo possono essere definite attraverso le proprietà del vettore.

![image39](images/datadefinedproperties2.png)
### Novità: Gestione simbologia vettore migliorata
La nuova vista del simbolo usa una chiara e pulita struttura ad albero che permette un facile e rapido accesso a tutti i simboli del vettore.

![image40](images/symbollayertree.png)
### Novità: supporto alla trasparenza nei colori
In most places where you select colours, QGIS now allows you to specify the alpha channel (which determins how transparent the colour should be). This allows you to create great looking maps and to hide data easily that you don\'t want users to see.

![image41](images/Layer_Properties_-_nat_026_1.png)
### Novità: controllo del colore per i raster
QGIS 2.0 allows you to precisely control exactly how you\'d like raster layers to appear. You now have complete control over the brightness, contrast and saturation of raster layers. There\'s even options to allow display of rasters in grayscale or by colorising with a specified color.

![image42](images/Layer_Properties_-_blue_marble_032.png)
### Novità: copia della simbologia tra vettori
Its now super easy to copy symbology from one layer to another layer. If you are working with several similar layer, you can simply `right-click` on one layer, choose `Copy Style` from the context menu and then `right-click` on another layer and choose `Paste-Style`.

![image43](images/Selection_034.png)
### Novità: Salva stile nel database
Se stai usando un database vettoriale, puoi immagazzinare lo stile dei layer direttamente nel database. Questo permette di condividere layer stilizzati in ambienti enterpirse o multi-utente.

![image44](images/Selection_037.png)
### Novità: supporto alle scale dei colori
Colour ramps are now available in many places in QGIS symbology settings and QGIS ships with a rich, extensible set of colour ramps. You can also design your own and many [cpt-city](http://soliton.vm.bytemark.co.uk/pub/cpt-city/) themes are included in QGIS now \'out of the box\'. Color ramps even have full support for transparency!

![image45](images/Selection_038.png)
### Novità: stili di default per i layer
Now QGIS lets you control how new layers will be drawn when they do not have an existing `.qml` style defined. You can also set the default transparency level for new layers and whether symbols should have random colours assigned to them.

![image46](images/Screen_Shot_2013-09-12_at_11.18.52_PM.png)
## Interfaccia Utente
### Novità: nuovo tema di icone
We have updated out icon theme to use the \'GIS\' theme which introduces an improved level of consistency and professionalism to the QGIS user interface.

![image47](images/Selection_001_1.png)
### Novità: schede e menu raggruppabili
Abbiamo standardizzato il layout delle schede e in molte finestre di dialogo molti menu sono ora raggruppabili in modo da facilitare la navigazione e migliorare la visualizzazione.

![image48](images/Selection_005.png)
### Novità: modifiche leggere
In many cases we want to tell you something, but we don\'t want to stop your work or get in your way. With the new notification system QGIS can let you know about important information via a yellow message bar that appears at the top of the map canvas but doesn\'t force you to deal with it if you are busy doing something else. Programmers can create these notification (e.g. from a plugin) too using our python API.

![image49](images/Selection_030.png)
### Novità: carattere predefinito per l'applicazione e foglio di stile QT
The system font used for the application\'s user interface can now be set. Any C++ or Python plugin that is a child of the QGIS GUI application or has copied/applied the application\'s GUI stylesheet can inherit its styling, which is useful for GUI fixes across platforms and when using custom QGIS Qt widgets, like `QgsCollapsibleGroupBox`.

Il foglio di stile personalizzato di QGIS è accessibile, dopo aver seguito (all'interno di PyQGIS)::

    qgis.utils.iface.mainWindow().styleSheet()
    
![image50](images/changelog-2.0_app-font.png)
### Novità: finestre di dialogo del selettore di colori 
Every color chooser button throughout the interface has been updated to give visual feedback on whether the current color has a transparent, or \'alpha,\' component. The color chooser opened by the new color buttons will now always be the default for the operating system. If the user has `Use live-updating color chooser dialogs` checked under `Options -> General -> Application`, any change in the color chooser will immediately be shown in the color button and for any item currently being edited, where applicable.

![image51](images/changelog-2.0_live-color-dlgs.png)
### Novità: annotazioni SVG
Con QGIS 2.0 è ora possibile aggiungere annotazioni SVG alla mappa - sia appuntato ad un luogo determinato o in una posizione relativa sulla mappa.

![image52](images/Screen_Shot_2013-09-14_at_9.39.11_AM.png)
### Novità: costruttore di moduli con drag e drop
QGIS 2.0 supports a great new system for creating data entry forms. With the drag and drop form designer you can create smart looking forms with tabs to group common fields together. Now it is much easier to control the data entry experience for your users.

![image53](images/Screen_Shot_2013-09-14_at_2.17.27_PM.png)
### Novità: strumento predefenito
Se sei un utente di operazioni sui vettori (piccoli compiti che possono essere eseguite quando si fa clic su una funzione), amerete il nuovo strumento di azione sulla barra degli strumenti. Con esso è possibile selezionare un'azione attiva e quindi fare clic su vostre caratteristiche per richiamare l'azione.

![image54](images/Screen_Shot_2013-09-14_at_2.27.03_PM.png)

{{<content-end >}}
