---
Reviewed: 5 June 2024
Reviewer: Tim Sutton
draft: false
sidebar: true
subtitle: ''
title: Beveiliging
type: page

---
{{<content-start >}}
# Beveiliging
## Informatie over beveiliging
De gemeenschap van QGIS neemt beveiliging serieus. We zijn ons ervan bewust dat QGIS wordt uitgerold in gevoelige omgevingen. Deze pagina geeft een overzicht van hoe het project QGIS reageert op kwetsbaarheden en zaken met betrekking tot beveiliging.
### Wat is een kwetsbaarheid in QGIS?
QGIS is een project dat in vele contexten kan worden gebruikt en een hele rijke set aan mogelijkheden heeft. Om deze functionaliteit te kunnen verschaffen, vertrouwt het op veel componenten. Vertrouwen op een grote basis van externe afhankelijkheden (bijv. GDAL, PROJ, bibliotheken voor Python, Qt, etc.). Problemen met beveiliging in QGIS kunnen optreden in verscheidene scenario's, inclusief, maar niet beperkt tot, kwetsbaarheden in zijn afhankelijkheden, problemen binnen de code van QGIS zelf, of door het misbruiken van zijn bindingen van Python. Dit zijn de hoofdcategorieën:
#### Kwetsbaarheden van onderliggende bibliotheken
Wanneer u een codescanner uitvoert, zullen de meeste vermelde kwetsbaarheden niet zijn gerelateerd aan QGIS, maar aan zijn afhankelijkheden. De specifieke versie van de afhankelijkheden dat wordt meegeleverd met QGIS is afhankelijk van het besturingssysteem en het gebruikte verpakkingssysteem.

**Op Windows** gebruikt QGIS.org het project OSGeo4W om een volledige omgeving te distribueren. De bouw van OSGeo4W wordt volledig onderhouden door het project QGIS.

