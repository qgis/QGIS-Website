---
draft: false
sidebar: true
subtitle: ''
title: FAQ
type: page

---
{{<content-start >}}
# FAQ
よく寄せられる質問への回答をまとめています。
## ユーザーの質問
### ダウンロードの問題
QGISをダウンロードしようとしても何も起こらないようであれば、ブラウザのダウンロードマネージャーを参照してください。ダウンロードマネージャーは通常、ブラウザーの右上にアイコン（矢印、ストップウォッチ、円グラフ）として表示されます。アイコンをクリックすると、ダウンロードの進行状況を確認したり、ダウンロードをキャンセルしたりできます。ブラウザでのダウンロードの通常の手順は、まず（ファイルブラウザのダイアログで）ファイルの保存先を尋ねられ、ダウンロードが完了するまで待つ必要があるというものです。QGISのインストール・パッケージは、オペレーティング・システムによってはかなり大きくなることがあるため、辛抱強く待つ必要があります。ダウンロードサイズは数百メガバイトから時には1ギガバイトを超えることもあります（MS Windows MSIパッケージの場合）。ダウンロード速度やQGISサーバーの負荷にもよりますが、ダウンロードには数分から数時間かかることもあります。
### QGISをダウンロードするには寄附が必要ですか？
これは時々耳にする誤解で、真実ではありません。QGISへの寄付は任意です。QGISをダウンロードすると、オプションでQGISに寄付できることを知らせるメッセージが表示されます。しかし、「このメッセージを閉じる」を押せば、問題なくダウンロードを続けることができます。私たちは、QGISを誰でも、どんな経済状況でも利用できるようにしたいと考えています。初めてQGISを利用される方は、まずQGISをダウンロード、インストール、テストし、解決したいタスクにQGISが役立つかどうかを確認することをお勧めします。そして、QGISが気に入り、あなたのビジネスやタスク、プロセスに大いに役立つようであれば、QGISへの寄付や維持会員としての支援をご検討いただきたい。
### QGISの質問をするには？
[メーリングリスト]({{< ref "community/organisation/mailinglists" >}}) を通じてQGIS関連の質問をしようとしている場合は、問題が何なのかを他の人が簡単に理解するのに十分な情報を提供してください。明確かつ正確でない質問に答えるのは誰にとっても非常に難しいです。あるいは、答えがあなたへの質問になり、・・・となって、時間がかかりすぎます。ご提供していただきたい情報は:
- 電子メールのタイトルは説明的なものが望ましい
- その時点で使用しているQGISバージョン（正確に）
- 何を得ることを期待しているか
- 該当する場合、何を試してみて、得られた結果は何だったか
- 質問が何かが壊れているということについてであれば、以下も提供できます：
  - エラーがまさに何なのか（可能な場合：スクリーンダンプ、スタックトレース、エラーテキストのコピー）
  - どのオペレーティングシステムとバージョンか
  - それをインストールした方法（osgeo4w？スタンドアロンインストーラ？独自のビルド？）
  - それがいつ壊れたか（再インストール新しいインストール、システムの更新、プロジェクトの変更）

ご質問がより精密であるほど、より迅速かつ正確に回答できることに留意してください。

{{<rich-box-start icon="💁" layoutClass="tips" mode="html" >}}

