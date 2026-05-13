---
HasDownloadBanner: true
Reviewed: 1 June 2024
Reviewer: Tim Sutton
draft: false
sidebar: true
subtitle: ''
title: Скачать
type: page

---
{{<content-start >}}

{{< rich-box-start mode="html" layoutClass="has-right" id="donate-prompt">}} {{< rich-content-start themeClass="coloring-2" >}}
## Прежде чем начнётся загрузка
Наше ПО всегда было и будет доступно бесплатно на QGIS.org.

Этот проект - результат огромных усилий множества участников, которые на волонтёрской основе вкладывают в него своё время и профессиональные навыки. Помимо этого, развитию QGIS помогает множество коммерческих компаний и государственных организаций. Они поддерживают проект, чтобы QGIS мог решать их конкретные задачи, или из-за социального значения общедоступности такого инструмента, как QGIS. Наша цель — улучшить общество, помогая принимать информированные решения в сфере территориального планирования. Если у вас есть такая возможность, мы просим вас поддержать нашу работу.

Независимо от того, решите ли вы сделать пожертвование, мы надеемся, что вы с удовольствием будете использовать наше детище. Делитесь своей копией программы и распространяйте её как можно шире, чтобы она помогала и другим пользователям.

С наилучшими пожеланиями!

<p class="is-size-7 has-text-weight-medium">
Пожертвования в QGIS могут предусматривать налоговый вычет в некоторых странах. Пожалуйста, обратитесь в ваш налоговый орган за подробностями. Если вы хотите получить налоговый вычет как немецкая компания или организация, пожалуйста, оформите пожертвование через <a href="https://qgis.de/doku.php/verein/spenden">Немецкое сообщество QGIS</a>. Там вам выдадут подтверждение платежа от освобождённой от налогов немецкой ассоциации.
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

Также вы можете установить QGIS через MacPorts, см. [инструкцию по установке через MacPorts]({{< ref "resources/installation-guide/#macports" >}})

{{<platform-content-end >}}

{{<platform-content-end >}}

{{<platform-content-start platform="linux" >}}
## Linux
GNU/Linux - свободно распространяемая операционная система, основанная на тех же принципах, что и QGIS. У нас вы найдёте установщики для разных бинарных пакетов GNU/Linux  (в том числе rpm и deb). Выберите подходящий дистрибутив ниже:
- [Debian/Ubuntu]({{< ref "resources/installation-guide#debian--ubuntu" >}})
- [Fedora]({{< ref "resources/installation-guide#fedora" >}})
- [NixOS]({{< ref "resources/installation-guide#nixos" >}})
- [openSUSE]({{< ref "resources/installation-guide#suse--opensuse" >}})
- [Mandriva]({{< ref "resources/installation-guide#mandriva" >}})
- [Slackware]({{< ref "resources/installation-guide#slackware" >}})
- [Arch Linux]({{< ref "resources/installation-guide#arch-linux" >}})
- [Flatpak]({{< ref "resources/installation-guide#flatpak" >}})
- [Spack]({{< ref "resources/installation-guide#spack" >}})

[Инструкция по установке для Linux]({{< ref "resources/installation-guide#linux" >}}) {{< platform-content-end >}}

{{<platform-content-start platform="bsd" >}}
## BSD
[Инструкция по установке для BSD]({{< ref "resources/installation-guide#freebsd" >}}) {{< platform-content-end >}}

{{<platform-content-start platform="container" >}}
## Образы контейнеров
[Инструкция по установке образов контейнеров]({{< ref "resources/installation-guide#container-images" >}}) {{< platform-content-end >}}

{{<platform-content-start platform="mobile" >}}
## Мобильные устройства
{{< mobile-downloads >}} {{< platform-content-end >}}

{{<platform-content-start platform="source" >}}
## Исходный код
QGIS - ПО с открытым кодом, доступно по лицензии <b>GNU General Public License</b>, это означает, что его исходный код можно скачать через 'tarballs'  или репозиторий git.

Исходный код QGIS доступен <a href="/downloads/qgis-latest.tar.bz2">здесь (актуальный релиз)</a> и <a href="/downloads/qgis-latest-ltr.tar.bz2">здесь (long term release)</a>

Чтобы скомпилировать QGIS для других платформ, воспользуйтесь [следующим руководством](https://github.com/qgis/QGIS/blob/master/INSTALL.md)

Исходный код вы также можете получить путём клонирования или создания форка нашего <a href="https://github.com/qgis/QGIS">репозитория GitHub</a>. {{< platform-content-end >}}

{{<platform-content-start platform="example" >}}
## Примеры данных
Для целей тестирования и обучения [доступен пример набора данных](https://docs.qgis.org/latest/en/docs/user_manual/introduction/getting_started.html#downloading-sample-data), который содержит данные из разных источников в разных форматах. {{< platform-content-end >}}

{{<download-platform-selector-end >}}

{{<content-end >}}
