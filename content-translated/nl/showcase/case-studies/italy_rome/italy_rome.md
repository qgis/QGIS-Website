---
draft: 'true'

---
# QGIS geoprocessing model om seismische microzonering-analyse op het eerste niveau te vereenvoudigen
Het Instituut voor Environmental Geology and Geoengineering (IGAG) van de National Research Council (CNR) is gevestigd in Rome, in het onderzoeksgebied \"Roma 1\". Het werd opgericht in 2002 door de samenvoeging van vijf bestaande onderzoeksinstituten en centra die meer dan 40 jaar actief waren op hun gebied van expertise. IGAG behandelt een brede variëteit aan wetenschappelijke onderwerpen op het gebied van Aardwetenschappen, voornamelijk met de focus op het bestuderen van:
- Milieukundige geo-scheikunde en het tegengaan van verontreinigde bodem en wateren;
- Minerale uitstroom en minerale verwerking, inclusief de behandeling van afvalwater;
- Geo-ingenieurswerk en veiligheid bij afgravingen van rotsen;
- Recente geologische evolutie;
- Matiging van natuurlijk gevaar;
- Geo-archaeologie en archaeometrie.
- Marine geologie
- Geomatica, GIS-analyses en ontwikkeling.

D studie van de niveau 1 seismische microzonering van het gebied Pietramontecorvino (Apulia, Zuid-Italië, gelegen langs de centraal-zuidelijke Apennijnen) is deel van een project, in samenwerking met de Basin Authority van Apulia (Puglia AdB) en het Departement van geologie en geofysica (DGG) van de universiteit van Bari, gericht op de seismische microzonering van 63 gemeenten in het gebied Foggia. De activiteiten werden gepromoot door het Italiaanse Departement van civiele bescherming (DPC) en gefinanciertd door het Interministerieel comité voor economische planning (CIPE n. 20/2004).
## QGIS gereedschap voor geoprocessing voor bestuderen van seismische microzonering-analyse op het eerste niveau
De seismische microzonering evalueert het seismische gevaar op lokale schaal met als doel gebieden te identificeren die worden gekarakteriseerd door homogeen seismisch gedrag. Het eerste niveau van of seismische microzonering heeft tot doel het definiëren van de lithologische eigenschappen en geometrie van geologische eenheden die deze gebiedsdelen karakteriseren (microzones).

De observatie van door een aardbeving veroorzaakte schade laat vaak variaties op een lokale schaal zien die niet alleen worden veroorzaakt door geologische structuren, maar ook door de verschillende kwaliteit en type van structuren, resulterend in verschillende seismische gevaren.

De seismische microzonering evalueert het lokale seismische gevaar, door het identificeren van gebiedsdelen die worden gekarakteriseerd door homogeen seismisch gedrag.

