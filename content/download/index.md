---
type: "page"
title: "Download"
subtitle: ""
draft: false
sidebar: true
url: '/download'
Reviewed: 1 June 2024
Reviewer: Tim Sutton
---

{{< content-start  >}}

{{< rich-box-start mode="html" layoutClass="has-right" id="donate-prompt">}}
{{< rich-content-start themeClass="coloring-2" >}}
## Before download starts

Our software is, and always will be, available free of charge if downloaded from QGIS.org.

The project is a result of a huge effort and social contribution from many community members who volunteer their time and expertise. In addition, many businesses, government agencies and commercial entities have contributed to the development of QGIS. They do this either to ensure that QGIS meets their specific needs or to contribute to and accelerate the huge social impact that is realised by making a tool such as QGIS freely available. Our goal is the betterment of society through informed spatial decision making. If you are able, we gently request that you support our work.

Whether you choose to donate or not, we hope that you enjoy using our labour of love and encourage you to share and spread your downloaded copy far and wide so that others may enjoy it too.

Our very best regards!

{{< rich-content-end >}}
{{< rich-right-start mode="html" >}}
{{< stripe-widget otherMethods="true" >}}
{{< rich-right-end >}}
{{< rich-box-end >}}

{{< hide-donate-prompt >}}

{{< download-platforms-start >}}

{{< spoiler-start id="download-win" title="Download for Windows">}}
{{< download-windows >}}
{{< spoiler-end >}}


{{< spoiler-start id="download-linux" title="🐧 Linux" >}}
GNU/Linux is a Free operating system built on the same principles that QGIS is built on.
We provide installers for many flavors of GNU/Linux binary packages (including rpm and deb packages). Please select your choice of distro below:

- [Debian/Ubuntu]({{< ref "resources/installation-guide#debianubuntu" >}})
- [Fedora]({{< ref "resources/installation-guide#fedora" >}})
- [NixOS]({{< ref "resources/installation-guide#nixos" >}})
- [openSUSE]({{< ref "resources/installation-guide#suse-opensuse" >}})
- [Mandriva]({{< ref "resources/installation-guide#mandriva" >}})
- [Slackware]({{< ref "resources/installation-guide#slackware" >}})
- [Arch Linux]({{< ref "resources/installation-guide#arch-linux" >}})
- [Flatpak]({{< ref "resources/installation-guide#flatpak" >}})
- [Spack]({{< ref "resources/installation-guide#spack" >}})

[Linux Installation Instructions]({{< ref "resources/installation-guide#linux" >}})
{{< spoiler-end >}}


{{< spoiler-start id="download-mac" title="🍏 macOS" >}}
{{< download-macos >}}

Alternatively, for native support of both Intel x86 and Apple ARM architectures, together with the latest versions of key components (e.g. GDAL, PDAL, GRASS GIS) see [MacPorts Installing Instructions]({{< ref "resources/installation-guide/#macports" >}})

{{< rich-box-start icon="💁" layoutClass="tips">}}
{{< rich-content-start themeClass="coloring-1" >}}

##### Tips for first launch
After installing QGIS, the first launch attempt may fail due to Apple's security framework. To enable QGIS, command-click on its icon in your Applications folder and select 'Open' in the context menu. A confirmation dialog will display where you need to click the 'Open' button again. This only has to be done once.
{{< rich-content-end >}}
{{< rich-box-end >}}

{{< spoiler-end >}}


{{< spoiler-start id="download-bsd" title="👿 BSD" >}}
[BSD Installation Instructions]({{< ref "resources/installation-guide#freebsd" >}})
{{< spoiler-end >}}


{{< spoiler-start id="download-mobile" title="📱Mobile and tablet" >}}
{{< mobile-downloads >}}
{{< spoiler-end >}}


{{< spoiler-start title="📃 Source Code" >}}
QGIS is open source software available under the terms of the <b>GNU General Public License</b> meaning that its source code can be downloaded through 'tarballs' or the git repository.

QGIS Source Code is available <a href="/downloads/qgis-latest.tar.bz2">here (latest release)</a> and <a href="/downloads/qgis-latest-ltr.tar.bz2">here (long term release)</a>

Refer to the installation guide on how to compile QGIS from source for the different platforms: [here](https://github.com/qgis/QGIS/blob/master/INSTALL.md)

You can also obtain the source code by cloning or forking our <a href="https://github.com/qgis/QGIS">GitHub repository</a>.
{{< spoiler-end >}}


{{< spoiler-start title="🗾 Example Datasets" >}}
For testing and learning purposes, [a sample dataset is available](https://docs.qgis.org/latest/en/docs/user_manual/introduction/getting_started.html#downloading-sample-data), which contains collections of data from different sources and in different formats.
{{< spoiler-end >}}


{{< download-platforms-end >}}

{{< script src="js/spoiler.js" >}}

{{< content-end >}}
