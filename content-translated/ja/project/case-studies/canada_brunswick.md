---
HasBanner: false
archived: true
date: 2013-01-01
draft: false
featured: false
section: project
sidebar: true
thumbnail: images/canada_brunswick1.jpg
title: QGISでファンディ小径トレイルマップの作成
type: case-study

---
{{<content-start >}}
# QGISでファンディ小径トレイルマップの作成
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>January 01, 2013</span>
</p>

![](../images/canada_brunswick1.jpg)

The Fundy Footpath is a wilderness hiking trail located along the Fundy coast of New Brunswick, Canada. It is a charter member of the [UNESCO Fundy Biosphere Reserve](http://fundy-biosphere.ca/en/about-us/the-reserve) and affiliated with the [NB Trails Council Inc.](http://www.sentiernbtrail.com/) and the Trans Canada Trail. The Footpath takes hikers through the coastal Acadian Forest, home to the world's highest tides, old growth forests, and several rare and unique types of flora and fauna.

トレイルはファンディハイキングトレイル協会（FHTA）（1975）として知られているボランティアのグループによって作成、維持、および促進されます。非営利組織としてFHTAはトレイル地図が含まれるガイドブックの販売を通じて、その活動のための資金を調達しています。2011年に私は、公式のトレイル地図を更新するためにボランティアをFHTAに近づきました。非営利団体のための地図を作成するボランティアとしてQGISは、編集データの両方のツールとして、最終的な地図レイアウトのための法案をフィット。ファンディ小道の新しい公式地図はガイドブックに含まれて自分自身とFHTAのメンバーの努力を通じて、最初から最後までQGISで作成されました。

<figure>
<img src="../images/canada_brunswick2.jpg" class="align-right" alt="canada_brunswick2.jpg" />
<figcaption>QGIS GPS Tools Plugin for data collection</figcaption>
</figure>

## プロジェクト
QGISで新しいファンディ小径地図を作成するプロセスは、3つの異なる部分に分けることができます。
- データ収集。
- データ編集と準備。
- 地図制作。

Data was collected both with handheld GPS units and from various free data sources. Trail data (e.g. trail centerline, campsite locations, and tidal crossings) was collected with a Garmin GPSMap 60CSX. This data was then transferred from the GPS and to shapefile format in QGIS using the GPS plugin. Free data in vector formats was then obtained from the [Natural Resources Canada (NRCan) CanVec](http://geogratis.cgdi.gc.ca/geogratis/en/product/search.do?id=5460AA9D-54CD-8349-C95E-1A4D03172FDF) website and from [Service New Brunswick (SNB) online](http://www.snb.ca/gdam-igec/e/2900e_1.asp).

<figure>
<img src="../images/canada_brunswick3.jpg" class="align-right" alt="canada_brunswick3.jpg" />
<figcaption>Creation of the footpath map in QGIS</figcaption>
</figure>

最終地図製品で使用するためのデータを準備するため、QGIS内の以下のツールが特定のタスクを達成するために使用されました：
- GPSで収集されたデータは、編集ツールバーを使用して洗浄しました。
- NRCanとSNBから得られたベクターデータは、マージ照会、およびベクターツールを使用して、最終的な地図領域に対してクリップされました。
- SNBから得られたカンマ区切りファイルが追加区切りテキストレイヤープラグインを使用して点レイヤーとしてQGISにインポートし、補間プラグインは次いでGDALラスターツールプラグインと陰影起伏ラスターと標高等高線レイヤーを作成するために使用された標高ラスターを作成するために使用されました。

<figure>
<img src="../images/canada_brunswick4.jpg" class="align-right" alt="canada_brunswick4.jpg" />
<figcaption>Footpath map in the Print Composer</figcaption>
</figure>

Once the data required to create the map was assembled and in a usable format the creation of the final map was started. To create the hiking map data was symbolized and labeled with the symbolization properties dialog and labeled with QGIS's very functional label engine. Once labels and symbolization were in place the map composer tool was run to create the layout. It was very easy to add useful map elements such as a custom north arrow and elevation profile in the print composer. Two layouts were created since it was to be a double-sided map. Once both layouts were created they were exported as PDF files and sent to the printers.
## 結論
The hiking map was printed on heavy-duty waterproof paper, folded and inserted in the back of the new edition of the Fundy Footpath Hiker's Guide Book. QGIS was the best and most functional choice for the creation of this map. Being free software the price was right for a volunteer creating a map for a non-profit organization. But the real advantage of QGIS was that it had all of the functionality and tools required to create a highly useful and detailed hiking map from start to finish. I would highly recommend QGIS to both experienced and beginning GIS users alike.

<figure>
<img src="../images/canada_brunswick5.jpg" class="align-right" alt="canada_brunswick5.jpg" />
<figcaption>The final Fundy Footpath map with accompanying guidebook</figcaption>
</figure>

## リンク
- <http://fundy-biosphere.ca/en/about-us/the-reserve>
- <http://www.sentiernbtrail.com>
- <http://www.snb.ca/gdam-igec/e/2900e_1.asp>

## 著者
<figure>
<img src="../images/canada_brunswickaut.jpg" class="align-left" height="200" alt="canada_brunswickaut.jpg" />
<figcaption>Jarrett Totton</figcaption>
</figure>

この記事は、2013年に1月ジャレット・トットンによって寄稿されました。ジャレットは、カナダのアルバータ州在住のGIS技術者です。

{{<content-end >}}
