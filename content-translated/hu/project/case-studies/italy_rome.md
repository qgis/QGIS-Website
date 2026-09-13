---
HasBanner: false
archived: true
date: 2015-03-01
draft: false
featured: false
section: projekt
sidebar: true
thumbnail: images/italy_igag1.png
title: QGIS térinformatikai feldolgozó eszköz az első szintű szeizmológiai mikrózónációs
  elemzésekhez
type: case-study

---
{{<content-start >}}
# QGIS térinformatikai feldolgozó eszköz az első szintű szeizmológiai mikrózónációs elemzésekhez
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>March 01, 2015</span>
</p>

The Institute of Environmental Geology and Geoengineering (IGAG) of the National Research Council (CNR) is located in Rome, in the Area of Research \"Roma 1\". It was founded in 2002 by regrouping five former research Institutes and Centers that had been active for more than 40 years in their field of expertise. IGAG covers a wide range of scientific topics in the field of Earth sciences, mainly focusing towards the study of:
- Környezet geokémia és szennyezett talaj és víz kármentesítés;
- Ásvány lerakatok és feldolgozásuk, beleértve a szennyvízkezelést is;
- Geotechnológiai mérnöki tevékenység és biztonságos kőzet feltárás;
- Recens geológiai evolúció;
- Természeti kockázatok csökkentése;
- Geoarcheológia és archeometria.
- Tenger Geológia
- Geomatika, GIS elemzések és fejlesztések.

Az első szintű mikrózónációs tanulmány a Pietramontecorvino területen (Dél-Olaszország, Apulia, a Déli és Közép-Appennin-hegységlánc mentén található) egy projekt része volt, együttműködésben az Apuliai vízgyűjtő-terület Hatósággal (Puglia AdB) és a Bari Egyetem Geológiai és Geofizikai Tanszékével (DGG), melynek célja Foggia megye 63 önkormányzati területének szeizmológiai mikrózónációja. A kutatási tevékenységet támogatta az Olasz Katasztrófavédelmi Osztály (DPC) és finanszírozta a Tárcaközi Gazdasági Tervezés Bizottság (CIPE n 20/2004). 
## QGIS térinformatikai feldolgozó eszköz az első szintű szeizmológiai mikrózónációs tanulmányokhoz
A szeizmikus mikrózónáció helyi szinten értékeli a szeizmikus kockázatokat, meghatározza az egységes szeizmikus viselkedéssel leírható területeket. Az első szintű szeizmikus mikrózónáció célja a kőzettani tulajdonságok felmérése és a geológiai egységek geometriájának meghatározása, amelyek segítésegével karakterizálhatók az egyes területek (mikrozónák).

A földrengések okozta károk megfigyeléséből kiderült, hogy helyi szinten változatosságot mutatnak az eltérő szeizmikus tevékenységek hatására, nem csak geológiai struktúrákban de a különböző minőségű és típusú épület struktúrákban is.

A szeizmikus mikrózónáció a homogén szeizmikus viselkedés alapján karakterizált területi egységek azonosítása segítésével értékeli a helyi szeizmikus kockázatokat.

