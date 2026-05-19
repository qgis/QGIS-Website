---
HasBanner: false
draft: false
releaseDate: 23-10-2015
section: project
sidebar: true
title: Log met wijzigingen voor QGIS 2.12
type: visual-changelog

---
{{<content-start >}}
# Log met wijzigingen voor QGIS 2.12{#changelog212 }
![image1](images/projects/3648539707d0789903fdfedac3705584f12fa6ac.png)

Datum uitgave 23-10-2015

Dit is het log met wijzigingen voor de volgende uitgave van QGIS - versie 2.12.0 \'Lyon\' - gastheer voor de ontmoeting van de ontwikkelaars in april 2012.

**Nieuwe mogelijkheden in QGIS 2.12 \'Lyon\'**

Dit is de volgende uitgave in onze 4-maandelijkse uitgaveserie. Het geeft u toegang tot de nieuwe mogelijkheden waaraan we hebben gewerkt en vertegenwoordigt het \'ultieme product\' van de ontwikkeling van QGIS.

QGIS \'Lyon\' is verpakt met fantastische nieuwe mogelijkheden. Speciale vermeldingen zijn ondersteuning voor op regels gebaseerd labelen, op regels gebaseerd opmaken van attributentabellen en geavanceerde controle voor geometrieën, ondersteuning voor digitaliseren van op bogen gebaseerde geometrieën, beter beheer van authenticatie en nog veel, veel meer! QGIS 2.12 bevat ook vele oplossingen voor problemen en geheugenlekken. De in QGIS 2.12 verschafte mogelijkheden zullen worden opgenomen in de volgende LTR-uitgave (geplande uitgave in 2016), dus verschaft het gebruik van deze uitgave u een excellente mogelijkheid om nieuwe mogelijkheden te testen die hun weg zullen vinden in de volgende LTR.

