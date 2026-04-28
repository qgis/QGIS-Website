---
HasDownloadBanner: true
Reviewed: 1 June 2024
Reviewer: Tim Sutton
draft: false
sidebar: true
subtitle: ''
title: Изтегляне
type: page

---
{{<content-start >}}

{{< rich-box-start mode="html" layoutClass="has-right" id="donate-prompt">}} {{< rich-content-start themeClass="coloring-2" >}}
## Преди да започне изтеглянето
Our software is, and always will be, available free of charge if downloaded from QGIS.org.

Проектът е резултат от огромни усилия и социален принос от много членове на общността, които доброволно отделят своето време и експертиза. Освен това много фирми, държавни агенции и търговски организации са допринесли за разработването на QGIS. Те правят това или за да гарантират, че QGIS отговаря на техните специфични нужди, или за да допринесат и ускорят огромното социално въздействие, което се постига чрез предоставянето на инструмент като QGIS безплатно. Нашата цел е подобряването на обществото чрез информирано вземане на пространствени решения. Ако можете, учтиво ви молим да подкрепите нашата работа.

Whether you choose to donate or not, we hope that you enjoy using our labour of love and encourage you to share and spread your downloaded copy far and wide so that others may enjoy it too.

Най-сърдечните ни поздрави!

<p class="is-size-7 has-text-weight-medium">
Donations to QGIS might be tax-deductible in some countries. Please refer to your local tax office for details. If you want to tax-deduct as a German company or organization, please donate through the <a href="https://qgis.de/doku.php/verein/spenden">German QGIS user group</a>. They can issue a payment confirmation as a tax-exempt German association.
</p>

{{< rich-content-end >}} {{< rich-right-start mode="html" >}} {{< stripe-widget otherMethods="true" skipToDownload="true" >}}

<!-- {{< payrexx-widget otherMethods="true" skipToDownload="true" >}} -->

{{< rich-right-end >}} {{< rich-box-end >}}

{{<download-platform-selector-start >}}

{{<platform-content-start platform="windows" >}}
## Windows
{{< download-windows>}} {{< platform-content-end >}}

{{<platform-content-start platform="macos" >}}
## macOS
{{<download-macos >}}

Alternatively, it is also possible to install QGIS via MacPorts, see the [MacPorts Installing Instructions]({{< ref "resources/installation-guide/#macports" >}})

{{<platform-content-end >}}

{{<platform-content-end >}}

{{<platform-content-start platform="linux" >}}
## Linux
GNU/Linux is a Free operating system built on the same principles that QGIS is built on. We provide installers for many flavors of GNU/Linux binary packages (including rpm and deb packages). Please select your choice of distro below:
- [Debian/Ubuntu]({{< ref "resources/installation-guide#debian--ubuntu" >}})
- [Fedora]({{< ref "resources/installation-guide#fedora" >}})
- [NixOS]({{< ref "resources/installation-guide#nixos" >}})
- [openSUSE]({{< ref "resources/installation-guide#suse--opensuse" >}})
- [Mandriva]({{< ref "resources/installation-guide#mandriva" >}})
- [Slackware]({{< ref "resources/installation-guide#slackware" >}})
- [Arch Linux]({{< ref "resources/installation-guide#arch-linux" >}})
- [Flatpak]({{< ref "resources/installation-guide#flatpak" >}})
- [Spack]({{< ref "resources/installation-guide#spack" >}})

[Инструкции за инсталиране на Linux]({{< ref "resources/installation-guide#linux" >}}) {{< platform-content-end >}}

{{<platform-content-start platform="bsd" >}}
## BSD
[Инструкции за инсталиране на BSD]({{< ref "resources/installation-guide#freebsd" >}}) {{< platform-content-end >}}

{{<platform-content-start platform="container" >}}
## Container Images
[Инструкции за инсталиране на изображения на контейнери]({{< ref "resources/installation-guide#container-images" >}}) {{< platform-content-end >}}

{{<platform-content-start platform="mobile" >}}
## Мобилни устройства и таблети
{{< mobile-downloads >}} {{< platform-content-end >}}

{{<platform-content-start platform="source" >}}
## Изходен код
QGIS is open source software available under the terms of the <b>GNU General Public License</b> meaning that its source code can be downloaded through 'tarballs' or the git repository.

QGIS Source Code is available <a href="/downloads/qgis-latest.tar.bz2">here (latest release)</a> and <a href="/downloads/qgis-latest-ltr.tar.bz2">here (long term release)</a>

Refer to the installation guide on how to compile QGIS from source for the different platforms: [here](https://github.com/qgis/QGIS/blob/master/INSTALL.md)

You can also obtain the source code by cloning or forking our <a href="https://github.com/qgis/QGIS">GitHub repository</a>. {{< platform-content-end >}}

{{<platform-content-start platform="example" >}}
## Примерни набори от данни
For testing and learning purposes, [a sample dataset is available](https://docs.qgis.org/latest/en/docs/user_manual/introduction/getting_started.html#downloading-sample-data), which contains collections of data from different sources and in different formats. {{< platform-content-end >}}

{{<download-platform-selector-end >}}

{{<content-end >}}
