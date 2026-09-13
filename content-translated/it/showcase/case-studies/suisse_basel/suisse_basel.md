---
draft: 'true'

---
# QGIS \-\-- an interesting instrument for forestry planning concepts at local and regional level
Almost 35% of Switzerland\'s surface is covered by forests. Changing demands upon the forest and the poor financial situation of forest enterprises in Switzerland led to the development of a new forestry planning concept about fifteen years ago. This concept introduced a clear distinction between planning at the level of the authorities and planning at the level of the owners1. As a new forestry planning office, guaraci works primarily in the region of Basel (Switzerland) on both mentioned planning levels. This case study discusses the use of QGIS at the forest owner level. On this level, a simple, dynamic and compatible geographic information system is required for the establishment of a forest management plan. This plan covers about 1000 ha of forests, will be valid for about 20 years and is implemented by the local forest manager. The area is situated in the region of Basel (see google maps).
## Come viene utilizzato QGIS
Nell'intero processo di pianificazione, QGIS è stato utilizzato per le seguenti quattro compiti:
- Importazione di dati esistenti. Il dato include mappe di sfondo geo-referenziate (\*.tif) insieme ai shapefile di poligoni, linee e punti. Per il gestore della foresta, la visualizzazione di dati tematici esistenti (per esempio, terra e risorse di acqua potabile, zone di protezione della natura) sono importanti per il suo lavoro quotidiano.
- Digitizing. The forestry measurements planned by the forest manager had been digitized. The QGIS digitizing tools with the advanced snapping options are very useful and user friendly. The „delimited text" plugin enabled the import of additional data tables.
- Analisi. Sono stati calcolate aree delle diverse categorie di valutazione. Partendo da alcune delle geometrie lineari, quali binari del treno o strade, sono stati determinate aree di protezione dei boschi con l'aiuto di un buffer.
- Stampa ed esportazione. Il compositore di stampa permette la creazione layout della mappa. La mappa è stata esportata come file PDF e immagini.

![Extract of the forestry measurements map](./images/suisse_basel1.jpg){.align-right}
## Conclusione
QGIS is an interesting tool for small planning offices, such as guaraci, as well as for the forest managers and owners. It can be used in a professional context and the presented output result was appreciated by all parties involved. For the mentioned tasks the present QGIS version 1.4 "Enceladus" offers all necessary GIS tools. The most important qualities of QGIS are the intuitive user interface and the compatibility with different file formats. It is an ideal tool for projects that are on one hand based on existing geographic data and on the other hand require the acquisition of new data. The user-manual is helpful and easy to understand. Both from the technical as well as the financial perspective QGIS is an interesting alternative to other GIS software.
## In prospettiva
I compiti principali di un concetto di pianificazione forestale possono essere risolti con gli strumenti GIS di base citati. Guaraci continuerà ad usare QGIS per la pianificazione forestale a livello del proprietario della foresta. Sulla base delle esperienze con il progetto presentato, QGIS può anche essere raccomandato per i concetti forestali a livello degli enti locali. Progetti più grandi e più complessi con esigenze di analisi dettagliate possono essere gestite dalla combinazione di QGIS con il server di database spaziale Postgis. Le nuove zone di registrazione così come reservates forestali e zone di protezione possono essere facilmente digitalizzati. Noi crediamo che proprietari e gestori forestali possano utilizzare il potenziale di QGIS anche per la loro programmazione annuale, nonché per la documentazione delle loro attività forestali.
## Autore
![Raphael Häner](./images/suisse_baselaut.jpg){.align-left height="200px"}

This article was contributed in June 2010 by Raphael Häner. He is Dipl. Forst Ing. at ETH Zürich, Switzerland and founded his one-man company guaraci in 2009.
