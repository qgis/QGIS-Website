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
Standalone installers include everything QGIS needs in a single download. Once you have the installer, no internet is required to complete the installation. When a new release is available, you need to download the complete installer again in order to upgrade. For beginners, the standalone installer is probably the easiest way to install QGIS:
| Uitgave | Versie | Pakket | Alternatief |
| --- | --- | --- | --- |
| Laatste uitgave | {{< param "release" >}} {{< param "codename" >}} {{< param "releasenote" >}} | [Installatieprogramma]({{< param "lr_msi" >}}) [Controlesom]({{< param "lr_sha" >}}) | [Torrent]({{< param "lr_msi_torrent" >}}) [Magnet]({{< param "lr_msi_magnet" >}}) [Metalink]({{< param "lr_msi_meta4" >}}) |
| Lange Termijn Release | {{< param "ltrrelease" >}} {{< param "ltrcodename" >}} {{< param "ltrnote" >}} | [Installer]({{< param "ltr_msi">}}) [Checksum]({{< param "ltr_sha">}}) | [Torrent]({{< param "ltr_msi_torrent" >}}) [Magnet]({{< param "ltr_msi_magnet" >}}) [Metalink]({{< param "ltr_msi_meta4" >}}) |
| Ontwikkeling | {{< param "devversion" >}} master | [Weekly snapshots]({{< param "weekly_msi">}}) | – |

Due to their extensive size the optional projection grids were excluded from the default installer. QGIS will identify at runtime when grids are required for reprojection and ask for manual download.

For environments where that isn't possible or inconvienient there are still standalone installers that include the grids. As of 4.0.1 the regular installer is 0.5 GiB, while the installer including all the grids is 1.2 GiB.
| Uitgave | Versie | Pakket | Alternatief |
| --- | --- | --- | --- |
| Laatste uitgave | {{< param "release" >}} {{< param "codename" >}} {{< param "releasenote" >}} | [Installer]({{< param "lr_grids_msi" >}}) [Checksum]({{< param "lr_grids_sha" >}}) | [Torrent]({{< param "lr_grids_msi_torrent" >}}) [Magnet]({{< param "lr_grids_msi_magnet" >}}) [Metalink]({{< param "lr_grids_msi_meta4" >}}) |
| Lange Termijn Release | {{< param "ltrrelease" >}} {{< param "ltrcodename" >}} {{< param "ltrnote" >}} | [Installer]({{< param "ltr_grids_msi">}}) [Checksum]({{< param "ltr_grids_sha">}}) | [Torrent]({{< param "ltr_grids_msi_torrent" >}}) [Magnet]({{< param "ltr_grids_msi_magnet" >}}) [Metalink]({{< param "ltr_grids_msi_meta4" >}}) |

It's also possible to add the grids later by using the included "OSGeo4W Setup" to install the `proj-data` package. Or to use the also included command line tool [projsync](https://proj.org/en/stable/apps/projsync.html) to download grids for a given area.

The weekly snapshots of the nightly qgis-dev package of OSGeo4W are for users that cannot use OSGeo4W (see below) for some reason or just prefer standalone installers. In the feature freeze phase, these also act as **release candidate** installers.
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
Most linux distributions split QGIS into several packages; you’ll probably need `qgis` and `qgis-python` (to run plugins). Packages like `qgis-grass` (or `qgis-plugin-grass`), `qgis-server` can be installed when you need them.

