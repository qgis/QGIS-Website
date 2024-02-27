---
type: "page"
title: "Download"
subtitle: ""
draft: false
sidebar: true
url: '/download'
---

{{< content-start  >}}

{{< rich-box mode="html" layoutClass="has-right" id="donate-prompt">}}
{{< rich-content themeClass="coloring-2" >}}
## Before download starts

QGIS is free of charge, and will always be free of charge if downloaded from QGIS.org.

If you can afford to support the project and people making this software, please consider making a small donation to support our efforts. Whether you choose to donate or not, we hope that you enjoy using our labour of love and encourage you to share and spread your downloaded copy far and wide so that others may enjoy it too.

Our very best regards!

We use the stripe.com service to receive credit card donations. Note that the payment fees at Stripe are substantially lower than at Paypal - so we would appreciate it, if you could use Stripe instead of PayPal. No signup needed.
{{< /rich-content >}}
{{< rich-right mode="html" >}}
{{< stripe-widget otherMethods="true" >}}
{{< /rich-right >}}
{{< /rich-box >}}

{{< hide-donate-prompt >}}

{{< download-platforms-start >}}

{{< spoiler-start id="download-win" title="Download for Windows">}}
{{< download-windows >}}
{{< spoiler-end >}}


{{< spoiler-start id="download-linux" title="Download for Linux" >}}
For many flavors of GNU/Linux binary packages (rpm and deb) or software repositories (to add to your installation manager) are available. Please select your choice of distro below:

- [Debian/Ubuntu](../resources/installation-guide#debian-ubuntu)
- [Fedora](../resources/installation-guide#fedora)
- [openSUSE](../resources/installation-guide#suse-opensuse)
- [Mandriva](../resources/installation-guide#mandriva)
- [Slackware](../resources/installation-guide#slackware)
- [Arch Linux](../resources/installation-guide#arch-linux)
- [Flatpak](../resources/installation-guide#flatpak)
- [Spack](../resources/installation-guide#spack)

[Linux Installation Instructions](../resources/installation-guide#linux)
{{< spoiler-end >}}


{{< spoiler-start id="download-mac" title="Download for MacOS" >}}
{{< download-macos >}}

Alternatively, for native support of both Intel x86 and Apple ARM architectures, together with the latest versions of key components (e.g. GDAL, PDAL, GRASS GIS) see [MacPorts Installing Instructions]({{< ref "resources/installation-guide/#macports" >}})

{{< rich-box icon="💁" layoutClass="tips">}}
{{< rich-content themeClass="coloring-1" >}}
##### Tips for first launch
After installing QGIS, the first launch attempt may fail due to security protections. To enable QGIS, control-click on its icon in your Applications folder and select Open in the context menu. A confirmation dialog will display where you need to click the Open button again. This only has to be done once.
{{< /rich-content >}}
{{< /rich-box >}}

{{< spoiler-end >}}


{{< spoiler-start id="download-bsd" title="Download for BSD" >}}
[BSD Installation Instructions](../resources/installation-guide#freebsd)
{{< spoiler-end >}}


{{< spoiler-start id="download-mobile" title="Apps for mobile and tablet" >}}
{{< mobile-downloads >}}
{{< spoiler-end >}}


{{< spoiler-start title="Sources" >}}
QGIS is open source software available under the terms of the <b>GNU General Public License</b> meaning that its source code can be downloaded through tarballs or the git repository.

QGIS Source Code is available <a href="https://qgis.org/downloads/qgis-latest.tar.bz2">here (latest release)</a> and <a href="https://qgis.org/downloads/qgis-latest-ltr.tar.bz2">here (long term release)</a>

Refer to the INSTALL guide on how to compile QGIS from source for the different platforms: [here](https://github.com/qgis/QGIS/blob/master/INSTALL.md)
{{< spoiler-end >}}


{{< spoiler-start title="Datasets" >}}
For testing and learning purposes, [a sample dataset is available](https://docs.qgis.org/3.28/en/docs/user_manual/introduction/getting_started.html#downloading-sample-data), which contains collections of data from different sources and in different formats.
{{< spoiler-end >}}


{{< download-platforms-end >}}

{{< script src="js/spoiler.js" >}}

{{< content-end >}}
