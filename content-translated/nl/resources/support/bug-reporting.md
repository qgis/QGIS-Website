---
draft: false
sidebar: true
subtitle: ''
title: Problemen rapporteren
type: page

---
{{<content-start >}}
# Bugs, mogelijkheden en problemen
QGIS is een grotendeels door vrijwilligers gedreven project, en is het werk van een toegewijd team van ontwikkelaars, schrijvers van documentatie, vertalers en supporters. Ondanks de inspanningen van het team om QGIS uit te geven zonder bugs, zouden er enkele bugs kunnen achterblijven. Als u een bug vindt of wilt dat nieuwe mogelijkheden worden toegevoegd, rapporteer ze dan!
## Waar te melden?
Elk deel van het project QGIS heeft een toegewezen plaats waar problemen (verzoeken voor mogelijkheden of bugs) kunnen worden gerapporteerd, beheerd en besproken. Afhankelijk van het gebied waar u het probleem tegenkwam geeft de tabel hieronder de juiste opslagplaats  weer om het te melden:
| Plaats waar u het probleem vond of een mogelijkheid voor wilt vragen | Plaats om het probleem te melden |
| --- | --- |
| Toepassingen (QGIS Desktop, QGIS Server) | https://github.com/qgis/QGIS/issues |
| QGIS Website (https://qgis.org) | https://github.com/qgis/QGIS-Website/issues |
| QGIS documentatie (https://docs.qgis.org) | https://github.com/qgis/QGIS-Documentation/issues |
| C++ API (https://qgis.org/api) | https://github.com/qgis/QGIS/issues |
| PyQGIS API (https://qgis.org/pyqgis) | https://github.com/qgis/QGIS/issues (voor inhoud) en https://github.com/qgis/pyqgis/issues (voor opmaak) |
| QGIS Plugins Website (https://plugins.qgis.org) | https://github.com/qgis/QGIS-Plugins-Website/issues |
| QGIS Hub Website (https://hub.qgis.org) | https://github.com/qgis/QGIS-Hub-Website/issues |
| QGIS Planet Website (https://planet.qgis.org) | https://github.com/qgis/QGIS-Planet-Website/issues |
| QGIS Changelog Website (https://changelog.qgis.org) | https://github.com/kartoza/prj.app/issues |
| QGIS Feed Website (https://feed.qgis.org) | https://github.com/qgis/qgis-feed/issues |
| Externe plug-ins | De opslagplaats die door de auteur is ingesteld in de beschrijving van de plug-in |

Voor hulp en vragen, neem contact op met de [mailinglijsten]({{< ref "community/organisation/mailinglists" >}}).
## Problemen rapporteren over toepassingen van QGIS
Problemen voor toepassingen voor QGIS (QGIS Desktop en QGIS Server) zijn beschikbaar in  [Github](https://github.com/qgis/QGIS/issues). U dient zich te registreren en in te loggen als u een rapport wilt indienen of daarbij een opmerking wilt achterlaten.
### Vóór het rapporteren van een probleem
Controleer, voordat u een fout gaat registreren, of u de momenteel ondersteunde versies {{< param "ltrrelease" >}} of {{< param "release" >}} uitvoert of de ontwikkelversie {{< param "devversion" >}} (bekijk ook [het uitgaveschema]({{< ref "resources/roadmap#release-schedule" >}})) en bekijk de momenteel nog openstaande problemen om er zeker van te zijn dat u geen duplicaat maakt. Wanneer u aanvullende informatie heeft voor een bestaand ticket, kunt u die hieraan toevoegen. Plug-ins van derden kunnen ook leiden tot problemen. Wanneer u plug-ins hebt geïnstalleerd, controleer of de fout zich ook voordoet zonder geïnstalleerde plug-ins. Rapporteer niet meerdere fouten in één ticket als die niets met elkaar te maken hebben. 

Als u bent ingelogd, is een knop `New Issue` beschikbaar. Selecteer die en volg de instructies die daar gegeven worden.

Controleer de opmaak van uw rapport door te klikken op “Preview” vóór u het probleem verzendt. Vermijd het bewerken van bestaande rapporten, met uitzondering van typefouten. Voeg verder opmerkingen liever in een afzonderlijke aanvulling toe.
#### Maken van een backtrace
Als u een crash heeft zou het handig zijn om een backtrace op te nemen omdat het probleem misschien niet te reproduceren is op een andere machine.

Op Linux probeert QGIS automatisch `gdb` te gebruiken om te verbinden met het gecrashte proces om een backtrace te produceren. Maar sommige distributies schakelen de mogelijkheid om debuggers met lopende processen te verbinden uit. In dat geval produceert `gdb` alleen een nogal onbruikbaar bericht zoals:

QGIS died on signal 11Could not attach to process. If your uid matches the uid of the target process, check the setting of /proc/sys/kernel/yama/ptrace_scope, or try again as the root user. For more details, see /etc/sysctl.d/10-ptrace.conf ptrace: Operation not permitted. No thread selected No stack. gdb returned 0 Aborted (core dumped)

In dat geval zou u die optie opnieuw in moeten schakelen door `kernel.yama.ptrace_scope` in te stellen op 0 in `/etc/sysctl.d/10-ptrace.conf` (of `/etc/sysctl.conf` of enig ander bestand in `/etc/sysctl.d/`) en `sysctl -p` uit te voeren als root.  Wanneer u daarna de crash reproduceert, zal in plaats daarvan een backtrace worden afgedrukt.

Als u de crash niet kunt reproduceren, zou er nog steeds een bron-dump in de huidige map moeten staan, die kan worden geanalyseerd nadat het proces al was beëindigd.  Het is genaamd `core`  hoewel op sommige systemen een punt en het proces_ID aan de bestandsnaam worden toegevoegd.

Op sommige distributies is het maken van brondumps ook uitgeschakeld. Dat is het geval als u slechts `Aborted` krijgt in plaats van `Aborted (core dumped)` als de crash voorkomt. Dan moet u `ulimit -c unlimited` uitvoeren voordat u QGIS start. U kunt dat ook in uw `.profile` opnemen, zodat het altijd ingeschakeld is als u inlogt.

U start `gdb /pad/naar/de/qgis/binary core` om een backtrace uit het bronbestand te produceren. De binary is gewoonlijk `/usr/bin/qgis` of `/usr/bin/qgis.bin` op Debian met de plug-in GRASS geïnstalleerd. In `gdb` voert u `bt` uit wat de backtrace zal produceren.
#### Log uitvoer op Windows
De nachtelijke bouw in [OSGeo4W](https://trac.osgeo.org/osgeo4w) (package qgis-dev) wordt gebouwd met uitvoer als debuggen, die u kunt bekijken met [DebugView](https://docs.microsoft.com/en-us/sysinternals/downloads/debugview). Als het probleem niet eenvoudig is te reproduceren, zou de uitvoer misschien enig licht kunnen werpen op waar QGIS crasht.
## Problemen rapporteren over QGIS website of documentatie
Het project QGIS verschaft een actieve [website](https://qgis.org) en rijke [documentatie](https://qgis.org/en/docs/index.html). Ondanks onze inspanningen, als u gedateerde informatie vindt, of een verkeerd of niet juist argument, of als er waardevolle informatie ontbreekt, laat het ons dan weten.

De belangrijkste bronnen van deze documenten worden gehost en beheerd in opslagplaatsen van GitHub, dus om bugs te rapporteren of patches in te dienen, heeft u een account voor GitHub nodig om in te kunnen loggen.

Maak, om te beginnen, eerst [een account voor GitHub](https://github.com/join) aan.

Kies dan de van toepassing zijnde opslagplaats :
- https://github.com/qgis/QGIS-Documentation/issues voor documentatie van QGIS
- https://github.com/qgis/QGIS-Website/issues voor de website

Controleer of het probleem dat u wilt melden al niet is geregistreerd.

Klik op **New Issue**, typ een titel en een heldere beschrijving voor uw probleem.

Wanneer u gereed bent, klik op **Submit new issue**.

Opmerking

Een link `Fix me` wordt verschaft aan de onderzijde van elke pagina van de website om u te helpen deze pagina direct te verbeteren en een pull request in te dienen.

Deze optie is ook beschikbaar in de voettekst van de documentatie.
## Problemen met plug-ins melden
De meeste plug-ins in QGIS zijn gepubliceerd op de officiële [QGIS Plugins repository](https://plugins.qgis.org/plugins/). Problemen of verzoeken voor mogelijkheden in relatie daarmee **moeten** worden geopend in hun respectievelijke systeem voor het volgen van problemen.
- Voor elke beschikbare plug-in in de opslagplaats van QGIS vindt u in de metadata ervan een link naar het volgsysteem voor problemen ervan. Raadpleeg anders de documentatie van de plug-in om naar het adres van het relevante systeem voor het volgen van problemen te zoeken of om contact op te nemen met een ontwikkelaar.
  
  Als er geen informatie beschikbaar is, rapporteer dat dan op de [Developer mailinglijst](https://lists.osgeo.org/mailman/listinfo/qgis-developer).
- Voor andere plug-ins hebben we geen mogelijkheden om er voor te zorgen dat dergelijke informatie wordt verschaft.

## Een patch indienen voor projecten van QGIS
In aanvulling op het rapporteren van het probleem, kunt u helpen om ze op te lossen. Oplossen van problemen wordt gedaan in GitHub door middel van pull requests. U dient de [repository te forken](https://help.github.com/articles/working-with-forks/) wanneer u wilt deelnemen en pull requests wilt indienen.
- https://github.com/qgis/QGIS voor de toepassingen QGIS Desktop of QGIS Server
- https://github.com/qgis/QGIS-Website voor de website op https://qgis.org
- https://github.com/qgis/QGIS-Documentation voor de beschikbare documentatie op https://docs.qgis.org

U kunt een aantal richtlijnen vinden die u helpen om uw patches en pull requests gemakkelijk in projecten van QGIS te krijgen op [Submitting Pull Requests](https://docs.qgis.org/testing/en/docs/developers_guide/git.html#submitting-pull-requests). En breder, misschien moet u het hoofdstuk [Development Process](https://docs.qgis.org/testing/en/docs/developers_guide/git.html) lezen.

{{<content-end >}}
