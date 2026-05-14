---
HasBanner: false
archived: true
date: 2011-01-01
draft: false
featured: false
section: project
sidebar: true
thumbnail: images/australia_queens1.jpg
title: 地方政府の森林火災ハザードマップでのQGISとGRASS
type: case-study

---
{{<content-start >}}
# 地方政府の森林火災ハザードマップでのQGISとGRASS
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>January 01, 2011</span>
</p>

## 前書き
南ダウンズ広域行政機関（SDRC）は南東クイーンズランド、オーストラリアの中小地方政府です。協議会地域、主に南部では、主要な山火事に苦しんでいます。山火事は南ダウンズ地域の住民や土地所有者のための現実と存在関心事である、そして生命と財産の損失をもたらしました。

このプロジェクトによって、行政機関およびこの地域の人々がリスクをより意識できるようになり、将来のより良い意思決定ができます。

![](../images/australia_queens1.jpg)
## プロジェクト
As bushfire is not only a problem for SDRC but also for the whole of Queensland, the state government requires that each local government identifies the bushfire hazard in their area via the State Planning Policy 1/03 Mitigating the Adverse Impacts of Flood, Bushfire and Landslide \[1\]. This kind of job would normally be done using consultants but was instead done by the council itself using a combination of QGIS and GRASS.

プロジェクトの GIS側は主に6つのステップに分けられます
- 傾斜の評価と図化
- 斜面方向の評価と図化
- 植生の評価と図化
- 山火事の危険の重大度を識別するためのスコアを組み合わせます
- フィールドの検証および定性的評価
- 最終的な地図

## QGISとGRASSの使用
![](../images/australia_queens2.jpg)

QGIS, using the GRASS plugin, was selected as it provided the tools needed to complete the job and the interaction between QGIS and GRASS made it easy to process the raster maps and present them in a meaningful way to users. SDRC uses MapInfo for its main GIS system, however MapInfo's addons were not as powerful as GRASS GIS for raster processing.

QGIS GRASSプラグインは次いでr.surf.contourを用いて等高線ラスター地図に変換したGRASSに全領域の5メートルの等高線をインポートするために使用されました。傾斜方向図は、次に、ラスター等高線図からr.slope.aspectを用いて作製しました。カテゴリは、異なる傾斜および斜面方向範囲に割り当てられ、ハザードリスクスコアを与えました。植生領域も異なるリスクスコアを与えられました。すべての得られたラスター地図は次いでmapcalcを使用して結合し、最終的なリスクの危険スコアを与えました。それからリスクスコアは次の3つの主なカテゴリーに分けられます：高・中・低。

プロセスの最後の部分は地方消防サービスを通じての現場検証でした。レビュープロセスの後、QGISが、プレゼンテーションのための最終的な地図を印刷するのに使用されました。

すべてのGRASSのコマンドはコマンドラインから実行できるので、山火事のハザードマップを生成するのに必要とされたすべてのコマンドは、文書化のためおよび将来いつかの時に地図を再作成するために必要な場合のために、記録されました。
## 結論
全体的にQGIS、一緒にGRASSプラグインで、素晴らしい経験と、自分の山火事ハザードマップ作成を行う協議会のための偉大な最終的な結果を提供します。GRASSプラグインはQGISを通じてGRASSへのインターフェイスを非常に使いやすいを提供します。QGISではGRASSラスター形式をネイティブに開けるため、統合は非常にシームレスで、地図を容易に作成できます。

The project won an encouragement award at the Queensland Planning Institute of Australia state planning awards in 2010 \[2\]
## リファレンス
- \[1\] <http://www.emergency.qld.gov.au/publications/spp/>
- \[2\] <http://digital.crowtherblayne.com.au/default.aspx?xml=crowther_pia.xml>

## 著者
<figure>
<img src="../images/australia_queensaut.jpg" class="align-left" height="200" alt="australia_queensaut.jpg" />
<figcaption>Nathan Woodrow</figcaption>
</figure>

この記事は、ネイサン・ウッドローにより、2011年1月に寄稿されました。ネイサンは南ダウンズ地域協議会でのGISの役員であり、サウザークイーンズランド大学の空間科学の準学士で勉強中です

{{<content-end >}}
