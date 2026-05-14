---
HasBanner: false
archived: true
date: 2014-05-01
draft: false
featured: false
section: projekt
sidebar: true
thumbnail: images/india_pune1.png
title: Použití python konzole k přípravě offline mapy z WMS (stahovač dlaždic)
type: case-study

---
{{<content-start >}}
# Použití python konzole k přípravě offline mapy z WMS (stahovač dlaždic)
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>May 01, 2014</span>
</p>

Tato studie vysvětluje, jak připravit offline mapy z WMS/WFS nebo jakékoli mapy načtené v zobrazení mapy QGIS stažením dlaždic pomocí skriptu v python konzoli. Skript také vygeneruje mozaiku všech dlaždic pro další použití.

Přístup k rastrovým/vektorovým mapám prostřednictvím služby Web Mapping Service (WMS) je velmi běžný a efektivní. Má několik výhod, jako je zabezpečení, centralizované a flexibilní styly map. Příkladem jsou mapy Google, Yahoo, Bing, MODIS, Landsat, mapy vydané NASA, NRSC (Indie). Nevýhodou/omezením WMS je, že funguje přes internet nebo intranet. Zejména v terénu během průzkumu nemusí být vždy možné získat připojení k internetu. Také WMS pracuje pomalu ve srovnání s jakýmkoli offline formátem obrázků, jako je GeoTiff, jpg, img atd.
## Použití QGIS
QGIS provides a tool to connect/access any WMS service. WMS connection is based on simple URL and once connection is established map can be seen on QGIS mapview. If we save the map of visible extent from QGIS mapview as jpg (File \> Save as Image) it creates world file which has the geographic coordinate information of particular region E.g. sample.jpg is the map and sample.jpgw have the coordinates. That means the downloaded image is georeferenced. We can download tiles in grid format manually and use later offline. Manual downloading is possible if the area is very small or low resolution images are fine.

<figure>
<img src="../images/india_pune1.png" class="align-left" alt="india_pune1.png" />
<figcaption>QGIS with WMS tiles</figcaption>
</figure>

## Python konzole
A short script was written in "Python Console" with help available on QGIS official website in PyQGIS Developer Cookbook. Script consists of basically 4 components as following,
1. Souřadnice X,Y (vlevo nahoře a vpravo dole) první dlaždice
2. Velikost dlaždice ke stažení (např. 0,001 x 0,001 stupně)
3. Počet dlaždic ke stažení (vypočteno na základě plného rozsahu mapy a velikosti dlaždice)
4. Výstupní adresář pro uložení výstupních dlaždic/souborů

The script works in two simple for loops first which defines the extent of map in QGIS map view and run row/columns. Once the map extent is set then map is loaded in QGIS. The delay of 3 seconds (depends on internet connection) was introduced before saving map as jpg in user defined directory. Once the script is executed all the tiles created in directory can be directly loaded in QGIS or single mosaic is prepared from Raster \> Miscellaneous \> Merge or Build Virtual Raster (Catalog). Both tools generates mosaic but basic difference in Merge creates an image independent of tiles whereas Virtual raster generates a link in all individual tiles (tiles are required).

<figure>
<img src="../images/india_pune2.png" class="align-left" alt="india_pune2.png" />
<figcaption>Python script and directory where tiles are stored</figcaption>
</figure>

Metoda má omezení, že změny v mapě na konci serveru se neprojeví v offline (stažené mapě). V tomto případě uživatel bude muset proces opakovat a vygenerovat novou offline mapu. Druhým omezením je, že offline mapa vytvořená bude ve formátu obrázku; nelze jej použít pro tematické mapování nebo klasifikaci obrázků. S určitým zvláštním úsilím lze některé landuse mapy převést na vektorové s určitou ztrátou dat.
## Rozsah
Vygenerovaná mozaika je čistý obrázek, i když je stažena z tematické mapy (7-8 barev). Pomocí pokročilého nástroje, jako je reklasifikace, vrstvení/skládání pásem lze tento rastr převést na polygonový vektor. WMS má několik požadavků, jako jsou getcapabilities, getmap, getfeatureinfo atd. Pomocí atributu getgeatureinfo lze získat informace pro každý polygon. Skript lze převést na plugin, takže jej bude moci používat kdokoli bez znalosti skriptování.
## Závěr
Výše uvedené zkušenosti ukazují, že QGIS lze používat na jakékoli pokročilé úrovni. Se základními programovacími dovednostmi lze napsat malý skript nebo zásuvný modul, který zlepší kvalitu práce a ušetří čas. V rámci QGIS je přístup k úložišti zásuvných modulů vyvinutých po celém světě tím nejlepším z QGIS. PyQGIS Developer Cookbook je skvělým zdrojem pro psaní skriptů a zpracování rastrových dat je nyní s pomocí nástrojů GDAL mnohem snadné.
## Autoři
K tomuto článku přispěl v květnu 2014 Prashant Kadgi se sídlem v Pune (Indie) a v současnosti pracuje jako konzultant v GIS APP Consultancy Services. Od roku 2009 používá GIS & RS v NRM, lesnictví, e-governance, projektech vývoje softwaru v různých regionech Indie a světa.
- Contact: <kadgiprashant@gmail.com>
- Webové stránky www.gisappco.com (ve výstavbě)

{{<content-end >}}
