---
HasBanner: false
draft: false
releaseDate: '2020-02-21'
section: project
sidebar: true
title: QGIS 3.12 の変更履歴
type: visual-changelog

---
{{<content-start >}}
# QGIS 3.12 の変更履歴{#changelog312 }
![image1](images/projects/dbf38cfe3b603e7e0b840336d39b399a1a46e52d.png)

リリース日: 2020-02-21

もし新しい機能やたくさんのバグ修正を求めているのであれば、このリリースはあなたを大いに喜ばせるでしょう！ QGIS 3.12は、ほぼ全ての部分に豊富な新しい機能を追加します。ラベルマスクからネイティブのPGラスタプロバイダー、信じられないほどの新しいメッシュレイヤの機能まで、このリリースには誰にでも何かがあります。いつものように、QGISはオープンソースのプロジェクトであり、寄付、スポンサーシップ、コードドキュメント、ウェブサイトなどへの貢献を考えることができる場合は、私たちの仕事をサポートしていただければと思います。

**謝辞**

私たちは開発者、文書作成者、テスターなどの時間や労力を提供してくれる数多くのボランティアの皆さん（また資金を提供してくれる方々）に感謝します。 QGIS コミュニティとして、このリリースを楽しんでいただきたいと思います。もし時間やお金を寄付したいと考えている場合や、 QGIS をもっと素晴らしいものにすることに参加したい場合は、 qgis.org を見て回って手を貸して下さい。

QGISは寄付者やスポンサーの支援を受けています。プロジェクトに多額の資金拠出を行った寄付者の現在のリストは寄付者リストをご覧ください。公式プロジェクトスポンサーになりたい場合、詳細はスポンサーシップのページをご覧ください。QGISへの出資は、半年毎の開発者会議に資金提供したり、プロジェクトインフラストラクチャを維持したり、バグ修正の取り組みに資金提供するのに役立ちます。現在のスポンサーの完全なリストは以下に掲載します。すべてのスポンサーの皆様に大変感謝しております！

{{<fund type="active" >}}

QGIS はフリーのソフトウェアです。利用する上で金銭を支払う義務はありません。実際、私たちは利用者の財政状況や社会的地位にかかわらず、より多くの人に QGIS を利用して欲しいと思っています。私たちは地理空間的な意思決定ツールによって人々が力を持つことが、全人類の社会をより良くすると信じています。

{{<table-of-contents >}}
## ツール
### 機能: QgsMapLayerAction: 選択したアクションに対する凡例コンテキストメニューエントリを追加
新しいメニューエントリ（選択範囲のアクション）がレイヤツリーコンテキストメニューに追加されます。必要な場合にのみ表示されます（レイヤに選択範囲があり、指定されたレイヤでアクションを実行できる場合に表示されます）。

