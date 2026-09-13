---
HasBanner: false
archived: true
date: 2015-03-01
draft: false
featured: false
section: proiect
sidebar: true
thumbnail: images/italy_igag1.png
title: Modelul QGIS de geoprocesare pentru simplificarea primului nivel de analiză
  a microzonării seismice
type: case-study

---
{{<content-start >}}
# Modelul QGIS de geoprocesare pentru simplificarea primului nivel de analiză a microzonării seismice
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>March 01, 2015</span>
</p>

The Institute of Environmental Geology and Geoengineering (IGAG) of the National Research Council (CNR) is located in Rome, in the Area of Research \"Roma 1\". It was founded in 2002 by regrouping five former research Institutes and Centers that had been active for more than 40 years in their field of expertise. IGAG covers a wide range of scientific topics in the field of Earth sciences, mainly focusing towards the study of:
- Environmental geochemistry and remediation of contaminated soils and waters;
- Mineral deposits and mineral processing, including the treatment of waste waters;
- Geoengineering and safety of rock excavations;
- Evoluțiile geologice recente;
- Reducerea riscurilor naturale;
- Geoarheologia și arheometria.
- Geologie Marină
- Geomatică, analiză și dezvoltare GIS.

Nivelul 1 al studiului de microzonare seismică pentru zona Pietramontecorvino (Apulia, sudul Italiei, de-a lungul lanțului central-sudic al Apeninilor) este parte a unui proiect, în colaborare cu Autoritatea Bazinului Apulia (Puglia AdB) și Departamentul de Geologie și Geofizică (DGG) de la Universitatea din Bari, care vizează microzonarea seismică a 63 municipalități din zona Foggia. Activitatea a fost promovată de către Departamentul italian de protecție civilă (DPC) și finanțată de Comitetul Interministerial pentru Planificare Economica (CIPE n. 20/2004).
## Instrumentul QGIS de geoprocesare pentru primul nivel al studiilor microzonării seismice
Microzonarea seismică a evaluat riscul seismic la scară locală, propunându-și să identifice suprafețele din teritoriu caracterizate printr-un comportament seismic omogen. Primul nivel de microzonare seismică are scopul de a defini proprietățile litologice și geometria unităților geologice care caracterizează aceste porțiuni ale teritoriului (microzone).

Observarea prejudiciului cauzat de un cutremur prezintă, de multe ori, variații la nivel local cauzate nu numai de structurile geologice, ci, de asemenea, de diferitele calități și tipuri de structuri construite, care au ca rezultat diferite pericole seismice.

Microzonarea seismică evaluează riscul seismic local, prin identificarea zonelor din teritoriu caracterizate prin comportament seismic omogen.

