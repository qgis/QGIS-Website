---
author: Edward Crowther
categories:
- ケーススタディ
date: '2015-04-01'
description: The Danish Demining Group (DDG), the specialised mine action unit of
  the Danish Refugee Council, has been working in Afghanistan since 1999, undertaking
  humanitarian mineclearance, unexploded ordnance (UXO) disposal and mine risk education.
draft: 'true'
heroImage: ''
tags:
- humanitarian
- afghanistan
- ケーススタディ
- ショーケース
thumbnail: afghanistan3.jpg
title: アフガニスタンでQGISを使用するデンマークの地雷除去グループ
type: showcase/case-studies

---
{{<content-start classes="notification is-light" >}}

デンマーク難民評議会の専門地雷対策ユニットであるデンマーク地雷除去グループ（DDG）は、1999年以来アフガニスタンで活動しており、人道的地雷除去、不発弾（UXO）処分、地雷回避教育を担当しています。DDGアフガニスタンは人道的地雷対策を実施することにより、人命を救い、リスク教育を通じて安全の感覚を強化し、資源の生産的な活用を妨げる障害の除去を支援しており、アフガニスタン開発の潜在能力の実現に役立っています。DDGは、アフガニスタンでの活動開始以来24,000個以上の地雷と94万発以上の不発弾を除去してきました。現在、DDGは北部地方のバルフとサマンガーン、中央地方のカブール、パルヴァーン、パンジシールで活動しています。

アフガニスタンでは、地雷除去活動はアフガニスタン地雷対策調整センター（MACCA）を通して調整されています。この団体では既知の危険（地雷原、戦場、「スポット」UXOタスク）の地理空間情報を収集、配布し、除去の進捗に応じてこの情報を更新しています。これらの「ハザードポリゴン」の新しいシェープファイルは定期的にMACCAによって発行され、地雷除去団体は活動領域における地雷除去の状況を評価するためにこれを使用することができます。DDGでは、過去に使用してきた高価な商用ソフトウェアを置き換えるために、組織内でのQGISの使用を試しています。

![数値標高モデルは、DDGが地雷原の場所に関して当たりを付けることに役立っています](afghanistan1.png)

地理空間データの使用は計画や調査段階で最も有用です。アフガニスタンでは、セキュリティ上の問題や険しい地形が知られているサイトの物理的な再調査は必ずしも容易ではないことを意味します。代わりに、データの混合物（衛星や航空写真の下敷き、デジタイズされたソ連時代の地形図、ハザードシェープファイルと数値標高モデル）を使用することで、DDGでは、測量チームを送りこむ前に、地形と周辺の自然および物理的地物との関係で地雷原の場所の当りを付けることができます。QGISのプラグインは3Dで地形を可視化する機能など、便利な機能を追加します。上記添付のスクリーンショットは、プラグインQgis2threejsを用いて作製したものですが、カブールのダルラマン宮殿のすぐ南の領域を示していて、SRTMデータと組み合わせたソビエト地形ラスタレイヤ上にアクティブ地雷原が（左の稜線に沿って）赤色で表示されています。すでに除去された地雷原は明緑色で表示されています。

![未除去の危険区域は赤で示されており、すでに除去された危険区域は明るい緑色で示されています。](afghanistan2.jpg)

カブール大学のキャンパスには、空から投下された爆弾やそれに類する兵器で構成されていると考えられる危険区域がまだ存在しています。これらの危険は直ちに学生や職員への脅威とはなりませんが、アフガニスタンの将来の発展に不可欠な教育機関での将来の工事を可能にするために、最終的には除去する必要があります。また、これらの危険は、カブール首都圏に残る最後の重要な危険区域の一つとしても注目されます。以前の調査から得たハザードポリゴンとUSGSから提供された高い正確度の航空写真をQGISを使って組み合わせることにより、矛盾に着目することができます。例えばキャンパスの北西部分で明らかなように、ポリゴンが建物の形状と一致していないところからより正確な再調査を実施するよう、調査チームを送ることができます。

またQGISは、携帯式のGarmin GPSを使った野外活動にて収集されたデータと同期し、発見・破壊された地雷の場所で除去地図を作ることを可能にします。

The use of QGIS, along with a renewed interest in data analysis, has spurred new ways of looking at the data available, and combining it with other data sources to better target mineclearance activities. It is also driving improved mapping capabilities within the organisation, and an ability to better communicate the impact of its work to international donors. In a part of the world where 'formal' GIS training is difficult to acquire, the collaborative nature of the QGIS user community is greatly appreciated, as technical problems can often be solved by consulting online forums. In short, QGIS is playing a role in working towards ridding Afghanistan of landmines and UXO.
## リンク
- Danish Demining Group <http://www.danishdemininggroup.dk/>

## 著者
![Edward Crowther](afghanistan3.jpg)

Edward Crowther is Deputy Country Director at Danish Demining Group Afghanistan. Prior to joining DDG in Afghanistan, Edward worked with the humanitarian mineclearance agency The HALO Trust in Angola and Sri Lanka. He holds an MSc in Development Studies from the University of London's School of Oriental and African Studies.

{{<content-end >}}
