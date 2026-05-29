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
- Check you are using the latest version of QGIS, and have a glance at the nightly version for potential ongoing changes (fixes or regressions).
- Check if your issue concerns QGIS desktop or QGIS server.
- Please check our [bug tracker](https://github.com/qgis/QGIS/issues) to see if we already have an existing and potential fix.
- Assuming you still need to raise the issue, raise a private disclosure to the security teams via [our GitHub security page](https://github.com/qgis/QGIS/security). Please avoid publicly disclosing the vulnerability until it has been resolved to prevent potential exploitation.

#### Running python QGIS
Python bindings allow you to extend QGIS by writing plugins, geoprocessing models, actions, project macros, or even rewrite a full application.

In a desktop environment, any scripting language typically has full access to the user's resources and can execute arbitrary code with the permissions of the user. If you execute external code it can potentially do a lot of harm.

The [QGIS plugins repository](https://plugins.qgis.org) is open for anyone to use to publish their work. We review submissions manually. We do not undertake advanced QA assessments of plugin code. Plugins should not bundle compiled code, so you know what you get in each plugin and are free to audit the code.

If your are working in a sensitive environment, we advise you to :
- Carefully audit each plugin in a sandboxed environment before you allow your users to use it.
- Deploy your own plugin repository so that you can control which plugins are available to your users.
- Make use of the advanced customization capabilities of QGIS to constrain settings around connections, authentication etc.
- Don't only focus on code breaches, but also on user behavior regarding credentials and the risk of leaks in project files if users insist on using basic authentication (which will result in credentials being stored in plain text in project files).

### Do we generate Common Vulnerabilities and Exposures (CVE)?
Currently, QGIS project is **not** a CVE Numbering Authority (CNA), so we don't emit CVE identifiers.
### Security Process and workflow
Disclosures are discussed in a private dedicated repository.

Fixes are shipped as soon as possible in point releases - depending on the criticality of the issue.

If you want to secure your QGIS enterprise deployment, please ensure you are able to quickly deploy fixes to the machines you manage.

OSGeo4W provides update scripts that can run unattended. These scripts also allow you to upgrade only the necessary libraries without the need to re-download the entire package. For more information on setting up these scripts for your deployment, refer to the [OSGeo4W documentation](https://trac.osgeo.org/osgeo4w/).

{{<content-end >}}