![imageQ1](https://user-images.githubusercontent.com/127259/74035907-7f334580-49bb-11ea-8d2d-b99eaa10aa89.png)

This feature was developed by [Denis Rouzaud](https://api.github.com/users/3nids)
### 機能: GPSロック位置から現在のカーソルまでの距離を表示
GPSデバイスが接続されている場合、ユーザーがキャンバス上のカーソルを移動するたびに、ライブステータスバーメッセージにカーソルからGPS固定位置までの距離と方位が表示されます。

プロジェクトの距離と方位設定は、この表示で尊重されます。

![Peek 2020-01-14 16-06](https://user-images.githubusercontent.com/1829991/72318360-cd6c6600-36e7-11ea-9f2d-9a47d8772623.gif)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### 機能: プロジェクトに角度方位を表示するための形式設定を追加
設定 - オプション - マップツールタブには、新しく作成されたプロジェクトの角度方位を表示するためのデフォルトの形式を制御できる、新しい設定が含まれています。新しいプロジェクトが作成されるたびに、このデフォルトの設定が継承されます。

プロジェクトのプロパティダイアログには、プロジェクト固有の方位形式の新しい設定もあります。

The intention is that whenever angular bearings are shown in QGIS, they will be formatted using the current project\'s bearing format settings.

また、その方位形式などの設定や取得のための安定した、見つけやすい場所を提供するための多くの便利なAPIの追加も含まれています。

![Peek 2020-01-09 11-08](https://user-images.githubusercontent.com/1829991/72029046-5fcbce80-32d0-11ea-8571-0ae8fa8e3bb0.gif)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
## ユーザーインタフェース
### 機能: PostgreSQLデータを追加する際、追加ボタンをクリックした後にテーブルの選択を解除します。
PostgreSQLデータをデータソースマネージャに追加する際、追加ボタンを押した後、QGISは以前に選択されたテーブルの選択を解除する必要があります。

This feature was funded by [Kartoza](http://kartoza.com/)

This feature was developed by [Samweli Mwakisambwe](http://samweli.github.io/)
### 機能: ステータスバーに総パン距離と方位を表示する
We added the total pan distance and bearing in the status bar during canvas pan operations. Allows users to know exactly how far (and in what direction) they\'ve dragged the map.

![image5](images/entries/48c75d20d3805af3dad8c7faae3c3786a8f6fed0.gif)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### 機能: デフォルトのプロジェクトファイル形式(qgs/qgz)を設定する新しいオプション
新しいグローバルオプションを追加して、優先されるプロジェクトファイルの形式を定義します。

![imageQ2](https://user-images.githubusercontent.com/127259/72597971-2bc75d80-390f-11ea-84af-7f2c25d5568a.png)

この機能は GEM foundation によって資金提供されました

This feature was developed by [Denis Rouzaud](https://api.github.com/users/3nids)
### 機能: 別のレイヤにコピーする際に無効な属性ダイアログを修正する
It\'s possible to copy features from one layer to another. If there are the same fields in the destination layer, then the attributes for them are taken from the original feature. If not, the default value is taken. Otherwise, the new attribute is null.

宛先のレイヤのフィールドに制約がある場合、これらはすぐに満たされるか、意図的に無視されるべきです。ただし、以前のように無効なままコピーされるべきではありません。

That\'s why now the attributes are checked against the constraints. And for all the invalid features a dialog pops up.

![copydialog2](https://user-images.githubusercontent.com/28384354/72243171-7e410b00-35eb-11ea-8903-11bd56cd9da6.gif)

地物を1つだけ貼り付けると、オプションが減少します:

![copypastesingle](https://user-images.githubusercontent.com/28384354/72243125-5ce01f00-35eb-11ea-897e-0bccdcf083d7.png)

This feature was developed by [signedav](https://api.github.com/users/signedav)
### 機能：レイヤツリーから地図レイヤをプロジェクション選択ウィジェットにドロップできるようにする
\...to set the projection to match that layer. Just a little timesaving shortcut!

![Peek 2019-12-20 11-27](https://user-images.githubusercontent.com/1829991/71222288-b7070080-231b-11ea-89f4-af856dece4c3.gif)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### 機能: プロセシングラスタcalc: 無いボタンを追加し、検証
ABS/MIN/MAXのボタンを追加し、式を検証します。

![image10](https://user-images.githubusercontent.com/142164/68952420-1bd0b780-07c0-11ea-88d1-2ad0a8b5591e.gif)

この機能はAlessandro Pasottiが開発しました
## シンボロジ
### 機能: ベクタトレースアニメーションとメッシュレイヤのストリームライン
Mesh vector renderer now can visualize streamlines and particles on top of existing \"arrow\" mode.

![image11](images/entries/5b772e74d433e766b50023cd107aad9cb1d68de6.webp)

This feature was funded by [TUFLOW](http://www.tuflow.com)

This feature was developed by [Vincent Cloarec (Lutra Consulting)](http://www.lutraconsulting.co.uk)
### 機能: 選択的マスキング
A new advanced rendering feature has been added: selective masking. It allows the definition of \'masks\' areas around labels or point markers. These masks will \"un-draw\" only some symbol layers of other layers underneath, chosen by the user.

![image12](https://user-images.githubusercontent.com/1618556/62111873-d68c8680-b2b1-11e9-8cd4-19077f99a8ff.gif)

This feature was funded by [QGIS.CH and others through a cofunding campaign](https://oslandia.com/en/offre-qgis/selective-masking/)

This feature was developed by [Hugo Mercier (Oslandia)](https://www.oslandia.com)
### 機能：小数点の度の回転が評価できない場合、静的な値にフォールバックする
凡例は、データ定義された回転ともうまく機能します。QGISはすでにシンボルと個々のシンボルレイヤにデータ定義された回転を適用することができましたが、これにより凡例が壊れてしまいました。凡例上のシンボル（およびシンボルレイヤで定義されたシンボルパーツ）の回転は、データ定義されたプロパティの隣にあるデフォルト値を変更することで制御できるようになりました。

古い動作は、失敗した式の場合に常に0にフォールバックすることでした。いくつかの場合、これが適切な凡例を作成するのを難しくしていました。

例 もし、以下の回転式を持つ2つのシンボルレイヤがある場合

    "orientation"
    
同時に

    90 + "orientation"
    
二つの直交するシンボルレイヤ（例えば、直角を示す）が、方向フィールドによって回転されることになります。

今の凡例（およびシンボルのプレビュー）では、両方のレイヤが回転0で表示されます。なぜなら、属性の向きに関連付けられた地物が存在しないからです。

新しい動作では、これらのケースで凡例を設定するのが非常に直感的になるように、静的な設定値にフォールバックするようになりました。

**変更前**

![Peek 2019-12-08 09-18](https://user-images.githubusercontent.com/588407/70386652-acec1600-199b-11ea-8457-f9dd54c84272.gif)

**変更後**

![Peek 2019-12-08 09-16](https://user-images.githubusercontent.com/588407/70386651-acec1600-199b-11ea-8ce2-27798aec38a7.gif)

This feature was developed by [Matthias Kuhn](https://api.github.com/users/m-kuhn)
### 機能: ランダム塗りつぶしの密度ベースのポイントカウントを追加する
この機能は、新しいランダム塗りつぶしに密度ベースのポイントカウント方法を追加します。

![image15](https://user-images.githubusercontent.com/1728657/67672096-c2881c00-f9a9-11e9-8394-d73505d05309.gif)

この機能はMathieu Pellerinによって開発されました
### 機能: ランダム塗りつぶしシンボルレイヤータイプ
This feature adds a new fill symbol layer type \"Random marker fill\". It allows polygon features to be rendered using a marker symbol placed at random locations within the polygon boundary.

オプション：
- ポリゴンをレンダリングするマーカーシンボルの数
- ポリゴン境界付近にレンダリングされるマーカーがポリゴン境界でクリップされるかどうか
- オプションの乱数シードで、マップが更新されたときにマーカーを一貫して配置できるようにします（QGIS サーバやタイルベースのレンダリングとの相性が良いよう、ランダムに配置することもできます）

![image16](https://user-images.githubusercontent.com/1829991/66734145-51267480-eea5-11e9-9e0a-3bfeee15f976.png)

This feature was funded by [SLYR](https://north-road.com/slyr/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### 機能: ラスタレイヤでnodataピクセルをレンダリングするときの色を設定するオプションを追加
Allows raster nodata pixels to be colored in a specific (non-transparent) color. Designed to match the \"Display background value\" option from ArcMap.

![image17](https://user-images.githubusercontent.com/1728657/64846100-f4c9fe00-d635-11e9-8acb-367ad2dd2915.png)

This feature was funded by [SLYR](https://north-road.com/slyr/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
## ラベリング
### 機能: カスタムラベルの位置を削除できる
ラベルを移動する際にDELキーを押すことで、カスタムラベルの位置を削除することができる、新しいオプションを追加しました。

![image18](images/entries/e8064c56705b7a74befa85e8a34e7b7311626f0a.gif)

This feature was developed by [Denis Rouzaud](https://www.opengis.ch)
## ダイアグラム
### 機能: ダイアグラムレンダラーのペイント効果をサポート
this new feature allows for diagrams to use paint effects, including drop shadows, outer glows, etc\...

![image19](images/entries/37d0a22707eca463e5aba7c0a349b2d8029fb823.gif)

This feature was funded by [SLYR](https://north-road.com/slyr/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: New diagram type \"stacked bars\"
With this new feature users will have possibility to create stacks bars of varying colors for each attribute on top of each other vertically or horizontally. Designed to match the \"Stacked\" chart renderer option available in ArcGIS.

![image20](images/entries/933c25cf0cd8997e177eee809b4fa26462b6d8c2.webp)

This feature was funded by [SLYR](https://north-road.com/slyr/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### 機能：ベクタレイヤのバーチャートダイアグラムの間隔オプション
ユーザーがチャート内の各バーの間隔を制御できるようにします。

![image21](images/entries/7906ea6467d1d5ea19550ce1711fcc277df709a0.webp)

This feature was funded by [SLYR](https://north-road.com/slyr/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### 機能: パイダイアグラムの角度方向を制御する新しいオプション
この機能により、セクションが時計回りまたは反時計回りの方向でレンダリングされるかどうかを制御できます。

![image22](images/entries/c2484d36648c335d16d1e3a45ac1a132ca2baafe.webp)

This feature was funded by [SLYR](https://north-road.com/slyr/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
## レンダリング
### 機能：メッシュレイヤ再生の再生/停止ボタン
It is possible to switch the timeframes of mesh layer\'s datasets by play/stop button. The playback setting could be adjusted in the time setting dialog.

![image23](images/entries/4799685965addef6ca2c788d82eea77e67e2f1f3.webp)

This feature was funded by [Lutra Consulting](http://www.lutraconsulting.co.uk)

This feature was developed by [Lutra Consulting](http://www.lutraconsulting.co.uk)
### 機能: 面で定義されたデータの頂点へのオンザフライ・リサンプリング（メッシュレイヤ）
面で定義されたデータセットの場合、隣接平均法を使用してデータを頂点に補間することができます。データ補間方法が選択されていない場合、単一の面上の各ピクセルは単一の値/色を持ちます。頂点上の値から各ピクセルのレンダリングが補間されるため、より滑らかな図形が作成されます。

メッシュの等高線スタイルパネルを使用して、データの補間方法を切り替えます。

![image24](images/entries/c9c38ee8c59693b2971ab6269db22681a61002a1.webp)

This feature was funded by [Austrian Ministry of Agriculture, Forestry, Environment and Water Management](https://www.bmlfuw.gv.at)

This feature was developed by [Peter Petrik (Lutra Consulting)](http://www.lutraconsulting.co.uk)
### 機能：メッシュ参照時間のサポート
さまざまなデータセットの種類について、例えばGRIBやNetCDFなど、QGISの時間設定ダイアログの参照時間は、生データから自動的に設定されるため、手動で設定する必要はありません。また、時間の解析に関連するさまざまなバグも修正されているため、QGIS 3.12ではプロット/アニメーションで時間を適切な方法でフォーマットして表示することが可能になります:
- データセットグループに有効な時間参照が提供されている場合、この時間参照は時間の表示に使用されます（絶対時間を使用）。
- 参照時間が提供されていない場合、時間は相対時間を使用して表示され、ユーザーが絶対時間を表示するために時間参照を設定できます。
- 時間参照が指定されていない場合、デフォルトは現在の日付+時刻 00:00:00で設定されます。

必要な場合、データセットグループに提供された参照時間を再読み込みするためのプッシュボタンが追加されました。

プロバイダの時間単位が時以外の場合に、ユーザーが時間単位をコンボボックスで設定する新しい機能も追加されます。

![imageQ3](https://user-images.githubusercontent.com/7416892/70955568-bb939680-2047-11ea-9857-8aba122e43dd.png)

This feature was funded by [TUFLOW](http://www.tuflow.com)

This feature was developed by [Vincent Cloarec (Lutra Consulting)](http://www.lutraconsulting.co.uk)
## 三次元機能
### 機能：3Dメッシュレイヤ地形レンダラ
3Dビューでメッシュレイヤを地形としてレンダリングすることが可能です。

ユーザーは、スムーズな三角形とワイヤーフレームを有効/無効にすることができます。ワイヤーフレームのライン幅とライン色を選択することができ、垂直スケールを変更し、レンダリングのスタイル（単一の色またはカラーランプのシェーディング）を選択することが可能です。

3Dビューでメッシュレイヤをレンダリングするための2つのエントリがあります:
- 設定ウィジェットで地形としてメッシュを選択してください
- レイヤのプロパティで3Dビューをアクティブにしてください。

ユーザーはこれらの設定を選択できます:
- スムーズな三角形を有効/無効にする
- ワイヤーフレームを有効/無効にする
- ワイヤーフレームのライン幅とライン色を選ぶ
- 鉛直スケールを変更する
- レンダリングのスタイルを選択する：単一の色またはカラーランプのシェーディング
- カラーランプシェーディングをラスタレイヤに設定します

今のところ、メッシュはTINとしてレンダリングされることができますが、データセットのレンダリングはサポートされていません。ただし、インフラストラクチャは将来の作業のために適応されています。

![mesh3dsettings](https://user-images.githubusercontent.com/7416892/72482783-41d10300-37d5-11ea-9a21-8f906abcb14a.gif)

![image27](images/entries/f19c25acbd1eb462cdc0365d3af3f706c1b4d2fe.gif)

This feature was funded by [TUFLOW](http://www.tuflow.com)

This feature was developed by [Vincent Cloarec (Lutra Consulting)](http://www.lutraconsulting.co.uk)
### 機能: バックグラウンドで3Dベクタレイヤデータを読み込む + タイリング
このベクタレイヤから3Dマップビューへのデータのバックグラウンド読み込みを対応させます。これまでは、読み込み（およびテッセレーション）はGUIを完全にフリーズさせていました - 入力データの複雑さに応じて数秒かかることがあります。

基本的なベクタレイヤレンダラとルールベースレンダラは、地形のレンダリングに既に使用されているQgsChunkedEntityを使うように変換されました。GUIのロック解除に加えて、2つの改善があります:
- 読み込みプロセスは、単一のコアを使用する代わりに、マルチスレッドで行われます
- 読み込みはタイルで行なわれます - そのため、他のデータがまだ読み込まれている間に3Dデータが表示されるタイルを見ることができます。

There is a new configuration option in the 3D tab of vector layers - it determines how deep the quadtree will be. For example, one zoom level means there will be a single tile for the whole layer. Three zoom levels means there will be 16 tiles at the leaf level (every extra zoom level multiplies that by 4, so I have limited GUI to max. 8 levels which gives \~16K tiles which is already a lot).

How a vector layer\'s tiling quadtree gets populated: all internal tree nodes are empty and thus the 3D map scene tries to immediately replace them with their children - this goes until leaf nodes are reached. Only nodes at the leaf level currently hold any data. This may change in the future when we introduce more elaborate strategies - for example, internal nodes may contain a small percentage of features of the child nodes (this would allow us to show something while zoomed out a lot, not requiring to load all data).

For debugging purposes, there is also a new configuration option \"show bounding boxes\". This allows you to see the bounding box of each tile (especially useful if there are some issues with tiles not showing up when they should).

この機能は QGIS.org grant によって資金提供されました

This feature was developed by [Martin Dobias](https://api.github.com/users/wonder-sk)
## 印刷レイアウト
### 機能：地図レイアウトに写真をドラッグ＆ドロップできる
This new feature allows user e.g. drag an svg from a file explorer onto the layout to create a new picture item containing that svg image.

![image28](images/entries/21b9f2fba7bf1576f794410fd238ef7553154d53.gif)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### 機能: 新しいレイアウトアイテムタイプ：手動で作成された固定テーブル
This new item type allows for the creation of tables with contents manually entered by users (i.e. spreadsheet-style) so that users can create completely custom tables. Supports control custom cell contents, foreground and background colors (and soon, preset row and column heights). A brand new table designer dialog has been added which allows for customization of these tables.

![image29](images/entries/95cfa9a8c44fb0141474d80e4b3a5e7f98352e70.webp)

この機能は City of Canning によって資金提供されました

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### 機能: スケールバーの数値形式についてユーザー制御を追加
これでレイアウトスケールバーで使用される数値の形式を制御するオプションができました。

You can manage all the formatting properties for the numbers in scale bars, including whether they want a thousand separator, decimal places, scientific notation, etc. Very useful in the case of making maps for audiences outside of the current QGIS locale, or when you\'d just prefer to vary the style from the locale defaults (e.g. adding thousands separators when the locale default is to hide them).

![image30](images/entries/99c97baaee3e5930bca0cb63db1391b6fd49b34f.gif)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### 機能：一致する条件付きスタイルの前景色と背景色を使用して、レイアウト属性テーブルにスタイルを適用できるようにする
When the new \"Apply layer conditional styling colors\" option is enabled in the layout attribute table settings, any conditional styling rules present in the layer will be applied inside the layout attribute table (foreground and background colors only, for now!).

![image31](images/entries/baded0d05539439d58e6df5a8f24157293cf8022.gif)

この機能は City of Canning によって資金提供されました

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### 機能: レイアウトマネージャに検索ボックスを追加
Allows filtering the list of layouts in a project by name, handy when a project has many layouts..!

![image32](images/entries/fb510c6c079d55dab2dd22f02c7c5355b317ac47.webp)

この機能はNyall Dawsonによって開発されました
## 計算式
### 機能：関数のためのタグを検索する
Tags on static expression functions to make them more retrievable. Functions like array_to_string are listed when the user enters \"split\" or \"convert\" or - like before - a part of the function name.

![image33](images/entries/689a669fe84721d7574aba7e595e019a9936f0b9.gif)

This feature was funded by [SwissTierras-Colombia](https://www.proadmintierra.info)

This feature was developed by [David Signer (OPENGIS.ch)](http://www.opengis.ch)
### 機能: リスト参照先レイヤの値
フィールドがRelationReference、ValueRelation、およびValueMapの場合、現在のレイヤの値だけでなく、参照先のレイヤ/設定された可能性の値も表示する可能性があります。

![image34](images/entries/394c762c41e71764d9be397b718252eddb2dbd3e.gif)

This feature was funded by [SwissTierras-Colombia](https://www.proadmintierra.info)

This feature was developed by [David Signer (OPENGIS.ch)](http://www.opengis.ch)
### 機能: 新しい式
- `is_empty(geom)`, check if a geometry is empty (geometry that contain no coordinates)
- `is_empty_or_null(geom)`, check if a geometry is empty or NULL (does not have geometry)
- `hash`, cryptographic hashes functions using [QCryptographicHash](https://doc.qt.io/qt-5/qcryptographichash.html). Use case is the same as PgCrypto but in client side for all supported format.

This feature was developed by [Loïc Bartoletti (Oslandia)](https://www.oslandia.com)
### Feature: New algorithm \"Rename table field\"
Takes an input layer, existing field and a new name for the field, and outputs a new layer with the selected field renamed.

While this result could also be achieved with the Refactor Fields algorithm, Refactor Fields isn\'t particularly model friendly. It relies on a constant, fixed table structure, and can\'t adapt to input tables with different field structures.

In contrast, this simple Rename Field algorithm adapts nicely for model use, because it operates on a single field only and leaves all the other fields untouched.

![image35](images/entries/c01edc8ee51dff2b4df8f825e0dcaf27940e4aba.webp)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### 機能: 保存された式
- Store user expressions
- Clear editor icon/action

![expression-storage-opt](https://user-images.githubusercontent.com/142164/70983414-faae0000-20b8-11ea-9f25-14b338d4c680.gif)

See also QEP <https://github.com/qgis/QGIS-Enhancement-Proposals/issues/135>

This feature was funded by [Salvatore Fiandaca](https://pigrecoinfinito.com/2019/12/14/field-calc-di-qgis-save-expressions-crowdfunding/)

This feature was developed by [Alessandro Pasotti](https://api.github.com/users/elpaso)
### 機能：参照されたレイヤの値を式ビルダでリストアップする
フィールドがRelationReference、ValueRelation、およびValueMapの場合、現在のレイヤの値だけでなく、参照先のレイヤ/設定された可能性の値も表示する可能性があります。

*age* is a ValueMap, *species* is a ValueRelation and *island_id* is a RelationReference

![uniquevalues](https://user-images.githubusercontent.com/28384354/70978774-ab63d180-20b0-11ea-901b-d51d44fa8fa4.gif)

In the example we have the persons:
- *George (in Cuba, in his twenties, human) Paul (in Vietnam, in his thirties, human) Ringo (in Venezuela, in his forties, cat) John (in Vietnam as well, in his forties, table)*
- And the entries in the country layer are *USSR, Cuba, Vietnam, Burma, Venezuela, North Korea*

This feature was developed by [signedav](https://api.github.com/users/signedav)
### 機能: WKBへ/から変換する式関数を追加
- `geom_from_wkb( geom_to_wkb( make_point(4,5) ) ) → a point geometry object` Returns a geometry created from a Well-Known Binary (WKB) representation.
- `geom_to_wkb( $geometry ) → binary blob containing a geometry object` Returns the Well-Known Binary (WKB) representation of a geometry as a binary blob.

Adds geom_from_wkb and geom_to_wkb, which mirror the existing geom_from_wkt/geom_to_wkt functions but for WKB representations of geometries.

Since QGIS 3.6 we\'ve had good support for binary blob values in expressions and field values, so adding these functions allows users to work with binary blob fields containing WKB representations of geometries (e.g. with a geometry generator showing the encoded geometries)

This feature was funded by [SLYR](https://north-road.com/slyr/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: is_valid expression
`is_valid(geom_from_wkt('LINESTRING(0 0, 1 1, 2 2, 0 0)')) → true` Returns true if a geometry is valid; if it is well-formed in 2D according to the OGC rules

Add an is_valid function to the expressions, which reuses GEOS is valid and returns true if a geometry is valid; if it is well-formed in 2D according to the OGC rules.

この機能は Pete King によって開発されました
### Feature: Add datetime_from_epoch (MSec from epoch) expression function
`datetime_from_epoch(1483225200000) → 2017-01-01T00:00:00` Returns a datetime whose date and time are the number of milliseconds, msecs, that have passed since 1970-01-01T00:00:00.000, Coordinated Universal Time (Qt.UTC), and converted to Qt.LocalTime.

この機能はRichard Duivenvoordeによって開発されました
### Feature: rotate() expression function
`rotate($geometry, 45, make_point(4, 5)) → geometry rotated 45 degrees clockwise around the (4, 5) point` Returns a rotated version of a geometry. Calculations are in the Spatial Reference System of this geometry.

この機能は Raymond Nijssen, Nyall Dawson によって開発されました
### 機能: random関数にシードを設定できるようにする
- `rand(10, 80, 1) → 30` Returns a random integer within the range specified by the minimum and maximum argument (inclusive). If a seed is provided, the returned will always be the same, depending on the seed.
- `randf(10, 80, 1) → 19.37136508087729` Returns a random float within the range specified by the minimum and maximum argument (inclusive). If a seed is provided, the returned will always be the same, depending on the seed.

This feature adds an optional seed parameter to rand() and randf() functions This is very useful if you want the result to be deterministic, for instance to assign random but fixed colors to features. Using color_hsb(rand(0,360,\$id),50,50) for instance yields always the same color for the same feature. We also improves the rand() function, which didn\'t work for high values (over 32000) by using Qt\'s QRandomGenerator instead of qrand (which it seems was deprecated in Qt 5.11).

この機能は olivierdalang によって開発されました
### Feature: Language support for format_date() and to\_{date,datetime,time}()
- `format_date('2012-05-15','d MMMM yyyy','fr') → '15 mai 2012'`
- `format_date('2012-05-15','d MMMM yyyy','it') → '15 maggio 2012'`
- `format_date('2012-05-15','d MMMM yyyy','en') → '15 May 2012'` Formats a date type or string into a custom string format. Uses Qt date/time format strings. See QDateTime::toString.

By default, those expression use the application\'s locale. The addition of an optional language parameter allows handling of dates that wouldn\'t match that default locale (say for e.g. an English system running QGIS trying to transform a French-formatted string into a date object).

この機能はMathieu Pellerinによって開発されました
## デジタイズ
### 機能：別のレイヤにコピー/貼り付けする際に無効な属性を編集する
On copy-paste features from one layer to another, in case there are constraints (e.g. not null) on the destination layer, that cannot bee fulfilled automatically by default values, a dialog pops up to fix the invalid attributes or disregard the constraints on purpose.

![image38](images/entries/5bd43dd39955e37ace130038b968550c6fa260c5.gif)

This feature was funded by [Amt für Wald und Wild Zug](https://www.zg.ch/behoerden/direktion-des-innern/wald-und-wild)

This feature was developed by [David Signer (OPENGIS.ch)](http://www.opengis.ch)
### 機能: スナップキャッシュの並列化
In previous version of QGIS, the snapping index cache was built sequentially and you had to wait for all your layers to be indexed before starting edition. Thanks to the QGIS.org grant program, QGIS now builds the snapping index cache in parallel for each layer, so it speeds up the whole process. Snapping has also been relaxed, meaning that you don\'t have to wait for the cache to be complete, you can start editing and snapping information will appear as soon as they are ready.

![image39](images/entries/d77958db7175267448d9b94950532dee8b90145c.webp)

This feature was funded by [QGIS.org](https://qgis.org)

This feature was developed by [Julien Cabieces (Oslandia)](https://oslandia.com/en/)
## データ管理
### 機能：DXFエクスポートの改善
We did a revamp of the DXF export process. This solidifies the export process and offers new features.
- Styles of geometries are exported and blocks are used
- The Z coordinate of 3D geometries are preserved
- Labels are exported with their anchor points and horizontal and vertical alignment or quadrant settings respected

The whole DXF export process has also been made ready for running in a thread. With this in place, it\'s now only one step away from being sent to the background, allow cancellation of an ongoing export process or being exposed as a processing algorithm.

This feature was funded by [Kanton Schaffhausen](https://sh.ch/CMS/Webseite/Kanton-Schaffhausen/Beh-rde/Verwaltung/Volkswirtschaftsdepartement/Amt-f-r-Geoinformation-1262910-DE.html)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](https://www.opengis.ch)
## フォームとウィジェット
### 機能: リレーションエディタからジオメトリの地物を作成する
We added the ability to add a new feature and digitize its geometry directly from within the relation editor widget. It\'s now easier to add a geometric feature related to your currently displayed parent feature.

![image40](images/entries/fe03aefab87464e54b70569e6d05ad09a1b8fae5.gif)

This feature was funded by [QWAT user group](http://qwat.org/about/)

This feature was developed by [Julien Cabieces (Oslandia)](https://oslandia.com/en/)
### 機能: 地物選択ダイアログの改善
From the relation editor widget, you can link your currently displayed feature with existing features. The feature selection dialog allows you to choose these features. Thanks to the QWAT user group, feature selection is now shared with the canvas\' one so it is easy to find out and pick the feature you want to link. We have also added the ability to filter displayed features (selected ones, visible on map, matching an expression\...) reusing the same widgets already existing in attribute form.

![image41](images/entries/a65364e6a48857a8720643c41a3cb17461d9e16a.gif)

This feature was funded by [QWAT user group](http://qwat.org/about/)

This feature was developed by [Julien Cabieces (Oslandia)](https://oslandia.com/en/)
### Feature: UX improvements in drag\'n\'drop form designer
The drag\'n\'drop form designer has received some nice UX improvements
- The two lists (available fields and layout tree) are now synchronized: whenever you select an entry in a list, the matching item is selected in the other one.
- Hidden config dialogs (under double-click) have been brought to the right panel

![image42](images/entries/5f47cb6311a9bffef94128a703719d709deb995a.gif)

この機能は QGIS.org bugfixing によって資金提供されました

This feature was developed by [Denis Rouzaud, OPENGIS.ch](https://opengis.ch)
## レイヤ凡例
### 機能：レイヤツリーでWMTS凡例グラフィックスの表示に対応
We added support for displaying WMTS legend graphics directly in the layer tree, as is already the case with WMS legend graphics.

例:

![imageQ4](https://user-images.githubusercontent.com/1298852/72462785-33351c80-37d2-11ea-98f2-ce0d5221e1f5.png)

Sample use case: <https://wmts10.geo.admin.ch/EPSG/2056/1.0.0/WMTSCapabilities.xml>

This feature was developed by [Sandro Mani](https://api.github.com/users/manisandro)
## 分析ツール
### 機能: メッシュレイヤからの等高線のスムーズなエクスポート
A new algorithm in QGIS's analysis library API to export directly contour lines and polygons is added. The method is not based on GDAL algorithms, but directly uses mesh layer triangular mesh interpolation methods. It is both fast and with smooth shapes, matching rendered images from QGIS. You can try the new processing algorithm in Crayfish processing toolbox.

![image44](images/entries/044ad55bfb4287026b4e002c46c8687093488d22.webp)

This feature was funded by [Austrian Ministry of Agriculture, Forestry, Environment and Water Management](https://www.bmlfuw.gv.at)

This feature was developed by [Peter Petrik (Lutra Consulting)](http://www.lutraconsulting.co.uk)
### Feature: Support of Datasets Defined on Faces in QGIS Mesh Calculator
You can use mesh calculator for all dataset types, both defined on faces and vertices. Additionally, it allows users to store the result of mesh calculator under different name or format. This allows for example to work with FLO-2D or HEC-RAS data in the QGIS mesh calculator

![image45](images/entries/044d52fe937887854583ecfdc551e73eafb94a41.webp)

This feature was funded by [Austrian Ministry of Agriculture, Forestry, Environment and Water Management](https://www.bmlfuw.gv.at)

This feature was developed by [Peter Petrik (Lutra Consulting)](http://www.lutraconsulting.co.uk)
## プロセシング
### Feature: Package new layers to existing GeoPackage
We improved the existing *package layers* processing algorithm to be able to add new layers to existing GeoPackages. All you need to do to make use of this is disable the OVERWRITE parameter and specify an existing GeoPackage.

![image46](images/entries/35d87f4826aad132de4a0b99ac7c775f6aa9b029.webp)

This feature was funded by [BikePlan](https://www.bikeplan.ch/)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](https://www.opengis.ch)
### 機能: ファジー理論 - ラスタのファジー化 (linear membership)
The Fuzzify raster (linear membership) algorithm is a native implementation of a fuzzy logic algorithm. It transforms an input raster to a fuzzified raster and thereby assigns values between 0 and 1 following a linear fuzzy membership function. The value of 0 implies no membership with the defined fuzzy set, a value of 1 depicts full membership. In between, the degree of membership of raster values follows a linear membership function.

![image47](images/entries/bfb37d710293c252dae11b67b25bdc1431f13815.webp)

This feature was developed by [Clemens Raffler](https://github.com/root676)
### 機能: ファジー理論 - ラスタのファジー化 (power membership)
The Fuzzify raster (power membership) algorithm is a native implementation of a fuzzy logic algorithm. It transforms an input raster to a fuzzified raster and thereby assigns values between 0 and 1 following a power fuzzy membership function. The value of 0 implies no membership with the defined fuzzy set, a value of 1 depicts full membership. In between, the degree of membership of raster values follows a power membership function.

![image48](images/entries/7a81ecd4414ee39b37e575863687615c88e9a856.webp)

This feature was developed by [Clemens Raffler](https://github.com/root676)
### 機能: Fuzzy Logic - Fuzzfiy ラスタ (small membership)
The Fuzzify raster (small membership) algorithm is a native implementation of a fuzzy logic algorithm. It transforms an input raster to a fuzzified raster and thereby assigns values between 0 and 1 following the \'small\' fuzzy membership function. The value of 0 implies no membership with the defined fuzzy set, a value of 1 depicts full membership. In between, the degree of membership of raster values follows the \'small\' membership function. The \'small\' function is constructed using two user-defined input raster values which set the point of half membership (midpoint, results to 0.5) and a predefined function spread which controls the function uptake.

![image49](images/entries/2bef948a7b02bd26208ca98e9ddb243d46d104a6.webp)

This feature was developed by [Clemens Raffler](https://github.com/root676)
### 機能: ファジー理論 - ラスタのファジー化 (large membership)
The Fuzzify raster (large membership) algorithm is a native implementation of a fuzzy logic algorithm. It transforms an input raster to a fuzzified raster and thereby assigns values between 0 and 1 following the \'large\' fuzzy membership function. The value of 0 implies no membership with the defined fuzzy set, a value of 1 depicts full membership. In between, the degree of membership of raster values follows the \'large\' membership function.The \'large\' function is constructed using two user-defined input raster values which set the point of half membership (midpoint, results to 0.5) and a predefined function spread which controls the function uptake.

![image50](images/entries/10963d11812664a76d4fc3fac72777c34a08c767.webp)

This feature was developed by [Clemens Raffler](https://github.com/root676)
### 機能: ファジー理論 - ラスタのファジー化 (gaussian membership)
The Fuzzify raster (gaussian membership) algorithm is a native implementation of a fuzzy logic algorithm. It transforms an input raster to a fuzzified raster and thereby assigns values between 0 and 1 following the \'gaussian\' fuzzy membership function. The value of 0 implies no membership with the defined fuzzy set, a value of 1 depicts full membership. In between, the degree of membership of raster values follows the \'gaussian\' membership function. The gaussian function is constructed using two user-defined input values which set the midpoint of the gaussian function (midpoint, results to 1) and a predefined function spread which controls the function spread.

![image51](images/entries/58068dc6518a0df20a39df69ea4175f7b196b049.webp)

This feature was developed by [Clemens Raffler](https://github.com/root676)
### 機能: ファジー理論 - ラスタのファジー化 (near membership)
The Fuzzify raster (near membership) algorithm is a native implementation of a fuzzy logic algorithm. It transforms an input raster to a fuzzified raster and thereby assigns values between 0 and 1 following the \'near\' fuzzy membership function. The value of 0 implies no membership with the defined fuzzy set, a value of 1 depicts full membership. In between, the degree of membership of raster values follows the \'near\' membership function. The near function is constructed using two user-defined input values which set the midpoint of the near function (midpoint, results to 1) and a predefined function spread which controls the function spread.

![image52](images/entries/a4873da4c5e782a14caaa02f279ef92ba5bf5a38.webp)

This feature was developed by [Clemens Raffler](https://github.com/root676)
### 機能: 頂点を高密度化アルゴリズムをC++に移植
We ported the Densify by count algorithm to C++ in order to enhance it\'s speed when compared to the previous Python implementation. The new algorithm also exposes the count parameter as dynamic parameter so that it can be controlled by expressions or field values.

![image53](images/entries/680eb97f65d08de5541f4b1f5ac4425f45988cc2.webp)

This feature was developed by [Clemens Raffler](https://github.com/root676)
### 機能: 指定範囲にランダム点群アルゴリズムをC++に移植
We ported the Random points in extent algorithm to C++. This boosts it\'s speed when comparing it to the previous Python implementation. The new algorithm also exposes an advanced parameter of maximum numbers of retrys for the algorithm when searching for randomly placed points that respect a certain distance between all points.

![image54](images/entries/c452431d9a2cd9f9f76869cf98e09e18bf2a81a4.webp)

This feature was developed by [Clemens Raffler](https://github.com/root676)
### 機能: 線密度アルゴリズム
In this version we added a native algorithm to calculate the raster based density of lines. This algorithm calculates the line density based on a search radius and weights of the lines inside the search radius. The algorithm was ported to provide more functionality form the ArcGIS Spatial Analyst extension in QGIS.

![image55](images/entries/b28bbe3d5129ccc5dd61585dc1a9e31383a59c6f.webp)

This feature was developed by [Clemens Raffler](https://github.com/root676)
### Feature: New algorithm \"Repair Shapefile\"
We added a new algorithm which uses GDAL to repair shapefiles which have a broken or missing .SHX file.

![image56](images/entries/c3a6a174187284126ea0af289614505ab8c0c593.webp)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: Add new algorithm \"Detect Dataset Changes\"
This algorithm compares two vector layers, and determines which features are unchanged, added or deleted between the two. It is designed for comparing two different versions of the same dataset.

When comparing features, the original and revised feature geometries will be compared against each other. Depending on the Geometry Comparison Behavior setting, the comparison will either be made using an exact comparison (where geometries must be an exact match for each other, including the order and count of vertices) or a topological comparison only (where are geometries area considered equal if all of the their component edges overlap. E.g. lines with the same vertex locations but opposite direction will be considered equal by this method). If the topological comparison is selected then any z or m values present in the geometries will not be compared.

By default, the algorithm compares all attributes from the original and revised features. If the Attributes to Consider for Match parameter is changed, then only the selected attributes will be compared (e.g. allowing users to ignore a timestamp or ID field which is expected to change between the revisions).

If any features in the original or revised layers do not have an associated geometry, then care must be taken to ensure that these features have a unique set of attributes selected for comparison. If this condition is not met, warnings will be raised and the resultant outputs may be misleading.

The algorithm outputs three layers, one containing all features which are considered to be unchanged between the revisions, one containing features deleted from the original layer which are not present in the revised layer, and one containing features add to the revised layer which are not present in the original layer.

![image57](images/entries/e38dcea12e1198341eb9f0bd45a33ebf7eda390b.webp)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Feature: New mode to \"Join Attributes by Location\" to take attributes from matching feature with largest area of overlap only
This allows for easy polygon-\>polygon joins, where you expect there to be only a single matching feature and don\'t want to include features which are just touching or have just tiny sliver polygon overlaps.

![image58](images/entries/27b8e5e11deca93ffade31b86edc712ce918d179.webp)

この機能は、SMEC/SJによって資金提供されました

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### 機能: ベクタのネイティブアフィン変換アルゴリズムを追加
Offers the following benefits over the GRASS/SAGA versions:
- Full support for z/m values and handling curved geometries without loss of curves
- Works with all native data types, no need for format transformation
- Supports dynamic (data defined, per feature) translate/scale/rotate parameters
- Allows transformation and scaling of both Z and M values (if present)
- Supports in-place edit mode

![image59](images/entries/1bfee3c2e208ecca6c235d96f83966ec808a0b1c.webp)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Feature: add gdal_viewshed algorithm
Expose new gdal_viewshed tool via Processing toolbox. Note: this requires GDAL \>= 3.1.

この機能はAlexander Bruyによって開発されました
## ブラウザ
### 機能: ブラウザに表示されるアイテムのカスタマイズ
Add customization of the items shown in browser to the Interface Customization dialog. User can hide some of the root items in the browser panel (e.g. Favourites, PostGIS provider, MSSQL, Oracle, Volumes, \...)

![image60](images/entries/5e8e9037420b83cd44d4e1994d4119e4ae92c8aa.webp)

This feature was funded by [Limerick City and County Council](https://www.limerick.ie/council)

This feature was developed by [Peter Petrik (Lutra Consulting)](http://www.lutraconsulting.co.uk)
### 機能: ブラウザパネルにhtmlファイルを表示
This feature allows .htm(l) files to be shown and opened from the browser panel. These are often used to document data files or mapping projects.

![image61](images/entries/0db8930d20ca6f2fbf5b29593afdcf59e1af8d1e.webp)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: Show \"Open Document\...\" action in browser
When right clicking certain files in the browser, allowing them to be opened with the default external application for that file type

E.g. PDFs will open with the default external PDF viewer.

Works with PDF, ODS, XLS(X), CSV, TXT, PNG, JPEG, TIFF, SVG (other types will likely need more work, since they aren\'t currently shown in the browser).

![image62](images/entries/447f201d2342a64912bbef1e1d0aa3ebb8963ae4.gif)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: Allow customization of the items shown in browser
You can now customize items shown in the browser. User can decide (in the Interface Customization dialog) to hide some of the root items in the browser panel (e.g. Favourites, or POSTGIS provider, \...)

![Screenshot 2020-01-09 at 09 17 05](https://user-images.githubusercontent.com/804608/72050388-466f5600-32c1-11ea-94f5-092cc8471243.png)

この機能は Limerick City and County Council によって資金提供されました

This feature was developed by [Peter Petrik](https://api.github.com/users/PeterPetrik)
### Feature: Add Refresh action to OGC services
You can now refresh OGC services in the browser. Below is a screenshot showing an example of how this function works in WMS/WMTS connections:

![OGCrefreshonaction](https://user-images.githubusercontent.com/2663775/71974919-cfd04b00-3223-11ea-834d-ff016c70a8c6.gif)

This feature was developed by [Samweli Mwakisambwe](https://api.github.com/users/Samweli)
## データプロバイダ
### Feature: Changed WMTS layer collection icon
This was a change of the icon used for WMTS layer collection item, a database schema was used instead of a WMTS related icon. A general WMS icon is now used.

This feature was funded by [Kartoza](http://kartoza.com/)

This feature was developed by [Samweli Mwakisambwe](http://samweli.github.io/)
### Feature: Added Metadata URL property in the layer metadata tab for WMS / WMTS and WCS services
This feature was funded by [Kartoza](http://kartoza.com/)

This feature was developed by [Samweli Mwakisambwe](http://samweli.github.io/)
### Feature: Fetch and show dimensions metadata for a WMS layer metadata
![image65](images/entries/d058ac6b89a8d06169b06580843967ad26e1ef54.webp)

This feature was funded by [Kartoza](http://kartoza.com/)

This feature was developed by [Samweli Mwakisambwe](http://samweli.github.io/)
### Feature: Added refresh action to OGC services entries
![image66](images/entries/7ce331ee78be7f8b0693c653ecc58916d70a1a92.gif)

This feature was funded by [Kartoza](http://kartoza.com/)

This feature was developed by [Samweli Mwakisambwe](http://samweli.github.io/)
### Feature: 3d Stacked Meshes
MDAL and QGIS now supports 3D Stacked Meshes, particularly for TUFLOW-FV format. For this release, you need to choose appropriate averaging method in the QGIS interface and you are able to browse the data similarly to any other 2D dataset.

![image67](images/entries/dc3d85153d9bcecdf7ebbc6433c7cb40319e00dd.webp)

This feature was funded by [TUFLOW](http://www.tuflow.com)

This feature was developed by [Peter Petrik (Lutra Consulting)](http://www.lutraconsulting.co.uk)
### 機能: シェープファイルの符号化のとても多くの数の問題を修正
This fixes the (broken by design?) handling of Shapefile encoding, which has been an ongoing issue for years in QGIS.

See discussion at
- [#21264](https://github.com/qgis/QGIS/issues/21264)
- <http://osgeo-org.1560.x6.nabble.com/Shapefile-with-file-cpg-codepage-td5275106.html>
- <http://osgeo-org.1560.x6.nabble.com/QGIS-ignore-the-cpg-files-when-loading-shapefiles-td5348021.html>

(+ others!)

The situation was that we had two different code paths for handling GDAL side attribute decoding OR QGIS side decoding. Unfortunately, they are both incompatible with each other, and due to GDAL API for this, we can\'t unify the two approaches. (More technical detail in the commit log message!)

So, now we:
- always do the decoding on QGIS\' side. This allows users to manually override a shapefile\'s declared encoding because they are often incorrect!
- use a port of GDAL\'s shapefile detection logic (it\'s not exposed in GDAL API, so I had to re-implement it here) so that we default to reading shapefiles by respecting the embedded encoding information (via CPG files or DBF LDID information)
- Completely remove the confusing/broken \"Ignore shapefile encoding declaration\" option, as it\'s no longer required \-- users are ALWAYS able to manually change the encoding of shapefiles layers if needed
- Always show users the detected embedded encoding in the layer properties, instead of always showing \"UTF-8\" when the embedded encoding information is used

This should give the best of both worlds \-- a nice default behavior resulting in shapefiles being read with the correct encoding, whilst still allowing users to override this on a layer-by-layer basis as needed.

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Feature: Oracle curve type edition support
In earlier versions of QGIS, it was not possible to edit some geometry types coming from an Oracle database. We have then added edition support for the following geometry types:
- CircularString(Z)
- CompoundCurve(Z)
- MultiCurve(Z)
- CurvePolygon(Z)
- MultiSurface(Z)

この機能は Lille Metropole によって資金提供されました

This feature was developed by [Julien Cabieces (Oslandia)](https://oslandia.com/en/)
### 機能: WMS プロバイダでMBTiles ラスタの対応
This feature adds MBTiles tiled raster map support to WMS provider so that it uses the same code paths like WMTS or XYZ tiles. Here are the advantages of the approach through WMS provider:
- correctly scaling tiles on high dpi display
- better look when not zoomed to the native resolution of the tiles. WMS provider uses smooth scaling while GDAL uses nearest neighbor by default.
- map tile showing up while rendering (with GDAL it\'s blank map until everything is loaded)
- possible to use tile scale slider dock widget
- faster - mainly a side effect of loading fewer tiles on high dpi display

This feature was developed by [Martin Dobias](https://api.github.com/users/wonder-sk)
### 機能: ネイティブのPostGISラスタデータプロバイダ
This is an implementation of a PostGIS raster data provider in QGIS core. Tiles are cached in RAM memory.

この機能は Christmas Holidays Inc. によって資金提供されました

This feature was developed by [Alessandro Pasotti](https://api.github.com/users/elpaso)
### 機能: WMSレイヤのメタデータに寸法のメタデータを表示する
![wms-ttimelayermetadataqgis](https://user-images.githubusercontent.com/2663775/71542497-37f77500-2978-11ea-854b-d9a9ca2d6c77.png)

This feature was developed by [Samweli Mwakisambwe](https://api.github.com/users/Samweli)
### Feature: Other average methods 3d mesh
QGIS now includes numerous methods for averaging mesh layers (see [related QEP](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/158), and for a description of the methods see [TUFLOW documentation](https://fvwiki.tuflow.com/index.php?title=Depth_Averaging_Results).
- SingleLevelAverageMethod (top)
- SingleLevelAverageMethod (bottom)
- MultiLevelsFromTopAveragingMethod
- MultiLevelsFromBottomAveragingMethod
- SigmaAveragingMethod
- DepthAveragingMethod
- HeightAveragingMethod
- ElevationAveragingMethod

![Screenshot 2019-12-19 at 13 59 47](https://user-images.githubusercontent.com/804608/71175509-068bf480-2268-11ea-9d60-adad896912e2.png)

This feature was developed by [Peter Petrik](https://api.github.com/users/PeterPetrik)
### Feature: OGC API - Features provider
This new provider is a client-side implementation of the recently adopted [OGC API - Features - Part 1: Core](http://docs.opengeospatial.org/is/17-069r3/17-069r3.html) specification, previously known as WFS3. It is integrated within the graphical user interface of the WFS provider, and leverages its core mechanisms to offer background downloading of features, using paging, and a local cache of already downloaded features for a smoother interactive use of datasets.

![image70](images/entries/d74a13f520336e0c2e44469ee4e527188e2466de.webp)

This feature was funded by [Planet](https://planet.com)

This feature was developed by [Even Rouault (Spatialys)](https://www.spatialys.com)
## QGISサーバー
### Feature: QGIS Development Server Application
**QGIS Development HTTP Server**

This is a small independent command-line application that implements a minimal HTTP development server for QGIS Server.

It can be useful when developing and testing QGIS Server projects, modules, and plugins without requiring a full webserver/FCGI stack.

![qgismapserver](https://user-images.githubusercontent.com/142164/73081781-84c36280-3ec8-11ea-9285-ab4c41e3082c.gif)
``` bash
Usage: qgis\_mapserver [options] [address:port]
QGIS Development Server

Options:
-h, --help Displays this help.
-v, --version Displays version information.
-l Sets log level (default: 0)
0: INFO
1: WARNING
2: CRITICAL
-p Path to a QGIS project file (*.qgs or* .qgz),
if specified it will override the query string MAP argument
and the QGIS\_PROJECT\_FILE environment variable

Arguments:
addressAndPort Listen to address and port (default: "localhost:8000")
address and port can also be specified with the environment
variables QGIS\_SERVER\_ADDRESS and QGIS\_SERVER\_PORT
```
Sample output:

`bash QGIS Development Server listening on http://localhost:8000 CTRL+C to exit 127.0.0.1 [lun gen 20 15:16:41 2020] 5140 103ms "GET /wfs3/?MAP=/home/ale/dev/QGIS/tests/testdata/qgis_server/test_project.qgs HTTP/1.1" 200 127.0.0.1 [lun gen 20 15:16:41 2020] 3298 2ms "GET /wfs3/static/jsonFormatter.min.js HTTP/1.1" 200 127.0.0.1 [lun gen 20 15:16:41 2020] 1678 3ms "GET /wfs3/static/jsonFormatter.min.css HTTP/1.1" 200 127.0.0.1 [lun gen 20 15:16:41 2020] 1310 5ms "GET /wfs3/static/style.css HTTP/1.1" 200 127.0.0.1 [lun gen 20 15:16:43 2020] 4285 13ms "GET /wfs3/collections?MAP=/home/ale/dev/QGIS/tests/testdata/qgis_server/test_project.qgs HTTP/1.1" 200`

This feature was developed by [Alessandro Pasotti](https://api.github.com/users/elpaso)
### Feature: Add DXF server export params NO_MTEXT and FORCE_2D
QGIS server now supports the new parameters `NO_MTEXT` and `FORCE_2D` to control text and line symbology for generated DXF files. Adds missing parameters to GetDxf request

This feature was developed by [Matthias Kuhn](https://api.github.com/users/m-kuhn)
### Feature: Add json support to WMS GetLegendGraphic
This feature adds support for GetLegendGraphic responses encoded as JSON. It builds on previous work by \@pblottiere, who added QgsLegendRenderer::exportLegendToJson for that exact purpose.

For example a GetLegendGraphic request with FORMAT=image/png producing the image

![image72](https://user-images.githubusercontent.com/76594/64876231-fbb13a80-d64e-11e9-83e5-120fb1bc0ea8.png)

will produce the following with FORMAT=application/json

The icon image is encoded in base64, and directly displayable in a web page.

この機能は Éric Lemoine によって開発されました
## プログラム可能
### Feature: Exposes shape digitizing methods to QgisInterface
The actions to trigger the drawing tools were not exposed in the API, if you wanted to do an action for one of these tools, you had to recreate classes. So a call of the type `qgis.utils.iface.actionCircleCenterPoint().trigger()` simplifies programmability.

この機能は QWAT/QGEP グループによって資金提供されました

This feature was developed by [Loïc Bartoletti (Oslandia)](https://www.oslandia.com)
## 注目すべき修正
### 機能: Stephen Knoxによるバグ修正
| Bug Title | URL issues (if reported) | URL PR or commit |----|----|----|----| | Allow editing of postgres JSON fields from Text Edit Widget | [#29361](https://github.com/qgis/QGIS/issues/29361) | [#30758](https://github.com/qgis/QGIS/pull/30758)

この機能は Stephen Knox によって開発されました
### 機能: Alessandro Pasotti によるバグ修正
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| \"Recent\" Group do not appear when opening the \"Select by expression\" dialog | [#33791](https://github.com/qgis/QGIS/issues/33791) | [PR #33922](https://github.com/qgis/QGIS/pull/33922) | [PR #33922](https://github.com/qgis/QGIS/pull/33922) |
| QGISserver cannot find shp; tries to open absolute instead of relative path | [#33200](https://github.com/qgis/QGIS/issues/33200) | [PR #33925](https://github.com/qgis/QGIS/pull/33925) | risky |
| unreported: wrong link in server WFS3 items page (too many slashes) | 未報告 | [PR #33926](https://github.com/qgis/QGIS/pull/33926) | risky |
| Qgis scans raster tables on connection to postgis | [#33885](https://github.com/qgis/QGIS/issues/33885) | [PR #33922](https://github.com/qgis/QGIS/pull/33922) | [PR #34288](https://github.com/qgis/QGIS/pull/34288) |
| Layer Properties Information tab - formatting problems | [#33862](https://github.com/qgis/QGIS/issues/33862) | [PR #33955](https://github.com/qgis/QGIS/pull/33955) | [PR #34289](https://github.com/qgis/QGIS/pull/34289) |
| Can\'t set min/max values to decimal in raster symbology with QGis Linux versions | [#33859](https://github.com/qgis/QGIS/issues/33859) | works for me in current master |  |
| QgsVectorLayer readStyle does not read scale based visibility | [#33840](https://github.com/qgis/QGIS/issues/33840) | [PR #33987](https://github.com/qgis/QGIS/pull/33987) | [PR #34289](https://github.com/qgis/QGIS/pull/34289) |
| Categorized symbolization does not work on bigint columns in QGIS | [#33585](https://github.com/qgis/QGIS/issues/33585) | [PR #33992](https://github.com/qgis/QGIS/pull/33992) | [PR #34290](https://github.com/qgis/QGIS/pull/34290) |
| QGIS fails to apply style file to rasters | [#29427](https://github.com/qgis/QGIS/issues/29427) | no change required, but still investigating |  |
| copy / paste feature does not work correctly for MultilinestringZ | [#33977](https://github.com/qgis/QGIS/issues/33977) | works for me in current master |  |
| Edit Form shows and saves raw default-values from geopackage, spatialite or sqlite | [#33383](https://github.com/qgis/QGIS/issues/33383) | [PR #34012](https://github.com/qgis/QGIS/pull/34012) | [PR #34298](https://github.com/qgis/QGIS/pull/34298) |
| Not possible to uncheck layers in Order Panel | [#33854](https://github.com/qgis/QGIS/issues/33854) | [PR #34015](https://github.com/qgis/QGIS/pull/34015) | [PR #34288](https://github.com/qgis/QGIS/pull/34288) |
| PostgreSQL identity column not recognized properly | [#29560](https://github.com/qgis/QGIS/issues/29560) | [PR #34017](https://github.com/qgis/QGIS/pull/34017) | [PR #34291](https://github.com/qgis/QGIS/pull/34291) |
| Spatialite provider does not recognize autoincrement PKs when table definition uses backticks | [#34085](https://github.com/qgis/QGIS/issues/34085) | [PR #34012](https://github.com/qgis/QGIS/pull/34012) | [PR #34298](https://github.com/qgis/QGIS/pull/34298) |
| QGIS crash when I click on the button \"Manage Map Themes\" | [#33295](https://github.com/qgis/QGIS/issues/33295) | [PR #34090](https://github.com/qgis/QGIS/pull/34090) | [PR #34098](https://github.com/qgis/QGIS/pull/34098) |
| QGIS Server - WMS Request GetPrint fails with ATLAS_PK | [#30817](https://github.com/qgis/QGIS/issues/30817) | works for me in current master |  |
| QGIS 3.10.2 replace 0 to NULL | [#34118](https://github.com/qgis/QGIS/issues/34118) | [PR #34152](https://github.com/qgis/QGIS/pull/34152) | [PR #34292](https://github.com/qgis/QGIS/pull/34292) |
| Representation for NULL values inconsistent use/display | [#28643](https://github.com/qgis/QGIS/issues/28643) | [PR #34157](https://github.com/qgis/QGIS/pull/34157) | [PR #34293](https://github.com/qgis/QGIS/pull/34293) |
| DB Manager in 3.11 Master can\'t connect to PostGIS Enabled database | [#34132](https://github.com/qgis/QGIS/issues/34132) | [PR #34171](https://github.com/qgis/QGIS/pull/34171) | N/A |
| QGIS doesn\'t respect OGC guidelines for KVP parameters | [#34148](https://github.com/qgis/QGIS/issues/34148) | [PR #34175](https://github.com/qgis/QGIS/pull/34175) | [PR #34294](https://github.com/qgis/QGIS/pull/34294) |
| QGIS 3.10 can\'t find pkey of postgres views | [#34167](https://github.com/qgis/QGIS/issues/34167) | [PR #34179](https://github.com/qgis/QGIS/pull/34179) | [PR #34295](https://github.com/qgis/QGIS/pull/34295) |
| Duplicating a scratch layer ignores added fields | [#34134](https://github.com/qgis/QGIS/issues/34134) | [PR #34199](https://github.com/qgis/QGIS/pull/34199) | [PR #34203](https://github.com/qgis/QGIS/pull/34203) |
| QGIS master project XML is invalid | [#34218](https://github.com/qgis/QGIS/issues/34218) | [PR #34219](https://github.com/qgis/QGIS/pull/34219) | [PR #34297](https://github.com/qgis/QGIS/pull/34297) |
| Full row conditional formatting formats wrong full rows | [#34122](https://github.com/qgis/QGIS/issues/34122) | [PR #34305](https://github.com/qgis/QGIS/pull/34305) | [PR #34315](https://github.com/qgis/QGIS/pull/34315) |
| filter expression error returns true | [#34259](https://github.com/qgis/QGIS/issues/34259) | [PR #34309](https://github.com/qgis/QGIS/pull/34309) | [PR #34512](https://github.com/qgis/QGIS/pull/34512) |
| Fields are shifted when importing a layer with an FID attribute into GeoPackage | [#32927](https://github.com/qgis/QGIS/issues/32927) | [PR #32934](https://github.com/qgis/QGIS/pull/32934) | N/A |
| \"split features\" of PostGIS layers become slow since 3.6 | [#34326](https://github.com/qgis/QGIS/issues/34326) | closed: cannot reproduce with any of the (several) provided datasets |  |
| Cannot add/save more than 1 record/feature in a Spatialite layer/table | [#34379](https://github.com/qgis/QGIS/issues/34379) | [PR #34423](https://github.com/qgis/QGIS/pull/34423) | [PR #34513](https://github.com/qgis/QGIS/pull/34513) |
| QGIS crashes when changing \"default value\" in layer property on a point scratch layer, after editing feature | [#34404](https://github.com/qgis/QGIS/issues/34404) | [PR #34428](https://github.com/qgis/QGIS/pull/34428) | [PR #34514](https://github.com/qgis/QGIS/pull/34514) |
| Raster calculator turns one row of pixels into nodata | [#34435](https://github.com/qgis/QGIS/issues/34435) | [PR #34460](https://github.com/qgis/QGIS/pull/34460) | [PR #34511](https://github.com/qgis/QGIS/pull/34511) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Alessandro Pasotti](https://www.itopen.it/)
### 機能: Sandro Santilliによるバグ修正
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| repository files modified by \'make check\' | [#25830](https://github.com/qgis/QGIS/issues/25830) |  |  |
| Runs of testsuite leaves hundreds of directories in \~/.local/share | [#34185](https://github.com/qgis/QGIS/issues/34185) | [Commit 96a7fb8](https://github.com/qgis/QGIS/commit/96a7fb8f5acf3a278919f88c7c5abc4d20b8b6c2) | N/A |
| Drop use of deprecated QgsCoordinateReferenceSystem constructor | [PR #34186](https://github.com/qgis/QGIS/pull/34186) | [Commit b4fa419](https://github.com/qgis/QGIS/commit/b4fa419f7654ea7d1bce666b99f0534c415d8634) | N/A |
| Only look for pointcloud in its installed extension schema | [#33509](https://github.com/qgis/QGIS/issues/33509) | [Commit 1f44b29](https://github.com/qgis/QGIS/commit/1f44b29933bff3b8806bba75b761dd47b6c349c8) | N/A |
| QGIS 3.10 unable to load PostGIS-table on MacOS Catalina | [#32558](https://github.com/qgis/QGIS/issues/32558) | [Commit d15ce6b](https://github.com/qgis/QGIS/commit/d15ce6b4c30f9faed8b818c575d6b729192fa064) | [Commit a06b164](https://github.com/qgis/QGIS/commit/a06b164b5465ee7a0f8509e737d7c71ea7c166db) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

この機能はSandro Santilliによって開発されました
### 機能: Even Rouault によるバグ修正
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Crash when applying wrong filter to OAFeat layer | [#33878](https://github.com/qgis/QGIS/issues/33878) | [PR #33927](https://github.com/qgis/QGIS/pull/33927) | [PR #33958](https://github.com/qgis/QGIS/pull/33958) |
| Oracle provider: fix compiler warnings | - | [PR #33930](https://github.com/qgis/QGIS/pull/33930) | - |
| Cannot import 3D vector into Spatialite datasource (works for GPKG) | [#33883](https://github.com/qgis/QGIS/issues/33883) | [PR #33938](https://github.com/qgis/QGIS/pull/33938) | [PR #33945](https://github.com/qgis/QGIS/pull/33945) |
| \[Oracle\] Fix MultiSurface with straight polygon | - | [PR #33959](https://github.com/qgis/QGIS/pull/33959) | not doable |
| Geometries stored in Oracle table fail sdo_geom.validate_geometry_with_context(..) check | [#29085](https://github.com/qgis/QGIS/issues/29085) | [PR #33959](https://github.com/qgis/QGIS/pull/33959) | not doable |
| QGIS WFS / OGC API -- Features not showing list typed attributes correctly | [#33758](https://github.com/qgis/QGIS/issues/33758) | [PR #33983](https://github.com/qgis/QGIS/pull/33983) | N/A |
| Legend causing a crash | [#32913](https://github.com/qgis/QGIS/issues/32913) | [PR #34004](https://github.com/qgis/QGIS/pull/34004) | [PR #34063](https://github.com/qgis/QGIS/pull/34063) |
| Draw effects units setting doesn\'t persist | [#34089](https://github.com/qgis/QGIS/issues/34089) | [PR #34135](https://github.com/qgis/QGIS/pull/34135) | [PR #34151](https://github.com/qgis/QGIS/pull/34151) |
| Bad georeferencing of OZI .map | [#34299](https://github.com/qgis/QGIS/issues/34299) | [GDAL commit](https://github.com/OSGeo/gdal/commit/7bedf61bbb8d8c331642b44f30c083abb43f4085) | - |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Even Rouault](http://www.spatialys.com/)
### 機能: Alexander Bruyによるバグ修正
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Remove verbose wording on layout toolbar buttons | [#30161](https://github.com/qgis/QGIS/issues/30161) | [PR #33912](https://github.com/qgis/QGIS/pull/33912) |  |
| Unable to paste a layer in an empty project | [#26710](https://github.com/qgis/QGIS/issues/26710) | [PR #33961](https://github.com/qgis/QGIS/pull/33961) | [PR #33965](https://github.com/qgis/QGIS/pull/33965) |
| データベースマネージャ: 新しいレイヤが生成されたとき、レイヤを作成するダイアログは閉じるかクリアされるべき | [#25535](https://github.com/qgis/QGIS/issues/25535) | [PR #33910](https://github.com/qgis/QGIS/pull/33910) |  |
| Two different default shortcuts for the Layer styling panel (F7 vs Ctrl+3) | [#26696](https://github.com/qgis/QGIS/issues/26696) | [PR #33984](https://github.com/qgis/QGIS/pull/33984) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

この機能はAlexander Bruyによって開発されました
### 機能: Paul Blottiereによるバグ修正
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fixes compilation on Arch Linux | 未報告 | [PR #34110](https://github.com/qgis/QGIS/pull/34110) | [PR #34146](https://github.com/qgis/QGIS/pull/34146) |

| Move labels doesn\'t work with GPKG QGIS 3.4 | [#30408](https://github.com/qgis/QGIS/issues/30408) | Closed (works on master and 3.10) | - |

| Auxiliary storage not usable in non editable layer | [#30376](https://github.com/qgis/QGIS/issues/30376) | Feedback (works on master and 3.10) | - |

| Labels Buffer DD options do not have fields set and do not render in map canvas | [#28544](https://github.com/qgis/QGIS/issues/28544) | [PR #34153](https://github.com/qgis/QGIS/pull/34153) | risky |

| QGIS does not load embedded layers when opening projects | [#34060](https://github.com/qgis/QGIS/issues/34060) | [PR #34311](https://github.com/qgis/QGIS/pull/34311) | [PR #34706](https://github.com/qgis/QGIS/pull/34706) |

| Embedded layers are duplicated after opening | Unreported | [PR #34311](https://github.com/qgis/QGIS/pull/34311) | [PR #34706](https://github.com/qgis/QGIS/pull/34706) |

| Raise log level of server exception | [Discussed on qgis-developers list](https://lists.osgeo.org/pipermail/qgis-developer/2020-February/060108.html) | [PR #34256](https://github.com/qgis/QGIS/pull/34256) | [PR #34539](https://github.com/qgis/QGIS/pull/34539) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Paul Blottiere](https://hytech-imaging.fr/)
### 機能: Denis Rouzaudによるバグ修正
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Crash with relations | [#33120](https://github.com/qgis/QGIS/issues/33120) | [PR #34255](https://github.com/qgis/QGIS/pull/34255) | - |
| Crash with relations V2 | [#33120](https://github.com/qgis/QGIS/issues/33120) | [PR #34403](https://github.com/qgis/QGIS/pull/34403) | done |
| Fix map layer actions rendering in attribute table | 未報告 | [PR #34266](https://github.com/qgis/QGIS/pull/34266) | done |
| DnD improvements (sync selections) | [#28570](https://github.com/qgis/QGIS/issues/28570) | [PR #34411](https://github.com/qgis/QGIS/pull/34411) | TODO? |
| DnD improvements (container config) | [#29063](https://github.com/qgis/QGIS/issues/29063) | [PR #34433](https://github.com/qgis/QGIS/pull/34433) |  |
| DnD improvements (do not hide behind double click) | [#29063](https://github.com/qgis/QGIS/issues/29063) | [PR #34479](https://github.com/qgis/QGIS/pull/34479) |  |
| disable browsing auto pan/scale in attribute table when showing visible features only | [#34486](https://github.com/qgis/QGIS/issues/34486) | [PR #34493](https://github.com/qgis/QGIS/pull/34493) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Denis Rouzaud](https://www.opengis.ch/)
### 機能: Julien Cabiecesによるバグ修正
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Snapping and vertex tool not working with some layers if snapping was enabled when loaded | [#33449](https://github.com/qgis/QGIS/issues/33449) | [PR #33757](https://github.com/qgis/QGIS/pull/33757) | N/A |
| Snapping not possible in new project with new layer | [#32969](https://github.com/qgis/QGIS/issues/32969) | 重複 | - |
| Vertex Tool cache not refreshing after changes to line features | [#33947](https://github.com/qgis/QGIS/issues/33947) | Won\'t fix | - |
| \"fill ring\" do not trigger the correct computation of the area in the \"default value\" expression | [#32377](https://github.com/qgis/QGIS/issues/32377) | Closed (fixed in 3.10 and master) | - |
| \"view feature form\" opens the wrong feature/record | [#33880](https://github.com/qgis/QGIS/issues/33880) | [PR #34009](https://github.com/qgis/QGIS/pull/34009) | TODO |
| setFilterExpression and QGIS Filter output different results | [#33454](https://github.com/qgis/QGIS/issues/33454) | Closed (not a QGIS issue) | - |
| Crash while using Oracle views with primary key defined as number without precision | [#31626](https://github.com/qgis/QGIS/issues/31626) | [PR #34312](https://github.com/qgis/QGIS/pull/34312) | TODO |
| WCS client stopped working on a specific service from 2.18 to 3.x | [#33339](https://github.com/qgis/QGIS/issues/33339) | [PR #34300](https://github.com/qgis/QGIS/pull/34300) | TODO |
| Crash in relation reference test | [#34779](https://github.com/qgis/QGIS/issues/34779) | [PR #34822](https://github.com/qgis/QGIS/pull/34822) | TODO |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Julien Cabieces](https://www.oslandia.com/)
### 機能: Bertrand Rixによるバグ修正
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Snapping and vertex tool not working with some layers if snapping was enabled when loaded | [#33449](https://github.com/qgis/QGIS/issues/33449) | [PR #33757](https://github.com/qgis/QGIS/pull/33757) | N/A |
| Snapping not possible in new project with new layer | [#32969](https://github.com/qgis/QGIS/issues/32969) | 重複 | - |
| Vertex Tool cache not refreshing after changes to line features | [#33947](https://github.com/qgis/QGIS/issues/33947) | Won\'t fix | - |
| \"fill ring\" do not trigger the correct computation of the area in the \"default value\" expression | [#32377](https://github.com/qgis/QGIS/issues/32377) | Closed (fixed in 3.10 and master) | - |
| \"view feature form\" opens the wrong feature/record | [#33880](https://github.com/qgis/QGIS/issues/33880) | [PR #34009](https://github.com/qgis/QGIS/pull/34009) | TODO |
| setFilterExpression and QGIS Filter output different results | [#33454](https://github.com/qgis/QGIS/issues/33454) | Closed (not a QGIS issue) | - |
| Crash while using Oracle views with primary key defined as number without precision | [#31626](https://github.com/qgis/QGIS/issues/31626) | [PR #34312](https://github.com/qgis/QGIS/pull/34312) | TODO |
| WCS client stopped working on a specific service from 2.18 to 3.x | [#33339](https://github.com/qgis/QGIS/issues/33339) | [PR #34300](https://github.com/qgis/QGIS/pull/34300) | TODO |
| Crash in relation reference test | [#34779](https://github.com/qgis/QGIS/issues/34779) | [PR #34822](https://github.com/qgis/QGIS/pull/34822) | TODO |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Bertrand Rix](https://www.oslandia.com/)
### 機能: Loïc Bartoletti によるバグ修正
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Close vertex for line when editing | [#32359](https://github.com/qgis/QGIS/issues/32359) | [PR #34217](https://github.com/qgis/QGIS/pull/34217) | [PR #34285](https://github.com/qgis/QGIS/pull/34285) |
| Fix Grass linking on FreeBSD | reported on FreeBSD ML | [PR #34088](https://github.com/qgis/QGIS/pull/34088) | [PR #34238](https://github.com/qgis/QGIS/pull/34238) |
| \[Regular Shape\] Allow undo click when digitizing new features | [#25597](https://github.com/qgis/QGIS/issues/25597) | [PR #34080](https://github.com/qgis/QGIS/pull/34080) | [PR #34302](https://github.com/qgis/QGIS/pull/34302) |
| Remove Added Vertex with Add Circular String | [#29688](https://github.com/qgis/QGIS/issues/29688) | [PR #34058](https://github.com/qgis/QGIS/pull/34058) | [PR #34301](https://github.com/qgis/QGIS/pull/34301) |
| Rubberband not working correctly with \"Shapes\" digtizing in rotated map window | [#33287](https://github.com/qgis/QGIS/issues/33287) | 重複 |  |
| Digitizing: LineStringZ does not inherit Z-coordinates from points if line starts by snapping to a point with no Z coordinate | [#33201](https://github.com/qgis/QGIS/issues/33201) | [PR #33642](https://github.com/qgis/QGIS/pull/33642) | [PR #33951](https://github.com/qgis/QGIS/pull/33951) |
| Split feature makes QGIS 3.4.6 crash | [#33408](https://github.com/qgis/QGIS/issues/33408) | 修正済み |  |
| Fix oriented minimum bounding box algorithm | [#33532](https://github.com/qgis/QGIS/issues/33532) | [PR #34334](https://github.com/qgis/QGIS/pull/34334) | [PR #34338](https://github.com/qgis/QGIS/pull/34338) |
| error with returned angle by orientedMinimumBoundingBox() | [#31371](https://github.com/qgis/QGIS/issues/31371) | Closed. Lacks of feedback |  |
| Fix build with txt2tags \>= 3.5 | directly reported by FreeBSD qgis maintainer | [PR #34377](https://github.com/qgis/QGIS/pull/34377) | [PR #34389](https://github.com/qgis/QGIS/pull/34389) |
| Fix identify menu when an expression is used as display name | 未報告 | [PR #34361](https://github.com/qgis/QGIS/pull/34361) | [PR #34402](https://github.com/qgis/QGIS/pull/34402) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Loïc Bartoletti](https://www.oslandia.com/)
### 機能: Sebastien Peilletによるバグ修正
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Extend line does not work in compoundCurvedZ layer | [#32080](https://github.com/qgis/QGIS/issues/32080) | [PR #34055](https://github.com/qgis/QGIS/pull/34055) |  |
| Feature attribute selection design bug | [#29542](https://github.com/qgis/QGIS/issues/29542) | [PR #34359](https://github.com/qgis/QGIS/pull/34359) |  |
| Unable to add a new feature when joining two PostGIS tables | [#33148](https://github.com/qgis/QGIS/issues/33148) | [PR #34216](https://github.com/qgis/QGIS/pull/34216) |  |
| Copy/Paste fails from one layer to another when layer has NOT NULL constraints and transaction groups are enabled | [#29603](https://github.com/qgis/QGIS/issues/29603) | Already fixed by [PR #33688](https://github.com/qgis/QGIS/pull/33688) |  |
| QGIS freezes when creating new shapefiles | [#32069](https://github.com/qgis/QGIS/issues/32069) | 修正済み |  |
| Oracle : tables are listed once for Polygons and once for MultiPolygons but both show all geometries | [#32521](https://github.com/qgis/QGIS/issues/32521) | [PR #34358](https://github.com/qgis/QGIS/pull/34358) |  |
| BUG: fix invalid layer result when Oracle version is under 12 | 未報告 | [PR #34546](https://github.com/qgis/QGIS/pull/34546) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Sebastien Peillet](https://www.oslandia.com/)
### 機能: Nyall Dawsonによるバグ修正
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fix IN/NOT IN evaluation with very long number like strings | [#34314](https://github.com/qgis/QGIS/issues/34314) | [Commit 167e0de](https://github.com/qgis/QGIS/commit/167e0de65b0106a3c19181a2c415c2b0ba0da117) | [Commit aca059a](https://github.com/qgis/QGIS/commit/aca059a82021cb05b58664d3b0f2db751b8f37df) |
| \[processing\] Define Layer Projection tool should write .prj files using ESRI WKT1 format | [#34007](https://github.com/qgis/QGIS/issues/34007) | [Commit f41dd11e](https://github.com/qgis/QGIS/commit/f41dd11e9214b4d6ca5dcc31c6612a65d134ce83) | Submitted |
| Show \'unknown CRS\' in status bar instead of blank text when project is set to an unknown CRS | [#33458](https://github.com/qgis/QGIS/issues/33458) | [Commit c6319b2](https://github.com/qgis/QGIS/commit/c6319b263992c9d52646096d851cab6c674125ff) | Submitted |
| Don\'t force users to make a choice in the datum transform dialog | [#34234](https://github.com/qgis/QGIS/issues/34234) | [Commit 644a552](https://github.com/qgis/QGIS/commit/644a5525ec08a77b4c703a7066c94802bbfa1036) | Submitted |
| Fix crash when changing raster data source | [#34231](https://github.com/qgis/QGIS/issues/34231) | [Commit caf334e6](https://github.com/qgis/QGIS/commit/caf334e65b11f9ee1590f74fe395e97d92bbe699) | [Commit b4142c3](https://github.com/qgis/QGIS/commit/b4142c3832b9f14de97df08caf20a06dee12c02f) |
| Handle unit type \"m\" in custom WKT strings on proj 6 builds | [#34196](https://github.com/qgis/QGIS/issues/34196) | [Commit bb20cee](https://github.com/qgis/QGIS/commit/bb20cee00a931da46b830f0d1e9565d9863f9ba3) | [Commit 97c50f9](https://github.com/qgis/QGIS/commit/97c50f929fbbdd9b3eaef8f8bdf423f9daa3a163) |
| Show full CRS WKT for custom CRS in layer properties | [#33862](https://github.com/qgis/QGIS/issues/33862) | [Commit 19d58bda](https://github.com/qgis/QGIS/commit/19d58bda08c202b29020a3e9c485fac80350fc79) | [Commit 2908227](https://github.com/qgis/QGIS/commit/2908227f91ccfde245a0a608b50b7758b3eba8dd) |
| \[processing\] Fix modeler draws lines to wrong output when connecting green output boxes | 未報告 | [Commit 5ae9807](https://github.com/qgis/QGIS/commit/5ae9807303e909a504288d97a2efc4cc04a62670) | [Commit 528a45d](https://github.com/qgis/QGIS/commit/528a45d7453b7cbeb44450d5c81de80c8dd66611) |
| \[processing\] Fix Points Along Geometry handling of multipart geometries | [#34022](https://github.com/qgis/QGIS/issues/34022) | [Commit 3fb18a2](https://github.com/qgis/QGIS/commit/3fb18a2260cbc432e892a4dacbae0092a775ec9d) | [Commit ac3b446](https://github.com/qgis/QGIS/commit/ac3b446aead90d5ea5cab101807859e5ce6f1b44) |
| \[processing\] Fix QStringList values are not accepted as valid values for multi-field parameters | 未報告 | [Commit abcb8d2](https://github.com/qgis/QGIS/commit/abcb8d20c66b3c235802b10e68d6abc34736e2c5) | [Commit d421313](https://github.com/qgis/QGIS/commit/d421313f05fd0e5a6974568eccd36c4213f41f8f) |
| \[processing\] Fix some field names are rejected in modeler for non-multi field parameters | 未報告 | [Commit 9bcd980](https://github.com/qgis/QGIS/commit/9bcd98094c015265e7e94c55f248248e56c24e51) | N/A - 3.12 only |
| Fix crash in server feature info | 未報告 | [Commit b3f37fde](https://github.com/qgis/QGIS/commit/b3f37fde9bc4785aebca29e6553d6c1de715f523) | Submitted |
| Fix overflow by assigning double max to float, invalid min | 未報告 | [Commit 2b15e255](https://github.com/qgis/QGIS/commit/2b15e255eaf63f1d45b8e963fca7f9f9e4bf8d40) | N/A - 3.12 only |
| Fix crash in QgsGeometryDuplicateCheck due to heap use after free | 未報告 | [Commit 195576e](https://github.com/qgis/QGIS/commit/195576e57f0aff064e962ce16b37533ab4924dce) | [Commit dc647bc](https://github.com/qgis/QGIS/commit/dc647bc56fb37207a75d55638926e7a2db75a8be) |
| Fix crash on destruction of QgsPointLocator, if object is destroyed while indexing is happening in the background | 未報告 | [Commit 08adb23](https://github.com/qgis/QGIS/commit/08adb23a7ec284a2f84ecf7ac469fbe9004ab57e) | N/A - 3.12 only |
| Fix crashes when reading certain resampled raster files | [#33711](https://github.com/qgis/QGIS/issues/33711) | [Commit b2c5a45](https://github.com/qgis/QGIS/commit/b2c5a456fa4e9613ac33b8aaaed774ad3b7293a1) | [Commit 388277e](https://github.com/qgis/QGIS/commit/388277e642d99b93bd7f25197d6418b5dfb888bd) |
| Fix use after free in 3d point symbol | 未報告 | [Commit df7979c](https://github.com/qgis/QGIS/commit/df7979cf94c43352cd10db97c16075b8816ec6c4) | [Commit 7204de2](https://github.com/qgis/QGIS/commit/7204de27f3305146fbd6f8e32355c365030afc31) |
| Fix leaks in geometry generator symbol layer | 未報告 | [Commit 1610fb8](https://github.com/qgis/QGIS/commit/1610fb8766a13351bb303ee3bfd6301dbdc6648b) | [Commit 3944db4](https://github.com/qgis/QGIS/commit/3944db47dda6b08ea4b22f61c5e72d97597362b1) |
| Fix crash in rendering on proj 6 builds | [#33902](https://github.com/qgis/QGIS/issues/33902) | [Commit 8a71091](https://github.com/qgis/QGIS/commit/8a7109163a9362af2a5e0187cf2b57fc0219fe59) | [Commit f41076d](https://github.com/qgis/QGIS/commit/f41076d45f5f259c50e3ead2cac4d664be11bbfb) |
| Don\'t try to label empty geometries | [#33931](https://github.com/qgis/QGIS/issues/33931) | [Commit 1144974](https://github.com/qgis/QGIS/commit/11449743788f3fd346c01c46cff01bcf3f84edf0) | N/A - 3.12 only |
| Fix crashes when attempting to export reprojected raster layers | [#33801](https://github.com/qgis/QGIS/issues/33801) | [Commit bbd055c](https://github.com/qgis/QGIS/commit/bbd055ca13a3d6ee150251222d73e3b9e76d94c5) | [Commit 2fff8e1](https://github.com/qgis/QGIS/commit/2fff8e1205daffafa257b9312cc2c005b5e3017e) |
| シェープファイルの符号化の問題を修正 | [#21264](https://github.com/qgis/QGIS/issues/21264) | Submitted | Held off to 3.10.4 |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Nyall Dawson](https://north-road.com/)

{{<content-end >}}
