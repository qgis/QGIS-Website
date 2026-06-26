---
Reviewed: 4 June 2024
Reviewer: Tim Sutton
draft: false
sidebar: true
subtitle: ''
title: インストレーションガイド
type: page

---
{{<content-start >}}
# QGIS のインストーラー
QGIS は Windows, macOS, Linux, FreeBSD, OpenBSD, Android とiOSで利用可能です。

![Icons of Operating Systems](img/icons.png)

LTR（長期リリース）バージョンは、リリースの前により厳格なテストが行われ、少なくとも1年間のバグ修正アップデートが提供されるため、LTRパッケージをインストールすることをお勧めします。

 [the main installers page]({{< ref "download" >}}) も参照してください。

次期リリースの評価や、開発者以外の方にも開発をサポートしていただけるよう、テスト用パッケージも提供しています (注  [警告](#warning) をご確認して下さい).

 リリース前のフィーチャーフリーズ期間中  ( [リリーススケジュール]({{< ref "roadmap#release-schedule" >}}) 参照)  、これらのパッケージは事実上 **プレリリース版となります。ユーザーの皆様にはテストへのご協力を強くお願いします** 。
# Windows
Windowsへのインストール方法は2つあります:
## オフライン (単独) インストーラー
スタンドアロンインストーラーには、QGISに必要なすべてが1つのダウンロードファイルに含まれています。一度インストーラーを入手すれば、インストールを完了するのにインターネット接続は必要ありません。新しいリリースが利用可能になった際にアップグレードするには、完全なインストーラーを再度ダウンロードする必要があります。初心者にとって、スタンドアロンインストーラーはおそらく最も簡単なQGISのインストール方法です:
| リリース | バージョン | パッケージ | 代替手段 |
| --- | --- | --- | --- |
| 最新のリリース | {{< param "release" >}} {{< param "codename" >}} {{< param "releasenote" >}} | [Installer]({{< param "lr_msi" >}}) [Checksum]({{< param "lr_sha" >}}) | [Torrent]({{< param "lr_msi_torrent" >}}) [Magnet]({{< param "lr_msi_magnet" >}}) [Metalink]({{< param "lr_msi_meta4" >}}) |
| 長期サポートリリース | {{< param "ltrrelease" >}} {{< param "ltrcodename" >}} {{< param "ltrnote" >}} | [Installer]({{< param "ltr_msi">}}) [Checksum]({{< param "ltr_sha">}}) | [Torrent]({{< param "ltr_msi_torrent" >}}) [Magnet]({{< param "ltr_msi_magnet" >}}) [Metalink]({{< param "ltr_msi_meta4" >}}) |
| 開発版 | {{< param "devversion" >}} master | [Weekly snapshots]({{< param "weekly_msi">}}) | – |

オプションの投影グリッドはファイルサイズが大きいため、デフォルトのインストーラーには含まれていません。QGISは実行時に再投影にグリッドが必要かどうかを判断し、手動ダウンロードを求めます。

それが難しい環境や不便な場合のために、グリッドを含むスタンドアロンインストーラーも引き続き提供しています。4.0.1時点では、通常のインストーラーは0.5 GiB、全グリッドを含むインストーラーは1.2 GiBです。
| リリース | バージョン | パッケージ | 代替手段 |
| --- | --- | --- | --- |
| 最新のリリース | {{< param "release" >}} {{< param "codename" >}} {{< param "releasenote" >}} | [Installer]({{< param "lr_grids_msi" >}}) [Checksum]({{< param "lr_grids_sha" >}}) | [Torrent]({{< param "lr_grids_msi_torrent" >}}) [Magnet]({{< param "lr_grids_msi_magnet" >}}) [Metalink]({{< param "lr_grids_msi_meta4" >}}) |
| 長期サポートリリース | {{< param "ltrrelease" >}} {{< param "ltrcodename" >}} {{< param "ltrnote" >}} | [Installer]({{< param "ltr_grids_msi">}}) [Checksum]({{< param "ltr_grids_sha">}}) | [Torrent]({{< param "ltr_grids_msi_torrent" >}}) [Magnet]({{< param "ltr_grids_msi_magnet" >}}) [Metalink]({{< param "ltr_grids_msi_meta4" >}}) |

付属の "OSGeo4W Setup" を使って `proj-data`  パッケージをインストールすることで、後からグリッドを追加することもできます。または、同じく付属のコマンドラインツール  [projsync](https://proj.org/en/stable/apps/projsync.html)  を使って、特定のエリアのグリッドをダウンロードすることもできます。

OSGeo4Wのナイトリー qgis-dev パッケージのウィークリースナップショットは、何らかの理由でOSGeo4W（下記参照）を使用できないユーザーや、単にスタンドアロンインストーラーを好むユーザー向けに提供されています。機能フリーズ（開発凍結）フェーズでは、これらは  **リリース候補（RC）** インストーラーとしての役割も果たします。
## オンライン (OSGeo4W) インストーラー
上級者向けには、OSGeo4Wパッケージの使用をお勧めします。このインストーラーを使うと、複数バージョンのQGISを並行してインストールできるほか、新しいリリースのたびに変更されたコンポーネントのみがダウンロード・インストールされるため、より効率的なアップデートが可能です。

OSGeo4W リポジトリには、多くの OSGeo プロジェクトのソフトウェアが含まれています。Python、GRASS、GDAL などとともに、QGIS とすべての依存関係が含まれています。インストーラーは、インターネットからインストールすることも、必要なパッケージを事前にダウンロードすることも可能です。ダウンロードしたファイルは、将来のインストールのためにローカルディレクトリに保存され、オフラインでインストールするために使用することもできます。

インストール手順:
- [OSGeo4W Installer](https://download.osgeo.org/osgeo4w/v2/osgeo4w-setup.exe) をダウンロードして実行して下さい。
- Choose _Express Install_ and select _QGIS_ to install the _latest release_ and/or _QGIS LTR_ to install the _long term release_.

Alternatively, instead of doing the _Express_ install, you can use the _Advanced Install_, navigate to the _Desktop_ section and pick one or more of the following packages:
| リリース | バージョン | パッケージ | 説明 |
| --- | --- | --- | --- |
| 最新のリリース | {{< param "release" >}} {{< param "codename" >}} {{< param "releasenote" >}} | qgis | リリース |
|  |  | qgis-rel-dev [[1]](#id1) | 次バージョンの Nightly ビルド |
| 長期サポートリリース | {{< param "ltrrelease" >}} {{< param "ltrcodename" >}} {{< param "ltrnote" >}} | qgis-ltr | リリース |
|  |  | qgis-ltr-dev [[1]](#id1) | 次期長期サポートポイントリリースのナイトリービルド（Qt5） |
| 開発版 | {{< param "devversion" >}} master | qgis-dev [[1]](#id1) | 開発版のナイトリービルド [[2]](#id2) |

{{< footnote "1" >}} ナイトリービルドはデバッグビルドです (開発者がビルドの問題をより深く理解するために活用できるデバッグ出力を含みます)。

{{< footnote "2" >}} 4.0はQt6への移行を示すバージョンです。それ以前のQGISバージョンではQt6は実験的なサポートでした。4.0以降はQt6のみがサポートされます。

上記の表に記載されているパッケージは、QGISの実行に必要な依存関係のみをインストールします。これらのパッケージに対応して、 `-full-free` および  `-full` というサフィックスを持つメタパッケージも提供しています。 `-full-free` には、一部の人気プラグイン（デフォルトのQGISインストールには含まれない）が使用する追加のオプション依存関係が含まれます。 `-full`  は `-full-free` のすべてに加え、Oracleドライバー、ECW、MrSIDなどのプロプライエタリな拡張機能も含みます。

 エクスプレスインストールは対応する `-full` バリアントを参照しており、スタンドアロンインストーラーもこれらのOSGeo4Wパッケージセットから作成されています。

 `-full-grids`  バリアントはオプションの投影グリッドを含みます（つまり、`-full` に `proj-data` パッケージを加えたものです）。大容量のスタンドアロンインストーラーはこれらをベースにしています。

 ナイトリービルドをインストールする前に、以下の  [警告](#warning) をご確認ください。
# Linux
ほとんどのLinuxディストリビューションではQGISは複数のパッケージに分割されています。通常は  `qgis` と  `qgis-python` （プラグインの実行に必要）が必要です。 `qgis-grass` （または  `qgis-plugin-grass` ）や  `qgis-server` などのパッケージは、必要に応じてインストールできます。

以下に、ディストリビューションごとの具体的なインストール手順を記載しています。ほとんどのディストリビューションについて、安定版QGISおよび最新のQGISテストビルドのインストール手順を提供しています ( [warning](#warning) 参照) 。
## Debian / Ubuntu
### クイックスタート
{{<rich-box-start icon="💁" layoutClass="tips" >}}

{{<rich-content-start themeClass="coloring-1" >}}
##### Note
この次のセクションでは、さまざまなバージョンのDebian/Ubuntuに、さまざまなバージョンのQGISをインストールするためのすべての選択肢を紹介します。問題が発生した場合は、お使いのディストリビューションが現在もサポートされているか確認してください。リポジトリには、すでにサポート対象外となった古いディストリビューション向けに、当時サポートされていた最終バージョンのQGISも含まれています。これらは現在、動作しなくなっている可能性があることに注意してください。

{{<rich-content-end >}}

{{<rich-box-end >}}

設定ファイルを編集することなく、DebianまたはUbuntuに最新の安定版QGIS  ({{< param "version" >}}.x {{< param "codename" >}}) を簡単にインストールできます。

{{<rich-box-start icon="🌀" layoutClass="tips" >}}

{{<rich-content-start themeClass="coloring-1" >}}
##### Note
一部の箇所に  ‘Debian’ と表示されていますが、サーバー上では一方がもう一方へのシンボリックリンクになっているため、 ‘Ubuntu’ でも同様に機能します。

{{<rich-content-end >}}

{{<rich-box-end >}}

まず、この手順に必要なツールをインストールします:
```
sudo apt install gnupg software-properties-common
```
次に、QGISリポジトリからのソフトウェアが信頼され、インストールできるようにQGIS署名キーをインストールします:
```
sudo mkdir -m755 -p /etc/apt/keyrings  # not needed since apt version 2.4.0 like Debian 12 and Ubuntu 22 or newer
sudo wget -O /etc/apt/keyrings/qgis-archive-keyring.gpg https://download.qgis.org/downloads/qgis-archive-keyring.gpg
```
最新の安定版QGIS  ({{< param "version" >}}.x {{< param "codename" >}})  のQGISリポジトリを `/etc/apt/sources.list.d/qgis.sources` に追加します。 テキストエディターでファイルを開き (例 `sudo editor /etc/apt/sources.list.d/qgis.sources`) 、以下の内容を貼り付けてください ( `your-distributions-codename` は実際のディストリビューションのコードネームに置き換えてください,  [利用可能なコードネーム](#available-codenames) 参照):
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
 上記の `Suites`  はディストリビューションによって異なります。　`lsb_release -cs`  でディストリビューション名を確認できます。

（Linux Mintなどの）一部のディストリビューションでは、 `. /etc/os-release; echo "$UBUNTU_CODENAME"` を実行することで正しいディストリビューション名を確認できます。

 [利用可能なコードネーム](#available-codenames) を参照して下さい。

{{<rich-content-end >}}

{{<rich-box-end >}}

ファイルを保存して閉じるとあなたのリポジトリ情報が更新されます:
```
sudo apt update
```
QGISをインストールするには、次のコマンドを実行します:
```
sudo apt install qgis qgis-plugin-grass
```
{{<rich-box-start icon="✍️" layoutClass="tips" >}}

{{<rich-content-start themeClass="coloring-1" >}}
##### Note
 QGIS Serverもインストールする場合は、上記のコマンドに `qgis-server`  を追加してください。

{{<rich-content-end >}}

{{<rich-box-end >}}
### リポジトリ
DebianおよびUbuntuのデフォルトのソフトウェアリポジトリには、古いバージョンのQGISが含まれていることがよくあります。

 より新しいバージョンを入手するには、以下のdebラインのいずれかを `/etc/apt/sources.list.d/qgis.sources` ファイルに追加して、代替ソフトウェアリポジトリを設定する必要があります。

私たちのメインリポジトリには、個々のディストリビューションが提供する依存関係に基づいて、 **DebianとUbuntu** のいくつかのバージョンのパッケージが複数含まれています。

 Ubuntuについては、以前は  [ubuntugis](https://launchpad.net/~ubuntugis) をベースにした別リポジトリで追加パッケージを提供していました。このリポジトリには、LTSバージョンのUbuntu自体よりも新しい他のGISパッケージが含まれていました。これらが必要な場合は、/etc/apt/sources.list.d/qgis.list ファイルに ubuntugis-unstable ppa も追加する必要があります ([ubuntugisのドキュメント](https://trac.osgeo.org/ubuntugis/wiki/UbuntuGISRepository) 参照)。

{{<rich-box-start icon="💁" layoutClass="tips" mode="html" >}}

{{<rich-content-start themeClass="coloring-1" >}}
##### Note
リリースパッケージは、新バージョンのリリース直後に一度だけ作成されます。不安定版や未リリースのDebianバージョン（testing）およびubuntugis-unstableではライブラリが変更される場合があり、Debian・Ubuntu・ubuntugis-unstableの開発が進んでQGISの依存パッケージが変わると、これらのターゲット向けパッケージが動作しなくなることがあります。その場合は、以下のいずれかの対応が可能です:
- 安定したバージョンの debian に移行し、リリース済みのパッケージを使用する
- 毎月リリースされる次のポイントリリース (予定日 {{< param "nextpointreleasedate" >}}) を待つ。これには更新された依存関係が含まれます。
 
 
 
 
 
 
- パッケージが定期的に再構築され、更新された依存関係を自動的に取得する nightly リポジトリ（ **2** つのリリースブランチと master が利用可能）に切り替える
- 独自のパッケージセットをビルドする ( [build-debian-packages](https://github.com/qgis/QGIS/blob/master/INSTALL.md#310-building-debian-packages) 参照).

{{<rich-content-end >}}

{{<rich-box-end >}}

パッケージのラインアップ：
| リリース | バージョン | 説明 | リポジトリ |
| --- | --- | --- | --- |
| 最新のリリース | {{< param "version" >}}.x {{< param "codename" >}} {{< param "releasenote">}} | **DebianとUbuntu** 用のリリース | https://qgis.org/debian <br> https://qgis.org/ubuntu |
|  |  | ubuntugis-unstable 依存関係用のリリース | https://qgis.org/ubuntugis |
|  |  | DebianとUbuntuの今後のポイントリリースの夜間ビルド | https://qgis.org/debian-nightly-release <br> https://qgis.org/ubuntu-nightly-release |
|  |  | ubuntugis-unstable依存関係を持つ、今後のポイントリリースの夜間ビルド | https://qgis.org/ubuntugis-nightly-release |
| 長期リリースリポジトリ | {{< param "ltrversion" >}}.x {{< param "ltrcodename" >}} {{< param "ltrnote" >}} | **DebianとUbuntu** 用のリリース | https://qgis.org/debian-ltr https://qgis.org/ubuntu-ltr |
|  |  | ubuntugis-unstable 依存関係用のリリース | https://qgis.org/ubuntugis-ltr |
|  |  | DebianとUbuntuの今後のポイントリリースの夜間ビルド | https://qgis.org/debian-nightly-ltr <br> https://qgis.org/ubuntu-nightly-ltr |
|  |  | ubuntugis-unstable依存関係を持つ、今後のポイントリリースの夜間ビルド | https://qgis.org/ubuntugis-nightly-ltr |
| 開発バージョン | {{< param "devversion" >}} master | Nightly build for **Debian and Ubuntu** [[2]](#id2) | https://qgis.org/debian-nightly <br> https://qgis.org/ubuntu-nightly |
|  |  | Nightly build with ubuntugis-unstable dependencies [[2]](#id2) | https://qgis.org/ubuntugis-nightly |

{{< footnote "2" >}} Nightlies are debug builds (including debugging output)

<small>
Next point release: {{< param "nextpointreleasedate" >}}

Next release: {{< param "nextreleasedate" >}}

(For more dates see Release Schedule on [Road Map]({{< ref "resources/roadmap" >}})) </small>
#### サポートされているディストリビューションのバージョン：{#available-codenames }
| ディストリビューション | バージョン | コードネーム | Only LTR[[1]](#id1) | ubuntugis[[2]](#id2) |
| --- | --- | --- | --- | --- |
| Debian | 12.x (oldstable) | bookworm | はい |  |
|  | 13.x (stable) | trixie[[3]](#id3) |  |  |
|  | 不安定 | sid |  |  |
| Ubuntu | 26.04 (LTS) | resolute[[5]](#id5) |  |  |
|  | 25.10 | questing[[4]](#id4) |  |  |
|  | 25.04 | plucky[[3]](#id3) |  |  |
|  | 24.04 (LTS) | noble | はい | はい |
|  | 22.04 (LTS) | jammy | はい | はい |

{{< footnote "1" >}} debian/ubuntuの利用可能な依存関係がQGIS 4に対応していない (Qt6または依存パッケージ、pythonまたはsipが古すぎる)

{{< footnote "2" >}} ubuntugis依存関係に基づくビルド

{{< footnote "3" >}} 3.40.8/3.44.0から開始

{{< footnote "4" >}} 3.40.11/3.44.3 から開始

{{< footnote "5" >}} 4.0.1/3.44.9 から開始

QGISアーカイブを使用するには、まずアーカイブのリポジトリ公開鍵を追加する必要があります:
```
wget https://download.qgis.org/downloads/qgis-archive-keyring.gpg
gpg --no-default-keyring --keyring ./qgis-archive-keyring.gpg --list-keys
```
出力結果:
```
./qgis-archive-keyring.gpg
--------------------------
pub   rsa4096 2022-08-08 [SCEA] [expires: 2027-08-08]
      2D7E3441A707FDB3E7059441D155B8E6A419C5BE
uid           [ unknown] QGIS Archive Automatic Signing Key (2022-2027) <qgis-developer@lists.osgeo.org>
```
出力を確認したら、以下のコマンドでキーをインストールできます:
```
sudo mkdir -m755 -p /etc/apt/keyrings  # not needed since apt version 2.4.0 like Debian 12 and Ubuntu 22 or newer
sudo cp qgis-archive-keyring.gpg /etc/apt/keyrings/qgis-archive-keyring.gpg
```
または、手動での確認なしに直接キーをダウンロードすることもできます:
```
sudo mkdir -m755 -p /etc/apt/keyrings  # not needed since apt version 2.4.0 like Debian 12 and Ubuntu 22 or newer
sudo wget -O /etc/apt/keyrings/qgis-archive-keyring.gpg https://download.qgis.org/downloads/qgis-archive-keyring.gpg
```
 キーリングが設定されたら、リポジトリを追加できます。`/etc/apt/sources.list.d/qgis.sources` ファイルを作成または編集用に開き（例：`sudo editor /etc/apt/sources.list.d/qgis.sources` ）、以下の内容を追加してください（*repository* と *codename* は上記の表の値に置き換えてください）:
```
Types: deb deb-src
URIs: *repository*
Suites: *codename*
Architectures: amd64
Components: main
Signed-By: /etc/apt/keyrings/qgis-archive-keyring.gpg
```
Ubuntu 22.04 Jammy向けの最新長期サポートリリースの例:
```
Types: deb deb-src
URIs: https://qgis.org/ubuntu-ltr
Suites: jammy
Architectures: amd64
Components: main
Signed-By: /etc/apt/keyrings/qgis-archive-keyring.gpg
```
その後、以下のコマンドを入力してQGISをインストールします:
```
sudo apt update
sudo apt install qgis qgis-plugin-grass
```
QGIS Serverをインストールする場合は、次のコマンドを入力します:
```
sudo apt update
sudo apt install qgis-server --no-install-recommends --no-install-suggests
# if you want to install server Python plugins
apt install python3-qgis
```
{{<rich-box-start icon="💁" layoutClass="tips" >}}

{{<rich-content-start themeClass="coloring-1" >}}
##### Note
更新を行う前に他のリポジトリからインストールした全てのQGISとGRASSのパッケージを削除して下さい。

{{<rich-content-end >}}

{{<rich-box-end >}}
## Flatpak
{{<rich-box-start icon="💡" layoutClass="tips" >}}

{{<rich-content-start themeClass="coloring-1" >}}
##### Note
FlatpakはすべてのLinuxディストリビューション向けの汎用パッケージ形式です。パッケージはシステムから隔離されており、セキュリティと安定性のメリットをもたらします。例えば、安定したディストリビューション上で最新バージョンのQGISを使用することができます。

Flatpakはデフォルトですべてのユーザー向けにインストールされますが、`--user` 引数を使用して単一ユーザーのみにインストールすることもできます。

`sudo`  権限を持つユーザーのみがシステム全体のFlatpakアプリとリポジトリを変更できますが、すべてのユーザーがそれらを更新できます。これは管理されたマシンで役立ちます。

{{<rich-content-end >}}

{{<rich-box-end >}}

Flathubコミュニティによってメンテナンスされている、QGIS安定版とLTR向けのFlatpakが利用可能です。

一般的なインストール手順については、　[Flathubのウェブサイト](https://flatpak.org/setup) を参照してください。

[こちらでFlathub上のQGISを見つけることができます](https://flathub.org/apps/details/org.qgis.qgis).

インストールするには:
```
flatpak install flathub org.qgis.qgis
```
使用するQGISのバージョンを選択するよう求められます。

アプリがアプリランチャーに表示されるはずです。または、以下のコマンドを使用してください:
```
flatpak run org.qgis.qgis
```
QGISを含むFlatpakアプリを更新するには:
```
flatpak update
```
特定のディストリビューションでは、ファイルダイアログが表示されるようにするために `xdg-desktop-portal` パッケージと `xdg-desktop-portal-gtk` 、`xdg-desktop-portal-kde` 、または `xdg-desktop-portal-cosmic` のインストールが必要な場合があります。
 

 [Flathubのファイルはこちらで](https://github.com/flathub/org.qgis.qgis) 確認でき  [問題の報告はこちらから](https://github.com/flathub/org.qgis.qgis/issues) 行えます。
### ランタイムバージョンの表示
以下の追加機能が必要な場合、QGISが使用しているランタイムを確認する必要があります:
```
flatpak info org.qgis.qgis --show-runtime
```
### 拡張機能のサポート
プラグインに必要な追加のPythonモジュールをインストールする場合、以下のコマンドでモジュールをインストールできます（ここでは  `scipy ` モジュールをインストールする例）:
```
flatpak run --devel --command=pip3 org.qgis.qgis install scipy --user

# NOTE: you will likely get an error like: "error: runtime/org.kde.Sdk/x86_64/VERSION not installed" then also do:
flatpak install runtime/org.kde.Sdk/x86_64/VERSION
```
### HTML レンダリング
マップレイアウトなどでHTMLを使用したい場合は、`QtWebkit` が必要です。FlatpakのコマンドラインインターフェースからインストールできますL
```
flatpak install app/io.qt.qtwebkit.BaseApp/x86_64/VERSION
# ⚠️ WARNING: This is considered insecure and is therefore not provided by default.
```
## Fedora
{{<rich-box-start icon="🙋‍♂️" layoutClass="tips" >}}

{{<rich-content-start themeClass="coloring-1" >}}
##### Note
クライアントとサーバーアプリケーションを同じマシンにインストールすることは一般的な慣行ではありません。

{{<rich-content-end >}}

{{<rich-box-end >}}

Fedora系ディストリビューション向けのパッケージを `dnf` を使用して以下のコマンドで取得します:
```
sudo dnf install qgis python3-qgis qgis-grass qgis-server
```
**Fedora Atomic Desktops** を使用している場合、3つのオプションがあります:
1. Flatpak のインストール

FlatpakはFedora Atomic Desktopsにパッケージをインストールするための推奨方法です, [skip to the instructions](#flatpak).
2. システムへのQGISのインストール

これは最も簡単な方法で、データとディスクスペースを節約できますが、システムの更新が少し遅くなります。
```
rpm-ostree install qgis python3-qgis qgis-grass qgis-server
```
3. toolboxまたはdistroboxへのインストール

`toolbx` と `distrobox` の [instructions](#distrobox--toolbx) に従ってください。

FedoraはQGISの現在のリリースとLTRリリースを切り替えます。不安定な "Rawhide" ブランチでは、より新しいがバグを含む可能性があるQGISバージョンが提供されます。
| ディストリビューション | バージョン | QGISバージョン |
| --- | --- | --- |
| Fedora | 40 | {{< param "ltrversion" >}}.x {{< param "ltrcodename" >}} {{< param "ltrnote" >}} |
|  | 41 | {{< param "ltrversion" >}}.x {{< param "ltrcodename" >}} {{< param "ltrnote">}} |
|  | 42 | {{< param "version" >}}.x {{< param "codename" >}} {{< param "releasenote">}} |

常に更新されるバージョン情報はこちらです:
- [QGIS](https://packages.fedoraproject.org/pkgs/qgis/qgis)
- [QGIS-GRASS](https://packages.fedoraproject.org/pkgs/qgis/qgis-grass)

## NixOS
最新の安定版とLTRパッケージは [nixpkgsで利用可能](https://search.nixos.org/packages?channel=unstable&from=0&size=50&sort=relevance&type=packages&query=qgis) です。単一のコマンドで最先端の開発者バージョンを実行することもできます。
### 基本インストール
**一時的な利用:**
```
nix-shell -p qgis --command qgis
```
または
```
nix-shell -p qgis-ltr  --command qgis
```
**またはNixOSのconfiguration.nixに追加してシステムインストールの一部にする:**

LTR用
```  
  environment.systemPackages = [
    pkgs.qgis-ltr
  ];
```
最新安定版用:
```
environment.systemPackages = [
    pkgs.qgis
  ];
```
### 開発者スナップショットの実行 - リモート
ブランチまたはPRからの任意のgitリビジョン（2025年7月9日以降）について、GitHubから直接単一のコマンドで開発中のQGISバージョンを実行できます。Nixは参照したバージョンを自動的にビルドして実行します。

masterブランチの現在のコミットからQGISを実行するには:
```
nix run github:qgis/QGIS#qgis
```
特定のリビジョンを実行するには:
```
nix run github:qgis/QGIS/<git revision>#qgis
```
プルリクエストまたはブランチを実行するには:
```
nix run github:qgis/QGIS/<git branch>#qgis
```
### 開発者スナップショットの実行 - ローカル
QGISのローカルgitチェックアウトがある場合、ローカルのソースコードツリーを実行できます:
```
nix run .#qgis
```
QGISのgitチェックアウトディレクトリのルートで以下のコマンドを実行して開発者環境を作成することもできます:
```
nix develop
```
このコマンドを実行すると、ターミナルにビルドの追加手順が表示されます。
### 追加のPythonパッケージを使用して実行する場合:
Nixパッケージの隔離のため、追加のPythonパッケージをQGISで利用可能にするにはパッケージをオーバーライドする必要があります。例えば、numpy、geopandas、rasterioのPythonライブラリとともにQGISを実行するには以下を実行できます:

**一時的な利用:**
```
nix-shell -p \
      'qgis.override { extraPythonPackages = (ps: [ ps.numpy ps.future ps.geopandas ps.rasterio ps.debugpy ]);}' \
      --command "qgis"
```
**またはNixOSのconfiguration.nixに追加してシステムインストールの一部にする:**
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
 `qgis`  および  `qgis-ltr` という名前の最新の安定版とLTRパッケージが以下のリポジトリで利用可能です: 
| ディストリビューション | リポジトリ |
| --- | --- |
| Tumbleweed | https://download.opensuse.org/repositories/Application:/Geo/openSUSE_Tumbleweed/ |
| Leap 15.2 | https://download.opensuse.org/repositories/Application:/Geo/openSUSE_Leap_15.2/ |
| Leap 15.1 | https://download.opensuse.org/repositories/Application:/Geo/openSUSE_Leap_15.1/ |
| Factory ARM | https://download.opensuse.org/repositories/Application:/Geo/openSUSE_Factory_ARM/ |
| Factory PowerPC | https://download.opensuse.org/repositories/Application:/Geo/openSUSE_Factory_PowerPC/ |
| SLE 15 SP1 Backports | https://download.opensuse.org/repositories/Application:/Geo/SLE_15_SP1_Backports/ |
| SLE 15 SP1 Backports debug | https://download.opensuse.org/repositories/Application:/Geo/SLE_15_SP1_Backports_debug/ |

すべてのパッケージには GRASS と Pythonのサポートが含まれています。

全てのopenSUSE Geo リポジトリは、 https://download.opensuse.org/repositories/Application:/Geo/ にあります。

Install QGIS with this command:
```
sudo zypper in qgis qgis-plugin-grass 
```
OpenSUSE microOS、Kalpa、Aeonおよびその他のイミュータブルバリアントについては、`distrobox` [instructions](#distrobox--toolbx) の手順を参照してください。ベースシステムへのインストールは可能ですが推奨されません。
## Mandriva
### QGIS安定版
Current:
```
urpmi qgis-python qgis-grass
```
## Slackware
### QGIS安定版
https://slackbuilds.org/result/?search=qgis 上のパッケージ
## Arch Linux
### QGIS安定版
QGIS安定版はArch Linuxの公式リポジトリで利用可能です: https://archlinux.org/packages/extra/x86_64/qgis/

以下でインストールします:
```
pacman -S qgis
```
### QGIS LTR
QGIS長期リリースはAUR（Arch User Repository）にあります。

yaourtまたはAURをサポートするその他のパッケージマネージャーでインストールします:
```
yaourt -S qgis-ltr
```
バグやその他の振る舞いについては、ここのコメントを読んでください： https://aur.archlinux.org/packages/qgis-ltr/
### QGIS テスト版
QGIS テスト版は AUR (Arch User Repository) にあります。

yaourtまたはAURをサポートするその他のパッケージマネージャーでインストールします:
```
yaourt -S qgis-git
```
バグやその他の振る舞いについては、ここのコメントを読んでください： https://aur.archlinux.org/packages/qgis-git
## Spack
SpackはLinux用のdistro-agnosticパッケージマネージャで、ハイパフォーマンスコンピューティングの文脈で開発されています。

Spackのインストール方法に関する一般的な情報: https://github.com/spack/spack

QGIS package info on the Spack website: https://packages.spack.io/package.html?name=qgis

インストールするには:
```
spack install qgis
```
 これによりQGISと **すべての** 依存関係がゼロから構築されインストールされます。その後、QGISは以下から使用できます:
```
spack load qgis
```
追加のPythonパッケージをインストールする必要がある場合は、Spack環境の使用を推奨します。例えば:
```
spack env create myenv
spack env activate -p myenv
spack add qgis py-lz4
spack install
```
Spackに関係した問題は次に報告してください: https://github.com/spack/spack/issues
## Distrobox と Toolbx
To install QGIS on any Linux system, you can also use `distrobox` or `toolbx`. These allow you to install common distributions like Fedora, OpenSUSE or Ubuntu inside a container. This can be a different version than your main operating system, and thus allows you to have a newer, testing, or more stable version of QGIS.

{{<rich-box-start icon="🙋‍♀️" layoutClass="tips" >}}

{{<rich-content-start themeClass="coloring-1" >}}
##### Note
OpenSUSEとuBlueのFedoraベースのシステムは  `distrobox` をプリインストールしており、Fedoraは "Atomic Desktops" に `toolbx` をプリインストールしています。`distrobox`  は簡単なグラフィカル統合が可能ですが、`toolbx` の場合は自分でデスクトップエントリを追加する必要があります。`distrobox` の方がより多くの利用可能なオプションを表示しますが、`distrobox` と `toolbx` の両方ですべての利用可能なシステムイメージを使用できます。

{{<rich-content-end >}}

{{<rich-box-end >}}

distroboxをセットアップ方法、例えばOpenSUSE Tumbleweedを使用する場合:
 
```
distrobox-create box -i registry.opensuse.org/opensuse/toolbox:latest

distrobox-enter box
sudo zypper in qgis
distrobox-export --app qgis qgis-plugin-grass
```
distrobox内のQGISを更新するには:
```
distrobox upgrade --all
```
toolbxを作成するには:
```
toolbox create box -i registry.fedoraproject.org/fedora-toolbox:rawhide

toolbox enter box
sudo dnf install qgis qgis-grass python3-qgis
```
toolbx内のQGISを更新するには:
```
toolbx run -c box sudo dnf update
```
# Mac OS X / macOS
## バイナリパッケージ (installers)
macOS用の公式オールインワン、署名・公証済みインストーラーは  [QGIS download page]({{< ref "download" >}}) からダウンロードできます。これらは、Intel x64およびAppleシリコン（ARM）デバイスのHigh Sierra（10.14）以降に対応しています。

QGISをダウンロードしたら、DMGファイルを開きます。QGISアプリケーションをアプリケーションフォルダにドラッグ＆ドロップします。
| リリース | バージョン | パッケージ | 代替手段 |
| --- | --- | --- | --- |
| 最新のリリース | {{< param "release" >}} {{< param "codename" >}} | [Installer]({{< param "lr_dmg" >}}) [Checksum]({{< param "lr_dmg_sha" >}}) | [Torrent]({{< param "lr_dmg_torrent" >}}) [Magnet]({{< param "lr_dmg_magnet" >}}) [Metalink]({{< param "lr_dmg_meta4" >}}) |
| 長期サポートリリース | {{< param "ltrrelease" >}} {{< param "ltrcodename" >}} {{< param "ltrnote" >}} | [Installer]({{< param "ltr_dmg" >}}) [Checksum]({{< param "ltr_dmg_sha" >}}) | [Torrent]({{< param "ltr_dmg_torrent" >}}) [Magnet]({{< param "ltr_dmg_magnet" >}}) [Metalink]({{< param "ltr_dmg_meta4" >}}) |

## MacPorts
パッケージ管理システム [MacPorts](https://www.macports.org) では、最新リリース版 (port `qgis3`) と長期サポート版 (port `qgis3-ltr`) の両方を提供しています。これにより、Intel x64またはApple Silicon のネイティブアーキテクチャでQGISがインストールされます。GDAL、PDAL、GRASS GISなどの主要な依存ソフトウェアは通常、利用可能な最新バージョンが使用されます。

[MacPorts のインストールと更新](https://guide.macports.org) 、および ports の操作は ターミナル から行います。QGISはアプリバンドルとして  `/Applications/MacPorts/QGIS3.app`  にインストールされます。

ポートの情報取得:
```
sudo port info qgis3
```
ポートのインストール, e.g with GRASS GIS:
```
sudo port install qgis3 +grass
```
更新:
```
sudo port selfupdate
sudo port upgrade outdated
```
{{<rich-box-start icon="👩‍💻" layoutClass="tips" >}}

{{<rich-content-start themeClass="coloring-1" >}}
##### Note
HomebrewとMacPortsの同時インストールは互換性がなく、ほぼ確実に競合を引き起こします。どちらかのパッケージシステムをインストールする場合は、もう片方をアンインストールする必要があります。

{{<rich-content-end >}}

{{<rich-box-end >}}
## 古いリリース
以前のリリースの公式インストーラーは、 https://qgis.org/downloads/macos/ からダウンロードできます。

以前のリリースの kyngchaos インストーラーは https://www.kyngchaos.com/software/archive/qgis/ からダウンロードできます。最も古いインストーラーはmacOS 10.4 Tigerをサポートしています。
# FreeBSD
## QGIS安定版
バイナリパッケージタイプからQGISをインストールする
```
pkg install qgis
```
または、コンパイルオプションをカスタマイズしたい場合は、FreeBSD portsからビルドすることもできます。
```
cd /usr/ports/graphics/qgis
make install clean
```
## QGIS LTR
バイナリパッケージタイプからQGISをインストールする
```
pkg install qgis-ltr
```
または、コンパイルオプションをカスタマイズしたい場合は、FreeBSD portsからビルドすることもできます。
```
cd /usr/ports/graphics/qgis-ltr
make install clean
```
# OpenBSD
QGIS Stable

サードパーティパッケージからQGISをインストールする
```
pkg_add qgis
```
参照:
- https://openbsd.app/?search=qgis for -stable OpenBSD
- https://openbsd.app/?search=qgis&current=on for -current OpenBSD

# コンテナイメージ
実験的な（GPUアクセラレーション対応）マルチアーキテクチャ JupyterLab QGISコンテナイメージ。
- 現在の `os/arch`: `linux/amd64`, `linux/arm64/v8`
  - [Docker Desktop](https://www.docker.com/products/docker-desktop/) を使用したApple Mシリーズでの実行
  - または [Podman Desktop](https://podman-desktop.io) を使用して（ルートレスモード）。
- ベースイメージ [Debian](https://hub.docker.com/_/debian) と [Ubuntu](https://hub.docker.com/_/ubuntu)
  - GPUアクセラレーション対応イメージは [CUDA](https://hub.docker.com/r/nvidia/cuda)-ベース (Ubuntu) です。
- [TurboVNC](https://turbovnc.org): High-speed VNC バージョン
  - OpenGLアプリケーションを高速化するために [VirtualGL](https://virtualgl.org) を実行するCUDAベースのイメージ。
- Just Python – no [Conda](https://github.com/conda/conda) / [Mamba](https://github.com/mamba-org/mamba)

{{<rich-box-start icon="🧑‍💻" layoutClass="tips" >}}

{{<rich-content-start themeClass="coloring-1" >}}
##### Note
The `linux/arm64/v8` JupyterLab QGIS container images are known to crash randomly on Apple M series.

GPU acceleration requires an NVIDIA GPU, the NVIDIA Linux driver and the NVIDIA Container Toolkit.

{{<rich-content-end >}}

{{<rich-box-end >}}

For further information, see <https://github.com/b-data/jupyterlab-qgis-docker-stack>.
## QGIS安定版
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
## QGISバージョン
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
# QGIS テスト版に関する警告
{{<rich-box-start icon="⚠️" layoutClass="tips" >}}

{{<rich-content-start themeClass="coloring-6" >}}
##### 警告
QGISテストパッケージは、安定版QGISに加えて一部のプラットフォーム向けに提供されています。QGISテスト版には、現在開発中の未リリースのソフトウェアが含まれています。これらはアーリーアダプター向けに、バグが修正されているか、また新たなバグが混入していないかを確認するためのテスト目的のみで提供されています。問題が発生しないよう注意を払っていますが、いかなる時点においても正常に動作しない場合や、データに悪影響を及ぼす可能性があります。ご注意ください。警告しました！

{{<rich-content-end >}}

{{<rich-box-end >}}
# ソースからインストールする
サポートしている各プラットフォームでのQGISのソースからのビルドおよびインストール方法については、 [開発者向けインストールノート](https://github.com/qgis/QGIS/blob/master/INSTALL.md) を参照してください。

{{<content-end >}}
