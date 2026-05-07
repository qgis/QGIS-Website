---
HasDownloadBanner: true
Reviewed: 1 June 2024
Reviewer: Tim Sutton
draft: false
sidebar: true
subtitle: ''
title: Téléchargement
type: page

---
{{<content-start >}}

{{< rich-box-start mode="html" layoutClass="has-right" id="donate-prompt">}} {{< rich-content-start themeClass="coloring-2" >}}
## Avant le début du téléchargement
Notre logiciel est, et restera toujours, disponible gratuitement s'il est téléchargé depuis QGIS.org.

Ce projet est le fruit d'un immense effort et d'une contribution sociale de la part de nombreux membres de la communauté qui mettent bénévolement à disposition leur temps et leur expertise. De plus, de nombreuses entreprises, agences gouvernementales et entités commerciales ont contribué au développement de QGIS. Elles le font soit pour s'assurer que QGIS réponde à leurs besoins spécifiques, soit pour contribuer à l'énorme impact social généré par la mise à disposition gratuite d'un outil tel que QGIS et pour l'accélérer. Notre objectif est d'améliorer la société grâce à une prise de décision spatiale éclairée. Si vous en avez la possibilité, nous vous invitons chaleureusement à soutenir notre travail.

Que vous décidiez de faire un don ou non, nous espérons que vous apprécierez le fruit de notre travail et nous vous encourageons à partager et à diffuser largement votre copie téléchargée afin que d'autres puissent eux aussi en profiter.

Bien cordialement !

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

Official All-in-one, signed and notarized installers for macOS. [Learn more]({{< ref "resources/installation-guide#binary-packages-installers" >}}).

Alternatively, it is also possible to install QGIS via MacPorts, see the [MacPorts Installing Instructions]({{< ref "resources/installation-guide/#macports" >}})

{{<platform-content-end >}}

{{<platform-content-end >}}

{{<platform-content-start platform="linux" >}}
## Linux
GNU/Linux est un système d'exploitation libre fondé sur les mêmes principes que QGIS. Nous proposons des programmes d'installation pour de nombreuses distributions GNU/Linux sous forme de paquets binaires (notamment des paquets rpm et deb). Veuillez sélectionner ci-dessous la distribution de votre choix :
- [Debian/Ubuntu]({{< ref "resources/installation-guide#debian--ubuntu" >}})
- [Fedora]({{< ref "resources/installation-guide#fedora" >}})
- [NixOS]({{< ref "resources/installation-guide#nixos" >}})
- [openSUSE]({{< ref "resources/installation-guide#suse--opensuse" >}})
- [Mandriva]({{< ref "resources/installation-guide#mandriva" >}})
- [Slackware]({{< ref "resources/installation-guide#slackware" >}})
- [Arch Linux]({{< ref "resources/installation-guide#arch-linux" >}})
- [Flatpak]({{< ref "resources/installation-guide#flatpak" >}})
- [Spack]({{< ref "resources/installation-guide#spack" >}})

[Instructions d'installation sous Linux]({{< ref "resources/installation-guide#linux" >}}) {{< platform-content-end >}}

{{<platform-content-start platform="bsd" >}}
## BSD
[Instructions d'installation de BSD]({{< ref "resources/installation-guide#freebsd" >}}) {{< platform-content-end >}}

{{<platform-content-start platform="container" >}}
## Container Images
[Container Images Installation Instructions]({{< ref "resources/installation-guide#container-images" >}}) {{< platform-content-end >}}

{{<platform-content-start platform="mobile" >}}
## Mobile et tablette
{{< mobile-downloads >}} {{< platform-content-end >}}

{{<platform-content-start platform="source" >}}
## Code source
QGIS is open source software available under the terms of the <b>GNU General Public License</b> meaning that its source code can be downloaded through 'tarballs' or the git repository.

QGIS Source Code is available <a href="/downloads/qgis-latest.tar.bz2">here (latest release)</a> and <a href="/downloads/qgis-latest-ltr.tar.bz2">here (long term release)</a>

Consultez le guide d'installation pour savoir comment compiler QGIS à partir du code source sur les différentes plateformes : [ici](https://github.com/qgis/QGIS/blob/master/INSTALL.md)

You can also obtain the source code by cloning or forking our <a href="https://github.com/qgis/QGIS">GitHub repository</a>. {{< platform-content-end >}}

{{<platform-content-start platform="example" >}}
## Exemples de jeux de données
For testing and learning purposes, [a sample dataset is available](https://docs.qgis.org/latest/en/docs/user_manual/introduction/getting_started.html#downloading-sample-data), which contains collections of data from different sources and in different formats. {{< platform-content-end >}}

{{<download-platform-selector-end >}}

{{<content-end >}}
