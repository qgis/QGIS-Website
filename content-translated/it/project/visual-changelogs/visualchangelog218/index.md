---
HasBanner: false
draft: false
releaseDate: '2016-10-21'
section: progetto
sidebar: true
title: Elenco cambiamenti per QGIS 2.18
type: visual-changelog

---
{{<content-start >}}
# Elenco cambiamenti per QGIS 2.18{#changelog218 }
![image1](images/projects/ac3b0a08203e87505a823b0d8a0895d44489f916.png)

Release date: 2016-10-21

Questa è l'ultima versione della serie 2.x. L'attuale versione a lungo supporto (LTR) resta la 2.14.x. Questa versione fornisce ulteriori miglioramenti rispetto alla versione precedente. La maggior parte dell'attività è attualmente focalizzata sullo sviluppo di QGIS 3.0 che è la nostra versione di generazione successiva, pianificata per la fine del primo quarto del 2017.

**Ringraziamenti**

We would like to thank the developers, documenters, testers and all the many folks out there who volunteer their time and effort (or fund people to do so). From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

QGIS is supported by donors and sponsors. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become and official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

QGIS è un Software Libero e non c'è alcun obbligo di pagare nulla per utilizzarlo - vogliamo infatti incoraggiare le persone di ogni parte del mondo ad usarlo, indipendentemente dalla propria situazione finanziaria o sociale - crediamo che mettere tutti nella condizione di utilizzare gli strumenti decisionali spaziali produrrà una società migliore per tutta l'umanità.

{{<table-of-contents >}}
## Sponsor per QGIS versione 2.18.0
Annualmente riceviamo supporto da diverse organizzazioni che apprezzano il nostro lavoro e che vogliono agevolare il lavoro di sviluppo che coinvolge l'intero progetto. Tutti gli sponsor sono elencati qui sotto.

{{<fund type="changelog" relativeImgPath=true >}}
## Generale
### Novità: Link automatici nello strumento di identificazione
Any `http` or `mailto` links within attribute values will now automatically be converted to clickable links within the identify results panel.

![image58](images/entries/eab95eb0acb92a68edeee71a13ea23d77b88d307.png.400x300_q85_crop.webp)

