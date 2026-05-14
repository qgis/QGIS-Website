---
HasBanner: false
archived: true
date: 2014-05-01
draft: false
featured: false
section: project
sidebar: true
thumbnail: images/india_pune1.png
title: WMSからオフラインマップを作成するためのPythonコンソールの使用（タイルダウンローダ）
type: case-study

---
{{<content-start >}}
# WMSからオフラインマップを作成するためのPythonコンソールの使用（タイルダウンローダ）
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>May 01, 2014</span>
</p>

この研究は、WMS / WFSやPythonコンソールのスクリプトの助けを借りて、タイルをダウンロードすることにより、QGISマップビューにロードされた任意の地図からオフライン地図を準備する方法について説明します。skriptは、さらなる使用のためにすべてのタイルのモザイクを生成します。

Webマッピングサービス（WMS）サービスを通じて、ラスター/ベクター地図にアクセスすることは非常に一般的かつ効率的です。それは、セキュリティ、集中管理、柔軟な地図スタイルなどのいくつかの利点を有しています。例では、グーグルマップ、ヤフー、ビング、MODIS、ランドサット、NASAによる公開地図、NRSC（インド）です。WMSの欠点/制限は、インターネットやイントラネットを経由して動作することです。特に調査中の現場で、常にインターネット接続を取得できないことがあります。またWMSは、IMGなどのGeoTiff、JPG、などの何らかのオフライン画像フォーマットに比べると、動作が遅いです。
## QGISの使用
QGIS provides a tool to connect/access any WMS service. WMS connection is based on simple URL and once connection is established map can be seen on QGIS mapview. If we save the map of visible extent from QGIS mapview as jpg (File \> Save as Image) it creates world file which has the geographic coordinate information of particular region E.g. sample.jpg is the map and sample.jpgw have the coordinates. That means the downloaded image is georeferenced. We can download tiles in grid format manually and use later offline. Manual downloading is possible if the area is very small or low resolution images are fine.

<figure>
<img src="../images/india_pune1.png" class="align-left" alt="india_pune1.png" />
<figcaption>QGIS with WMS tiles</figcaption>
</figure>

## Pythonコンソール
A short script was written in "Python Console" with help available on QGIS official website in PyQGIS Developer Cookbook. Script consists of basically 4 components as following,
1. 最初のタイルのX、Y座標（左上と右下）
2. ダウンロードするタイルのサイズ（0.001 X 0.001など）
3. ダウンロードするタイルのNO（地図の全範囲とタイルのサイズに基づいて計算されます）
4. 出力タイル/ファイルを格納する出力ディレクトリ

The script works in two simple for loops first which defines the extent of map in QGIS map view and run row/columns. Once the map extent is set then map is loaded in QGIS. The delay of 3 seconds (depends on internet connection) was introduced before saving map as jpg in user defined directory. Once the script is executed all the tiles created in directory can be directly loaded in QGIS or single mosaic is prepared from Raster \> Miscellaneous \> Merge or Build Virtual Raster (Catalog). Both tools generates mosaic but basic difference in Merge creates an image independent of tiles whereas Virtual raster generates a link in all individual tiles (tiles are required).

<figure>
<img src="../images/india_pune2.png" class="align-left" alt="india_pune2.png" />
<figcaption>Python script and directory where tiles are stored</figcaption>
</figure>

この方法には、サーバー側での地図での変更がオフライン（ダウンロードした地図）には反映されないという限界があります。この場合、ユーザーは、プロセスを繰り返し、新しいオフライン地図を生成する必要があります。第2の限界は、作成されるオフライン地図が画像形式となることです。それは、主題図や画像の分類には使用できません。いくつかの土地利用図は、いくつかの余分な努力といくつかのデータ損失でベクターに変換できます。
## 適用範囲
生成されたモザイクは、それが主題図（7-8色）からダウンロードされても、純粋な画像です。再分類のような事前のツールを使用して、このラスタースタッキングレイヤー/バンドポリゴンベクターに変換できます。WMSはgetgeatureinfoを使用してこのようなgetfeatureinfo等は、GetCapabilities、GetMapリクエスト、などのいくつかの要求を取得でき、各ポリゴンの属性情報を有しています。スクリプト知識がなくても誰でも、スクリプトを使用できるようになりますように、スクリプトはプラグインに変換できます。
## 結論
上記の経験は、QGISを任意の高度なレベルで使用できることを示しています。基本的なプログラミングのスキルがあれば、小さなスクリプトやプラグインを書くことで、仕事の質を向上させ時間を節約できます。QGISの中で、世界的に開発されたプラグインのリポジトリへアクセスできることは、QGISの最高です。PyQGIS開発者クックブックは、スクリプトを書くための素晴らしいリソースであり、ラスタデータ処理はGDALツールの助けで今ははるかに簡単です。
## 著者
この記事はPrashant Kadgiによって2014年5月寄稿されました。氏はプネ（インド）を拠点に、現在、GIS APPコンサルティングサービスでコンサルタントとして働いています。2009年以来NRM、林業、電子政府、インドと世界のさまざまな地域でのソフトウェア開発プロジェクトでGIS＆RSを使用しています。
- Contact: <kadgiprashant@gmail.com>
- ウェブサイトwww.gisappco.com（建設中）

{{<content-end >}}
