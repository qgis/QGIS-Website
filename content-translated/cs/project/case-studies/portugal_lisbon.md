---
HasBanner: false
archived: true
date: 2012-01-01
draft: false
featured: false
section: projekt
sidebar: true
thumbnail: images/portugal_lisbon1.jpg
title: Využití QGIS k mapování oblastí s vysokou biodiverzitou a ekosystémovými službami
  (HABEaS)
type: case-study

---
{{<content-start >}}
# Využití QGIS k mapování oblastí s vysokou biodiverzitou a ekosystémovými službami (HABEaS)
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>January 01, 2012</span>
</p>

HABEaS —— Hotspot Areas for Biodiversity and Ecosystem Services is an online geographic information system (WebGIS) that was created by the [Centre for Applied Ecology](http://www.isa.utl.pt/ceabn/content/2/123/homepage) ([Instituto Superior de Agronomia](http://www.isa.utl.pt/home/), Technical University of Lisbon), Worldwide Fund for Nature (WWF) and Faunalia.

Hlavním cílem této platformy je poskytnout volný přístup k nejrůznějším údajům o biologické rozmanitosti a ekosystémových službách v povodí Středozemního moře, které byly rozptýleny v řadě veřejných i soukromých subjektů. V současné době pokrývá HABEaS WebGIS jižní část Portugalska, ale do konce roku 2012/začátku roku 2013 bude rozšířen na sever Portugalska a také na kanton Tuzla v Bosně a Hercegovině. V dlouhodobém horizontu chceme tento nástroj rozšířit na celou středomořskou pánev.

![](../images/portugal_lisbon1.jpg)

Since the main goal of this tool is to promote free and easy access to information on biodiversity and ecosystem services we decided to use only free and open source software, that any person or entity can use regardless of their location or financial constraints. The website where HABEaS WebGIS is hosted on a server that runs Debian Linux and was developed with Drupal CMS. PostgreSQL/PostGIS was used to store the data and QGIS was used to process and analyze the GIS that we obtained from several entities. We used both QGIS\'s native tools but also GRASS GIS and SAGA GIS tools through the GRASS plugin and SEXTANTE Toolbox.

![](../images/portugal_lisbon2.jpg)

Geografické informace obsažené v systému HABEaS využil také WWF k podpoře identifikace lesů s vysokou ochranářskou hodnotou (HCVF) na jihu Portugalska, což je povinný krok pro vlastníky půdy, kteří chtějí, aby jejich lesy získaly certifikaci FSC (Forest Stewardship Council).

![](../images/portugal_lisbon3.jpg)

Abychom zjistili, které ochranné hodnoty se vyskytují v každé nemovitosti, použili jsme program SEXTANTE Modeller k vytvoření skriptu, který protíná všechny vrstvy HABEaS s hranicemi nemovitosti. Pomocí stejného nástroje jsme také mohli vytvořit skript, který automaticky vypočítá množství uhlíku, které je v současné době uloženo v každé nemovitosti.

![](../images/portugal_lisbon4.jpg)
## Závěry
QGIS se snadno používá a má velmi výkonné možnosti geoprocessingu. Integrace nástrojů GRASS GIS a SAGA GIS prostřednictvím SEXTANTE Toolbox nám umožnila provádět řadu složitých prostorových analýz a jejich pipeline pomocí SEXTANTE Modeler. Bylo také velmi snadné vytvářet vysoce kvalitní mapy pomocí nového nástroje Print Composer a exportovat je ve formátu SVG pro další úpravy pomocí programu Inkscape, což je výkonný open source vektorový grafický editor.

In general, our experience with QGIS has been very positive, the software runs smoothly and the community is very active and supportive. Reported bugs are usually resolved shortly after being reported by users and QGIS developers are always willing to listen to "end user\'s" needs and suggestions.
## Autor
<figure>
<img src="../images/portugal_lisbonaut.jpg" class="align-left" height="200" alt="portugal_lisbonaut.jpg" />
<figcaption>Filipe Dias</figcaption>
</figure>

Filipe Dias je doktorandem Centra aplikované ekologie (Instituto Superior de Agronomia, Techinical University of Lisbon) a konzultantem Středomořského programu Světového fondu na ochranu přírody (WWF).

{{<content-end >}}
