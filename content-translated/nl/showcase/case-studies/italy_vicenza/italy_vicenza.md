---
draft: 'true'

---
# QGIS gebruiken voor stedelijke planning in de gemeente Montecchio Maggiore, Vicenza, Italië
Montecchio Maggiore is een kleine stad in het midwesten van Vicenza (ongeveer 24.000 inwoners). Net zoals zo vele andere Italiaanse gemeenten beheert het de planning in de stad; in het bijzonder de ruimtelijke planning en dat wat we het "recovery plan" of PDR \-\-- Piani Di Recupero noemen. Dit stedelijke gereedschap is bedoeld voor de historische gebieden in het centrum van de stad en vereist een speciale studie: status van het gebouw met betrekking tot conservatie, bedoeld gebruik, bijzondere historische vastlegging via onderzoek en restitutie om planimetrische en afbeeldingen voor prospectussen te maken. Voor dit doel heeft het QGIS gebruikt in aanvulling op de database van PostgreSQL/PostGIS, code in PHP en het pakket LibreOffice, QCAD (LibreCAD).
## De taak
![Schema werkstroom](./images/italy_vicenza1.png){.align-right}

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

Een foto werd dus gekoppeld aan elk gebouw, wat het ontwerp en analyse in het GIS-project faciliteerde (met behulp van de mogelijkheid "action"). De gereedschappen voor SQL (pgquery, Postgis manager, dbmanager et al.) maakten het mogelijk zeer uitgebreide query's te verkrijgen die onmiddellijk zichtbaar waren in het kaartvenster, zoals de berekening van het volume gesplitst naar het beoogde gebruik, standaard berekening van het gebied in percentage van het totale gebied voor de planning en andere minder belangrijke query's. Alle nuttige items voor het ontwerp en de studie voor de planning die anders niet mogelijk waren geweest zonder bijzonder krachtige gereedschappen, zoals GIS (en QGIS in het bijzonder).

![Project van QGIS met weergave van gegevens van gebouwen](./images/italy_vicenza2.png){.align-right}

Tenslotte werd een synthese rapport voor elk gebouw geproduceerd met behulp van het pakket LibreOffice. Het rapport bestaat uit een overzichtsschema met foto, uitname van de cartografie die het gebouw in de context lokaliseert en gegevens over de huidige status.

![QGIS printvormgeving voor uiteindelijke grafische lay-out](./images/italy_vicenza3.png){.align-right}
## Conclusie
De kracht van QGIS is de uiterst gebruiksvriendelijke interface, gekoppeld aan de verscheidene gereedschappen die het biedt. De verbinding met verschillende indelingen voor gegevens (shapefiles, SpatiaLite db, PostgreSQL/Postgis db,\...) faciliteert en vergroot de interoperabiliteit tussen verschillende werelden. En dus stimuleert en opent de door de gratis software (QGIS, PHP, LibreOffice, QCAD) geboden vrijheden, nieuwe horizonten.

En tenslotte: we werkten op verschillende platformen (Windows 7 64 bit, Windows xp 32 bit, Debian server en Debian cliënt) maar we kwamen geen onoverkomelijke problemen tegen.
## Auteur
![Flavio Rigolon](./images/italy_vicenzaaut.png){.align-left height="200px"}

Dit artikel werd in mei 2012 ingediend door Flavio Rigolon. Hij woont in Vicenza (Italië) en werkt in de gemeente Montecchio Maggiore als SIT-manager. Hij heeft bijna alle GIS-gegevens gemigreerd van merkgebonden naar het vrije platform (QGIS, Postgresql/Postgis, Spatialite). Hij is lid van GFOSS.it (Associazione Italiana per l\'Informazione Geografica Libera) sinds 2007 en was lid van de raad van bestuur van GFOSS.it van 2010 tot en met 2012.