De Guidelines and Criteria for Seismic microzoning 2008 (<http://www.protezionecivile.gov.it/jcms/it/view_pub.wp?contentId=PUB1137>) verschaffen standaarden voor studies van seismische microzonering in Italiaans gebied; ze onderscheiden drie niveaus van toenemende grootte (van 1 tot en met 3).

Het eerste niveau seismische microzonering bestaat uit het maken van drie thematische kaarten:
1. Onderzoekskaart bevat de gegevens voor bestuderen van seismische microzonering;
2. Geo-lithologische kaart, verkregen uit gedetailleerde geologische en geomorphologische kaarten op schaal die bestaande lithologische, stratigrafische en geotechnische gegevens, gerelateerd aan de onderzoeken, integreert;
3. Seismische microzoneringskaart voor niveau 1 (het principale product van niveau microzonering), die de microzones identificeert naar drie categorieën van lokale gevaren:
   - Stabiele zones;
   - Stabiele zones gevoelig voor grondverschuivingen;
   - Onstabiele zones.

Het doel van dit werk is om bij te dragen aan het maken van een methodologie voor het verwerken van topografische, geologische, geofysische en geo-technische gegevens, gericht op het tekenen van een kaart voor niveau 1 seismische microzonering, door middle van het gebruiken van open source gereedschappen.

Het gereedschap Grafische modellen bouwen, geïntegreerd in de laatste versie van QGIS (2.8.1 op het moment van schrijven) is gebruikt voor het maken van een eenvoudig model voor geoprocessing. Dit gereedschap is nuttig om een van de veel voorkomende analyses, die vaak wordt uitgevoerd voor het maken van kaarten voor niveau 1 seismische microzonering, te automatiseren, in het bijzonder om instabiele zones als polygoon-objecten te identificeren.

Het model maakt gebruik van verschillende open source software en bibliotheken (GRASS, GDAL, QGIS), wat de bruikbaarheid van QGIS als een vereenvoudigde en geünificeerde interface voor heterogene gereedschappen voor GFOSS (Geospatial Free and Open Source Software) demonstreert (Fig. 1).

![(Fig. 1) Screenshot from the geoprocessing model.](./images/italy_igag1.png){.align-right}

Het model neemt als invoer (Fig. 2):
- Een shapefile van contourlijnen die een veld met waarden voor hoogten bevat;
- De naam van het veld dat de waarden voor hoogte bevat;
- De gewenste rasterresolutie in meters voor DEM en Slope (standaard 10);
- Een polygoon-shapefile waaruit objecten die kruisen met gebieden met een helling groter dan 15 graden zullen worden uitgenomen;
- De naam van de resulterende polygoonlaag.

![(Fig. 2) Model input form (left) and execution log (right).](./images/italy_igag2.png){.align-right}

Na het starten voert het model de volgende bewerkingen uit:
- Het gereedschap voor GRASS v.to.rast.attribute converteert contour hoogtelijnen naar raster, met het contour-shapefile, de naam van het Z-veld en de rasterresolutie als invoer;
- Het gereedschap voor GRASS r.surf.contour genereert het hoogtemodel, met als invoer de gerasteriseerde tijdelijke uitvoer uit de vorige stap en de rasterresolutie;
- Het gereedschap voor GDAL "gdaldem" genereert de helling, uitgedrukt in graden, uit het hoogtemodel;
- Het gereedschap voor GRASS r.mapcalculator wordt gebruikt om een 1 bit raster te genereren dat gebieden identificeert met een helling die groter is dan 15 graden (deze waarde is gecodeerd in de richtlijnen voor microzonering en dus een vaste waarde), met behulp van de expressie:

if(A\>15,1,null())

waar A het tijdelijke hellingsraster is dat werd gegenereerd door gdaldem;
- Het gereedschap voor GDAL "gdal_polygonize" converteert het 1 bit raster naar polygonen;
- Het gereedschap voor QGIS "Intersection" wordt gebruikt om de gebieden te overleggen met een helling van 15 graden met de gekozen laag met kruisingen.

Het resultaat is een polygoonlaag met gebieden die gevoelig zijn voor instabiliteit vanwege een hellingswaarde van meer dan 15 graden, automatisch uitgenomen uit een thematische kaart, zoals een polygoonlaag van aardverschuivingen (Fig. 3) of een lithologische kaart.

![(Fig. 3) The model output (in red) shows highly unstable areas extracted from a landslides layer (orange).](./images/italy_igag3.png){.align-right}
## Conclusies
Dit werk demonstreert helder dat open source GIS-gereedschappen, zoals QGIS, GRASS, GDAL/OGR, met succes kunnen worden gebruikt voor ruimtelijke analyses en het verwerken van gegevens die zijn gericht op studies voor seismische microzonering op het eerste niveau. In dit voorbeeldwerk is QGIS gebruikt als een vereenvoudigde en geünificeerde interface voor verschillende gereedschappen van hoge kwaliteit voor GFOSS. Grafische modellen bouwen maakt het mogelijk intuïtieve modellen voor geoprocessing te maken die eenvoudig kunnen worden gedeeld als draagbare gereedschappen en voor verschillende platformen, die geen dure softwarelicenties vergen. Het gereedschap koppelt de mogelijkheid voor het maken van modellen van QGIS aan een grafische keten van verschillende algoritmen, het definiëren van parameters voor invoer en uitvoer en laat het aan de software over om de tussenliggende gegevensuitvoer te beheren. Het gebruiken van algoritmen van GRASS vereist niet het definiëren en gebruiken van een database en mapset voor GRASS, wat het ontwerpen van het model enorm vereenvoudigt. Toekomstige ontwikkelingen omvatten het maken van een pakket gereedschappen en modellen, gebaseerd op open source-software, die kunnen worden gebruikt om taken van ruimtelijke analyses die nodig zijn voor seismische microzonering te vereenvoudigen en te versnellen.
## Verwijzingen
- G. Baldassarre; Gallicchio, S.; Giannandrea, P. & Tropeano, M.: \"Relazione Finale Geolitologica per la microzonazione sismica di livello 1dei Comuni della Provincia di Foggia Dipartimento di Geologia e Geofisica dell\'Università di Bari, 2011\"
- Cavinato,G.P.; Cavuoto, G.; Coltella, M.; Cosentino, G.; Paolucci, E.; Peronace, E. & Simionato, M.: \"Studio di fattibilità per il monitoraggio e la messa in sicurezza delle aree urbane a rischio di stabilità statica e vulnerabilità strutturale del Comune e della Provincia di Foggia -CIPE 20/2004 Consiglio Nazionale delle Ricerche - Istituto di Geologia Ambientale e Geoingegneria, 2013, 526\"
- Contributi per l\'aggiornamento degli \"Indirizzi e criteri per la microzonazione sismica \" 2008. Ingegneria sismica, Pàtron Editore Bologna, 2011 (<http://www.protezionecivile.gov.it/jcms/it/view_pub.wp?contentId=PUB28083>)
- Gruppo di lavoro MS, 2008. Indirizzi e criteri per la microzonazione sismica. Conferenza delle Regioni e delle Province autonome - Dipartimento della protezione civile, Roma, 3 vol. e Dvd, Presidenza del Consiglio dei Ministri, Dipartimento di Protezione Civile, 2008, 424. (<http://www.protezionecivile.gov.it/jcms/it/view_pub.wp?contentId=PUB1137>)

## Auteurs
Dit artikel werd bijgedragen in maart 2015 door Giuseppe Cosentino en Francesco Pennica (www.igag.cnr.it).

![Giuseppe Cosentino](./images/guiseppe_cosentino.png){.align-left height="200px"}

Giuseppe Cosentino \<<g.cosentino@igag.cnr.it>\> is geoloog en technoloog, gespecialiseerd in Geographic Information Systems voor het beheer van geologische en bouwkundige gevaren. Momenteel werkt hij in het veld van seismische microzonering en milieutechnische karakterisering van grond in verontreinigde gebieden. Interesses: geologische en milieugevaren, cartografie, structurele geologie, verkennende boringen.

![Francesco Pennica](./images/francesco_pennica.png){.align-left height="200px"}

Francesco Pennica verschaft GIS en WebGIS softwareontwikkeling en gegevensbeheer: GeoServer, MapServer, ArcGIS Server, GeoNetwork OGC standaard gebaseerde webgisservices, Java, HTML, CSS, Javascript, Python, PHP-talen en frameworks, WebGIS front-end ontwikkeling met OpenLayers, ExtJS, GeoExt, JQuery, GWT, Ext-GWT, Google Maps API SQL, beheer van geodatabases, PostgreSQL, PostGIS, op GIS desktop software gebaseerde analyses en scripten (gereedschappen voor ArcGIS, GRASS, GFOSS), softwareconfiguratie en beheer in op Linux en Windows gebaseerde servers en desktops.
