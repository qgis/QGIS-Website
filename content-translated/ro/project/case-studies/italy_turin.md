---
HasBanner: false
archived: true
date: 2013-01-01
draft: false
featured: false
section: proiect
sidebar: true
thumbnail: images/italy_turin1.jpg
title: The Research Institute for Geo-hydrological Protection of Turin —— Aerial photo
  archive management
type: case-study

---
{{<content-start >}}
# The Research Institute for Geo-hydrological Protection of Turin —— Aerial photo archive management
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>January 01, 2013</span>
</p>

Institutul de Cercetare pentru Protecția Geo-hidrologică din Torino (IRPI), membru al Consiliului Național Italian de Cercetare (CNR), și-a început activitatea în 1970. Competențele s-au conturat încă de la înființare, în diverse sectoare de cercetare, cum ar fi, în studiul proprietăților geologice și hidrogeologice ale sistemului de râuri Alpine-Po (nordul Italiei) sau în monitorizarea, predicția și prevenirea dezastrelor naturale. Aceste sarcini sunt efectuate printr-o abordare multidisciplinară, incluzând științele cheie, ingineria și geomatica.

In order to carry out exhaustive researches and studies, in addition to field survey, modelling and historical records analysis, aerial photograms are employed. Their use varies, from "simple" visual analyses to complex processing as stereoplotting or image segmentation.

The institute, for the explained purposes, keeps in its archive about 170000, recent and historical, photograms —— the oldest one dating back to 1920s (Figure 1) —— covering, in different years, the Po basin or part of it. Some photograms cover other basins in northern Italy. In addition the archives keeps flight plans of the described photograms (Figure 1).

<figure>
<img src="../images/italy_turin1.jpg" class="align-left" alt="italy_turin1.jpg" />
<figcaption>1929 photogram (left) and 1954 flight plan (right).</figcaption>
</figure>

## Managementul arhivei
In order to cope with such amount of data a GIS approach was adopted. First each flight plan, showing photograms' footprints, was scanned, georeferenced and digitized in shapefile format. Then photograms were scanned, at 600 DpI, and files were named according to a code including map sheet, year of acquisition, strip number, photogram's serial number and code of property (IRPI's or external).

Each footprint in digitized flight plan was provided, in its attributes, with the previous codes in order to link shapefile to scanned photograms, by the use of eVis plugin (Horning et al, 2009), and to allow a user friendly interface to search and refer to (Figure 2). Data concerning photogram code were stored in attribute table fields than, by field calculator, a "Link" field was created storing photograms' file paths.

<figure>
<img src="../images/italy_turin2.jpg" class="align-left" alt="italy_turin2.jpg" />
<figcaption>Photogram display (eVis Plugin)</figcaption>
</figure>

Moreover, due to the amount of searchable data a geographical search interface was developed. Thanks to the graphical modeler (in Processing, formerly SEXTANTE, plugin) capabilities, the developed tool, by different selection masks and input boxes, allows the user to select among three layers (administrative boundaries, map sheets and rivers), find a feature by querying its table and employ it to spatially query a digitized flight plan with the purpose of selecting photograms' footprints intersecting the selected feature (Figure 3). With this procedure, is then possible to point out selected photogram and simply display them with the previously described tool or extract, by their filenames and path, photograms' files for further processing.

<figure>
<img src="../images/italy_turin3.jpg" class="align-left" alt="italy_turin3.jpg" />
<figcaption>Graphic modeler scheme used in the selection tool (in background: purple polygons-map sheets; labeled orange polygons-photogram footprints; brown polygons-municipalities administrative borders)</figcaption>
</figure>

Colectarea fotogramelor este de mare interes, atât în ​​cercetare (Godone et al, 2014) cât și în mediile profesionale (Figura 4). Acum, datorită procedurilor și instrumentelor descrise, colectarea este pe deplin accesibilă iar din 2009 fotogramele au fost folosite în mai multe proiecte ale Institutului, atât interne cât și externe. Funcțiile QGIS precum și plugin-urile sale au permis dezvoltarea unor instrumente și proceduri de optimizare a gestiunii și exploatării arhivei fotogramelor.

<figure>
<img src="../images/italy_turin4.jpg" class="align-left" alt="italy_turin4.jpg" />
<figcaption>Pie chart showing different area of interest employing photograms in year 2013</figcaption>
</figure>

## Referințe
- Godone D., Garbarino M., Sibona E., Garnero G., Godone F. (2014) "Progressive fragmentation of a traditional Mediterranean landscape by hazelnut plantations: The impact of CAP over time in the Langhe region (NW Italy)", Land use policy, ISSN: 0264-8377
- Horning N., Koy K., Ersts P. (2009) "eVis (v1.1.0) User\'s Guide. American Museum of Natural History, Center for Biodiversity and Conservation" Available from <http://biodiversityinformatics.amnh.org/>

## Legături
- Aerial photo archive website: <http://www.irpi.to.cnr.it/index_en.php?page=aerofototeca_en>

## Autori
<figure>
<img src="../images/italy_turinaut1.jpg" class="align-left" height="120" alt="italy_turinaut1.jpg" />
<figcaption>Danilo Godone</figcaption>
</figure>

Danilo Godone is a Postdoc grant holder, at Turin University, studying geomatic contribution in landslide, glacier and, more generally, natural disasters monitoring. He is a member of NATRISK —— Research Centre on Natural Risks in Mountain and Hilly Environments, in the same University. He acts as a freelance consultant in the same topics, too.

<figure>
<img src="../images/italy_turinaut2.jpg" class="align-left" width="120" alt="italy_turinaut2.jpg" />
<figcaption>Franco Godone</figcaption>
</figure>

Franco Godone lucrează ca tehnician specialist la Institutul de Cercetare pentru Protecția Geo-hidrologică din Torino (IRPI-CNR), încă din anul 1972. El este implicat în studii topografice, aerofotogrammetrie și analiza datelor în regiunile alpine.

{{<content-end >}}
