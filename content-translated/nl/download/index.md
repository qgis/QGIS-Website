---
Reviewed: 1 June 2024
Reviewer: Tim Sutton
draft: false
sidebar: true
subtitle: ''
title: Downloaden
type: page

---
{{<content-start >}}

{{< rich-box-start mode="html" layoutClass="has-right" id="donate-prompt">}} {{< rich-content-start themeClass="coloring-2" >}}
## Voordat het downloaden begint
QGIS is gratis, en zal altijd gratis blijven, zonder kosten beschikbaar als het wordt gedownload vanaf QGIS.org.

Het project is een resultaat van de grote inspanningen en sociale bijdragen van veel leden van de gemeenschap die vrijwillig hun tijd en expertise beschikbaar stellen. In aanvulling daarop hebben heel veel zakelijke deelnemers, afdelingen van overheden en commerciële bedrijven bijgedragen aan de ontwikkeling van QGIS. Ze doen dat om ofwel ervoor te zorgen dat QGIS voldoet aan hun specifieke behoeften of om bij te dragen aan en door te laten gaan de grote sociale impact die wordt gerealiseerd door een gereedschap, zoals QGIS, gratis beschikbaar te maken. Ons doel is het verbeteren van de maatschappij door het geïnformeerd kunnen nemen van ruimtelijke beslissingen. Als u dat kunt, verzoeken wij u vriendelijk ons werk te ondersteunen.

Of u ervoor kiest om te doneren of niet, we hopen dat u geniet van ons werk van liefde en moedigen u aan om uw gedownloade kopie te delen en breed verder te verspreiden, zodat anderen er ook van kunnen genieten.

Onze allerbeste groeten!

<p class="is-size-7 has-text-weight-medium">
Donations to QGIS might be tax-deductible in some countries. Please refer to your local tax office for details. If you want to tax-deduct as a German company or organization, please donate through the <a href="https://qgis.de/doku.php/verein/spenden">German QGIS user group</a>. They can issue a payment confirmation as a tax-exempt German association.
</p>

{{< rich-content-end >}} {{< rich-right-start mode="html" >}} {{< payrexx-widget otherMethods="true" skipToDownload="true" >}} {{< rich-right-end >}} {{< rich-box-end >}}

{{<download-platforms-start >}}

{{< spoiler-start id="download-win" title="Downloaden voor Windows">}} {{< download-windows >}} {{< spoiler-end >}}

{{< spoiler-start id="download-linux" title="🐧 Linux" >}} GNU/Linux is een gratis besturingssysteem, gebouwd op dezelfde principes als waar QGIS op is gebouwd. We verschaffen installatieprogramma's voor vele soorten van binaire pakketten van GNU/Linux (inclusief pakketten rpm en deb). Selecteer de distributie van uw keuze hieronder:
- [Debian/Ubuntu]({{< ref "resources/installation-guide#debian--ubuntu" >}})
- [Fedora]({{< ref "resources/installation-guide#fedora" >}})
- [NixOS]({{< ref "resources/installation-guide#nixos" >}})
- [openSUSE]({{< ref "resources/installation-guide#suse--opensuse" >}})
- [Mandriva]({{< ref "resources/installation-guide#mandriva" >}})
- [Slackware]({{< ref "resources/installation-guide#slackware" >}})
- [Arch Linux]({{< ref "resources/installation-guide#arch-linux" >}})
- [Flatpak]({{< ref "resources/installation-guide#flatpak" >}})
- [Spack]({{< ref "resources/installation-guide#spack" >}})

[Linux installatie-instructies]({{< ref "resources/installation-guide#linux" >}}) {{< spoiler-end >}}