{{<rich-content-start themeClass="coloring-1" >}}
##### 注意
関数が壊れている場合は、リストにメールする前に [QGISイシュートラッカー](https://github.com/qgis/QGIS/issues) を見てください。詳細は [バグ報告]({{< ref "resources/support/bug-reporting" >}}) を参照してください。

{{<rich-content-end >}}

{{<rich-box-end >}}
### QGISのリリース名はどのように選択されていますか？
チューリッヒ（スイス）での成功した開発者会議の後、私たちは次のリリースをそれに関連付けるべきだと決めました。それ以来、すべてのリリースは開発者会議の場所にちなんで名付けられています。
### QGISでECWファイルを開くことはできますか？
ECW is a proprietary file format - please consult their [Licensing Page](https://supportsi.hexagon.com/s/article/License-for-reading-or-writing-ECW-in-third-party-software) to understand how you may use it. Also, please consult the [GDAL documentation](https://gdal.org/en/stable/drivers/raster/ecw.html#creation-options-1) for notes on how to enable licensed features if you have a paid version of ECW. ECW support is not included in all QGIS binary versions and for all platforms by default.

**プラットフォーム固有の注意事項:**

***Windows***: Windows をお使いで、**オフラインインストーラー**（**Windows 向け長期リリース版 ({{< param "ltrversion" >}} {{< param "ltrnote" >}})** および **Windows用最新バージョン ({{< param "version" >}})** と表示されたダウンロードボタンから入手可能）をダウンロードした場合、ECWの読み取りサポートはデフォルトで含まれています。

If you are using the **OSGeo4W Network Installer**, ECW support is installed by default if you use the express install workflow. If manually selecting components, you need to explicitly enable the `gdal-ecw` package in order to ensure that ECW support is included in your installation.

***macOS***: If you are using macOS, you can download the DMG file from [QGIS Downloads](https://qgis.org/download/). This includes ECW support by default.

***Linux***: By default, the QGIS binaries for most Linux distributions *do not* include default ECW support. However, you can find discussions and solutions for adding this support in various resources for guidance.

For Ubuntu, for example, you can check out the following resources:
- [Github - GDAL: How to open ECW Maps in QGIS 3.22](https://github.com/OSGeo/gdal/issues/8239)
- [Reddit - QGIS: Problem loading ECW file in Ubuntu (Linux)](https://www.reddit.com/r/QGIS/comments/icw98f/problem_loading_ecw_file_in_ubuntu_linux/?rdt=54968)
- [GIS Stack Exchange: Installing QGIS with ECW support on ubuntu 20.04](https://gis.stackexchange.com/questions/429214/installing-qgis-with-ecw-support-on-ubuntu-20-04/434980#434980).

### How can I get a VPAT / HECVAT / other US compliance form or information?
Please get in touch with the US User group. They are looking into these topics. More info and contact details: https://www.qgis-us.org
## 開発者の質問
### QGISを自分でコンパイルできますか？
はい。あなたがどんなOS (Windows, macOS, Linux)を使っていてもQGISをソースからコンパイルすることができます。[ソースからQGISをビルドする](https://github.com/qgis/QGIS/blob/master/INSTALL.md) をお読みください。
## Citation information
### どのようにQGISを引用するのですか？
作品の中や業務のためにQGISを引用する必要がある場合は、最も役立つ引用スタイルを使用してください:

Here are some choices to cite the overall QGIS software project, a specific QGIS version being used used, or QGIS documentation to allow reproducibility:

**The QGIS project as an evolving software project, independent of a specific software release, by Digital Object Identifier (concept DOI)**

Use the concept DOI [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6139224.svg)](https://doi.org/10.5281/zenodo.6139224) when
- referring to the QGIS software in general (e.g., in introductions or background sections)
- describing workflows where the exact version is not critical
- citing QGIS as a long-term research tool or infrastructure

The concept DOI will always resolve to the latest version of QGIS and provide a stable reference to the software project over time.

**Specific QGIS software releases by Digital Object Identifier (version DOI)**

Each QGIS release since release 3.22.4 (2022) has its own version DOI identifying a precise, archived snapshot of the software (e.g., a specific software release). All version DOI are linked to the concept DOI of the QGIS project.

Please refer to the QGIS Zenodo Landing Page ([QGIS Zenodo Landing Page](https://zenodo.org/search?q=parent.id%3A6139224&f=allversions%3Atrue&l=list&p=1&s=10&sort=version)) for all specific version DOI.
- QGIS 4.0.0 [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18889261.svg)](https://doi.org/10.5281/zenodo.18889261)
- QGIS 3.44 LTR [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15705458.svg)](https://doi.org/10.5281/zenodo.15705458)

**一般的にQGISプロジェクトを引用する**

QGIS.org, {{< yeartag >}}. QGIS Geographic Information System. QGIS Association. http://www.qgis.org

**QGIS開発者マニュアルを引用する**

QGIS.org, {{< yeartag >}}. QGIS {{< param "ltrversion" >}}. Geographic Information System Developers Manual. QGIS Association. Electronic document: {{< param-link "devcite" >}}

**QGISインストールガイドを引用する**

QGIS.org, {{< yeartag >}}. QGIS {{< param "ltrversion" >}}. Geographic Information System Installation Guide. QGIS Association. Electronic document: https://github.com/qgis/QGIS/blob/master/INSTALL.md

**QGISユーザーガイドを引用する**

QGIS.org, {{< yeartag >}}. QGIS {{< param "ltrversion" >}}. Geographic Information System User Guide. QGIS Association. Electronic document: {{< param-link "userguidecite" >}}

**QGIS Serverドキュメントを引用する**

QGIS.org, {{< yeartag >}}. QGIS {{< param "ltrversion" >}}. Geographic Information System API Documentation. QGIS Association. Electronic document: {{< param-link "servercite" >}}

**QGIS APIドキュメントを引用する**

QGIS.org, {{< yeartag >}}. QGIS {{< param "ltrversion" >}}. Geographic Information System API Documentation. QGIS Association. Electronic document: {{< param-link "apicite" >}}

**望ましい形式:** [BibTeX](https://en.wikipedia.org/wiki/BibTeX)

BibTeXエントリの例:
```
@Manual{QGIS_software,
  title = {QGIS Geographic Information System},
  author = {{QGIS Development Team}},
  organization = {QGIS Association},
  year = {{{< yeartag >}}},
  url = {https://www.qgis.org},
}
```
**QGISペーパーをPatterns誌で引用する**
```
@article{graser2025,
  title = {The QGIS project: Spatial without compromise},
  journal = {Patterns},
  volume = {6},
  number = {7},
  pages = {101265},
  year = {2025},
  issn = {2666-3899},
  doi = {https://doi.org/10.1016/j.patter.2025.101265},
  url = {https://www.sciencedirect.com/science/article/pii/S2666389925001138},
  author = {Anita Graser and Tim Sutton and Marco Bernasocchi}
}
```
### QGISで地図を作成したのですが、QGISについて言及する必要はありますか？
QGISで作成された地図についてそれを言及する必要はありません。もちろん、地図がQGISで作成されたというメモを追加したい場合は大歓迎です。 「QGISで作成」または「当地図はフリーかつオープンソースのQGISを使用して作成されました」はそのようなメモの良い例です。

{{<rich-box-start icon="✋" layoutClass="tips" >}}

{{<rich-content-start themeClass="coloring-1" >}}
##### 注意
QGISはあなたの作品の著作権を保有しないため、©QGISとは記載しないでください。

{{<rich-content-end >}}

{{<rich-box-end >}}

{{<content-end >}}
