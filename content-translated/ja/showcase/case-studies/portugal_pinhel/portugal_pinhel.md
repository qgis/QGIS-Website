---
draft: 'true'

---
# QGISとポルトガルの森林火災リスクの地図化
ポルトガルは、巨額の損失、環境的なだけでなく経済的、社会的な損失、を発生させる大規模な山火事の影響を受けています。このリスクに向き合うため、ポルトガル政府は、国有林局（AFN）を介して、地方政府に割り当てられる技術的な事務所を作成することを、数年前に、決定しました。これは、他のスキルの中でも、森林防火と動作応答のための市の計画を準備する必要があります。

In order to support the elaboration of these documents, the AFN provided technical guides with a methodology for calculating and mapping the Forest Fire Hazard and Risk. Moreover, tutorials have been offered to follow this methodology, using Proprietary Software. However, the acquisition and licensing costs of that software are unaffordable for most of the smaller local administrations and so, it was decided to create and make available a guide with a methodology for developing Hazard and Risk cartography using only Free and Open Source Software \[<http://goo.gl/TSv2E>\].

QGIS、GRASS GIS、gvSIGとGDAL / OGRライブラリ：これは、ソフトウェアの次のセットを使用することが提案されました。このガイドは、AFNの方法に従って、森林防火と動作応答のための計画の精緻化のために必要なすべてのジオプロセシングタスクについて説明します。作業の大部分はQGISで開発され、ラスタモデルの空間分析はGRASSで開発されました。gvSIGが、そのネットワーク解析拡張とともに、ネットワーク解析のために使用されました。そしてGDAL / OGRライブラリーが、基準座標系間の変換のために使用されました。

広範な方法論へのテストスイートの後、およびピニェルの自治体の運用計画の作成における実際の応用から3年後の今、提案されている代替には多くの利点があり、通常このタスクを実行するために使用される商用ソフトウェアを置き換えることを可能にする、と言うことができます。結果の検証が示したことは、この概念モデルが比較的単純であるにもかかわらずその予測能力はかなり良いこと、そしてオープンソースソフトウェアでモデルの実装は結果にマイナスに干渉しない、むしろ全く逆であることです。
> ![](./images/portugal_pinhel1.jpg){.align-right}

![Forest Fire Hazard and Risk Maps of Pinhel, implemented with Open Source Software.](./images/portugal_pinhel2.jpg){.align-right}

第二段階では、ほとんどの人間の介入なしに、タスクの広いセットを実行するワークフローを確立するためのモデルを使用して、この手順を高速化することを試みました。この第二段階は本質的に、第一段階から得られた実用的なガイドで説明全体手順を自動化することで成っていました。このような自動化は、年次森林防衛計画を作成する予定技術者の一部に強烈な仕事の数時間の短縮、人間の介入がわずか数分の入力データの選択および出力データを保持するつもりな場所の指示に帰着する、を意味するかもしれません。

![Interface of the Sextante Model to calculate the Probability of the Forest Fire Hazard.](./images/portugal_pinhel3.png){.align-right}

In furtherance of this second phase, we used the Python version of Sextante software, that works integrated into QGIS and adds a broad set of independent applications (GRASS GIS, SAGA GIS, OTB, R, GDAL/OGR, Pymorph, LASTools, Python scrips, etc..) in a single interface, providing a huge geoprocessing toolbox to QGIS users. Besides the integration of these applications in QGIS, Sextante has a tool for creating models, taking advantage of the modules offered by any of those softwares which aggregates. So, we\'ve created a model to automate the process of producing Forest Fire Hazard and Risk maps, using GRASS, SAGA, fTools and MMQGIS tools.

![Part of the model developed for automation of the production of cartography for Forest Fire Hazard and Risk.](./images/portugal_pinhel4.png){.align-right}

The results obtained so far are very promising, as already can be automatically achieved the creation of the Hazard and Risk Maps \[2\]. Taking into account that the Python version of Sextante is still very recent and is in heavy construction, there are some problems that must be corrected so that the models may be completed, which certainly will happen very soon, given the momentum that Sextante project presents. As future work, we intend to apply, also automatically, the symbology to the results as well as provide the final layouts in QGIS Composer, ready for export and/or print. Upon completion of the second phase and the realization of a sufficient set of tests that can validate the results obtained, it is our intention to provide the model free and openly.
## 結論
検討された代替案はずば抜けた品質のものであることが判明しました。国有林局の技術的なガイドで推奨されたすべての操作が、多くの点で、商用ソフトウェアでするより効率的に、できます。使いやすさの点では、それはソフトウェアのこのタイプは、しかしながら、より高い自由度を可能にする、実現モデルおよびアルゴリズムの唯一のより技術的な知識を必要とする任意の方法で、商用ソフトウェアよりも、より複雑ではないことが観察されました、それぞれの特定の状況にモデルを模索して微調整することが可能となります。独占的に、オープンソースソフトウェアを使用して森林火災の危険やリスク地図を作成する方法の工程は、Pinhelの自治体でのテストとアプリケーションの数年後、完全に統合されます。

オープンソースソフトウェアは、標準規格に基づいており、オープンなデータフォーマットのほとんどをサポートしているという事実は、ユーザが各瞬間に最も適したを選ぶすることができ、ソフトウェア間の完全な相互運用性を可能にします。ソフトウェアの特定のセットに私たちの提案のポイントにもかかわらず、何も無料と地理空間のためのオープンソースソフトウェアのための提案の広い範囲で、既存の選択肢のいずれかで交換する妨げません。しかし、QGISはますます、ほとんど、完全な安定した、使いやすいFOSS4Gソリューションとしての地位を提示し、その事業活動の中で最も多様な分野に特定の機能を追加し、バグのと新しいプラグインのほぼ毎日実施して急速な補正で、よりダイナミックであります。
## 著者
![Pedro Venâncio](./images/portugal_pinhelaut.png){.align-left height="200px"}

ペドロ・ヴェナンシオ学士号 地質、フリーソフトウェアでの大学院生および地理情報システムでの修士です。氏は、土木工学のための国立研究所で、コインブラ大学の地球物理学センターの研究者でした。現在はピニェルの自治体での地図作成や地理情報システムのサービスを担当しています。
