---
HasBanner: false
archived: true
date: 2017-12-31
draft: false
featured: false
section: project
sidebar: true
thumbnail: images/usa_polczynski_table1.png
title: Historische Gazetteer van de Krim
type: case-study

---
{{<content-start >}}
# Historische Gazetteer van de Krim
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>31 december 2017</span>
</p>

Elke dag genereren Ottomanen over de gehele waardevol materiaal zoals componenten van hun research voor hun studies, maar dit materiaal is vaak niet beschikbaar voor studenten met dezelfde interesses. Het doel van de OpenOttoman (Amy Singer, OpenOttoman: A Collaborative Platform for Digital Scholarship, https://networks.hnet.org/node/11419/discussions/166360/openottoman-collaborative-platform-digital-scholarship, 2017) is om het genereren van dergelijk materiaal te stimuleren en open en handige toegang te verschaffen tot dit materiaal. Het OpenOttoman Portal (http://www.openottoman.org) (OOP) is één mogelijkheid om toegang te verkrijgen tot dit materiaal. Materiaal dat beschikbaar is via OOP omvat databases, met als een voortreffelijk voorbeeld een gazetteer te zijn voor Ottomaanse plaatsen in de wereld. Hier beschrijven we de Historical Gazetteer of the Crimea (HGC), een prototype OOP gazetteer die bewoonde plaatsen, districten en provincies van de Krim omvat zoals die bestonden aan het einde van het kanaat van de Krim.

De primaire gegevensbron voor de databases van HGC is Jankowski\’s woordenboek van vóór-Russische plaatsen in de Krim (Henryk Jankowski, Historical-Etymological Dictionary of Pre-Russian Habitation Names of the Crimea, Brill, Leiden, 2006). Deze bron bevat een kaart die de locaties weergeeft van 137 bewoonde plaatsen, waarvan 99 die zijn geassocieerd met bestaande plaatsen die zijn opgenomen in de database van GeoNames. Dit zijn de items voor bewoonde plaatsen in de HGC, met lengte- en breedtegraad voor deze plaatsen die zijn opgehaald uit de database van GeoNames.

Jankowski\’s kaart geeft ook grenzen voor zes provincies en 43 districten weer. Locaties van HGC voor deze objecten zijn geschatte zwaartepunten voor de regio met behulp van de grenzen die worden weergegeven op de kaart van Jankowski. De HGC bevat items voor 14 van de 16 weergegeven rivieren die worden weergegeven op Jankowski\’s kaart, plus 61 aanvullende rivieren die zijn opgenomen om te helpen bij het lokaliseren van bewoonde plaatsen en grenzen van district en provincie.

Hoogtegegevens voor het terrein (Shuttle Radar Topography Mission (SRTM), beschikbaar op <https://lta.cr.usgs.gov/SRTM1Arc>) werden ingepast in een basiskaart voor de regio die wordt bedekt door Jankowski\’s kaart.  Grenzen voor districten en provincies werden geschat met behulp van de kaart van Jankowski, plus objecten in het terrein, zoals rivieren, lijnen van bergkammen en valleien, omdat grenzen op de kaart van Jankowski moeilijk te traceren waren. Gazetteerlocaties voor rivieren zijn de lengte- en breedtegraad van de monding van de rivier, genomen uit de database van GeoNames. Per Tabel 1 omvat de HGC drie afzonderlijke sets van databases waartoe toegang kan worden verkregen op <http://epublications.marquette.edu/ottoman_crimea/>.  Deze website verschaft ook toegang tot een project genaamd HGC-QGIS-Project.qgs. Openen van het project in QGIS geeft het resultaat dat wordt weergegeven in Afbeelding 1. Voor de KML- en shapefiledatabase voor rivieren werden rivieren getraceerd in QGIS met behulp van de fysieke kaart van Google Maps.

<figure>
<img src="../images/usa_polczynski_table1.png" class="align-right" alt="usa_polczynski_table1.png" />
<figcaption>Tabel 1: Gazetteer databases</figcaption>
</figure>

Openen van het project in QGIS geeft het resultaat dat wordt weergegeven in Afbeelding 1. Voor de KML- en shapefiledatabase voor rivieren werden rivieren getraceerd in QGIS met behulp van de fysieke kaart van Google Maps.

<figure>
<img src="../images/usa_polczynski_figure1.png" class="align-right" alt="usa_polczynski_figure1.png" />
<figcaption>Afbeelding 1: HGC-QGIS-Project.qgs geopend in QGIS.</figcaption>
</figure>

Tabel 2 geeft de velden van de database van HGC weer. Merk de manier op waarop een unieke ID wordt toegewezen aan elke plaats in de database. Omdat elke plaats op de kaart van Jankowski is geassocieerd met een plaats in de database van GeoNames, en omdat elke plaats in de database van GeoNames als URL een unieke ID is gegeven, dient de URL van GeoNames voor de plaats als een unieke identificatie voor de plaats in HGC.

<figure>
<img src="../images/usa_polczynski_table2.png" class="align-right" alt="usa_polczynski_table2.png" />
<figcaption>Tabel 2: HGC databasevelden.</figcaption>
</figure>

Onthoud dat de ID kan worden geopend in een webbrowser, waarbij automatisch een kaart van GeoNames wordt weergegeven met de bewoonde plaats als het centrum, zoals weergegeven in Afbeelding 2.

<figure>
<img src="../images/usa_polczynski_figure2.png" class="align-right" alt="usa_polczynski_figure2.png" />
<figcaption>Afbeelding 2: Openen van de URL-ID voor Qarağy in een webbrowser.</figcaption>
</figure>

Voor Tabel 2 zijn de velden voor de district-, provincie- en de rivierendatabases dezelfde velden voor bewoonde plaatsen, met als uitzondering dat het veld Page leeg is gelaten, omdat districten, provincies en rivieren niet als items voorkomen in Jankowski\’s woordenboek.  Districten, provincies en rivieren worden op dezelfde manier URL-ID's toegewezen als waarop ze worden toegewezen aan bewoonde plaatsen. Dus in Tabel 2 het Part of field voor de bewoonde plaats Qarağy is de URL van GeoNames voor Tarɣan, het district waarin deze plaats ligt. De velden Code en Class gebruiken de naamgeving die wordt gebruikt in de database van GeoNames. Als voorbeeld: de code P is gewoonlijk van toepassing voor bewoonde plaatsen, en de klasse PPLH (sub-code) is van toepassing voor historische bewoonde plaatsen die niet langer bestaan.

Het veld Confidence reflecteert de mate van betrouwbaarheid van de gegevens die zijn opgenomen in een bepaald item van de database. Omdat alle bewoonde plaatsen in de HGC kunnen worden geassocieerd met bestaande plaatsen in de database van GeoNames, wordt een betrouwbaarheidsniveau van 1 toegekend. Rivieren krijgen ook een betrouwbaarheidsniveau van 1, omdat ze direct zijn getraceerd vanaf Google Maps.

Waar het een nuttige gazetteer verschaft, was een primair doel van de HGC om te dienen als testomgeving en als gebruiksmogelijkheid voor hoe andere Ottomaanse wereldgazetteers zouden kunnen worden ingepast in de OOP. Gebaseerd op de ervaring die uit dit project werd verkregen, werd een nieuw project geïnitieerd om ongeveer 3000 bewoonde plaatsen, rivieren, oversteekplaatsen in rivieren, stroomversnellingen, eilanden, bossen, bergen en valleien, die zijn te vinden op een set van kaarten uit de 17e eeuw van Oekraïne, geproduceerd door Guillaume Le Vasseur, sieur de Beauplan, te voorzien van geoverwijzingen. Dit project ondersteunt direct een van de onderzoeken van de belangrijkste onderzoeker over de grens van de Pools-Litouwse gemeenschap/Ottomaanse Rijk. Meer in het algemeen beantwoordt dit werk de vraag naar gazetteers voor de Ottomaanse wereld, zoals uitgesproken door het OpenOttoman initiatief (<http://openottoman.org>).
## Auteurs
Afbeelding 3: Michael en Mark Polczynski

<figure>
<img src="../images/usa_polczynski_authors.jpg" class="align-left" alt="usa_polczynski_authors.jpg" />
<figcaption>Michael en Mark Polczynski</figcaption>
</figure>

Michael Polczynski (<Michael.Polczynski@georgetown.edu>) is een lector aan de Georgetown University, waar zijn werk focust op vroegmoderne Ottomaanse en Oost-/Centraal-Europese geschiedenis, geschiedenis van grenzen, historische geografie, diplomatie, en intellectuele geschiedenis. Michael studeert ook laatmiddeleeuwse Euraziatische geschiedenis en 19e-eeuwse Europese emigranten in het Ottomaanse Rijk en werkt uitgebreid met historisch GIS en beheert verscheidene online academische gemeenschappen.

Mark Polczynski (<mark.polczynski@marquette.edu>) is gepensioneerd van Marquette University’s College of Engineering, en verschaft momenteel technische assistentie aan OpenOttoman (openottoman.org), een ontwikkeling van transnationale digitale samenwerking van scholing en publieke geschiedenis, gefocust op de Ottomaanse wereld.

{{<content-end >}}
