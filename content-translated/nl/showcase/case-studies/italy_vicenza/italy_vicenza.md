---
draft: 'true'

---
# QGIS gebruiken voor stedelijke planning in de gemeente Montecchio Maggiore, Vicenza, Italië
Montecchio Maggiore is a small town in the middle west of Vicenza (about 24.000 population). And as many other italian municipality it manages the town planning; in particular the urban planning and what we call "recovery plan" aka PDR \-\-- Piani Di Recupero. This urbanistic tool is dedicated to the historical area in the center of the town and it requires a specific study: building state of conservation, intended use, particular historical notice via survey and restitution to produce planimetric and prospectus graphics. For this purpose it has used QGIS in addition to Postgresql/Postgis database, PHP code and Libreoffice suite, QCAD (LibreCAD).
## De taak
![Workflow Schema](./images/italy_vicenza1.png){.align-right}

Een schema zal de werkstroom verhelderen:

Alle gegevens van een gebouw werden onderzocht en opgeschreven. Eenmaal op kantoor werden de gegevens ingevoerd in de database van Postgresql/Postgis via een formulier in PHP met behulp van canonical webbrowser (Firefox, ook Iceweasel). Op een tweede tijdstip werd de vorm van elk gebouw getekend met QGIS en gekoppeld aan de tabel met onderzoeksgegevens via het sleutelveld ID (weergave PostgreSQL/Postgis).

Tegelijkertijd werden de façades van de gebouwen ontworpen met behulp van QCAD (LibreCAD).

De PDR (piani di recupero) moest strikte regels volgen die specifieke afbeeldingen vergen:
- Huidige status
- Projectstatus
- Beoogd gebruik (momenteel)
- Beoogd gebruik (project)
- Type toegepaste interventie

Voor elk gebouw werden grafische thematische kaarten gemaakt met behulp van de gedurende het onderzoek verkregen attributen en gegevens (voor de huidige status) en gegevens werden aangepast gedurende de studie- en ontwerpfase.

Thus a photo was linked to every building facilitating the design and analisys in the gis project (using the "action" feature). The SQL tools (pgquery, postgis manager, dbmanager et al.) allowed to obtain very sophisticated query immediately viewable in the map canvas such as: volume calculation split by building intended use, standards area calculation in percentage of the total planning area and other minor queries. All useful items for the design and planning study otherwise not possible without a very strength tool like gis (and QGIS in particular).

![QGIS project with building data viewing](./images/italy_vicenza2.png){.align-right}

Tenslotte werd een synthese rapport voor elk gebouw geproduceerd met behulp van het pakket LibreOffice. Het rapport bestaat uit een overzichtsschema met foto, uitname van de cartografie die het gebouw in de context lokaliseert en gegevens over de huidige status.

![QGIS print composer for final graphic layout](./images/italy_vicenza3.png){.align-right}
## Conclusie
The strength of QGIS is the very user friendly interface coupled with the several tools it offers. The connection with vary data formats (shape files, spatialite db, postgresql/postgis db,\...) facilitates and increases the interoperability between different worlds. And thus the freedom offered by the free software (QGIS, PHP, Libreoffice, QCAD) stimulates and open new horizons.

En tenslotte: we werkten op verschillende platformen (Windows 7 64 bit, Windows xp 32 bit, Debian server en Debian cliënt) maar we kwamen geen onoverkomelijke problemen tegen.
## Auteur
![Flavio Rigolon](./images/italy_vicenzaaut.png){.align-left height="200px"}

This article was contributed May 2012 by Flavio Rigolon. He lives in Vicenza (Italy) and works in Montecchio Maggiore municipality as SIT manager. He has migrated almost all the gis data from proprietary to free platform (QGIS, Postgresql/Postgis, Spatialite). He is a member of GFOSS.it (Associazione Italiana per l\'Informazione Geografica Libera) since 2007 and was a member of the GFOSS.it board from 2010 to 2012.
