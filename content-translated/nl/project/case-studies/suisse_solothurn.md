---
HasBanner: false
archived: true
date: 2009-05-01
draft: false
featured: false
section: project
sidebar: true
thumbnail: images/suisse_solothurn1.png
title: QGIS in de gouvernementele stapel FOSSGIS van het Canton van Solothurn in Zwitserland
type: case-study

---
{{<content-start >}}
# QGIS in de gouvernementele stapel FOSSGIS van het Canton van Solothurn in Zwitserland
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>1 mei 2009</span>
</p>

![](../images/suisse_solothurn1.png)

Het Kanton Solothurn verschaft services en infrastructuur aan 250,000 inwoners van Solothurn. In het jaar 2001 besliste het Staatsparlement om te migreren van Windows naar Linux. De motivatie was om onafhankelijk te zijn van één leverancier, om vrije handel aan te moedigen en licentiekosten te reduceren. Als  resultaat daarvan begon het SO!GIS departement van het Kanton Solothurn met het leveren van vereisten voor GIS van meer dan 3500 werknemers met een FOSSGIS-strategie.

De eerste stap die we namen was het introduceren van UMN MapServer en het maken van een cliënt voor SO!MAP die een eenvoudig te gebruiken WebGIS-cliënt biedt voor alle 3500 werknemers. De tweede stap was de migratie van al onze geo-ruimtelijke gegevens van Shapefiles naar de voorziening van de PostGIS ruimtelijke database. De introductie was erg succesvol, maar een eenvoudig te gebruiken desktop GIS ontbrak.

Na evaluatie van verschillende Desktop GIS-sen besloten we QGIS te gebruiken in samenwerking met GRASS, door ESRI ArcInfo en ArcView3 te vervangen in 2006.

De beslissing werd ingegeven door de volgende aspecten:
- Vanwege het gebruik van desktop GIS in een Linux Terminal Server-omgeving was Java geen optie.
- OSGeo Projectorganisatie
- GUI vertaald in de Duitse taal
- Documentatie geschreven in de Duitse taal
- Een actieve ontwikkelaar (Marco Hugentobler) nabij Solothurn in Zwitserland.
- We konden Marco Hugentobler contracteren om ontbrekende mogelijkheden, zoals Digitaliseren en Printvormgeving, te implementeren.
- Ontwikkeling van toepassing en plug-ins met Python
- Groeiende gebruikersgemeenschap
- Zeer actieve gemeenschap van ontwikkelaar
- Onafhankelijkheid van één enkel besturingssysteem

## Waar gebruiken we QGIS
In tegenstelling tot de interactieve kaarten die worden geboden door UMN MapServer, moet de desktop GIS een flexibele weergave bieden op de geo-ruimtelijke gegevens van Solothurn. QGIS Desktop GIS is voor hun dagelijkse werk in gebruik bij meer dan 50 gebruikers. Maar veel van hen zijn geen experts in GIS. Zij willen geo-ruimtelijke gegevens visualiseren en/of vastleggen met een intuïtieve gebruikersinterface.

Een van de belangrijkste problemen met Desktop GIS is de vraag: \"Hoe krijg ik de informatie die ik nodig heb uit de opslagplaats van PostGIS geogegevens?\". Omdat onze eindgebruikers niet bekend zijn met gegevensmodellen en de onderliggende structuren van onze ruimtelijke database, was het aanbieden van een ruwe verbinding naar de database van PostGIS DB geen optie. We hebben een database van metadata die de beschrijving van alle productiegegevens opslaat, genaamd \'SO!DATA\'.

SO!DATA bevat een menselijk leesbare inventaris van de gegevensmodellen en de niet GIS-Experts-gebruikers zijn in staat deze database te gebruiken om de informatie die zij nodig hebben op te zoeken.

<figure>
<img src="../images/suisse_solothurn2.png" class="align-right" alt="suisse_solothurn2.png" />
<figcaption>Plug-in "SO!GIS Layer", ontwikkeld in het Kanton Solothurn</figcaption>
</figure>

Een plug-in is in Python ontwikkeld om de noodzaak voor eindgebruikers om direct te interacteren met de verbindingen met PostGIS en dialoogvensters voor tabelselectie. De plug-in is genaamd \"SO!GIS Layer\" (zie Afbeelding 1). De plug-in verbindt met de opslagplaats van SO!GIS PostGIS, haalt de informatie van alle gepubliceerde geo-ruimtelijke gegevenslagen uit SO!DATA en biedt de gebruiker een gebruikersinterface om de gegevenslagen te zoeken die nodig zijn. Met deze infrastructuur op zijn plaats zijn onze gebruikers tevreden —— ze kunnen op een individuele manier geo-verwerking voorbereiden en lay-outs voor kaarten bewerken.

<figure>
<img src="../images/suisse_solothurn3.png" class="align-right" alt="suisse_solothurn3.png" />
<figcaption>Plug-in "SO!GIS Suche", ontwikkeld in het Kanton Solothurn</figcaption>
</figure>

Een andere vereiste plug-in voor QGIS die we hebben gemaakt, is genaamd \'SO!GIS Suche\'. Dit verschaft de mogelijkheid om te zoeken naar locaties zoals dorpen, adressen of kadastrale percelen (zie Afbeelding 2). Als resultaat daarvan kan de gebruiker heel eenvoudig naar een gebied van interesse navigeren.

Op dit moment worden nog veel meer plug-ins ontwikkeld. Deze zullen het bewerken van gegevens, analyses of maken van kaarten voor verschillende projecten ondersteunen. Onze plug-ins in ontwikkeling omvatten onderwerpen zoals natuurreservaten, conservatie van de bodem, verificatie van kadastrale gegevens, crisisbeheer, verlaten gebieden enzovoort.
## Conclusie
Vandaag kunnen we zeggen dat het gebruiken van QGIS voor ons de juiste beslissing was. QGIS biedt de meeste mogelijkheden die onze gebruikers nodig hebben. Het Kanton Solothurn subcontracteert het maken van mogelijkheden die ontbreken in QGIS aan commerciële verschaffers van ondersteuning. Met PyQgis en PyQt zijn er excellente opties voor gemakkelijke in-huisontwikkeling van toepassingen, gebaseerd op QGIS. Een groot voordeel is het onbeperkte aantal installaties. Iedereen die QGIS dient te gebruiken, kan het zonder beperkingen gebruiken. Om de ontwikkeling van QGIS te stimuleren heeft het Kanton Solothurn elk jaar ongeveer \$30,000 in QGIS geïnvesteerd, sinds 2007. Dit is veel efficiënter en doelgerichter dan het betalen van ondersteuning in de zwarte doos van onze voormalige softwareverschaffer. Los van het gebruiken van FOSSGIS, verschaft het Kanton Solothurn ook publieke geodata, zonder kosten, via het webportaal SO!ONLINE.
## Auteur
<figure>
<img src="../images/suisse_solothurnaut.jpg" class="align-left" height="200" alt="suisse_solothurnaut.jpg" />
<figcaption>Horst Düster</figcaption>
</figure>

Dit artikel werd bijgedragen in mei 2009 door Dr. Horst Düster. Hij is GIS-coördinator aan het Departement van Geoinformatie in het Canton van Solothurn, Zwitserland.

{{<content-end >}}
