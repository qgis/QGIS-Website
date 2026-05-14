---
HasBanner: false
draft: false
releaseDate: '2015-10-23'
section: project
sidebar: true
title: Log met wijzigingen voor QGIS 2.12
type: visual-changelog

---
{{<content-start >}}
# Log met wijzigingen voor QGIS 2.12{#changelog212 }
![image1](images/projects/3648539707d0789903fdfedac3705584f12fa6ac.png)

Datum uitgave 23-10-2015

This is the change log for the next release of QGIS - version 2.12.0 \'Lyon\' - host city to our developer meet up in April 2012.

**New Features in QGIS 2.12 \'Lyon\'**

This is the next release in our 4-monthly release series. It gives you access to the new features we have been working on and represents the \'cutting edge\' of QGIS development.

QGIS \'Lyon\' is jam-packed with awesome new features. Special highlights are support for rule based labelling, rule based styling of attribute tables, and advanced geometry checker, support for digitising curve based geometries, better authentication management and much, much more! QGIS 2.12 also has many bug fixes and memory leaks addressed. The features provided in QGIS 2.12 will be included in the next LTR release (slated for release in 2016), so using this release provides you with an excellent opportunity to test new features that will make their way into the next LTR.

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org). If you are working in a production environment where you wish to be more conservative about rolling out new features to your users, we also provide a Long Term Release (LTR) version of QGIS. The current LTR is version 2.8.3 and is available at [download.qgis.org](http://download.qgis.org).

**Dankwoord**

We willen de ontwikkelaars, schrijvers van documentatie, testers en alle andere vele mensen bedanken die vrijwillig hun tijd en inspanningen bijdragen (of mensen ondersteunen om dat te doen).

From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

Tenslotte willen we onze officiële sponsoren bedanken voor de onschatbare financiële ondersteuning die zij aan dit project verlenen:
- **GOLD Sponsor:** [Asia Air Survey, Japan](http://www.asiaairsurvey.com/)
- SILVER Sponsor: [AGH University of Science and Technology, Krakow, Poland](http://www.agh.edu.pl/en)
- SILVER Sponsor: [State of Vorarlberg, Austria](http://www.vorarlberg.at/)
- SILVER Sponsor: [Office of Public Works, Ireland, Ireland](http://www.opw.ie/)
- SILVER Sponsor: [Sourcepole AG, Switzerland](http://www.sourcepole.com/)
- BRONZE Sponsor: [Lutra Consulting, UK](http://www.lutraconsulting.co.uk/)
- BRONZE Sponsor: [WhereGroup GmbH & Co. KG, Germany](http://wheregroup.com/)
- BRONZE Sponsor: [Nicholas Pearson Associates, UK](http://www.npaconsult.co.uk/)
- BRONZE Sponsor: [QGIS Poland, Poland](http://qgis-polska.org/)
- BRONZE Sponsor: [www.terrelogiche.com, Italy](http://www.terrelogiche.com/)
- BRONZE Sponsor: [GeoSynergy, Australia](http://www.geosynergy.com.au/)
- BRONZE Sponsor: [Gaia3D, South Korea](http://www.gaia3d.com/)
- BRONZE Sponsor: [Royal Borough of Windsor and Maidenhead, UK](http://www.rbwm.gov.uk/)
- BRONZE Sponsor: [Chartwell Consultants Ltd, Canada](http://www.chartwell-consultants.com/)
- BRONZE Sponsor: [Trage Wegen vzw, Belgium](http://www.tragewegen.be/)
- BRONZE Sponsor: [GFI - Gesellschaft fr Informations technologie mbH, Germany](http://www.gfi-gis.de/)
- BRONZE Sponsor: [GKG Kassel,(Dr.-Ing. Claas Leiner), Germany](http://www.gkg-kassel.de/)
- BRONZE Sponsor: [GIS-Support, Poland](http://www.gis-support.com/)
- BRONZE Sponsor: [ADLARES GmbH, Germany](http://www.adlares.com/)
- BRONZE Sponsor: [www.molitec.it, Italy](http://www.molitec.it/)
- BRONZE Sponsor: [www.argusoft.de, Germany](http://www.argusoft.de)
- BRONZE Sponsor: [Customer Analytics, USA](http://www.customeranalytics.com/)
- BRONZE Sponsor: [Avioportolano Italia, Italy](http://www.avioportolano.it/)
- BRONZE Sponsor: [Faculty of Geology, Geophysics and Environmental Protection, AGH, University of Science and Technology, Poland](http://www.wggios.agh.edu.pl/en)
- BRONZE Sponsor: [Urbsol, Australia](http://www.urbsol.com.au/)
- BRONZE Sponsor: [MappingGIS, Spain](http://www.mappinggis.com/)
- BRONZE Sponsor: [GIS3W, italy](http://www.gis3w.it/)

A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become and official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts.

QGIS is gratis software en u bent niet verplicht om maar iets te betalen voor het gebruik ervan - in feite willen we mensen, wijd en zijd verspreid, aanmoedigen om het te gebruiken ongeacht uw financiële of sociale status - wij geloven dat het uitrusten van mensen met gereedschappen voor het maken van ruimtelijke beslissingen zal resulteren in een betere wereld voor de gehele mensheid.

{{<table-of-contents >}}
## Algemeen
### Mogelijkheid: Nieuw welkomstscherm
In plaats van eenvoudigweg een blanco, wit venster weer te geven, zal QGIS u nu een lijst van uw meest recente projecten laten zien, samen met miniaturen om snel en eenvoudig terug te keren naar het werk dat u achterliet in uw laatste sessie.

**This feature was developed by:** Matthias Kuhn at [OPENGIS.ch](http://www.opengis.ch)

![image11](images/entries/30f2ab32f4ae0d135a26b6a6ddb6705f0f6dd74a.webp)
### Mogelijkheid: Doorlopende verbeteringen aan kwaliteit van de code
Door het gebruiken van de bibliotheek address sanitizer zijn honderden geheugenlekken geïdentificeerd en opgelost. Geautomatiseerde scans van de code met behulp van Coverity Scan worden regelmatig uitgevoerd om potentiële problemen te identificeren, en onze Coverity defectdichtheid is nu indrukwekkend laag op slechts 0.02 defecten per 1000 regels code. De bibliotheek met geautomatiseerde unittesten is ook significant gegroeid gedurende 2.12, wat resulteert in meer geïdentificeerde regressies, die onmiddellijk werden opgelost. In 2.12 hebben we ook doorlopende testen toegevoegd op OSX, zodat elke toevoeging wordt getest tegen de suite van unittesten op zowel Linux- als OSX-platformen.

![image12](images/entries/774d1839283f357009c64811bd000e2f8ad97c7a.webp)
### Mogelijkheid: Geavanceerde instellingen bewerken
Een nieuw paneel is toegevoegd aan het dialoogvenster Instellingen dat u de opties laat bewerken die al zijn gedefinieerd in uw profiel. Dat is alleen bedoeld voor gevorderde gebruikers omdat u onverwacht gedrag zou kunnen ervaren in QGIS als u deze instellingen wijzigt zonder dat u volledig begrijpt wat u doet.

**This feature was developed by:** Matthias Kuhn at [OpenGIS](http://www.opengis.ch/)

![image13](images/entries/6d59988bf11726192579915cff18f2b81e3f9c8f.webp)
### Mogelijkheid: Gezamenlijke exclusieve groepen in lagenboom
Met deze mogelijkheid kunt u lagen groepen maken waarvan per keer slechts één laag in de groep zichtbaar kan zijn. De mogelijkheid kan individueel worden geschakeld voor groepen in het contextmenu van de Lagenboom.

**This feature was developed by:** Martin Dobias at [Lutra Consulting](http://www.lutraconsulting.co.uk/) on subcontract to [Gis3W](http://www.gis3w.it/)

**Deze mogelijkheid werd mogelijk gemaakt door:** Tuscany Region (Italië) - SITA (CIG: 63526840AE)

![image14](images/entries/5c68a4deab4d6058d05d3129fec89c6f9abb8530.webp)
### Mogelijkheid: Filteren op veldwaarden in widget Expressie
Bij het maken van een expressie die waarden uit ene veld gebruikt, kunt u nu de de velden filteren in een voorbeeldpaneel.

**Deze mogelijkheid werd ontwikkeld door:** Salvatore Larosa

![image15](images/entries/5d41174bdf2a059d41824590520857002a70a056.webp)
### Mogelijkheid:: Ondersteuning voor thema in gebruikersinterface
QGIS 2.12 now supports user interface theming support which you can use to customise the appearance of window backgrounds, buttons etc. By default we ship with two themes: **Default** and **Night mapping**. The latter is a dark theme which some people may prefer if they find that light themes cause eye strain. If you know a little CSS you can create your own custom themes fairly easily too\...

Find out more about theming support by reading [Nathan Woodrow\'s blog article](http://nathanw.net/2015/08/29/ui-theme-support-now-core-in-qgis/).

**This feature was developed by:** [Nathan Woodrow](http://nathanw.net/)

![image16](images/entries/2ec302b12a3b0db8e7a66465afccb227bc543a3e.webp)
### Mogelijkheid: Nieuwe functies voor expressies in 2.12
A set of functions for \"fuzzy matching\" have been added. These include functions for finding the similarity of two strings and also for performing phonetic matching between strings, and allow you to perform filters for records which \"nearly match\" a specified string.

Ook zijn meer op geometrie gebaseerde functies toegevoegd, inclusief:
- `num_points(geom)` for calculating the number of nodes in a geometry
- `area(geom)`, `length(geom)` and `perimeter(geom)`, for calculating the area, length and perimeter of any geometry object. Previously only calculation of the area, length and perimeter of the current feature\'s geometry was possible.
- `start_point(geom)`, `end_point(geom)`, `point_n(geom, n)`, for retrieving the first, last and numbered points from a geometry
- `make_point(x,y)`, for manual creation of a point geometry
- `x(geom)`, `y(geom)` functions which return the x and y coordinate for point geometries or the centroid x/y for non-point geometries

A new `project_color` function has been added, which allows you to retrieve a color from the project\'s color scheme by name. This lets you create \'linked colors\', where the color of symbol or labeling components can be bound to a color in the project\'s color scheme. Update the color in the scheme, and all the linked colors will be automatically refreshed to match!

Aanvullend zijn enkele bijzonder handige expressies geporteerd vanuit de plug-in Expressions+, inclusief:
- `color_part`: allows retreival of a specific color component (eg red, hue, alpha) from a color
- `set_color_part`: allows a specific color component to be overridden, eg alter the alpha value (opacity) of a color
- `day_of_week`: returns the day of week as a number from a date

Aanvullend is de contexthelp voor functies van expressies verbeterd voor betere leesbaarheid.

![image17](images/entries/b56f529af78b2d970f057c2c25ba89b87a85ce85.webp)
### Mogelijkheid: Variabelen in expressies
U kunt nu aangepaste variabelen definiëren om te gebruiken in expressies. Variabelen kunnen worden gedefinieerd op het globale niveau van de toepassing, niveau van het project, niveau van de laag en op het niveau van de lay-out. Net als met gestapelde regels van CSS kunnen variabelen worden overschreven - bijv een variabele op het niveau van het project zal elke variabele die is ingesteld op het niveau van de toepassing overschrijven. U kunt deze variabelen gebruiken om tekenreeksen van tekst of andere aangepaste expressies te bouwen. Bijvoorbeeld in de lay-out een label maken met deze inhoud:

`This map was made using QGIS [% @qgis_version %].` `The project file for this map is: [% @project_path %]`

Zal het label renderen zoals hier:

`This map was made using QGIS 2.12.` `The project file for this map is: /gis/qgis-user-conference-2015.qgs`

You can manage global variables from the `Settings -> Options` menu, and project level variables from `Project properties` (including adding your own custom variables).

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image18](images/entries/19aca1d680543a4013c53ba80406bdd5ebff88c5.webp)
## Analyse-gereedschappen
### Mogelijkheid: Aantal punten in afgeleide velden in het gereedschap Objecten identificeren toegevoegd
Gebruiken van het gereedschap Objecten definiëren op een object Lijn zal nu het aantal punten in het object weergeven als een aanvullend afgeleid attribuut.
### Mogelijkheid: Gereedschap Raster uitlijnen
This new tool in qgis_analysis library is able to take several rasters as input and:
- opnieuw projecteren naar hetzelfde CRS
- opnieuw samplen naar dezelfde celgrootte en verschuiving in het raster
- een interessegebied te clippen
- waarden, indien nodig, opnieuw op schaal te brengen

**This feature was developed by:** Martin Dobias at [Lutra Consulting](http://www.lutraconsulting.co.uk/) on subcontract to [Kartoza](http://kartoza.com/)

**This feature was funded by:** [DFAT](http://dfat.gov.au) for the [InaSAFE project](http://inasafe.org/)

![image2](images/entries/c613bb210ba0e85eb3b479ab79cd895827c22602.webp)
### Mogelijkheid: Plug-ins Geometry Checker en Geometry Snapper
Twee nieuwe plug-ins (die u handmatig dient te activeren in Plug-ins beheren en installeren) zijn beschikbaar voor het controleren en corrigeren van geometrieën. De plug-in **Geometry Checker** (rechts weergegeven) zal uw vector gegevensset controleren en corrigeren op een aantal verschillende typen systematische fouten en ze voor u proberen op te lossen. Na het oplossen van een fout, wordt de foutenlijst automatisch bijgewerkt zodat als, bijvoorbeeld, het oplossen van één fout ook andere fouten oplost, alle fouten worden verwijderd van de foutenlijst.

Met het gereedschap **Geometry Snapper** kunt u de randen en punten van de ene vectorlaag uitlijnen aan de randen en punten van een tweede laag met behulp van een gebruikergedefinieerde tolerantie.

**This feature was developed by:** Sandro Mani at [Sourcepole AG](http://www.sourcepole.ch/)

**This feature was funded by:** [Canton of Solothurn](http://www.sogis.so.ch/)

![image3](images/entries/319136e65a51c7a8d76adac7aef89806db170c2e.webp)
## Opties voor toepassing en projecten
### Mogelijkheid: Beheren van versleutelde wachtwoorden
QGIS 2.12 introduces a new authentication system (see [PR 2330, QEP 14](https://github.com/dakcarto/QGIS-Enhancement-Proposals/blob/auth-system/qep-14-authentication-system.rst)). Here\'s what is included:
- Configuraties van authenticatie met versleuteld hoofdwachtwoord opgeslagen in een database van SQLite
- Authenticatiemethode met plug-in architectuur (zoals gegevensproviders)
- plug-in Basis authenticatiemethode 
- Basis plug-in geïntegreerd met PostGIS- en OWS-provider verbindingen
- In lijn met de huidige opzet van gebruikersnaam/wachtwoord (nog steeds volledig te gebruiken)
- Configuraties voor SSL-serververbinding (uitzonderingen opslaan of aangepaste configuraties voor verbindingsfouten in SSL)

PKI-authenticatie gerelateerd:
- Importeren van extra Certificate Authorities, uitgevers van tijdelijke certificaten en persoonlijke identiteitsbundels
- Certificaatcomponenten beheren zoals in Firefox
- Plug-ins voor authenticatiemethode voor PEM en PKCS#12 bundels op schijf, en voor opgeslagen persoonlijke identiteiten
- Geïntegreerd met verbindingen van OWS-provider (PostGIS en andere databases zullen iets meer werk vergen)

Voor gedeelde projectscenario's, inclusief een set-up voor netwerkschijf, u kunt de configuratie voor de authenticatie (authcfg) ID bewerken naar iets dat wordt gedeeld door gebruikers.

Since the authcfg ID is embedded in the project file, each user just needs to make an auth config that has their specific credentials for that resource, then edit the ID (upon creation of config or after) to the same ID in the project file. Then, when the resource loads, the same configuration will be queried on everyone\'s QGIS, just with their respective credentials for the authentication method used.

Voor het dialoogvenster Handle Bad Layers kunnen gebruikers configuraties voor authenticatie Toevoegen/Berwerken/Verwijderen in het dialoogvenster en de URI van de gegevensbron hebben bijgewerkt, zodat die overeenkomt. Dus in het scenario van een gedeeld project, zou de gebruiker onmiddellijk een toepasselijke nieuwe configuratie voor authenticatie kunnen toevoegen (en exact zien welk gedeelde ID voor configuratie voor authenticatie zou moeten worden gebruikt) bij het laden van een project.

Currently, the master password auto-set can be set via Python, or by way of a custom C++ plugin, on launch setups using a call to `QgsAuthManager::instance()->setMasterPassword( "mypassword", true )`, or by QGIS_AUTH_PASSWORD_FILE environment variable to set the path to a file with the master password.

**Note:** for Server, you can also use QGIS_AUTH_DB_DIR_PATH to set the path to a qgis-auth.db directory and QGIS_AUTH_PASSWORD_FILE to set the path to a file with the master password on the server.

PKI example docs: <https://github.com/dakcarto/QGIS-Enhancement-Proposals/blob/auth-system/extras/auth-system/pkiuser.rst>

**Deze mogelijkheid werd ontwikkeld door:** Larry Shaffer

**This feature was funded by:** [Boundless Spatial, Inc.](http://boundlessgeo.com/)

![image4](images/entries/d6c9305a8dcaea3a5a6c039dec40d50e0caf23ff.webp)
## Browser
### Mogelijkheid: Verbeteringen aan verbindingen naar PostGIS in browser
De browser van QGIS ondersteunt nu aanvullende functionaliteit voor verbindingen van PostGIS, inclusief de mogelijkheid om ** schema's te maken, te hernoemen en te verwijderen**, **ondersteuning voor het hernoemen en afbreken van lagen** en om **tabellen van het ene naar het andere schema te kopiëren**.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

**Table copying by:** Jürgen Fischer at [norBIT GmbH](http://www.norbit.de/)

![image5](images/entries/00820dbcf67c97b61154e7e1f41af0397009b548.webp)
## Gegevensproviders
### Mogelijkheid: Verbeteringen aan PostGIS-provider
De volgende verbeteringen werden gemaakt aan de provider PostGIS:
- verbeteringen aan de uitvoering voor op regel gebaseerde renderer voor lagen van PostGIS
- toegevoegde ondersteuning voor compound keys in weergaven

**Compound keys developed by:** Jürgen Fischer at [norBIT GmbH](http://www.norbit.de/)

![image6](images/entries/bc56564581d97034137956cd27e945b3d3ceb3df.webp)
## Gegevensbeheer
### Mogelijkheid: Verbeteringen aan DBManager
Er zijn een aantal verbeteringen doorgevoerd in het gereedschap DB Manager:
- In de DB Manager kunt u nu uw gegevens exporteren naar elk door OGR ondersteunde gegevensindeling in plaats van naar alleen shapefile, die beschikbaar was in de vorige versie.
- Oracle Spatial wordt nu ondersteund in de DB Manager
- Bij het importeren van gegevens in een tabel kunt u nu de nieuwe optie **Alleen geselecteerde objecten importeren** gebruiken om wat zal worden geïmporteerd te beperken.
- Nieuwe vensters voor query's worden nu als tabs gebruikt om het aantal dialoogvensters te verkleinen

![image7](images/entries/daa22cc4517b58f2457d78781d4dbab12663ce9d.webp)
### Mogelijkheid: Voorwaardelijke opmaak voor cellen in de attributentabel
This is a major improvement to QGIS\'s attribute table rendering support. You can now style table cells according to rules. For example you can colour all cells with a population of less than 50 000 in red. The option is enabled via a new icon on the table toolbar at the top right of the attribute table window. You can read more about this feature on [Nathan Woodrow\'s blog article](http://nathanw.net/2015/08/20/mixing-a-bit-of-excel-into-qgis-conditional-formatted-table-cells/).

**This feature was developed by:** [Nathan Woodrow](http://nathanw.net/)

![image8](images/entries/ae9afefda043d31ef7718528d506d98e90e7a1f7.webp)
### Mogelijkheid: Ondersteuning voor relatieve paden in widgets
Voor de volgende typen wijzig hulpmiddelen:
- Bestandsnaam
- Foto
- Webweergave

Indien het pad dat is geselecteerd met de bestandsbrowser is geplaatst in dezelfde map als het projectbestand .qgs of lager, worden paden geconverteerd naar relatieve paden. Dit verhoogt de portabiliteit van een project van QGIS met aangehechte informatie voor multimedia.

**This feature was developed by:** Matthias Kuhn at [OpenGIS](http://www.opengis.ch/)

**This feature was funded by:** [Alta ehf](http://www.alta.is/)

![image9](images/entries/fcf703990b5cb743ffa5cc7778cb151022ff2d20.webp)
## Digitaliseren
### Mogelijkheid: Verbeteringen aan Digitaliseren
In QGIS 2.10 we mentioned that there is a new geometry architecture for QGIS but that not all features were supported in the digitising tools. With QGIS 2.12 we now have editing support for the **creation of curves / \'circular strings\`**. Note again that you need to be using a data provider (e.g. PostGIS, GML or WFS) that supports curves. These improvements to the digitising tools were also added in QGIS 2.12:
- gereedschap om cirkel tekenreeksen toe te voegen met twee punten en radius
- gereedschap om cirkel-tekenreeksen met startpunt, boogpunt en eindpunt toe te voegen
- escape toestaan om het tekenen van nieuwe objecten te annuleren
- weergeven van een tabel met knopen bij het bewerken met behulp van het Knooppunt-gereedschap, war u in staat stelt de exacte X- en Y-coördinaten voor knopen handmatig in te voeren, als ook de waarden voor Z en M (afhankelijk van het type laag)

Aanvullend werden meer van de gereedschappen voor het bewerken en aanpassen van geometrie bijgewerkt om correct te kunnen werken met lagen die dimensies Z of M bevatten.

**This feature was developed by:** Marco Hugentobler at [Sourcepole AG](http://www.sourcepole.ch/)

**This feature was funded by:** [Canton of Solothurn](http://www.sogis.so.ch/)

![image10](images/entries/215ead2dd5e43e394d47169a7fd82aa5cc08b6b6.webp)
## Labelen
### Feature: Data defined quadrant when in \"around point\" mode
Het is nu mogelijk om een gegevens gedefinieerd kwadrant te specificeren als een label voor een punt wordt ingesteld in de plaatsingsmodus Rondom punt. Dit stelt u in staat handmatig de plaatsing van het kwadrant te overschrijven voor een specifiek label waarbij de resterende labels kunnen worden ingesteld om terug te vallen op de automatische plaatsing.

See [this article](http://nyalldawson.net/2015/07/recent-labelling-improvements-in-qgis-master/) for more details.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image19](images/entries/27a58b65cf449505c92cc6c8470a93d1f09893a1.webp)
### Mogelijkheid: Alleen labels teken die passen binnen polygonen
Een optie is aan polygoonlagen toegevoegd om alleen labels te tekenen die compleet binnen objecten polygoon passen.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image20](images/entries/5c8461abe3aa5483c3243c0f145940b0d5fd1310.webp)
### Mogelijkheid: Beheren van prioriteit voor labelen van obstakel
In 2.12 it\'s now possible to specify the priority for labeling obstacles. This allows you to make labels prefer to overlap features from certain layers rather than others. The priority can also be data defined so that certain features are more likely to be covered than others. You can also use data defined expressions or fields to control whether a specific feature in layer will act as an obstacle for labels.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image21](images/entries/f07a082bd4e62f059788c18a9de353107b8bdc44.webp)
### Mogelijkheid: Nieuwe opties om te beheren hoe polygoonlagen dienen als obstakels
New options have been added to control how labels should be placed to avoid overlapping the features in polygon layers. The options are to either avoid placing labels over polygon interiors or avoid placing them over polygon boundaries. Avoiding placing labels over boundaries is useful for regional boundary layers, where the features cover an entire area. In this case it\'s impossible to avoid placing labels within these features and it looks much better to avoid placing them over the boundaries between features instead. The result is better cartographic placement of labels in this situation.

See [this article](http://nyalldawson.net/2015/07/recent-labelling-improvements-in-qgis-master/) for more details.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image22](images/entries/e37943c654080e33219acb5e519970cf748c87bf.webp)
### Mogelijkheid: Gegevens gedefinieerd beheer over prioriteit  van labels
Deze veelgevraagde mogelijkheid stelt gebruikers in staat om de prioriteit voor individuele labels in te stellen. In eerdere uitgaven stond QGIS het instellen van de prioriteit voor labels voor een gehele laag toe, maar was er geen optie om de prioriteit van objecten op ene laag te beheren. Nu kunt u een gegevens gedefinieerde expressie of veld gebruiken om het labelen van bepaalde objecten boven andere op een laag te prioriteren!

See [this article](http://nyalldawson.net/2015/07/recent-labelling-improvements-in-qgis-master/) for more details

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image23](images/entries/bd185cde38420f50fb540d742d178768d28ac577.webp)
### Mogelijkheid: Optie voor lagen met alleen obstakels
This allows users to set a layer as just an obstacle for other layer\'s labels without rendering any labels of its own. It means that a non-labelled layer can act as an obstacle for the labels in other layers, so they will be discouraged from drawing labels over the features in the obstacle layer, and allows for improved automatic label placement by preventing overlap of labels and features from other layers.

In the screenshot you can see that the Streets have the option \"Discourage other labels from covering features in this layer\" enabled. The red labels derived from polygon geometries are thus placed to avoid intersection with the street axis. You have to enable \"Horizontal\" or \"Free\" on the polygon layer in order to achieve proper results.

Note, that it is also possible to both label a layer, but also act as obstacle layer, by enabling the checkbox \"Discourage labels from covering features\" in the \"rendering\" tab of the label settings.

See [this article](http://nyalldawson.net/2015/07/recent-labelling-improvements-in-qgis-master/) for more details.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image24](images/entries/de1eae1359ce92045d51c6fa9bc3f014a3f3ae67.webp)
### Mogelijkheid: Op regels gebaseerd labelen
Labels voor objecten kunnen nu met behulp van regels worden opgemaakt om nog meer beheer mogelijk te maken voor plaatsen en opmaken van labels. Net als het op regels gebaseerd cartografische renderen, kunnen regels voor labels worden genest om extreem flexibele opties voor opmaak mogelijk te maken. U kunt bijvoorbeeld labels verschillend renderen, gebaseerd op de grootte van het object waarin zij zullen worden gerenderd (zoals weergegeven in de schermafdruk).

See [blogpost](http://www.lutraconsulting.co.uk/blog/2015/10/25/rule-based-labeling/) for more details

**This feature was developed by:** Martin Dobias at [Lutra Consulting](http://www.lutraconsulting.co.uk/) on subcontract to [Gis3W](http://www.gis3w.it/)

**Deze mogelijkheid werd mogelijk gemaakt door:** Tuscany Region (Italië) - SITA (CIG: 63526840AE)

![image25](images/entries/8846f57f0395e7f6b2543a92a5c55b67e8b19923.webp)
## Printvormgeving
### Mogelijkheid: Verbeteringen aan navigatie in atlas
You can now set a field or expression as the \"page name\" for atlas compositions. A page number combobox has been added to the atlas toolbar, which shows both a list of available page numbers and names. This allows you to jump directly to a specific page within your atlas.

De paginanaam kan ook worden gebruikt binnen expressies van symbologie en labelen om geavanceerd op maak objecten van de atlas mogelijk te maken, gebaseerd op hun paginanaam.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image26](images/entries/bbf6147ef8be9d209fa188d6c524bce9d13d5ba8.webp)
### Mogelijkheid: Aangepaste indeling voor annotaties van het raster
Annotaties voor het raster van Printvormgeving kunnen nu worden opgemaakt in aangepaste indelingen, die worden geëvalueerd met behulp van het mechanisme voor de expressies. Nu kunt u elke esoterische indeling voor rasternummering gebruiken die uw kaart nodig heeft!

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image27](images/entries/a6cd03594ca802015ef4a5bf7806cc1ce291214b.webp)
### Mogelijkheid: Tekstafhandeling voor meerdere regels en automatische tekstdoorloop in attributentabellen van Printvormgeving
Attributentabellen bevatten nu volledige ondersteuning voor tekenreeksen van meerdere regels. Beheer over de verticale uitlijning van tekst in een cel is ook toegevoegd, naast opties voor het doorlopen van tekst voor bepaalde tekens of automatisch berekende tekstdoorloop om te passen in de grootte van de kolommen. Stel de breedte van de kolom in op ene vaste grootte om automatische tekstdoorloop met automatische rijhoogten af te dwingen.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

**This feature was funded by:** [City of Uster](http://gis.uster.ch/)

![image28](images/entries/db66b56f79949779ea32126bd22f2f1c9d4b55e6.webp)
### Mogelijkheid: Geavanceerde aanpassing van achtergrondkleur van cellen
Deze wijziging stelt gebruikers in staat om verschillende kleuren in te stellen voor wisselende rijen en kolommen, eerste/laatste rij/kolom en koprij in attributentabellen van Printvormgeving.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

**This feature was funded by:** [Ville de Morges](http://www.morges.ch/)

![image29](images/entries/68266f6b11599dfa226952455ca150448a5d082a.webp)
### Mogelijkheid: Optie Pagina aanpassen aan inhoud toegevoegd en opties voor bijsnijden van export naar inhoud
Een nieuwe optie is toegevoegd in het paneel Lay-out om een lay-out aan te passen aan de inhoud daarvan, met optioneel extra marges indien nodig.

Composer exports can also be cropped to their contents. If selected, this option will make the images output by composer include only the area of the composition with content. There\'s also an option for margins to add around the item bounds if required.

If the composition includes a single page, then the output will be sized to include EVERYTHING on the composition. If it\'s a multi-page composition, then each page will be cropped to only include the area of that page with items.

Een nieuw optiedialoogvenster voor exporteren is toegevoegd om dit mogelijk te maken, die ook handige sneltoetsen bevat voor het overschrijven van de afdrukresolutie of dimensies van de geëxporteerde afbeelding.

**Sponsored by:** [NIWA](https://www.niwa.co.nz/)

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image30](images/entries/38572cf4aa662cc4463c2a29f3d5ca38aa382632.webp)
### Mogelijkheid: Vectorlagen forceren om te renderen als rasterafbeeldingen
A new option has been added under the layer properties, rendering tab to force a vector layer to render as a raster. Extremely detailed layers (eg polygon layers with a huge number of nodes) can cause composer exports in PDF/SVG format to be huge as all nodes are included in the exported file. This can also make the resultant file very slow to work with or open in external programs. Now, you can force these layers to be rasterised on a layer-by-layer basis, so that the exported files won\'t have to include all the nodes contained in these layers. The end result is smaller file sizes and PDFs/SVGs which are faster to open.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image31](images/entries/0127fe10ecae31dbcd133492c93f33b0d569dcba.webp)
### Mogelijkheid: Gegevens gedefinieerd beheer over kaartlagen en voorkeuren voor opmaak
Een nieuw gegevens gedefinieerd besturingselement is toegevoegd aan de kaartlagen en voorkeuren voor opmaak om in een kaart van printvormgeving weer te geven. De expressie voor gegevens gedefinieerde kaartlagen zou moeten resulteren in een \| (pipe) gescheiden lijst van laagnamen die op de kaart zullen worden weergegeven, of de expressie voor voorkeur gegevens gedefinieerde opmaak zou moeten resulteren in de naam van een bestaande voorkeur voor opmaak.

Using this control over map layers allows for \"layer-based\" atlases, where the map layers should change between atlas pages instead of or in combination with the map extent changing. An example could be an atlas looping over different administrative units and at the same time looping over several historic maps or aerial images.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

**This feature was funded by:** [City of Uster](http://gis.uster.ch/)

![image32](images/entries/a8dc3b35df4020897e39c81bd22a469ab5ea6225.webp)
### Mogelijkheid: Optie om pagina's te verbergen in een weergave/export
There\'s now an option to hide the display of pages while editing and exporting compositions. This option is useful for compositions which aren\'t intended for print and are not bound by any preset page sizes. You can hide the pages, then add and resize items in any way you desire without the visual distraction of page boundaries!

**Sponsored by:** [NIWA](https://www.niwa.co.nz/)

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)
## Plug-ins
### Mogelijkheid: Bijwerken van de plug-in GRASS
De plug-in GRASS werd bijgewerkt om ondersteuning voor GRASS 7 mogelijk te maken. Door lagen voor GRASS kan worden gebladerd en geladen vanuit de browser van QGIS of het paneel Browser. GRASS vectorgegevens kunnen direct worden bewerkt in QGIS. Het project bevat de volgende werkpakketten:
- Plug-in bibliotheek upgrade en bouw voor meerdere versies
- Integratie van QGIS-browser en paneel Browser
- Ondersteuning voor mapsets, modules en shell om gegevensanalyses mogelijk te maken
- bewerken van vector

Vo zowel gebruikers van GRASS 6 en GRASS 7 zult u merken dat de integratie tussen GRASS en QGIS veel meer naadloos is. U kunt lagen voor GRASS direct in het paneel van de QGIS Browser maken, GRASS vectorlagen opmaken met behulp van de standaard gereedschappen voor opmaak van QGIS en bekende QGIS gereedschappen voor Digitaliseren gebruiken om nieuwe vector geometrieën te maken in een mapset van GRASS.

See also [QGIS GRASS Plugin Upgrade project page](http://www.gissula.eu/qgis-grass-plugin-crowdfunding/) and [progress report](http://www.gissula.eu/qgis-grass-plugin-crowdfunding/progress.html)

**This feature was developed by:** [Radim Blazek](http://www.gissula.eu/)

**This feature was funded by:** Crowd funding, see [project page](http://www.gissula.eu/qgis-grass-plugin-crowdfunding/)

![image33](images/entries/fb9ac25e9ca6c5e4030167e289435e995f5af8f5.webp)
## Programmeerbaarheid
### Feature: Map tools moved from app-\>gui
Deze wijziging maakt het mogelijk gereedschappen voor de kaart opnieuw te gebruiken binnen scripts van PyQGIS en Python plug-ins.

**This feature was developed by:** Matthias Kuhn at [OpenGIS](http://www.opengis.ch/)

**This feature was funded by:** [SIGE](http://www.sige.ch/)
### Mogelijkheid: Lagen bewerken via \`with edit(layer):\`
Voorbeeld:

    from qgis.core import edit
    
    with edit(layer):
       f=layer.getFeatures().next()
       f[0]=5
       layer.updateFeature(f)
    
Dit zal automatisch commitChanges() aan het eind aanroepen. Indien er een uitzondering optreedt zal het rollBack() alle wijzigingen.

**This feature was developed by:** Matthias Kuhn at [OpenGIS](http://www.opengis.ch/)
### Mogelijkheid: Nieuwe API voor mechanisme voor labelen (QgsLabelingEngineV2)
Het idee is om het mechanisme meer flexibel te maken ten opzichte van QgsPalLabeling implementation:
> - abstract afhandelen met tekstlabels / diagrammen uit de aandrijving zelf
> - meerdere typen labels per laag toestaan
> - ondersteuning voor aangepaste labelproviders (bijv. geïmplementeerd door plug-ins)
> - de aandrijving voor de labels onafhankelijk maken van de aandrijving voor het renderen van de kaart
> - gemakkelijker maken voor het auto-testen van de aandrijving voor de labels en de componenten ervan

See [blogpost](http://www.lutraconsulting.co.uk/blog/2015/10/25/rule-based-labeling/) for more details

**This feature was developed by:** Martin Dobias at [Lutra Consulting](http://www.lutraconsulting.co.uk/) on subcontract to [Gis3W](http://www.gis3w.it/)

**Deze mogelijkheid werd mogelijk gemaakt door:** Tuscany Region (Italië) - SITA (CIG: 63526840AE)
### Mogelijkheid: Scripts openen in externe bewerker
Vreugde voor Pythonistas- u kunt nu uw scripts openen in een externe bewerker met behulp van de nieuwe knop die is toegevoegd aan de console.

**This feature was developed by:** [Nathan Woodrow](http://nathanw.net/)

![image34](images/entries/78acf0058f4306bf408a58df3762dff5986633a7.webp)
### Mogelijkheid: Nieuwe klassen voor programma's in PyQGIS
Een nieuwe klasse QgsStringUtils is toegevoegd wat het mogelijk maakt dat scripts van PyQGIS het nieuwe algoritmen voor fuzzy overeenkomsten kan gebruiken dat is toegevoegd in 2.12. Deze bevatten functies voor het zoeken naar de Levenshtein bewerkingsafstand tussen twee tekenreeksen en voor het berekenen van de fonetische weergave in Soundex van een tekenreeks. Deze algoritmen zijn zeer geoptimaliseerd voor uitvoering, dus zij zijn voor u klaar om te gebruiken voor beginnen te vergelijken van fuzzy overeenkomsten in miljoenen tekenreeksen!

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)
## QGIS Server
### Mogelijkheid: QGIS Server Python API
QGIS Server is nu verpakt als een bibliotheek met een initiële (maar groeiende) API en verbindingen voor Python. Met de nieuwe API hebben we een verzameling Python-testen voor de hoofdcomponent van de server en voor de plug-ins van de server. Opstarten van de server vanuit Python is nu zo eenvoudig als:

    from qgis.server import QgsServer
    headers, body =  QgsServer().handleRequest(my_query_string)
    
For more information see [this article](http://www.itopen.it/qgis-server-binding-news/)

**This work has been developed and funded by**: Alessandro Pasotti at [ItOpen](http://www.itopen.it/)
### Mogelijkheid: getMap in indeling dxf
Het is nu mogelijk om het resultaat van een WMS-verzoek GetMap op te halen in de indeling DXF. Het ondersteunt dezelfde mogelijkheden en opties zoals die beschikbaar zijn in de desktop van QGIS. Met dezelfde beperkingen.

| Sample URL: | `http://yourserver.org/cgi-bin/qgismapserver.fcgi?` | `map=/path/to/your/projectfile.qgs&` | `SERVICE=WMS&` | `VERSION=1.3.0&` | `REQUEST=GetMAP&` | `FORMAT=application/dxf&` | `FORMAT_OPTIONS=SCALE:500;MODE:SYMBOLLAYERSYMBOLOGY&` | `FILE_NAME=youroutputfilename.dxf&` | `CRS=EPSG:EPSG:21781&` | `BBOX=695558.73070825,244430.77224034,697158.88528251,245722.25976142&` | `WIDTH=1042&` | `HEIGHT=841&` | `LAYERS=yourdxfexportlayers`

See also [QGIS as OGC data server](http://docs.qgis.org/2.18/en/docs/user_manual/working_with_ogc/ogc_server_support.html#dxf-export) for all the available options.

In de schermafdruk ziet u links de QGIS Web Cliënt met de DXF exportfunctionaliteit (die gebruik maakt van QGIS server) en rechts hetzelfde bereik bekeken in Autodesk TrueView.

**This feature was developed by:** Marco Hugentobler [Sourcepole AG](http://www.sourcepole.ch/)

**This feature was funded by:** [City of Uster](http://gis.uster.ch/)

![image35](images/entries/beb2e9c00102c67ae703eac097ffba8866379609.webp)
## Symbologie
### Mogelijkheid: Miniaturen exporteren vanuit Stijlbeheer
Stijlbeheer stelt u nu in staat geselecteerde miniaturen van stijl te exporteren, ofwel als afbeelding SVG of als PNG.

**This feature was developed by:** [Nathan Woodrow](http://nathanw.net/)

![image36](images/entries/8861a040751804f6c2691ee4d93d410efd6d99ac.webp)
### Mogelijkheid: Nieuwe optie voor beperken van de grootte in mm bij gebruiken van grootten in kaarteenheden
Eerder was alleen de beperking voor het schaalbereik van kaarteenheden beschikbaar. Nu kunt u ook de overeenkomende gerenderde grootte in mm kiezen. 

![image37](images/entries/b822235ddb09b4184b926bf2e0acc5c892147d0b.webp)
### Mogelijkheid: Verbeteringen aan renderer voor verplaatsingen
- Tolerantie in mm/pixels mogelijk maken voor renderer van verplaatsingen
- Instellen van transparantie voor kleuren mogelijk maken
- Modus Concentrische ringplaatsing (maakt een meer compacte weergave mogelijk dan alleen met ringen)

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image38](images/entries/33b5f15429279a7ec75dd1f6a2e01b1a7df789ca.webp)
### Mogelijkheid: Alle kleurverlopen kunnen nu worden bewerkt
In QGIS 2.12 \"edit\" buttons have been added next to every color ramp choice. This allows you to easily edit an existing color ramp without having to create a new ramp and overwrite the existing one.

![image39](images/entries/6ca1426e6e9bfd5500b08fb2185ae50a77258892.webp)
### Mogelijkheid: Verbeterde behandeling van SVG markeringsomtrekkken
QGIS 2.12 repareert een aantal problemen met betrekking tot de afhandeling van omtrekken binnen SVG-markeringen en SVG-vulsymbolen.

Eerdere versies van QGIS renderden de omtrekken in een significant kleinere grootte dan ingesteld, en tekenen van SVG's in grootten van kaarteenheden was defect.

These issues have been fixed in QGIS 2.12, but as a result you may need to update your project symbology if you\'ve previously set oversized outlines for your symbols to overcome these bugs. In the image you see QGIS 2.12 vs QGIS 2.10 SVG markers in the symbol layer dialogs.

![image40](images/entries/a678d22393345b4fcc07b5bd023babe383151b46.webp)
### Mogelijkheid: Pixels toegevoegd als optie voor alle keuzen van de eenheid van grootte voor Symbologie
For all size input widgets there is now a third option \"pixel\", next to \"mm\" and \"map units\". This concerns symbol sizes, stroke widths, dash sizes, offsets, etc. This may help, if you design for screens and not for print output.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image41](images/entries/cbc683061bcc06764361ab79874f1020ccfe8eb7.webp)

{{<content-end >}}
