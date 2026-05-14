---
draft: 'true'

---
# Het gebruiken van QGIS in de infrastructuur voor geogegevens in de stad Uster
De stad Uster gebruikt QGIS sinds 2007. Aangemoedigd door de beslissing van het kanton Solothurn om QGIS te gebruiken als Desktop GIS als vervanging voor ArcView, Uster besloot om et ook een kans te geven. De stad sloot aan bij de inspanningen voor verdere ontwikkeling van de toepassing QGIS, door nieuwe mogelijkheden voor te stellen en te testen en door de ontwikkeling financieel te steunen. Als tegenprestatie ontving Uster een snel evoluerend en platformonafhankelijk Desktop GIS en oplossing voor WebGIS, gesteund door een wereldwijde gebruikers- en ontwikkelgemeenschap.

![](./images/suisse_uster1.png){.align-right}

Postgis/PostgreSQL wordt gebruikt als centrale opslag voor geogegevens. Andere databases en gegevensbronnen worden gerepliceerd naar PostgreSQL met een regelmatige, met behulp van gereedschappen als OGR en FME. In het begin werd QGIS voornamelijk gebruikt als een viewer. De eerste QGIS-gebruiker was een boer die de taak had om de declaraties die werden ingediend door lokale boeren voor het ontvangen van landbouwsubsidies te controleren. Later werd QGIS ook geïntroduceerd als een gegevensbewerker en platform voor het publiceren van kaarten, tezamen met de verbeteringen aan de gereedschappen voor bewerken en de printvormgeving. Samenmet andere Zwitserse QGIS-gebruikers (Solothurn, Thun en CDE (Universiteit van Bern)) coördineren en sponsoren wij de verbeteringen van deze gereedschappen, naast enkele verbeteringen in de door gegevens gestuurde symbolisering, geautomatiseerd labelen, afhandeling van attributen en formulieren.

![](./images/suisse_uster2.png){.align-right}

De stadsadministratie gebruikt ook commerciële GIS software: Autodesk Topobase, voor het vastleggen en bewerken van gegevens van de kadastrale en afvalwater-infrastructuur, en GE Smallworld voor het beheren van netwerken voor gas, water en elektriciteit. Dit zijn echter expertsystemen die in gebruik zijn bij speciaal getrainde werknemers. Alle andere GIS-projecten en het bekijken van alle gegevens wordt afgehandeld door QGIS.

In the second half of 2010, first tests with QGIS server were carried out. In 2011 we introduced a new WebGIS system based on the QGIS WMS server and GeoExt/OpenLayers as the web client. The main reasons for the decision to use QGIS server were the considerable time savings made possible by re-using the existing QGIS desktop project configurations, rather than having to manage parallel Web project configurations. Additional advantages are the rich set of symbolization and labeling options and the consistent map rendering between the Desktop GIS application and the Web-GIS. The QGIS webclient can be tested and used at <http://gis.uster.ch/>

![](./images/suisse_uster3.png){.align-right}

Tegenwoordig wordt QGIS gebruikt voor de volgende GIS-projecten:
- bekijken van gegevens voor afvalwater, integratie van aanvullende databases en directe toegang tot video's van afvoerkanalen en protocollen voor inspectie
- bekijken en bewerken voor het monitoren en de milieutechnische en stedelijke planning van afvalwater en hydrologische systemen (Duits: Genereller Entwässerungsplan)
- bekijken van ondergrondse kadastrale gegevens (afvalwater, netwerken voor water, gas en elektriciteit, later ook telecommunicatie) (Duits: Leitungskataster)
- bekijken van kadastrale en onderzoeksgegevens
- bekijken en bewerken van de communale inventaris van beschermde natuurgebieden
- bekijken en bewerken van gegevens voor stedelijke en regionale planning
- bekijken en bewerken van gegevens van de infrastructuur voor wegen
- bekijken van statistieken, direct gegenereerd vanuit de database voor huidige en oudere inwoners
- planning en visualisatie voor planning van energie  (regionale gasvoorziening, gebruiken van warmte uit afvalwater, geothermische energie nabij oppervlakte, blokverwarming van stations, etc.)

Aanvullende projecten zijn momenteel in ontwikkeling.

![](./images/suisse_uster4.png){.align-right}

In 2007 was nog niet geheel duidelijk met welke snelheid QGIS verder zou worden ontwikkeld en hoe zowel de gemeenschap als de commerciële ondersteuning zou evolueren. Vandaag kan worden gezegd dat de snelheid van ontwikkeling en de door de gemeenschap van QGIS gemaakte verbeteringen onze verwachtingen overtroffen. Gemeenschap en commerciële ondersteuning van de bedrijven Sourcepole en Norbit is fantastisch. Er is directe communicatie met ontwikkelaars zonder te worden afgeschermd door productmanagement of verkoopteam. De ontwikkelaars van deze twee bedrijven zijn ook hoofdontwikkelaars van het project QGIS en hebben een uitstekende kennis van de codebasis.

Problemen worden vaak binnen uren of dagen na het melden opgelost en nieuwe ontwikkelen worden binnen een kort tijdframe geïmplementeerd. Nieuwe mogelijkheden kunnen direct worden getest nadat ze zijn ontwikkeld en zijn uitgezet voor de gebruikers als de kwaliteit goed genoeg is voor de eindgebruiker. Er is geen reden om te wachten op officiële uitgaven van de software. We waarderen de vrijheid om het project te kunnen beïnvloeden en de software te kunnen installeren op zoveel computers als we willen zonder afhankelijk te zijn van het beheer van licenties. We kijken uit naar de toekomstige samenwerking met de gemeenschap van QGIS en onze commerciële ondersteuners voor de voortgang van het project QGIS.
## Auteur
![Andreas Neumann](./images/suisse_usteraut.jpg){.align-left height="200px"}

Dit artikel werd bijgedragen in april 2011 door Dr. Andreas Neumann. Hij is de GIS-coördinator van de stad Uster, Zwitserland.
