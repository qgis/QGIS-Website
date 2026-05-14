---
draft: 'true'

---
# L'uso di QGIS nella città di Uster
La città di Uster utilizza QGIS dal 2007. Incoraggiata dalla decisione del Cantone di Soletta di usare QGIS come sostituto di ArcView, la città di Uster ha deciso di fare una prova. La città si è unita allo sforzo per lo sviluppo di QGIS, proponendo e testando nuove funzionalità e sostenendo finanziariamente lo sviluppo. In cambio Uster riceve un software GIS in rapida evoluzione e multi-piattaforma, comprendente un WebGIS sostenuta da una comunità mondiale.

![](./images/suisse_uster1.png){.align-right}

PostGIS / PostgreSQL è usato come database spaziale centrale. Altri database e fonti di dati vengono replicati in PostgreSQL a intervalli regolari, utilizzando strumenti come OGR e FME. In principio QGIS stato utilizzato principalmente come visualizzatore. Il primo utente QGIS era un contadino che aveva il compito di vigilare le dichiarazioni rilasciate da agricoltori locali per ricevere i sussidi agricoli. Più tardi, in QGIS è stato introdotto anche un editor di dati e una piattaforma per la pubblicazione di mappe, insieme con i miglioramenti agli strumenti di editing e al compositore di stampa. Insieme con altri utenti QGIS svizzeri (Solothurn, Thun e CDE (Università di Berna)), coordiniamo e sponsorizziamo i miglioramenti di questi strumenti, e alcuni perfezionamenti neila simbologia, nell'etichettatura automatica, nella gestione degli attributi e dei moduli.

![](./images/suisse_uster2.png){.align-right}

L'amministrazione comunale utilizza anche software commerciale: Autodesk Topobase, per la cattura e la modifica dei dati catastali e delle infrastrutture delle acque reflue, e GE Smallworld per la gestione di gas, acqua e reti elettriche. Tuttavia, questi sono sistemi complessi in uso da parte di personale specializzato. Tutti gli altri progetti di GIS e la visualizzazione di tutti i dati sono gestiti da QGIS.

In the second half of 2010, first tests with QGIS server were carried out. In 2011 we introduced a new WebGIS system based on the QGIS WMS server and GeoExt/OpenLayers as the web client. The main reasons for the decision to use QGIS server were the considerable time savings made possible by re-using the existing QGIS desktop project configurations, rather than having to manage parallel Web project configurations. Additional advantages are the rich set of symbolization and labeling options and the consistent map rendering between the Desktop GIS application and the Web-GIS. The QGIS webclient can be tested and used at <http://gis.uster.ch/>

![](./images/suisse_uster3.png){.align-right}

Oggi, QGIS viene usato per i seguenti progetti GIS:
- visualizzazione dei dati delle acque reflue, l'integrazione di banche dati complementari e l'accesso diretto ai video del canale e protocolli di ispezione
- visualizzazione e la modifica per il monitoraggio e la pianificazione ambientale e urbanistica delle acque reflue e dei sistemi idrologici (in tedesco: Genereller Entwässerungsplan)
- visualizzazione dei dati catastali sotterranee (reti di acque reflue, acqua, gas ed elettricità, in seguito anche di telecomunicazione) (tedesco: Leitungskataster)
- visualizzazione dei catastali e dati di rilievo
- visualizzazione e modifica dell'inventario comunale di siti naturali protetti
- visualizzazione e modifica dei dati di pianificazione urbana e regionale
- visualizzazione e modifica dei dati delle infrastrutture stradali
- visualizzazione delle statistiche generate direttamente dal database di residenti attuali e passati
- progettazione e visualizzazione per la pianificazione energetica (regioni di approvvigionamento del gas, l'uso del calore dalle acque di scarico, in prossimità della superficie di energia geotermica, centrali di riscaldamento a blocchi, ecc)

Inoltre ulteriori progetti sono attualmente in fase di sviluppo.

![](./images/suisse_uster4.png){.align-right}

Nel 2007 non era del tutto chiaro a quale ritmo QGIS sarebbe stato sviluppato e di come si sarebbero evoluti la comunità e il supporto commerciale. Oggi si può affermare che la velocità di sviluppo e le migliorie apportate dalla comunità QGIS superato le nostre aspettative. La comunità e supporto commerciale delle aziende Sourcepole e Norbit è eccellente. C'è una comunicazione diretta con gli sviluppatori, senza essere schermato via da una gestione del prodotto o team di vendita. Gli sviluppatori di queste due società stanno anche portare sviluppatori del progetto QGIS ed avere un'ottima conoscenza della base di codice.

I bug sono spesso risolti entro poche ore o giorni dopo la segnalazione e nuovi sviluppi sono implementati in un breve lasso di tempo. Le nuove caratteristiche possono essere testati immediatamente dopo lo sviluppo e distribuiti agli utenti ogni volta che la qualità è abbastanza buona per l'utente finale. Non c'è bisogno di aspettare per i rilasci software ufficiali. Ci godiamo la libertà di essere in grado di influenzare il progetto e di installare il software su tutti i computer che vogliamo, senza avere a che fare con la gestione delle licenze. Siamo lieti per la futura collaborazione con la comunità QGIS ed i nostri fornitori commerciali per lo sviluppo del progetto QGIS.
## Autore
![Andreas Neumann](./images/suisse_usteraut.jpg){.align-left height="200px"}

Questo articolo è stato scritto nel mese di aprile del 2011 dal Dott. Andreas Neumann. È coordinatore GIS presso la città di Uster, Svizzera.
