---
HasBanner: false
archived: true
date: 2009-05-01
draft: false
featured: false
section: projekt
sidebar: true
thumbnail: images/suisse_solothurn1.png
title: QGIS ve vládním stacku FOSSGIS kantonu Solothurn ve Švýcarsku
type: case-study

---
{{<content-start >}}
# QGIS ve vládním stacku FOSSGIS kantonu Solothurn ve Švýcarsku
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>May 01, 2009</span>
</p>

![](../images/suisse_solothurn1.png)

Kanton Solothurn poskytuje služby a infrastrukturu 250 000 obyvatel Solothurnu. V roce 2001 se zemský parlament rozhodl přejít z Windows na Linux. Motivací byla nezávislost na jednom konkrétním dodavateli, podpora svobodného podnikání a snížení nákladů na licence. V důsledku toho začalo oddělení SO!GIS kantonu Solothurn zajišťovat požadavky GIS pro více než 3500 zaměstnanců pomocí strategie FOSSGIS.

Prvním krokem bylo zavedení UMN MapServeru a vytvoření klienta SO!MAP, který nabízí snadno použitelného klienta WebGIS pro všech 3500 zaměstnanců. Druhým krokem byla migrace všech našich geoprostorových dat ze Shapefiles do prostorového databázového stroje PostGIS. Zavedení bylo velmi úspěšné, ale chyběl snadno použitelný desktopový GIS.

Po vyhodnocení různých desktopových GIS jsme se rozhodli použít QGIS ve spojení s GRASS a nahradit ESRI ArcInfo a ArcView3 v roce 2006.

K rozhodnutí vedly následující aspekty:
- Due to our use of desktop GIS in a Linux Terminal Server environment, Java wasn\'t an option.
- Projekt OSGeo - organizace
- Grafické rozhraní přeložené do němčiny
- Dokumentace psaná v německém jazyce
- Aktivní vývojář (Marco Hugentobler) poblíž Solothurnu ve Švýcarsku.
- Mohli bychom uzavřít smlouvu s Marcem Hugentoblerem, aby implementoval chybějící funkce, jako je digitalizace a skládání map.
- Vývoj aplikací a zásuvných modulů v jazyce Python
- Rostoucí komunita uživatelů
- Velmi aktivní vývojářská komunita
- Nezávislost na jediném operačním systému

## Kde používáme QGIS
Na rozdíl od interaktivních map, které nabízí UMN MapServer, musí desktopový GIS nabízet flexibilní pohled na geoprostorová data Solothurnu. Desktopový GIS QGIS využívá ke své každodenní práci více než 50 uživatelů. Mnozí z nich však nejsou odborníky na GIS. Chtějí vizualizovat a/nebo zachycovat geoprostorová data pomocí intuitivního uživatelského rozhraní.

One of the most important Desktop GIS issues is the question: \"How do I get the information from the PostGIS geodata repository I need?\". Since our end users are unfamiliar with data models and the underlying structures of our spatial database, offering the users a raw connection to the PostGIS DB was not an option. We have a metadata database that stores the descriptions of all production data called \'SO!DATA\'.

SO!DATA obsahuje lidsky čitelný soupis datových modelů a uživatelé, kteří nejsou odborníky na GIS, mohou tuto databázi použít k vyhledání potřebných informací.

<figure>
<img src="../images/suisse_solothurn2.png" class="align-right" alt="suisse_solothurn2.png" />
<figcaption>"SO!GIS Layer" plugin developed at the Canton of Solothurn</figcaption>
</figure>

To remove the need for end users to interact directly with PostGIS connections and table selection dialogs, a plugin has been developed in python. The plugin is called \"SO!GIS Layer\" (see Figure 1). The plugin connects to the SO!GIS PostGIS repository, gets the information of all published geospatial data layers from SO!DATA and offers the user a GUI to find the data layers they need. With this infrastructure in place, our users are happy —— they can prepare for geoprocessing, editing and map composing in an individual way.

<figure>
<img src="../images/suisse_solothurn3.png" class="align-right" alt="suisse_solothurn3.png" />
<figcaption>"SO!GIS Suche" plugin developed at the Canton of Solothurn</figcaption>
</figure>

Another required QGIS plugin we created is called \'SO!GIS Suche\'. This provides the possibility to search for locations like townships, addresses or cadastral parcels (see Figure 2). As a result the user is able to navigate very easily to an area of interest.

At the moment many other plugins are under development. These will support data manipulation, analysis or mapping for different projects. Our in-development plugins cover topics such as nature reserves, soil conservation, cadastral data verification, crisis management, abandoned sites and so on.
## Závěr
Today we can say that using QGIS was the right decision for us. QGIS offers most of the features requested by our users. The Canton of Solothurn subcontracts the creation of features that QGIS lacks to commercial support providers. With PyQgis and PyQt there are excellent options for easy in-house application development based on QGIS. One huge benefit is the unlimited number of installations. Everyone who needs to use QGIS can use it without any limitations. To push the development of QGIS the Canton of Solothurn has invested approximately \$30,000 into QGIS every year since 2007. This is much more efficient and target-oriented than the payment of support into the black box of our former software provider. Apart from using FOSSGIS, the Canton of Solothurn also provides public geodata free of charge via the SO!ONLINE web portal.
## Autor
<figure>
<img src="../images/suisse_solothurnaut.jpg" class="align-left" height="200" alt="suisse_solothurnaut.jpg" />
<figcaption>Horst Düster</figcaption>
</figure>

Do tohoto článku přispěl v květnu 2009 Dr. Horst Düster. Je koordinátorem GIS na oddělení geoinformací v kantonu Solothurn ve Švýcarsku.

{{<content-end >}}