Below you will find specific instructions per distribution. For most distro’s there are instructions to install QGIS stable and instructions to install a cutting edge QGIS testing build (note the [warning](#warning)).
## Debian / Ubuntu
### Snel starten
{{<rich-box-start icon="💁" layoutClass="tips" >}}

{{<rich-content-start themeClass="coloring-1" >}}
##### Opmerking
In the section following this one, you will find ALL possible options to install different versions of QGIS in different versions of Debian/Ubuntu. If you have problems, verify whether your distribution is still supported as the repositories also contain older **unsupported** distributions with the last QGIS version that was supported. Be aware that those might have meanwhile ceased to work.

{{<rich-content-end >}}

{{<rich-box-end >}}

Simply install the latest stable QGIS ({{< param "version" >}}.x {{< param "codename" >}}) in your Debian or Ubuntu without having to edit config files.

{{<rich-box-start icon="🌀" layoutClass="tips" >}}

{{<rich-content-start themeClass="coloring-1" >}}
##### Opmerking
Although you see ‘Debian’ in some places, this also works for ‘Ubuntu’, as one is actually a symlink to the other on our server.

{{<rich-content-end >}}

{{<rich-box-end >}}

First install some tools you will need for these instructions:
```
sudo apt install gnupg software-properties-common
```
Now install the QGIS Signing Key, so QGIS software from the QGIS repo will be trusted and installed:
```
sudo mkdir -m755 -p /etc/apt/keyrings  # not needed since apt version 2.4.0 like Debian 12 and Ubuntu 22 or newer
sudo wget -O /etc/apt/keyrings/qgis-archive-keyring.gpg https://download.qgis.org/downloads/qgis-archive-keyring.gpg
```
Add the QGIS repo for the latest stable QGIS ({{< param "version" >}}.x {{< param "codename" >}}) to `/etc/apt/sources.list.d/qgis.sources`. Open the file in a text editor (e.g. `sudo editor /etc/apt/sources.list.d/qgis.sources`) and paste the following content (replace `your-distributions-codename` with your actual distribution codename, see [Available codenames](#available-codenames)):
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
`Suites` in above lines depends on your distribution. `lsb_release -cs` will show your distribution name.

In some distributions (like Linux Mint), `. /etc/os-release; echo "$UBUNTU_CODENAME"` will show the correct distibution name.

See [Available codenames](#available-codenames).

{{<rich-content-end >}}

{{<rich-box-end >}}

Save and close the file, then update your repository information:
```
sudo apt update
```
To install QGIS, run:
```
sudo apt install qgis qgis-plugin-grass
```
{{<rich-box-start icon="✍️" layoutClass="tips" >}}

{{<rich-content-start themeClass="coloring-1" >}}
##### Opmerking
Add `qgis-server` to the above line if you also want to install QGIS Server

{{<rich-content-end >}}

{{<rich-box-end >}}
### Repositories
Default Debian and Ubuntu software repositories often contain older versions of QGIS.

To have newer versions, you have to add alternative software repositories, by adding one of the deb-lines below to your `/etc/apt/sources.list.d/qgis.sources` file.

Onze hoofdopslagplaats bevat meerdere regels met pakketten voor verscheidene versies van **Debian en Ubuntu**, gebaseerd op de afhankelijkheden die de afzonderlijke distributies bieden.

For Ubuntu we also used to have extra packages in a separate repository that are based on [ubuntugis](https://launchpad.net/~ubuntugis), which held more up-to-date versions of other GIS packages than Ubuntu itself for LTS versions. If you want those you also need to include ubuntugis-unstable ppa in your /etc/apt/sources.list.d/qgis.list file (see [ubuntugis documentation](https://trac.osgeo.org/ubuntugis/wiki/UbuntuGISRepository)).

{{<rich-box-start icon="💁" layoutClass="tips" mode="html" >}}

{{<rich-content-start themeClass="coloring-1" >}}
##### Opmerking
The release packages are only produced once, shortly after a new version has been released. As unstable, not yet released debian versions (testing) and ubuntugis-unstable can have library changes the packages might sooner or later be broken for these targets, when the development in debian, ubuntu or ubuntugis-unstable moves on and their packages used as dependencies in QGIS change. In that event you can either:
- overgaan naar een stabiele versie van Debian en de daarvoor uitgegeven pakketten gebruiken,
- wait for the next point release (due {{< param "nextpointreleasedate" >}}), which happens every month and will include the updated dependencies,
- overschakelen naar een nightly-opslagplaats (beschikbaar voor de **twee** releasebranches en master) waarvan de pakketten op een regelmatige basis opnieuw worden gebouwd en dan ook automatisch de bijgewerkte afhankelijkheden zullen bevatten of
- build your own set of packages (see [build-debian-packages](https://github.com/qgis/QGIS/blob/master/INSTALL.md#310-building-debian-packages)).

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
| Ontwikkelversie | {{< param "devversion" >}} master | Nightly build for **Debian and Ubuntu** [[2]](#id2) | https://qgis.org/debian-nightly <br> https://qgis.org/ubuntu-nightly |
|  |  | Nightly build with ubuntugis-unstable dependencies [[2]](#id2) | https://qgis.org/ubuntugis-nightly |

{{< footnote "2" >}} Nightlies are debug builds (including debugging output)

<small>
Next point release: {{< param "nextpointreleasedate" >}}

Next release: {{< param "nextreleasedate" >}}

(For more dates see Release Schedule on [Road Map]({{< ref "resources/roadmap" >}})) </small>
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
With the keyring in place you can add the repository. Create or open for editing the file `/etc/apt/sources.list.d/qgis.sources` (e.g. `sudo editor /etc/apt/sources.list.d/qgis.sources`) and add the following content (replace `*repository*` and `*codename*` with values from the table above):
```
Types: deb deb-src
URIs: *repository*
Suites: *codename*
Architectures: amd64
Components: main
Signed-By: /etc/apt/keyrings/qgis-archive-keyring.gpg
```
Example for the latest long term release for Ubuntu 22.04 Jammy:
```
Types: deb deb-src
URIs: https://qgis.org/ubuntu-ltr
Suites: jammy
Architectures: amd64
Components: main
Signed-By: /etc/apt/keyrings/qgis-archive-keyring.gpg
```
After that type the commands below to install QGIS:
```
sudo apt update
sudo apt install qgis qgis-plugin-grass
```
In case you would like to install QGIS Server, type:
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
Flatpak is a universal package format for all Linux distributions. Packages are isolated from the system, which can have security and stability benefits. For example, you can use the latest QGIS version on a stable distribution.

Flatpaks are installed for all users by default, but can also be installed for a single user only with the `--user` argument.

Only users with `sudo` permission can change systemwide Flatpak apps and repositories, but all users can update them. This can be useful on managed machines.

{{<rich-content-end >}}

{{<rich-box-end >}}

There is a Flatpak for QGIS Stable and LTR available, maintained by the Flathub community.

For general install notes, see [the Flathub website](https://flatpak.org/setup).

[Here you can find QGIS on Flathub](https://flathub.org/apps/details/org.qgis.qgis).

To install:
```
flatpak install flathub org.qgis.qgis
```
You will be prompted for the version of QGIS you want to use.

The app should appear in your app launcher, alternatively use this command:
```
flatpak run org.qgis.qgis
```
To update your Flatpak apps, including QGIS:
```
flatpak update
```
On certain distributions, you may also need to install the packages `xdg-desktop-portal`, together with `xdg-desktop-portal-gtk`, `xdg-desktop-portal-kde` or `xdg-desktop-portal-cosmic` in order for file dialogs to appear.

See the [Flathub files here](https://github.com/flathub/org.qgis.qgis) and [report issues here](https://github.com/flathub/org.qgis.qgis/issues).
### Show runtime version
If you need the following additions, you want to know which runtime QGIS is using:
```
flatpak info org.qgis.qgis --show-runtime
```
### Extension support
If you need to install additional Python modules, because they are needed by a plugin, you can install the module with (here installing the `scipy` module):
```
flatpak run --devel --command=pip3 org.qgis.qgis install scipy --user

# NOTE: you will likely get an error like: "error: runtime/org.kde.Sdk/x86_64/VERSION not installed" then also do:
flatpak install runtime/org.kde.Sdk/x86_64/VERSION
```
### HTML rendering
If you want to use HTML, for example in map layouts, `QtWebkit` is needed. You can install it from the flatpak command line interface
```
flatpak install app/io.qt.qtwebkit.BaseApp/x86_64/VERSION
# ⚠️ WARNING: This is considered insecure and is therefore not provided by default.
```
## Fedora
{{<rich-box-start icon="🙋‍♂️" layoutClass="tips" >}}

{{<rich-content-start themeClass="coloring-1" >}}
##### Opmerking
It’s not a common practice to install both client and server applications on the same machine.

{{<rich-content-end >}}

{{<rich-box-end >}}

Get packages for Fedora variants using `dnf` by typing:
```
sudo dnf install qgis python3-qgis qgis-grass qgis-server
```
If you are on **Fedora Atomic Desktops**, you have 3 options:
1. Install the Flatpak

Flatpak is the recommended way to install packages on Fedora Atomic Desktops, [skip to the instructions](#flatpak).
2. Install QGIS to the system

This is the easiest method, saves data and disk space, but will slow down system updates a bit
```
rpm-ostree install qgis python3-qgis qgis-grass qgis-server
```
3. Install in a toolbox or distrobox

Follow the `toolbx` and `distrobox` [instructions](#distrobox--toolbx).

Fedora switches between the current QGIS release and the LTR releases. The unstable "Rawhide" branch will ship newer but possibly buggy QGIS versions.
| Distributie | Versie | QGIS-versie |
| --- | --- | --- |
| Fedora | 40 | {{< param "ltrversion" >}}.x {{< param "ltrcodename" >}} {{< param "ltrnote" >}} |
|  | 41 | {{< param "ltrversion" >}}.x {{< param "ltrcodename" >}} {{< param "ltrnote">}} |
|  | 42 | {{< param "version" >}}.x {{< param "codename" >}} {{< param "releasenote">}} |

Always up-to-date version infos:
- [QGIS](https://packages.fedoraproject.org/pkgs/qgis/qgis)
- [QGIS-GRASS](https://packages.fedoraproject.org/pkgs/qgis/qgis-grass)

## NixOS
Latest stable and LTR packages are [available in nixpkgs](https://search.nixos.org/packages?channel=unstable&from=0&size=50&sort=relevance&type=packages&query=qgis). You can also run bleeding edge developer versions with a single command.
### Basic Install
**Ephemeral use:**
```
nix-shell -p qgis --command qgis
```
of
```
nix-shell -p qgis-ltr  --command qgis
```
**Or added to your NixOS configuration.nix so that it becomes part of your system install:**

For the LTR:
```  
  environment.systemPackages = [
    pkgs.qgis-ltr
  ];
```
For latest stable:
```
environment.systemPackages = [
    pkgs.qgis
  ];
```
### Running developer snapshots - Remote
You can run in-development versions of QGIS with a single command directly from GitHub for any git revision (subsequent to 9 July 2025) from a branch or PR. Nix will automatically build and run the version you reference.

To run QGIS from the current commit of the master branch:
```
nix run github:qgis/QGIS#qgis
```
To run a specific revision:
```
nix run github:qgis/QGIS/<git revision>#qgis
```
To run a Pull Request or branch:
```
nix run github:qgis/QGIS/<git branch>#qgis
```
### Running developer snapshots - Local
If you have a local git checkout of QGIS, you can run your local source code tree:
```
nix run .#qgis
```
You can also create a developer environment by running the following command in the root of your QGIS git checkout directory:
```
nix develop
```
After running this command, you will see additional instructions for building displayed in the terminal.
### Running with extra python packages:
Due to isolation of Nix packages, you need to override the package if you want extra python packages to be available to QGIS. For example to run QGIS with numpy, geopandas and rasterio Python libraries you can do:

**Ephemeral use:**
```
nix-shell -p \
      'qgis.override { extraPythonPackages = (ps: [ ps.numpy ps.future ps.geopandas ps.rasterio ps.debugpy ]);}' \
      --command "qgis"
```
**Or added to your NixOS configuration.nix so that it becomes part of your system install:**
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
Latest stable and LTR packages called `qgis` and `qgis-ltr` are available in the following repositories:
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

Install QGis with this command:
```
sudo zypper in qgis qgis-plugin-grass 
```
On OpenSUSE microOS, Kalpa, Aeon and other immutable variants, refer to the `distrobox` [instructions](#distrobox--toolbx). Installing on the base system is possible but not recommended.
## Mandriva
### QGIS stable
Current:
```
urpmi qgis-python qgis-grass
```
## Slackware
### QGIS stable
Pakketten op https://slackbuilds.org/result/?search=qgis
## Arch Linux
### QGIS stable
QGIS stable is available in Arch Linux official repository : https://archlinux.org/packages/extra/x86_64/qgis/

Install with:
```
pacman -S qgis
```
### QGIS LTR
QGIS Long Term Release is beschikbaar in AUR (Arch User Repository).

Install with yaourt or other package manager which supports AUR:
```
yaourt -S qgis-ltr
```
Voor problemen en ander gedrag, lees de opmerkingen hier : https://aur.archlinux.org/packages/qgis-ltr/
### QGIS testing 
QGIS testing is beschikbaar in AUR (Arch User Repository).

Install with yaourt or other package manager which supports AUR:
```
yaourt -S qgis-git
```
Voor problemen en ander gedrag, lees de opmerkingen hier : https://aur.archlinux.org/packages/qgis-git
## Spack
Spack is een distro agnostische pakketbeheerder voor Linux, die is ontwikkeld in de context van het werken met computers voor hoge uitvoering.

Algemene informatie voor het installeren van Spack: https://github.com/spack/spack

QGIS pakketbestand op Spack: https://github.com/spack/spack/blob/develop/var/spack/repos/builtin/packages/qgis/package.py

To install:
```
spack install qgis
```
which builds and installs QGIS and **all** dependencies from scratch. Afterwards, QGIS can be used via:
```
spack load qgis
```
If additional python packages need to be installed, using a Spack environment is recommended. For example:
```
spack env create myenv
spack env activate -p myenv
spack add qgis py-lz4
spack install
```
Aan Spack gerelateerde problemen zouden moeten worden gerapporteerd op: https://github.com/spack/spack/issues
## Distrobox & Toolbx
To install QGis on any Linux system, you can also use `distrobox` or `toolbx`. These allow you to install common distributions like Fedora, OpenSUSE or Ubuntu inside a container. This can be a different version than your main operating system, and thus allows you to have a newer, testing, or more stable version of QGIS.

{{<rich-box-start icon="🙋‍♀️" layoutClass="tips" >}}

{{<rich-content-start themeClass="coloring-1" >}}
##### Opmerking
OpenSUSE and uBlue's Fedora-based Systems preinstall `distrobox`, Fedora preinstalls `toolbx` on their "Atomic Desktops". `distrobox` allows easy graphical integration, for `toolbx` you need to add a desktop entry yourself. You can use all available system images with `distrobox` and `toolbx`, even though `distrobox` displays more available options.

{{<rich-content-end >}}

{{<rich-box-end >}}

To setup a distrobox, here for example using OpenSUSE Tumbleweed:
```
distrobox-create box -i registry.opensuse.org/opensuse/toolbox:latest

distrobox-enter box
sudo zypper in qgis
distrobox-export --app qgis qgis-plugin-grass
```
Update QGIS in a distrobox:
```
distrobox upgrade --all
```
To create a toolbx:
```
toolbox create box -i registry.fedoraproject.org/fedora-toolbox:rawhide

toolbox enter box
sudo dnf install qgis qgis-grass python3-qgis
```
Update QGIS in a toolbx:
```
toolbx run -c box sudo dnf update
```
# Mac OS X / macOS
## Binaire pakketten (installatieprogramma's)
Official All-in-one, signed and notarized installers for macOS can be downloaded from the [QGIS download page]({{< ref "download" >}}). They are compatible with High Sierra (10.14) and newer for Intel x64 and Apple silicon (ARM) devices.

After downloading QGIS, open the DMG file. Drag and drop the QGIS application into the Applications folder.
| Uitgave | Versie | Pakket | Alternatief |
| --- | --- | --- | --- |
| Laatste uitgave | {{< param "release" >}} {{< param "codename" >}} | [Installer]({{< param "lr_dmg" >}}) [Checksum]({{< param "lr_dmg_sha" >}}) | [Torrent]({{< param "lr_dmg_torrent" >}}) [Magnet]({{< param "lr_dmg_magnet" >}}) [Metalink]({{< param "lr_dmg_meta4" >}}) |
| Lange Termijn Release | {{< param "ltrrelease" >}} {{< param "ltrcodename" >}} {{< param "ltrnote" >}} | [Installer]({{< param "ltr_dmg" >}}) [Checksum]({{< param "ltr_dmg_sha" >}}) | [Torrent]({{< param "ltr_dmg_torrent" >}}) [Magnet]({{< param "ltr_dmg_magnet" >}}) [Metalink]({{< param "ltr_dmg_meta4" >}}) |

## MacPorts
The package management system [MacPorts](https://www.macports.org) offers both the latest release version (port `qgis3`) and the long term version (port `qgis3-ltr`). This will install QGIS with native architecture, Intel x64 or Apple silicon. Main software dependencies such as GDAL, PDAL and GRASS GIS are usually the latest version available.

[Installing MacPorts and updating](https://guide.macports.org) it and the _ports_ are made with the _Terminal_. QGIS is however installed as an app bundle at `/Applications/MacPorts/QGIS3.app`.

Get information of a port:
```
sudo port info qgis3
```
Install port, e.g with GRASS GIS:
```
sudo port install qgis3 +grass
```
Update:
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
To install QGIS from binary packages type
```
pkg install qgis
```
Or to customize compilation options, you can build it from FreeBSD ports
```
cd /usr/ports/graphics/qgis
make install clean
```
## QGIS LTR
To install QGIS from binary packages type
```
pkg install qgis-ltr
```
Or to customize compilation options, you can build it from FreeBSD ports
```
cd /usr/ports/graphics/qgis-ltr
make install clean
```
# OpenBSD
QGIS Stable

To install QGIS from third-party package
```
pkg_add qgis
```
See:
- https://openbsd.app/?search=qgis for -stable OpenBSD
- https://openbsd.app/?search=qgis&current=on for -current OpenBSD

# Afbeeldingscontainer
Experimental (GPU accelerated) multi-arch JupyterLab QGIS container images.
- Current `os/arch`s: `linux/amd64`, `linux/arm64/v8`
  - Run on Apple M series using [Docker Desktop](https://www.docker.com/products/docker-desktop/)
  - or using [Podman Desktop](https://podman-desktop.io) (rootless mode).
- Base images: [Debian](https://hub.docker.com/_/debian) and [Ubuntu](https://hub.docker.com/_/ubuntu)
  - GPU accelerated images are [CUDA](https://hub.docker.com/r/nvidia/cuda)-based (Ubuntu).
- [TurboVNC](https://turbovnc.org): High-speed VNC version
  - CUDA-based images run [VirtualGL](https://virtualgl.org) to accelerate OpenGL applications.
- Just Python – no [Conda](https://github.com/conda/conda) / [Mamba](https://github.com/mamba-org/mamba)

{{<rich-box-start icon="🧑‍💻" layoutClass="tips" >}}

{{<rich-content-start themeClass="coloring-1" >}}
##### Opmerking
The `linux/arm64/v8` JupyterLab QGIS container images are known to crash randomly on Apple M series.

GPU acceleration requires an NVIDIA GPU, the NVIDIA Linux driver and the NVIDIA Container Toolkit.

{{<rich-content-end >}}

{{<rich-box-end >}}

For further information, see <https://github.com/b-data/jupyterlab-qgis-docker-stack>.
## QGIS stable
To run the container with the latest QGIS stable version, command
```shell
docker run -it --rm \
  -p 8888:8888 \
  -v jupyterlab-jovyan:/home/jovyan \
  quay.io/bedata/jupyterlab/qgis/base
```
To run the GPU accelerated container with the latest QGIS stable version, command
```shell
docker run -it --rm \
  --gpus 'device=all' \
  -p 8888:8888 \
  -v jupyterlab-jovyan:/home/jovyan \
  quay.io/bedata/jupyterlab/cuda/qgis/base
```
## QGIS LTR
To run the container with the latest QGIS LTR version, command
```shell
docker run -it --rm \
  -p 8888:8888 \
  -v jupyterlab-jovyan:/home/jovyan \
  quay.io/bedata/jupyterlab/qgis/base:ltr
```
To run the GPU accelerated container with the latest QGIS LTR version, command
```shell
docker run -it --rm \
  --gpus 'device=all' \
  -p 8888:8888 \
  -v jupyterlab-jovyan:/home/jovyan \
  quay.io/bedata/jupyterlab/cuda/qgis/base:ltr
```
## QGIS-versie
To run a container with a specific QGIS version, command
```shell
docker run -it --rm \
  -p 8888:8888 \
  -v jupyterlab-jovyan:/home/jovyan \
  quay.io/bedata/jupyterlab/qgis/base:MAJOR[.MINOR[.PATCH]]
```
{{<rich-box-start icon="🐳" layoutClass="tips" >}}

{{<rich-content-start themeClass="coloring-1" >}}
##### Opmerking
Container images on Quay are available for QGIS versions ≥ 3.40.4.

For QGIS versions 3.28.4 to 3.40.3 use `glcr.b-data.ch/jupyterlab/qgis/base:MAJOR[.MINOR[.PATCH]]`.

{{<rich-content-end >}}

{{<rich-box-end >}}

To run a GPU accelerated container with a specific QGIS version, command
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
GPU accelerated container images on Quay are available for QGIS versions ≥ 3.40.4.

For QGIS versions 3.34.0 to 3.40.3 use `glcr.b-data.ch/jupyterlab/cuda/qgis/base:MAJOR[.MINOR[.PATCH]]`.

{{<rich-content-end >}}

{{<rich-box-end >}}
# Waarschuwing voor QGIS Testing
{{<rich-box-start icon="⚠️" layoutClass="tips" >}}

{{<rich-content-start themeClass="coloring-6" >}}
##### Waarschuwing
QGIS testing packages are provided for some platforms in addition to the QGIS stable version. QGIS testing contains unreleased software that is currently being worked on. They are only provided for testing purposes to early adopters to check if bugs have been resolved and that no new bugs have been introduced. Although we carefully try to avoid breakages, it may at any given time not work, or may do bad things to your data. Take care. You have been warned!

{{<rich-content-end >}}

{{<rich-box-end >}}
# Installeren vanuit broncode
Please refer to [the developer installation notes](https://github.com/qgis/QGIS/blob/master/INSTALL.md) for notes on how to build and install QGIS from source for the different platforms we support.

{{<content-end >}}
