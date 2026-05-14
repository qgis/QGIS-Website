---
HasBanner: false
archived: true
date: 2012-07-01
draft: false
featured: false
section: project
sidebar: true
thumbnail: images/portugal_ribeira1.png
title: 北ポルトガルのオオカミの生態系回廊をモデル化するためのQGISとGRASS
type: case-study

---
{{<content-start >}}
# 北ポルトガルのオオカミの生態系回廊をモデル化するためのQGISとGRASS
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>July 01, 2012</span>
</p>

The Iberian wolf is a sub-species of the gray wolf that exists only in north of Portugal and Spain, with small isolated groups in the south of Douro river. During the last century, it suffered a high regression, being a "vulnerable" species in Spain and "endangered" in Portugal. Nowadays, there are only around 300 wolves in Portugal, due to the high persecution, destruction and fragmentation of the habitat.

<figure>
<img src="../images/portugal_ribeira1.png" class="align-right" alt="portugal_ribeira1.png" />
<figcaption>Study area in Portugal</figcaption>
</figure>

リベイラ・デ・ペーニャは、ポルトガル北部のヴィラレアル地区の自治体です。これは、オオカミのための避難所及び食品を提供する低密度ヒトとともに、農業、放牧畜産、森林、山、谷及び多様な動物相によって特徴付け農村自治体、、です。リベイラデペナは、過酷な山岳トラスオスモンテスと緑豊かなミーニョの間の遷移ゾーンに位置し、北の高い狼濃度と南の低い濃度の領域間の生態学的回廊のように機能しうる自治体の一つです。

私は生物学の課程中にGISソフトウェアを使用し始め、修士論文中はより頻繁に使用しました。その時は主に商用ソフトウェアを使用していましたが、修士課程終了後、商用ソフトウェアへのアクセス権を失いました。

その間に、私はLinuxの新しい世界に入りました。その後で私は、リベイラ・デペーニャでオオカミのための生態回廊をGISを使用してモデル化するのを支援するため何人かの研究者に連絡をとりました。彼らはこの種のソフトウェアで作業したことがなかったからです。私はすでにWindowsではなくLinuxを使用していたので、私の最初の問題はどのソフトウェアを使用するかでした。それから私はQGISの話を聞き、すでに知っていたものに比較すると、それは非常に単純かつ不完全に見えたが、それを試してみることにしました。すぐに私がいかに間違っていたかに気づき、QGIS提供の分析能力、特にGRASSの統合、に本当に大信者になりました。

生態回廊をモデル化するために、私たちは、GRASSプラグインと一緒にQGISを使用しました。私たちは、生態回廊をモデル化するために種の存在データとともに、いくつかの地理情報を使用していました。ここではほんの数に名前を付けるために、QGISこの場合に使用さGRASSの両方の機能の一部を以下に示します。
- QGISでのプラグインの補間：デジタル標高モデルを作成する
- GRASSのr.watershed：DEMから水の流れを作り出す
- GRASSのr.grow.distance：入力レイヤーの地物までの距離のラスター地図レイヤーを生成する
- GRASSのr.reclass：地図レイヤーの再分類
- GRASSのr.slope.aspect.slope：DEMからの勾配を計算する
- GRASSのr.mapcalculator：単純なマップ代数を計算する
- GRASSでr.cost.coord：そのセルカテゴリ値の入力ラスター地図上の地理的に異なる場所間の移動の累積コストを示すラスター地図を作成するコストを表します
- r.drain in GRASS: Traces a flow through an elevation model on a raster map — the one used to create the corridors

この作品で、私たちは、リベイラデペーナの自治体でオオカミのための潜在的な生態回廊で地図を得ました。これらは、種のための保全対策を計画する際に市議会の技術者によって考慮される分野です。彼らははるかに安定ペネダ・ジェレスとスペインからのものと連続している北部のもの、と南にヴィラレアルで脆弱なオオカミパックを接続することができますので、これらの回廊は非常に重要です。それは小さな村、都市や道路のように、特定の重要性から、人間の居住地を横断し、それらの回廊です。これらの領域は、オオカミの保全のための重要と考えられており、この種のヒトへの影響を軽減するための措置を適用する必要があります。

<figure>
<img src="../images/portugal_ribeira2.png" class="align-right" style="width:100.0%" alt="portugal_ribeira2.png" />
<figcaption>Ecological corridors and critical conservation areas for wolves in northern Portugal.</figcaption>
</figure>

## 結論
Both QGIS and plugin GRASS are very intuitive with user-friendly interface, with all essential functions to perform most analysis. For what I could see, QGIS and GRASS perform equally as well as the proprietary programs I was most familiar with from college days, with the big advantage of free open-source software, usable in every computer or notebook without licenses, constant upgrades and the ultimate advantage to contribute to it\'s improvement and/or tip the developers about some essential function.

Changing to Linux and then to QGIS and GRASS was one of my best calls, and although there can be some missing issues, easily resolved in the future with the developers, I don\'t regret my decision and advise everyone to use them.
## 著者
<figure>
<img src="../images/portugal_ribeiraaut.png" class="align-left" height="200" alt="portugal_ribeiraaut.png" />
<figcaption>Monica Almeida</figcaption>
</figure>

この記事は、モニカ・アルメイダによって2012年7月に寄稿されました。彼女はポルトガルで狼の保全に非政府組織で働く保全生物学者です。

{{<content-end >}}