OSGeo4W verschaft updatescripts, wat het voor u mogelijk maakt alleen de noodzakelijke bibliotheken te upgraden, zonder de noodzaak om het gehele pakket opnieuw te downloaden. Voor meer informatie over het instellen van deze scripts voor uw uitrol, bekijk de [documentatie van OSGeo4W](https://trac.osgeo.org/osgeo4w/).

Op **[Ubuntu / Debian](/resources/installation-guide/#debian--ubuntu)** verschaffen we QGIS-binaries en werken nauw samen met de verpakkers van bibliotheken van OSGEO (GDAL / PROJ / GRASS). Voor bibliotheken van Python en Qt, die vertrouwen op uw besturingssysteem, zorg ervoor dat ze regelmatig worden bijgewerkt met de updatebeheerder van uw systeem. Voor Ubuntu/Debian wordt dit gewoonlijk gedaan met opdrachten zoals `sudo apt update` en `sudo apt upgrade`.

Andere pakketten voor distributies van Linux worden door de gemeenschap onderhouden, zoals Conda, FlatPak, etc. Elk probleem zou moeten worden voorgelegd aan de onderhouders van die lagergelegen distributies.
#### Valse positieven
Het ontvangen van rode vlaggen van meldingen van de codescanner kan alarmerend zijn, maar veel van de huidige meldingen zijn valse positieven. Blijf dus kalm en raak niet in paniek.

Een veelvoorkomende valse positieve zou bijvoorbeeld kunnen zijn dat de bibliotheek voor de cliënt van PostgreSQL (libpq) wordt gevlagd voor kwetsbaarheden aan de zijde van de server, die in het gebruiksgeval van QGIS niet van toepassing zijn.

Bij het ontdekken van een potentiële kwetsbaarheid, lees het CVE-rapport, ga naar de upstream project CVE-beschrijving en verifieer of dit echt betrekking heeft op QGIS.

Communiceer deze bevindingen ook met de verkoper van uw codescanner voor het bijwerken van de catalogus, om het aantal valse positieven dat in de toekomst wordt verzonden te verminderen.

Er is niet veel wat deelnemers aan QGIS kunnen doen om rapporten op te lossen waar de classificatie van afhankelijkheden niet nauwkeurig is in de database van CVE.
### Kwetsbaarheden van QGIS zelf
Deze zijn extreem uitzonderlijk, maar kunnen voorkomen (net zoals dat kan in elke software).

QGIS server en QGIS Desktop zijn geschreven om de mogelijkheid voor het injecteren van SQL en verscheidene bekende beveiligingsvectoren te beperken, en worden al vele jaren gebruikt door grote bedrijven en overheden.
## Wat te doen als u denkt dat u een beveiligingsprobleem hebt gevonden
Als u denkt dat u een probleem met de beveiliging hebt gevonden, zoals kwetsbaarheden in QGIS of de afhankelijkheden daarvan, doe dan het volgende:
- Controleer of u de laatste versie van QGIS gebruikt  hebt gekeken naar de nachtelijke versie voor potentiële doorgevoerde wijzigingen (reparaties of regressies).
- Controleer of uw probleem QGIS desktop betreft of QGIS server.
- Controleer onze [bug tracker](https://github.com/qgis/QGIS/issues) om te zien of we al een bestaande en potentiële reparatie hebben.
- Ervan uitgaande dat u nog steeds de issue wilt indienen, maakt u een privaat bericht aan de beveiligingsteams via [uw GitHub pagina voor beveiliging](https://github.com/qgis/QGIS/security). Vermijd publieke berichten die de kwetsbaarheid onthullen totdat die is opgelost, om mogelijk potentieel gebruik ervan te voorkomen.

#### Python QGIS uitvoeren
Bindingen voor Python stellen u in staat QGIS uit te breiden door het schrijven van plug-ins, modellen voor geoverwerking, acties, projectmacro's, of zelfs het herschrijven van een hele toepassing.

In een desktopomgeving geeft elke scripttaal over het algemeen volledige toegang tot de bronnen voor de gebruiker en kan deze willekeurige code uitvoeren met de rechten van de gebruiker. Wanneer u externe code uitvoert, kan dat in potentie behoorlijk veel schade aanrichten.

De [QGIS opslagplaats voor plug-ins](https://plugins.qgis.org) is open voor iedereen om te gebruiken om hun werk te publiceren. We beoordelen indieningen handmatig. We voeren geen geavanceerde beoordelingen voor QA uit van de code voor de plug-in. Plug-ins zouden geen gecompileerde code moeten bundelen, dus u weet van elke plug-in wat u krijgt en het staat u vrij de code te beoordelen.

Als u werkt in een gevoelige omgeving, adviseren we u om :
- Elke plug-in zorgvuldig te beoordelen in een zandbakomgeving, voordat u uw gebruikers toestaat om die te gebruiken.
- Rol uw eigen opslagplaats voor plug-ins uit, zodat u kunt beheren welke plug-ins voor uw gebruikers beschikbaar zijn.
- Maak gebruik van de geavanceerde mogelijkheden voor het aanpassen van QGIS om instellingen rond verbindingen, authenticatie etc. te beperken.
- Focus niet alleen op breuken in de code, maar ook op het gedrag van gebruikers met betrekking tot inloggegevens en het risico van lekken in projectbestanden als gebruikers staan op het gebruiken van basisauthenticatie (wat zal resulteren in het feit dat inloggegevens worden opgeslagen in platte tekst in projectbestanden).

### Maken we Common Vulnerabilities and Exposures (CVE)?
We kunnen CVE-identificaties verschaffen, wanneer u uw kwetsbaarheid doorgeeft via [Github advisories](https://github.com/qgis/QGIS/security). We zullen de CVE niet beïnvloeden als de kwetsbaarheid een upstream afhankelijkheid betreft.
### Beheren van beveiligingskwetsbaarheden en processen voor het doorgeven van kwetsbaarheden
Gevonden kwetsbaarheden worden privé besproken [Github advisories](https://github.com/qgis/QGIS/security)

Reparaties worden zo snel als mogelijk is doorgevoerd in puntuitgaven - afhankelijk van de ernst van het probleem.

Als u uw zakelijke uitrol van QGIS veilig wilt houden, zorg er dan voor dat u in staat bent snel reparaties uit te kunnen voeren aan de machines die u beheert.

OSGeo4W verschaft updatescripts die zonder toezicht kunnen worden uitgevoerd. Deze scripts maken het voor u mogelijk alleen de noodzakelijke bibliotheken te upgraden, zonder de noodzaak om het gehele pakket opnieuw te downloaden. Voor meer informatie over het instellen van deze scripts voor uw uitrol, bekijk de [documentatie van OSGeo4W](https://trac.osgeo.org/osgeo4w/).
### Zijn er onafhankelijke beveiligingsaudits beschiikbaar ?
De laatste beschikbare publieke audit werd uitgevoerd door het Zwitserse National Cyber Security Centre (NCSC) gedurende een [pilotproject voor het testen van beveiligingskwetsbaarheden in open source-software](https://www.bacs.admin.ch/en/25-ntc-oss-en).

{{<rich-list listLink="../media/ntc-test-report-qgis-v1-2025-10-13.pdf" linkAttr="download" layoutClass="third" listTitle="Security Audit QGIS Server and QWC2 - Test Report 2025.10.13 NCSC" listSubtitle=" PDF downloaden" >}}

QGIS is door vele organisaties privaat beoordeeld, soms in heel gevoelige context van beveiligingsbeheer tot netwerkprogramma's.<br />QGIS-server, omdat het een webserver is die interacteert met databases, is het kritiekste deel. Het is verhard tegen SQL-injecties.
### Zijn testen voor binnendringen uitgevoerd ?
QGIS Desktop is een programma voor de desktop, geen SaaS-software. Het heeft geen infrastructuur op afstand nodig.

QGIS-server is getest tegen kwetsbaarheden en volgt een klassieke procedure voor doorgeven / repareren.
### Veilige softwareontwikkeling en werkwijzen voor beoordelen van code
Een globaal overzicht van onze beveiliging is te vinden met het [gereedschap OpenSSF Scorecard report](https://securityscorecards.dev/viewer/?uri=github.com/qgis/QGIS).

MultiFactor-authenticatie is verplicht voor onze opslagplaatsen van Github.
### Mechanismen voor integriteit en verificatie van softwareuitgaven
Elk [beschikbaar pakket](https://www.qgis.org/resources/installation-guide/) is beschikbaar met een controlesom. Pakketten van macOS zijn genotariseerd. We zijn ons bewust van de risico's van XZ-stijl aanvallen op de aanvoerlijn. De deelnemers kunnen alleen privileges verdienen na een lange en betrokken periode, en na ontmoetingen in de echte wereld, gedurende onze bijeenkomsten voor deelnemers.
### Wat is het beleid voor ondersteunde versies en beveiligingsreparaties/EOL
Bekijk <https://www.qgis.org/resources/roadmap/>.
### Hoe wordt het beveiligingsbeheer voor afhankelijkheden van derde partijen uitgevoerd ?
QGIS.org ondersteunt alleen het verpakken van Ubuntu/Debian en Windows.

Afhankelijkheden voor Ubuntu/Debian zijn afhankelijk van de distributie van de gebruikers en is geen verantwoordelijkheid van QGIS.org.

De Windows-bibliotheek voor installatieprogramma's, via het [project OSGEO4W](https://trac.osgeo.org/osgeo4w). Onze beheerders zijn attent om zo snel mogelijk te reageren, afhankelijk van de kritieke ernst van de kwetsbaarheid.
### Beveiligingsbeheer of processen voor beoordelen van toepassing op plug-ins van derde partijen voor QGIS
QGIS Desktop wordt verpakt met een installatieprogramma voor plug-ins van Python, dat gebruikers in staat stelt uitbreidingen van derde partijen te installeren, net zoals webbrowsers doen.

Bekijk <https://plugins.qgis.org/docs/security-scanning>

Omdat het uitvoeren van Python in een desktopomgeving alle privileges van een gebruiker erft, zou het uitrollen in gevoelige omgevingen direct toegang tot deze opslagplaats moeten deactiveren en die vervangen door een interne opslagplaats die alleen geaudite plug-ins toestaat.
### Geeft u ISO 27001-certificatie, SOC 2, CRA-attestatie uit ?
Nee, dat doen we niet. Als u ze nodig hebt, neem dan contact met ons op en overweeg het ondersteunen van QGIS.org om de werkdruk, die de vereisten voor compliance van ons vragen, te verlichten. QGIS.org is geen serviceprovider, en QGIS is beschikbaar volgens de bepalingen van de licentie GPL 2.
### Kan QGIS.org mijn eigen formulier voor compliance vullen ?
QGIS.org is een stichting die wordt bekostigd uit donaties en kosten voor lidmaatschap. We hebben beperkte bronnen naast onze vrijwillige en betaalde staf. We zien tegenwoordig een tendens dat elke organisatie zijn eigen formulier maakt. We kunnen ze niet voor u invullen, maar we zullen zoveel mogelijk informatie hier op de website plaatsen om u te helpen bij het invullen van die formulieren. Zodra die formulieren een nationale of internationale standaard volgen, zal het voor ons een plezier zijn om die online te publiceren.

U kunt bijvoorbeeld de formulieren US HECVAT en VPAT, beheerd door de US-gebruikersgroep, gepubliceerd vinden op <https://www.qgis-us.org/hecvat/> and <https://www.qgis-us.org/vpat/>.

{{<content-end >}}
