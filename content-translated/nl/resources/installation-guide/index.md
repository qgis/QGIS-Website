---
Reviewed: 4 June 2024
Reviewer: Tim Sutton
draft: false
sidebar: true
subtitle: ''
title: Installatiehandleiding
type: page

---
{{<content-start >}}
# QGIS Installatiepakketten
QGIS is beschikbaar voor Windows, macOS, Linux, FreeBSD, OpenBSD, Android en iOS.

![Icons of Operating Systems](img/icons.png)

We raden aan de pakketten voor de Long Term Release (LTR) te installeren, omdat onze versies voor LTR meer intensieve testen ondergaan voor de uitgave en ten minste een jaar lang probleemvrije updates ontvangen.

Bekijk ook [de hoofdpagina voor installatieprogramma's]({{< ref "download" >}}).

We verschaffen ook testpakketten om de aanstaande uitgaven te evalueren en het voor niet-ontwikkelaars mogelijk te maken de ontwikkeling te ondersteunen (let op de [waarschuwing](#warning)).

In de fase Bevriezing, voorafgaande aan een uitgave (bekijk [Uitgaveschema]({{< ref "roadmap#release-schedule" >}})), zijn deze pakketten in feite **pre-uitgaven, waarvoor we gebruikers sterk adviseren ze te testen**.
# Windows
Er zijn twee opties voor het installeren op Windows:
## Offline (zelfstandige) installatieprogramma's
Zelfstandige installatieprogramma's bevatten alles wat QGIS nodig heeft in een enkele download. Als u het installatieprogramma eenmaal hebt, is er geen internet vereist om de installatie te voltooien. Wanneer een nieuwe uitgave beschikbaar is, moet u het volledige installatieprogramma opnieuw downloaden om te upgraden. Voor beginners is het zelfstandige installatieprogramma waarschijnlijk de gemakkelijkste manier om QGIS te installeren:
| Uitgave | Versie | Pakket | Alternatief |
| --- | --- | --- | --- |
| Laatste uitgave | {{< param "release" >}} {{< param "codename" >}} {{< param "releasenote" >}} | [Installatieprogramma]({{< param "lr_msi" >}}) [Controlesom]({{< param "lr_sha" >}}) | [Torrent]({{< param "lr_msi_torrent" >}}) [Magnet]({{< param "lr_msi_magnet" >}}) [Metalink]({{< param "lr_msi_meta4" >}}) |
| Lange Termijn Release | {{< param "ltrrelease" >}} {{< param "ltrcodename" >}} {{< param "ltrnote" >}} | [Installatieprogramma]({{< param "ltr_msi">}}) [Controlesom]({{< param "ltr_sha">}}) | [Torrent]({{< param "ltr_msi_torrent" >}}) [Magnet]({{< param "ltr_msi_magnet" >}}) [Metalink]({{< param "ltr_msi_meta4" >}}) |
| Ontwikkeling | {{< param "devversion" >}} master | [Wekelijkse snapshots]({{< param "weekly_msi">}}) | – |

Wegens hun enorme grootte werden de optionele projectierasters uitgesloten van de standaardinstallatieprogramma's. QGIS zal in runtime identificeren welke rasters vereist zijn voor opnieuw projecteren en vragen om ze handmatig te downloaden.

Voor omgevingen waarvoor dat niet mogelijk of onhandig is, zijn er nog steeds zelfstandige installatieprogramma's die de rasters bevatten. Vanaf 4.0.1 is het normale installatieprogramma 0.5 GiB, waar het installatieprogramma dat alle rasters bevat 1.2 GiB groot is.
| Uitgave | Versie | Pakket | Alternatief |
| --- | --- | --- | --- |
| Laatste uitgave | {{< param "release" >}} {{< param "codename" >}} {{< param "releasenote" >}} | [Installatieprogramma]({{< param "lr_grids_msi" >}}) [Controlesom]({{< param "lr_grids_sha" >}}) | [Torrent]({{< param "lr_grids_msi_torrent" >}}) [Magnet]({{< param "lr_grids_msi_magnet" >}}) [Metalink]({{< param "lr_grids_msi_meta4" >}}) |
| Lange Termijn Release | {{< param "ltrrelease" >}} {{< param "ltrcodename" >}} {{< param "ltrnote" >}} | [Installatieprogramma]({{< param "ltr_grids_msi">}}) [Controlesom]({{< param "ltr_grids_sha">}}) | [Torrent]({{< param "ltr_grids_msi_torrent" >}}) [Magnet]({{< param "ltr_grids_msi_magnet" >}}) [Metalink]({{< param "ltr_grids_msi_meta4" >}}) |

Het is ook mogelijk de rasters later toe te voegen door de opgenomen "OSGeo4W Setup" te gebruiken om het pakket `proj-data` te installeren. Of door het ook opgenomen programma voor de opdrachtegrel te gebruiken [projsync](https://proj.org/en/stable/apps/projsync.html) om de rasters voor een opgegeven gebied te downloaden.

De wekelijkse snapshots van het nachtelijke qgis-dev pakket van OSGeo4W zijn voor gebruikers die om de een of andere reden OSGeo4W (zie hieronder) niet kunnen gebruiken of juist zelfstandige installatieprogramma's prefereren. In de fase Mogelijkheden bevriezen treden deze ook op als installatieprogramma's voor **release candidate**.
## Online (OSGeo4W) installatieprogramma
Meer gevorderde gebruikers van QGIS zouden de pakketten van OSGeo4W willen gebruiken. Dit installatieprogramma maakt het mogelijk om verscheidene versies van QGIS parallel te installeren en ook veel efficiëntere updates uit te voeren, omdat alleen gewijzigde componenten worden gedownload en geïnstalleerd met elke nieuwe uitgave.

De opslagplaats voor OSGeo4W bevat daarnaast veel software van andere OSGeo-projecten. QGIS en alle daarvoor noodzakelijke pakketten zijn aanwezig, naast Python, GRASS, GDAL enzovoort. Het installatiepakket geeft de mogelijkheid om direct vanaf internet te installeren of eerst de benodigde pakketten te downloaden en daarna te installeren. De gedownloade bestanden worden in een lokale map geplaatst voor toekomstige installaties. En zouden ook kunnen worden gebruikt om offline te installeren.:

Stappen voor installeren zijn:
- Download [OSGeo4W installatiepakket](https://download.osgeo.org/osgeo4w/v2/osgeo4w-setup.exe) en voer het uit.
- Kies _Express Install_ en selecteer _QGIS_ om de _latest release_ te installeren en/of _QGIS LTR_ om de _long term release_ te installeren.

Als alternatief, in plaats van installeren met _Express_ zou u ook de _Advanced Install_ kunnen gebruiken. Navigeer naar het gedeelte _Desktop_ en selecteer een of meer van de volgende pakketten:
| Uitgave | Versie | Pakket | Beschrijving |
| --- | --- | --- | --- |
| Laatste uitgave | {{< param "release" >}} {{< param "codename" >}} {{< param "releasenote" >}} | qgis | Uitgave |
|  |  | qgis-rel-dev [[1]](#id1) | Nachtelijke bouw van de komende uitgave |
| Lange Termijn Release | {{< param "ltrrelease" >}} {{< param "ltrcodename" >}} {{< param "ltrnote" >}} | qgis-ltr | Uitgave |
|  |  | qgis-ltr-dev [[1]](#id1) | Nachtelijke bouw van de komende lange termijn puntuitgave (Qt5) |
| Ontwikkeling | {{< param "devversion" >}} master | qgis-dev [[1]](#id1) | Nachtelijke bouw van de ontwikkelversie[[2]](#id2) |

{{< footnote "1" >}} Nachtelijke bouw zijn bouwsels voor debuggen (inclusief uitvoer voor debuggen die door ontwikkelaars kan worden gebruikt om problemen met de bouw beter te begrijpen).

{{< footnote "2" >}} 4.0 markeert de wisseling naar Qt6. Eerdere versies van QGIS waren experimenteel met Qt6. Vanaf 4.0 wordt alleen Qt6 ondersteund.

De in de bovenstaande tabel vermelde pakketten installeren alleen de noodzakelijke pakketten om QGIS uit te kunnen voeren.  Corresponderend met deze pakketten zijn er ook metapakketten met de achtervoegsels `-full-free` en `-full`.   De `-full-free` bevat aanvullende optionele afhankelijkheden die enkele populaire (niet in de standaardinstallatie van QGIS opgenomen) plug-ins gebruiken. De `-full` bevat alles van `-full-free` en voegt ook merkgebonden extensies toe, zoals Oracle, ECW en MrSID.

De installatie van Express verwijst naar de corresponderende variant `-full` en de zelfstandige installatieprogramma's worden ook gemaakt uit deze sets van OSGeo4W-pakketten.

De varianten `-full-grids` bevatten de optionele projectierasters (d.i. `-full` plus het pakket `proj-data`). De grote zelfstandige zijn op deze gebaseerd.

Let op de [waarschuwingen](#warning) hieronder voordat u een van de nachtelijke bouwsels installeert.
# Linux
De meeste Linuxdistributies splitsen QGIS in verschillende installatiepakketten; meestal heb je `qgis` en `qgis-python` (voor plug-ins) nodig. Installatiepakketten zoals `qgis-grass` (of `qgis-plugin-grass`), `qgis-server` kunnen worden geïnstalleerd als die nodig zijn. 

Hieronder vindt u specifieke instructies per distributie. Voor de meeste distro's zijn er instructies om QGIS stabiel te installeren en instructies om een allernieuwste QGIS testversie te installeren (let op de [waarschuwing](#warning)).
## Debian / Ubuntu
### Snel starten
{{<rich-box-start icon="💁" layoutClass="tips" >}}

{{<rich-content-start themeClass="coloring-1" >}}
##### Opmerking
In het gedeelte dat hierop volgt zult u ALLE mogelijke opties vinden om verschillende versies van QGIS in verschillende versies van Debian/Ubuntu te installeren. Als u problemen tegenkomt, verifieer dan of uw distributie nog steeds wordt ondersteund. Omdat de opslagplaatsen ook oudere **niet ondersteunde** distributies, met de laatste versie van QGIS die wel werd ondersteund, bevatten. Wees er bedacht op dat die in de tussentijd kunnen zijn gestopt met werken.

{{<rich-content-end >}}

{{<rich-box-end >}}

Installeer eenvoudigweg de laatste stabiele versie van QGIS ({{< param "version" >}}.x {{< param "codename" >}}) in uw Debian of Ubuntu, zonder config-bestanden te moeten bewerken.

{{<rich-box-start icon="🌀" layoutClass="tips" >}}

{{<rich-content-start themeClass="coloring-1" >}}
##### Opmerking
Hoewel u op enkele plaatsen ‘Debian’ zult zien staan, werkt dit ook voor ‘Ubuntu’, omdat de een in feite een symlink is naar de andere op uw server.

{{<rich-content-end >}}

{{<rich-box-end >}}

Installeer eerst enkele gereedschappen die nodig zijn voor deze instructies:
```
sudo apt install gnupg software-properties-common
```
Installeer nu de QGIS Signing Key, zodat de software van QGIS vanuit de opslagplaats van QGIS zal worden vertrouwd en geïnstalleerd:
```
sudo mkdir -m755 -p /etc/apt/keyrings  # not needed since apt version 2.4.0 like Debian 12 and Ubuntu 22 or newer
sudo wget -O /etc/apt/keyrings/qgis-archive-keyring.gpg https://download.qgis.org/downloads/qgis-archive-keyring.gpg
```
Voeg de repo van QGIS voor de laatste stabiele QGIS ({{< param "version" >}}.x {{< param "codename" >}}) toe aan `/etc/apt/sources.list.d/qgis.sources`. Open het bestand in een tekstbewerker (bijv. `sudo editor /etc/apt/sources.list.d/qgis.sources`) en plak de volgende inhoud (vervang `your-distributions-codename` door de feitelijke codenaam van uw distributie, bekijk [Beschikbare codenamen](#available-codenames)):
```
Types: deb deb-src
URIs: https://qgis.org/debian
Suites: your-distributions-codename
Architectures: amd64
Components: main
Signed-By: /etc/apt/keyrings/qgis-archive-keyring.gpg
```
{{<rich-box-start icon="💬" layoutClass="tips" >}}

{{<rich-content-start themeClass="coloring-1" >}}
##### Opmerking
`Suites` in bovenstaande regels zijn afhankelijk van uw distributie. `lsb_release -cs` zal de naam van uw distributie weergeven.

In sommige distributies (zoals Linux Mint), zal `. /etc/os-release; echo "$UBUNTU_CODENAME"` de correcte naam van de distributie weergeven.

Bekijk [Beschikbare codenamen](#available-codenames).

{{<rich-content-end >}}

{{<rich-box-end >}}

Sla het bestand op en sluit het. Werk dan de informatie van uw repository bij:
```
sudo apt update
```
Voer, om QGIS te installeren, uit:
```
sudo apt install qgis qgis-plugin-grass
```
{{<rich-box-start icon="✍️" layoutClass="tips" >}}

{{<rich-content-start themeClass="coloring-1" >}}
##### Opmerking
Voeg `qgis-server` toe aan bovenstaande regel als u ook QGIS Server wilt installeren

{{<rich-content-end >}}

{{<rich-box-end >}}
### Repositories
Standaardopslagplaatsen voor software van Debian en Ubuntu bevatten vaak oudere versies van QGIS.

U moet, om de nieuwere versies te verkrijgen, eerst alternatieve opslagplaatsen voor software toevoegen, door een van de deb-regels hieronder toe te voegen aan uw bestand `/etc/apt/sources.list.d/qgis.sources`.

Onze hoofdopslagplaats bevat meerdere regels met pakketten voor verscheidene versies van **Debian en Ubuntu**, gebaseerd op de afhankelijkheden die de afzonderlijke distributies bieden.

Voor Ubuntu hebben we ook extra pakketten, die zijn gebaseerd op [ubuntugis](https://launchpad.net/~ubuntugis), in een afzonderlijke opslagplaats, wat meer up-to-date versies van andere GIS-pakketten bevat dan Ubuntu zelf voor versies LTS. Als u deze wilt, dient u ook ubuntugis-unstable ppa op te nemen in uw bestand /etc/apt/sources.list.d/qgis.list (bekijk de [documentatie van ubuntugis](https://trac.osgeo.org/ubuntugis/wiki/UbuntuGISRepository)).

{{<rich-box-start icon="💁" layoutClass="tips" mode="html" >}}

{{<rich-content-start themeClass="coloring-1" >}}
##### Opmerking
De uitgavenpakketten worden eenmalig gemaakt, kort nadat een nieuwe versie wordt uitgebracht. Onstabiele of nog niet uitgebrachte versies van Debian (testing) en ubuntugis-unstable kunnen verschillen in onderliggende functiebibliotheken bevatten, en zouden voor deze doelen na verloop van tijd misschien niet meer werken. Omdat de ontwikkeling van Debian, Ubuntu en Ubuntugis-unstable doorgaat en hun pakketten voor afhankelijkheden in de door QGIS gebruikte versie wijzigen. In dat geval kunt u ofwel:
- overgaan naar een stabiele versie van Debian en de daarvoor uitgegeven pakketten gebruiken,
- wachten op de volgende puntuitgave (verwacht {{< param "nextpointreleasedate" >}}), die elke maand komt en de bijgewerkte afhankelijkheden zal bevatten,
- overschakelen naar een nightly-opslagplaats (beschikbaar voor de **twee** releasebranches en master) waarvan de pakketten op een regelmatige basis opnieuw worden gebouwd en dan ook automatisch de bijgewerkte afhankelijkheden zullen bevatten of
- uw eigen set pakketten bouwen (bekijk [Debian pakketten bouwen](https://github.com/qgis/QGIS/blob/master/INSTALL.md#310-building-debian-packages)).

{{<rich-content-end >}}

{{<rich-box-end >}}

Lijnen van pakketten:
| Uitgave | Versie | Beschrijving | Opslagplaats |
| --- | --- | --- | --- |
| Laatste uitgave | {{< param "version" >}}.x {{< param "codename" >}} {{< param "releasenote">}} | Uitgave voor **Debian en Ubuntu** | https://qgis.org/debian <br> https://qgis.org/ubuntu |
|  |  | Uitgave met afhankelijkheden voor ubuntugis-unstable | https://qgis.org/ubuntugis |
|  |  | Nachtelijke bouw van de komende puntuitgave voor Debian en Ubuntu | https://qgis.org/debian-nightly-release <br> https://qgis.org/ubuntu-nightly-release |
|  |  | Nachtelijke bouw van de komende puntuitgave met afhankelijkheden voor ubuntugis-unstable | https://qgis.org/ubuntugis-nightly-release |
| Opslagplaats Lange termijn-uitgave | {{< param "ltrversion" >}}.x {{< param "ltrcodename" >}} {{< param "ltrnote" >}} | Uitgave voor **Debian en Ubuntu** | https://qgis.org/debian-ltr https://qgis.org/ubuntu-ltr |
|  |  | Uitgave met afhankelijkheden voor ubuntugis-unstable | https://qgis.org/ubuntugis-ltr |
|  |  | Nachtelijke bouw van de komende puntuitgave voor Debian en Ubuntu | https://qgis.org/debian-nightly-ltr <br> https://qgis.org/ubuntu-nightly-ltr |
|  |  | Nachtelijke bouw van de komende puntuitgave met afhankelijkheden voor ubuntugis-unstable | https://qgis.org/ubuntugis-nightly-ltr |
| Ontwikkelversie | {{< param "devversion" >}} master | Nachtelijke bouw voor **Debian en Ubuntu** [[2]](#id2) | https://qgis.org/debian-nightly <br> https://qgis.org/ubuntu-nightly |
|  |  | Nachtelijke bouw met afhankelijkheden voor ubuntugis-unstable [[2]](#id2) | https://qgis.org/ubuntugis-nightly |

{{< footnote "2" >}} Nachtelijke zijn bouwsels voor debuggen (inclusief de uitvoer voor debuggen)

<small>
Volgende puntuitgave: {{< param "nextpointreleasedate" >}}

Volgende uitgave: {{< param "nextreleasedate" >}}

(Voor meer datums, bekijk het Uitgaveschema op [Road Map]({{< ref "resources/roadmap" >}})) </small>
#### Ondersteunde versies distributie:{#available-codenames }
| Distributie | Versie | Codenaam | Alleen LTR[[1]](#id1) | ubuntugis[[2]](#id2) |
| --- | --- | --- | --- | --- |
| Debian | 12.x (oldstable) | boekenwurm | ja |  |
|  | 13.x (stable) | trixie[[3]](#id3) |  |  |
|  | onstabiel | sid |  |  |
| Ubuntu | 26.04 (LTS) | resolute[[5]](#id5) |  |  |
|  | 25.10 | questing[[4]](#id4) |  |  |
|  | 25.04 | plucky[[3]](#id3) |  |  |
|  | 24.04 (LTS) | noble | ja | ja |
|  | 22.04 (LTS) | jammy | ja | ja |

{{< footnote "1" >}} beschikbare afhankelijkheden in Debian/Ubuntu zijn niet klaar voor QGIS 4 (Qt6 of afhankelijk pakket, Python of SIP voor oude)

{{< footnote "2" >}} bouwsels gebaseerd op afhankelijkheden van Ubuntugis

{{< footnote "3" >}} vanaf 3.40.8/3.44.0

{{< footnote "4" >}} vanaf 3.40.11/3.44.3

{{< footnote "5" >}} vanaf 4.0.1/3.44.9

U moet, om het archief van QGIS te kunnen gebruiken, eerst de publieke sleutel van de opslagplaats voor het archief toevoegen:
```
wget https://download.qgis.org/downloads/qgis-archive-keyring.gpg
gpg --no-default-keyring --keyring ./qgis-archive-keyring.gpg --list-keys
```
Zou uit moeten voeren:
```
./qgis-archive-keyring.gpg
--------------------------
pub   rsa4096 2022-08-08 [SCEA] [expires: 2027-08-08]
      2D7E3441A707FDB3E7059441D155B8E6A419C5BE
uid           [ unknown] QGIS Archive Automatic Signing Key (2022-2027) <qgis-developer@lists.osgeo.org>
```
Nadat u de uitvoer heeft geverifieerd, kunt u de sleutel installeren met:
```
sudo mkdir -m755 -p /etc/apt/keyrings  # not needed since apt version 2.4.0 like Debian 12 and Ubuntu 22 or newer
sudo cp qgis-archive-keyring.gpg /etc/apt/keyrings/qgis-archive-keyring.gpg
```
Als alternatief kunt u de sleutel direct downloaden zonder handmatige verificatie:
```
sudo mkdir -m755 -p /etc/apt/keyrings  # not needed since apt version 2.4.0 like Debian 12 and Ubuntu 22 or newer
sudo wget -O /etc/apt/keyrings/qgis-archive-keyring.gpg https://download.qgis.org/downloads/qgis-archive-keyring.gpg
```
Met de sleutelring op zijn plaats kunt u de repository toevoegen. Maak of open het bestand `/etc/apt/sources.list.d/qgis.sources` (bijv. `sudo editor /etc/apt/sources.list.d/qgis.sources`) om dat te bewerken en voeg de volgende inhoud toe (vervang `*repository*` en `*codename*` door de waarden uit de tabel hierboven):
```
Types: deb deb-src
URIs: *repository*
Suites: *codename*
Architectures: amd64
Components: main
Signed-By: /etc/apt/keyrings/qgis-archive-keyring.gpg
```
Voorbeeld voor de laatste lange termijn uitgave voor Ubuntu 22.04 Jammy:
```
Types: deb deb-src
URIs: https://qgis.org/ubuntu-ltr
Suites: jammy
Architectures: amd64
Components: main
Signed-By: /etc/apt/keyrings/qgis-archive-keyring.gpg
```
Typ daarna onderstaande opdrachten om QGIS te installeren:
```
sudo apt update
sudo apt install qgis qgis-plugin-grass
```
In het geval dat u QGIS Server wilt installeren, typ:
```
sudo apt update
sudo apt install qgis-server --no-install-recommends --no-install-suggests
# if you want to install server Python plugins
apt install python3-qgis
```
{{<rich-box-start icon="💁" layoutClass="tips" >}}

{{<rich-content-start themeClass="coloring-1" >}}
##### Opmerking
Verwijder eerst alle QGIS en GRASS onderdelen die je geïnstalleerd hebt van andere repositories, voordat je begint met de update. 

{{<rich-content-end >}}

{{<rich-box-end >}}
## Flatpak
{{<rich-box-start icon="💡" layoutClass="tips" >}}

{{<rich-content-start themeClass="coloring-1" >}}
##### Opmerking
Flatpak is een universele pakketindeling voor alle distributies van Linux. Pakketten zijn geïsoleerd van het systeem, wat voordelen kan hebben voor beveiliging en stabiliteit. U kunt bijvoorbeeld de laatste versie van QGIS gebruiken op een stabiele distributie.

Flatpaks worden standaard geïnstalleerd voor alle gebruikers, maar kunnen ook voor slechts één enkele gebruiker worden geïnstalleerd met het argument `--user`.

Alleen gebruikers met het recht `sudo` kunnen systeembrede toepassingen voor Flatpak en repositories wijzigen, maar alle gebruikers mogen ze bijwerken. Dat kan nuttig zijn op beheerde machines.

{{<rich-content-end >}}

{{<rich-box-end >}}

Er is een QGIS flatpak voor QGIS Stable en LTR beschikbaar, onderhouden door de gemeenschap van Flathub.

Voor algemene instructies voor het installeren, bekijk [de website van Flathub](https://flatpak.org/setup).

[Hier vindt u QGIS op Flathub](https://flathub.org/apps/details/org.qgis.qgis).

Installeren:
```
flatpak install flathub org.qgis.qgis
```
U zult worden gevraagd naar de versie van QGIS die u wilt gebruiken.

De toepassing zou moeten verschijnen in uw startprogramma, gebruik als alternatief deze opdracht:
```
flatpak run org.qgis.qgis
```
Bijwerken van uw toepassingen van Flatpak, inclusief QGIS:
```
flatpak update
```
Op bepaalde distributies zult u misschien ook pakketten `xdg-desktop-portal`, samen met `xdg-desktop-portal-gtk`, `xdg-desktop-portal-kde` of `xdg-desktop-portal-cosmic` moeten installeren om de dialoogvensters voor bestanden te laten verschijnen.

Bekijk de [bestanden voor Flathub hier](https://github.com/flathub/org.qgis.qgis) en [rapporteer problemen hier](https://github.com/flathub/org.qgis.qgis/issues).
### Runtime-versie weergeven
Als u de volgende aanvullingen nodig hebt, zult u willen weten welke runtime QGIS gebruikt:
```
flatpak info org.qgis.qgis --show-runtime
```
### Ondersteuning extensies
Als u aanvullende modules voor Python moet installeren, omdat ze nodig zijn voor een plug-in, kunt u de module installeren met (hier het installeren van de module `scipy`):
```
flatpak run --devel --command=pip3 org.qgis.qgis install scipy --user

# NOTE: you will likely get an error like: "error: runtime/org.kde.Sdk/x86_64/VERSION not installed" then also do:
flatpak install runtime/org.kde.Sdk/x86_64/VERSION
```
### HTML renderen
Wanneer u HTML wilt gebruiken, bijvoorbeeld in lay-outs voor kaarten, is `QtWebkit` nodig. U kunt het installeren vanuit de interface voor de opdrachtregel van Flatpak
```
flatpak install app/io.qt.qtwebkit.BaseApp/x86_64/VERSION
# ⚠️ WARNING: This is considered insecure and is therefore not provided by default.
```
## Fedora
{{<rich-box-start icon="🙋‍♂️" layoutClass="tips" >}}

{{<rich-content-start themeClass="coloring-1" >}}
##### Opmerking
Het is geen algemene gewoonte om zowel de cliënt als de servertoepassing op dezelfde machine te installeren.

{{<rich-content-end >}}

{{<rich-box-end >}}

Verkrijg de pakketten voor varianten van Fedora met `dnf` door te typen:
```
sudo dnf install qgis python3-qgis qgis-grass qgis-server
```
Als u op **Fedora Atomic Desktops** zit, hebt u 3 opties:
1. Installeer het Flatpak

Flatpak is de aanbevolen manier om pakketten te installeren op Atomic Desktops, [doorgaan naar de instructies](#flatpak).
2. Installeer QGIS op het systeem

Dit is de gemakkelijkste methode, het bespaart gegevens en schijfruimte, maar zal het bijwerken van het systeem ietsje langzamer maken
```
rpm-ostree install qgis python3-qgis qgis-grass qgis-server
```
3. Installeren in een toolbox of distrobox

Volg de `toolbx` en `distrobox` [instructies](#distrobox--toolbx).

Fedora schakelt tussen de huidige uitgave van QGIS en de uitgaven LTR. De onstabiele branch "Rawhide" zal waarschijnlijk nieuwere, maar mogelijk problematische versies van QGIS leveren.
| Distributie | Versie | QGIS-versie |
| --- | --- | --- |
| Fedora | 40 | {{< param "ltrversion" >}}.x {{< param "ltrcodename" >}} {{< param "ltrnote" >}} |
|  | 41 | {{< param "ltrversion" >}}.x {{< param "ltrcodename" >}} {{< param "ltrnote">}} |
|  | 42 | {{< param "version" >}}.x {{< param "codename" >}} {{< param "releasenote">}} |

Altijd up-to-date versie-info:
- [QGIS](https://packages.fedoraproject.org/pkgs/qgis/qgis)
- [QGIS-GRASS](https://packages.fedoraproject.org/pkgs/qgis/qgis-grass)

## NixOS
Laatste stabiele en LTR-pakketten zijn [beschikbaar voor nixpkgs](https://search.nixos.org/packages?channel=unstable&from=0&size=50&sort=relevance&type=packages&query=qgis). U kunt ook de allerlaatste ontwikkelversie uitvoeren met slechts een enkele opdracht.
### Basisinstallatie
**Voor kort gebruik:**
```
nix-shell -p qgis --command qgis
```
of
```
nix-shell -p qgis-ltr  --command qgis
```
**Of toegevoegd aan uw NixOS configuration.nix, zodat het deel van uw systeeminstallatie wordt:**

Voor de LTR:
```  
  environment.systemPackages = [
    pkgs.qgis-ltr
  ];
```
Voor de laatste stabiele:
```
environment.systemPackages = [
    pkgs.qgis
  ];
```
### Uitvoeren van ontwikkelsnapshots - Op afstand
U kunt in-ontwikkeling-versies van QGIS uitvoeren met een enkele opdracht. Direct vanuit GitHub of enige andere GIT-revisie (na 9 juli 2025) vanuit een branch of PR. Nix zal automatisch bouwen en de versie uitvoeren waarnaar u verwijst.

QGIS uitvoeren vanuit de huidige commit of de branch master:
```
nix run github:qgis/QGIS#qgis
```
Een specifieke revisie uitvoeren:
```
nix run github:qgis/QGIS/<git revision>#qgis
```
Een Pull Request of branch uitvoeren:
```
nix run github:qgis/QGIS/<git branch>#qgis
```
### Uitvoeren van ontwikkelsnapshots - Lokaal
Als u een lokale git checkout van QGIS hebt, kunt u de boom van uw lokale broncode uitvoeren:
```
nix run .#qgis
```
U kunt ook een ontwikkelomgeving maken door de volgende opdracht uit te voeren in de bron van de map van uw git-checkout van uw QGIS:
```
nix develop
```
Na het uitvoeren van deze opdracht zult u aanvullende instructies in de terminal zien weergegeven voor het bouwen.
### Uitvoeren met extra pakketten van Python:
Wegens de isolatie van pakketten voor Nix, moet u het pakket overschrijven als u wilt dat extra pakketten voor Python beschikbaar zijn voor QGIS. Bijvoorbeeld: voor het uitvoeren van QGIS met de bibliotheken voor Python numpy, geopandas en rasterio, kunt u doen:

**Voor kort gebruik:**
```
nix-shell -p \
      'qgis.override { extraPythonPackages = (ps: [ ps.numpy ps.future ps.geopandas ps.rasterio ps.debugpy ]);}' \
      --command "qgis"
```
**Of toegevoegd aan uw NixOS configuration.nix, zodat het deel van uw systeeminstallatie wordt:**
```
{
  config,
  pkgs,
  ...
}: {
  environment.systemPackages = with pkgs; [
    (qgis.override {
      extraPythonPackages = ps:
        with ps; [
          numpy
          geopandas
          rasterio
        ];
    })
    # other packages
  ];
}

```
## SUSE / OpenSUSE
Laatste stabiele en LTR-pakketten, genaamd `qgis` en `qgis-ltr`, zijn beschikbaar in de volgende opslagplaatsen:
| Distributie | Opslagplaats |
| --- | --- |
| Tumbleweed | https://download.opensuse.org/repositories/Application:/Geo/openSUSE_Tumbleweed/ |
| Leap 15.2 | https://download.opensuse.org/repositories/Application:/Geo/openSUSE_Leap_15.2/ |
| Leap 15.1 | https://download.opensuse.org/repositories/Application:/Geo/openSUSE_Leap_15.1/ |
| Factory ARM | https://download.opensuse.org/repositories/Application:/Geo/openSUSE_Factory_ARM/ |
| Factory PowerPC | https://download.opensuse.org/repositories/Application:/Geo/openSUSE_Factory_PowerPC/ |
| SLE 15 SP1 Backports | https://download.opensuse.org/repositories/Application:/Geo/SLE_15_SP1_Backports/ |
| SLE 15 SP1 Backports debug | https://download.opensuse.org/repositories/Application:/Geo/SLE_15_SP1_Backports_debug/ |

Alle pakketten bevatten GRASS- en Python-ondersteuning

Alle opslagplaatsen voor openSUSE Geo zijn hier te vinden: https://download.opensuse.org/repositories/Application:/Geo/

Install QGIS with this command:
```
sudo zypper in qgis qgis-plugin-grass 
```
Op OpenSUSE microOS, Kalpa, Aeon en andere other onveranderlijke varianten, bekijk de `distrobox` [instructies](#distrobox--toolbx). Installeren op het basissysteem is mogelijk, maar wordt niet aangeraden.
## Mandriva
### QGIS stable
Huidige:
```
urpmi qgis-python qgis-grass
```
## Slackware
### QGIS stable
Pakketten op https://slackbuilds.org/result/?search=qgis
## Arch Linux
### QGIS stable
QGIS stabiel is beschikbaar in de officiële opslagplaats van Arch Linux: https://archlinux.org/packages/extra/x86_64/qgis/

Installeren met:
```
pacman -S qgis
```
### QGIS LTR
QGIS Long Term Release is beschikbaar in AUR (Arch User Repository).

Installeer met yaourt of een andere pakketbeheerder die AUR ondersteunt:
```
yaourt -S qgis-ltr
```
Voor problemen en ander gedrag, lees de opmerkingen hier : https://aur.archlinux.org/packages/qgis-ltr/
### QGIS testing 
QGIS testing is beschikbaar in AUR (Arch User Repository).

Installeer met yaourt of een andere pakketbeheerder die AUR ondersteunt:
```
yaourt -S qgis-git
```
Voor problemen en ander gedrag, lees de opmerkingen hier : https://aur.archlinux.org/packages/qgis-git
## Spack
Spack is een distro agnostische pakketbeheerder voor Linux, die is ontwikkeld in de context van het werken met computers voor hoge uitvoering.

Algemene informatie voor het installeren van Spack: https://github.com/spack/spack

QGIS pakketbestand op Spack: https://github.com/spack/spack/blob/develop/var/spack/repos/builtin/packages/qgis/package.py

Installeren:
```
spack install qgis
```
dat QGIS en **alle** afhankelijkheden bouwt en installeert vanaf nul. Daarna kan QGIS worden gebruikt via:
```
spack load qgis
```
Als aanvullende pakketten voor Python moeten worden geïnstalleerd, wordt het gebruiken van een omgeving voor Spack aanbevolen. Bijvoorbeeld:
```
spack env create myenv
spack env activate -p myenv
spack add qgis py-lz4
spack install
```
Aan Spack gerelateerde problemen zouden moeten worden gerapporteerd op: https://github.com/spack/spack/issues
## Distrobox & Toolbx
To install QGIS on any Linux system, you can also use `distrobox` or `toolbx`. These allow you to install common distributions like Fedora, OpenSUSE or Ubuntu inside a container. This can be a different version than your main operating system, and thus allows you to have a newer, testing, or more stable version of QGIS.

{{<rich-box-start icon="🙋‍♀️" layoutClass="tips" >}}

{{<rich-content-start themeClass="coloring-1" >}}
##### Opmerking
OpenSUSE en uBlue's op Fedora gebaseerde Systems installeren `distrobox` vooraf, Fedora installeert `toolbx` vooraf op hun "Atomic Desktops". `distrobox` maakt grafische integratie gemakkelijk, voor `toolbx` moet u zelf een desktop-item toevoegen. U kunt alle beschikbare systeemafbeeldingen gebruiken met `distrobox` en `toolbx`, zelfs hoewel `distrobox` meer beschikbare opties weergeeft.

{{<rich-content-end >}}

{{<rich-box-end >}}

Instellen van een distrobox, hier bijvoorbeeld met OpenSUSE Tumbleweed:
```
distrobox-create box -i registry.opensuse.org/opensuse/toolbox:latest

distrobox-enter box
sudo zypper in qgis
distrobox-export --app qgis qgis-plugin-grass
```
QGIS bijwerken in een distrobox:
```
distrobox upgrade --all
```
Een toolbx maken:
```
toolbox create box -i registry.fedoraproject.org/fedora-toolbox:rawhide

toolbox enter box
sudo dnf install qgis qgis-grass python3-qgis
```
QGIS bijwerken in een toolbx:
```
toolbx run -c box sudo dnf update
```
# Mac OS X / macOS
## Binaire pakketten (installatieprogramma's)
Officiële Alles-in-een, getekende en genotariseerde installatieprogramma's voor macOS kunnen worden gedownload van de [downloadpagina van QGIS]({{< ref "download" >}}). Ze zijn compatibel met High Sierra (10.14) en nieuwer voor apparaten met Intel x64 en Apple Silicon (ARM).

Na het downloaden van QGIS, open het bestand DMG. Sleep de toepassing QGIS naar de map Toepassingen en zet het daar neer.
| Uitgave | Versie | Pakket | Alternatief |
| --- | --- | --- | --- |
| Laatste uitgave | {{< param "release" >}} {{< param "codename" >}} | [Installatieprogramma]({{< param "lr_dmg" >}}) [Controlesom]({{< param "lr_dmg_sha" >}}) | [Torrent]({{< param "lr_dmg_torrent" >}}) [Magnet]({{< param "lr_dmg_magnet" >}}) [Metalink]({{< param "lr_dmg_meta4" >}}) |
| Lange Termijn Release | {{< param "ltrrelease" >}} {{< param "ltrcodename" >}} {{< param "ltrnote" >}} | [Installatieprogramma]({{< param "ltr_dmg" >}}) [Controlesom]({{< param "ltr_dmg_sha" >}}) | [Torrent]({{< param "ltr_dmg_torrent" >}}) [Magnet]({{< param "ltr_dmg_magnet" >}}) [Metalink]({{< param "ltr_dmg_meta4" >}}) |

## MacPorts
Het beheerssysteem voor pakketten van [MacPorts](https://www.macports.org) biedt zowel de laatste versie van de uitgave (port `qgis3` als de lange termijn-versie (port `qgis3-ltr`). Dit zal QGIS installeren met zijn eigen architectuur, Intel x64 of Apple Silicon. Van belangrijke afhankelijkheden voor de software, zoals GDAL, PDAL en GRASS GIS zijn gewoonlijk de laatste versies beschikbaar.

[Installeren van MacPorts en het bijwerken ervan](https://guide.macports.org) en de _ports_ worden gemaakt met de _Terminal_. QGIS wordt echter geïnstalleerd als een app-bundel in `/Applications/MacPorts/QGIS3.app`.

Informatie over een port verkrijgen:
```
sudo port info qgis3
```
Installeer de port, bijv. met GRASS GIS:
```
sudo port install qgis3 +grass
```
Bijwerken:
```
sudo port selfupdate
sudo port upgrade outdated
```
{{<rich-box-start icon="👩‍💻" layoutClass="tips" >}}

{{<rich-content-start themeClass="coloring-1" >}}
##### Opmerking
Gelijktijdige installatie van Homebrew en MacPorts is niet compatibel en zal vrijwel zeker leiden tot conflicten. Als u er voor kiest een van de pakketsystemen te installeren, zult u de andere moeten de-installeren.

{{<rich-content-end >}}

{{<rich-box-end >}}
## Oude uitgaven
Eerdere uitgaven van het officiële installatieprogramma kunnen worden gedownload vanaf https://qgis.org/downloads/macos/.

Eerdere uitgaven van het installatieprogramma van kyngchaos kan worden gedownload vanaf https://www.kyngchaos.com/software/archive/qgis/. De oudste installatieprogramma's ondersteunen macOS 10.4 Tiger.
# FreeBSD
## QGIS stable
QGIS installeren vanuit binaire pakketten, typ
```
pkg install qgis
```
Of, om opties voor compileren aan te passen, kunt u het bouwen uit de ports van FreeBSD
```
cd /usr/ports/graphics/qgis
make install clean
```
## QGIS LTR
QGIS installeren vanuit binaire pakketten, typ
```
pkg install qgis-ltr
```
Of, om opties voor compileren aan te passen, kunt u het bouwen uit de ports van FreeBSD
```
cd /usr/ports/graphics/qgis-ltr
make install clean
```
# OpenBSD
QGIS Stable

QGIS installeren vanuit pakketten van derde partijen
```
pkg_add qgis
```
Bekijk:
- https://openbsd.app/?search=qgis for -stable OpenBSD
- https://openbsd.app/?search=qgis&current=on for -current OpenBSD

# Afbeeldingscontainer
Experimenteel (GPU-geaccelereerde) multi-arch JupyterLab QGIS containerafbeeldingen.
- Huidige `os/arch`s: `linux/amd64`, `linux/arm64/v8`
  - Uitvoeren op Apple M-serie met [Docker Desktop](https://www.docker.com/products/docker-desktop/)
  - of gebruik [Podman Desktop](https://podman-desktop.io) (modus rootless).
- Basisafbeeldingen: [Debian](https://hub.docker.com/_/debian) en [Ubuntu](https://hub.docker.com/_/ubuntu)
  - GPU-geaccelereerde afbeeldingen zijn [CUDA](https://hub.docker.com/r/nvidia/cuda)-based (Ubuntu).
- [TurboVNC](https://turbovnc.org): High-speed VNC-versie
  - CUDA-gebaseerde afbeeldingen voeren [VirtualGL](https://virtualgl.org) uit om toepassingen van OpenGL te accelereren.
- Python gewoon – geen [Conda](https://github.com/conda/conda) / [Mamba](https://github.com/mamba-org/mamba)

{{<rich-box-start icon="🧑‍💻" layoutClass="tips" >}}

{{<rich-content-start themeClass="coloring-1" >}}
##### Opmerking
Van de `linux/arm64/v8` JupyterLab QGIS containerafbeeldingen is bekend dat ze willekeurig crashen op Apple M-serie.

GPU-acceleratie vereist een NVIDIA GPU, het NVIDIA Linux stuurprogramma en de NVIDIA Container Toolkit.

{{<rich-content-end >}}

{{<rich-box-end >}}

Voor meer informatie, bekijk <https://github.com/b-data/jupyterlab-qgis-docker-stack>.
## QGIS stable
De container uitvoeren met de laatste stabiele versie van QGIS, opdracht
```shell
docker run -it --rm \
  -p 8888:8888 \
  -v jupyterlab-jovyan:/home/jovyan \
  quay.io/bedata/jupyterlab/qgis/base
```
De GPU-geaccelereerde container uitvoeren met de laatste stabiele versie van QGIS, opdracht
```shell
docker run -it --rm \
  --gpus 'device=all' \
  -p 8888:8888 \
  -v jupyterlab-jovyan:/home/jovyan \
  quay.io/bedata/jupyterlab/cuda/qgis/base
```
## QGIS LTR
De container uitvoeren met de versie LTR van QGIS, opdracht
```shell
docker run -it --rm \
  -p 8888:8888 \
  -v jupyterlab-jovyan:/home/jovyan \
  quay.io/bedata/jupyterlab/qgis/base:ltr
```
De GPU-geaccelereerde container uitvoeren met de versie LTR van QGIS, opdracht
```shell
docker run -it --rm \
  --gpus 'device=all' \
  -p 8888:8888 \
  -v jupyterlab-jovyan:/home/jovyan \
  quay.io/bedata/jupyterlab/cuda/qgis/base:ltr
```
## QGIS-versie
De container uitvoeren met een specifieke versie van QGIS, opdracht
```shell
docker run -it --rm \
  -p 8888:8888 \
  -v jupyterlab-jovyan:/home/jovyan \
  quay.io/bedata/jupyterlab/qgis/base:MAJOR[.MINOR[.PATCH]]
```
{{<rich-box-start icon="🐳" layoutClass="tips" >}}

{{<rich-content-start themeClass="coloring-1" >}}
##### Opmerking
Containerafbeeldingen op Quay zijn beschikbaar voor versies van QGIS ≥ 3.40.4.

Voor QGIS versies 3.28.4 tot en met 3.40.3, gebruik `glcr.b-data.ch/jupyterlab/qgis/base:MAJOR[.MINOR[.PATCH]]`.

{{<rich-content-end >}}

{{<rich-box-end >}}

De GPU-geaccelereerde container uitvoeren met een specifieke versie van QGIS, opdracht
```shell
docker run -it --rm \
  --gpus 'device=all' \
  -p 8888:8888 \
  -v jupyterlab-jovyan:/home/jovyan \
  quay.io/bedata/jupyterlab/cuda/qgis/base:MAJOR[.MINOR[.PATCH]]
```
{{<rich-box-start icon="🔥" layoutClass="tips" >}}

{{<rich-content-start themeClass="coloring-1" >}}
##### Opmerking
GPU-geaccelereerde containerafbeeldingen op Quay zijn beschikbaar voor versies van QGIS ≥ 3.40.4.

Voor QGIS versies 3.34.0 tot en met 3.40.3, gebruik `glcr.b-data.ch/jupyterlab/cuda/qgis/base:MAJOR[.MINOR[.PATCH]]`.

{{<rich-content-end >}}

{{<rich-box-end >}}
# Waarschuwing voor QGIS Testing
{{<rich-box-start icon="⚠️" layoutClass="tips" >}}

{{<rich-content-start themeClass="coloring-6" >}}
##### Waarschuwing
QGIS-testpakketten worden voor sommige platformen in aanvulling op de stabiele versie van QGIS uitgebracht. De testversie van QGIS bevat nog niet vrijgegeven software, waaraan momenteel nog wordt gewerkt. Zij worden daarom niet ondersteund, maar alleen beschikbaar gesteld voor testdoeleinden, om te kijken of bugs zijn opgelost en er geen nieuwe bugs zijn ontstaan. Hoewel we zorgvuldig proberen beschadigingen te voorkomen, zouden deze versies slecht kunnen werken of uw gegevens kunnen beschadigen. Wees voorzichtig! U bent gewaarschuwd!

{{<rich-content-end >}}

{{<rich-box-end >}}
# Installeren vanuit broncode
Bekijk de [de installatienotities van de ontwikkelaars](https://github.com/qgis/QGIS/blob/master/INSTALL.md) over hoe QGIS te bouwen en te installeren vanuit de broncode voor de verschillende platforms die we ondersteunen.

{{<content-end >}}
