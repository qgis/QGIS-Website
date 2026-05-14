---
draft: 'true'

---
# Usare QGIS per la pianificazione urbanistica nel Comune di Montecchio Maggiore, Vicenza, Italia
Montecchio Maggiore is a small town in the middle west of Vicenza (about 24.000 population). And as many other italian municipality it manages the town planning; in particular the urban planning and what we call "recovery plan" aka PDR \-\-- Piani Di Recupero. This urbanistic tool is dedicated to the historical area in the center of the town and it requires a specific study: building state of conservation, intended use, particular historical notice via survey and restitution to produce planimetric and prospectus graphics. For this purpose it has used QGIS in addition to Postgresql/Postgis database, PHP code and Libreoffice suite, QCAD (LibreCAD).
## L'obiettivo
![Workflow Schema](./images/italy_vicenza1.png){.align-right}

Un diagramma chiarirà il flusso di lavoro:

Ogni edificio è stato visionato attraverso un rilievo in campo  e schedato su un modulo cartaceo. Una volta in ufficio, i dati sono stati inseriti all'interno di un database database PostgreSQL/PostGIS attraverso un modulo PHP, utilizzando un comune browser web (Firefox o Iceweasel). In un secondo momento, la geometria di ogni edificio è stata disegnata utilizzando QGIS, ed è stata collegata alla tabella del rilievo attraverso il campo "id" (vista di PostgreSQL/PostGIS).

Nello stesso tempo, sono state restituite le facciate degli edifici utilizzando QCAD (LibreCAD).

I Piani di Recupero (PDR) dovevano seguire regole ben precise che richiedevano disegni specifici:
- Stato dell'arte
- Stato di progetto
- Destinazione d'uso (attuale)
- Destinazione d'uso (di progetto)
- Tipo di intervento consentito

Per ogni tematismo sono state prodotte mappe usandoi dati e attributi recuperati durante l'indagine (per lo stato attuale) e dati modificati durante la fase di studio e progettazione.

Thus a photo was linked to every building facilitating the design and analisys in the gis project (using the "action" feature). The SQL tools (pgquery, postgis manager, dbmanager et al.) allowed to obtain very sophisticated query immediately viewable in the map canvas such as: volume calculation split by building intended use, standards area calculation in percentage of the total planning area and other minor queries. All useful items for the design and planning study otherwise not possible without a very strength tool like gis (and QGIS in particular).

![QGIS project with building data viewing](./images/italy_vicenza2.png){.align-right}

Infine, è stato prodotto un report di sintesi per ciascun edificio utilizzando la suite LibreOffice. Il report consiste in una scheda riepilogativa con fotografie, estratto di mappa con evidenziato l'edificio all'interno del suo contesto e i dati dello stato dell'arte dello stesso.

![QGIS print composer for final graphic layout](./images/italy_vicenza3.png){.align-right}
## Conclusione
The strength of QGIS is the very user friendly interface coupled with the several tools it offers. The connection with vary data formats (shape files, spatialite db, postgresql/postgis db,\...) facilitates and increases the interoperability between different worlds. And thus the freedom offered by the free software (QGIS, PHP, Libreoffice, QCAD) stimulates and open new horizons.

Ultimo, ma non per importanza: abbiamo lavorato su diverse piattaforme (Windows 7 64 bit, Windows xp 32 bit, Debian server e client) ma non abbiamo mai incontrato problemi insormontabili.
## Autore
![Flavio Rigolon](./images/italy_vicenzaaut.png){.align-left height="200px"}

This article was contributed May 2012 by Flavio Rigolon. He lives in Vicenza (Italy) and works in Montecchio Maggiore municipality as SIT manager. He has migrated almost all the gis data from proprietary to free platform (QGIS, Postgresql/Postgis, Spatialite). He is a member of GFOSS.it (Associazione Italiana per l\'Informazione Geografica Libera) since 2007 and was a member of the GFOSS.it board from 2010 to 2012.
