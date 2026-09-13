---
draft: 'true'

---
# Použití QGIS pro územní plánování v obci Montecchio Maggiore, Vicenza, Itálie
Montecchio Maggiore is a small town in the middle west of Vicenza (about 24.000 population). And as many other italian municipality it manages the town planning; in particular the urban planning and what we call "recovery plan" aka PDR \-\-- Piani Di Recupero. This urbanistic tool is dedicated to the historical area in the center of the town and it requires a specific study: building state of conservation, intended use, particular historical notice via survey and restitution to produce planimetric and prospectus graphics. For this purpose it has used QGIS in addition to Postgresql/Postgis database, PHP code and Libreoffice suite, QCAD (LibreCAD).
## Úkol
![Workflow Schema](./images/italy_vicenza1.png){.align-right}

Schéma objasní pracovní postup:

Všechna data budovy byla získána pomocí průzkumu a zapsána do papírového plánu. Jakmile jsme byli v kanceláři, data byla vložena do databáze Postgresql/Postgis přes PHP formulář pomocí kanonického webového prohlížeče (Firefox, Iceweasel také). Ve druhém okamžiku byl pomocí QGIS nakreslen tvar každé budovy a propojen s přehledovou tabulkou pomocí pole id key (PostgreSQL/Postgis pohled).

Současně byly fasády budov navrženy pomocí QCAD (LibreCAD).

PDR (piani di recupero) musí dodržovat přísná pravidla, která vyžadují specifickou grafiku:
- Současný stav
- Projektovaný stav
- Zamýšlené použití (současnost)
- Zamýšlené použití (projekt)
- Typ zásahu připuštěn

Ke každému byly vytvořeny grafické tematické mapy s využitím atributů a dat získaných během průzkumu (pro současný stav) a dat upravených v průběhu studie a návrhu.

Thus a photo was linked to every building facilitating the design and analisys in the gis project (using the "action" feature). The SQL tools (pgquery, postgis manager, dbmanager et al.) allowed to obtain very sophisticated query immediately viewable in the map canvas such as: volume calculation split by building intended use, standards area calculation in percentage of the total planning area and other minor queries. All useful items for the design and planning study otherwise not possible without a very strength tool like gis (and QGIS in particular).

![QGIS project with building data viewing](./images/italy_vicenza2.png){.align-right}

Nakonec byla vytvořena syntetická zpráva pro každou budovu pomocí sady libreoffice. Zpráva se skládá z harmonogramu shrnutí s fotografií, kartografickým výpisem, který lokalizuje stavbu v soutěži a údaji o současném stavu.

![QGIS print composer for final graphic layout](./images/italy_vicenza3.png){.align-right}
## Závěr
The strength of QGIS is the very user friendly interface coupled with the several tools it offers. The connection with vary data formats (shape files, spatialite db, postgresql/postgis db,\...) facilitates and increases the interoperability between different worlds. And thus the freedom offered by the free software (QGIS, PHP, Libreoffice, QCAD) stimulates and open new horizons.

A v neposlední řadě: pracovali jsme na jiné platformě (Windows 7 64 bit, Windows xp 32 bit, Debian server a Debian klient), ale nikdy jsme nenarazili na nepřekonatelné problémy.
## Autor
![Flavio Rigolon](./images/italy_vicenzaaut.png){.align-left height="200px"}

This article was contributed May 2012 by Flavio Rigolon. He lives in Vicenza (Italy) and works in Montecchio Maggiore municipality as SIT manager. He has migrated almost all the gis data from proprietary to free platform (QGIS, Postgresql/Postgis, Spatialite). He is a member of GFOSS.it (Associazione Italiana per l\'Informazione Geografica Libera) since 2007 and was a member of the GFOSS.it board from 2010 to 2012.