The Guidelines and Criteria for Seismic microzoning 2008 (<http://www.protezionecivile.gov.it/jcms/it/view_pub.wp?contentId=PUB1137>) provide standards for seismic microzoning studies on Italian territory; they distinguish three levels of increasing depth (from 1 to 3).

Az első szintű szeizmikus mikrózónáció tartalmazza három tematikus térkép elkészítését:
1. Survey map containing the surveys for seismic microzonation studies;
2. Geo-lithological map, obtained from detailed scale geological and geomorphological maps integrating existing lithological, stratigraphic and geotechnical data related to surveys;
3. Level 1 seismic microzonation map (the principal product of level 1 microzonation), identifying the microzones into three categories of local hazards:
   - Stable zones;
   - Stable zones prone to ground amplification;
   - Unstable zones.

A jelen kutatás témája open source eszközök felhasználásával első szintű mikrózónációs térképek készítése, amely hozzájárul a topográfiai, geológiai, geofizikai és geotechnológiai adatok feldolgozásban kialakított módszertan kidolgozásához. 

A grafikus modellező eszköz a legutolsó QGIS  (2.8.1) verzióba került beépítésre, ezt használtuk fel az egyszerű térinformatikai modellünk létrehozásában. Ez az eszköz hasznos a gyakran használt az első szintű mikrózónációs térképek létrehozásához használt elemzések automatikus futtatásában, különösen az instabil zónák poligonokként történő azonosítására. 

A modell különböző open source szoftvereket és könyvtárakat használ fel (GRASS, GDAL, QGIS), ezáltal is bemutatja a QGIS szoftver használhatóságát mint egy egyszerűsített és egységesített felhasználó felülete a különböző GFOSS (Geospatial Free and Open Source Software) eszközöknek (1. ábra).

<figure>
<img src="../images/italy_igag1.png" class="align-right" alt="italy_igag1.png" />
<figcaption>(Fig. 1) Screenshot from the geoprocessing model.</figcaption>
</figure>

A modell bemenő adatai (2. ábra):
- Szintvonalakat tartalmazó shapefájl magassági attribútum oszloppal;
- The name of the field containing elevation values;
- A kívánt raszter felbontása méterben domborzatmodell és lejtőkategória (alapértelmezett 10) előállításához;
- Egy poligon shapefájl előállításra kerül, amely tartalmazza a 15 foknál nagyobb lejtőkategóriájú területeket a kiválasztott elemek átmetsző területével;
- Az eredmény polygon réteg neve.

<figure>
<img src="../images/italy_igag2.png" class="align-right" alt="italy_igag2.png" />
<figcaption>(Fig. 2) Model input form (left) and execution log (right).</figcaption>
</figure>

Indítás után, a modell elvégzi a következő műveleteket:
- The GRASS tool v.to.rast.attribute converts contour elevation lines to raster, taking the contour shapefile, the name of the z field and the raster resolution as input;
- The GRASS tool r.surf.contour generates the elevation model taking as input the rasterized temporary output from previous step and the raster resolution;
- The GDAL tool "gdaldem" generates the slope expressed as degrees from the elevation model;
- A GRASS r.mapcalculator eszköz segítségével generáltuk az 1 bites rasztereket amelyek tartalmazzák a 15 foknál nagyobb lejtőkategóriájú területeket (ez a határérték a mikrózónációs irányelvekben van meghatározva és ezek fixnek tekinthetők) a következő képlet felhasználásával: 

if(A\>15,1,null())

ahol A állandó lejtőkategória a raszter 'gdaldem'-el generálva;
- The GDAL tool "gdal_polygonize" converts the 1 bit raster to polygons;
- The QGIS tool "Intersection" is used to overlay the areas with slope greater than 15 degrees with the chosen intersection layer.

Az eredmény egy polygon réteg, amely tartalmazza a 15 foknál nagyobb lejtés miatt lehetséges instabil zónákat, automatikusan előállítva tematikus térképek alapján mint például a földcsuszamlás poligon réteg (3.ábra) vagy a kőzettani tematikus térkép.

<figure>
<img src="../images/italy_igag3.png" class="align-right" alt="italy_igag3.png" />
<figcaption>(Fig. 3) The model output (in red) shows highly unstable areas extracted from a landslides layer (orange).</figcaption>
</figure>

## Következtetések
This work clearly demonstrates that open source GIS tools like QGIS, GRASS, GDAL/OGR, can successfully be used for spatial analysis and data processing aimed at first level seismic microzonation studies. In this example work, QGIS has been used as a simplified and unified interface for different high quality GFOSS tools; the Graphical Modeler allows to intuitively construct geoprocessing models that can be easily shared as portable and cross-platform tools that doesn\'t require expensive software licenses. The tool leverages the QGIS modeling capabilities to graphically chain different algorithms, defining input and output parameters and leaving to the software the task of managing intermediate data output. The use of GRASS algorithms does not require defining and using a GRASS database and mapset, greatly simplifying the design of the model. Future developments include the creation of a package of tools and models, based on open source software, that can be used to simplify and speed up spatial analysis tasks necessary for seismic microzonation studies.
## Hivatkozások
- G. Baldassarre; Gallicchio, S.; Giannandrea, P. & Tropeano, M.: \"Relazione Finale Geolitologica per la microzonazione sismica di livello 1dei Comuni della Provincia di Foggia Dipartimento di Geologia e Geofisica dell\'Università di Bari, 2011\"
- Cavinato,G.P.; Cavuoto, G.; Coltella, M.; Cosentino, G.; Paolucci, E.; Peronace, E. & Simionato, M.: \"Studio di fattibilità per il monitoraggio e la messa in sicurezza delle aree urbane a rischio di stabilità statica e vulnerabilità strutturale del Comune e della Provincia di Foggia -CIPE 20/2004 Consiglio Nazionale delle Ricerche - Istituto di Geologia Ambientale e Geoingegneria, 2013, 526\"
- Contributi per l\'aggiornamento degli \"Indirizzi e criteri per la microzonazione sismica \" 2008. Ingegneria sismica, Pàtron Editore Bologna, 2011 (<http://www.protezionecivile.gov.it/jcms/it/view_pub.wp?contentId=PUB28083>)
- Gruppo di lavoro MS, 2008. Indirizzi e criteri per la microzonazione sismica. Conferenza delle Regioni e delle Province autonome - Dipartimento della protezione civile, Roma, 3 vol. e Dvd, Presidenza del Consiglio dei Ministri, Dipartimento di Protezione Civile, 2008, 424. (<http://www.protezionecivile.gov.it/jcms/it/view_pub.wp?contentId=PUB1137>)

## Szerzők
Ez a cikk Giuseppe Cosentino és Francesco Pennica (www.igag.cnr.it) közreműködésével készült 2015. márciusban.

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
