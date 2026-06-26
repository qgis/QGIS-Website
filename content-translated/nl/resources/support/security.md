____
type: "page" title: "Security" subtitle: "" draft: false sidebar: true Reviewed: 5 June 2024 Reviewer: Tim Sutton
-
{{<content-start >}}
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
Momenteel is het project QGIS **geen** CVE Numbering Authority (CNA), dus geven we geen identificaties voor CVE uit.
### Beveiligingsproces en werkstroom
Onthullingen worden besproken in een daarvoor aangewezen private opslagplaats.

Reparaties worden zo snel als mogelijk is doorgevoerd in puntuitgaven - afhankelijk van de ernst van het probleem.

Als u uw zakelijke uitrol van QGIS veilig wilt houden, zorg er dan voor dat u in staat bent snel reparaties uit te kunnen voeren aan de machines die u beheert.

OSGeo4W verschaft updatescripts die zonder toezicht kunnen worden uitgevoerd. Deze scripts maken het voor u mogelijk alleen de noodzakelijke bibliotheken te upgraden, zonder de noodzaak om het gehele pakket opnieuw te downloaden. Voor meer informatie over het instellen van deze scripts voor uw uitrol, bekijk de [documentatie van OSGeo4W](https://trac.osgeo.org/osgeo4w/).

{{<content-end >}}
