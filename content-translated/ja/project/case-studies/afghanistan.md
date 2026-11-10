---
HasBanner: false
archived: false
date: 2015-04-01
draft: false
featured: false
section: project
sidebar: true
thumbnail: images/afghanistan1.png
title: アフガニスタンでQGISを使用するデンマークの地雷除去グループ
type: case-study

---
{{<content-start >}}
# アフガニスタンでQGISを使用するデンマークの地雷除去グループ
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>2015年4月1日</span>
</p>

デンマーク難民評議会の専門地雷対策ユニットであるデンマーク地雷除去グループ（DDG）は、1999年以来アフガニスタンで活動しており、人道的地雷除去、不発弾（UXO）処分、地雷回避教育を担当しています。DDGアフガニスタンは人道的地雷対策を実施することにより、人命を救い、リスク教育を通じて安全の感覚を強化し、資源の生産的な活用を妨げる障害の除去を支援しており、アフガニスタン開発の潜在能力の実現に役立っています。DDGは、アフガニスタンでの活動開始以来24,000個以上の地雷と94万発以上の不発弾を除去してきました。現在、DDGは北部地方のバルフとサマンガーン、中央地方のカブール、パルヴァーン、パンジシールで活動しています。

アフガニスタンでは、地雷除去活動はアフガニスタン地雷対策調整センター（MACCA）を通して調整されています。この団体では既知の危険（地雷原、戦場、「スポット」UXOタスク）の地理空間情報を収集、配布し、除去の進捗に応じてこの情報を更新しています。これらの「ハザードポリゴン」の新しいシェープファイルは定期的にMACCAによって発行され、地雷除去団体は活動領域における地雷除去の状況を評価するためにこれを使用することができます。DDGでは、過去に使用してきた高価な商用ソフトウェアを置き換えるために、組織内でのQGISの使用を試しています。

<figure>
<img src="../images/afghanistan1.png" class="align-right" alt="afghanistan1.png" />
<figcaption>数値標高モデルは、DDGが地雷原の場所に関して当たりを付けることに役立っています</figcaption>
</figure>

地理空間データの使用は計画や調査段階で最も有用です。アフガニスタンでは、セキュリティ上の問題や険しい地形が知られているサイトの物理的な再調査は必ずしも容易ではないことを意味します。代わりに、データの混合物（衛星や航空写真の下敷き、デジタイズされたソ連時代の地形図、ハザードシェープファイルと数値標高モデル）を使用することで、DDGでは、測量チームを送りこむ前に、地形と周辺の自然および物理的地物との関係で地雷原の場所の当りを付けることができます。QGISのプラグインは3Dで地形を可視化する機能など、便利な機能を追加します。上記添付のスクリーンショットは、プラグインQgis2threejsを用いて作製したものですが、カブールのダルラマン宮殿のすぐ南の領域を示していて、SRTMデータと組み合わせたソビエト地形ラスタレイヤ上にアクティブ地雷原が（左の稜線に沿って）赤色で表示されています。すでに除去された地雷原は明緑色で表示されています。

<figure>
<img src="../images/afghanistan2.jpg" class="align-right" alt="afghanistan2.jpg" />
<figcaption>未除去の危険区域は赤で示されており、すでに除去された危険区域は明るい緑色で示されています。</figcaption>
</figure>

Kabul University's campus is still contaminated with suspected hazardous areas — thought to comprise of air-dropped bombs or similar ordnance. While not posing any immediate threat to students or staff, these hazards will require eventual clearance to allow future construction within an educational institution vital to Afghanistan's future development. The hazards are also notable as among the last significant remaining hazardous areas in the Kabul metropolitan area. By using QGIS to combine the hazard polygons from earlier surveys with highly accurate aerial photography provided by the USGS, discrepancies can be noted — e.g. where the polygons do not match the shape of the buildings, as evident in the northwest part of the campus —— which can direct survey teams to places to first conduct a more accurate re-survey.

またQGISは、携帯式のGarmin GPSを使った野外活動にて収集されたデータと同期し、発見・破壊された地雷の場所で除去地図を作ることを可能にします。

The use of QGIS, along with a renewed interest in data analysis, has spurred new ways of looking at the data available, and combining it with other data sources to better target mineclearance activities. It is also driving improved mapping capabilities within the organisation, and an ability to better communicate the impact of its work to international donors. In a part of the world where 'formal' GIS training is difficult to acquire, the collaborative nature of the QGIS user community is greatly appreciated, as technical problems can often be solved by consulting online forums. In short, QGIS is playing a role in working towards ridding Afghanistan of landmines and UXO.
## リンク
- Danish Demining Group <http://www.danishdemininggroup.dk/>

## 著者
<figure>
<img src="../images/afghanistan3.jpg" class="align-left" height="220" alt="afghanistan3.jpg" />
<figcaption>Edward Crowther</figcaption>
</figure>

エドワード・クラウザーはデンマーク地雷除去グループ・アフガニスタンの副カントリーディレクターです。エドワードはアフガニスタンでDDGに入社する前、アンゴラとスリランカで人道的地雷除去機関HALOトラストと働きました。彼はロンドン大学東洋アフリカ研究学院で開発研究の理学修士を取得しました。

{{<content-end >}}
