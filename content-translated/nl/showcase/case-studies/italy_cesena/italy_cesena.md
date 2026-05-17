---
draft: 'true'

---
# QGIS om de Muur van Cesena te beschrijven
De ECAMPUS UNIVERSITY werd gemaakt als een online iniversiteit en erkend door de MIUR (Italian Ministry of Education, University and Research) bij ministerieel decreet van 30 januari 2006. Het werd gevormd met als doel om aan jonge mensen, professionals, ondernemers,uitvoerenden, zakenmensen en culturele actoren toegang tot de universiteit te verschaffen via zijn platform voor e-Learning platform om bij te dragen  aan de arbeidsmarkt. Het hoofdkwartier, ook bekend als Milan International Campus, of Campus of Novedrate, is gesitueerd in het voormalige leercentrum van IBM in Novedrate (Como, Italy), op een campus in de rustige groene Brianza.

De universiteit heeft 5 virtuele faculteiten: bouwkunde, economie, psychologie, kunst, rechten. De historische kaarten en het project van QGIS. De stadswal karakteriseert de stad Cesena. De vorm van een schorpioen scheidt het historische centrum van het nieuwe deel.

De historische cartografische documenten beschrijven zijn evolutie en zijn verval. Het programma QGIS stelde mij in staat de verschillende historische kaarten met elkaar te vergelijken, omdat het het mogelijk maakt alle kaarten over te zetten naar hetzelfde ReferentieSysteem, met de plug-in Georeferencing. Als verwijzing zijn de open laag van Google Satellite en de open laag OpenStreetMap gebruikt om alle historische kaarten over te zetten naar het ReferentieSysteem EPSG: 3857 (Web Mercator of Pseudo Mercator).

QGIS was een fundamenteel gereedschap om deze kaarten met geoverwijzingen te lezen, te analyseren en te vergelijken met de vectorlagen of shapefiles, waarin alle elementen van de kaarten waren opgeslagen, zoals wegen, gebouwen, parken en tuinen, de stadsmuur, de oude gefortificeerde torens en de oude stadspoorten. Ik gebruikte punten, lineaire en polygoonlagen. Ik vergeleek deze lagen door middel van gereedschappen voor analyses, onderzoek, geoverwerking, geometrie en gegevensbeheer (Fig. 1).

![Fig. 1 Concept Map of the QGIS project](./images/italy_cesena1.png){width="100.0%"}

Met behulp van die gereedschappen vergaarde in informatie over:
- De precisie van het topografische onderzoek van Leonardo Da Vinci, gerealiseerd in 1502, zoals hoeveel punten van zijn onderzoek juist waren (Afb. 2);
- De ontwikkeling van de muur van Cesena van de Romeinse tijd tot aan de 15e eeuw;
- Het verval van de muur van Cesena vanaf de 19e eeuw tot aan het begin van de 20e eeuw;
- De morfologische wijzigingen van de stadsmuur, zoals het verval van zijn oude geforitficeerde torens en zijn oude stadspoorten;
- De stedelijke vooruitgang van Cesena vanaf de 16e eeuw tot heden;

![Fig. 2: Openlayer Google Satellite overlapped by the informations recorded in different layers: the present City Wall in black, the Leonardo Da Vinci\'s topographic survey of the City Wall in orange, the Leonardo Da Vinci\'s points of survey in yellow and the present ancient City Gates in red.](./images/italy_cesena2.png){width="100.0%"}

Er zijn heel veel gereedschappen in QGIS en ik gebruikte sommige daarvan om te maken:
- Koppelingen die elk deel van de lineaire laag van de huidige stadsmuur verbonden met foto's, die de feitelijke staat van conservatie weergeven;
- Een kaart van Cesena in de 19e eeuw vanuit Printvormgeving;
- Een 3D-model van Cesena met de plug-in qgis2threejs (Fig. 3);

![Fig. 3: The 3D model of the present City Wall and Cesena\'s buildings inside and outside the Wall. The ancient fortified towers and the ancient City Gates are indicated.](./images/italy_cesena3.png){width="100.0%"}
## Conclusie
De historische kaarten zijn belangrijke documenten zelfs als de precisie ervan niet kan worden vergeleken met de precisie van het actuele cartografische document, en zij zijn ook zeer communicatieve weergaven voor hen die geen specialisten zijn op het gebied van geografische weergaven. QGIS was het enige middel dat mij in staat stelde de numerieke inhoud van de historische kaarten te gebruiken voor een effectieve en betekenisvolle weergave.
## Bibliografische index
De historische kaarten zijn afkomstig uit:
- \"Costruzione, alterazione e recupero del centro storico di Cesena\", Ballardini, Cantori, Pezzi, Righetti, Tossani, Bruno Ghigi Editore, 1977
- \"La cinta muraria di Cesena\", Pino Montalti, Edizioni Panini, 1986

De historische informatie is afkomstig uit:
- \"La cartografia in Italia: nuovi metodi e nuovi strumenti dal Settecento ad Oggi\", Andrea Cantile, IGM Firenze, 2007
- \"Lineamenti di storia della cartografia italiana, volume secondo, dal Seicento al Novecento\" Andrea Cantile, Geoweb, 2013
- \"I rilievi cartografici di Leonardo per Cesena ed Urbino contenuti nel manoscritto \'L\' dell\'Istituto di Francia\", Nando De Toni, G. Barbéra Editore, 1965
- \"La città da guerra\", Amelio Fara, Einaudi, 1993
- \"La cartografia dall\'antichità fino al XVIII secolo\", Carlo Monti, Maggioli Editore, 2011

## Auteur
Camilla Fabbri is een bachelor in Civil and Environmental Engineering. Zij heeft haar dissertatie gebaseerd op de historische cartografie van de muur van Cesena met behulp van het programma QGIS, met als supervisor Alessandra Borghi, die de University Teacher of Topography and Theoretical Mechanics van de bachelors in Civil and Environmental Engineering op de eCampus University is.
