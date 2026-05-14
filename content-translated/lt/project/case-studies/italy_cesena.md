---
HasBanner: false
archived: true
date: 2015-10-30
draft: false
featured: false
section: projektą
sidebar: true
thumbnail: images/italy_cesena1.png
title: QGIS Čezenos miesto sienos aprašymui
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

ECAMPUS UNIVERSITETAS buvo sukurtas kaip internetinis Universitetas, kurį pripažįsta MIUR (Italijos Švietimo, Universitetų ir Tyrimų Ministerija) pagal 2006 sausio 30 dekretą. Jo sukūrimo tikslas - teikti prieigą jauniems žmonėms, profesionalams, verslininkams, vadovams, verslo ir kultūros veikėjams prie universiteto per jo eMokymų platformą, taip prisidedant prie darbo rinkos. Buveinė, dar žinoma kaip Milano Tarptautinis Miestelis arba Noverdate Miestelis, yra buvusiame IBM Novedrate mokymų centre (Como, Italija), miestelyje tylioje žalioje Brianzoje.

Universitetas turi 5 virtualius fakultetus: Inžinerijos, Ekonomikos, Psichologijos, Menų ir Teisės. ISTORINIAI ŽEMĖLAPIAI IR QGIS PROJEKTAS Miesto siena charakterizuoja Česenos miestą. Jo skorpiono forma dalina istorinį centrą nuo naujų zonų.

Istoriniai kartografiniai dokumentai aprašo jos raidą ir jos sugriovimus. QGIS programa leidžia man lyginti skirtingus istorinius žemėlapius, nes leidžia transformuoti visus žemėlapius į tą pačią atskaitos sistemą, naudojant geopririšimo priedą. Google palydovinis ir atviras Open Street Map buvo naudotas kaip atskaitos sluoksnis, pririšant visus istorinius žemėlapius prie atskaitos sistemos EPSG: 3857 (Web Merkatorius arba Pseugo Merkatorius).

QGIS buvo esminis įrankis šių geo-pririštų žemėlapių supratimui, analizei ir lyginimui su vektoriniais duomenimis ar shape failais, kurie padėjo man atsiminti visus žemėlapių elementus, tokius kaip kelius, pastatus, parkus ir sodus, miesto sieną, senuosius įtvirtintus bokštus ir senuosius miesto vartus. Aš naudojau taškinius, linijinius ir poligoninius sluoksnius, lyginau šiuos sluoksnius naudojant analizę, tyrimą, geoapdorojimą, geometrijos ir duomenų valdymo įrankius (1 pav.).

<figure>
<img src="../images/italy_cesena1.png" style="width:100.0%" alt="italy_cesena1.png" />
<figcaption>Fig. 1 Concept Map of the QGIS project</figcaption>
</figure>

Naudojant šiuos įrankius aš gavau informaciją apie:
- The precision of the Leonardo Da Vinci\'s topographic survey, realized in 1502, such as how many points of this survey are correct (Fig. 2);
- The Cesena Wall\'s Development from the Roman Age to the 15th Century;
- The Cesena Wall\'s Demolitions from the 19th Century to the Early 20th Century;
- Morfologinius miesto sienos pasikeitimus, tokius kaip jos senųjų įtvirtintų bokštų ir senų miesto vartų sugriovimus;
- The Cesena\'s Urban Progress from the 16th Century to the Present;

<figure>
<img src="../images/italy_cesena2.png" style="width:100.0%" alt="italy_cesena2.png" />
<figcaption>Fig. 2: Openlayer Google Satellite overlapped by the informations recorded in different layers: the present City Wall in black, the Leonardo Da Vinci's topographic survey of the City Wall in orange, the Leonardo Da Vinci's points of survey in yellow and the present ancient City Gates in red.</figcaption>
</figure>

QGIS turi daug įrankių ir aš panaudojau kelis iš jų, kad sukurčiau:
- Jungtis tarp kiekvienos dabartinės miesto sienos linijinio sluoksnio dalies su nuotraukomis, kurios rodo dabartinę konservavimo būseną;
- Česenos XIXa. žemėlapio spausdinimo maketą;
- Česenos 3D modelį naudojant qgis2threejs priedą (3 pav.);

<figure>
<img src="../images/italy_cesena3.png" style="width:100.0%" alt="italy_cesena3.png" />
<figcaption>Fig. 3: The 3D model of the present City Wall and Cesena's buildings inside and outside the Wall. The ancient fortified towers and the ancient City Gates are indicated.</figcaption>
</figure>

## Išvada
Istoriniai žemėlapiai yra svarbūs dokumentai, net jei jų tikslumo negalima lyginti su šiandienos kartografinių dokumentų tikslumu. Jie labai gerai komunikuoja bei reprezentuoja tiems, kas nėra geografinių reprezentacijų specialistai. QGIS buvo vienintelis būdas, leidžiantis man naudoti skaitmeninį istorinių žemėlapių turinį pagal efektyvią ir prasmingą reprezentaciją.
## Bibliografija
Istoriniai žemėlapiai ištraukti iš:
- \"Costruzione, alterazione e recupero del centro storico di Cesena\", Ballardini, Cantori, Pezzi, Righetti, Tossani, Bruno Ghigi Editore, 1977
- \"La cinta muraria di Cesena\", Pino Montalti, Edizioni Panini, 1986

Istorinė informacija ištraukta iš:
- \"La cartografia in Italia: nuovi metodi e nuovi strumenti dal Settecento ad Oggi\", Andrea Cantile, IGM Firenze, 2007
- \"Lineamenti di storia della cartografia italiana, volume secondo, dal Seicento al Novecento\" Andrea Cantile, Geoweb, 2013
- \"I rilievi cartografici di Leonardo per Cesena ed Urbino contenuti nel manoscritto \'L\' dell\'Istituto di Francia\", Nando De Toni, G. Barbéra Editore, 1965
- \"La città da guerra\", Amelio Fara, Einaudi, 1993
- \"La cartografia dall\'antichità fino al XVIII secolo\", Carlo Monti, Maggioli Editore, 2011

## Autorius
Camilla Fabbri has a bachelor\'s degree in Civil and Environmental Engineering. She has developed her dissertation on historical cartography of the Cesena Wall using the QGIS program with the Supervisor Alessandra Borghi, who is the University Teacher of Topography and Theoretical Mechanics of the bachelor\'s degree in Civil and Environmental Engineering in the eCampus University.

{{<content-end >}}
