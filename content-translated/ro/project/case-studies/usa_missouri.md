---
HasBanner: false
archived: true
date: 2013-02-01
draft: false
featured: false
section: proiect
sidebar: true
thumbnail: images/usa_missouri1.png
title: Înregistrări Istorice ale Herpetofaunei, Cartografiate în QGIS (în Missouri,
  USA)
type: case-study

---
{{<content-start >}}
# Înregistrări Istorice ale Herpetofaunei, Cartografiate în QGIS (în Missouri, USA)
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>February 01, 2013</span>
</p>

The Missouri Herpetological Atlas Project (MOHAP) was initiated in 1997 as a result of the desire to obtain and easily update detailed distribution maps for Missouri (United States of America) amphibians and reptiles. A database was established to store all valid localities, including records published in historical literature sources and specimens vouchered from museums. From the database, a series of maps can be produced representing both locality records and \"county records\" for each species.

MOHAP hosts a web site at <http://atlas.moherp.org/> that describes the project in detail and displays a variety of static maps, all produced by QGIS. An atlas, published as a downloadable PDF, is released periodically as a gratis publication in the spirit of open access to scientific research (Daniel, R.E. and B.S. Edmond. 2012. Atlas of Missouri Amphibians and Reptiles for 2011. \<<http://atlas.moherp.org/pubs/atlas11.pdf>\>). Published maps are used by field biologists, land managers, and others to better understand species\' distributions in Missouri.

As of February 2013, the MOHAP database contained 31,495 entries representing the specimens housed in 34 museum collections and cited in 32 historical literature sources; 5,118 documented county records; 6,884 unique localities; and 12,866 unique species / locality combinations. The state\'s herpetofauna consists of 113 species.
## Generarea și exportul hărților statice
Procesul de creare a hărților cu QGIS începe cu datele stocate în mai multe tabele PostgreSQL, având activată extensia spațială PostGIS. Deoarece hărțile sunt statice și, în cele din urmă, destinate să fie expuse pe web sau într-un atlas imprimat, acestea sunt generate automat pentru fiecare specie, folosind un  plugin QGIS scris în Python (Figurile 1,2).

<figure>
<img src="../images/usa_missouri1.png" class="align-right" alt="usa_missouri1.png" />
<figcaption>Custom map generation and export user interface, maps are generated and exported in a batch process.</figcaption>
</figure>

The final species maps have a clean and professional appearance (Figure 3). To better understand species\' distributions, a series of base maps are also created and labelled (Figure 4). Because of the way styles are managed within each data layer, the base map layers can also be incorporated into a set of species maps with little extra effort.

<figure>
<img src="../images/usa_missouri2.png" class="align-right" alt="usa_missouri2.png" />
<figcaption>Maps are displayed as static images.</figcaption>
</figure>

<figure>
<img src="../images/usa_missouri3.png" class="align-right" alt="usa_missouri3.png" />
<figcaption>Labelled Level III Ecoregion map for Missouri and surrounding states.</figcaption>
</figure>

## Concluzii
La începutul proiectului MOHAP, mai multe instrumente comerciale și proprietare au fost folosite pentru a stoca și procesa datele si pentru a produce hărți pentru publicare. Începând cu 2007, am decis orientarea tuturor aspectelor proiectului înspre aplicațiile cu sursă deschisă. QGIS alături de PHP, PostgreSQL, PostGIS, Python și ReportLab, formează fundamentul MOHAP, care permite proiectului și datelor să coexiste fără complicațiile soft-ului proprietar.

QGIS conține suport nativ pentru PostGIS și o arhitectură de plugin-uri Python, care au fost esențiale în automatizarea generării și exportului hărții. Documentația API vastă a fost utilizată, alături de ghidul de dezvoltare a plugin-urilor, pentru a crea exact ceea ce este necesar pentru automatizare. Sprijinul comunității este, de asemenea, foarte bun și include o gamă foarte mare de plugin-uri partajate, gata de utilizare.

Deși am folosit QGIS doar într-un mod specific, capacitățile sale și extensibilitatea dată de Python sunt arhisuficiente pentru a aborda proiecte mai mari și mai complexe.
## Autor
<figure>
<img src="../images/usa_missouriaut.jpg" class="align-left" height="200" alt="usa_missouriaut.jpg" />
<figcaption>Brian Edmond</figcaption>
</figure>

This article was contributed by Brian Edmond in February 2013. He is a Senior Systems Analyst in Computer Services at Missouri State University. He holds a BS in Wildlife Biology from the University of Missouri and has spent his career in the intergrade zone between biology and technology.

{{<content-end >}}
