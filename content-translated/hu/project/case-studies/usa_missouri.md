---
HasBanner: false
archived: true
date: 2013-02-01
draft: false
featured: false
section: projekt
sidebar: true
thumbnail: images/usa_missouri1.png
title: QGIS térképek, történelmi hüllő és kétéltű adatbázis (Missouri, USA)
type: case-study

---
{{<content-start >}}
# QGIS térképek, történelmi hüllő és kétéltű adatbázis (Missouri, USA)
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>February 01, 2013</span>
</p>

The Missouri Herpetological Atlas Project (MOHAP) was initiated in 1997 as a result of the desire to obtain and easily update detailed distribution maps for Missouri (United States of America) amphibians and reptiles. A database was established to store all valid localities, including records published in historical literature sources and specimens vouchered from museums. From the database, a series of maps can be produced representing both locality records and \"county records\" for each species.

MOHAP hosts a web site at <http://atlas.moherp.org/> that describes the project in detail and displays a variety of static maps, all produced by QGIS. An atlas, published as a downloadable PDF, is released periodically as a gratis publication in the spirit of open access to scientific research (Daniel, R.E. and B.S. Edmond. 2012. Atlas of Missouri Amphibians and Reptiles for 2011. \<<http://atlas.moherp.org/pubs/atlas11.pdf>\>). Published maps are used by field biologists, land managers, and others to better understand species\' distributions in Missouri.

As of February 2013, the MOHAP database contained 31,495 entries representing the specimens housed in 34 museum collections and cited in 32 historical literature sources; 5,118 documented county records; 6,884 unique localities; and 12,866 unique species / locality combinations. The state\'s herpetofauna consists of 113 species.
## Statikus térkép készítés és exportálás
A QGIS-szel történő térképgeneráláshoz szükséges adatok egy PostgreSQL adatbázisban vannak tárolva, PostGIS térbeli kiterjesztéssel. Mivel a térképek statikus jellegűek és végső soron csak a webes megjelenítést, vagy a nyomtatott atlaszt szolgálják, ezért automatikusan generálhatóak minden egyes fajra egy egyedi QGIS Python bővítménnyel (1. és 2. ábra).

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

## Következtetések
A MOHAP projekt kezdetén számos kereskedelmi szoftver és eszköz volt használatos az adatok tárolásához, feldolgozásához és a térképek készítéséhez. 2007-tel kezdődően a projekt minden egyes részét fokozatosan nyílt forrású alapokra helyeztük. QGIS együtt PHP-val, PostgreSQL/PostGIS-szel, Python és ReportLab adják a projekt nyílt forrású lelkét, melyek hatékonyan biztosítják, hogy a projekt és az összes hozzá tartozó adat szabadon létezzen.

A QGIS natív PostGIS és Python bővítmény támogatása elengedhetetlen volt a térképek automatikus generálásához és exportálásához. A mindenre kiterjedő API dokumentáció és a Python bővítményfejlesztő dokumentáció végig hasznosnak bizonyult a fejlesztés során ahhoz, hogy pontosan azt fejlesszük, amire szükségünk volt. A közösségi támogatás is jónak mondható a nagyszámú közreadott bővítménnyel, melyek mind készek a használatra.

Habár a mi projektünk kis léptékű és specifikus módon használja a QGIS-t, úgy gondolom, hogy  a benne rejlő lehetőségek és a Pythonnal történő kiterjesztés rendkívül használhatóvá teszi nagyobb és komplexebb projektek esetében is.
## Szerző
<figure>
<img src="../images/usa_missouriaut.jpg" class="align-left" height="200" alt="usa_missouriaut.jpg" />
<figcaption>Brian Edmond</figcaption>
</figure>

This article was contributed by Brian Edmond in February 2013. He is a Senior Systems Analyst in Computer Services at Missouri State University. He holds a BS in Wildlife Biology from the University of Missouri and has spent his career in the intergrade zone between biology and technology.

{{<content-end >}}