This feature was developed by [Sandro Mani (Sourcepole)](https://sourcepole.ch/)
### Feature: Mouse wheel over color dialog sliders
In QGIS 2.18 you can now scroll the mouse wheel over any of the sliders within the color picker dialog to increment the value by small amounts. This is a handy shortcut for small tweaks to color components.

![image59](images/entries/ab472e2c8270ba64bee64bbbf8c9f5104edc79de.gif)

This feature was funded by [Nyall Dawson (North Road)](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Feature: Add custom color schemes to color button drop down menu
QGIS 2.18 adds the ability for users to set whether a user created color scheme should show up in the color button drop-down menus. This setting is controlled through the color picker dialog, on the lists tab. Just add a new color scheme, then from the scheme menu tick the new \"show in buttons\" option. It\'s a handy shortcut if you have sets of common palettes and want them to be instantly available through the color menu.

![image60](images/entries/9453954d199c4950d7aecf153b6d5e53f820ff19.PNG.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Simbologia
### Novità: Il selettore del colore è ora integrato nel pannello di stile del layer
In QGIS 2.18, cliccare sul pulsante del colore all'interno del pannello di stile del layer genera l'apertura della finestra di dialogo del selettore del colore all'interno del pannello di stile stesso invece che in una finestra di dialogo separata. Ciò consente una modifica interattiva dei colori con anteprima immediata del risultato.

![image42](images/entries/3af7533f5148810d0c26a221d7acdccaf1d7a835.png.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Etichettatura
### Novità: Supporto alla lista di sostituzione per l'etichettatura
Aggiunge la possibilità di specificare una lista di elementi di testo sostitutivi per definire quali applicare al testo dell'etichetta. Ad es. per abbreviare tipi di strade.

Gli utenti possono esportare e importare liste di elementi sostitutivi da riutilizzare e condividere più facilmente.

![image43](images/entries/a73aec5fad4c5e39800e462bbac6dd2597f98cba.png.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Novità: miglioramento dell'algoritmo di posizionamento dell'etichetta per le linee
La modalità di etichettatura parallela per i vettori di linee è stata notevolmente migliorata con un nuovo algoritmo che evita di posizionare etichette sulle parti irregolari delle geometrie dell'elemento.

![image44](images/entries/5b77d12263e0dabfb0649f27d92188613796f409.png.400x300_q85_crop.webp)

Questa funzionalità è stata finanziata da Andreas Neumann

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Novità: Etichetta i poligoni utilizzando etichette curvate lungo il perimetro
Questa funzionalità aggiunge una nuova modalità per etichettare i poligoni nei casi in cui il perimetro del poligono è etichettato utilizzando l'etichettatura curvata.

![image45](images/entries/c7a28cf09a0f1646210faaae85a56c2209ee15e9.PNG.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Visualizzazione
### Novità: Anteprima delle mattonelle raster (raster WMTS and XYZ)
Nelle versioni precedenti di QGIS, gli utenti dovevano attendere lo scaricamento di tutte le mattonelle di un raster per poter visualizzare la mappa risultante. Tale comportamento è stato corretto e le mattonelle sono mostrate nella mappa non appena sono scaricate, con conseguente miglioramento dell'esperienza utente e riducendo il tempo richiesto prima che qualcosa sia mostrato. Inoltre, le mattonelle precedentemente scaricate con risoluzioni da più basse a più alte possono essere usate per la funzionalità di anteprima nella aree in cui le mattonelle con la corretta risoluzione non sono ancora state scaricate.

![image46](images/entries/007bf6d09a1f67e0c0c4ee71d48081185c0c5c84.gif)

This feature was funded by [Land Information New Zealand](http://www.linz.govt.nz/)

This feature was developed by [Martin Dobias (Lutra Consulting)](http://www.lutraconsulting.co.uk/)
### Novità: Visualizzazione dei raster cancellabile (raster WMS, WMTS, WCS e XYZ)
Questa funzionalità aumenta l'esperienza utente quando si lavora con raster che provengono da server remoti. In passato era necessario attendere fino al completamento dei download per avere la possibilità di ingrandire o spostare la mappa nuovamente, poiché l'interfaccia utente rimaneva congelata nel mentre. Ciò è stato corretto dal fatto che la visualizzazione dei raster può essere cancellata in qualunque momento.

This feature was funded by [Land Information New Zealand](http://www.linz.govt.nz/)

This feature was developed by [Martin Dobias (Lutra Consulting)](http://www.lutraconsulting.co.uk/)
## Gestione Dati
### Novità: Aggiungi flag per copiare solo le geometrie selezionate
Il Plugin Offline Editing è un plugin predefinito offerto da QGIS e ti consente di rendere offline un insieme di dati remoti (ad es. da un database), modificarne i campi, e in seguito sincronizzarlo di nuovo quando torni a lavoro. Ciò estende le possibilità di modifica offline per lavorare soltanto con un sottoinsieme di layer di grosse dimensioni.

![image47](images/entries/ec977674f356d5376d19be49534818a4cc830c64.png.400x300_q85_crop.webp)

Questa funzionalità è stata finanziata da DB Fahrwegdienste GmbH

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch/)
## Moduli e Widget
### Novità: Consenti il controllo delle etichette per widget per singoli widget per la modifica
Allow controlling labels for individual edit widgets in a form. In the drag and drop designer, a double click on an item will allow controlling if the label should be shown for each item individually.

In addition it is possible to configure if the link/unlink buttons are shown in relation reference widget, which is useful to hide in 1:n relations where a child can\'t exist without its parents.

![image48](images/entries/6d827c6b286f137ec9de1d97a15c745764494d0a.png.400x300_q85_crop.webp)

This feature was funded by [Kanton Zug, GIS-Fachstelle](http://geo.zg.ch/)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch/)
### Novità: Visibilità condizionale per schede e caselle di gruppo
This adds a new configuration option to conditionally show or hide tabs and groupboxes in drag and drop designer forms.

Configuration is done via a double click in the designer tree in the fields configuration interface.

An expression can be entered to control the visibility. The expression will be re-evaluated everytime values in the form change and the tab or groupbox shown/hidden accordingly.

![image49](images/entries/8adda1d639ba9b46b15f8a70b38c6cfd407d2515.png.400x300_q85_crop.webp)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch/)
### Feature: Client side default field values
Allows an expression to be set for a vector layer field which is used to evaluate a default value for this field. Default value expressions can utilise properties of the feature which exist at the time of calling, such as digitized geometries. Expression variables can also be used in default value expressions, making it easy to eg insert a user\'s name, the current datetime, project path, etc.

![image50](images/entries/49a9d8a5c38f04d96cf37ad190a97dd4dc4b5025.png.400x300_q85_crop.webp)

Questa funzionalità è stata finanziata da DB Fahrwegdienste GmbH

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Compositore di Mappe
### Feature: True North Arrows
QGIS 2.18 adds support for orienting north arrows in the composer to True North. Previously all arrows were aligned to grid north, which is unsuitable for polar regions or non-north up projections (such as some South African projection systems). Now, you can choose to orient arrows to either grid north or true north. There\'s also an optional offset angle, which can be used to specify a grid convergence to make your arrows orient to magnetic north!

![image51](images/entries/b36b83066c2361e4a9647ee830b55b01a04ce4c5.png.400x300_q85_crop.webp)

This feature was funded by [Norwegian Polar Institute\'s Quantarctica project](http://quantarctica.npolar.no)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Processing
### Feature: Point on surface algorithm
This new algorithm is similar to the centroids algorithm, but where a centroid may fall outside its corresponding feature the \'Point on surface\' algorithm is guaranteed to create a point which is inside the corresponding polygon feature (or touching the corresponding line feature for line layers).

![image52](images/entries/133a854441e2ade7bec91a48e9a1f1d4b1d012ac.png.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Feature: Processing dissolve algorithm accepts multiple fields
The dissolve algorithm now allows you to dissolve based on more than one field value. In previous QGIS versions a dissolve could only group features by a single field value.

![image53](images/entries/a75b372f431c98592bdaccbc0bf4e90654969fa2.PNG.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Feature: Optimised processing clip algorithm
The processing clip algorithm has been optimised for common use scenarios, resulting in dramatic speedups for clipping operations. For example:

**Clipping a roads layer with 1 million lines against 2 polygons**

| **Earlier versions:** 5 mins 30 seconds | **QGIS 2.18:** 10 seconds

**Clipping a 5 million point address layer against 2 polygons**

| **Earlier versions:** 50 minutes | **QGIS 2.18:** 30 seconds

![image54](images/entries/f975cb641b319e952264dc1e706deafdfd2b7496.png.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Feature: Bounding boxes algorithm
This new algorithm calculates the bounding box (envelope) of each feature in the input layer.

![image55](images/entries/398557f0cfe897a227fea70ceef700f9ab048e2d.png.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Feature: Merge connected lines algorithm
This algorithm joins all the connected parts of MultiLineString geometries into single LineString geometries. If any parts of the input MultiLineString geometries are not connected, the resultant geometry will be a MultiLineString containing any lines which could be merged and any non-connected line parts.

![image56](images/entries/7ebf10a71a1c3f28d48a2c19f7ad1f08ca75bf80.PNG.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Feature: Geometry boundary algorithm
This new algorithm returns the closure of the combinatorial boundary of the input geometries (ie the topological boundary of the geometry). For instance, a polygon geometry will have a boundary consisting of the linestrings for each ring in the polygon, and a line geometry will have a boundary consisting of the start and end points of the line. This algorithm is only valid for polygon or line layers.

![image57](images/entries/907b7b5c36af36547f10f33f65e9655a5cbe5a67.png.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Sorgenti Dati
### Feature: Native support of XYZ tile layers
Raster tiles in XYZ format are now natively supported within WMS data providers, allowing users to display basemaps from other sources without requiring third-party plugins like QuickMapServices or OpenLayers anymore.

To add connections to XYZ layers, just open browser dock widget, look for item called \"Tile Server (XYZ)\" and right click it to get a popup menu with \"New connection\" action. You will be asked for URL, in which `{x}`, `{y}`, `{z}` will be replaced by the actual tile numbers according to the current map view. For example, to add OpenStreetMap base map, one may use this URL: `http://c.tile.openstreetmap.org/{z}/{x}/{y}.png`

The data provider also supports encoding of XYZ tile numbers into \"quadkeys\" used by Bing. Simply use `{q}` instead of `{x}`, `{y}` and `{z}` in the URL.

![image61](images/entries/f69a3601e9201e38f9a561d40807512035da2298.gif)

This feature was funded by [Lutra Consulting](http://www.lutraconsulting.co.uk/)

This feature was developed by [Martin Dobias (Lutra Consulting)](http://www.lutraconsulting.co.uk/)
## QGIS Server
### Feature: Possibility to segmentize feature info geometry in server
Necessary for geometries that contain curves (CircularArc, CompoundCurve, CurvePolygon), but the web client (e.g. QGIS Web Client) can\'t handle the display of these geometry types.

This feature can be enabled in the \"OWS server\" tab in the \"Project Properties\" dialogue.

![image62](images/entries/f4b9cf3ba10669b933eb3f3a5c401f675ad76533.png.400x300_q85_crop.webp)

Questa funzionalità è stata finanziata da Andreas Neumann

This feature was developed by [Marco Hugentobler (Sourcepole)](http://www.sourcepole.ch/)
## Plugin
### Feature: DB Manager: Add the ability to update SQL Layer
With this feature the user can update the layer datasource if it\'s based on an SQL request.

This feature was funded by [Ifremer](http://wwz.ifremer.fr)

This feature was developed by [3Liz](http://3liz.com)
## Programmabilità
### Feature: Expose GEOS linear referencing function to QgsGeometry
A new function `QgsGeometry::lineLocatePoint()` has been added for retrieving the distance along a linestring to the nearest position on the linestring to a given point.

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Feature: New PyQGIS classes in 2.18
### New core classes
- [QgsAnnotation](https://qgis.org/api/classQgsAnnotation.html) - an interface for annotation items which are drawn over a map
- [QgsFeedback](https://qgis.org/api/classQgsFeedback.html) - a base class for feedback objects to be used for cancellation of something running in a worker thread
- [QgsOptionalExpression](https://qgis.org/api/classQgsOptionalExpression.html) - an expression with an additional enabled flag

### New GUI classes, Reusable widgets
- [QgsExpressionLineEdit](https://qgis.org/api/classQgsExpressionLineEdit.html) - includes a line edit for entering expressions together with a button to open the expression creation dialog. This widget is designed for use in contexts where no layer fields are available for use in an expression and space is constrained.
- [QgsTabWidget](https://qgis.org/api/classQgsTabWidget.html) - similar to QTabWidget but with additional methods to temporarily hide/show tabs

## Novità: nuove funzioni per il calcolo delle espressioni
QGIS 2.18 adds several new expression functions, including functions for angle/distance interpolation.
- `line_merge`: merges a MultiLineString geometry into connected LineStrings
- `boundary`: returns a geometry\'s topological boundary, ie for polygons this is a MultiLineString representing the polygon\'s rings
- `angle_at_vertex`: returns the average (bisector) angle to a geometry at a specified vertex index
- `distance_to_vertex`: returns distance along geometry to a specified vertex index
- `line_interpolate_angle`: calculates the angle parallel to a geometry at the specified distance along the geometry
- `line_interpolate_point`: returns a point on line at distance
- `line_locate_point`: returns distance along line to nearest line location closest to specified point

Questa funzionalità è stata finanziata da Andreas Neumann

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)

{{<content-end >}}
