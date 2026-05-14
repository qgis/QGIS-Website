---
HasBanner: false
archived: true
date: 2009-05-01
draft: false
featured: false
section: progetto
sidebar: true
thumbnail: images/suisse_solothurn1.png
title: QGIS nell'ambiente governativo FOSSGIS del Canton Soletta in Svizzera.
type: case-study

---
{{<content-start >}}
# QGIS nell'ambiente governativo FOSSGIS del Canton Soletta in Svizzera.
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>May 01, 2009</span>
</p>

![](../images/suisse_solothurn1.png)

Il Canton Soletta fornisce servizi e infrastrutture a 250.000 cittadini. Nel 2001 il Parlamento cantonale ha deciso di migrare da Windows a Linux. Le motivazioni erano quelle di essere indipendenti da un particolare fornitore, per favorire la libera impresa, e di ridurre i costi di licenza. Come risultato, il reparto SO!GIS del Cantone ha iniziato a fornire i requisiti per un GIS a più di 3500 dipendenti, con una strategia FOSSGIS.

Il primo passo che abbiamo fatto è stato l'introduzione di UMN MapServer e la creazione di un client SO!MAP, che offre un WebGIS facile da usare per tutti i 3500 dipendenti. Il secondo passo è stato quello della migrazione di tutti i nostri dati geospaziali da shapefile al database spaziale PostGIS. La migrazione ha avuto molto successo, ma mancava un software GIS facile da usare sul desktop. 

Dopo una valutazione di diversi software desktop GIS, abbiamo scelto QGIS in unione con GRASS, sostituendo ESRI ArcInfo e ArcView3 nel 2006. 

La decisione è stata presa per i seguenti aspetti
- Due to our use of desktop GIS in a Linux Terminal Server environment, Java wasn\'t an option.
- Progetto gestito e organizzato da OSGeo
- Interfaccia utente in tedesco
- Documentazione in tedesco
- Uno sviluppatore attivo (Marco Hugentobler) vicino a Soletta, in Svizzera.
- Abbiamo potuto contattare Marco Hugentobler, per implementare caratteristiche mancanti, come quelle nella digitalizzazione e nella composizione di mappe.
- Sviluppo di applicazioni e plugin con Python
- Comunità di utenti sempre crescente
- Comunità di sviluppatori molto attiva
- Indipendenza dal sistema operativo

## Dove usiamo QGIS
A differenza delle mappe interattive servite da UMN MapServer, il desktop GIS offre un modo flessibile di gestire i dati geospaziali del Canton Soletta. QGIS è in uso da più di 50 utenti per il loro lavoro quotidiano. Molti di loro non sono esperti di GIS. Vogliono visualizzare e/o catturare i dati geospaziali con un'interfaccia utente intuitiva.

One of the most important Desktop GIS issues is the question: \"How do I get the information from the PostGIS geodata repository I need?\". Since our end users are unfamiliar with data models and the underlying structures of our spatial database, offering the users a raw connection to the PostGIS DB was not an option. We have a metadata database that stores the descriptions of all production data called \'SO!DATA\'.

SO!DATA contiene un inventario leggibile dei modelli di dati e l'utente non esperto è in grado di utilizzare questo database per scoprire le informazioni di cui ha bisogno.

<figure>
<img src="../images/suisse_solothurn2.png" class="align-right" alt="suisse_solothurn2.png" />
<figcaption>"SO!GIS Layer" plugin developed at the Canton of Solothurn</figcaption>
</figure>

To remove the need for end users to interact directly with PostGIS connections and table selection dialogs, a plugin has been developed in python. The plugin is called \"SO!GIS Layer\" (see Figure 1). The plugin connects to the SO!GIS PostGIS repository, gets the information of all published geospatial data layers from SO!DATA and offers the user a GUI to find the data layers they need. With this infrastructure in place, our users are happy —— they can prepare for geoprocessing, editing and map composing in an individual way.

<figure>
<img src="../images/suisse_solothurn3.png" class="align-right" alt="suisse_solothurn3.png" />
<figcaption>"SO!GIS Suche" plugin developed at the Canton of Solothurn</figcaption>
</figure>

Another required QGIS plugin we created is called \'SO!GIS Suche\'. This provides the possibility to search for locations like townships, addresses or cadastral parcels (see Figure 2). As a result the user is able to navigate very easily to an area of interest.

At the moment many other plugins are under development. These will support data manipulation, analysis or mapping for different projects. Our in-development plugins cover topics such as nature reserves, soil conservation, cadastral data verification, crisis management, abandoned sites and so on.
## Conclusione
Today we can say that using QGIS was the right decision for us. QGIS offers most of the features requested by our users. The Canton of Solothurn subcontracts the creation of features that QGIS lacks to commercial support providers. With PyQgis and PyQt there are excellent options for easy in-house application development based on QGIS. One huge benefit is the unlimited number of installations. Everyone who needs to use QGIS can use it without any limitations. To push the development of QGIS the Canton of Solothurn has invested approximately \$30,000 into QGIS every year since 2007. This is much more efficient and target-oriented than the payment of support into the black box of our former software provider. Apart from using FOSSGIS, the Canton of Solothurn also provides public geodata free of charge via the SO!ONLINE web portal.
## Autore
<figure>
<img src="../images/suisse_solothurnaut.jpg" class="align-left" height="200" alt="suisse_solothurnaut.jpg" />
<figcaption>Horst Düster</figcaption>
</figure>

Questo articolo è stato scritto nel mese di maggio 2009 dal Dr. Horst Düster, coordinatore GIS presso il Dipartimento di geoinformazione del Canton Soletta, in Svizzera.

{{<content-end >}}