The Guidelines and Criteria for Seismic microzoning 2008 (<http://www.protezionecivile.gov.it/jcms/it/view_pub.wp?contentId=PUB1137>) provide standards for seismic microzoning studies on Italian territory; they distinguish three levels of increasing depth (from 1 to 3).

Primul nivel de microzonare seismică constă în crearea a trei hărți tematice:
1. Harta oservațiilor care conține datele prelevate pentru studiile de microzonare seismică;
2. Harta geo-litologică, obținută din hărțile geologice și geomorfologice detaliate, la scară, care integrează, datele litologice, stratigrafice și geotehnice aferente observațiilor;
3. Harta de microzonare seismică, de nivelul 1 (produsul principal al nivelului 1 de microzonare), cu microzonele împărțite în trei categorii de pericole locale:
   - Zone stabile;
   - Zonele stabile predispuse la amplificare la nivelul solului;
   - Zone instabile.

Domeniul de aplicare al acestei lucrări este de a contribui la crearea unei metodologii de procesare a datelor topografice, geologice, geofizice și geo-tehnice care vizează schițarea  hărții de microzonare seismică de nivelul 1, cu ajutorul instrumentelor open source.

Instrumentul de Modelare Grafică integrat în cea mai recentă versiune a QGIS (2.8.1 la momentul scrierii acestui articol) a fost folosit pentru crearea unui model de geoprocesare simplu. Acest instrument este util pentru automatizarea uneia din analizele efectuate de obicei pentru crearea hărților de microzonare seismică de nivel 1, în special pentru a reprezenta zonele instabile ca entități de tip poligon.

Modelul face uz de diferite aplicații și biblioteci cu sursă deschisă (GRASS, GDAL, QGIS), demonstrând utilitatea QGIS ca interfață simplificată și unificată pentru instrumentele eterogene GFOSS (Software Geospațial Gratuit și Cu Sursă Deschisă) (Fig. 1).

<figure>
<img src="../images/italy_igag1.png" class="align-right" alt="italy_igag1.png" />
<figcaption>(Fig. 1) Screenshot from the geoprocessing model.</figcaption>
</figure>

Modelul folosește ca intrare (Fig. 2):
- Un fișier shape al curbelor de nivel, care conține un câmp cu valorile elevației;
- The name of the field containing elevation values;
- Rezoluția raster dorită în metri pentru DEM și Slope (implicit 10);
- Un fișier shape de tip poligon din care vor fi extrase entitățile care se intersectează cu zonele cu pantă mai mare de 15 de grade;
- Numele stratului poligonal rezultat.

<figure>
<img src="../images/italy_igag2.png" class="align-right" alt="italy_igag2.png" />
<figcaption>(Fig. 2) Model input form (left) and execution log (right).</figcaption>
</figure>

Când se lansează, modelul efectuează următoarele operațiuni:
- Instrumentul GRASS v.to.rast.attribute convertește curbele de nivel în raster, pornind de la fișierul shape al curbelor, numele câmpului z și rezoluția rasterului;
- Instrumentul GRASS r.surf.contour generează modelul de elevație, primind ca date de intrare rezultatul temporar rasterizat din etapa anterioară și rezoluția rasterului;
- The GDAL tool "gdaldem" generates the slope expressed as degrees from the elevation model;
- Instrumentul GRASS r.mapcalculator este utilizat pentru a genera un raster de 1 bit, identificând zonele cu pantă mai mare de 15 de grade (această valoare fiind codată în liniile directoare de microzonare, fiind astfel fixă), cu ajutorul expresiei:

if(A\>15,1,null())

unde A este rasterul temporar al pantei, generat de gdaldem;
- The GDAL tool "gdal_polygonize" converts the 1 bit raster to polygons;
- The QGIS tool "Intersection" is used to overlay the areas with slope greater than 15 degrees with the chosen intersection layer.

Rezultatul constă într-un strat poligonal cu zone predispuse la instabilitate, datorită unei pante mai mari de 15 de grade extrasă automat dintr-o hartă tematică, cum ar fi un strat poligonal al terenurilor surpate  (Fig. 3) sau o hartă litologică.

<figure>
<img src="../images/italy_igag3.png" class="align-right" alt="italy_igag3.png" />
<figcaption>(Fig. 3) The model output (in red) shows highly unstable areas extracted from a landslides layer (orange).</figcaption>
</figure>

## Concluzii
This work clearly demonstrates that open source GIS tools like QGIS, GRASS, GDAL/OGR, can successfully be used for spatial analysis and data processing aimed at first level seismic microzonation studies. In this example work, QGIS has been used as a simplified and unified interface for different high quality GFOSS tools; the Graphical Modeler allows to intuitively construct geoprocessing models that can be easily shared as portable and cross-platform tools that doesn\'t require expensive software licenses. The tool leverages the QGIS modeling capabilities to graphically chain different algorithms, defining input and output parameters and leaving to the software the task of managing intermediate data output. The use of GRASS algorithms does not require defining and using a GRASS database and mapset, greatly simplifying the design of the model. Future developments include the creation of a package of tools and models, based on open source software, that can be used to simplify and speed up spatial analysis tasks necessary for seismic microzonation studies.
## Referințe
- G. Baldassarre; Gallicchio, S.; Giannandrea, P. & Tropeano, M.: \"Relazione Finale Geolitologica per la microzonazione sismica di livello 1dei Comuni della Provincia di Foggia Dipartimento di Geologia e Geofisica dell\'Università di Bari, 2011\"
- Cavinato,G.P.; Cavuoto, G.; Coltella, M.; Cosentino, G.; Paolucci, E.; Peronace, E. & Simionato, M.: \"Studio di fattibilità per il monitoraggio e la messa in sicurezza delle aree urbane a rischio di stabilità statica e vulnerabilità strutturale del Comune e della Provincia di Foggia -CIPE 20/2004 Consiglio Nazionale delle Ricerche - Istituto di Geologia Ambientale e Geoingegneria, 2013, 526\"
- Contributi per l\'aggiornamento degli \"Indirizzi e criteri per la microzonazione sismica \" 2008. Ingegneria sismica, Pàtron Editore Bologna, 2011 (<http://www.protezionecivile.gov.it/jcms/it/view_pub.wp?contentId=PUB28083>)
- Gruppo di lavoro MS, 2008. Indirizzi e criteri per la microzonazione sismica. Conferenza delle Regioni e delle Province autonome - Dipartimento della protezione civile, Roma, 3 vol. e Dvd, Presidenza del Consiglio dei Ministri, Dipartimento di Protezione Civile, 2008, 424. (<http://www.protezionecivile.gov.it/jcms/it/view_pub.wp?contentId=PUB1137>)

## Autori
Acest articol a fost transmis în martie 2015 de Giuseppe Cosentino și Francesco Pennica (www.igag.cnr.it).

<figure>
<img src="../images/guiseppe_cosentino.png" class="align-left" height="200" alt="guiseppe_cosentino.png" />
<figcaption>Giuseppe Cosentino</figcaption>
</figure>

Giuseppe Cosentino \<<g.cosentino@igag.cnr.it>\> is geologist and technologist specializied in Geographic Information Systems for the management of geological and engineering hazards. Currently working in the field of seismic microzonation and environmental characterization of the lands in contaminated sites. Areas of interest: geological and environmental hazards, cartography, structural geology, explorative drillings.

<figure>
<img src="../images/francesco_pennica.png" class="align-left" height="200" alt="francesco_pennica.png" />
<figcaption>Francesco Pennica</figcaption>
</figure>

Francesco Pennica provides GIS and WebGIS software development and data management: GeoServer, MapServer, ArcGIS Server, GeoNetwork OGC standard based webgis services, Java, HTML, CSS, Javascript, Python, PHP languages and frameworks, WebGIS front-end development with OpenLayers, ExtJS, GeoExt, JQuery, GWT, Ext-GWT, Google Maps API SQL, geodatabase management, PostgreSQL, PostGIS, GIS desktop software based analysis and scripting (ArcGIS, GRASS, GFOSS tools), Software configuration and management in Linux and Windows based servers and desktops.

{{<content-end >}}
