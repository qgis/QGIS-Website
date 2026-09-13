---
HasBanner: false
archived: true
date: 2013-02-01
draft: false
featured: false
section: проект
sidebar: true
thumbnail: images/usa_missouri1.png
title: Картографування історичних даних герпетології і QGIS (Міссурі, США)
type: case-study

---
{{<content-start >}}
# Картографування історичних даних герпетології і QGIS (Міссурі, США)
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>February 01, 2013</span>
</p>

The Missouri Herpetological Atlas Project (MOHAP) was initiated in 1997 as a result of the desire to obtain and easily update detailed distribution maps for Missouri (United States of America) amphibians and reptiles. A database was established to store all valid localities, including records published in historical literature sources and specimens vouchered from museums. From the database, a series of maps can be produced representing both locality records and \"county records\" for each species.

MOHAP hosts a web site at <http://atlas.moherp.org/> that describes the project in detail and displays a variety of static maps, all produced by QGIS. An atlas, published as a downloadable PDF, is released periodically as a gratis publication in the spirit of open access to scientific research (Daniel, R.E. and B.S. Edmond. 2012. Atlas of Missouri Amphibians and Reptiles for 2011. \<<http://atlas.moherp.org/pubs/atlas11.pdf>\>). Published maps are used by field biologists, land managers, and others to better understand species\' distributions in Missouri.

As of February 2013, the MOHAP database contained 31,495 entries representing the specimens housed in 34 museum collections and cited in 32 historical literature sources; 5,118 documented county records; 6,884 unique localities; and 12,866 unique species / locality combinations. The state\'s herpetofauna consists of 113 species.
## Генерація та експорт статичних карт
Процес створення карт в QGIS починається з завантаження даних з просторової бази даних PostgreSQL/PostGIS. Оскільки карти статичні та призначені як для розміщення в інтернеті, так і для публікації в складі атласу, вони генеруються для кожного виду автоматично за допомогою спеціального плаґіна (мал. 1 та 2)

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

## Підсумки
На початку роботи над MOHAP для зберігання та обробки даних використовувалось декілька комерційних та власницьких інструментів. Починаючи з 2007 р. ми вирішили перевести проект на використання вільного програмного забезпечення. QGIS, разом з PHP, PostgreSQL, PostGIS, Python, та ReportLab, сформували стрижень MOHAP та дозволили повністю відмовитися від власницького програмного забезпечення.

QGIS підтримує роботу з PostgreSQL та дозволяє створювати власні плаґіни на Python, які були необхідні для автоматичної генерації карт. Розгорнута документація дозволила нам дуже швидко автоматизувати процеси. Підтримка співтовариства також знаходиться на високому рівні, сюди ж можна віднести й наявність великої кількості плаґінів.

Хоча ми використовуємо QGIS для вирішення маленької та специфічної задачі, її можливості та підтримка плаґінів дозволяють вирішувати набагато складніші задачі.
## Автор
<figure>
<img src="../images/usa_missouriaut.jpg" class="align-left" height="200" alt="usa_missouriaut.jpg" />
<figcaption>Brian Edmond</figcaption>
</figure>

This article was contributed by Brian Edmond in February 2013. He is a Senior Systems Analyst in Computer Services at Missouri State University. He holds a BS in Wildlife Biology from the University of Missouri and has spent his career in the intergrade zone between biology and technology.

{{<content-end >}}