{{< spoiler-start id="download-mac" title="🍏 macOS" >}} {{< rich-box-start icon="⚠️" layoutClass="tips">}} {{< rich-content-start themeClass="coloring-2" >}}
#### QGIS versions for macOS notice
The QGIS installers for macOS are currently **outdated** and do not reflect the latest version of QGIS. If you need newer features or fixes, please consider installing QGIS via [MacPorts]({{< ref "resources/installation-guide/#macports" >}}). We are working on new, solid macOS builds for QGIS 4. If you wish to be an early beta tester, you can test a preview build at [this repository](https://github.com/opengisch/qgis-notarize). This package will become an official, OSGEO signed package as of QGIS 4.0.

{{< rich-content-end >}} {{< rich-box-end >}} {{< download-macos >}}

Alts alternatief, voor eigen ondersteuning van zowel architectuur van Intel x86 als van Apple ARM, samen met de laatste versies van sleutelcomponenten (bijv. GDAL, PDAL, GRASS GIS) bekijk [MacPorts installatie-instructies]({{< ref "resources/installation-guide/#macports" >}})

{{< rich-box-start icon="💁" layoutClass="tips">}} {{< rich-content-start themeClass="coloring-1" >}}
##### Tips voor de eerste keer opstarten
Na het installeren van QGIS zou de eerste keer opstarten kunnen mislukken door het beveiligingsframewerk van Apple.

**Voor macOS Sonoma (14) en eerder:** Inschakelen van QGIS, command-klik op zijn pictogram in uw map Toepassingen en selecteer ***Openen*** in het contextmenu om QGIS in te schakelen. Een dialoogvenster voor bevestiging zal worden weergegeven waarin u opnieuw moet klikken op de knop ***Openen***. Dit hoeft slechts eenmaal te worden gedaan.

**Voor macOS Sequoia (15) en nieuwer:** Inschakelen van QGIS, command-klik op zijn pictogram in uw map Toepassingen en selecteer ***Openen*** in het contextmenu om QGIS in te schakelen. Een dialoogvenster voor bevestiging zal worden weergegeven waarin u opnieuw moet klikken op de knop ***Voltooid***. Navigeer vervolgens naar ***Systeeminstellingen > Privacy & beveiliging*** en scroll naar het gedeelte ***Beveiliging***. U zou een bericht moeten zien dat vermeld dat ***"QGIS" werd geblokkeerd om uw Mac te beschermen***. Klik op ***Toch openen***. Een dialoogvenster voor bevestiging zal verschijnen; klik opnieuw op ***Toch openen***. Dit hoeft slechts eenmaal te worden gedaan.

{{< rich-content-end >}} {{< rich-box-end >}}

{{<spoiler-end >}}

{{< spoiler-start id="download-bsd" title="👿 BSD" >}} [BSD installatie-instructies]({{< ref "resources/installation-guide#freebsd" >}}) {{< spoiler-end >}}

{{< spoiler-start id="download-container-images" title="🐳 Container-images" >}} [Container-images installatie-instructies]({{< ref "resources/installation-guide#container-images" >}}) {{< spoiler-end >}}

{{< spoiler-start id="download-mobile" title="📱Mobiel en tablet" >}} {{< mobile-downloads >}} {{< spoiler-end >}}

{{< spoiler-start title="📃 Broncode" >}} QGIS is open source software, beschikbaar onder de termen van de <b>GNU General Public License</b> wat betekent dat zijn broncode kan worden gedownload in 'tarballs' of vanuit de opslagplaats van git.

QGIS broncode is beschikbaar <a href="/downloads/qgis-latest.tar.bz2">hier (laatste uitgave)</a> en <a href="/downloads/qgis-latest-ltr.tar.bz2">hier (lange termijn uitgave)</a>

Bekijk de installatiegids om te zien hoe QGIS te compileren vanuit de bron voor de verschillende platforms: [hier](https://github.com/qgis/QGIS/blob/master/INSTALL.md)

U kunt de broncode ook verkrijgen door onze <a href="https://github.com/qgis/QGIS">opslagplaats van GitHub</a>te klonen of te forken. {{< spoiler-end >}}

{{< spoiler-start title="🗾 Voorbeeld gegevenssets" >}} Voor doeleinden van testen en leren, [is een voorbeeld gegevensset beschikbaar](https://docs.qgis.org/latest/en/docs/user_manual/introduction/getting_started.html#downloading-sample-data), die collecties van gegevens bevat uit verschillende bronnen en in verschillende indelingen. {{< spoiler-end >}}

{{<download-platforms-end >}}

{{<script src="js/spoiler.js" >}}

{{<content-end >}}
