---
draft: 'true'

---
# Historische Gazetteer van de Krim
Every day, Ottomanists around the world generate valuable materials as components of their scholarly research, but these materials may not be readily available to scholars with similar interests. The purpose of the OpenOttoman (Amy Singer, OpenOttoman: A Collaborative Platform for Digital Scholarship, <https://networks.hnet.org/node/11419/discussions/166360/openottoman-collaborative-platform-digital-scholarship>, 2017) is to stimulate generation of such materials and provide open and convenient access to these materials. The OpenOttoman Portal (<http://> www.openottoman.org) (OOP) is one vehicle for accessing these materials. Materials made available through the OOP include databases, with a prime example being gazetteers of Ottoman world places. Here, we describe the Historical Gazetteer of the Crimea (HGC), a prototype OOP gazetteer that includes populated places, districts, and provinces of Crimea in existence at the end of the Crimean Khanate.

De primaire gegevensbron voor de databases van HGC is Jankowski\’s woordenboek van vóór-Russische plaatsen in de Krim (Henryk Jankowski, Historical-Etymological Dictionary of Pre-Russian Habitation Names of the Crimea, Brill, Leiden, 2006). Deze bron bevat een kaart die de locaties weergeeft van 137 bewoonde plaatsen, waarvan 99 die zijn geassocieerd met bestaande plaatsen die zijn opgenomen in de database van GeoNames. Dit zijn de items voor bewoonde plaatsen in de HGC, met lengte- en breedtegraad voor deze plaatsen die zijn opgehaald uit de database van GeoNames.

Jankowski\’s kaart geeft ook grenzen voor zes provincies en 43 districten weer. Locaties van HGC voor deze objecten zijn geschatte zwaartepunten voor de regio met behulp van de grenzen die worden weergegeven op de kaart van Jankowski. De HGC bevat items voor 14 van de 16 weergegeven rivieren die worden weergegeven op Jankowski\’s kaart, plus 61 aanvullende rivieren die zijn opgenomen om te helpen bij het lokaliseren van bewoonde plaatsen en grenzen van district en provincie.

Hoogtegegevens voor het terrein (Shuttle Radar Topography Mission (SRTM), beschikbaar op <https://lta.cr.usgs.gov/SRTM1Arc>) werden ingepast in een basiskaart voor de regio die wordt bedekt door Jankowski\’s kaart.  Grenzen voor districten en provincies werden geschat met behulp van de kaart van Jankowski, plus objecten in het terrein, zoals rivieren, lijnen van bergkammen en valleien, omdat grenzen op de kaart van Jankowski moeilijk te traceren waren. Gazetteerlocaties voor rivieren zijn de lengte- en breedtegraad van de monding van de rivier, genomen uit de database van GeoNames. Per Tabel 1 omvat de HGC drie afzonderlijke sets van databases waartoe toegang kan worden verkregen op <http://epublications.marquette.edu/ottoman_crimea/>.  Deze website verschaft ook toegang tot een project genaamd HGC-QGIS-Project.qgs. Openen van het project in QGIS geeft het resultaat dat wordt weergegeven in Afbeelding 1. Voor de KML- en shapefiledatabase voor rivieren werden rivieren getraceerd in QGIS met behulp van de fysieke kaart van Google Maps.

![Table 1: Gazetteer databases](./images/usa_polczynski_table1.png){.align-right}

Openen van het project in QGIS geeft het resultaat dat wordt weergegeven in Afbeelding 1. Voor de KML- en shapefiledatabase voor rivieren werden rivieren getraceerd in QGIS met behulp van de fysieke kaart van Google Maps.

![Figure 1: HGC-QGIS-Project.qgs opened in QGIS.](./images/usa_polczynski_figure1.png){.align-right}

Tabel 2 geeft de velden van de database van HGC weer. Merk de manier op waarop een unieke ID wordt toegewezen aan elke plaats in de database. Omdat elke plaats op de kaart van Jankowski is geassocieerd met een plaats in de database van GeoNames, en omdat elke plaats in de database van GeoNames als URL een unieke ID is gegeven, dient de URL van GeoNames voor de plaats als een unieke identificatie voor de plaats in HGC.

![Table 2: HGC database fields.](./images/usa_polczynski_table2.png){.align-right}

Onthoud dat de ID kan worden geopend in een webbrowser, waarbij automatisch een kaart van GeoNames wordt weergegeven met de bewoonde plaats als het centrum, zoals weergegeven in Afbeelding 2.

![Figure 2: Opening the URL ID for Qarağy in a web browser.](./images/usa_polczynski_figure2.png){.align-right}

Voor Tabel 2 zijn de velden voor de district-, provincie- en de rivierendatabases dezelfde velden voor bewoonde plaatsen, met als uitzondering dat het veld Page leeg is gelaten, omdat districten, provincies en rivieren niet als items voorkomen in Jankowski\’s woordenboek.  Districten, provincies en rivieren worden op dezelfde manier URL-ID's toegewezen als waarop ze worden toegewezen aan bewoonde plaatsen. Dus in Tabel 2 het Part of field voor de bewoonde plaats Qarağy is de URL van GeoNames voor Tarɣan, het district waarin deze plaats ligt. De velden Code en Class gebruiken de naamgeving die wordt gebruikt in de database van GeoNames. Als voorbeeld: de code P is gewoonlijk van toepassing voor bewoonde plaatsen, en de klasse PPLH (sub-code) is van toepassing voor historische bewoonde plaatsen die niet langer bestaan.

Het veld Confidence reflecteert de mate van betrouwbaarheid van de gegevens die zijn opgenomen in een bepaald item van de database. Omdat alle bewoonde plaatsen in de HGC kunnen worden geassocieerd met bestaande plaatsen in de database van GeoNames, wordt een betrouwbaarheidsniveau van 1 toegekend. Rivieren krijgen ook een betrouwbaarheidsniveau van 1, omdat ze direct zijn getraceerd vanaf Google Maps.

Waar het een nuttige gazetteer verschaft, was een primair doel van de HGC om te dienen als testomgeving en als gebruiksmogelijkheid voor hoe andere Ottomaanse wereldgazetteers zouden kunnen worden ingepast in de OOP. Gebaseerd op de ervaring die uit dit project werd verkregen, werd een nieuw project geïnitieerd om ongeveer 3000 bewoonde plaatsen, rivieren, oversteekplaatsen in rivieren, stroomversnellingen, eilanden, bossen, bergen en valleien, die zijn te vinden op een set van kaarten uit de 17e eeuw van Oekraïne, geproduceerd door Guillaume Le Vasseur, sieur de Beauplan, te voorzien van geoverwijzingen. Dit project ondersteunt direct een van de onderzoeken van de belangrijkste onderzoeker over de grens van de Pools-Litouwse gemeenschap/Ottomaanse Rijk. Meer in het algemeen beantwoordt dit werk de vraag naar gazetteers voor de Ottomaanse wereld, zoals uitgesproken door het OpenOttoman initiatief (<http://openottoman.org>).
## Auteurs
Afbeelding 3: Michael en Mark Polczynski

![Michael and Mark Polczynski](./images/usa_polczynski_authors.jpg){.align-left}

Michael Polczynski (<Michael.Polczynski@georgetown.edu>) is een lector aan de Georgetown University, waar zijn werk focust op vroegmoderne Ottomaanse en Oost-/Centraal-Europese geschiedenis, geschiedenis van grenzen, historische geografie, diplomatie, en intellectuele geschiedenis. Michael studeert ook laatmiddeleeuwse Euraziatische geschiedenis en 19e-eeuwse Europese emigranten in het Ottomaanse Rijk en werkt uitgebreid met historisch GIS en beheert verscheidene online academische gemeenschappen.

Mark Polczynski (<mark.polczynski@marquette.edu>) is gepensioneerd van Marquette University’s College of Engineering, en verschaft momenteel technische assistentie aan OpenOttoman (openottoman.org), een ontwikkeling van transnationale digitale samenwerking van scholing en publieke geschiedenis, gefocust op de Ottomaanse wereld.
