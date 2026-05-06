---
HasDownloadBanner: true
Reviewed: 1 June 2024
Reviewer: Tim Sutton
draft: false
sidebar: true
subtitle: ''
title: ダウンロード
type: page

---
{{<content-start >}}

{{< rich-box-start mode="html" layoutClass="has-right" id="donate-prompt">}} {{< rich-content-start themeClass="coloring-2" >}}
## ダウンロードを始める前に
QGIS.orgからダウンロードするQGISは、現在も将来にわたって常に無料でご利用いただけます。

このプロジェクトは、多くのコミュニティメンバーが時間と専門知識を惜しみなく提供してきた多大な努力と社会的貢献の賜物です。また、多くの企業・政府機関・商業団体もQGISの開発に貢献しています。これらの組織は、QGISが自らのニーズに応えられるよう、またはQGISのようなツールを無償提供することで生まれる大きな社会的インパクトに貢献・加速するために支援を行っています。私たちの目標は、空間情報に基づいた意思決定を通じて社会をより良くすることです。ご支援いただける方は、ぜひ私たちの活動をお支えください。

寄付をされるかどうかにかかわらず、私たちの心を込めた作品をお楽しみいただけることを願っています。また、他の方々にも楽しんでいただけるよう、ダウンロードしたコピーを広くシェア・共有していただくことをお勧めします。

どうぞよろしくお願いいたします！

<p class="is-size-7 has-text-weight-medium">
QGISへの寄付は、一部の国において税控除の対象となる場合があります。詳細については、地域の税務署にお問い合わせください。ドイツの企業や組織として税控除を受けたい場合は、German QGIS user groupを通じてご寄付ください。 <a href="https://qgis.de/doku.php/verein/spenden">German QGIS user group</a>はドイツの税免除団体として、寄付の支払い確認書を発行することができます。
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

または、MacPortsを使用してQGISをインストールすることも可能です。 [MacPortsインストール手順]({{< ref "resources/installation-guide/#macports" >}}) をご参照ください。

{{<platform-content-end >}}

{{<platform-content-end >}}

{{<platform-content-start platform="linux" >}}
## Linux
GNU/Linuxは、QGISと同じ理念で構築されたフリーオペレーティングシステムです。多くのGNU/Linuxディストリビューション向けにバイナリパッケージ（rpmおよびdebパッケージを含む）のインストーラーを提供しています。以下からお使いのディストリビューションをお選びください:
- [Debian/Ubuntu]({{< ref "resources/installation-guide#debian--ubuntu" >}})
- [Fedora]({{< ref "resources/installation-guide#fedora" >}})
- [NixOS]({{< ref "resources/installation-guide#nixos" >}})
- [openSUSE]({{< ref "resources/installation-guide#suse--opensuse" >}})
- [Mandriva]({{< ref "resources/installation-guide#mandriva" >}})
- [Slackware]({{< ref "resources/installation-guide#slackware" >}})
- [Arch Linux]({{< ref "resources/installation-guide#arch-linux" >}})
- [Flatpak]({{< ref "resources/installation-guide#flatpak" >}})
- [Spack]({{< ref "resources/installation-guide#spack" >}})

[Linux インストール解説]({{< ref "resources/installation-guide#linux" >}}) {{< platform-content-end >}}

{{<platform-content-start platform="bsd" >}}
## BSD
[BSD インストール解説]({{< ref "resources/installation-guide#freebsd" >}}) {{< platform-content-end >}}

{{<platform-content-start platform="container" >}}
## Container Images
[コンテナイメージインストール解説]({{< ref "resources/installation-guide#container-images" >}}) {{< platform-content-end >}}

{{<platform-content-start platform="mobile" >}}
## モバイルとタブレット
{{< mobile-downloads >}} {{< platform-content-end >}}

{{<platform-content-start platform="source" >}}
## ソースコード
QGISは <b>GNU General Public License</b> の条件のもとで利用可能なオープンソースソフトウェアであり、ソースコードは 'tarballs' またはgitリポジトリからダウンロードすることができます。

QGIS ソースコードは <a href="/downloads/qgis-latest.tar.bz2">here (latest release)</a> と <a href="/downloads/qgis-latest-ltr.tar.bz2">here (long term release)</a> から取得できます　　

各プラットフォームでQGISをソースからコンパイルする手順については、以下のインストールガイドをご覧ください : [こちら](https://github.com/qgis/QGIS/blob/master/INSTALL.md)

私たちの <a href="https://github.com/qgis/QGIS">GitHub repository</a> をクローンまたはフォークすることによっても、ソースコードを取得できます。　. {{< platform-content-end >}}

{{<platform-content-start platform="example" >}}
## データセットの例
テストや学習用として、さまざまなソースとフォーマットのデータを収録した[サンプルデータセット](https://docs.qgis.org/latest/en/docs/user_manual/introduction/getting_started.html#downloading-sample-data)をご利用いただけます。 {{< platform-content-end >}}

{{<download-platform-selector-end >}}

{{<content-end >}}
