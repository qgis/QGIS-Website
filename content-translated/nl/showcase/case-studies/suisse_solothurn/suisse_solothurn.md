---
draft: 'true'

---
# QGIS in de gouvernementele stapel FOSSGIS van het Canton van Solothurn in Zwitserland
![](./images/suisse_solothurn1.png){.align-left}

Het Kanton Solothurn verschaft services en infrastructuur aan 250,000 inwoners van Solothurn. In het jaar 2001 besliste het Staatsparlement om te migreren van Windows naar Linux. De motivatie was om onafhankelijk te zijn van één leverancier, om vrije handel aan te moedigen en licentiekosten te reduceren. Als  resultaat daarvan begon het SO!GIS departement van het Kanton Solothurn met het leveren van vereisten voor GIS van meer dan 3500 werknemers met een FOSSGIS-strategie.

De eerste stap die we namen was het introduceren van UMN MapServer en het maken van een cliënt voor SO!MAP die een eenvoudig te gebruiken WebGIS-cliënt biedt voor alle 3500 werknemers. De tweede stap was de migratie van al onze geo-ruimtelijke gegevens van Shapefiles naar de voorziening van de PostGIS ruimtelijke database. De introductie was erg succesvol, maar een eenvoudig te gebruiken desktop GIS ontbrak.

Na evaluatie van verschillende Desktop GIS-sen besloten we QGIS te gebruiken in samenwerking met GRASS, door ESRI ArcInfo en ArcView3 te vervangen in 2006.

De beslissing werd ingegeven door de volgende aspecten:
- Due to our use of desktop GIS in a Linux Terminal Server environment, Java wasn\'t an option.
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

One of the most important Desktop GIS issues is the question: \"How do I get the information from the PostGIS geodata repository I need?\". Since our end users are unfamiliar with data models and the underlying structures of our spatial database, offering the users a raw connection to the PostGIS DB was not an option. We have a metadata database that stores the descriptions of all production data called \'SO!DATA\'.

SO!DATA bevat een menselijk leesbare inventaris van de gegevensmodellen en de niet GIS-Experts-gebruikers zijn in staat deze database te gebruiken om de informatie die zij nodig hebben op te zoeken.

![\"SO!GIS Layer\" plugin developed at the Canton of Solothurn](./images/suisse_solothurn2.png){.align-right}

To remove the need for end users to interact directly with PostGIS connections and table selection dialogs, a plugin has been developed in python. The plugin is called \"SO!GIS Layer\" (see Figure 1). The plugin connects to the SO!GIS PostGIS repository, gets the information of all published geospatial data layers from SO!DATA and offers the user a GUI to find the data layers they need. With this infrastructure in place, our users are happy \-\-- they can prepare for geoprocessing, editing and map composing in an individual way.

![\"SO!GIS Suche\" plugin developed at the Canton of Solothurn](./images/suisse_solothurn3.png){.align-right}

Another required QGIS plugin we created is called \'SO!GIS Suche\'. This provides the possibility to search for locations like townships, addresses or cadastral parcels (see Figure 2). As a result the user is able to navigate very easily to an area of interest.

At the moment many other plugins are under development. These will support data manipulation, analysis or mapping for different projects. Our in-development plugins cover topics such as nature reserves, soil conservation, cadastral data verification, crisis management, abandoned sites and so on.
## Conclusie
Today we can say that using QGIS was the right decision for us. QGIS offers most of the features requested by our users. The Canton of Solothurn subcontracts the creation of features that QGIS lacks to commercial support providers. With PyQgis and PyQt there are excellent options for easy in-house application development based on QGIS. One huge benefit is the unlimited number of installations. Everyone who needs to use QGIS can use it without any limitations. To push the development of QGIS the Canton of Solothurn has invested approximately \$30,000 into QGIS every year since 2007. This is much more efficient and target-oriented than the payment of support into the black box of our former software provider. Apart from using FOSSGIS, the Canton of Solothurn also provides public geodata free of charge via the SO!ONLINE web portal.
## Auteur
![Horst Düster](./images/suisse_solothurnaut.jpg){.align-left height="200px"}

Dit artikel werd bijgedragen in mei 2009 door Dr. Horst Düster. Hij is GIS-coördinator aan het Departement van Geoinformatie in het Canton van Solothurn, Zwitserland.
