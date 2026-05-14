---
HasBanner: false
archived: true
date: 2015-03-01
draft: false
featured: false
section: projektą
sidebar: true
thumbnail: images/italy_igag1.png
title: QGIS geoapdorojimo modelis pirmo lygio seisminio mikrozonavimo analizės supaprastinimui
type: case-study

---
{{<content-start >}}
# QGIS geoapdorojimo modelis pirmo lygio seisminio mikrozonavimo analizės supaprastinimui
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>March 01, 2015</span>
</p>

The Institute of Environmental Geology and Geoengineering (IGAG) of the National Research Council (CNR) is located in Rome, in the Area of Research \"Roma 1\". It was founded in 2002 by regrouping five former research Institutes and Centers that had been active for more than 40 years in their field of expertise. IGAG covers a wide range of scientific topics in the field of Earth sciences, mainly focusing towards the study of:
- Aplinkos geochemijai ir užteršto dirvožemio ir vandens atkūrimui;
- Mineralų klodų ir mineralų apdorojimo, įskaitant ir nuotekų valymui;
- Geoinžinerija ir uolų kasybos saugumas;
- Paskutinių laikų geologinė evoliucija;
- Natūralių pavojų valdymas;
- Geoarcheologija ir archeometrija.
- Jūrų geologija
- Geomatika, GIS analizė ir vystymas.

Pietramontecorvino zonos 1 lygio seisminio mikrozonavimo studija (Apulia, Pietų Italija, esanti greta centrinės-pietinės Apeninų grandinės) yra dalis projekto, vykdomo kartu su Apulia Baseino vadovybe (Puglia AdB) ir Bari universiteto geologijos ir geofizikos departamentu (DGG). Projekto tikslas yra 63 Foggia savivaldybių seisminis mikrozonavimas. Šią veiklą skatino Italijos Civilinės Saugos departamentas (DPC) ir finansavo Tarpministerinis ekonominio planavimo komitetas (CIPE n. 20/2004).
## QGIS geoapdorojimo įrankis pirmo lygio seisminio mikrozonavimo tyrimams
Seisminis mikrozonavimas įvertina seisminius pavojus vietiniu masteliu, siūlant identifikuoti teritorijos plotus, kuriems charakteringa homogeninė seisminė elgsena. Pirmo lygio seisminio mikrozonavimo tikslas yra nustatyti geologinių vienetų litologines savybes ir geometriją, kuri charakterizuoja teritorijos dalis (mikrozonas).

Žemės drebėjimo sukeltų nuostolių stebėjimas dažnai rodo skirtumus vietiniu masteliu ne tik pagal geologines struktūras, bet taip pat ir pagal skirtingus statinių tipus ir statybos kokybę, įtakojančius skirtingus seisminius pavojus.

Seisminis mikrozonavimas įvertina vietinius seisminius pavojus identifikuojant teritorijos plotus, charakterizuojamus homogenine seismine elgsena.

