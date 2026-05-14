---
HasBanner: false
archived: true
date: 2013-01-01
draft: false
featured: false
section: projekt
sidebar: true
thumbnail: images/canada_brunswick1.jpg
title: Vytvoření mapy Fundy Footpath Trail pomocí QGIS
type: case-study

---
{{<content-start >}}
# Vytvoření mapy Fundy Footpath Trail pomocí QGIS
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>January 01, 2013</span>
</p>

![](../images/canada_brunswick1.jpg)

The Fundy Footpath is a wilderness hiking trail located along the Fundy coast of New Brunswick, Canada. It is a charter member of the [UNESCO Fundy Biosphere Reserve](http://fundy-biosphere.ca/en/about-us/the-reserve) and affiliated with the [NB Trails Council Inc.](http://www.sentiernbtrail.com/) and the Trans Canada Trail. The Footpath takes hikers through the coastal Acadian Forest, home to the world's highest tides, old growth forests, and several rare and unique types of flora and fauna.

Stezku vytvořila, udržuje a propaguje skupina dobrovolníků známá jako Fundy Hiking Trail Association Inc. (FHTA)(1975). Jako nezisková organizace získává FHTA finanční prostředky na svou činnost prodejem průvodců, jejichž součástí je mapa stezky. V roce 2011 jsem oslovil FHTA, abych se přihlásil jako dobrovolník k aktualizaci oficiální mapy stezky. Jako dobrovolník vytvářející mapu pro neziskovou organizaci se mi hodil QGIS jako nástroj pro úpravu dat i pro finální rozvržení mapy. Díky úsilí mému a členů FHTA byla nová oficiální mapa Fundy Footpath, která je součástí průvodce, vytvořena od začátku do konce v QGIS.

<figure>
<img src="../images/canada_brunswick2.jpg" class="align-right" alt="canada_brunswick2.jpg" />
<figcaption>QGIS GPS Tools Plugin for data collection</figcaption>
</figure>

## Projekt
Proces vytváření nové mapy Fundy Footpath pomocí QGIS lze rozdělit do tří různých částí:
- Sběr dat.
- Úprava a příprava dat.
- Tvorba mapy.

Data was collected both with handheld GPS units and from various free data sources. Trail data (e.g. trail centerline, campsite locations, and tidal crossings) was collected with a Garmin GPSMap 60CSX. This data was then transferred from the GPS and to shapefile format in QGIS using the GPS plugin. Free data in vector formats was then obtained from the [Natural Resources Canada (NRCan) CanVec](http://geogratis.cgdi.gc.ca/geogratis/en/product/search.do?id=5460AA9D-54CD-8349-C95E-1A4D03172FDF) website and from [Service New Brunswick (SNB) online](http://www.snb.ca/gdam-igec/e/2900e_1.asp).

<figure>
<img src="../images/canada_brunswick3.jpg" class="align-right" alt="canada_brunswick3.jpg" />
<figcaption>Creation of the footpath map in QGIS</figcaption>
</figure>

K přípravě dat pro použití ve finálním mapovém produktu byly použity následující nástroje v rámci QGIS pro splnění konkrétních úkolů:
- Data získaná pomocí GPS byla vyčištěna pomocí panelu nástrojů pro úpravy.
- Vektorová data získaná z NRCan a SNB byla sloučena dohromady, dotazována a oříznuta pro konečnou oblast mapy pomocí vektorových nástrojů.
- Soubor oddělený čárkou získaný z SNB byl importován do QGIS jako bodová vrstva pomocí zásuvného modulu Add Delimited Text Layer, zásuvný modul Interpolation byl použit k vytvoření výškového rastru, který byl poté použit k vytvoření rastru hillshade a vrstvy výškových kontur pomocí zásuvného modulu GDAL raster tools.

<figure>
<img src="../images/canada_brunswick4.jpg" class="align-right" alt="canada_brunswick4.jpg" />
<figcaption>Footpath map in the Print Composer</figcaption>
</figure>

Once the data required to create the map was assembled and in a usable format the creation of the final map was started. To create the hiking map data was symbolized and labeled with the symbolization properties dialog and labeled with QGIS's very functional label engine. Once labels and symbolization were in place the map composer tool was run to create the layout. It was very easy to add useful map elements such as a custom north arrow and elevation profile in the print composer. Two layouts were created since it was to be a double-sided map. Once both layouts were created they were exported as PDF files and sent to the printers.
## Závěr
The hiking map was printed on heavy-duty waterproof paper, folded and inserted in the back of the new edition of the Fundy Footpath Hiker's Guide Book. QGIS was the best and most functional choice for the creation of this map. Being free software the price was right for a volunteer creating a map for a non-profit organization. But the real advantage of QGIS was that it had all of the functionality and tools required to create a highly useful and detailed hiking map from start to finish. I would highly recommend QGIS to both experienced and beginning GIS users alike.

<figure>
<img src="../images/canada_brunswick5.jpg" class="align-right" alt="canada_brunswick5.jpg" />
<figcaption>The final Fundy Footpath map with accompanying guidebook</figcaption>
</figure>

## Odkazy
- <http://fundy-biosphere.ca/en/about-us/the-reserve>
- <http://www.sentiernbtrail.com>
- <http://www.snb.ca/gdam-igec/e/2900e_1.asp>

## Autor
<figure>
<img src="../images/canada_brunswickaut.jpg" class="align-left" height="200" alt="canada_brunswickaut.jpg" />
<figcaption>Jarrett Totton</figcaption>
</figure>

Tento článek napsal Jarrett Totton v lednu 2013. Jarrett je technolog GIS žijící v kanadské Albertě.

{{<content-end >}}
