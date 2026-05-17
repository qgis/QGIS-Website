---
draft: 'true'

---
# The Research Institute for Geo-hydrological Protection of Turin \-\-- Aerial photo archive management
Het Research Institute for Geo-hydrological Protection van Turijn (IRPI), lid van de Italian National Research Council (CNR), begon zijn activiteiten in 1970. De sinds de stichting verkregen vaardigheden betreffen verscheidene sectoren voor vervolgonderzoek, bijv. de studie van geologische en hydrogeologische objecten van het Alpine-Po rivierensysteem (Noord-Italië) of het monitoren, voorspellen en voorkomen van natuurrampen. Deze taken worden uitgevoerd door de middel van een multidisciplinaire benadering, inclusief wetenschappen over de aarde, bouwkunde en geomatica.

Modellen maken en analyses van historische records, luchtfotografie worden gebruikt om de uitgebreide onderzoeken en studies uit te voeren, in aanvulling op veldonderzoeken. Hun gebruik varieert van "eenvoudige" visuele analyses tot complex verwerken zoals stereoplotten of segmentatie van afbeeldingen.

The institute, for the explained purposes, keeps in its archive about 170000, recent and historical, photograms \-\-- the oldest one dating back to 1920s (Figure 1) \-\-- covering, in different years, the Po basin or part of it. Some photograms cover other basins in northern Italy. In addition the archives keeps flight plans of the described photograms (Figure 1).

![1929 photogram (left) and 1954 flight plan (right).](./images/italy_turin1.jpg){.align-left}
## Archiefbeheer
Een benadering met GIS werd toegepast om om te kunnen gaan met een dergelijke hoeveelheid aan gegevens. Eerst werd elk vluchtplan, dat de voetafdrukken van de fotogrammen weergeeft, gescand, voorzien van geoverwijzingen en gedigitaliseerd naar de indeling shapefile. Daarna werden de fotogrammen gescand op 600 dpi en de bestanden werden benoemd aan de hand van een code die onder meer bestond uit kaartblad, jaar van verkrijgen, nummer van de strip, serienummer van het fotogram en de eigendomscode (IRPI’s of extern).

Elke voetafdruk in het gedigitaliseerde vluchtplan werd in zij attributen voorzien van de eerdere codes om het shapefile te kunnen koppelen aan gescande fotogrammen, door middel van de plug-in eVis (Horning et al, 2009), en om een gebruikersvriendelijke gebruikersinterface ter beschikking te stellen om te zoeken en te verwijzen (Afbeelding 2). Gegevens met betrekking tot de code van het fotogram werden opgeslagen in velden van de attributentabel. Daarna werd, door veldberekening, een veld "Link" gemaakt waarin de paden van het fotogram werden opgeslagen.

![Photogram display (eVis Plugin)](./images/italy_turin2.jpg){.align-left}

Meer nog, vanwege de hoeveelheid doorzoekbare gegevens werd een geografische zoekinterface ontwikkeld. Dankzij de mogelijkheden van Grafische modellen maken (in Processing, eerder plug-in SEXTANTE), maakt het ontwikkelde gereedschap, door verschillende maskers voor selectie en voervakken, het de gebruiker mogelijk te selecteren uit drie lagen (administratieve grenzen, kaartbladen en rivieren), een object te zoeken door zijn tabel te bevragen en dat te gebruiken om een gedigitaliseerd vluchtplan te bevragen met het doel om voetafdrukken van fotogrammen te selecteren die snijden met het geselecteerde object (Figure 3). Met deze procedure is het dan mogelijk om het geselecteerde fotogram aan te wijzen en ze eenvoudig weer te geven met het eerder beschreven gereedschap of bestanden van fotogrammen uit te nemen, op hun bestandsnamen en pad, voor verdere verwerking.

![Graphic modeler scheme used in the selection tool (in background: purple polygons-map sheets; labeled orange polygons-photogram footprints; brown polygons-municipalities administrative borders)](./images/italy_turin3.jpg){.align-left}

De collectie fotogrammen is van groot belang, zowel in onderzoeks- (bijv. Godone et al, 2014) als in professionele omgevingen (Figure 4). Dankzij de beschreven procedures en gereedschappen is de collectie volledig toegankelijk en sinds 2009 werden de fotogrammen gebruikt in verscheidene projecten, zowel intern als extern bij het Institute. Mogelijkheden en plug-ins van QGIS maakten het ontwikkelen van gereedschappen en procedures mogelijk om het archief van de fotogrammen te optimaliseren, zowel in de in de implementatie van zijn beheer als in zijn exploitatie.

![Pie chart showing different area of interest employing photograms in year 2013](./images/italy_turin4.jpg){.align-left}
## Verwijzingen
- Godone D., Garbarino M., Sibona E., Garnero G., Godone F. (2014) "Progressive fragmentation of a traditional Mediterranean landscape by hazelnut plantations: The impact of CAP over time in the Langhe region (NW Italy)", Land use policy, ISSN: 0264-8377
- Horning N., Koy K., Ersts P. (2009) "eVis (v1.1.0) User\'s Guide. American Museum of Natural History, Center for Biodiversity and Conservation". Beschikbaar vanaf <http://biodiversityinformatics.amnh.org/>

## Links
- Archief luchtfoto's website: <http://www.irpi.to.cnr.it/index_en.php?page=aerofototeca_en>

## Auteurs
![Danilo Godone](./images/italy_turinaut1.jpg){.align-left height="120px"}

Danilo Godone is a Postdoc grant holder, at Turin University, studying geomatic contribution in landslide, glacier and, more generally, natural disasters monitoring. He is a member of NATRISK \-\-- Research Centre on Natural Risks in Mountain and Hilly Environments, in the same University. He acts as a freelance consultant in the same topics, too.

![Franco Godone](./images/italy_turinaut2.jpg){.align-left width="120px"}

Franco Godone is een gespecialiseerde technicus aan het Research Institute for Geo-hydrological Protection van Turijn (IRPI-CNR) sinds 1972. Hij is betrokken bij topografische onderzoeken en onderzoeken met metrische luchtfoto's en gegevensanalyse in de alpine regio's.
