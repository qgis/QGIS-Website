---
HasBanner: false
archived: true
date: 2013-01-01
draft: false
featured: false
section: progetto
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

L'Istituto di Ricerca per la Protezione Idrogeologica di Torino (IRPI), membro del Consiglio Nazionale delle Ricerche italiano (CNR), ha iniziato la sua attività nel 1970. Le competenze raccolte sin dalla sua fondazione riguardano diversi settori di indagine, ad esempio, lo studio delle caratteristiche geologiche e idrogeologiche del sistema alpino-Po (Nord Italia) o il monitoraggio, la previsione e la prevenzione delle catastrofi naturali. Questi compiti vengono svolti mediante l'impiego di un approccio multidisciplinare comprendenti le scienze della Terra, ingegneria e geomatica.

In order to carry out exhaustive researches and studies, in addition to field survey, modelling and historical records analysis, aerial photograms are employed. Their use varies, from "simple" visual analyses to complex processing as stereoplotting or image segmentation.

The institute, for the explained purposes, keeps in its archive about 170000, recent and historical, photograms —— the oldest one dating back to 1920s (Figure 1) —— covering, in different years, the Po basin or part of it. Some photograms cover other basins in northern Italy. In addition the archives keeps flight plans of the described photograms (Figure 1).

<figure>
<img src="../images/italy_turin1.jpg" class="align-left" alt="italy_turin1.jpg" />
<figcaption>1929 photogram (left) and 1954 flight plan (right).</figcaption>
</figure>

## Gestione dell'archivio
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

La collezione dei fotogrammi è di grande interesse sia nella ricerca (ad es Godone et al, 2014) e negli ambienti professionali (Figura 4). Grazie alle procedure e strumenti descritti, la collezione è completamente accessibile e dal 2009 i fotogrammi sono stati impiegati in numerosi progetti interni ed esterni all'Istituto. Le caratteristiche di QGIS e dei plugin consentito lo sviluppo di strumenti e procedure per ottimizzare l'archivio dei fotogrammi sia nella sua gestione e nella sua esplorazione.

<figure>
<img src="../images/italy_turin4.jpg" class="align-left" alt="italy_turin4.jpg" />
<figcaption>Pie chart showing different area of interest employing photograms in year 2013</figcaption>
</figure>

## Riferimenti
- Godone D., Garbarino M., Sibona E., Garnero G., Godone F. (2014) "Progressive fragmentation of a traditional Mediterranean landscape by hazelnut plantations: The impact of CAP over time in the Langhe region (NW Italy)", Land use policy, ISSN: 0264-8377
- Horning N., Koy K., Ersts P. (2009) "eVis (v1.1.0) User\'s Guide. American Museum of Natural History, Center for Biodiversity and Conservation" Available from <http://biodiversityinformatics.amnh.org/>

## Collegamenti
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

Franco Godone è un tecnico specializzato presso l'Istituto di Ricerca per la Protezione Idrogeologica di Torino (IRPI-CNR) dal 1972. Si occupa di rilievi topografici e degli aerofotogrammi e analisi dei dati nelle regioni alpine.

{{<content-end >}}
