---
HasBanner: false
archived: true
date: 2015-03-01
draft: false
featured: false
section: projekt
sidebar: true
thumbnail: images/italy_igag1.png
title: Model geoprocessingu QGIS pro zjednodušení analýzy první úrovně seismické mikrozonizace
type: case-study

---
{{<content-start >}}
# Model geoprocessingu QGIS pro zjednodušení analýzy první úrovně seismické mikrozonizace
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>March 01, 2015</span>
</p>

The Institute of Environmental Geology and Geoengineering (IGAG) of the National Research Council (CNR) is located in Rome, in the Area of Research \"Roma 1\". It was founded in 2002 by regrouping five former research Institutes and Centers that had been active for more than 40 years in their field of expertise. IGAG covers a wide range of scientific topics in the field of Earth sciences, mainly focusing towards the study of:
- Environmentální geochemie a sanace kontaminovaných půd a vod;
- Ložiska nerostů a zpracování nerostů včetně čištění odpadních vod;
- Geoinženýrství a bezpečnost skalních výkopů;
- Nedávný geologický vývoj;
- Zmírňování přírodních rizik;
- Geoarcheologie a archeologie.
- Mořská geologie
- Geomatika, analýza a vývoj GIS.

Studie seismické mikrozonizace 1. úrovně v oblasti Pietramontecorvino (Apulie, jižní Itálie, která se nachází podél středo-jižního Apeninského řetězce) je součástí projektu ve spolupráci se správou povodí Apulie (Puglia AdB) a katedrou geologie a geofyziky (DGG) University of Bari, zaměřené na seismickou mikrozonaci 63 obcí v oblasti Foggia. Aktivita byla podporována italským ministerstvem civilní ochrany (DPC) a financována Meziministerským výborem pro hospodářské plánování (CIPE č. 20/2004).
## QGIS geoprocessingový nástroj pro první úroveň studií seismické mikrozonizace
Seismická mikrozonizace vyhodnocuje seismické ohrožení v místním měřítku a navrhuje identifikovat oblasti území vyznačující se homogenním seismickým chováním. První úroveň seismického mikrozónování má za účel definovat litologické vlastnosti a geometrii geologických jednotek, které charakterizují tyto části území (mikrozóny).

Pozorování škod způsobených zemětřesením často vykazuje odchylky v místním měřítku způsobené nejen geologickými strukturami, ale také odlišnou kvalitou a typem stavebních konstrukcí, což má za následek různá seismická nebezpečí.

Seismická mikrozonizace vyhodnocuje místní seismické nebezpečí prostřednictvím identifikace oblastí území vyznačujících se homogenním seismickým chováním.