The Guidelines and Criteria for Seismic microzoning 2008 (<http://www.protezionecivile.gov.it/jcms/it/view_pub.wp?contentId=PUB1137>) provide standards for seismic microzoning studies on Italian territory; they distinguish three levels of increasing depth (from 1 to 3).

Pirmo lygio seisminį mikrozonavimą sudaro trijų teminių žemėlapių kūrimas:
1. Mikrozonavimo tyrimo apžiūrų žemėlapis;
2. Geo-litologinis žemėlapis, gautas iš detalaus mastelio geologinių ir geomorfologinių žemėlapių, integruojant esamas litologinius, stratigrafinius ir geotechnius duomenis, susijusius su apžiūromis;
3. 1 lygio seisminio mikrozonavimo žemėlapis (1 lygio mikrozonavimo pagrindinis rezultatas), identifikuojantis mikrozonas į tris vietinių pavojų kategorijas:
   - Stabilios zonos;
   - Stabilios zonos, linkusios į žemės plėtimąsi;
   - Nestabilios zonos.

Šio darbo apimtis yra sukurti topografinių, geologinių, geofizinių ir geotechninių duomenų apdorojimo metodologiją, skirtą 1 lygio seisminio mikrozonavimo juodraštinio žemėlapio kūrimui, naudojant atviro kodo įrankius.

Grafinio modeliavimo įrankis, integruotas į paskutinę QGIS versiją (rašymo metu tai 2.8.1) buvo panaudotas paprasto geoapdorojimo modelio kūrimui. Šis įrankis naudingas automatizuojant dažnai vykdomų 1 lygio seisminio mikrozonavimo žemėlapio kūrimo veiksmus. Pavyzdžiui identifikuojant nestabilias zonas kaip poligono tipo geoobjektus.

Modelis panaudoja įvairią atviro kodo programinę įrangą ir bibliotekas (GRASS, GDAL, QGIS), demonstruoja QGIS, kaip supaprastintos ir apjungtos sąsajos heterogeniškiems GFOSS (Geoerdvinė laisva ir atviro kodo programinė įranga) įrankiams naudingumą (Pav. 1).

<figure>
<img src="../images/italy_igag1.png" class="align-right" alt="italy_igag1.png" />
<figcaption>(Fig. 1) Screenshot from the geoprocessing model.</figcaption>
</figure>

Modelis kaip įvesti ima (Pav. 2):
- Kontūro linijų shape failą, kuriame yra laukas su aukščio reikšmėmis;
- The name of the field containing elevation values;
- Norima rastro rezoliucija metrais skirtą DEM ir Nuolydžiui (pagal nutylėjimą 10);
- Poligonų shape failas, iš kurio ištraukiami geoobjektai, susikertantys su plotais, kurių nuožulnumas didesnis už 15 laipsnių;
- Gaunamo poligonų sluoksnio pavadinimas.

<figure>
<img src="../images/italy_igag2.png" class="align-right" alt="italy_igag2.png" />
<figcaption>(Fig. 2) Model input form (left) and execution log (right).</figcaption>
</figure>

Paleidus modelis vykdo šiuos veiksmus:
- GRASS įrankis v.to.rast.attribute keičia aukščio kontūro linijas į rastrą, kaip įvestį naudojant kontūro shape failą, z lauko pavadinimą ir rastro rezoliuciją;
- GRASS įrankis r.surf.contour sukuria aukščio modelį, kaip įvesti imant rastrizuotą laikiną ankstesnio žingsnio išvestį ir rastro rezoliuciją;
- The GDAL tool "gdaldem" generates the slope expressed as degrees from the elevation model;
- GRASS įrankis r.mapcalculator naudojamas kuriant 1 bito rastrą, identifikuojantį plotus su didesniu nei 15 laipsnių nuožulnumu (ši reikšmė įkoduota į mikrozonavimo gaires, todėl yra fiksuota), naudojant išraišką;

if(A\>15,1,null())

kur A yra laikinas nuokalnės rastras, sukurtas gdaldem;
- The GDAL tool "gdal_polygonize" converts the 1 bit raster to polygons;
- The QGIS tool "Intersection" is used to overlay the areas with slope greater than 15 degrees with the chosen intersection layer.

Gaunamas poligonų sluoksnis su plotais, linkusiais į nestabilumą dėl nuokalnės, didesnės nei 15 laipsnių, automatiškai ištrauktais iš tematinio žemėlapio, tokio kaip nuošliaužų poligono sluoksnio (Pav. 3) arba litologinio žemėlapio.

<figure>
<img src="../images/italy_igag3.png" class="align-right" alt="italy_igag3.png" />
<figcaption>(Fig. 3) The model output (in red) shows highly unstable areas extracted from a landslides layer (orange).</figcaption>
</figure>

## Išvados
This work clearly demonstrates that open source GIS tools like QGIS, GRASS, GDAL/OGR, can successfully be used for spatial analysis and data processing aimed at first level seismic microzonation studies. In this example work, QGIS has been used as a simplified and unified interface for different high quality GFOSS tools; the Graphical Modeler allows to intuitively construct geoprocessing models that can be easily shared as portable and cross-platform tools that doesn\'t require expensive software licenses. The tool leverages the QGIS modeling capabilities to graphically chain different algorithms, defining input and output parameters and leaving to the software the task of managing intermediate data output. The use of GRASS algorithms does not require defining and using a GRASS database and mapset, greatly simplifying the design of the model. Future developments include the creation of a package of tools and models, based on open source software, that can be used to simplify and speed up spatial analysis tasks necessary for seismic microzonation studies.
## Šaltiniai
- G. Baldassarre; Gallicchio, S.; Giannandrea, P. & Tropeano, M.: \"Relazione Finale Geolitologica per la microzonazione sismica di livello 1dei Comuni della Provincia di Foggia Dipartimento di Geologia e Geofisica dell\'Università di Bari, 2011\"
- Cavinato,G.P.; Cavuoto, G.; Coltella, M.; Cosentino, G.; Paolucci, E.; Peronace, E. & Simionato, M.: \"Studio di fattibilità per il monitoraggio e la messa in sicurezza delle aree urbane a rischio di stabilità statica e vulnerabilità strutturale del Comune e della Provincia di Foggia -CIPE 20/2004 Consiglio Nazionale delle Ricerche - Istituto di Geologia Ambientale e Geoingegneria, 2013, 526\"
- Contributi per l\'aggiornamento degli \"Indirizzi e criteri per la microzonazione sismica \" 2008. Ingegneria sismica, Pàtron Editore Bologna, 2011 (<http://www.protezionecivile.gov.it/jcms/it/view_pub.wp?contentId=PUB28083>)
- Gruppo di lavoro MS, 2008. Indirizzi e criteri per la microzonazione sismica. Conferenza delle Regioni e delle Province autonome - Dipartimento della protezione civile, Roma, 3 vol. e Dvd, Presidenza del Consiglio dei Ministri, Dipartimento di Protezione Civile, 2008, 424. (<http://www.protezionecivile.gov.it/jcms/it/view_pub.wp?contentId=PUB1137>)

## Autoriai
Šį straipsnį 2015 metų kovą parašė Giuseppe Casentino ir Francesco Pennica (www.igag.cnr.it).

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
