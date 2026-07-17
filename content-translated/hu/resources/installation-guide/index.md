---
Reviewed: 4 June 2024
Reviewer: Tim Sutton
draft: false
sidebar: true
subtitle: ''
title: Telepítési útmutató
type: page

---
{{<content-start >}}
# QGIS telepítők
A QGIS elérhető Windows, macOS, Linux, FreeBSD, OpenBSD, Android és iOS rendszerekre.

![Operációs rendszerek ikonjai](img/icons.png)

Javasoljuk a hosszútávú kiadású (LTR) csomagok telepítését, mivel az LTR-verzióinkat a kiadás előtt szigorúbb tesztelésnek vetjük alá, és legalább egy évig kapnak hibajavító frissítéseket.

Lásd még [a telepítők főoldalát]({{< ref "download" >}}).

A következő kiadás kipróbálásához tesztcsomagokat kínálunk, ez lehetővé teszi, hogy a felhasználók is hozzájáruljanak a fejlesztéshez (olvassa el a [figyelmeztetést](#warning)).

A kiadás előtti, befagyasztási fázisban (lásd [Kiadási ütemterv]({{< ref "roadmap#release-schedule" >}})) ezek a csomagok gyakorlatilag **előzetes kiadásoknak minősülnek, amelyeket a felhasználóknak feltétlenül javasolunk tesztelni**.
# Windows
A Windows-ra történő telepítéshez két lehetőség áll rendelkezésre:
## Offline (önálló) telepítők
Az önálló telepítőprogramok egyetlen letöltésben tartalmazzák mindazt, amire a QGIS-nek szüksége van. A telepítőprogram letöltése után a telepítés befejezéséhez nincs szükség internetkapcsolatra. Ha új verzió jelenik meg, a frissítéshez újra le kell tölteni a teljes telepítőprogramot. A kezdők számára az önálló telepítőprogram valószínűleg a legegyszerűbb módja a QGIS telepítésének:
| Kiadás | Verzió | Csomag | Alternatíva |
| --- | --- | --- | --- |
| Legutóbbi kiadás | {{< param "release" >}} {{< param "codename" >}} {{< param "releasenote" >}} | [Telepítő]({{< param "lr_msi" >}}) [Ellenőrzőösszeg]({{< param "lr_sha" >}}) | [Torrent]({{< param "lr_msi_torrent" >}}) [Magnet]({{< param "lr_msi_magnet" >}}) [Metalink]({{< param "lr_msi_meta4" >}}) |
| Hosszútávú kiadás | {{< param "ltrrelease" >}} {{< param "ltrcodename" >}} {{< param "ltrnote" >}} | [Telepítő]({{< param "ltr_msi">}}) [Ellenőrzőösszeg]({{< param "ltr_sha">}}) | [Torrent]({{< param "ltr_msi_torrent" >}}) [Magnet]({{< param "ltr_msi_magnet" >}}) [Metalink]({{< param "ltr_msi_meta4" >}}) |
| Fejlesztői verzió | {{< param "devversion" >}} master | [Heti pillanatképek]({{< param "weekly_msi">}}) | – |

Az opcionális vetületrácsok nagy mérete miatt azok nem kerültek be az alapértelmezett telepítőcsomagba. A QGIS futás közben felismeri, ha a vetületátalakításhoz rácsokra van szükség, és kéri azok kézi letöltését.

Azokban a környezetekben, ahol ez nem lehetséges vagy kényelmetlen, továbbra is rendelkezésre állnak olyan önálló telepítőprogramok, amelyek tartalmazzák a rácsokat. A 4.0.1-es verziótól kezdve a szokásos telepítőprogram mérete 0,5 GiB, míg az összes rácsot tartalmazó telepítőprogramé 1,2 GiB.
| Kiadás | Verzió | Csomag | Alternatíva |
| --- | --- | --- | --- |
| Legutóbbi kiadás | {{< param "release" >}} {{< param "codename" >}} {{< param "releasenote" >}} | [Telepítő]({{< param "lr_grids_msi" >}}) [Ellenőrzőösszeg]({{< param "lr_grids_sha" >}}) | [Torrent]({{< param "lr_grids_msi_torrent" >}}) [Magnet]({{< param "lr_grids_msi_magnet" >}}) [Metalink]({{< param "lr_grids_msi_meta4" >}}) |
| Hosszútávú kiadás | {{< param "ltrrelease" >}} {{< param "ltrcodename" >}} {{< param "ltrnote" >}} | [Telepítő]({{< param "ltr_grids_msi">}}) [Ellenőrzőösszeg]({{< param "ltr_grids_sha">}}) | [Torrent]({{< param "ltr_grids_msi_torrent" >}}) [Magnet]({{< param "ltr_grids_msi_magnet" >}}) [Metalink]({{< param "ltr_grids_msi_meta4" >}}) |

A rácsokat később is hozzá lehet adni a mellékelt „OSGeo4W Setup” segítségével, amellyel telepíthető a `proj-data` csomag. Vagy a szintén mellékelt [projsync](https://proj.org/en/stable/apps/projsync.html) parancssori eszközzel letölthetők a rácsok egy adott területre.

Az OSGeo4W qgis-dev nigthly csomagok heti pillanatképei azoknak a felhasználóknak szólnak, akik valamilyen okból nem tudják használni az OSGeo4W-t (lásd lent), vagy csak az önálló telepítőket részesítik előnyben. A funkcióbefagyási időszakban ezek egyben **kiadásra jelölt** telepítőként is működnek.
## Online (OSGeo4W) telepítő
A haladóbb QGIS-felhasználóknak az OSGeo4W-csomagokat ajánljuk. Ez a telepítő lehetővé teszi a QGIS több verziójának párhuzamos telepítését, valamint a frissítések sokkal hatékonyabb elvégzését, mivel minden új kiadáskor csak a megváltozott összetevőket tölti le és telepíti a rendszer.

Az OSGeo4W tárház sok szoftvert tartalmaz az OSGeo projektek közül. A QGIS-t és az összes függőségeket tartalmazza a Python, GRASS, GDAL, stb. mellett. A telepítő az internetről képes telepíteni vagy előzetesen letölthetjük az összes szükséges csomagot. A letöltött fájlok egy helyi könyvtárba kerülnek a későbbi telepítéshez, de offline telepítésre is használhatók.

A telepítés lépései a következők:
- Töltse le az [OSGeo4W telepítőt](https://download.osgeo.org/osgeo4w/v2/osgeo4w-setup.exe) és indítsa el.
- Válassza az _Express Install_ lehetőséget, majd válassza ki a _QGIS_-t a _legújabb kiadás_ telepítéséhez, illetve a _QGIS LTR_-t a _hosszú távú kiadás_ telepítéséhez.

Alternatív megoldásként az _Express_ telepítés helyett használhatja az _Advanced Install_ lehetőséget is: az _Asztalról_ válasszon ki egy vagy több csomagot a következők közül:
| Kiadás | Verzió | Csomag | Leírás |
| --- | --- | --- | --- |
| Legutóbbi kiadás | {{< param "release" >}} {{< param "codename" >}} {{< param "releasenote" >}} | qgis | Kiadás |
|  |  | qgis-rel-dev [[1]](#id1) | A következő karbantartási kiadás nightly összeállítása |
| Hosszútávú kiadás | {{< param "ltrrelease" >}} {{< param "ltrcodename" >}} {{< param "ltrnote" >}} | qgis-ltr | Kiadás |
|  |  | qgis-ltr-dev [[1]](#id1) | A következő hosszútávú karbantartási kiadás nightly összeállítása (Qt5) |
| Fejlesztői verzió | {{< param "devversion" >}} master | qgis-dev [[1]](#id1) | A fejlesztői változat nightly összeállítása[[2]](#id2) |

{{< footnote "1" >}} Nightlies are debug builds (including debugging output that can be used by developers to better understand issues with the build).

{{< footnote "2" >}} 4.0 marks the switch to Qt6. Earlier versions of QGIS were experimental with Qt6. Starting with 4.0 only Qt6 is supported.

The packages listed in the above table only install the necessary dependencies needed to run QGIS. Corresponding to those packages there are also meta packages with the suffix `-full-free` and `-full`. The `-full-free` contains additional optional dependencies that some popular (not included in the default QGIS install) plugins use. The `-full` includes everything from `-full-free` and also adds proprietary extensions like Oracle drivers, ECW and MrSID.

The Express installs reference the corresponding `-full` variant and the standalone installers are also made from these OSGeo4W package sets.

The `-full-grids` variants include the optional projection grids (ie. `-full` plus the `proj-data` package). The huge standalones are based on these.

Before installing any of the nightly builds note the [warnings](#warning) below.
# Linux
Most linux distributions split QGIS into several packages; you’ll probably need `qgis` and `qgis-python` (to run plugins). Packages like `qgis-grass` (or `qgis-plugin-grass`), `qgis-server` can be installed when you need them.

Below you will find specific instructions per distribution. For most distro’s there are instructions to install QGIS stable and instructions to install a cutting edge QGIS testing build (note the [warning](#warning)).
## Debian / Ubuntu
### Rövid útmutató
{{<rich-box-start icon="💁" layoutClass="tips" >}}

{{<rich-content-start themeClass="coloring-1" >}}
##### Note
In the section following this one, you will find ALL possible options to install different versions of QGIS in different versions of Debian/Ubuntu. If you have problems, verify whether your distribution is still supported as the repositories also contain older **unsupported** distributions with the last QGIS version that was supported. Be aware that those might have meanwhile ceased to work.

{{<rich-content-end >}}

{{<rich-box-end >}}

Simply install the latest stable QGIS ({{< param "version" >}}.x {{< param "codename" >}}) in your Debian or Ubuntu without having to edit config files.

{{<rich-box-start icon="🌀" layoutClass="tips" >}}

{{<rich-content-start themeClass="coloring-1" >}}
##### Note
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
##### Note
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
##### Note
Add `qgis-server` to the above line if you also want to install QGIS Server

{{<rich-content-end >}}

{{<rich-box-end >}}
### Tárolók
Default Debian and Ubuntu software repositories often contain older versions of QGIS.

To have newer versions, you have to add alternative software repositories, by adding one of the deb-lines below to your `/etc/apt/sources.list.d/qgis.sources` file.

Fő tárolónk több csomagot tartalmaz számos **Debian és Ubuntu** verzióhoz, figyelembe véve az egyes disztribúciók által biztosított függőségeket.

For Ubuntu we also used to have extra packages in a separate repository that are based on [ubuntugis](https://launchpad.net/~ubuntugis), which held more up-to-date versions of other GIS packages than Ubuntu itself for LTS versions. If you want those you also need to include ubuntugis-unstable ppa in your /etc/apt/sources.list.d/qgis.list file (see [ubuntugis documentation](https://trac.osgeo.org/ubuntugis/wiki/UbuntuGISRepository)).

{{<rich-box-start icon="💁" layoutClass="tips" mode="html" >}}

{{<rich-content-start themeClass="coloring-1" >}}
##### Note
The release packages are only produced once, shortly after a new version has been released. As unstable, not yet released debian versions (testing) and ubuntugis-unstable can have library changes the packages might sooner or later be broken for these targets, when the development in debian, ubuntu or ubuntugis-unstable moves on and their packages used as dependencies in QGIS change. In that event you can either:
- áttér a stabil debian verzóra, és az erre a célra kiadott csomagokat használja,
- wait for the next point release (due {{< param "nextpointreleasedate" >}}), which happens every month and will include the updated dependencies,
- áttér a nightly verzió tárolójára (elérhető **mindkét** kiadási ágra és a mester fejlesztési ágra), amelynek csomagjaiból rendszeres időközönként új készül, és automatikusan telepíti a frissített függőségeket is, vagy
- build your own set of packages (see [build-debian-packages](https://github.com/qgis/QGIS/blob/master/INSTALL.md#310-building-debian-packages)).

{{<rich-content-end >}}

{{<rich-box-end >}}

Csomagok:
| Kiadás | Verzió | Leírás | Tároló |
| --- | --- | --- | --- |
| Legutóbbi kiadás | {{< param "version" >}}.x {{< param "codename" >}} {{< param "releasenote">}} | Kiadások **Debianhoz és Ubuntuhoz** | https://qgis.org/debian <br> https://qgis.org/ubuntu |
|  |  | Kiadás ubuntugis-unstable függőségekkel | https://qgis.org/ubuntugis |
|  |  | A következő kiadás nightly buildje Debianhoz és Ubuntuhoz | https://qgis.org/debian-nightly-release <br> https://qgis.org/ubuntu-nightly-release |
|  |  | A következő kiadás nightly build-je az ubuntugis-unstable függőségekkel | https://qgis.org/ubuntugis-nightly-release |
| Hosszútávon támogatott kiadás tárolója | {{< param "ltrversion" >}}.x {{< param "ltrcodename" >}} {{< param "ltrnote" >}} | Kiadások **Debianhoz és Ubuntuhoz** | https://qgis.org/debian-ltr https://qgis.org/ubuntu-ltr |
|  |  | Kiadás ubuntugis-unstable függőségekkel | https://qgis.org/ubuntugis-ltr |
|  |  | A következő kiadás nightly buildje Debianhoz és Ubuntuhoz | https://qgis.org/debian-nightly-ltr <br> https://qgis.org/ubuntu-nightly-ltr |
|  |  | A következő kiadás nightly build-je az ubuntugis-unstable függőségekkel | https://qgis.org/ubuntugis-nightly-ltr |
| Fejlesztői változat | {{< param "devversion" >}} master | Nightly build for **Debian and Ubuntu** [[2]](#id2) | https://qgis.org/debian-nightly <br> https://qgis.org/ubuntu-nightly |
|  |  | Nightly build with ubuntugis-unstable dependencies [[2]](#id2) | https://qgis.org/ubuntugis-nightly |

{{< footnote "2" >}} Nightlies are debug builds (including debugging output)

<small>
Next point release: {{< param "nextpointreleasedate" >}}

Next release: {{< param "nextreleasedate" >}}

(For more dates see Release Schedule on [Road Map]({{< ref "resources/roadmap" >}})) </small>
#### Támogatott disztribúciók és verziók:{#available-codenames }
| Disztribúció | Verzió | Kódnév | Only LTR[[1]](#id1) | ubuntugis[[2]](#id2) |
| --- | --- | --- | --- | --- |
| Debian | 12.x (oldstable) | bookworm | igen |  |
|  | 13.x (stable) | trixie[[3]](#id3) |  |  |
|  | nem stabil | sid |  |  |
| Ubuntu | 26.04 (LTS) | resolute[[5]](#id5) |  |  |
|  | 25.10 | questing[[4]](#id4) |  |  |
|  | 25.04 | plucky[[3]](#id3) |  |  |
|  | 24.04 (LTS) | noble | igen | igen |
|  | 22.04 (LTS) | jammy | igen | igen |

{{< footnote "1" >}} available dependencies in debian/ubuntu not QGIS 4 ready (Qt6 or dependant package, python or sip to old)

{{< footnote "2" >}} builds based on ubuntugis dependencies

{{< footnote "3" >}} starting with 3.40.8/3.44.0

{{< footnote "4" >}} starting with 3.40.11/3.44.3

{{< footnote "5" >}} starting with 4.0.1/3.44.9

To use the QGIS archive you have to first add the archive’s repository public key:
```
wget https://download.qgis.org/downloads/qgis-archive-keyring.gpg
gpg --no-default-keyring --keyring ./qgis-archive-keyring.gpg --list-keys
```
Should output:
```
./qgis-archive-keyring.gpg
--------------------------
pub   rsa4096 2022-08-08 [SCEA] [expires: 2027-08-08]
      2D7E3441A707FDB3E7059441D155B8E6A419C5BE
uid           [ unknown] QGIS Archive Automatic Signing Key (2022-2027) <qgis-developer@lists.osgeo.org>
```
After you have verified the output you can install the key with:
```
sudo mkdir -m755 -p /etc/apt/keyrings  # not needed since apt version 2.4.0 like Debian 12 and Ubuntu 22 or newer
sudo cp qgis-archive-keyring.gpg /etc/apt/keyrings/qgis-archive-keyring.gpg
```
Alternatively you can download the key directly without manual verification:
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
##### Note
Kérjük távolítsa el a frissítés előtt az összes QGIS és GRASS csomagot, melyet más tárolókból telepített.

{{<rich-content-end >}}

{{<rich-box-end >}}
## Flatpak
{{<rich-box-start icon="💡" layoutClass="tips" >}}

{{<rich-content-start themeClass="coloring-1" >}}
##### Note
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
##### Note
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
| Disztribúció | Verzió | QGIS-verzió |
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
vagy
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
| Disztribúció | Tároló |
| --- | --- |
| Tumbleweed | https://download.opensuse.org/repositories/Application:/Geo/openSUSE_Tumbleweed/ |
| Leap 15.2 | https://download.opensuse.org/repositories/Application:/Geo/openSUSE_Leap_15.2/ |
| Leap 15.1 | https://download.opensuse.org/repositories/Application:/Geo/openSUSE_Leap_15.1/ |
| Factory ARM | https://download.opensuse.org/repositories/Application:/Geo/openSUSE_Factory_ARM/ |
| Factory PowerPC | https://download.opensuse.org/repositories/Application:/Geo/openSUSE_Factory_PowerPC/ |
| SLE 15 SP1 Backports | https://download.opensuse.org/repositories/Application:/Geo/SLE_15_SP1_Backports/ |
| SLE 15 SP1 Backports debug | https://download.opensuse.org/repositories/Application:/Geo/SLE_15_SP1_Backports_debug/ |

Minden csomag tartalmazza a GRASS és Python támogatást

Az összes openSUSE Geo tároló megtalálható itt: https://download.opensuse.org/repositories/Application:/Geo/

Install QGIS with this command:
```
sudo zypper in qgis qgis-plugin-grass 
```
On OpenSUSE microOS, Kalpa, Aeon and other immutable variants, refer to the `distrobox` [instructions](#distrobox--toolbx). Installing on the base system is possible but not recommended.
## Mandriva
### Stabil QGIS
Current:
```
urpmi qgis-python qgis-grass
```
## Slackware
### Stabil QGIS
Csomagok itt: https://slackbuilds.org/result/?search=qgis
## Arch Linux
### Stabil QGIS
QGIS stable is available in Arch Linux official repository : https://archlinux.org/packages/extra/x86_64/qgis/

Install with:
```
pacman -S qgis
```
### QGIS LTR
A QGIS Hosszútávú kiadás elérhető AUR-ból (Arch User Repository).

Install with yaourt or other package manager which supports AUR:
```
yaourt -S qgis-ltr
```
A hibákkal és egyéb problémákkal kapcsolatban olvassa el a hozzászólásokat itt: https://aur.archlinux.org/packages/qgis-ltr/
### QGIS testing
A QGIS testing elérhető AUR-ból (Arch User Repository).

Install with yaourt or other package manager which supports AUR:
```
yaourt -S qgis-git
```
A hibákkal és egyéb problémákkal kapcsolatban olvassa el a hozzászólásokat itt: https://aur.archlinux.org/packages/qgis-git
## Spack
Spack is a distro agnostic package manager for Linux, which is developed in the context of high-performance computing.

General info on installing Spack: https://github.com/spack/spack

QGIS package info on the Spack website: https://packages.spack.io/package.html?name=qgis

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
Spack related issues should be reported at: https://github.com/spack/spack/issues
## Distrobox & Toolbx
To install QGIS on any Linux system, you can also use `distrobox` or `toolbx`. These allow you to install common distributions like Fedora, OpenSUSE or Ubuntu inside a container. This can be a different version than your main operating system, and thus allows you to have a newer, testing, or more stable version of QGIS.

{{<rich-box-start icon="🙋‍♀️" layoutClass="tips" >}}

{{<rich-content-start themeClass="coloring-1" >}}
##### Note
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
## Bináris csomagok (telepítők)
Official All-in-one, signed and notarized installers for macOS can be downloaded from the [QGIS download page]({{< ref "download" >}}). They are compatible with High Sierra (10.14) and newer for Intel x64 and Apple silicon (ARM) devices.

After downloading QGIS, open the DMG file. Drag and drop the QGIS application into the Applications folder.
| Kiadás | Verzió | Csomag | Alternatíva |
| --- | --- | --- | --- |
| Legutóbbi kiadás | {{< param "release" >}} {{< param "codename" >}} | [Installer]({{< param "lr_dmg" >}}) [Checksum]({{< param "lr_dmg_sha" >}}) | [Torrent]({{< param "lr_dmg_torrent" >}}) [Magnet]({{< param "lr_dmg_magnet" >}}) [Metalink]({{< param "lr_dmg_meta4" >}}) |
| Hosszútávú kiadás | {{< param "ltrrelease" >}} {{< param "ltrcodename" >}} {{< param "ltrnote" >}} | [Installer]({{< param "ltr_dmg" >}}) [Checksum]({{< param "ltr_dmg_sha" >}}) | [Torrent]({{< param "ltr_dmg_torrent" >}}) [Magnet]({{< param "ltr_dmg_magnet" >}}) [Metalink]({{< param "ltr_dmg_meta4" >}}) |

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
##### Note
Concurrent installation of Homebrew and MacPorts is not compatible and will almost certainly lead to conflicts. If you choose to install one of the package systems you need to uninstall the other.

{{<rich-content-end >}}

{{<rich-box-end >}}
## Régi kiadások
A hivatalos telepítő korábbi kiadásai letölthetők a https://qgis.org/downloads/macos/ címről.

A kyngchaos telepítők korábbi kiadásai letölthetők a https://www.kyngchaos.com/software/archive/qgis/ webhelyről. A legrégebbi telepítők a macOS 10.4 Tigert támogatják.
# FreeBSD
## Stabil QGIS
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

# Konténer-rendszerképek
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
##### Note
The `linux/arm64/v8` JupyterLab QGIS container images are known to crash randomly on Apple M series.

GPU acceleration requires an NVIDIA GPU, the NVIDIA Linux driver and the NVIDIA Container Toolkit.

{{<rich-content-end >}}

{{<rich-box-end >}}

For further information, see <https://github.com/b-data/jupyterlab-qgis-docker-stack>.
## Stabil QGIS
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
## QGIS-verzió
To run a container with a specific QGIS version, command
```shell
docker run -it --rm \
  -p 8888:8888 \
  -v jupyterlab-jovyan:/home/jovyan \
  quay.io/bedata/jupyterlab/qgis/base:MAJOR[.MINOR[.PATCH]]
```
{{<rich-box-start icon="🐳" layoutClass="tips" >}}

{{<rich-content-start themeClass="coloring-1" >}}
##### Note
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
##### Note
GPU accelerated container images on Quay are available for QGIS versions ≥ 3.40.4.

For QGIS versions 3.34.0 to 3.40.3 use `glcr.b-data.ch/jupyterlab/cuda/qgis/base:MAJOR[.MINOR[.PATCH]]`.

{{<rich-content-end >}}

{{<rich-box-end >}}
# QGIS Testing figyelmeztetés
{{<rich-box-start icon="⚠️" layoutClass="tips" >}}

{{<rich-content-start themeClass="coloring-6" >}}
##### Figyelmeztetés
QGIS testing packages are provided for some platforms in addition to the QGIS stable version. QGIS testing contains unreleased software that is currently being worked on. They are only provided for testing purposes to early adopters to check if bugs have been resolved and that no new bugs have been introduced. Although we carefully try to avoid breakages, it may at any given time not work, or may do bad things to your data. Take care. You have been warned!

{{<rich-content-end >}}

{{<rich-box-end >}}
# Telepítés forráskódból
Please refer to [the developer installation notes](https://github.com/qgis/QGIS/blob/master/INSTALL.md) for notes on how to build and install QGIS from source for the different platforms we support.

{{<content-end >}}