The Guidelines and Criteria for Seismic microzoning 2008 (<http://www.protezionecivile.gov.it/jcms/it/view_pub.wp?contentId=PUB1137>) provide standards for seismic microzoning studies on Italian territory; they distinguish three levels of increasing depth (from 1 to 3).

První stupeň seismické mikrozonizace spočívá ve vytvoření tří tematických map:
1. Průzkumná mapa obsahující průzkumy pro studie seismické mikrozonizace;
2. Geolitologická mapa získaná z podrobných geologických a geomorfologických map integrujících existující litologická, stratigrafická a geotechnická data související s průzkumy;
3. Mapa seismické mikrozonizace 1. úrovně (hlavní produkt mikrozonizace 1. úrovně), identifikující mikrozóny do tří kategorií místních nebezpečí:
   - Stabilní zóny;
   - Stabilní zóny náchylné k zemnímu zesílení;
   - Nestabilní zóny.

Náplní této práce je přispět k vytvoření metodiky pro zpracování topografických, geologických, geofyzikálních a geotechnických dat zaměřených na tvorbu map seismické mikrozonace 1. úrovně s využitím open source nástrojů.

Pro vytvoření jednoduchého geoprocesního modelu byl použit nástroj Graphical Modeler integrovaný v nejnovější verzi QGIS (2.8.1 v době psaní). Tento nástroj je užitečný pro automatizaci jedné z analýz běžně prováděných pro tvorbu seismických mikrozonačních map úrovně 1, zejména pro identifikaci nestabilních zón jako polygonových prvků.

Model využívá různé open source software a knihovny (GRASS, GDAL, QGIS), což demonstruje užitečnost QGIS jako zjednodušeného a jednotného rozhraní pro heterogenní nástroje GFOSS (Geospatial Free and Open Source Software) (obr. 1).

<figure>
<img src="../images/italy_igag1.png" class="align-right" alt="italy_igag1.png" />
<figcaption>(Fig. 1) Screenshot from the geoprocessing model.</figcaption>
</figure>

Vstupem modelu je (obr. 2):
- Shapefile obrysových linií obsahující pole s hodnotami nadmořské výšky;
- The name of the field containing elevation values;
- Požadované rozlišení rastru v metrech pro DEM a Slope (výchozí 10);
- polygonový shapefile, ze kterého budou extrahovány prvky protínající oblasti se sklonem větším než 15 stupňů;
- Název výsledné vrstvy polygonů.

<figure>
<img src="../images/italy_igag2.png" class="align-right" alt="italy_igag2.png" />
<figcaption>(Fig. 2) Model input form (left) and execution log (right).</figcaption>
</figure>

Po spuštění provádí model následující operace:
- Nástroj GRASS v.to.rast.attribute převede výškové čáry obrysů na rastr, přičemž jako vstupní údaje použije shapefile obrysu, název pole z a rozlišení rastru;
- Nástroj GRASS r.surf.contour vygeneruje výškový model, přičemž jako vstup použije rasterizovaný dočasný výstup z předchozího kroku a rozlišení rastru;
- The GDAL tool "gdaldem" generates the slope expressed as degrees from the elevation model;
- Nástroj GRASS r.mapcalculator se používá k vygenerování 1bitového rastru identifikujícího oblasti se sklonem větším než 15 stupňů (tato hodnota je zakódována ve směrnicích pro mikrozonování, a proto je pevně stanovena) pomocí výrazu:

if(A\>15,1,null())

kde A je dočasný rastr sklonu vygenerovaný pomocí gdaldem;
- The GDAL tool "gdal_polygonize" converts the 1 bit raster to polygons;
- The QGIS tool "Intersection" is used to overlay the areas with slope greater than 15 degrees with the chosen intersection layer.

Výsledkem je polygonová vrstva s oblastmi náchylnými k nestabilitě kvůli sklonu svahu většímu než 15 stupňů, automaticky extrahovaná z tematické mapy, jako je polygonová vrstva sesuvů (obr. 3) nebo litologická mapa.

<figure>
<img src="../images/italy_igag3.png" class="align-right" alt="italy_igag3.png" />
<figcaption>(Fig. 3) The model output (in red) shows highly unstable areas extracted from a landslides layer (orange).</figcaption>
</figure>

## Závěry
This work clearly demonstrates that open source GIS tools like QGIS, GRASS, GDAL/OGR, can successfully be used for spatial analysis and data processing aimed at first level seismic microzonation studies. In this example work, QGIS has been used as a simplified and unified interface for different high quality GFOSS tools; the Graphical Modeler allows to intuitively construct geoprocessing models that can be easily shared as portable and cross-platform tools that doesn\'t require expensive software licenses. The tool leverages the QGIS modeling capabilities to graphically chain different algorithms, defining input and output parameters and leaving to the software the task of managing intermediate data output. The use of GRASS algorithms does not require defining and using a GRASS database and mapset, greatly simplifying the design of the model. Future developments include the creation of a package of tools and models, based on open source software, that can be used to simplify and speed up spatial analysis tasks necessary for seismic microzonation studies.
## Reference
- G. Baldassarre; Gallicchio, S.; Giannandrea, P. & Tropeano, M.: \"Relazione Finale Geolitologica per la microzonazione sismica di livello 1dei Comuni della Provincia di Foggia Dipartimento di Geologia e Geofisica dell\'Università di Bari, 2011\"
- Cavinato,G.P.; Cavuoto, G.; Coltella, M.; Cosentino, G.; Paolucci, E.; Peronace, E. & Simionato, M.: \"Studio di fattibilità per il monitoraggio e la messa in sicurezza delle aree urbane a rischio di stabilità statica e vulnerabilità strutturale del Comune e della Provincia di Foggia -CIPE 20/2004 Consiglio Nazionale delle Ricerche - Istituto di Geologia Ambientale e Geoingegneria, 2013, 526\"
- Contributi per l\'aggiornamento degli \"Indirizzi e criteri per la microzonazione sismica \" 2008. Ingegneria sismica, Pàtron Editore Bologna, 2011 (<http://www.protezionecivile.gov.it/jcms/it/view_pub.wp?contentId=PUB28083>)
- Gruppo di lavoro MS, 2008. Indirizzi e criteri per la microzonazione sismica. Conferenza delle Regioni e delle Province autonome - Dipartimento della protezione civile, Roma, 3 vol. e Dvd, Presidenza del Consiglio dei Ministri, Dipartimento di Protezione Civile, 2008, 424. (<http://www.protezionecivile.gov.it/jcms/it/view_pub.wp?contentId=PUB1137>)

## Autoři
Do tohoto článku přispěli v březnu 2015 Giuseppe Cosentino a Francesco Pennica (www.igag.cnr.it).

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