Wanneer nieuwe mogelijkheden worden toegevoegd aan de software introduceren zij de mogelijkheid van nieuwe problemen - indien u een probleem met deze uitgave tegenkomt, maak dan een ticket aan [op de QGIS Bug Tracker <http://hub.qgis.org]. Indien u werkt in een productieomgeving waar u meer conservatief wilt zijn met betrekking tot het uitrollen van nieuwe mogelijkheden aan uw gebruikers, verschaffen we ook een Long Term Release (LTR)-versie van QGIS. De huidige LTR is versie 2.8.3 en die is beschikbaar op `download.qgis.org [download.qgis.org](http://download.qgis.org).

**Dankwoord**

We willen de ontwikkelaars, schrijvers van documentatie, testers en alle andere vele mensen bedanken die vrijwillig hun tijd en inspanningen bijdragen (of mensen ondersteunen om dat te doen).

Vanuit de gemeenschap van QGIS hopen we dat u van deze uitgave zult genieten! Als u tijd of geld wilt doneren of op een andere wijze betrokken wilt zijn in het opwaarderen van QGIS, kijk dan ook eens op [qgis.org](https://qgis.org) en help een handje!

Tenslotte willen we onze officiële sponsoren bedanken voor de onschatbare financiële ondersteuning die zij aan dit project verlenen:
- **GOUDEN Sponsor:** [Asia Air Survey, Japan](http://www.asiaairsurvey.com/)
- ZILVEREN Sponsor: [AGH University of Science and Technology, Krakow, Polen](http://www.agh.edu.pl/en)
- ZILVEREN sponsor: [Staat Vorarlberg, Oostenrijk](http://www.vorarlberg.at/)
- ZILVEREN sponsor: [Office of Public Works, Ireland, Ireland](http://www.opw.ie/)
- ZILVEREN sponsor: [Sourcepole AG, Zwitserland](http://www.sourcepole.com/)
- BRONZEN sponsor: [Lutra Consulting, VK](http://www.lutraconsulting.co.uk/)
- BRONZEN Sponsor: [WhereGroup GmbH & Co. KG, Duitsland](http://wheregroup.com/)
- BRONZEN Sponsor: [Nicholas Pearson Associates, VK](http://www.npaconsult.co.uk/)
- BRONZEN Sponsor: [QGIS Poland, Polen](http://qgis-polska.org/)
- BRONZEN Sponsor: [www.terrelogiche.com, Italië](http://www.terrelogiche.com/)
- BRONZEN Sponsor: [GeoSynergy, Australië](http://www.geosynergy.com.au/)
- BRONZEN Sponsor: [Gaia3D, Zuid-Korea](http://www.gaia3d.com/)
- BRONZEN Sponsor: [Royal Borough of Windsor and Maidenhead, VK](http://www.rbwm.gov.uk/)
- BRONZEN Sponsor: [Chartwell Consultants Ltd, Canada](http://www.chartwell-consultants.com/)
- BRONZEN Sponsor: [Trage Wegen vzw, België](http://www.tragewegen.be/)
- BRONZEN Sponsor: [GFI - Gesellschaft fr Informations technologie mbH, Duitsland](http://www.gfi-gis.de/)
- BRONZEN sponsor: [GKG Kassel,(Dr.-Ing. Claas Leiner), Duitsland](http://www.gkg-kassel.de/)
- BRONZEN Sponsor: [GIS-Support, Polen](http://www.gis-support.com/)
- BRONZEN sponsor: [ADLARES GmbH, Duitsland](http://www.adlares.com/)
- BRONZEN sponsor: [www.molitec.it, Italië](http://www.molitec.it/)
- BRONZEN sponsor: [www.argusoft.de, Duitsland](http://www.argusoft.de)
- BRONZEN sponsor: [Customer Analytics, USA](http://www.customeranalytics.com/)
- BRONZEN sponsor: [Avioportolano Italia, Italië](http://www.avioportolano.it/)
- BRONZEN Sponsor: [Faculty of Geology, Geophysics and Environmental Protection, AGH, University of Science and Technology, Polen](http://www.wggios.agh.edu.pl/en)
- BRONZEN sponsor: [Urbsol, Australië](http://www.urbsol.com.au/)
- BRONZEN sponsor: [MappingGIS, Spanje](http://www.mappinggis.com/)
- BRONZEN Sponsor: [GIS3W, italië](http://www.gis3w.it/)

Een huidige lijst van doneren die grote en kleine bijdragen hebben gegeven aan het project kan worden bekeken op onze [lijst van donoren](https://qgis.org/nl/site/about/sponsorship.html#list-of-donors). Als u een officiële sponsor voor het project zou willen worden, bekijk dan [onze pagina om te sponsoren](https://qgis.org/nl/site/about/sponsorship.html#sponsorship) voor de details. Sponsoren van QGIS helpen ons om fondsen te verkrijgen voor onze halfjaarlijkse ontmoetingen van ontwikkelaars, de infrastructuur van het project te onderhouden en inspanningen voor het oplossen van problemen te financieren.

QGIS is gratis software en u bent niet verplicht om maar iets te betalen voor het gebruik ervan - in feite willen we mensen, wijd en zijd verspreid, aanmoedigen om het te gebruiken ongeacht uw financiële of sociale status - wij geloven dat het uitrusten van mensen met gereedschappen voor het maken van ruimtelijke beslissingen zal resulteren in een betere wereld voor de gehele mensheid.

{{<table-of-contents >}}
## Algemeen
### Mogelijkheid: Nieuw welkomstscherm
In plaats van eenvoudigweg een blanco, wit venster weer te geven, zal QGIS u nu een lijst van uw meest recente projecten laten zien, samen met miniaturen om snel en eenvoudig terug te keren naar het werk dat u achterliet in uw laatste sessie.

**Deze mogelijkheid werd ontwikkeld door:** Matthias Kuhn at [OPENGIS.ch](http://www.opengis.ch)

![image11](images/entries/30f2ab32f4ae0d135a26b6a6ddb6705f0f6dd74a.webp)
### Mogelijkheid: Doorlopende verbeteringen aan kwaliteit van de code
Door het gebruiken van de bibliotheek address sanitizer zijn honderden geheugenlekken geïdentificeerd en opgelost. Geautomatiseerde scans van de code met behulp van Coverity Scan worden regelmatig uitgevoerd om potentiële problemen te identificeren, en onze Coverity defectdichtheid is nu indrukwekkend laag op slechts 0.02 defecten per 1000 regels code. De bibliotheek met geautomatiseerde unittesten is ook significant gegroeid gedurende 2.12, wat resulteert in meer geïdentificeerde regressies, die onmiddellijk werden opgelost. In 2.12 hebben we ook doorlopende testen toegevoegd op OSX, zodat elke toevoeging wordt getest tegen de suite van unittesten op zowel Linux- als OSX-platformen.

![image12](images/entries/774d1839283f357009c64811bd000e2f8ad97c7a.webp)
### Mogelijkheid: Geavanceerde instellingen bewerken
Een nieuw paneel is toegevoegd aan het dialoogvenster Instellingen dat u de opties laat bewerken die al zijn gedefinieerd in uw profiel. Dat is alleen bedoeld voor gevorderde gebruikers omdat u onverwacht gedrag zou kunnen ervaren in QGIS als u deze instellingen wijzigt zonder dat u volledig begrijpt wat u doet.

**Deze mogelijkheid werd ontwikkeld door:** Matthias Kuhn at [OpenGIS](http://www.opengis.ch/)

![image13](images/entries/6d59988bf11726192579915cff18f2b81e3f9c8f.webp)
### Mogelijkheid: Gezamenlijke exclusieve groepen in lagenboom
Met deze mogelijkheid kunt u lagen groepen maken waarvan per keer slechts één laag in de groep zichtbaar kan zijn. De mogelijkheid kan individueel worden geschakeld voor groepen in het contextmenu van de Lagenboom.

**Deze mogelijkheid werd ontwikkeld door:** Martin Dobias van [Lutra Consulting](http://www.lutraconsulting.co.uk/) onder subcontract voor [Gis3W](http://www.gis3w.it/)

**Deze mogelijkheid werd mogelijk gemaakt door:** Tuscany Region (Italië) - SITA (CIG: 63526840AE)

![image14](images/entries/5c68a4deab4d6058d05d3129fec89c6f9abb8530.webp)
### Mogelijkheid: Filteren op veldwaarden in widget Expressie
Bij het maken van een expressie die waarden uit ene veld gebruikt, kunt u nu de de velden filteren in een voorbeeldpaneel.

**Deze mogelijkheid werd ontwikkeld door:** Salvatore Larosa

![image15](images/entries/5d41174bdf2a059d41824590520857002a70a056.webp)
### Mogelijkheid:: Ondersteuning voor thema in gebruikersinterface
QGIS 2.12 ondersteunt nu thema's voor de gebruikersinterface, wat u kunt gebruiken om de achtergronden van vensters, knoppen etc. aan te passen. Standaard worden twee thema's meegeleverd: **Default** en **Night mapping**. De laatste is een donker thema dat sommige mensen prefereren als zij vinden dat lichtere thema's hun ogen belasten. Als u een beetje weet van CSS, kunt u ook vrij gemakkelijk uw eigen aangepaste thema's maken\...

Meer over de ondersteuning voor thema's in [Nathan Woodrow\'s blogartikel](http://nathanw.net/2015/08/29/ui-theme-support-now-core-in-qgis/).

**Deze mogelijkheid werd ontwikkeld door:** [Nathan Woodrow](http://nathanw.net/)

![image16](images/entries/2ec302b12a3b0db8e7a66465afccb227bc543a3e.webp)
### Mogelijkheid: Nieuwe functies voor expressies in 2.12
Een aantal functies voor \"fuzzy overeenkomsten\" is toegevoegd. Deze bevatten functies voor het zoeken naar overeenkomsten in twee tekenreeksen en ook voor het uitvoeren van fonetische overeenkomsten tussen tekenreeksen, en stellen u in staat filters uit te voeren voor records die \"bijna overeenkomen\" met een gespecificeerde tekenreeks.

Ook zijn meer op geometrie gebaseerde functies toegevoegd, inclusief:
- `num_points(geom)` voor het berekenen van het aantal knopen in een geometrie
- `area(geom)`, `length(geom)` en `perimeter(geom)`, voor het berekenen van het gebied, de lengte en de perimeter van enig object geometrie. Eerder was slechts berekening van het gebied, de lengte en de perimeter van de geometrie van het huidige object mogelijk.
- `start_point(geom)`, `end_point(geom)`, `point_n(geom)`, voor het achterhalen van het eerste, laatste en genummerde punten van een geometrie
- `make_point(x,y)`, voor het handmatig maken van een puntgeometrie
- functies `x(geom)`, `y(geom)` die de X- en Y-coördinaten voor puntgeometrieën teruggeven of de zwaartepunt X/Y voor niet-puntgeometrieën

Een nieuwe functie `project_color` is toegevoegd, die u in staat stelt op naam een kleur uit het kleurenschema van het project te achterhalen. Dit stelt u in staat \'gekoppelde kleuren\' te maken, waarmee de kleuren van een symbool of componenten van labelen kunnen worden gebonden aan een kleur uit het kleurenschema van het project. Werk de kleur in het schema bij en alle gekoppelde kleuren zullen automatisch worden bijgewerkt om overeen te komen!

Aanvullend zijn enkele bijzonder handige expressies geporteerd vanuit de plug-in Expressions+, inclusief:
- `color_part`: die het mogelijk maakt een specifieke kleurcomponent (bijv. rood, tint, alfa) van een kleur te achterhalen
- `set_color_part`: die het mogelijk maakt een specifieke kleurcomponent te overschrijven, bijv. de alfawaarde (doorzichtbaarheid) van een kleur
- `day_of_week`: geeft de dag van een week terug als een getal uit een datum

Aanvullend is de contexthelp voor functies van expressies verbeterd voor betere leesbaarheid.

![image17](images/entries/b56f529af78b2d970f057c2c25ba89b87a85ce85.webp)
### Mogelijkheid: Variabelen in expressies
U kunt nu aangepaste variabelen definiëren om te gebruiken in expressies. Variabelen kunnen worden gedefinieerd op het globale niveau van de toepassing, niveau van het project, niveau van de laag en op het niveau van de lay-out. Net als met gestapelde regels van CSS kunnen variabelen worden overschreven - bijv een variabele op het niveau van het project zal elke variabele die is ingesteld op het niveau van de toepassing overschrijven. U kunt deze variabelen gebruiken om tekenreeksen van tekst of andere aangepaste expressies te bouwen. Bijvoorbeeld in de lay-out een label maken met deze inhoud:

`Deze kaart werd gemaakt met QGIS [% @qgis_version %].` `Het projectbestand voor deze kaart is: [% @project_path %]`

Zal het label renderen zoals hier:

`Deze kaart werd gemaakt met QGIS 2.12.` `Het projectbestand voor deze kaart is: /gis/qgis-user-conference-2015.qgs`

U kunt globale variabelen beheren vanuit het menu `Extra -> Opties` en variabelen op het niveau van het project vanuit `Projecteigenschappen` (inclusief het toevoegen van uw eigen aangepaste variabelen).

**Deze mogelijkheid werd ontwikkeld door:** [Nyall Dawson](http://nyalldawson.net/)

![image18](images/entries/19aca1d680543a4013c53ba80406bdd5ebff88c5.webp)
## Analyse-gereedschappen
### Mogelijkheid: Aantal punten in afgeleide velden in het gereedschap Objecten identificeren toegevoegd
Gebruiken van het gereedschap Objecten definiëren op een object Lijn zal nu het aantal punten in het object weergeven als een aanvullend afgeleid attribuut.
### Mogelijkheid: Gereedschap Raster uitlijnen
Dit nieuwe gereedschap in de bibliotheek qgis_analysis is in staat om meerdere rasters als invoer te gebruiken en:
- opnieuw projecteren naar hetzelfde CRS
- opnieuw samplen naar dezelfde celgrootte en verschuiving in het raster
- een interessegebied te clippen
- waarden, indien nodig, opnieuw op schaal te brengen

**Deze mogelijkheid werd ontwikkeld door:** Martin Dobias van [Lutra Consulting](http://www.lutraconsulting.co.uk/) onder subcontract voor [Kartoza](http://kartoza.com/)

**Dit werd mogelijk gemaakt door:** [DFAT](http://dfat.gov.au) for the [InaSAFE project](http://inasafe.org/)

![image2](images/entries/c613bb210ba0e85eb3b479ab79cd895827c22602.webp)
### Mogelijkheid: Plug-ins Geometry Checker en Geometry Snapper
Twee nieuwe plug-ins (die u handmatig dient te activeren in Plug-ins beheren en installeren) zijn beschikbaar voor het controleren en corrigeren van geometrieën. De plug-in **Geometry Checker** (rechts weergegeven) zal uw vector gegevensset controleren en corrigeren op een aantal verschillende typen systematische fouten en ze voor u proberen op te lossen. Na het oplossen van een fout, wordt de foutenlijst automatisch bijgewerkt zodat als, bijvoorbeeld, het oplossen van één fout ook andere fouten oplost, alle fouten worden verwijderd van de foutenlijst.

Met het gereedschap **Geometry Snapper** kunt u de randen en punten van de ene vectorlaag uitlijnen aan de randen en punten van een tweede laag met behulp van een gebruikergedefinieerde tolerantie.

**Deze mogelijkheid werd ontwikkeld door:** Sandro Mani at [Sourcepole AG](http://www.sourcepole.ch/)

**Dit werd mogelijk gemaakt door:** [Canton of Solothurn](http://www.sogis.so.ch/)

![image3](images/entries/319136e65a51c7a8d76adac7aef89806db170c2e.webp)
## Opties voor toepassing en projecten
### Mogelijkheid: Beheren van versleutelde wachtwoorden
QGIS 2.12 introduceert een nieuw authenticatiesysteem (bekijk [PR 2330, QEP 14](https://github.com/dakcarto/QGIS-Enhancement-Proposals/blob/auth-system/qep-14-authentication-system.rst). Hier is wat erin is opgenomen:
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

Omdat de authcfg ID is ingebed in het projectbestand, dient elke gebruiker een configuratie voor authenticatie die hun specifieke gegevens bevat voor die bron, dan de ID bewerken (bij het maken van de configuratie of later) naar dezelfde ID als in het projectbestand. Dan, wanneer de bron wordt geladen, zal dezelfde configuratie worden bevraagd voor QGIS van iedereen, net als hun respectievelijke gegevens voor de gebruikte methode voor authenticatie.

Voor het dialoogvenster Handle Bad Layers kunnen gebruikers configuraties voor authenticatie Toevoegen/Berwerken/Verwijderen in het dialoogvenster en de URI van de gegevensbron hebben bijgewerkt, zodat die overeenkomt. Dus in het scenario van een gedeeld project, zou de gebruiker onmiddellijk een toepasselijke nieuwe configuratie voor authenticatie kunnen toevoegen (en exact zien welk gedeelde ID voor configuratie voor authenticatie zou moeten worden gebruikt) bij het laden van een project.

Momenteel kan het automatisch instellen van het hoofdwachtwoord worden ingesteld via Python, of door middel van een aangepaste plug-in in C++, bij het starten van set-ups met behulp van een aanroep van `QgsAuthManager::instance()->setMasterPassword( "mypassword", true )`. Of door de omgevingsvariabele QGIS_AUTH_PASSWORD_FILE in te stellen op het pad naar een bestand met het hoofdwachtwoord.

**Opmerking:** voor Server kunt u ook QGIS_AUTH_DB_DIR_PATH gebruiken om het pad in te stellen naar een map qgis-auth.db en QGIS_AUTH_PASSWORD_FILE om het pad in te stellen naar een bestand met het hoofdwachtwoord op de server.

PKI voorbeeld documenten: <https://github.com/dakcarto/QGIS-Enhancement-Proposals/blob/auth-system/extras/auth-system/pkiuser.rst>

**Deze mogelijkheid werd ontwikkeld door:** Larry Shaffer

**Dit werd mogelijk gemaakt door:** [Boundless Spatial, Inc.](http://boundlessgeo.com/)

![image4](images/entries/d6c9305a8dcaea3a5a6c039dec40d50e0caf23ff.webp)
## Browser
### Mogelijkheid: Verbeteringen aan verbindingen naar PostGIS in browser
De browser van QGIS ondersteunt nu aanvullende functionaliteit voor verbindingen van PostGIS, inclusief de mogelijkheid om ** schema's te maken, te hernoemen en te verwijderen**, **ondersteuning voor het hernoemen en afbreken van lagen** en om **tabellen van het ene naar het andere schema te kopiëren**.

**Deze mogelijkheid werd ontwikkeld door:** [Nyall Dawson](http://nyalldawson.net/)

**Kopiëren van tabel door:** Jürgen Fischer op [norBIT GmbH](http://www.norbit.de/)

![image5](images/entries/00820dbcf67c97b61154e7e1f41af0397009b548.webp)
## Gegevensproviders
### Mogelijkheid: Verbeteringen aan PostGIS-provider
De volgende verbeteringen werden gemaakt aan de provider PostGIS:
- verbeteringen aan de uitvoering voor op regel gebaseerde renderer voor lagen van PostGIS
- toegevoegde ondersteuning voor compound keys in weergaven

**Compound keys ontwikkeld door:** Jürgen Fischer op [norBIT GmbH](http://www.norbit.de/)

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
Dit is een belangrijke verbetering aan de ondersteuning van het renderen van de attributentabel van QGIS. U kunt nu tabelcellen opmaken overeenkomstig regels. U kunt bijvoorbeeld alle cellen kleuren rood die een bevolking hebben van minder dan 50.000. De optie wordt ingeschakeld door middel van een nieuw pictogram op de werkbalk Tabel aan de rechterbovenkant van het venster van de attributentabel. U kunt meer over deze mogelijkheid lezen in [Nathan Woodrow\'s blogartikel](http://nathanw.net/2015/08/20/mixing-a-bit-of-excel-into-qgis-conditional-formatted-table-cells/).

**Deze mogelijkheid werd ontwikkeld door:** [Nathan Woodrow](http://nathanw.net/)

![image8](images/entries/ae9afefda043d31ef7718528d506d98e90e7a1f7.webp)
### Mogelijkheid: Ondersteuning voor relatieve paden in widgets
Voor de volgende typen wijzig hulpmiddelen:
- Bestandsnaam
- Foto
- Webweergave

Indien het pad dat is geselecteerd met de bestandsbrowser is geplaatst in dezelfde map als het projectbestand .qgs of lager, worden paden geconverteerd naar relatieve paden. Dit verhoogt de portabiliteit van een project van QGIS met aangehechte informatie voor multimedia.

**Deze mogelijkheid werd ontwikkeld door:** Matthias Kuhn at [OpenGIS](http://www.opengis.ch/)

**Dit werd mogelijk gemaakt door:** [Alta ehf](http://www.alta.is/)

![image9](images/entries/fcf703990b5cb743ffa5cc7778cb151022ff2d20.webp)
## Digitaliseren
### Mogelijkheid: Verbeteringen aan Digitaliseren
In QGIS 2.10 vermeldden we dat er een nieuwe architectuur voor geometrie is voor QGIS, maar dat nog niet alle mogelijkheden werden ondersteund in de gereedschappen voor Digitaliseren. Met QGIS 2.12 hebben we nu ondersteuning voor het bewerken van **het maken van bogen / \'cirkel tekenreeksen\`**. Onthoud opnieuw dat u een gegevensprovider (bijv. PostGIS, GML of WFS) moet gebruiken die bogen ondersteunt. Deze verbeteringen aan de gereedschappen voor Digitaliseren werden ook toegevoegd in QGIS 2.12:
- gereedschap om cirkel tekenreeksen toe te voegen met twee punten en radius
- gereedschap om cirkel-tekenreeksen met startpunt, boogpunt en eindpunt toe te voegen
- escape toestaan om het tekenen van nieuwe objecten te annuleren
- weergeven van een tabel met knopen bij het bewerken met behulp van het Knooppunt-gereedschap, war u in staat stelt de exacte X- en Y-coördinaten voor knopen handmatig in te voeren, als ook de waarden voor Z en M (afhankelijk van het type laag)

Aanvullend werden meer van de gereedschappen voor het bewerken en aanpassen van geometrie bijgewerkt om correct te kunnen werken met lagen die dimensies Z of M bevatten.

**Dit werd mogelijk gemaakt door:** Marco Hugentobler at [Sourcepole AG](http://www.sourcepole.ch/)

**Dit werd mogelijk gemaakt door:** [Canton of Solothurn](http://www.sogis.so.ch/)

![image10](images/entries/215ead2dd5e43e394d47169a7fd82aa5cc08b6b6.webp)
## Labelen
### Mogelijkheid: Gegevens gedefinieerd kwadrant indien in modus \"rondom punt\"
Het is nu mogelijk om een gegevens gedefinieerd kwadrant te specificeren als een label voor een punt wordt ingesteld in de plaatsingsmodus Rondom punt. Dit stelt u in staat handmatig de plaatsing van het kwadrant te overschrijven voor een specifiek label waarbij de resterende labels kunnen worden ingesteld om terug te vallen op de automatische plaatsing.

Bekijk [dit artikel](http://nyalldawson.net/2015/07/recent-labelling-improvements-in-qgis-master/) voor meer details.

**Deze mogelijkheid werd ontwikkeld door:** [Nyall Dawson](http://nyalldawson.net/)

![image19](images/entries/27a58b65cf449505c92cc6c8470a93d1f09893a1.webp)
### Mogelijkheid: Alleen labels teken die passen binnen polygonen
Een optie is aan polygoonlagen toegevoegd om alleen labels te tekenen die compleet binnen objecten polygoon passen.

**Deze mogelijkheid werd ontwikkeld door:** [Nyall Dawson](http://nyalldawson.net/)

![image20](images/entries/5c8461abe3aa5483c3243c0f145940b0d5fd1310.webp)
### Mogelijkheid: Beheren van prioriteit voor labelen van obstakel
In 2.12 is het nu mogelijk om de prioriteit voor het labelen van een obstakel te specificeren. Dit stelt u in staat het mogelijk te maken dat labels voorkeur hebben om objecten uit bepaalde lagen te overlappen boven die van andere. De prioriteit kan ook gegevens gedefinieerd zijn, zodat bepaalde objecten waarschijnlijk meer bedekt worden dan andere. U mag ook gegevens, gedefinieerde expressies of velden gebruiken om te beheren of een specifiek object op de laag zal dienen als een obstakel voor labels.

**Deze mogelijkheid werd ontwikkeld door:** [Nyall Dawson](http://nyalldawson.net/)

![image21](images/entries/f07a082bd4e62f059788c18a9de353107b8bdc44.webp)
### Mogelijkheid: Nieuwe opties om te beheren hoe polygoonlagen dienen als obstakels
Nieuwe opties zijn toegevoegd om te beheren hoe labels zouden moeten worden geplaatst om te voorkomen dat ze de objecten in polygonenlagen bedekken. De opties zijn ofwel om plaatsing te voorkomen over het interieur, ofwel om plaatsing te voorkomen over de begrenzing van de polygoon. Voorkomen van plaatsing over begrenzing is nuttig voor lagen met regionale grenzen, waar de objecten een geheel gebied bedekken. In dat geval is het onmogelijk om plaatsing binnen deze objecten te voorkomen en het ziet er in plaats daarvan veel beter uit om plaatsing over de begrenzing tussen de objecten te voorkomen. Het resultaat is in deze situatie een betere cartografische plaatsing van labels.

Bekijk [dit artikel](http://nyalldawson.net/2015/07/recent-labelling-improvements-in-qgis-master/) voor meer details.

**Deze mogelijkheid werd ontwikkeld door:** [Nyall Dawson](http://nyalldawson.net/)

![image22](images/entries/e37943c654080e33219acb5e519970cf748c87bf.webp)
### Mogelijkheid: Gegevens gedefinieerd beheer over prioriteit  van labels
Deze veelgevraagde mogelijkheid stelt gebruikers in staat om de prioriteit voor individuele labels in te stellen. In eerdere uitgaven stond QGIS het instellen van de prioriteit voor labels voor een gehele laag toe, maar was er geen optie om de prioriteit van objecten op ene laag te beheren. Nu kunt u een gegevens gedefinieerde expressie of veld gebruiken om het labelen van bepaalde objecten boven andere op een laag te prioriteren!

Bekijk [dit artikel](http://nyalldawson.net/2015/07/recent-labelling-improvements-in-qgis-master/) voor meer details

**Deze mogelijkheid werd ontwikkeld door:** [Nyall Dawson](http://nyalldawson.net/)

![image23](images/entries/bd185cde38420f50fb540d742d178768d28ac577.webp)
### Mogelijkheid: Optie voor lagen met alleen obstakels
Dit stelt gebruikers in staat om een laag in te stellen als alleen een obstakel voor labels van andere lagen zonder neig label van zichzelf te renderen. Het betekent dat een niet gelabelde laag kan optreden als een obstakel voor de labels in andere lagen, zodat zij zullen worden ontmoedigd om labels te tekenen over de objecten in de obstakel-laag, en verbeterde automatische plaatsing van labels door het voorkomen van overlappen door labels en objecten van andere lagen mogelijk te maken.

In de schermafdruk kunt u zien dat de Streets de optie \"Voorkomen dat andere labels objecten op deze laag bedekken\" is ingeschakeld. De rode labels, afgeleid van geometrieën van polygonen, zijn dus geplaatst om kruising met de as van de straat te voorkomen. U dient \"Horizontaal\" of \"Vrij\" op de polygonenlaag in te schakelen om de juiste resultaten te behalen.

Onthoud dat het ook mogelijk is om een laag te labelen, maar ook op te laten treden als obstakel-laag, door het keuzevak \"Voorkom dat labels objecten bedekken\" te selecteren op de tab \"Renderen\" van de instellingen voor labels.

Bekijk [dit artikel](http://nyalldawson.net/2015/07/recent-labelling-improvements-in-qgis-master/) voor meer details.

**Deze mogelijkheid werd ontwikkeld door:** [Nyall Dawson](http://nyalldawson.net/)

![image24](images/entries/de1eae1359ce92045d51c6fa9bc3f014a3f3ae67.webp)
### Mogelijkheid: Op regels gebaseerd labelen
Labels voor objecten kunnen nu met behulp van regels worden opgemaakt om nog meer beheer mogelijk te maken voor plaatsen en opmaken van labels. Net als het op regels gebaseerd cartografische renderen, kunnen regels voor labels worden genest om extreem flexibele opties voor opmaak mogelijk te maken. U kunt bijvoorbeeld labels verschillend renderen, gebaseerd op de grootte van het object waarin zij zullen worden gerenderd (zoals weergegeven in de schermafdruk).

Bekijk [blogpost](http://www.lutraconsulting.co.uk/blog/2015/10/25/rule-based-labeling/) voor meer details

**Deze mogelijkheid werd ontwikkeld door:** Martin Dobias van [Lutra Consulting](http://www.lutraconsulting.co.uk/) onder subcontract voor [Gis3W](http://www.gis3w.it/)

**Deze mogelijkheid werd mogelijk gemaakt door:** Tuscany Region (Italië) - SITA (CIG: 63526840AE)

![image25](images/entries/8846f57f0395e7f6b2543a92a5c55b67e8b19923.webp)
## Printvormgeving
### Mogelijkheid: Verbeteringen aan navigatie in atlas
U kunt nu een veld of expressie instellen als de \"paginanaam\" voor lay-outs in atlas. Een combinatievak voor paginanummering is toegevoegd aan de werkbalk voor Atlas, die een lijst weergeeft van zowel paginanummering als paginanamen. Dit maakt het voor u mogelijk om direct naar een specifieke pagina in uw atlas te springen.

De paginanaam kan ook worden gebruikt binnen expressies van symbologie en labelen om geavanceerd op maak objecten van de atlas mogelijk te maken, gebaseerd op hun paginanaam.

**Deze mogelijkheid werd ontwikkeld door:** [Nyall Dawson](http://nyalldawson.net/)

![image26](images/entries/bbf6147ef8be9d209fa188d6c524bce9d13d5ba8.webp)
### Mogelijkheid: Aangepaste indeling voor annotaties van het raster
Annotaties voor het raster van Printvormgeving kunnen nu worden opgemaakt in aangepaste indelingen, die worden geëvalueerd met behulp van het mechanisme voor de expressies. Nu kunt u elke esoterische indeling voor rasternummering gebruiken die uw kaart nodig heeft!

**Deze mogelijkheid werd ontwikkeld door:** [Nyall Dawson](http://nyalldawson.net/)

![image27](images/entries/a6cd03594ca802015ef4a5bf7806cc1ce291214b.webp)
### Mogelijkheid: Tekstafhandeling voor meerdere regels en automatische tekstdoorloop in attributentabellen van Printvormgeving
Attributentabellen bevatten nu volledige ondersteuning voor tekenreeksen van meerdere regels. Beheer over de verticale uitlijning van tekst in een cel is ook toegevoegd, naast opties voor het doorlopen van tekst voor bepaalde tekens of automatisch berekende tekstdoorloop om te passen in de grootte van de kolommen. Stel de breedte van de kolom in op ene vaste grootte om automatische tekstdoorloop met automatische rijhoogten af te dwingen.

**Deze mogelijkheid werd ontwikkeld door:** [Nyall Dawson](http://nyalldawson.net/)

**Dit werd mogelijk gemaakt door:** [Stad Uster](http://gis.uster.ch/)

![image28](images/entries/db66b56f79949779ea32126bd22f2f1c9d4b55e6.webp)
### Mogelijkheid: Geavanceerde aanpassing van achtergrondkleur van cellen
Deze wijziging stelt gebruikers in staat om verschillende kleuren in te stellen voor wisselende rijen en kolommen, eerste/laatste rij/kolom en koprij in attributentabellen van Printvormgeving.

**Deze mogelijkheid werd ontwikkeld door:** [Nyall Dawson](http://nyalldawson.net/)

**Dit werd mogelijk gemaakt door:** [Stad Morges](http://www.morges.ch/)

![image29](images/entries/68266f6b11599dfa226952455ca150448a5d082a.webp)
### Mogelijkheid: Optie Pagina aanpassen aan inhoud toegevoegd en opties voor bijsnijden van export naar inhoud
Een nieuwe optie is toegevoegd in het paneel Lay-out om een lay-out aan te passen aan de inhoud daarvan, met optioneel extra marges indien nodig.

Export vanuit printvormgeving kan ook worden bijgesneden tot zijn inhoud. Indien geselecteerd, zorgt deze optie ervoor dat de uitvoer van afbeeldingen van Printvormgeving alleen het gebied van de lay-out met inhoud bevat. Er is ook een optie om marges toe te voegen rondom de grenzen van het item indien nodig.

Als de lay-out een enkele pagina omvat, dan zal de uitvoer worden begrensd door ALLES op de lay-out. Als het een lay-out met meerdere pagina's is, dan zal elke pagina worden bijgesneden tot alleen het gebied met items op die pagina.

Een nieuw optiedialoogvenster voor exporteren is toegevoegd om dit mogelijk te maken, die ook handige sneltoetsen bevat voor het overschrijven van de afdrukresolutie of dimensies van de geëxporteerde afbeelding.

**Gesponsord door:** [NIWA](https://www.niwa.co.nz/)

**Deze mogelijkheid werd ontwikkeld door:** [Nyall Dawson](http://nyalldawson.net/)

![image30](images/entries/38572cf4aa662cc4463c2a29f3d5ca38aa382632.webp)
### Mogelijkheid: Vectorlagen forceren om te renderen als rasterafbeeldingen
Een nieuwe optie is toegevoegd onder de Laageigenschappen, tab Renderen, om een vectorlaag te forceren om te renderen als een raster. Extreem gedetailleerde lagen (bijv. polygonenlagen met een zeer groot aantal knopen) kunnen ervoor zorgen dat exporteren vanuit Printvormgeving naar de indelingen PDF/SVG zeer groot wordt als alle knopen worden opgenomen in het geëxporteerde bestand. Dat kan ertoe leiden dat het resulterende bestand zeer traag zal werken of openen in externe programma's. Nu kunt u forceren dat deze jagen worden gerasteriseerd op een laag-naar-laag basis, zodat de geëxporteerde bestanden niet alle knopen behoeven te hebben opgenomen in deze lagen. Het eindresultaat is kleinere bestandsgrootten en PDF's/SVG's die sneller te openen zijn.

**Deze mogelijkheid werd ontwikkeld door:** [Nyall Dawson](http://nyalldawson.net/)

![image31](images/entries/0127fe10ecae31dbcd133492c93f33b0d569dcba.webp)
### Mogelijkheid: Gegevens gedefinieerd beheer over kaartlagen en voorkeuren voor opmaak
Een nieuw gegevens gedefinieerd besturingselement is toegevoegd aan de kaartlagen en voorkeuren voor opmaak om in een kaart van printvormgeving weer te geven. De expressie voor gegevens gedefinieerde kaartlagen zou moeten resulteren in een \| (pipe) gescheiden lijst van laagnamen die op de kaart zullen worden weergegeven, of de expressie voor voorkeur gegevens gedefinieerde opmaak zou moeten resulteren in de naam van een bestaande voorkeur voor opmaak.

Gebruiken van dit besturingselement voor kaartlagen voor \"op lagen gebaseerde\" atlassen, waar de kaartlagen zouden wisselen tussen de pagina's van de atlas in plaats van of in combinatie met het wijzigende kaartbereik. Een voorbeeld zou een atlas kunnen zijn die over verschillende administratieve eenheden loopt en tegelijkertijd over verscheidene historische kaarten of luchtfoto's.

**Deze mogelijkheid werd ontwikkeld door:** [Nyall Dawson](http://nyalldawson.net/)

**Dit werd mogelijk gemaakt door:** [Stad Uster](http://gis.uster.ch/)

![image32](images/entries/a8dc3b35df4020897e39c81bd22a469ab5ea6225.webp)
### Mogelijkheid: Optie om pagina's te verbergen in een weergave/export
Er is nu een optie om de weergave van pagina's te verbergen tijdens het bewerken en exporteren van lay-outs. Deze optie is nuttig voor lay-outs die niet bedoeld zijn om af te drukken en niet zijn gebonden aan een vooraf ingestelde paginagrootte. U kunt de pagina's verbergen, dan items toevoegen of op grootte brengen op elke manier die u wilt zonder de visuele afleiding of begrenzingen van de pagina's!

**Gesponsord door:** [NIWA](https://www.niwa.co.nz/)

**Deze mogelijkheid werd ontwikkeld door:** [Nyall Dawson](http://nyalldawson.net/)
## Plug-ins
### Mogelijkheid: Bijwerken van de plug-in GRASS
De plug-in GRASS werd bijgewerkt om ondersteuning voor GRASS 7 mogelijk te maken. Door lagen voor GRASS kan worden gebladerd en geladen vanuit de browser van QGIS of het paneel Browser. GRASS vectorgegevens kunnen direct worden bewerkt in QGIS. Het project bevat de volgende werkpakketten:
- Plug-in bibliotheek upgrade en bouw voor meerdere versies
- Integratie van QGIS-browser en paneel Browser
- Ondersteuning voor mapsets, modules en shell om gegevensanalyses mogelijk te maken
- bewerken van vector

Vo zowel gebruikers van GRASS 6 en GRASS 7 zult u merken dat de integratie tussen GRASS en QGIS veel meer naadloos is. U kunt lagen voor GRASS direct in het paneel van de QGIS Browser maken, GRASS vectorlagen opmaken met behulp van de standaard gereedschappen voor opmaak van QGIS en bekende QGIS gereedschappen voor Digitaliseren gebruiken om nieuwe vector geometrieën te maken in een mapset van GRASS.

Bekijk ook de [projectpagina QGIS GRASS Plugin Upgrade](http://www.gissula.eu/qgis-grass-plugin-crowdfunding/) en [voortgangsrapport](http://www.gissula.eu/qgis-grass-plugin-crowdfunding/progress.html)

**Deze mogelijkheid werd ontwikkeld door:** [Radim Blazek](http://www.gissula.eu/)

**Dit werd mogelijk gemaakt door:** Crowdfunding, bekijk de [projectpagina](http://www.gissula.eu/qgis-grass-plugin-crowdfunding/)

![image33](images/entries/fb9ac25e9ca6c5e4030167e289435e995f5af8f5.webp)
## Programmeerbaarheid
### Mogelijkheid: Gereedschappen voor kaart verplaatst van app-\>gui
Deze wijziging maakt het mogelijk gereedschappen voor de kaart opnieuw te gebruiken binnen scripts van PyQGIS en Python plug-ins.

**Deze mogelijkheid werd ontwikkeld door:** Matthias Kuhn at [OpenGIS](http://www.opengis.ch/)

**Dit werd mogelijk gemaakt door:** [SIGE](http://www.sige.ch/)
### Mogelijkheid: Lagen bewerken via \`with edit(layer):\`
Voorbeeld:

    from qgis.core import edit
    
    with edit(layer):
       f=layer.getFeatures().next()
       f[0]=5
       layer.updateFeature(f)
    
Dit zal automatisch commitChanges() aan het eind aanroepen. Indien er een uitzondering optreedt zal het rollBack() alle wijzigingen.

**Deze mogelijkheid werd ontwikkeld door:** Matthias Kuhn at [OpenGIS](http://www.opengis.ch/)
### Mogelijkheid: Nieuwe API voor mechanisme voor labelen (QgsLabelingEngineV2)
Het idee is om het mechanisme meer flexibel te maken ten opzichte van QgsPalLabeling implementation:
> - abstract afhandelen met tekstlabels / diagrammen uit de aandrijving zelf
> - meerdere typen labels per laag toestaan
> - ondersteuning voor aangepaste labelproviders (bijv. geïmplementeerd door plug-ins)
> - de aandrijving voor de labels onafhankelijk maken van de aandrijving voor het renderen van de kaart
> - gemakkelijker maken voor het auto-testen van de aandrijving voor de labels en de componenten ervan

Bekijk [blogpost](http://www.lutraconsulting.co.uk/blog/2015/10/25/rule-based-labeling/) voor meer details

**Deze mogelijkheid werd ontwikkeld door:** Martin Dobias van [Lutra Consulting](http://www.lutraconsulting.co.uk/) onder subcontract voor [Gis3W](http://www.gis3w.it/)

**Deze mogelijkheid werd mogelijk gemaakt door:** Tuscany Region (Italië) - SITA (CIG: 63526840AE)
### Mogelijkheid: Scripts openen in externe bewerker
Vreugde voor Pythonistas- u kunt nu uw scripts openen in een externe bewerker met behulp van de nieuwe knop die is toegevoegd aan de console.

**Deze mogelijkheid werd ontwikkeld door:** [Nathan Woodrow](http://nathanw.net/)

![image34](images/entries/78acf0058f4306bf408a58df3762dff5986633a7.webp)
### Mogelijkheid: Nieuwe klassen voor programma's in PyQGIS
Een nieuwe klasse QgsStringUtils is toegevoegd wat het mogelijk maakt dat scripts van PyQGIS het nieuwe algoritmen voor fuzzy overeenkomsten kan gebruiken dat is toegevoegd in 2.12. Deze bevatten functies voor het zoeken naar de Levenshtein bewerkingsafstand tussen twee tekenreeksen en voor het berekenen van de fonetische weergave in Soundex van een tekenreeks. Deze algoritmen zijn zeer geoptimaliseerd voor uitvoering, dus zij zijn voor u klaar om te gebruiken voor beginnen te vergelijken van fuzzy overeenkomsten in miljoenen tekenreeksen!

**Deze mogelijkheid werd ontwikkeld door:** [Nyall Dawson](http://nyalldawson.net/)
## QGIS Server
### Mogelijkheid: QGIS Server Python API
QGIS Server is nu verpakt als een bibliotheek met een initiële (maar groeiende) API en verbindingen voor Python. Met de nieuwe API hebben we een verzameling Python-testen voor de hoofdcomponent van de server en voor de plug-ins van de server. Opstarten van de server vanuit Python is nu zo eenvoudig als:

    from qgis.server import QgsServer
    headers, body =  QgsServer().handleRequest(my_query_string)
    
Voor meer informatie, bekijk [dit artikel])http://www.itopen.it/qgis-server-binding-news/)

**Deze mogelijkheid werd ontwikkeld en mogelijk gemaakt door**: Alessandro Pasotti bij [ItOpen](http://www.itopen.it/)
### Mogelijkheid: getMap in indeling dxf
Het is nu mogelijk om het resultaat van een WMS-verzoek GetMap op te halen in de indeling DXF. Het ondersteunt dezelfde mogelijkheden en opties zoals die beschikbaar zijn in de desktop van QGIS. Met dezelfde beperkingen.

| Sample URL: | `http://yourserver.org/cgi-bin/qgismapserver.fcgi?` | `map=/path/to/your/projectfile.qgs&` | `SERVICE=WMS&` | `VERSION=1.3.0&` | `REQUEST=GetMAP&` | `FORMAT=application/dxf&` | `FORMAT_OPTIONS=SCALE:500;MODE:SYMBOLLAYERSYMBOLOGY&` | `FILE_NAME=youroutputfilename.dxf&` | `CRS=EPSG:EPSG:21781&` | `BBOX=695558.73070825,244430.77224034,697158.88528251,245722.25976142&` | `WIDTH=1042&` | `HEIGHT=841&` | `LAYERS=yourdxfexportlayers`

Bekijk ook de [handleiding voor QGIS server](http://docs.qgis.org/2.18/en/docs/user_manual/working_with_ogc/ogc_server_support.html#dxf-export) voor alle beschikbare opties.

In de schermafdruk ziet u links de QGIS Web Cliënt met de DXF exportfunctionaliteit (die gebruik maakt van QGIS server) en rechts hetzelfde bereik bekeken in Autodesk TrueView.

**Deze mogelijkheid werd ontwikkeld door:** Marco Hugentobler [Sourcepole AG](http://www.sourcepole.ch/)

**Dit werd mogelijk gemaakt door:** [Stad Uster](http://gis.uster.ch/)

![image35](images/entries/beb2e9c00102c67ae703eac097ffba8866379609.webp)
## Symbologie
### Mogelijkheid: Miniaturen exporteren vanuit Stijlbeheer
Stijlbeheer stelt u nu in staat geselecteerde miniaturen van stijl te exporteren, ofwel als afbeelding SVG of als PNG.

**Deze mogelijkheid werd ontwikkeld door:** [Nathan Woodrow](http://nathanw.net/)

![image36](images/entries/8861a040751804f6c2691ee4d93d410efd6d99ac.webp)
### Mogelijkheid: Nieuwe optie voor beperken van de grootte in mm bij gebruiken van grootten in kaarteenheden
Eerder was alleen de beperking voor het schaalbereik van kaarteenheden beschikbaar. Nu kunt u ook de overeenkomende gerenderde grootte in mm kiezen. 

![image37](images/entries/b822235ddb09b4184b926bf2e0acc5c892147d0b.webp)
### Mogelijkheid: Verbeteringen aan renderer voor verplaatsingen
- Tolerantie in mm/pixels mogelijk maken voor renderer van verplaatsingen
- Instellen van transparantie voor kleuren mogelijk maken
- Modus Concentrische ringplaatsing (maakt een meer compacte weergave mogelijk dan alleen met ringen)

**Deze mogelijkheid werd ontwikkeld door:** [Nyall Dawson](http://nyalldawson.net/)

![image38](images/entries/33b5f15429279a7ec75dd1f6a2e01b1a7df789ca.webp)
### Mogelijkheid: Alle kleurverlopen kunnen nu worden bewerkt
In QGIS 2.12 zijn knoppen \"Bewerken\" toegevoegd naast elke keuze voor een kleurverloop. Dit stelt u in staat eenvoudig een bestaand kleurverloop te bewerken zonder een nieuw verloop te moeten maken of het bestaande te overschrijven.

![image39](images/entries/6ca1426e6e9bfd5500b08fb2185ae50a77258892.webp)
### Mogelijkheid: Verbeterde behandeling van SVG markeringsomtrekkken
QGIS 2.12 repareert een aantal problemen met betrekking tot de afhandeling van omtrekken binnen SVG-markeringen en SVG-vulsymbolen.

Eerdere versies van QGIS renderden de omtrekken in een significant kleinere grootte dan ingesteld, en tekenen van SVG's in grootten van kaarteenheden was defect.

Deze problemen zijn gerepareerd in QGIS 2.12, maar als een resultaat daarvan moet u misschien uw symbologie van het project bijwerken als u eerder grotere omtrekken voor uw symbolen heeft ingesteld om deze problemen te verhelpen. In de afbeelding ziet u QGIS 2.12 vs QGIS 2.10 SVG-markeringen in het dialoogvenster Symboollaag.

![image40](images/entries/a678d22393345b4fcc07b5bd023babe383151b46.webp)
### Mogelijkheid: Pixels toegevoegd als optie voor alle keuzen van de eenheid van grootte voor Symbologie
Voor alle invoerwidgets voor grootte is er nu een derde optie \"pixel\", naast \"mm\" en \"kaarteenheden\". Dit betreft grootten van symbolen, dikte van lijnen, grootten van streepjes, verschuivingen, etc. Dit kan helpen indien u ontwerpt voor schermen en niet om af te drukken.

**Deze mogelijkheid werd ontwikkeld door:** [Nyall Dawson](http://nyalldawson.net/)

![image41](images/entries/cbc683061bcc06764361ab79874f1020ccfe8eb7.webp)

{{<content-end >}}
