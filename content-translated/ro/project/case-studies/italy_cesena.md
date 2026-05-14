---
HasBanner: false
archived: true
date: 2015-10-30
draft: false
featured: false
section: proiect
sidebar: true
thumbnail: images/italy_cesena1.png
title: Folosirea QGIS la descrierea Zidului Cetății din Cesena
type: case-study

---
{{<content-start >}}
# QGIS to describe the Cesena\'s Wall
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>October 30, 2015</span>
</p>

Universitatea ECAMPUS a fost creată ca universitate on-line prin Decretul Ministerial din 30 ianuarie 2006, fiind recunoscută de către MIUR (Ministerul Italian al Educației, Universităților și Cercetării). Scopul principal constă în oferirea accesului la universitate, prin intermediul propriei platforme de eLearning, tinerilor, profesioniștilor, antreprenorilor, directorilor, oamenilor de afaceri și oamenilor de cultură, contribuind astfel la piața forței de muncă. Sediul central, cunoscut și sub numele de Milan International Campus, sau Campusul din Novedrate, este situat în fostul centru de formare IBM Novedrate (Como, Italia), într-o zonă liniștită din înverzita Brianza.

Universitatea are 5 facultăți virtuale: Inginerie, Economie, Psihologie, Arte, Drept. Hărțile istorice și proiectul QGIS. Zidul cetății caracterizează orașul Cesena. Forma sa de scorpion desparte centrul istoric de zona nouă.

Documentele cartografice istorice îi descriu evoluția și distrugerile suferite de-a lungul timpului. Programul QGIS permite compararea diverselor hărți, întrucât permite transferarea tuturor hărților în același sistem de referință, cu ajutorul plugin-ului de georeferențiere. Pentru toate hărțile istorice s-au folosit ca referință straturile publice Google Satellite și Open Street Map, având Sistemul de Referință EPSG:3857 (Web Mercator sau Pseudo Mercator).

QGIS a avut o contribuție fundamentală la elaborarea, analizarea și compararea hărților georeferențiate, în ale căror straturi vectoriale care am introdus drumurile, clădirile, parcurile și grădinile, Zidul Cetății, turnurile antice fortificate și Porțile Vechi ale orașului. Am folosit straturi de tip punct, line sau poligon. Straturile au fost comparate prin intermediul instrumentelor de analiză, cercetare, geoprocesare, și a celor de management a geometriei și a datelor (Fig. 1).

<figure>
<img src="../images/italy_cesena1.png" style="width:100.0%" alt="italy_cesena1.png" />
<figcaption>Fig. 1 Concept Map of the QGIS project</figcaption>
</figure>

Cu ajutorul acestor instrumente, am obținut informații despre:
- The precision of the Leonardo Da Vinci\'s topographic survey, realized in 1502, such as how many points of this survey are correct (Fig. 2);
- The Cesena Wall\'s Development from the Roman Age to the 15th Century;
- The Cesena Wall\'s Demolitions from the 19th Century to the Early 20th Century;
- Modificările morfologice ale Zidului Orașului, cum ar fi demolările vechilor turnuri fortificate și ale Porților antice ale Orașului;
- The Cesena\'s Urban Progress from the 16th Century to the Present;

<figure>
<img src="../images/italy_cesena2.png" style="width:100.0%" alt="italy_cesena2.png" />
<figcaption>Fig. 2: Openlayer Google Satellite overlapped by the informations recorded in different layers: the present City Wall in black, the Leonardo Da Vinci's topographic survey of the City Wall in orange, the Leonardo Da Vinci's points of survey in yellow and the present ancient City Gates in red.</figcaption>
</figure>

Din multitudinea instrumentelor QGIS, le-am folosit pe cele necesare pentru a crea:
- Legături care conectează fiecare secțiune a stratului liniar al Zidului actual al Orașului cu fotografiile care prezintă actuala stare de conservare;
- O hartă a Cesenei din secolul al 19-lea, realizată cu ajutorul Compozitorului de hărți;
- Un model 3D al Cesenei, realizat cu ajutorul plugin-ului qgis2threejs (Fig. 3);

<figure>
<img src="../images/italy_cesena3.png" style="width:100.0%" alt="italy_cesena3.png" />
<figcaption>Fig. 3: The 3D model of the present City Wall and Cesena's buildings inside and outside the Wall. The ancient fortified towers and the ancient City Gates are indicated.</figcaption>
</figure>

## Concluzii
Hărțile istorice au o mare importanță, chiar dacă precizia lor nu poate fi comparată cu precizia documentelor cartografice actuale, ele fiind ilustrări deosebit de comunicative chiar și față de cei care nu sunt specialiști în reprezentări geografice. QGIS a fost singurul mijloc care mi-a permis să folosesc informația numerică prezentă în hărțile istorice, conferindu-i acesteia o reprezentare eficientă și plină de înțeles.
## Index Bibliografic
Hărțile istorice au fost extrase din:
- \"Costruzione, alterazione e recupero del centro storico di Cesena\", Ballardini, Cantori, Pezzi, Righetti, Tossani, Bruno Ghigi Editore, 1977
- \"La cinta muraria di Cesena\", Pino Montalti, Edizioni Panini, 1986

Informațiile istorice au fost extrase din:
- \"La cartografia in Italia: nuovi metodi e nuovi strumenti dal Settecento ad Oggi\", Andrea Cantile, IGM Firenze, 2007
- \"Lineamenti di storia della cartografia italiana, volume secondo, dal Seicento al Novecento\" Andrea Cantile, Geoweb, 2013
- \"I rilievi cartografici di Leonardo per Cesena ed Urbino contenuti nel manoscritto \'L\' dell\'Istituto di Francia\", Nando De Toni, G. Barbéra Editore, 1965
- \"La città da guerra\", Amelio Fara, Einaudi, 1993
- \"La cartografia dall\'antichità fino al XVIII secolo\", Carlo Monti, Maggioli Editore, 2011

## Autor
Camilla Fabbri has a bachelor\'s degree in Civil and Environmental Engineering. She has developed her dissertation on historical cartography of the Cesena Wall using the QGIS program with the Supervisor Alessandra Borghi, who is the University Teacher of Topography and Theoretical Mechanics of the bachelor\'s degree in Civil and Environmental Engineering in the eCampus University.

{{<content-end >}}
