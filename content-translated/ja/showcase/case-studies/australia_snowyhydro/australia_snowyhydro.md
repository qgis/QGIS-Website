---
draft: 'true'

---
# プロセシングツールボックスを使用して雪の分類を自動化する
大雪水力株式会社（SHL）は、ニューサウスウェールズ州、オーストラリアの大雪山に基盤を置くピーク時発電の会社です。大雪水力株式会社は、全国に多様な発電資産を所有しているにもかかわらず、オーストラリアのインフラの象徴的な作品、大雪山水力発電スキームの管理権が最も有名です。

大雪山水力発電スキームは、ニューサウスウェールズ州の山岳地域での季節的降雪によって可能になります。春の雪解けの水は国家電力市場のピーク需要に対処する電気を生成するために使用されますが、また同時に、南オーストラリア東部のより乾燥した内陸部に灌漑農業のために水を流用しています。

冬季の月の間の積雪を分類することで、SHLは積雪地域のライフサイクルを監視し、積雪地域の歴史的記録を保管し、水収率および貯水の予測のために積雪の統計情報を水道事業チームへ提供することができます。

![Map 1.1 Snowy Water Catchment Map](images/australia_snowyhydro1.jpg){.align-center height="43400px"}
## 背景
毎年冬の間（10月31日から6月1日まで）、SHLはMODISテラ（EOS AM）衛星からできるだけ多くの雲のない画像を得ます。これらの画像は、その後、雪が存在する領域を示すために使用される正規化差分降雪指数（NDSI）として知られているアルゴリズムに摂取されます。このアルゴリズムはいずれか1つの特定のセンサに固有のものではありませんが、MODISの装置が十分な空間分解能があり、プロジェクトエリア（地図1.1　大雪流域）を日常的にカバーしているために選ばれました。
## 目的
このプロジェクトの目的は、NDSIのワークフローをQGIS処理ツールボックス内のモデルとして自動化することです。必要な出力は、大雪流域内の雪に覆われた範囲を示すベクターポリゴンで、雪に覆われた総面積を平方キロメートルで記述する属性と一緒にしたものです。 
## 点をランダムに抽出する基準
NDSIアルゴリズム自体は非常に簡単です（以下式1.1に示す - 正規化差分降雪指数（NDSI））。そして積雪をベクター形式で抽出するために必要なその後の工程は、プロセッシングツールボックスモデルにうまく適しています。

![Formula 1.1 - Normalised Difference Snow Index (NDSI)](./images/australia_snowyhydro8.png)

このNDSIアルゴリズムは-1と1の間で結果を返し、雪のための閾値は通常は0.4超となります。2014年7月13日について、自然色の画像（地図1.2 -MODISトゥルーカラー）と一緒にNDSI出力の例（地図1.3-NDSI出力）を以下に示します。これらの画像からわかるように、NDSI出力は雪で覆われた領域を他の土地被覆タイプおよび雲から弁別するのは非常に得意です。しかしながら大きな水域の一部を雪と誤分類することがあります。これは水がスペクトルの近赤外部分に吸収特性を有することで引き起こされます。NDSIのこの特徴は、モデル内のどこかの段階に水マスクを組み込むことが必要であると示唆しています。

![Map 1.2 - MODIS true colour](./images/australia_snowyhydro2.jpg){.align-left width="300px"}

![Map 1.3 - NDSI output](./images/australia_snowyhydro3.jpg){.align-center width="300px"}

![Map 1.4 - Recoded \"Snow\" vs \"Non snow\"](./images/australia_snowyhydro4.jpg){.align-left width="300px"}

The NDSI output is created with some very simple band map by using the GRASS module \"r.mapcalculator\". Once the NDSI grid was available the NDSI threshold of 0.4 needed to be applied and this would result in a boolean grid depicting \"Snow\" and \"Non snow\" areas. To get that classification another GRASS module \"r.recode\" was used and produced the result shown above in Map 1.4 Recoded 'Snow' vs 'Non Snow'.

The recoded grid was then converted to a vector polygon dataset and the snow covered areas were extracted (shown below, Map 1.5 - Extracted snow). The snow covered areas were then clipped to the Snowy Water Catchment (shown below, Map - 1.6 Snow inside the SWC), then the large water bodies are masked out (shown below, Map 1.7 - Final snow covered area), and finally the area statistics for the snow covered area is generated.

![Map 1.5 - Extracted Snow](./images/australia_snowyhydro5.jpg){.align-left width="300px"}

![Map 1.6 - Snow inside the SWC](./images/australia_snowyhydro6.jpg){.align-center width="300px"}

![Map 1.7 - Final snow covered area](./images/australia_snowyhydro7.jpg){.align-left width="300px"}

The output from the model is a vector polygon showing the snow covered area within the Snowy Water Catchment. The attributes of the polygon include the area covered by the snow and the percentage of the catchment that is covered. The model in its entirety can be seen below in \"Image 1.1 - Normalised Difference Snow Index (NDSI) QGIS processing toolbox model\".

![Image 1.1 - Normalised Difference Snow Index (NDSI) QGIS processing toolbox model](./images/australia_snowyhydro.png){.align-center width="600px"}
## 結果/結論
QGIS処理ツールボックスはこの雪の分類のようなワークフローを自動化するための強力な方法です。上に示したモデルでは、雪分類のプロセスを上手く自動化し、さらなる統計的アプリケーションで可視化して入力に使用できるGISデータセットを提供します。再現性と一貫性のある分類ツールを提供しながら、SHLで使用されていた以前の方法に関連づいた主観的なユーザの誤りを上手く除去しています。いくつかの季節の結果をここで見ることができます。
### 著者
アンドリュー・ジェフリーは、オーストラリアのニューサウスウェールズ州クーマに拠点を置く大雪水力株式会社に勤務するGISアナリストです。氏は科学の学士（BSC）、空間情報システム専攻で、ワガワガのチャールズ・スタート大学を2004年に卒業しました。大雪水力株式会社にいる間、氏は人工降雨実験のようなエキサイティングなプロジェクトや組織内での日常業務に空間的なサポートを提供することができました。
