---
HasBanner: false
archived: true
date: 2013-01-01
draft: false
featured: false
section: project
sidebar: true
thumbnail: images/italy_turin1.jpg
title: Het Research Institute for Geo-hydrological Protection van Turijn —— Luchtfoto
  archiefbeheer
type: case-study

---
{{<content-start >}}
# Het Research Institute for Geo-hydrological Protection van Turijn —— Luchtfoto archiefbeheer
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>1 januari 2013</span>
</p>

Het Research Institute for Geo-hydrological Protection van Turijn (IRPI), lid van de Italian National Research Council (CNR), begon zijn activiteiten in 1970. De sinds de stichting verkregen vaardigheden betreffen verscheidene sectoren voor vervolgonderzoek, bijv. de studie van geologische en hydrogeologische objecten van het Alpine-Po rivierensysteem (Noord-Italië) of het monitoren, voorspellen en voorkomen van natuurrampen. Deze taken worden uitgevoerd door de middel van een multidisciplinaire benadering, inclusief wetenschappen over de aarde, bouwkunde en geomatica.

Modellen maken en analyses van historische records, luchtfotografie worden gebruikt om de uitgebreide onderzoeken en studies uit te voeren, in aanvulling op veldonderzoeken. Hun gebruik varieert van "eenvoudige" visuele analyses tot complex verwerken zoals stereoplotten of segmentatie van afbeeldingen.

Het instituut beheert in zijn archief, voor de vermelde doeleinden, ongeveer 170.000, recente en historische, fotogrammen —— de oudste dateert terug tot de 1920's (Afbeelding 1) —— die, over verschillende jaren, het bassin van de Po of een deel daarvan bedekken. Sommige fotogrammen bedekken andere bassins in Noord-Italië. In aanvulling daarop bevat het archief vluchtplannen van de beschreven fotogrammen (Afbeelding 1).

<figure>
<img src="../images/italy_turin1.jpg" class="align-left" alt="italy_turin1.jpg" />
<figcaption>1929 fotogram (links) en 1954 vluchtplan (rechts).</figcaption>
</figure>

## Archiefbeheer
Een benadering met GIS werd toegepast om om te kunnen gaan met een dergelijke hoeveelheid aan gegevens. Eerst werd elk vluchtplan, dat de voetafdrukken van de fotogrammen weergeeft, gescand, voorzien van geoverwijzingen en gedigitaliseerd naar de indeling shapefile. Daarna werden de fotogrammen gescand op 600 dpi en de bestanden werden benoemd aan de hand van een code die onder meer bestond uit kaartblad, jaar van verkrijgen, nummer van de strip, serienummer van het fotogram en de eigendomscode (IRPI’s of extern).

Elke voetafdruk in het gedigitaliseerde vluchtplan werd in zij attributen voorzien van de eerdere codes om het shapefile te kunnen koppelen aan gescande fotogrammen, door middel van de plug-in eVis (Horning et al, 2009), en om een gebruikersvriendelijke gebruikersinterface ter beschikking te stellen om te zoeken en te verwijzen (Afbeelding 2). Gegevens met betrekking tot de code van het fotogram werden opgeslagen in velden van de attributentabel. Daarna werd, door veldberekening, een veld "Link" gemaakt waarin de paden van het fotogram werden opgeslagen.

<figure>
<img src="../images/italy_turin2.jpg" class="align-left" alt="italy_turin2.jpg" />
<figcaption>Weergave fotogram (eVis Plugin)</figcaption>
</figure>

Meer nog, vanwege de hoeveelheid doorzoekbare gegevens werd een geografische zoekinterface ontwikkeld. Dankzij de mogelijkheden van Grafische modellen maken (in Processing, eerder plug-in SEXTANTE), maakt het ontwikkelde gereedschap, door verschillende maskers voor selectie en voervakken, het de gebruiker mogelijk te selecteren uit drie lagen (administratieve grenzen, kaartbladen en rivieren), een object te zoeken door zijn tabel te bevragen en dat te gebruiken om een gedigitaliseerd vluchtplan te bevragen met het doel om voetafdrukken van fotogrammen te selecteren die snijden met het geselecteerde object (Figure 3). Met deze procedure is het dan mogelijk om het geselecteerde fotogram aan te wijzen en ze eenvoudig weer te geven met het eerder beschreven gereedschap of bestanden van fotogrammen uit te nemen, op hun bestandsnamen en pad, voor verdere verwerking.

<figure>
<img src="../images/italy_turin3.jpg" class="align-left" alt="italy_turin3.jpg" />
<figcaption>Schema van Grafische modellen maken gebruikt in het gereedschap voor selectie (op de achtergrond: paarse polygonen-kaartbladen; gelabelde oranje polygonen-voetafdrukken van fotogrammen; bruine polygonen-gemeentelijke administratieve grenzen)</figcaption>
</figure>

De collectie fotogrammen is van groot belang, zowel in onderzoeks- (bijv. Godone et al, 2014) als in professionele omgevingen (Figure 4). Dankzij de beschreven procedures en gereedschappen is de collectie volledig toegankelijk en sinds 2009 werden de fotogrammen gebruikt in verscheidene projecten, zowel intern als extern bij het Institute. Mogelijkheden en plug-ins van QGIS maakten het ontwikkelen van gereedschappen en procedures mogelijk om het archief van de fotogrammen te optimaliseren, zowel in de in de implementatie van zijn beheer als in zijn exploitatie.

<figure>
<img src="../images/italy_turin4.jpg" class="align-left" alt="italy_turin4.jpg" />
<figcaption>Taartdiagram dat verschillende gebieden weergeeft die fotogrammen gebruikten in het jaar 2013</figcaption>
</figure>

## Verwijzingen
- Godone D., Garbarino M., Sibona E., Garnero G., Godone F. (2014) "Progressive fragmentation of a traditional Mediterranean landscape by hazelnut plantations: The impact of CAP over time in the Langhe region (NW Italy)", Land use policy, ISSN: 0264-8377
- Horning N., Koy K., Ersts P. (2009) "eVis (v1.1.0) User\'s Guide. American Museum of Natural History, Center for Biodiversity and Conservation". Beschikbaar vanaf <http://biodiversityinformatics.amnh.org/>

## Links
- Archief luchtfoto's website: <http://www.irpi.to.cnr.it/index_en.php?page=aerofototeca_en>

## Auteurs
<figure>
<img src="../images/italy_turinaut1.jpg" class="align-left" height="120" alt="italy_turinaut1.jpg" />
<figcaption>Danilo Godone</figcaption>
</figure>

Danilo Godone is een Postdoc grant holder, aan de universiteit van Turijn, die de geomatische bijdragen in landverschuivingen bestudeert, gletsjers en, meer algemeen, natuurrampen monitort. Hij is lid van NATRISK —— Research Centre on Natural Risks in Mountain and Hilly Environments, aan dezelfde universiteit. Hij treedt ook op als freelance consultant voor dezelfde onderwerpen.

<figure>
<img src="../images/italy_turinaut2.jpg" class="align-left" width="120" alt="italy_turinaut2.jpg" />
<figcaption>Franco Godone</figcaption>
</figure>

Franco Godone is een gespecialiseerde technicus aan het Research Institute for Geo-hydrological Protection van Turijn (IRPI-CNR) sinds 1972. Hij is betrokken bij topografische onderzoeken en onderzoeken met metrische luchtfoto's en gegevensanalyse in de alpine regio's.

{{<content-end >}}
