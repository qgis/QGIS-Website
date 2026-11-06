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

The Danish Demining Group (DDG), the specialised mine action unit of the Danish Refugee Council, has been working in Afghanistan since 1999, undertaking humanitarian mineclearance, unexploded ordnance (UXO) disposal and mine risk education. DDG Afghanistan delivers humanitarian mine action to save life, strengthen the sense of safety through risk education and help remove obstacles to the productive use of resources, helping to realise Afghanistan's development potential. Since the start of operations in Afghanistan, DDG has removed over 24,000 landmines and over 940,000 pieces of UXO. Currently, DDG is working in the northern provinces of Balkh and Samangan, and the central provinces of Kabul, Parwan and Panjshir.

In Afghanistan, mineclearance activities are coordinated through the Mine Action Coordination Centre for Afghanistan (MACCA), who collect and disseminate geospatial information on known hazards (minefields, battlefields, 'spot' UXO tasks), and update this information as clearance progresses. New shapefiles of these 'hazard polygons' are issued by the MACCA on a regular basis, and mineclearance organisations can use these to assess the situation of mineclearance in their areas of operation. DDG is trialling the use of QGIS within the organization to replace the expensive commercial softwares it has used in the past.

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
