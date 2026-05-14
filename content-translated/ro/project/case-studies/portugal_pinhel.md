---
HasBanner: false
archived: false
date: 2015-01-01
draft: false
featured: false
section: proiect
sidebar: true
thumbnail: images/portugal_pinhel1.jpg
title: QGIS și Cartografierea Riscurilor de Incendii Forestiere în Portugalia
type: case-study

---
{{<content-start >}}
# QGIS și Cartografierea Riscurilor de Incendii Forestiere în Portugalia
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>January 01, 2015</span>
</p>

Portugalia a fost afectată de incendii mari, provocând pierderi uriașe, nu doar de mediu, dar și pierderi economice și sociale. Pentru a face față acestui risc, guvernul portughez, prin Autoritatea Națională a Pădurilor (AFN), a decis, în urmă cu câțiva ani, să creeze birouri tehnice alocate autorităților locale care, printre altele, trebuie să pregătească Planuri Municipale de Protecție Împotriva Incendiilor Forestiere și de Răspuns Operațional .

In order to support the elaboration of these documents, the AFN provided technical guides with a methodology for calculating and mapping the Forest Fire Hazard and Risk. Moreover, tutorials have been offered to follow this methodology, using Proprietary Software. However, the acquisition and licensing costs of that software are unaffordable for most of the smaller local administrations and so, it was decided to create and make available a guide with a methodology for developing Hazard and Risk cartography using only Free and Open Source Software \[<http://goo.gl/TSv2E>\].

S-a propus utilizarea următorului set de aplicații: QGIS, GRASS GIS, gvSIG și biblioteci GDAL/OGR. Ghidul descrie toate sarcinile de geoprocesare necesare pentru elaborarea planurilor de protecție împotriva incendiilor forestiere și de răspuns operațional, în conformitate cu metodologia AFN. O mare parte din sarcini au fost dezvoltate cu QGIS, iar analiza spațială în modelul raster a fost dezvoltată cu GRASS. gvSIG s-a utilizat pentru analiza de rețea, cu ajutorul extensiei de analiză de rețea, iar bibliotecile GDAL/OGR au fost folosite pentru transformările între sistemele de referință și coordonate.

După o suită extinsă de teste ale metodologiei, și trei ani de aplicare reală în pregătirea Planului Operațional pentru municipiul Pinhel, se poate spune că alternativele propuse permit înlocuirea, cu multe avantaje, a soft-ului proprietar, care era, înainte, utilizat pentru a efectua sarcinile. Validarea rezultatelor arată că, în ciuda simplității relative a modelului conceptual, capacitatea sa de predicție este chiar bună, și că implementarea modelului în software cu sursă deschisă nu interferează negativ rezultatele, ci dimpotrivă.
> ![](../images/portugal_pinhel1.jpg)

<figure>
<img src="../images/portugal_pinhel2.jpg" class="align-right" alt="portugal_pinhel2.jpg" />
<figcaption>Forest Fire Hazard and Risk Maps of Pinhel, implemented with Open Source Software.</figcaption>
</figure>

Într-o a doua etapă, s-a încercat accelerarea acestui proces, stabilindu-se un flux de lucru care efectuează o gamă largă de activități, aproape fără intervenție umană. Această a doua etapă a constat, în principal, în automatizarea întregii proceduri descrisă în ghidul practic al primei faze. O astfel de automatizare a însemnat o reducere de multe ore de muncă intensă din partea tehnicianului care generează planurile de apărare anuală a pădurilor, la doar câteva minute, în care intervenția umană se limitează la selectarea datelor de intrare și indicarea locului unde se salvează datele de ieșire.

<figure>
<img src="../images/portugal_pinhel3.png" class="align-right" alt="portugal_pinhel3.png" />
<figcaption>Interface of the Sextante Model to calculate the Probability of the Forest Fire Hazard.</figcaption>
</figure>

In furtherance of this second phase, we used the Python version of Sextante software, that works integrated into QGIS and adds a broad set of independent applications (GRASS GIS, SAGA GIS, OTB, R, GDAL/OGR, Pymorph, LASTools, Python scrips, etc..) in a single interface, providing a huge geoprocessing toolbox to QGIS users. Besides the integration of these applications in QGIS, Sextante has a tool for creating models, taking advantage of the modules offered by any of those softwares which aggregates. So, we\'ve created a model to automate the process of producing Forest Fire Hazard and Risk maps, using GRASS, SAGA, fTools and MMQGIS tools.

<figure>
<img src="../images/portugal_pinhel4.png" class="align-right" alt="portugal_pinhel4.png" />
<figcaption>Part of the model developed for automation of the production of cartography for Forest Fire Hazard and Risk.</figcaption>
</figure>

The results obtained so far are very promising, as already can be automatically achieved the creation of the Hazard and Risk Maps \[2\]. Taking into account that the Python version of Sextante is still very recent and is in heavy construction, there are some problems that must be corrected so that the models may be completed, which certainly will happen very soon, given the momentum that Sextante project presents. As future work, we intend to apply, also automatically, the symbology to the results as well as provide the final layouts in QGIS Composer, ready for export and/or print. Upon completion of the second phase and the realization of a sufficient set of tests that can validate the results obtained, it is our intention to provide the model free and openly.
## Concluzii
Alternativele studiate s-au dovedit a fi de enormă calitate, permițând toate operațiunile recomandate în ghidurile tehnice ale pădure Autorității Pădurilor Naționale, în multe feluri, mult mai eficient decât software-ul proprietar. În ceea ce privește ușurința în utilizare, s-a observat că acest tip de software nu este, în nici un fel, mai complex decât software-ul proprietar, necesitând doar cunoștințe mai tehnice despre modelele și algoritmii implementați care, cu toate acestea, permit un grad mai mare de libertate, făcând posibilă explorarea și reglarea fină a modelelor pentru fiecare situație particulară. Procesul de identificare a pericolelor de incendiu și cartografierea riscurilor prin utilizarea, exclusivă, a softului cu sursă deschisă este pe deplin consolidat, după mai mulți ani de testare și aplicare în municipalitatea Pinhel.

Faptul că soft-ul cu sursă deschisă se bazează pe standarde și suportă cele mai multe dintre formatele de date deschise, permite interoperabilitate completă între aplicații, permițând utilizatorului să o aleagă pe cea mai potrivită în fiecare moment. În ciuda opțiunii noastre pentru un set specific de softuri, nimic nu împiedică alegerea oricăreia dintre alternativele existente în gamă largă de propuneri de aplicații geospațiale gratuite și cu sursă deschisă. Cu toate acestea, QGIS se prezintă tot mai mult ca fiind cea mai completă, stabilă și ușor de utilizat soluție FOSS4G, al cărui proiect este mult mai dinamic, cu corectarea rapidă de erori și cu implementarea aproape zilnică de noi plugin-uri care adaugă funcționalități specifice pentru cele mai diverse domenii de activitate .
## Autor
<figure>
<img src="../images/portugal_pinhelaut.png" class="align-left" height="200" alt="portugal_pinhelaut.png" />
<figcaption>Pedro Venâncio</figcaption>
</figure>

Pedro Venâncio, B.Sc. în Geologie, Studii Postuniversitare în software-ul liber și Master în Sisteme Informatice Geografice. A fost cercetător la Centrul de Geofizică al Universității din Coimbra, la Laboratorul Național de Inginerie Civilă și este în prezent responsabil pentru serviciul de Cartografie și Sisteme Informatice Geografice al municipiului Pinhel.

{{<content-end >}}
