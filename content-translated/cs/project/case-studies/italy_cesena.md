---
HasBanner: false
archived: true
date: 2015-10-30
draft: false
featured: false
section: projekt
sidebar: true
thumbnail: images/italy_cesena1.png
title: QGIS k popisu Cesena's Wall
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

ECAMPUS UNIVERSITY byla vytvořena jako online univerzita a uznaná MIUR (Italské ministerstvo školství, univerzity a výzkumu) ministerským výnosem ze dne 30. ledna 2006. Byla vytvořena s cílem poskytnout mladým lidem přístup na univerzitu prostřednictvím své eLearningové platformy. lidé, odborníci, podnikatelé, vedoucí pracovníci a obchodní a kulturní činitelé s cílem přispět na trh práce. Centrála, známá také jako Milan International Campus nebo Campus of Novedrate, se nachází v bývalém školicím středisku IBM v Novedrate (Como, Itálie), v kampusu v klidné zelené Brianze.

Univerzita má 5 virtuálních fakult: inženýrství, ekonomie, psychologie, umění, právo. HISTORICKÉ MAPY A PROJEKT QGIS Městská zeď charakterizuje město Cesena. Svým tvarem štíra odděluje historické centrum od nově zóny.

Historické kartografické dokumenty popisují její vývoj a její zániky. Program QGIS mi umožňuje porovnávat různé historické mapy, protože umožňuje přenášet všechny mapy do stejného referenčního systému pomocí georeferenčního pluginu. Jako reference byla použita otevřená vrstva Google Satellite a otevřená vrstva Open Street Map k odkazování všech historických map na referenční systém EPSG: 3857 (Web Mercator nebo Pseudo Mercator).

QGIS byl základním nástrojem pro vypracování, analýzu, porovnání těchto georeferencovaných map prostřednictvím vektorových vrstev nebo tvarových souborů, ve kterých jsem si zapamatoval všechny prvky map, jako jsou silnice, budovy, parky a zahrady, městské hradby, starobylé opevněné věže a starověké městské brány. Použil jsem bodové, lineární a polygonální vrstvy. Tyto vrstvy jsem porovnával pomocí nástrojů analýzy, výzkumu, geoprocessingu, geometrie a správy dat (obr. 1).

<figure>
<img src="../images/italy_cesena1.png" style="width:100.0%" alt="italy_cesena1.png" />
<figcaption>Fig. 1 Concept Map of the QGIS project</figcaption>
</figure>

Pomocí těchto nástrojů jsem získal informace o:
- The precision of the Leonardo Da Vinci\'s topographic survey, realized in 1502, such as how many points of this survey are correct (Fig. 2);
- The Cesena Wall\'s Development from the Roman Age to the 15th Century;
- The Cesena Wall\'s Demolitions from the 19th Century to the Early 20th Century;
- Morfologické změny městské zdi, jako jsou demolice jejích starověkých opevněných věží a jejich starobylé městské brány;
- The Cesena\'s Urban Progress from the 16th Century to the Present;

<figure>
<img src="../images/italy_cesena2.png" style="width:100.0%" alt="italy_cesena2.png" />
<figcaption>Fig. 2: Openlayer Google Satellite overlapped by the informations recorded in different layers: the present City Wall in black, the Leonardo Da Vinci's topographic survey of the City Wall in orange, the Leonardo Da Vinci's points of survey in yellow and the present ancient City Gates in red.</figcaption>
</figure>

Existuje mnoho nástrojů QGIS a některé z nich jsem použil k vytvoření:
- Odkazy, které spojovaly jednotlivé části lineární vrstvy současné městské zdi s fotografiemi, které představují skutečný stav památkové péče;
- Mapa Ceseny v 19. století očima tiskaře
- 3D model Ceseny s pluginem qgis2threejs (obr. 3);

<figure>
<img src="../images/italy_cesena3.png" style="width:100.0%" alt="italy_cesena3.png" />
<figcaption>Fig. 3: The 3D model of the present City Wall and Cesena's buildings inside and outside the Wall. The ancient fortified towers and the ancient City Gates are indicated.</figcaption>
</figure>

## Závěr
Historické mapy jsou důležitým dokumentem, i když svou přesností nelze srovnávat s přesností skutečného kartografického dokumentu, a jsou velmi sdělným zobrazením i pro ty, kteří nejsou specialisty na geografické zobrazení. QGIS byl jediný prostředek, který mi umožnil využívat číselný obsah historických map podle efektivní a smysluplné reprezentace.
## Bibliografický rejstřík
Historické mapy byly extrahovány:
- \"Costruzione, alterazione e recupero del centro storico di Cesena\", Ballardini, Cantori, Pezzi, Righetti, Tossani, Bruno Ghigi Editore, 1977
- \"La cinta muraria di Cesena\", Pino Montalti, Edizioni Panini, 1986

Historické informace byly získány:
- \"La cartografia in Italia: nuovi metodi e nuovi strumenti dal Settecento ad Oggi\", Andrea Cantile, IGM Firenze, 2007
- \"Lineamenti di storia della cartografia italiana, volume secondo, dal Seicento al Novecento\" Andrea Cantile, Geoweb, 2013
- \"I rilievi cartografici di Leonardo per Cesena ed Urbino contenuti nel manoscritto \'L\' dell\'Istituto di Francia\", Nando De Toni, G. Barbéra Editore, 1965
- \"La città da guerra\", Amelio Fara, Einaudi, 1993
- \"La cartografia dall\'antichità fino al XVIII secolo\", Carlo Monti, Maggioli Editore, 2011

## Autor
Camilla Fabbri has a bachelor\'s degree in Civil and Environmental Engineering. She has developed her dissertation on historical cartography of the Cesena Wall using the QGIS program with the Supervisor Alessandra Borghi, who is the University Teacher of Topography and Theoretical Mechanics of the bachelor\'s degree in Civil and Environmental Engineering in the eCampus University.

{{<content-end >}}
