---
draft: 'true'

---
# Folosirea QGIS pentru planificarea urbană în municipiul Montecchio Maggiore, Vicenza, Italia. 
Montecchio Maggiore is a small town in the middle west of Vicenza (about 24.000 population). And as many other italian municipality it manages the town planning; in particular the urban planning and what we call "recovery plan" aka PDR \-\-- Piani Di Recupero. This urbanistic tool is dedicated to the historical area in the center of the town and it requires a specific study: building state of conservation, intended use, particular historical notice via survey and restitution to produce planimetric and prospectus graphics. For this purpose it has used QGIS in addition to Postgresql/Postgis database, PHP code and Libreoffice suite, QCAD (LibreCAD).
## Sarcina
![Workflow Schema](./images/italy_vicenza1.png){.align-right}

O schemă va clarifica fluxul de lucru:

Datele fiecărei construcții au fost preluate prin sondaj, după o programare scrisă. O dată ajunse în birou datele au fost introduse în baza de date PostgreSQL/PostGIS prin formularul PHP folosind browser-ul canonic (Firefox, Iceweasel de asemenea). Apoi forma fiecărei clădiri a fost trasată în QGIS și legată la tabela sondajului prin câmpul cheie id (vedere PostgreSQL/PostGIS).

În același timp, fațadele clădirilor au fost proiectate cu ajutorul QCAD (LibreCAD).

PDR (Planul De Recuperare) trebuie să respecte reguli stricte care impun grafice specifice:
- Stadiul actual
- Starea proiectului
- Utilizarea prevăzută (prezent)
- Utilizarea prevăzută (proiect)
- Tipul de intervenție admis

Pentru fiecare hartă tematică produsă s-au folosit atributele și datele preluate pe timpul studiului (stării actuale) și datele modificate pe parcursul studiului și a fazelor de proiectare.

Thus a photo was linked to every building facilitating the design and analisys in the gis project (using the "action" feature). The SQL tools (pgquery, postgis manager, dbmanager et al.) allowed to obtain very sophisticated query immediately viewable in the map canvas such as: volume calculation split by building intended use, standards area calculation in percentage of the total planning area and other minor queries. All useful items for the design and planning study otherwise not possible without a very strength tool like gis (and QGIS in particular).

![QGIS project with building data viewing](./images/italy_vicenza2.png){.align-right}

În cele din urmă, un raport sintetic pentru fiecare clădire a fost produs cu ajutorul LibreOffice Suite. Raportul constă într-o sinteză însoțită de fotografie, extras de cartografie care localizează clădirea în context și datele situației actuale.

![QGIS print composer for final graphic layout](./images/italy_vicenza3.png){.align-right}
## Concluzii
The strength of QGIS is the very user friendly interface coupled with the several tools it offers. The connection with vary data formats (shape files, spatialite db, postgresql/postgis db,\...) facilitates and increases the interoperability between different worlds. And thus the freedom offered by the free software (QGIS, PHP, Libreoffice, QCAD) stimulates and open new horizons.

În ultimul rând, dar nu mai puțin important: deși am lucrat pe platforme diferite (Windows 7 pe 64 de biți, Windows XP 32 bit, Debian server și Debian client), niciodată nu am întâlnit probleme insurmontabile.
## Autor
![Flavio Rigolon](./images/italy_vicenzaaut.png){.align-left height="200px"}

This article was contributed May 2012 by Flavio Rigolon. He lives in Vicenza (Italy) and works in Montecchio Maggiore municipality as SIT manager. He has migrated almost all the gis data from proprietary to free platform (QGIS, Postgresql/Postgis, Spatialite). He is a member of GFOSS.it (Associazione Italiana per l\'Informazione Geografica Libera) since 2007 and was a member of the GFOSS.it board from 2010 to 2012.
