---
HasBanner: false
draft: false
releaseDate: '2020-10-23'
section: project
sidebar: true
title: QGIS 3.16の変更履歴
type: visual-changelog

---
{{<content-start >}}
# QGIS 3.16の変更履歴{#changelog316 }
![image1](images/projects/dbc0cef663f2f652e0961ac2ed168eb45ed2e182.png)

リリース日: 2020-10-23

QGISプロジェクトのもう1つの素晴らしい日です！新しい長期サポートリリースは、QGISデスクトップとQGISサーバーの両方に幅広い機能をもたらします。このリリースでは、3Dマッピング、他のデータタイプからのメッシュ生成、追加の空間分析ツール、シンボル体系、ユーザーインターフェイスの拡張機能など、豊富な新しいオプションが提供されます。拡大し続ける処理フレームワークに多数のツールが組み込まれ、QGISブラウザーは、以前はDBManagerプラグイン用に予約されていた高度なデータベース対話機能をサポートするようになりました。これらは、このリリースから導入されたいくつかの改善点であり、以前のLTSのユーザーは、3.10以降に利用可能な膨大な数の新機能を見つけることができます。この新しいリリースの追加のハイライトのいくつかを以下に詳しく説明します。

**謝辞**

We would like to extend a big thank you to the developers, documenters, testers, and all the many folks out there who volunteer their time and effort (or fund people to do so) to make these releases possible. From the QGIS community, we hope you enjoy this release! If you wish to donate time, money, or otherwise get involved in making QGIS more awesome, please wander along to [QGIS.ORG](https://www.qgis.org/) and lend a hand!

QGIS is supported by donors and sustaining members. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://www.qgis.org/en/site/about/sustaining_members.html#list-of-donors). If you would like to become an official project sustaining member, please visit our [sustaining member page](https://www.qgis.org/en/site/getinvolved/governance/sustaining_members/sustaining_members.html#qgis-sustaining-memberships) for details. Sponsoring QGIS helps us to fund our regular developer meetings, maintain project infrastructure, and fund bug fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

{{<fund type="active" >}}

QGIS はフリーのソフトウェアです。利用する上で金銭を支払う義務はありません。実際、私たちは利用者の財政状況や社会的地位にかかわらず、より多くの人に QGIS を利用して欲しいと思っています。私たちは地理空間的な意思決定ツールによって人々が力を持つことが、全人類の社会をより良くすると信じています。

{{<table-of-contents >}}
## 一般情報
### ユーザーグループイースターエッグの追加
Type the words \"user groups\" into the current coordinates window and watch the magic happen.

![image2](images/entries/079434bceb5004b0ee2c4ad5d62edd1290c28575.webp)

This feature was developed by [Germán Carrillo](https://github.com/gacarrillor)
## 時系列
### 時間アニメーションフレームをエクスポートする機能
後で外部アプリケーションでつなぎ合わせるために、一時的なアニメーションフレームを連続する画像にエクスポートできます。ユーザーは、画像サイズと地図範囲を正確に制御できます。

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
## ツール
### Go-Toロケータ
新しいgotoロケータフィルタを追加しました。

gotoインジケータは次の文字列を受け取ります:
- x座標とy座標のペア（カンマまたはスペースで区切られた）。
- OSM、Leaflet、またはOpenLayers形式のURL。
- Google maps URL。

XY文字列の論理は次のとおり:
- If the canvas CRS isn\'t WGS84:
  - もし座標がWGS84の範囲内に収まる場合、WGS84の結果を追加します（これは下記のキャンバスCRSの結果よりも優先度が高い重み付けされています）。
  - もし座標がキャンバスのCRS境界内に収まる場合、キャンバスのCRS結果を追加します。
- キャンバスのCRSがWGS84の場合:
  - もし座標がWGS84の範囲内に収まる場合、WGS84の結果を追加します。

![image3](images/entries/acb9e856ac744d0e40d8de33c025deb075385856.gif)

This feature was developed by [Mathieu Pellerin](https://api.github.com/users/nirvn)
## ユーザーインタフェース
### マップキャンバスにコンテキストメニューを追加
The map canvas now has a right-click context menu. By default, it creates the \"Copy Coordinate\" menu that was introduced with QGIS 3.14, however, it is expected that this functionality will be extended to allow many more functionalities to be accessed with spatial context in the future.

![image4](images/entries/f6e3ce9dca04583c9fa791204fe7e1a3c49c61d0.webp)

This feature was developed by [jakimowb](https://api.github.com/users/jakimowb)
## シンボロジ
### ベクタタイルのスタイリングの改善
複雑なベクタタイルスタイルの編集に関する複数の改善が導入されました:
- リスト内でツールチップを表示することで、列のサイズを変更しないでフィルタルールと名前が完全に見えます
- ウィジェット内で現在のキャンバスのズームレベルを表示します
- スタイルのリストをフィルタして現在表示されているものだけを表示できます
- シンボルを編集する際に、式のプレビューがうまく機能するように、正しいキャンバスのズームレベルを設定する

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### ユーザーがベクタタイル接続のデフォルトスタイルのURLをオプションで指定できる
When setting up a vector tile source connection, there\'s a new option to enter a URL to a MapBox GL JSON style configuration. If one has been entered, then that style will be applied whenever the layers from the connection are added to QGIS.

これは、ArcGISベクタタイルサービス接続でも機能します。これにより、サーバー設定で指定されたデフォルトのスタイル構成が使用されます。

![image5](images/entries/f93d5dca726eb94be82cc47479424b8fe42f5920.gif)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### 塗りつぶしシンボルレイヤにデータ定義オフセットが使える
任意の塗りつぶしシンボルレイヤは、シンプル塗りつぶし、ラスタ画像塗りつぶし、シェイプバーストおよびグラデーション塗りつぶしを含む、ポリゴンのオフセットをサポートしていますが、データ定義オフセットが可能になりました。

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### ベクタタイルレイヤにMapBox GL JSONスタイルをインポートします
ベクタタイルレイヤのスタイルファイルをインポートする際に、MapBox GL JSONスタイル設定ファイルを読み込むことができます

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### 事前に設定する量で直線の破線パターンをオフセットするオプションを見えるようにする
Allows for tweaking the positioning of dashes/spaces in the line, so that the dashes/spaces can be placed at nicer positions to account for corners in the line (also can be used potentially to \"align\" adjacent dash pattern borders).

オフセットは、マップ単位を含む様々な単位で設定することができ、またデータ定義も可能です。

This feature was funded by [Kanton Solothurn](https://geo.so.ch/)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### 直線シンボルレイヤの破線パターンを動的に調整できるオプションを追加します
オプションが追加され、破線パターンの微調整が可能になりました。これにより、ラインシンボルのレンダリング品質を向上させるより多くの制御が可能になります。これらのオプションには以下が含まれます:
- 破線パターンを線の長さに揃える：チェックを入れると、破線パターンの長さが微調整され、線がレンダリングされるとき、ギャップ要素や部分的なダッシュ要素ではなく、完全なダッシュ要素で終わるようになります。
- Tweak dash pattern at sharp corners: If checked, this option dynamically adjusts the dash pattern placement so that sharp corners are represented by a full dash element coming into and out of the sharp corner. It\'s designed to better represent the underlying geometry while rendering dashed lines, especially for jagged lines.

The following images illustrate the \"Align dash pattern to line length\" change in action, with yellow lines indicating the true start and end position of the line features being symbolised.

実行前:

![image6](images/entries/87635346-39f11c00-c782-11ea-88bc-369866d7f57a.webp)

実行後:

![image7](images/entries/87635368-44131a80-c782-11ea-95d9-07fb7d00ffcf.webp)

![image8](images/entries/e1a4d82c248cdd0f04f236443897178c12574885.gif)

This feature was funded by [Kanton Solothurn](https://geo.so.ch/)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### スタイルマネージャによって3Dシンボルを管理する
QGISスタイルマネージャを介して3Dシンボルを管理するサポートが追加されました。これには、3Dシンボルのインポートとエクスポートライブラリの対応も含まれており、3Dシンボルとそのウィジェットハンドラを完全に抽象化する最近の作業を完了しました。

残念ながら、ライブラリ内の3Dシンボルにはサムネイルが生成されておらず、当面は全ての3Dシンボルに一般的なアイコンが使用されています。サムネイルの生成は容易な問題ではないので、当面は延期されています。

This feature addresses the issue raised in [31479](https://github.com/qgis/QGIS/issues/31479).

![image9](images/entries/7e4ee802abba7dfd7ec61cdd8b3db333b7a30fae.gif)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
## ラベリング
### ユーザーがライン地物に沿ってラベルの配置を制御できるオプションを追加
A new \"Label Anchoring\" section in the line placement settings for labels allows users to specify whether labels should be placed at the center, start or end of lines. In addition, it allows offsets of these positions (based on the percentage of the feature length), which may be defined statically or by using a data-defined definition.

![image10](images/entries/f5cc643fc4eafe75053c134b245e91d2e72e33d0.gif)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### ラインのラベルのアンカーポイントを制御する
ライン地物のラベル付けのアンカーポイントがヒントか厳密な要件かを制御できる新しいオプションが公開さました。結果として、以下の動作変更が含まれます:
- 厳格: ラベルはラベルアンカーのみに正確に配置され、他のフォールバック配置は許されません。
- ヒント：ラベルアンカーは、優先されるラベルの配置のヒントとして扱われますが、アンカーポイントに近い他の配置も許されます。

![image11](images/entries/a6c67225ee3b55a021a395ffbf58bd05352ef6fb.gif)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
## ダイアグラム
### 積み上げ棒グラフに軸をレンダリングする
これは、軸が設定された場合に、積み上げ棒グラフ図に軸をレンダリングするサポートを追加します。実装はヒストグラム図の軸のレンダリングを基にしています。

負の値は、軸の表示の有無に関係なく、積み上げ棒グラフで適切に処理されません。

Addresses [Issue 34915](https://github.com/qgis/QGIS/issues/34915)

![image12](images/entries/09739c5bed021a99baec41c98b87f5335a4bf8ec.webp)

This feature was developed by [Dan Minor](https://api.github.com/users/dminor)
## メッシュ
### 永続性を備えたインメモリメッシュデータセット
この機能は、メッシュレイヤにインメモリデータセットグループを作る機能を導入します。これらのデータセットグループは一時的であり、プロジェクトが閉じられると保持されません。

新しいオプションがメッシュ計算機に追加されました。これにより、インメモリデータセットグループを作ることができます。

この機能は、メモリデータセットグループを削除したり、指定されたドライバでファイルに保存する機能も導入します。

![image13](images/entries/85622744-4d9edc00-b635-11ea-91db-a02fa28e6bea.gif)

![image14](images/entries/b27519025102be3b07fc8241f0ff8f8f2f9b31c6.webp)

This feature was funded by [Artelia Group](https://www.arteliagroup.com/en)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk)
### メッシュレイヤの複数識別
識別ツールはメッシュレイヤで使用する場合に適合され、すべてのデータセットグループの時系列コントローラの現在の時刻に対応するデータセット値を表示するようになりました。アクティブなデータセットグループ（スカラー、最終的にはベクトル）が最初に表示され、次に他のデータセットグループが表示されます。次のような他の情報も表示されます。
- データセットが保存されているソース
- 表示されるデータセットのタイムステップ（時系列コントローラの時刻と異なる場合があります）。データセットグループが時系列でない場合は何も表示しません。
- 対応する面の重心
- スナップした頂点の座標（スナップされているとき）
- スナップした辺の中央（スナップされているとき）

マップキャンバスで時系列ナビゲーションが有効になっていない場合、識別結果には、メッシュプロパティダイアログで定義された静的データセットを持つアクティブなデータセットグループに関する情報のみが含まれます。

![image15](images/entries/c4974747f5bc0dcba02f30a97e68bb5edacc5f48.webp)

This feature was funded by [Artelia Group](https://www.arteliagroup.com/en)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk)
### メッシュレイヤの仮想データセットグループ
The ability to use \"virtual\" data set groups has been introduced for mesh layers. This replaces the \"memory\" dataset group used in [37389](https://github.com/qgis/QGIS/pull/37389).

With the mesh calculator, users may choose to create those \"virtual\" dataset groups that will be added to the layer. Values are not stored in memory but each dataset is rather calculated when needed with the formula entered in the mesh calculator.

プロジェクト内には、これらの仮想データセットグループが保存され、永続化のために削除またはファイルに保存されます。

永続的なデータセットグループと仮想データセットグループは、メッシュレイヤのプロパティのソースタブで、各アイテムの背景色の変更によって区別されます。それぞれのアイテムは以下のように示されます:

永続的: 黄色

仮想: 紫

![image16](images/entries/86540129-a8a3bf00-bed0-11ea-94b8-bf29b5818cb8.gif)

![image17](images/entries/803983acbaec38e8df0fb4fd12d28beef7399520.webp)

This feature was funded by [Artelia Group](https://www.arteliagroup.com/en)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk)
### QgsMeshメソッドにエクスポートを追加
三角形分割をQgsMeshインスタンスにエクスポートするメソッドが追加され、既存のポイントとラインから三角形分割を使用してメッシュレイヤを構築できるようになりました。これは、他の地図レイヤからQgsMeshを取得できるようにするための最初のステップです。

三角形分割とDualEdgeTriangulationクラスも、QGISのコードとより一貫性のあるように、名前が変更され、リファクタリングされました。
- 三角形分割をQgsMeshインスタンスにエクスポートするメソッドを追加する。

This feature was developed by [Vincent Cloarec](https://api.github.com/users/vcloarec)
### TINメッシュの作成
TINメッシュレイヤをベクタレイヤデータ（頂点および/または破線）から作成できます。結果のメッシュは、制約付きドロネー三角形分割で作成されます。このメッシュレイヤは、Python APIを使用するか、処理ツールボックスのアルゴリズムを使用して作成できます。

![image18](images/entries/fc8a9633b87b29bba052dacd166c0735b4449c90.webp)

This feature was developed by [Vincent Cloarec](https://api.github.com/users/vcloarec)
## レンダリング
### ラスタレイヤのガンマ補正フィルタ
既存の明るさ、コントラスト、色相、彩度のフィルターに加えて、ラスターレイヤーのガンマ補正フィルターパイプを追加します。ユーザーは、スタイリングパネルやラスターツールバーの新しいボタンを使用して、レイヤーのプロパティダイアログからガンマ値を調整できます。デフォルトのガンマ値は1.0で、0.1から10の範囲で調整できます。

Addresses [Issue 13512](https://github.com/qgis/QGIS/issues/34915)

Also adds a rendering test for brightness and contrast filter which has no test at all and fixes some deprecation warnings in the Python test for `QgsRasterLayer`.

![image19](images/entries/bf6076062db63bc4c789bc18d3b029c14b2ddc8e.gif)

This feature was developed by [Alexander Bruy](https://api.github.com/users/alexbruy)
## 三次元機能
### スタイル/プロジェクトに3D素材のテクスチャファイルを埋め込むことができる
いくつかのAPIとコードの小さなクリーンアップが行われ、また、プロジェクト内に埋め込むために3DテクスチャファイルにQgsImageCacheの使用が導入されました。

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### シャドーレンダリング
3Dビューで影をレンダリングできるようになりました。

![image20](images/entries/ef724bf261c7740d3cc92238d71d5ecb32a190c3.webp)

This feature was developed by [Nedjima Belgacem](https://api.github.com/users/NEDJIMAbelgacem)
### 3Dシーンのエクスポート
3Dシーンをエクスポートして、Blenderなどの他の3Dソフトウェアで使用できるようになりました。このエクスポート機能は、出力解像度の指定による出力モデルの簡略化、オプションのモデルスムージング、3Dベクトルレイヤーのエクスポートなど、複数の追加機能をサポートします。

![image21](images/entries/91c112ba42358124faec9c3427542524d6b593f9.webp)

This feature was developed by [Nedjima Belgacem](https://api.github.com/users/NEDJIMAbelgacem)
### QGIS 3Dの方向光源の対応
QGIS 3Dに方向光源を追加
- 3Dビューに方向光源を追加することができるようになりました。
- 3D設定ダイアログの光源セクションの下にタブウィジェットを追加しました。
- ユーザーは、光の方向、色、強度を指定することができます。
- これは、いくつかの変更が加えられた、既存の点光源の実装の単なる複製です。
- Later it may be useful to add a way to visualize the light direction by displaying a mesh that is positioned at camera\'s view point like an arrow that displays how the sun lights the scene for example.

![image22](images/entries/4dcd7d7f4bcfb71d765656bfe734ec32ddcaca9c.webp)

This feature was developed by [Nedjima Belgacem](https://api.github.com/users/NEDJIMAbelgacem)
### ベクタレイヤのテクスチャリングに対応
以下の新機能を持つテクスチャリングの対応がQGIS 3Dに追加されました:
- ユーザーは、シンボルのプロパティから拡散マップとして建物の表面に表示する画像を選択できるようになりました。
- ユーザーは、シンボルのプロパティからテクスチャの縮尺を変更することもできます。

Some visual issues may appear when using textures. These issues relate to the normals of surfaces that you may be able to fix by checking \"add back faces\" and playing around with the invert normals and culling mode in the symbol properties.

![image23](images/entries/1c4fc6ffc1b7a28aeff9c625fb6238998dd30b67.webp)

This feature was developed by [Nedjima Belgacem](https://api.github.com/users/NEDJIMAbelgacem)
### 3Dポイントシンボルに、埋め込みおよびリモートの3Dモデルを利用できます
ユーザーは、3Dポイントシンボルのためにリモートの3Dモデルを利用および埋め込むことができます。

![image24](images/entries/d4deaabbeddcf5f4784f602f19dabfac22b2d100.webp)

This feature was developed by [Mathieu Pellerin](https://api.github.com/users/nirvn)
### 光源を表示するオプションを追加
3Dシーンの光源の原点にある可視の球体を切り替える機能。

シーンの内容に対する光源の再配置と配置がより簡単に行えるようになります。

Addresses [Issue #37726](https://github.com/qgis/QGIS/issues/37726).

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### マテリアルの取扱いの改善
マテリアルの取扱いに関する更なる改善が行われ、Goochシェーディングモデルが追加されました。これにより、QgsAbstractMaterialSettings API が改善されます:
- 登録されたマテリアル型にアイコンのサポートを追加します（マテリアル選択コンボボックスで使うため）。
- Adds support for handling different rendering techniques to QgsAbstractMaterialSettings. Now material classes can indicate which rendering techniques they support (e.g. Triangles, Lines, InstancedPoints, etc.), and the material is only offered when it\'s compatible with the required technique.
- 特定のコンテキストで効果のない設定を表示しないように、goochマテリアルウィジェットの処理技術が改善されました（例えば、シンプルな2Dラインシンボルの環境色の選択肢以外を非表示にします）。
- A new material, \"Gooch\", was added. This material gives a CAD style 3D render, where the shading is not dependent on appropriate lighting setup in a scene and where the 3D details are always visible, regardless of the lighting choice.

![image25](images/entries/b6df518d57147bfdfd207d4499363c9d4653721b.webp)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
## 印刷レイアウト
### 手動のテキストテーブルで、個々のセルのテキスト形式と配置の制御を見えるようにします
個々のセルの内容に対して、テキストの形式（例：太字/斜体/バッファ/シャドウなど）とテキストの配置（水平および垂直）を設定するための制御を、手動のテキストテーブルに追加します。

この機能は City of Canning によって資金提供されました

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### 属性テーブルのテキストをレンダリングするためにQgsTextRendererを使います
属性テーブルのレイアウトで、バッファ、シャドウ、単語の間隔など、全てのテキストのフォーマットオプションを可能にします。

この機能は City of Canning によって資金提供されました

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### レイアウト内の地図グリッドテキストを描画するのにQgsTextRendererを使います
グリッドの注記に、バッファ、シャドウ、背景形状などが使えます

![image26](images/entries/86863750-26550e00-c10f-11ea-8dd4-1b740017949e.gif)

![image27](images/entries/349efbc988ccbf3499e18ec4453b637abf893c38.webp)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### レイアウトをPDFへエクスポートする時のPDF画像圧縮方法を制御するオプションを公開
オプションは、使用されるデフォルトのJPEG圧縮である非可逆圧縮と可逆圧縮（ほとんどの場合、より大きなファイルを作成しますが、プロの印刷出力やIllustratorなどの他の製品でのポストプロダクションにはるかに適しています）用です。

悪いニュースは、このオプションは、Qt 5.13以降のビルドでなければ利用できないということです。

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### 地図帳に自動切り抜き設定を追加
この機能により、現在の地図帳領域地物の境界で地図が切り抜かれるようにレイアウト地図アイテムの地図の切り抜きを有効にすることができます。

次のオプションがあります:
- 地図ごとに切り抜きを有効化するか無効化する
- 切り抜きの種類を指定する:
  - "Clip During Render Only": applies a painter based clip, so that portions of vector features which sit outside the atlas feature become invisible
  - "Clip Feature Before Render": applies the clip before rendering features, so borders of features which fall partially outside the atlas feature will still be visible on the boundary of the atlas feature
  - "Render Intersecting Features Unchanged": just renders all features which intersect the current atlas feature, but without clipping their geometry
- ラベルを地図帳地物の中に強制的に配置するか、外に配置するかを制御する
- 切り抜きをプロジェクトのレイヤの一部に制限し、一部のみが切り抜かれるようにします

![image28](images/entries/86433831-191ad680-bd3f-11ea-9289-cc6d2b3e2e11.gif)

![image29](images/entries/1f1343d09c75b0e1d131c25a79b905d7aaadbc35.webp)

この機能は City of Canning によって資金提供されました

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### 地図をレンダリングする際に適用するクリッピング領域を指定するAPIをQgsMapSettingsに追加します
現在、これはAPIのみの機能ですが、マップのレンダリングに使用できるクリッピング領域を指定するためのバックエンドの機能が追加されています。

Although primarily introduced in order to provide functionality which allows the automatic clipping of map elements to the current atlas feature geometry in print layouts, the API has been deliberately implemented in a manner that\'s very flexible to allow various use cases which require the clipping of regions during map render operations.

非ベクターレイヤの場合、クリッピングはQPainterのクリッピングパスを通じて適用されます。ベクターレイヤの場合、APIはクリッピングの適用方法に関する様々なオプションを公開しています。
1. As an \"intersects\" style test only: All vector features which intersect the path are rendered, without actually clipping the feature\'s geometry
2. By modifying the feature\'s geometry and clipping the geometry to the region: Any stroke or outline settings for the symbol will be rendered along the boundary of the clipping region, even if the feature actually partially falls outside this region.

または
1. ペインタークリップパスを使う: 地物は領域に切り抜かれますが、ペインターの時だけです。クリッピング領域外にある地物の境界は表示されません。

この機能は City of Canning によって資金提供されました

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### レイアウト凡例の最大マーカーサイズ
レイアウトの凡例ウィジェットに、最大マーカーサイズ（mm単位）を入力する機能を追加します。

場合によっては、ポイントレイヤが地図単位に基づいたシンボルサイズを使用する場合、レイアウトの凡例に表示されるポイントマーカーは非常に大きくなることがあります。この機能は、自動的な凡例の更新がまだアクティブな状態で、レイアウトの凡例ウィジェットに最大マーカーシンボルサイズの制限を設定する機能を追加します。

This feature was developed by [mhugent](https://api.github.com/users/mhugent)
### 手動のテキストテーブルのセルが式型の内容を持つことができます
手動のテキストテーブルの個々のセルがその内容を事前に設定された式から取得できるようにします。式は、セルがメタデータスタイルの値を計算および表示したり、集計に基づいた計算を行ったりするために、完全なレイアウトアイテムの式コンテキストにアクセスできます。

この機能は City of Canning によって資金提供されました

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### レイアウトマップをシェープに切り抜きます
新機能が導入され、レイアウト内のシェープまたはポリゴンアイテムにマップアイテムを切り抜くことができるようになり、レイアウト内で非矩形の地図が可能になります。

![image30](images/entries/88761088-c1428480-d1b1-11ea-90c0-a391d00b084d.gif)

![image31](images/entries/7179282b09e8d196251f543a9c5f059f89c701e2.webp)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### 回転した目盛り/注記の対応
Tick marks and annotations on a map frame in the print composer can now be rotated, allowing them to align with a rotated map frame as described in [issue 36904](https://github.com/qgis/QGIS/issues/36904). It works for both rotated maps and reprojected grids.

追加されたオプションは次のとおりです:
- 目盛:
  - 目盛を回転します（チェックが外れている場合、ティックは以前のように描画され、角度は考慮されません。）
  - 回転した目盛の配置（目盛りが一定の長さを持つか、直交に配置されるか）
  - Skip low angled ticks (an angle threshold below which ticks aren\'t drawn, so you can skip ticks for grid lines that are, for example, too close to being parallel with the map edge)
- 注記:
  - 目盛に平行（隣接／水平／垂直上向き／垂直下向き）
  - 低い角度で描画します（チェックが入っている場合、上でスキップされた目盛に注記が付きます）

![image32](images/entries/0da542215cefcd2e3ca120dd0381b47611734dce.gif)

This feature was funded by [Kanton Solothurn](https://geo.so.ch/)

This feature was developed by [Olivier Dalang, OPENGIS.ch](https://www.opengis.ch)
### Y位置のぺージオフセット式を追加します
A `layout_pageoffsets` expression was added for print layouts which returns an array of Y coordinates for the top of each page in the layout. this allows users to dynamically position items on pages in a context where page sizes may change.

For example, to set an item at 2.5mm from the top of page 2 (for the data-defined position Y of a map item) : `@layout_pageoffsets[1] + 2.5`

This constitutes a workaround for [Issue 37567](https://github.com/qgis/QGIS/issues/37567).

This feature was funded by [BikePlan](https://www.bikeplan.swiss/)

This feature was developed by [Olivier Dalang, OPENGIS.ch](https://www.opengis.ch)
## 計算式
### Add to_decimal() function to convert DMS to DD
A new `QgsCoordinateUtils::dmsToDecimal` function has been added which exposes the `to_decimal` function in expressions. This allows the conversion of DMS (degree/minute/second) strings into DD (decimal degree) format.

This feature was developed by [Mathieu Pellerin](https://api.github.com/users/nirvn)
### Add \"main_angle\" function to return the estimated main angle of a geometry
ジオメトリ値をカバーする最小バウンディングボックスの角度を返します。

Useful for data defined overrides in the symbology of label expressions, e.g. to rotate labels to match the overall angle of a polygon, and similar for line pattern fill. ![image33](images/entries/87367553-aae7d680-c5be-11ea-923a-e81200f2b90c.gif)

![image34](images/entries/03463ac0a8303444d94806fb2ff66d6a73c56ccb.webp)

This feature was funded by [Kanton Solothurn](https://geo.so.ch/)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### refFunctionsをコアへ移植します
様々なオーバーレイ操作が式エンジンに追加されました。これには、refFunctionsプラグインの機能が含まれています。

![image35](images/entries/90797864-7bd92900-e311-11ea-945f-0c2ade14e801.gif)

The following new expression functions are implemented:

    * overlay_intersects(layer[,expression][,filter][,limit][,cache])
    * overlay_contains(layer[,expression][,filter][,limit][,cache])
    * overlay_crosses(layer[,expression][,filter][,limit][,cache])
    * overlay_equals(layer[,expression][,filter][,limit][,cache])
    * overlay_touches(layer[,expression][,filter][,limit][,cache])
    * overlay_disjoint(layer[,expression][,filter][,limit][,cache])
    * overlay_within(layer[,expression][,filter][,limit][,cache])
    * overlay_nearest(layer[,expression][,filter][,limit][,max_distance][,cache])
    
全てのインスタンスで、空間演算子は他のレイヤに対して評価されます。式が指定されている場合、結果の配列が返されます。式が指定されていない場合、少なくとも1つの地物に一致するものがあるかどうかを示すブール値が返されます。地物はオプションで式によってフィルタリングされ、オプションで特定の数に制限されることがあります。

The `overlay_nearest` function has an additional max_distance filter.

![image36](images/entries/d4bb059729eecfc689e001f731d59fff25225615.webp)

This feature was developed by [Olivier Dalang, OPENGIS.ch](https://www.opengis.ch)
## デジタイズ
### 移動方向に基づいて方位を計算するオプションを追加します
誤った方位測定値を報告するデバイスについて、このオプションを使うと、代わりに前の2つの記録された位置に基づいたGPS方位を計算することができます。

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### 曲線の地物のデジタイズと分割
ベクタレイヤ地物をデジタイズまたは分割する際に、直線または円形ストリングを切り替えることができる新機能が導入されました。

ユーザーはキーボードショートカット **Ctrl+Shift+G** を使用して、線形/円形を切り替えることができます。

For splitting features, new overloading methods have been added to the API. When splitting, curves are preserved. For this, the curve is segmentized before splitting, and all the split features are \"de-segmentized\" after splitting.

A toolbar button was added to enable switching between linear/circular: ![image37](images/entries/88101713-6505b200-cb6c-11ea-9feb-68a4130d6f52.gif)

![image38](images/entries/86938423-6a93de80-c10e-11ea-8511-489d8b4f006f.gif)

![image39](images/entries/86938444-7089bf80-c10e-11ea-8fd0-0f419f71b52e.gif)

![image40](images/entries/8145ccfa4e659f7d8315830cecfe2b2f391b9aa4.webp)

This feature was developed by [Vincent Cloarec](https://api.github.com/users/vcloarec)
## データ管理
### プロセシングのためのラスタの再スケールアルゴリズム
Adds a rescale raster algorithm to change raster value range, whilst preserving the shape of the raster\'s histogram. Useful for when rasters from different sources should be compared or processed together and their pixel values should be in the same range. By default, the algorithm preserves the NODATA value of the input raster but there is an option to override it.

The following image displays a histogram of a DEM (value range is 85-243) ![image41](images/entries/86897604-53ee8700-c110-11ea-99ae-540d38f88154.webp) And the next image displays a histogram of same DEM rescaled to the range 100-1000 ![image42](images/entries/86897671-67015700-c110-11ea-8183-e0d6bd013dbb.webp)

Addresses [Issue 26099](https://github.com/qgis/QGIS/issues/26099).

This feature was developed by [Alexander Bruy](https://api.github.com/users/alexbruy)
## フォームとウィジェット
### ひとつの関連に複数のウィジェット
ひとつの関連に複数の関連ウィジェットが作成できるようになり、それぞれが独自の設定を持っています。

This feature changes the behavior of relation widgets created in the drag and drop interface and provides resolution for [Issue 37675](https://github.com/qgis/QGIS/issues/37675).

古いQGISバージョンで構成されたプロジェクトを読み込むと、設定が引き継がれて新しいウィジェットの構成に書き込まれます。自動生成されたフォームでは、リレーションエディタウィジェットの構成はもはや許可されませんが、古いQGISで構成されている場合、属性フォームはこの設定を引き続き読み込みます。

![image44](images/entries/d3a51f9b7ea6ffa3c8c8c457e3d6278d57bcf125.gif)

This feature was developed by [signedav](https://api.github.com/users/signedav)
### 地物情報結果ツリーに関連した地物を表示
識別ツールを使用する際に、結果ウィンドウで関連する（子）地物を表示することができるようになります。識別された各親地物の下には、新しいグループが関連する子地物の属性、アクションを表示し、その子地物の地物フォームを直接開くことができます。

This feature addresses issue [18634](https://github.com/qgis/QGIS/issues/18634).

![image45](images/entries/863b80851b995421b6f2ea455faf6b1c41211cd5.gif)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### リレーション参照ウィジェットのフィルタ式
静的フィルタ式をリレーション参照ウィジェットで使うためのオプションが追加されました。

![image46](images/entries/8048bb8df64e31bb733eea239c527f8be631ce6f.gif)

This feature was developed by [Ivan Ivanov](https://api.github.com/users/suricactus)
## 分析ツール
### デバッグツールのドックにプロジェクトの読み込みプロファイル時間を追加
Modification of the QgsRuntimeProfiler class which performs the following functions: 1. Make the profiling thread-safe, so that it\'s possible to record times across multiple threads 2. Allows different profiling \"groups\"

The new groups API is used here to expose a breakdown of project load times in the debugging dock, alongside the existing QGIS startup profiling. It\'s possible now to get a breakdown of the various stages of project load, in order to identify the causes of slow project load times.

TODO: In the majority of cases, performance problems will be caused by one or more layers, so it would be nice to further break down the individual layer load times. For example, for an individual WFS layer, we may see the time taken for the initial \"server capabilities\" or other queries. Add a group with profile times for map rendering, so you can see exactly which layers in your project are causing slow map redraw times.

現在の形式では、各個別のレイヤの全体的な読み込み時間のみが表示されます。

![image47](images/entries/85852208-7bca1a80-b7f3-11ea-8882-b3253622b1b6.webp)

![image48](images/entries/943a79db68aee3458cb88cacd7a69b66fda3caea.webp)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
## プロセシング
### パラメータのヘルプ文字列を追加します
パラメータレベルでヘルプ文字列を指定できるようになりました。

これはツールチップ、CLI、およびPythonプロセシングAPIで表示されます。

![image55](images/entries/2196bcb0123ced5e180ffb2b9469a65a38dcc41b.webp)

This feature was developed by [Étienne Trimaille](https://api.github.com/users/Gustry)
### New \"Align points to features\" algorithm
このアルゴリズムは、ポイント地物を別の参照レイヤの最も近い地物に合わせるために必要な回転を計算します。出力レイヤには、最も近い参照地物への角度（度数、時計回り）が入力された新しいフィールドが追加されます。

Optionally, the output layer\'s symbology can be set to automatically use the calculated rotation field to rotate marker symbols.

必要な場合、孤立したポイントを遠くの地物に合わせないようにするために、ポイントを整列する際に使用する最大距離を設定することができます。

この場合の使用例は、このアルゴリズムによって生成されたデータ定義の回転値を使用して、建物のポイントシンボルを最も近い道路の方向に合わせることです。

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### ディレクトリを作成するモデラーアルゴリズムを追加
このアルゴリズムにより、モデルで新しいファイルディレクトリを作ることができます。結果を特定の動的に作成されたパス（例　現在の日付を格納するフォルダ）に出力する必要があるモデルに便利です。

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### プロジェクトの式変数にセットするモデラーアルゴリズムを追加
Allows a model to set Project-level expression variables during execution. Especially useful with the new [Export Print Layout algorithms](https://github.com/qgis/QGIS/pull/36916) to allow models which dynamically set variables used in a layout prior to export.

This functionality was ported from <https://gis.stackexchange.com/questions/359386>

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### 印刷レイアウトをPDF/imageとしてエクスポートするプロセシングアルゴリズムを追加
モデルはプロジェクトから印刷レイアウトをエクスポートすることができます。これの使用例の1つは、特定のレイアウトのセットをプロジェクトから特定のフォルダーにエクスポートするときに、複数のレイアウトを手動で開いて1つずつエクスポートする代わりに、ひとつの操作で簡単に再エクスポートするプロジェクト内モデルが作れるようにすることです。

さらに、モデル内に式型の出力ファイルを持つ新しい機能を使えば、現在日付のタグを持つフォルダにレイアウトを自動的にエクスポートし、エクスポートされたファイル名にこれを含めることができます！

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### ファイルのアルゴリズムに保存機能を追加
モデル内のファイルデータセットにベクタ地物を保存するためのネイティブなプロセシングアルゴリズムができました。GDALにデータセットとレイヤのオプションを渡すための一対の高度な機能が付属しています。

![image56](images/entries/b238631365830b019300700cf59c3a8dd3d05a4f.webp)

This feature was developed by [Mathieu Pellerin](https://api.github.com/users/nirvn)
### 地図帳のレイアウトをPDFアルゴリズムとしてエクスポート
新しいQGISのプロセシングアルゴリズムが追加され、地図帳をPDFにエクスポートすることができるようになりました。これは最近の地図帳レイアウトを画像にエクスポートするアルゴリズムのPDF版です。

This feature was developed by [Mathieu Pellerin](https://api.github.com/users/nirvn)
### New \"Flatten Relationship\" algorithm
このアルゴリズムは、ベクタレイヤの全てのリレーションをフラット化し、関連する地物ごとに1つのマスター地物を含む単一のレイヤをエクスポートします。このマスター地物には、関連する地物の全ての属性が含まれています。

It\'s designed as a quick way to de-normalize a relation from a project, e.g. to allow exporting to CSV.

この機能は、SMEC/SJによって資金提供されました

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### 地図帳レイアウトを画像としてエクスポートするアルゴリズム
新しいネイティブのプロセシングアルゴリズムが追加され、地図帳レイアウトを画像としてエクスポートできるようになりました。

これは、地図帳の範囲レイヤとして使用するためにリモートのデータセットが処理されるモデルで役立ちます。

![image57](images/entries/e4f315e60743577c9f45ad44643fd5ba9778c040.webp)

This feature was developed by [Mathieu Pellerin](https://api.github.com/users/nirvn)
### 新しいセル統計アルゴリズム
**セル統計量** というラスタ解析アルゴリズムを追加しました。これは、NoDataを考慮しながらラスタレイヤのスタックに対してセルごとの統計を行います。現在の実装で利用可能な関数は以下の通りです:

|
- 合計
- 平均値
- 中央値
- 標準偏差
- 分散（Variance）
- 最大
- 最小値
- 最頻値
- 最稀値（最小頻値）
- 範囲（最大 - 最小）
- 種類（ユニークな値の個数）

![image49](images/entries/fca13f48b118ed13ebe84191a226ca0e20c37bfa.webp)

This feature was developed by [Clemens Raffler](https://api.github.com/users/root676)
### 新しい、値の一致頻度アルゴリズム
ラスタスタック内でセルごとに動作するいくつかの新しいラスタアルゴリズムを追加しました。ラスタスタックの値の一致頻度アルゴリズムは、入力ラスタスタックの値が、値ラスタの値と等しい頻度（回数）をセルごとに評価します。

![image50](images/entries/e368e10cfa5e19992176930121e0cb846c3d1ca8.webp)

This feature was developed by [Clemens Raffler](https://api.github.com/users/root676)
### 新しい、ラスタスタックの値の超過頻度アルゴリズム
ラスタスタック内でセルごとに動作するいくつかの新しいラスタアルゴリズムを追加しました。ラスタスタックの値の超過頻度アルゴリズムは、入力ラスタスタックの値が、値ラスタの値よりも大きい頻度（回数）をセルごとに評価します。

![image51](images/entries/97228db861367c2875dab0533ab616bb2ac2432c.webp)

This feature was developed by [Clemens Raffler](https://github.com/root676)
### 新しい、ラスタスタックの値の過小頻度アルゴリズム
ラスタスタック内でセルごとに動作するいくつかの新しいラスタアルゴリズムを追加しました。ラスタスタックの値の過小頻度アルゴリズムは、入力ラスタスタックの値が、値ラスタの値よりも小さい頻度（回数）をセルごとに評価します。

![image52](images/entries/114853cd3d7c245b56edea0024704c853997275c.webp)

This feature was developed by [Clemens Raffler](https://github.com/root676)
### 新しい、ラスタスタックの最小値の位置アルゴリズム
この新しいQGISバージョンには、いくつかのラスタ値位置分析ツールを追加しました：*ラスタスタックの最小値の位置* アルゴリズムは、ラスタスタック内の最低値の位置をセルごとに評価します。位置の数は1から入力ラスタの総数までの範囲です。アルゴリズムでは、入力ラスタの順序が重要です。

![image53](images/entries/f3383f5583c9096b1b8d1873679e1a495fac0485.webp)

This feature was developed by [Clemens Raffler](https://github.com/root676)
### 新しい、ラスタスタックの最大値の位置アルゴリズム
この新しいQGISバージョンには、いくつかのラスタ値位置分析ツールを追加しました：*ラスタスタックの最大値の位置* アルゴリズムは、ラスタスタック内の最高値の位置をセルごとに評価します。位置の数は1から入力ラスタの総数までの範囲です。アルゴリズムでは、入力ラスタの順序が重要です。

![image54](images/entries/a730b8c1566c99bdebff09c783ae320b0c138d76.webp)

This feature was developed by [Clemens Raffler](https://github.com/root676)
### プロセシングの結果をレイヤーグループに読み込む
Users can now optionally set a group name which ensures that the resulting output layers added to the project when using the *Open output file after running algorithm* option are grouped together. This allows all outputs from several processing algorithms to be grouped so that they may be easily located in the layer tree and be removed, exported, or have their visibility toggled easily. ![image58](images/entries/414c68839518d5b658d6e6f1565f6c27e1f4336f.gif)

This feature was developed by [Germán Carrillo](https://github.com/gacarrillor)
### 新しい出力を作成する、ゾーン統計量アルゴリズムを追加
Previously, when calculating zonal statistics, the algorithm always updated the original data source, adding additional fields. A new zonal statistics algorithm has been added which creates a new output instead. This functionality is an implementation of the [29504 feature request](https://github.com/qgis/QGIS/issues/29504).

This feature was developed by [Matthias Kuhn](https://api.github.com/users/m-kuhn)
### ジオメトリのプロセシングパラメータを追加
Added a new `QgisProcessingParameterGeometry` for passing geometries as a parameter to processing alogrithms.

これは、入力レイヤを必要とせずにアルゴリズムに簡単なジオメトリを渡す方法を提供します。

即時の使用例は次のとおり:
- 原子的な方法でジオメトリを操作する必要があるかもしれないアルゴリズム
- 親アルゴリズムからの継承。
- スタンドアロンのプロセシングツールでヘッドレスのQGISプロセシングを使用。

機能:
- パラメータは、値としてWell-Known-Textを渡すことができるため、文字列パラメータと互換性があります。
- 現在のウィジェットのインタラクションは、WKTの値を入力するための入力テキストウィジェットだけを使用しているので最小限です。

This feature was developed by [David Marteau](https://api.github.com/users/dmarteau)
### アプリケーションが安全に終了できるかどうかを判断するインタフェースを追加
プラグインやスクリプトがカスタムロジックを登録して、QGISアプリケーションが終了しないようにするためのインタフェースが追加されました。これにより、プラグインはアプリケーションが安全に終了できるかどうかを判断することができます。これにより、プラグインはQGISが終了する前に保存または破棄する必要のある未保存の変更があるかどうかを判断することができるようになりました。これは、コンソールスクリプトエディタで既に実装されている機能であり、未保存の変更がある場合に静かにアプリケーションをシャットダウンするのではなく、ユーザーにプロンプトを表示してデータの損失を防ぎます。

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
## アプリケーションとプロジェクトのオプション
### 利用可能なGDALベクタドライバを列記
A *Vector Drivers* tab is now available within the QGIS GDAL Settings window, which lists all the available GDAL vector drivers and allows users to toggle their active state. Where several drivers may be used to open data of a specific type, users may now modify these settings to ensure that the intended driver is used when importing specific vector data types. For example, the FileGDB and OpenFileGDB drivers are both capable of being used to import .gdb files, but if the data file has a version of 9.x, the FileGDB won\'t be able to open it. In this instance, a user may disable the FileGDB driver and ensure that the data is loaded using the OpenFileGDB driver instead.

This functionality directly addresses the limitations outlined in [Issue 18738](https://github.com/qgis/QGIS/issues/18738).

![image59](images/entries/5cc48d8ea8bc276446f8eae4a1c838e0d1f91a40.webp)

This feature was developed by [Alexander Bruy](https://api.github.com/users/alexbruy)
### MacOSでGRASSインストールフォルダを検出
MacOS previously had a platform-specific custom parameter setting Grass7Utils.GRASS_FOLDER. This caused crashes for many users with multiple QGIS installations or who had some invalid folder settings. The parameter has been removed and a GISBASE environment variable has been introduced instead, which is commonly used in GRASS scripts as the \"root\" installation directory, emulating the behavior used for GRASS detection in Windows environments. If GISBASE is not present (default), a search is performed for grass folders in `QgsApplication.prefixPath()` (when packaged in bundle format). If not found, the standalone GRASS instance is searched for. The new behaviour for GRASS is in-line with the methodology used for the GDAL and SAGA processing tools.

This resolves [Issue 38595](https://github.com/qgis/QGIS/issues/38595).

![image60](images/entries/e59bb83513293830df8ec4dcf825247b14dacc98.webp)

This feature was developed by [Lutra Consulting (Peter Petrik)](https://api.github.com/users/PeterPetrik)
## ブラウザ
### 属性をブラウザで見えるようにする
First part of QEP <https://github.com/qgis/QGIS-Enhancement-Proposals/issues/171>

接続APIを実装するプロバイダについてブラウザで属性列を見えるようにします:
- PG
- GPKG
- Spatialite
- MSSQL

フィールドに対して次の操作がサポートされています:
- 新しいフィールドを追加
- フィールドを削除

![image61](images/entries/87223743-a4b7e700-c37f-11ea-88a3-4b371bfadf89.gif)

![image62](images/entries/d4e761ad977a712aa1fc1fbc65d61c886e6e79fb.webp)

This feature was developed by [Alessandro Pasotti](https://api.github.com/users/elpaso)
## データプロバイダ
### ArcGIS Vector TIle Service接続
ArcGIS Vector Tile Serviceへの接続を作成するオプションが追加され、ArcGISサーバーのベクタタイルサービスから簡単にベクタタイルレイヤを読み込めるようになりました。また、ベクタタイル接続に対する認証、設定、およびカスタムリファラ文字列のサポートも追加されました。

この変更は、ESRIベクタタイルサービスへの接続の追加と設定のための明示的なUIオプションを追加します。これらのサービスはデータの取得に標準のベクタタイルフレームワークを使っていますが、ArcGISサーバ上のVectorTileService APIエンドポイントを使って直接追加することもできます。

After a user adds a layer from a VectorTileService, the server\'s default styling and labeling for the layer is automatically loaded.

![image63](images/entries/e31c882fa9552ed6bd247f0092305ae8c153948a.gif)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Trust layer metadata propagation
プロジェクトレベルの信頼フラグは、ベクタレイヤの範囲をプロバイダではなく、xmlから読み取るためにのみ使われます。

This flag was not available at the vector layer and data provider level. A new QgsMapLayer reading flag to propagate the trust layer metadata for the project\'s read flag and a new provider flag to trust the datasource config.

データソースの設定を信頼することで、プロバイダは推定されたメタデータを使用でき、主キーが一意であり、検出可能なジオメトリタイプとSRIDが要求されたものと同じであることが保証されます。

This feature was developed by [rldhont](https://api.github.com/users/rldhont)
### Add support for virtual columns in Oracle
Support for virtual (generated) Oracle columns has been added and is defined this way:

`sql CREATE TABLE QGIS.GENERATED_COLUMNS ( "pk" INTEGER PRIMARY KEY, "generated_field" GENERATED ALWAYS AS ('test:' || "pk") VIRTUAL);`

**Note:** It\'s not possible to define a generated column on an SDO_GEOMETRY field in Oracle.

For now, when creating a new feature, the generated field is editable and should not be. A new API method needs to be added to retrieve readonly field from the provider as discussed in [Issue 35995](https://github.com/qgis/QGIS/pull/35995#issuecomment-633055700).

This feature was developed by [Julien Cabieces](https://api.github.com/users/troopa81)
### データのインポートに高度なオプションを追加
New functionality has been introduced which allows advanced parameters to be specified when importing layers using the OGR data provider, opening a vast range of new possibilities, especially when working around expected dataset issues.

![image64](images/entries/e1c7474d19828b39f5872b289a1e8ba994556a10-1.webp)

![image65](images/entries/4a2d99c6ef6ec12e5f63a29ad00d9ebc3cd534e2.webp)

This feature was developed by [Even Rouault](https://api.github.com/users/rouault)
## QGISサーバー
### QGIS Server WFS3 API Sorting
Adds sorting functionality to the QGIS Server WFS3 API

This feature was developed by [Alessandro Pasotti](https://api.github.com/users/elpaso)
### QGIS Server landing page plugin
A Landing Page Plugin for QGIS Server was created, which is a C++ port of <https://github.com/elpaso/qgis-server-landing-page-plugin>

![image66](images/entries/a2254bbef892835317a9f608afd8bd3722ee4b38.gif)

This feature was developed by [Alessandro Pasotti](https://api.github.com/users/elpaso)
### Environment variable to disable GetPrint and to not load layouts
A new `QGIS_SERVER_DISABLE_GETPRINT` environment variable was added to QGIS Server which prevents the loading of layouts when projects are read and disables the WMS GetPrint request, improving the read time of projects.

This feature was funded by [Ifremer](https://wwz.ifremer.fr)

This feature was developed by [3Liz](https://www.3liz.com)
### Environment variable to trust layer metadata with server settings
Trust layer metadata can be defined at the project level. A new project reading flag was added which allows the forcing of trust layer metadata.

For QGIS server, the trust layer metadata option can be overridden with `QGIS_SERVER_TRUST_LAYER_METADATA` environment variable.

This feature was funded by [Ifremer](https://wwz.ifremer.fr)

This feature was developed by [3Liz](https://www.3liz.com)
## 注目すべき修正
### Even Rouaultによるバグ修正
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Scrolling attribute table of a layer added with the \"delimted text provider\" is almost impossible | [#38068](https://github.com/qgis/QGIS/issues/38068) | [PR #38735](https://github.com/qgis/QGIS/pull/38735) | [PR #38745](https://github.com/qgis/QGIS/pull/38745) |
| support for API-keys via query for API implementing OGC API - Features | [#38436](https://github.com/qgis/QGIS/issues/38436) | [PR #38738](https://github.com/qgis/QGIS/pull/38738) | N/A |
| Custom CRS does not always switch parameters correctly from wkt to proj string | [#38689](https://github.com/qgis/QGIS/issues/38689) | 再現できません |  |
| OGC API Features client always use limit=1000 | [#38666](https://github.com/qgis/QGIS/issues/38666) | 再現できません |  |
| Exporting to geopackage changes field type from DATE to DATETIME | [#37857](https://github.com/qgis/QGIS/issues/37857) | バグではない |  |
| CSV date field being interpreted as time type | [#38091](https://github.com/qgis/QGIS/issues/38091) | [PR #38741](https://github.com/qgis/QGIS/pull/38741) | N/A |
| Coordinate Transformation Difference between QGIS and Proj | [#38190](https://github.com/qgis/QGIS/issues/38190) | usage issue |  |
| gdal_rasterize not working when file has \'&\' symbol in name | [#38674](https://github.com/qgis/QGIS/issues/38674) | [PR #38743](https://github.com/qgis/QGIS/pull/38743) | [PR #38747](https://github.com/qgis/QGIS/pull/38747) |
| Core dump when using identify feature on a vector polygon | [#36213](https://github.com/qgis/QGIS/issues/36213) | already fixed |  |
| Error of the raster histogram of QGIS 3.10.8(LTR) | [#38298](https://github.com/qgis/QGIS/issues/38298) | [PR #38769](https://github.com/qgis/QGIS/pull/38769) | TODO |
| \[Postgres\] Cannot edit attribute when there is no primary key | [#37917](https://github.com/qgis/QGIS/issues/37917) | not a bug IMHO |  |
| Switching between WMS info-output formats throws: CRITICAL QTableWidget: cannot insert an item that is already owned by another QTableWidget | [#37215](https://github.com/qgis/QGIS/issues/37215) | [PR #38770](https://github.com/qgis/QGIS/pull/38770) | [PR #38783](https://github.com/qgis/QGIS/pull/38783) |
| SaveAs Geopackage: TEXT fields are converted to TEXT(255) | [#25405](https://github.com/qgis/QGIS/issues/25405) | already fixed |  |
| \"Join attributes by nearest\" tool defaults to \"None\" when using Max distance of 0 | [#38761](https://github.com/qgis/QGIS/issues/38761) | [PR #38773](https://github.com/qgis/QGIS/pull/38773) | No, not appropriate (see [PR #38778](https://github.com/qgis/QGIS/pull/38778)) |
| Lost edits in layer of same transaction group | [#38697](https://github.com/qgis/QGIS/issues/38697) | [PR #38779](https://github.com/qgis/QGIS/pull/38779) + [PR #38780](https://github.com/qgis/QGIS/pull/38780) | [PR #38824](https://github.com/qgis/QGIS/pull/38824) |
| Preview of Expression String Builder \'freezes\' if Feature id higher then available | [#38646](https://github.com/qgis/QGIS/issues/38646) | [PR #38797](https://github.com/qgis/QGIS/pull/38797) | N/A |
| VectorFileWriter/OGR provider: workaround GDAL 3.1.x bug regarding XLSX and ODS creation | not reported | [PR #38837](https://github.com/qgis/QGIS/pull/38837) | [PR #38853](https://github.com/qgis/QGIS/pull/38853) |
| Coordinate operation widget: avoid repeating scope and remarks | not reported | [PR #38847](https://github.com/qgis/QGIS/pull/38847) | N/A |
| WFSレイヤの属性テーブルを表示するとフリーズ | [#37224](https://github.com/qgis/QGIS/issues/37224) | [PR #38952](https://github.com/qgis/QGIS/pull/38952) | [PR #38956](https://github.com/qgis/QGIS/pull/38956) |
| OGR Error when editing a kml file | [#39087](https://github.com/qgis/QGIS/issues/39087) | [GDAL Commit 72e1a4d7c96e0381d2d335857697b5f8e1668450](https://github.com/OSGeo/gdal/commit/72e1a4d7c96e0381d2d335857697b5f8e1668450) | Backported to GDAL 3.1 branch too |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Even Rouault](http://www.spatialys.com/)
### Alessandro Pasotti によるバグ修正
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Loading PostGIS layers with no specified geometry loads all features in the attribute table. | [PR #35367](https://github.com/qgis/QGIS/pull/35367) [#38565](https://github.com/qgis/QGIS/issues/38565) | Backport only | [PR #38736](https://github.com/qgis/QGIS/pull/38736) |
| Server API: current project is not settable anymore | [#38755](https://github.com/qgis/QGIS/issues/38755) | [PR #38758](https://github.com/qgis/QGIS/pull/38758) | [PR #38758](https://github.com/qgis/QGIS/pull/38758) |
| PostGIS layer saved in 3.10 project, fail to load correctly on 3.14 | [#38567](https://github.com/qgis/QGIS/issues/38567) | [PR #38763](https://github.com/qgis/QGIS/pull/38763) | N/A |
| Server WFS-T 1.1.0 wrong case for totalUpdated, totalInserted, totalDeleted | [#38558](https://github.com/qgis/QGIS/issues/38558) | [PR #38764](https://github.com/qgis/QGIS/pull/38764) | TODO |
| Server crashes on GetLegendGraphics when RULE does not exists. | [#38766](https://github.com/qgis/QGIS/issues/38766) | [PR #38775](https://github.com/qgis/QGIS/pull/38775) | [PR #38794](https://github.com/qgis/QGIS/pull/38794) |
| Form view gets stuck in the last shown not-NULL-value for some attributes when browsing through data | [#38552](https://github.com/qgis/QGIS/issues/38552) | [PR #38801](https://github.com/qgis/QGIS/pull/38801) | TODO |
| Marker line Simple marker rotation override not respecting follow line direction setting | [#38716](https://github.com/qgis/QGIS/issues/38716) | [PR #38815](https://github.com/qgis/QGIS/pull/38815) |  |
| Unable to dock the \"snapping options\" widget | [#38604](https://github.com/qgis/QGIS/issues/38604) | works for me |  |
| Can\'t read PG data sources when saved in version 3.10 and using service / auth combo | [#38809](https://github.com/qgis/QGIS/issues/38809) | [PR #38833](https://github.com/qgis/QGIS/pull/38833) | N/A |
| DB Manager \"cancel\" button to stop a query is not working | [#38092](https://github.com/qgis/QGIS/issues/38092) | [PR #38870](https://github.com/qgis/QGIS/pull/38870) | N/A |
| GDAL enhancement related to [#38092](https://github.com/qgis/QGIS/issues/38092) | [#38092](https://github.com/qgis/QGIS/issues/38092)2 | <https://github.com/OSGeo/gdal/pull/2953#event-3788638320> | N/A |
| Shift values issue while creating new field under DB Manager | [#38800](https://github.com/qgis/QGIS/issues/38800) | works for me |  |
| Problem with VUV wms | [#38924](https://github.com/qgis/QGIS/issues/38924) | works for me |  |
| Data Source Manager: WMS/WMTS Window not resizable | [#38903](https://github.com/qgis/QGIS/issues/38903) | works for me, pending feedback |  |
| Form tab option \"Show as group box\" won\'t save or apply | [#38539](https://github.com/qgis/QGIS/issues/38539) | works for me |  |
| Scale lock is ignored when panning the map | [#38953](https://github.com/qgis/QGIS/issues/38953) | [PR #38954](https://github.com/qgis/QGIS/pull/38954) | N/A |
| Zoom to layer overwrites locked scale bug | [#38417](https://github.com/qgis/QGIS/issues/38417) | [PR #38954](https://github.com/qgis/QGIS/pull/38954) | N/A |
| Repeated column names cause visualization issues in DB Manager | [#38976](https://github.com/qgis/QGIS/issues/38976) | [PR #38981](https://github.com/qgis/QGIS/pull/38981) | N/A |
| \"show search_path\" returns 0 rows | [#38975](https://github.com/qgis/QGIS/issues/38975) | [PR #38981](https://github.com/qgis/QGIS/pull/38981) | N/A |
| PG NOTIFY not accessible | [#38986](https://github.com/qgis/QGIS/issues/38986) | works for me |  |
| Fix PG db-manager rename schema | [#38998](https://github.com/qgis/QGIS/issues/38998) | [PR #39000](https://github.com/qgis/QGIS/pull/39000) | N/A |
| Several PG browser items UX issues | [#39001](https://github.com/qgis/QGIS/issues/39001) | [PR #39006](https://github.com/qgis/QGIS/pull/39006) | N/A |
| Virtual vector does not load correctly on Windows | [#35016](https://github.com/qgis/QGIS/issues/35016) | works for me on windows/current master |  |
| DB Manager: PostgreSQL field comments are not displayed correctly | [#38394](https://github.com/qgis/QGIS/issues/38394) | [PR #39026](https://github.com/qgis/QGIS/pull/39026) |  |
| Only first row for Postgis raster table in DB Manager preview and when adding layer to Map canvas | [#39017](https://github.com/qgis/QGIS/issues/39017) | [PR #39039](https://github.com/qgis/QGIS/pull/39039) | N/A |
| erroneous postgis query when trying to discover relations | [#39036](https://github.com/qgis/QGIS/issues/39036) |  |  |
| many additional tables that are already loaded in the project are loaded on project load because of layer dependencies | [#39025](https://github.com/qgis/QGIS/issues/39025) | [PR #39043](https://github.com/qgis/QGIS/pull/39043) | N/A |
| Partial fix for : Wrong assignments of raster values to symbology Paletted/Unique values or Singleband Pseudocolor | [#39058](https://github.com/qgis/QGIS/issues/39058) | [PR #39071](https://github.com/qgis/QGIS/pull/39071) | N/A |
| Allow to set precision for raster single band presudocolor classification | not reported | [PR #39079](https://github.com/qgis/QGIS/pull/39079) |  |
| Complete fix for : Wrong assignments of raster values to symbology Paletted/Unique values or Singleband Pseudocolor | [#39058](https://github.com/qgis/QGIS/issues/39058) | [PR #39088](https://github.com/qgis/QGIS/pull/39088) | Risky |
| Failure with identifier sequence when adding feature | [#39093](https://github.com/qgis/QGIS/issues/39093) | works for me |  |
| Export report to PDF crashes QGIS if no layout is in edit mode | [#39086](https://github.com/qgis/QGIS/issues/39086) | [PR #39135](https://github.com/qgis/QGIS/pull/39135) | TODO |
| PG raster: float rasters do not show nodata values correctly in master/3.14 | [#39142](https://github.com/qgis/QGIS/issues/39142) | [#39142](https://github.com/qgis/QGIS/issues/39142) |  |
| Python API call QgsAbstractDatabaseProviderConnection::TableProperty exceptions not converted to QgsProviderConnectionException | [#39151](https://github.com/qgis/QGIS/issues/39151) | [PR #39152](https://github.com/qgis/QGIS/pull/39152) | N/A |
| DB Manager unable to show PostGIS geography column | [#37666](https://github.com/qgis/QGIS/issues/37666) | [PR #39154](https://github.com/qgis/QGIS/pull/39154) | N/A |
| setting a field to NULL via field calculator freezes qgis | [#39178](https://github.com/qgis/QGIS/issues/39178) | [PR #39257](https://github.com/qgis/QGIS/pull/39257) | TODO |
| Layer X: Feature has too many attributes (expecting 5, received 7) when \"Automatic Creation of Transaction Group\" is enabled | [#39230](https://github.com/qgis/QGIS/issues/39230) | [PR #39267](https://github.com/qgis/QGIS/pull/39267) | [PR #39278](https://github.com/qgis/QGIS/pull/39278) |
| unreported crash when calling data provider\'s lastError on no errors | not reported | [PR #39267](https://github.com/qgis/QGIS/pull/39267) | N/A |
| Crash digitizing a feature when transaction group is on (after save) | [#39265](https://github.com/qgis/QGIS/issues/39265) | [PR #39283](https://github.com/qgis/QGIS/pull/39283) |  |
| Transaction groups: not-current layers a set to not editable after save | [#39282](https://github.com/qgis/QGIS/issues/39282) | [PR #39286](https://github.com/qgis/QGIS/pull/39286) | not critical |
| OGR decodeUri: be tolerant on layerName case | not reported but impact the QGIS-Documentation | [PR #39328](https://github.com/qgis/QGIS/pull/39328) | N/A |
| Wrong extension handling in links when layer name has dots | not reported | [PR #39346](https://github.com/qgis/QGIS/pull/39346) | N/A |
| Passwords are URL-encoded before base64 encoding for HTTP Basic auth | [#39243](https://github.com/qgis/QGIS/issues/39243) | [PR #39347](https://github.com/qgis/QGIS/pull/39347) | [PR #39382](https://github.com/qgis/QGIS/pull/39382) |
| QGIS crash in Settings menu if NOT in english | [#39430](https://github.com/qgis/QGIS/issues/39430) | [PR #39434](https://github.com/qgis/QGIS/pull/39434) | N/A |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Alessandro Pasotti](https://www.itopen.it/)
### Peter Petrik によるバグ修正
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Problem with displaying mesh and canvas rotation | [#35147](https://github.com/qgis/QGIS/issues/35147) | [PR #38795](https://github.com/qgis/QGIS/pull/38795)/files | no, not critial |
| Crash while attempting to use mesh | [#31773](https://github.com/qgis/QGIS/issues/31773) | 再現できません |  |
| Spatial Bookmark Manager Bad Behavior and Crashing App | [#35348](https://github.com/qgis/QGIS/issues/35348) | 再現できません |  |
| Seqmentation fault 11 on QGIS shutdown on MacOS | not reported | [PR #38806](https://github.com/qgis/QGIS/pull/38806) | [PR #38748](https://github.com/qgis/QGIS/pull/38748) |
| Crash when creating New MSSQL connexion on macOS | [#35026](https://github.com/qgis/QGIS/issues/35026) | [PR #39084](https://github.com/qgis/QGIS/pull/39084) | different packaging system\... |
| qgis_process is installed in the wrong place on MacOS | [#38447](https://github.com/qgis/QGIS/issues/38447) | [Mac Packager Commit 97b0ec974e2309e447ebb69c4117580db27af6f0](https://github.com/qgis/QGIS-Mac-Packager/commit/97b0ec974e2309e447ebb69c4117580db27af6f0) | N/A |
| Unable to run GRASS plugin on MacOS | [#32511](https://github.com/qgis/QGIS/issues/32511) | [Mac Packager Commit 218a571f6f268dcc4490ebe1a00068bfe363b2ae](https://github.com/qgis/QGIS-Mac-Packager/commit/218a571f6f268dcc4490ebe1a00068bfe363b2ae) | different packaging system\... |
| Processing: GRASS r.drain fails on macOS: \"No module named site\", \"Raster not found\" | [#36126](https://github.com/qgis/QGIS/issues/36126) | [Mac Packager Commit 218a571f6f268dcc4490ebe1a00068bfe363b2ae](https://github.com/qgis/QGIS-Mac-Packager/commit/218a571f6f268dcc4490ebe1a00068bfe363b2ae) | different packaging system\... |
| The Grass7 processing toolbox option dialogue should include a way to specify a path to the GRASS binary, overriding Grass7Utils.command | [#29454](https://github.com/qgis/QGIS/issues/29454) | 再現できません |  |
| Path error GRASS plugin QGIS 3.14 | [#38595](https://github.com/qgis/QGIS/issues/38595) | [PR #38840](https://github.com/qgis/QGIS/pull/38840) | different packaging system\... |
| No Print dialog or Page Setup dialog in macOS | [#30791](https://github.com/qgis/QGIS/issues/30791) | 再現できません |  |
| Splash Screen Persists While \'Handle Bad Layers\' Dialog is Open | [#34784](https://github.com/qgis/QGIS/issues/34784) | [PR #38842](https://github.com/qgis/QGIS/pull/38842) | not appropriate |
| qgis terms of license pop up bug | [#38588](https://github.com/qgis/QGIS/issues/38588) | 再現できません |  |
| Cannot load pictures anymore in custom forms | [#30833](https://github.com/qgis/QGIS/issues/30833) | already fixed by [Mac Packager Issue #3](https://github.com/qgis/QGIS-Mac-Packager/issues/3) | not appropriate |
|  | [Mac Packager Issue #83](https://github.com/qgis/QGIS-Mac-Packager/issues/83) | [Mac Packager Commit 36f86759649abc4cb8f6875f6ad934070c13d56e](https://github.com/qgis/QGIS-Mac-Packager/commit/36f86759649abc4cb8f6875f6ad934070c13d56e) | different packaging system\... |
| Projections not reading in MacOS Nightly Build | [#38919](https://github.com/qgis/QGIS/issues/38919) | [PR #38922](https://github.com/qgis/QGIS/pull/38922) | different packaging system\... |
| layers in .osm format are not loading | [Mac Packager Issue #84](https://github.com/qgis/QGIS-Mac-Packager/issues/84) | 再現できません | works in 3.10 |
| missing metadata python package | [Mac Packager Issue #87](https://github.com/qgis/QGIS-Mac-Packager/issues/87) | [Mac Packager Commit 7c94749579acaf059e9b6c5094c7a2cb74d17f7a](https://github.com/qgis/QGIS-Mac-Packager/commit/7c94749579acaf059e9b6c5094c7a2cb74d17f7a) | different packaging system\... |
| GeoPDF Export fails | [Mac Packager Issue #75](https://github.com/qgis/QGIS-Mac-Packager/issues/75) | works now with qgis-deps-0.5.5 | different packaging system\... |
| GRASS Console not work on Mac | [#38961](https://github.com/qgis/QGIS/issues/38961) | [Mac Packager Commit bfc4ca0717de0e496d98f91e7a28e85216763ab1](https://github.com/qgis/QGIS-Mac-Packager/commit/bfc4ca0717de0e496d98f91e7a28e85216763ab1) | different packaging system\... |
| Processing Plugin Crashes QGIS on MacOS Nightly Build | [#38960](https://github.com/qgis/QGIS/issues/38960) | [PR #38973](https://github.com/qgis/QGIS/pull/38973) | different packaging system\... |
| Program crash when pasting file name | [#38939](https://github.com/qgis/QGIS/issues/38939) | 再現できません |  |
| Wrong Python default path in QGIS server on macOS | [#29843](https://github.com/qgis/QGIS/issues/29843) | [Mac Packager Commit 1a6ccb6e60adbfbbe05839e0c507e675a71c2491](https://github.com/qgis/QGIS-Mac-Packager/commit/1a6ccb6e60adbfbbe05839e0c507e675a71c2491) | different packaging system\... |
| qgis_map.fcgi on macOS doesn\'t find libraries | [#29399](https://github.com/qgis/QGIS/issues/29399) | [Mac Packager Commit 1a6ccb6e60adbfbbe05839e0c507e675a71c2491](https://github.com/qgis/QGIS-Mac-Packager/commit/1a6ccb6e60adbfbbe05839e0c507e675a71c2491) | different packaging system\... |
| GRASS provider cannot get projection | [#31397](https://github.com/qgis/QGIS/issues/31397) | [Mac Packager Commit bfdeab3f5c2ae9465efd1a55a29c0bbc9a88cd95](https://github.com/qgis/QGIS-Mac-Packager/commit/bfdeab3f5c2ae9465efd1a55a29c0bbc9a88cd95) | different packaging system\... |
| QGIS crashing on start on Mac | [#38858](https://github.com/qgis/QGIS/issues/38858) | corrupted user profile | N/A |
| Browser cannot open Volumes under macOS | [#29702](https://github.com/qgis/QGIS/issues/29702) | [PR #39096](https://github.com/qgis/QGIS/pull/39096) | no, not critial |
| MetaSearch unexpected keyword argument \'auth\' | [#38074](https://github.com/qgis/QGIS/issues/38074) | cannot reproduce on master | different packaging system\... |
| No QGIS plugins found in /Applications/QGIS3.10.app/Contents/MacOS/../PlugIns/qgis | [#39044](https://github.com/qgis/QGIS/issues/39044) | cannot reproduce on master | different packaging system\... |
| Browser Panel: unable to find all the connected drives | [#24641](https://github.com/qgis/QGIS/issues/24641) | duplicate of [#29702](https://github.com/qgis/QGIS/issues/29702) for MacOS |  |
| Provider Settings for GRASS avoid to active OTB | [#39112](https://github.com/qgis/QGIS/issues/39112) | cannot reproduce on master |  |
| Can\'t open GeoJSON vector via HTTP protocol on Windows and macOS | [#37107](https://github.com/qgis/QGIS/issues/37107) | \"[Mac Packager Commit d06bc3ac933c75071f36937aaf8189920dccc503](https://github.com/qgis/QGIS-Mac-Packager/commit/d06bc3ac933c75071f36937aaf8189920dccc503) | different packaging system\... |
| QGIS 3.0.1 Crash - Zooming in while moving node crashes QGIS | [#26509](https://github.com/qgis/QGIS/issues/26509) | 再現できません |  |
| Crash when switching user profiles (too early?) | [#26993](https://github.com/qgis/QGIS/issues/26993) | 再現できません |  |
| Aborted when debugging python plugin with pdb | [#27201](https://github.com/qgis/QGIS/issues/27201) | cannot reproduce/not valid |  |
| Customization: the widget catcher can\'t select icon from a toolbar when it\'s under a group of icons | [#22967](https://github.com/qgis/QGIS/issues/22967) | [PR #39209](https://github.com/qgis/QGIS/pull/39209) | not critical |
| QGIS on macOS can save file in qgz-format, but won\'t open files in qgz format | [#39204](https://github.com/qgis/QGIS/issues/39204) | 再現できません |  |
| Mouse pointer keeps switching type | [#32947](https://github.com/qgis/QGIS/issues/32947) | probably desired feature, not a bug |  |
| Aggregate function bug on macOS version | \"[#32932](https://github.com/qgis/QGIS/issues/32932) | cannot reproduce on master | different packaging system\... |
| Clear filter in Snapping Toolbar \> Edit advanced configuration causes crash | [#29750](https://github.com/qgis/QGIS/issues/29750) | cannot reproduce on master |  |
| Snapping Settings window with Night Mapping, low readability | [#29751](https://github.com/qgis/QGIS/issues/29751) | already fixed |  |
| Merge raster fails in macOS | [#39213](https://github.com/qgis/QGIS/issues/39213) | cannot reproduce on master | different packaging system\... |
| Can\'t get info on WFS feature in MacOS nightly build | [#39223](https://github.com/qgis/QGIS/issues/39223) | [Mac Packager Commit 54872e06a43ef61bf6dae8242e121bd5cec8be11](https://github.com/qgis/QGIS-Mac-Packager/commit/54872e06a43ef61bf6dae8242e121bd5cec8be11) | different packaging system\... |
| QGIS 3.4.10がクラッシュする - Python | [#31304](https://github.com/qgis/QGIS/issues/31304) | already fixed | already fixed |
| Exporting GRASS vector (save as\...) crashes QGIS | [#37508](https://github.com/qgis/QGIS/issues/37508) | [PR #39284](https://github.com/qgis/QGIS/pull/39284) | TODO |
| Crash when loading 3D project with DEM terrain and symbols that uses height value over the terrain | [#35483](https://github.com/qgis/QGIS/issues/35483) | [PR #39287](https://github.com/qgis/QGIS/pull/39287) | TODO |
| Creating 3D View from raster | [#37163](https://github.com/qgis/QGIS/issues/37163) | duplicate of [#35483](https://github.com/qgis/QGIS/issues/35483) | N/A |
| Crash when moving camera in 3D | \"[#37881](https://github.com/qgis/QGIS/issues/37881) | cannot reproduce on master |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Peter Petrik](https://www.lutraconsulting.co.uk/)
### Bug fixes by Paul Blottiere
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Linebreak issue with editing expression of \"Title Label Decoration\" | [#37803](https://github.com/qgis/QGIS/issues/37803) | [PR #38817](https://github.com/qgis/QGIS/pull/38817) | [PR #38748](https://github.com/qgis/QGIS/pull/38748) |
| QGIS Server GetPrint: EXTERNAL_WMS layer on top of QGIS layer | [#35873](https://github.com/qgis/QGIS/issues/35873) | [PR #38548](https://github.com/qgis/QGIS/pull/38548) | N/A |
| Fixes OGC API Features certification | not reported | [PR #37622](https://github.com/qgis/QGIS/pull/37622) | N/A |
| Outdated help for labels \"data-defined\" placement group options | [#36680](https://github.com/qgis/QGIS/issues/36680) | [PR #37344](https://github.com/qgis/QGIS/pull/37344) |  |
| Server GetFeatureInfo returns 0 where is should return NULL | [#37781](https://github.com/qgis/QGIS/issues/37781) | [PR #38807](https://github.com/qgis/QGIS/pull/38807) |  |
| z function returns Nan when used with a 2d point geometry | [#37772](https://github.com/qgis/QGIS/issues/37772) | [PR #38831](https://github.com/qgis/QGIS/pull/38831) |  |
| m function returns Nan when used with a 2d point geometry | not reported | [PR #38831](https://github.com/qgis/QGIS/pull/38831)/commits/829ee25d431b2b3d1ea08fa8a930bb519ab2dd2f |  |
| processing.algorithmHelp from terminal (outside QGIS desktop) | [#37524](https://github.com/qgis/QGIS/issues/37524) | 再現できません |  |
| Cache join layer in memory\" not toggling when editing join properties | [#37326](https://github.com/qgis/QGIS/issues/37326) | [PR #38838](https://github.com/qgis/QGIS/pull/38838) |  |
| Map tips should not appear for invisible features | [#37066](https://github.com/qgis/QGIS/issues/37066) | [PR #38861](https://github.com/qgis/QGIS/pull/38861) |  |
| Merge features: manual value is not respected | [#37659](https://github.com/qgis/QGIS/issues/37659) | [PR #39083](https://github.com/qgis/QGIS/pull/39083) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Paul Blottiere](https://hytech-imaging.fr/)
### Bug fixes by Matthias Kuhn
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Legend nodes overlapping each other after inserting | [#38881](https://github.com/qgis/QGIS/issues/38881) | [PR #38882](https://github.com/qgis/QGIS/pull/38882) | not critical |
| Poor legend performance with complex legends | [#38890](https://github.com/qgis/QGIS/issues/38890) | [PR #38891](https://github.com/qgis/QGIS/pull/38891) | not critical |
| AMS layers cannot be added when no project CRS is set | [#38892](https://github.com/qgis/QGIS/issues/38892) | [PR #38893](https://github.com/qgis/QGIS/pull/38893) | no intention |
| Legend performance problems | [#38978](https://github.com/qgis/QGIS/issues/38978) | [PR #39066](https://github.com/qgis/QGIS/pull/39066) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Matthias Kuhn](https://www.opengis.ch/)
### Julien Cabieces によるバグ修正
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| QgsProcessingAlgRunnerTask started inside function crashes QGIS | [#38583](https://github.com/qgis/QGIS/issues/38583) | Won't fix |  |
| Geometry generator symbol not rendered if the feature itself is not on the map canvas | [#38579](https://github.com/qgis/QGIS/issues/38579) | フィードバック |  |
| Relation widget in input form tabs - NULL value filled with data in form | [#38549](https://github.com/qgis/QGIS/issues/38549) | Won't backport (too risky) | (Closed) [#38549](https://github.com/qgis/QGIS/issues/38549) |
| Warning message: Missing layer form dependency : layer \'layerX\' requires layer \'layerY\' to be loaded | [PR #38802](https://github.com/qgis/QGIS/pull/38802) | [PR #38802](https://github.com/qgis/QGIS/pull/38802) | N/A |
| When embedding a layer, the display expression of a relation reference is not taken over | [#38422](https://github.com/qgis/QGIS/issues/38422) | Closed (FeatureRequest) |  |
| the keybord shortcut CTRL+C copy only the first cell, not the whole line | [#37503](https://github.com/qgis/QGIS/issues/37503) | [PR #38810](https://github.com/qgis/QGIS/pull/38810) |  |
| if shortcut is set for copy features then Ctrl+C not working anymore | [#37401](https://github.com/qgis/QGIS/issues/37401) | #37503の重複 |  |
| Organize columns not working if the table is empty | [#38653](https://github.com/qgis/QGIS/issues/38653) | Upstream (Qt) |  |
| Copy and paste style for forms ignores edit widget type | [#37702](https://github.com/qgis/QGIS/issues/37702) | [PR #38836](https://github.com/qgis/QGIS/pull/38836) |  |
| Keep order when drag and drop multiple widget | [#37038](https://github.com/qgis/QGIS/issues/37038) | [PR #38844](https://github.com/qgis/QGIS/pull/38844) | [PR #39239](https://github.com/qgis/QGIS/pull/39239) |
| QGIS crash removing QgsAnnotation in python | [#36098](https://github.com/qgis/QGIS/issues/36098) | フィードバック |  |
| Error in SQL statement for Virtual layers may lock layers in map canvas | [#34378](https://github.com/qgis/QGIS/issues/34378) | [PR #38949](https://github.com/qgis/QGIS/pull/38949) | [PR #39023](https://github.com/qgis/QGIS/pull/39023) |
| Virtual field in virtual layer not found | [#38523](https://github.com/qgis/QGIS/issues/38523) | フィードバック |  |
| Closed ID column for temporary layer is not detected when creating virtual layers using data source manager | [#34830](https://github.com/qgis/QGIS/issues/34830) | Won't fix |  |
| Boolean virtual field unusable in virtual layers | [#31798](https://github.com/qgis/QGIS/issues/31798) | [PR #38957](https://github.com/qgis/QGIS/pull/38957) | [PR #38748](https://github.com/qgis/QGIS/pull/38748) |
| fails to generate virtual geometry layer based on virtual wkt field | [#28265](https://github.com/qgis/QGIS/issues/28265) | フィードバック |  |
| Closed virtual fields can\'t be filtered | [#28072](https://github.com/qgis/QGIS/issues/28072) | Not reproduced |  |
| Qgis crached after calculated field removed | [#26486](https://github.com/qgis/QGIS/issues/26486) | Not reproduced |  |
| sql \"order by\" does not work with the \"Add/Edit Virtual Layer\" feature | [#29043](https://github.com/qgis/QGIS/issues/29043) | Won't fix |  |
| Form fails to initialize \$geometry | [#34791](https://github.com/qgis/QGIS/issues/34791) | [PR #39041](https://github.com/qgis/QGIS/pull/39041) |  |
| Oracle - can\'t create or a modify a connection | [#38979](https://github.com/qgis/QGIS/issues/38979) | [PR #39131](https://github.com/qgis/QGIS/pull/39131) |  |
| Test connection Oracle DB ready - OK greyed out ! | [#39116](https://github.com/qgis/QGIS/issues/39116) | #38979の重複 |  |
| Scale dependent snapping does not activate as long as it displays the scale as \"1:xxxxxx\" | [#39031](https://github.com/qgis/QGIS/issues/39031) | [PR #39133](https://github.com/qgis/QGIS/pull/39133) | N/A |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Julien Cabieces](https://www.oslandia.com/)
### Denis Rouzaud によるバグ修正
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| correctly determine if variables are static in aggregate expression and filter, give \@parent in generic aggregates | [#33382](https://github.com/qgis/QGIS/issues/33382) | [PR #39391](https://github.com/qgis/QGIS/pull/39391) | いいえ |
| Freeze when using aggregate in a virtual field | [#39366](https://github.com/qgis/QGIS/issues/39366) | Won't fix |  |
| Fix SVG marker anchor calculation and improve bounds | [PR #39336](https://github.com/qgis/QGIS/pull/39336) |  |  |
| Improve SVG UI + remove duplicated code | [PR #39421](https://github.com/qgis/QGIS/pull/39421) |  |  |
| Improve SVG UI + remove duplicated code | [PR #39519](https://github.com/qgis/QGIS/pull/39519) |  |  |
| Improve SVG UI + remove duplicated code | [PR #39524](https://github.com/qgis/QGIS/pull/39524) |  |  |
| Fix duplicating features | [PR #39548](https://github.com/qgis/QGIS/pull/39548) |  |  |
| fix duplication of feature being stopped at 1 level deep | [PR #39550](https://github.com/qgis/QGIS/pull/39550) |  |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Denis Rouzaud](https://www.opengis.ch/)
### Bug fixes by Olivier Dalang
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Core topology fixer issues | not reported | [PR #39392](https://github.com/qgis/QGIS/pull/39392) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Olivier Dalang](https://www.opengis.ch/)
### Nyall Dawsonによるバグ修正
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fix crash in dbmanager | [#38393](https://github.com/qgis/QGIS/issues/38393) | [Commit 8c623b268ed94ef65aa19e2271be10b75e1ef36a](https://github.com/qgis/QGIS/commit/8c623b268ed94ef65aa19e2271be10b75e1ef36a) | N/A |
| Fix GeoPDF page size issues when opened in Acrobat reader | [#33465](https://github.com/qgis/QGIS/issues/33465) | [Commit 460bf8e534eb32ccba665918a615b55a8cbccadd](https://github.com/qgis/QGIS/commit/460bf8e534eb32ccba665918a615b55a8cbccadd) | Delayed till more widespread user testing |
| Improve default lighting of 3d scenes | not reported | [Commit 350bc602e0ecd0f93dc2cc90ab34ce09993a687b](https://github.com/qgis/QGIS/commit/350bc602e0ecd0f93dc2cc90ab34ce09993a687b) | N/A |
| Allow conversion of QgsFeatureStoreList results to Python objects | [#39479](https://github.com/qgis/QGIS/issues/39479) | [Commit 49c508921d7ccb59b1f1abaff4f890456cca1455](https://github.com/qgis/QGIS/commit/49c508921d7ccb59b1f1abaff4f890456cca1455) | Too risky |
| Fix preview symbol when offsetting point symbols isn\'t shown correctly | not reported | [Commit 62409b92ce20a84dd92188cf42a98d7cdc0b08c3](https://github.com/qgis/QGIS/commit/62409b92ce20a84dd92188cf42a98d7cdc0b08c3) | N/A |
| Use click-click behavior for rotate and offset marker tools | not reported | [Commit 00a3a6b8057f96dfa6c37943427a276cd3a5065d](https://github.com/qgis/QGIS/commit/00a3a6b8057f96dfa6c37943427a276cd3a5065d) | N/A |
| Avoid massive UI hangs when a layer has complicated actions defined | not reported | [Commit 9aa805c15bb2cf8f9ba33fd2905f5784d6eb4668](https://github.com/qgis/QGIS/commit/9aa805c15bb2cf8f9ba33fd2905f5784d6eb4668) | Too risky |
| Ensure display expression is used for map action tool, not raw feature ids | not reported | [Commit e304d4d7e3eae0f48f336c7eb34542be6055df5d](https://github.com/qgis/QGIS/commit/e304d4d7e3eae0f48f336c7eb34542be6055df5d) | 低優先度 |
| Improve UX when configuring lights in a 3d scene, fixes confusing interface | not reported | [Commit 3019b82100d4fc405f64cebcddf9aaae253c4293](https://github.com/qgis/QGIS/commit/3019b82100d4fc405f64cebcddf9aaae253c4293) | N/A |
| Fix features with invalid geometries cannot be selected | [#38460](https://github.com/qgis/QGIS/issues/38460) | [Commit 22c2c5a41c7ca25cb1fdbb0e121578a2d9386d4d](https://github.com/qgis/QGIS/commit/22c2c5a41c7ca25cb1fdbb0e121578a2d9386d4d) | N/A |
| Expose metadata tab for mesh layers | not reported | [Commit 9482b1be70f36f778f6a409847244c5ff8a6a739](https://github.com/qgis/QGIS/commit/9482b1be70f36f778f6a409847244c5ff8a6a739) | N/A |
| Fix missing text codecs on Windows installs | [#36871](https://github.com/qgis/QGIS/issues/36871) | [Commit c3ca85e60bec73056bd87c426fd71c8f578363cb](https://github.com/qgis/QGIS/commit/c3ca85e60bec73056bd87c426fd71c8f578363cb) | Too risky |
| Don\'t force a whole layout map to be rasterised just because one vector layer has non 100% opacity | not reported | [Commit 2d15a4cfad6c732cf640fbb0eabd625856b643ca](https://github.com/qgis/QGIS/commit/2d15a4cfad6c732cf640fbb0eabd625856b643ca) | Too risky |
| Ensure mesh layer properties follows same appearance as other layer types | not reported | [Commit 3c67e1acde24a49bcb0356c2ef5ed6cb8102fdac](https://github.com/qgis/QGIS/commit/3c67e1acde24a49bcb0356c2ef5ed6cb8102fdac) | N/A |
| Speed up mesh triangulation algorithm by avoiding a bunch of unnecessary QVector detachments | not reported | [Commit 46ef391a7acf10515a11c19b69fafa4548046448](https://github.com/qgis/QGIS/commit/46ef391a7acf10515a11c19b69fafa4548046448) | N/A |
| Don\'t allow users to set 3d terrain to mesh or DEM without selecting an elevation layer, instead show friendly warning | not reported | [Commit 0d9f1da846c70764fa6840309b5460f713b30e1f](https://github.com/qgis/QGIS/commit/0d9f1da846c70764fa6840309b5460f713b30e1f) | N/A |
| Avoid 3d map config dialog opening with initially out-of-sync selected pane | not reported | [Commit 8b6477208f3c34e228734f7c04d32625965c48ed](https://github.com/qgis/QGIS/commit/8b6477208f3c34e228734f7c04d32625965c48ed) | N/A |
| Fix menu not shown when clicking \'add\' item in style manager dialog and color ramp tab is active | not reported | [Commit a085ce84b81a46896c9f00ee64eccaea63dad29a](https://github.com/qgis/QGIS/commit/a085ce84b81a46896c9f00ee64eccaea63dad29a) | N/A |
| Fix trying to create new color ramp from first page in style manager dialog does nothing | not reported | [Commit 34fb646f7ab69f20072b4d74ebec0595054089d7](https://github.com/qgis/QGIS/commit/34fb646f7ab69f20072b4d74ebec0595054089d7) | N/A |
| \[processing\] Fix generated layers stored in geopackage always report a feature count of 0 | not reported | [Commit 0675d99b34ee209a09857dfcba47cb5a92f55154](https://github.com/qgis/QGIS/commit/0675d99b34ee209a09857dfcba47cb5a92f55154) | Too risky |
| Fix Import Geotagged photos algorithm incorrectly assigns form widgets when saving the results to GPKG | not reported | [Commit ff336ade18f4d6b307e4ed0e98fee77ee11a157c](https://github.com/qgis/QGIS/commit/ff336ade18f4d6b307e4ed0e98fee77ee11a157c) | [PR #39563](https://github.com/qgis/QGIS/pull/39563) |
| \[processing\] Ensure driverName is passed to QgsVectorLayerExporter so that GPKG specific optimisations can be applied when saving outputs to geopackage | not reported | [Commit 501c63feb3887e18da35188062546186d8a767ac](https://github.com/qgis/QGIS/commit/501c63feb3887e18da35188062546186d8a767ac) | Too risky |
| Update strings and UI regarding layer CRS override setting | [#32101](https://github.com/qgis/QGIS/issues/32101) | [Commit 06cfdd9563b15d8fbb27aee94b83d1b15773df77](https://github.com/qgis/QGIS/commit/06cfdd9563b15d8fbb27aee94b83d1b15773df77) | N/A |
| Use proper SQL code editor in filter preview widget in vector layer properties, don\'t show filter as disabled | not reported | [Commit 0f4270cfe600e77f09db7727bd3ba965be7acb0e](https://github.com/qgis/QGIS/commit/0f4270cfe600e77f09db7727bd3ba965be7acb0e) | N/A |
| Fix boolean literal presentation in dox/PyQGIS docs | not reported | [Commit 746ee315bd0a4140f6e84617d547cc89103f79aa](https://github.com/qgis/QGIS/commit/746ee315bd0a4140f6e84617d547cc89103f79aa) | N/A |
| Speed up QGIS geometry validation | not reported | [Commit 2a15c3b0a4a631db1b55ac7e46256fdbd89949f9](https://github.com/qgis/QGIS/commit/2a15c3b0a4a631db1b55ac7e46256fdbd89949f9) | Too risky |
| \[processing\] Correctly discard fid field values when running algorithms with the RegeneratePrimaryKey flag in in-place mode | [#37761](https://github.com/qgis/QGIS/issues/37761), [#33816](https://github.com/qgis/QGIS/issues/33816) | [Commit db7b97705967041d4eaca7e7f69cbf49f5692aef](https://github.com/qgis/QGIS/commit/db7b97705967041d4eaca7e7f69cbf49f5692aef) | Too risky |
| \[processing\] When reporting that a feature is invalid, also mention the layer name | [#26664](https://github.com/qgis/QGIS/issues/26664) | [Commit a53bb3d49b59a3f814d862f30202ff156f74d6bc](https://github.com/qgis/QGIS/commit/a53bb3d49b59a3f814d862f30202ff156f74d6bc) | Too risky |
| Allow expanding xls, ods, gpx, pdf files in browser so that layer sources can be repaired for these file types | not reported | [Commit 252976b739527e213f5d1c8c98a345911dfeab32](https://github.com/qgis/QGIS/commit/252976b739527e213f5d1c8c98a345911dfeab32) | N/A |
| \[processing\] Fix \"Split with lines\" algorithm can get stuck in an endless loop | not reported | [Commit 05645b320d8547f50a308843e961e343c383036d](https://github.com/qgis/QGIS/commit/05645b320d8547f50a308843e961e343c383036d) | Too risky |
| Don\'t show cascaded feature deletion warnings and feedback if joined deleted features came from an auxilary layer | not reported | [Commit 8c79b94fcc14e41d4442a018554e889f81b8e080](https://github.com/qgis/QGIS/commit/8c79b94fcc14e41d4442a018554e889f81b8e080) | N/A |
| Fix crash in undo dock when clearing project/closing QGIS | [#38157](https://github.com/qgis/QGIS/issues/38157) | [Commit d87d230bb4bcbe091fe35bb047d54f7d9fcaabb8](https://github.com/qgis/QGIS/commit/d87d230bb4bcbe091fe35bb047d54f7d9fcaabb8) | [Commit 5c97ff66dd90d450a1ec60583da9626c14c9c08c](https://github.com/qgis/QGIS/commit/5c97ff66dd90d450a1ec60583da9626c14c9c08c) |
| Fix copy/paste/select all shortcuts don\'t work when layer tree is selected | [#38849](https://github.com/qgis/QGIS/issues/38849) | [Commit 02d7afae3f8699e83efacc781d3266700397d8b8](https://github.com/qgis/QGIS/commit/02d7afae3f8699e83efacc781d3266700397d8b8) | N/A |
| Fix edited and new features no longer correctly show their corresponding color shading in the feature list view | not reported | [Commit a195b056624c2fabe231be7c0e96c3d63e052e5b](https://github.com/qgis/QGIS/commit/a195b056624c2fabe231be7c0e96c3d63e052e5b) | Too risky/low priority |
| ALWAYS load processing plugin in qgis_process tool | [#37989](https://github.com/qgis/QGIS/issues/37989) | [Commit bc0df6d25e929a575d0821208f7d187737d80709](https://github.com/qgis/QGIS/commit/bc0df6d25e929a575d0821208f7d187737d80709) | N/A |
| Add \--json option to qgis_process tool | <https://github.com/paleolimbot/qgisprocess/issues/21> | [Commit fc8d916b8dd444b3edaee3c18ec308e74a9bb91e](https://github.com/qgis/QGIS/commit/fc8d916b8dd444b3edaee3c18ec308e74a9bb91e) | N/A |
| Ensure all code editors in QGIS follow the same appearance and behavior | not reported | (many) | N/A |
| When creating a CRS from WKT and the WKT has an embedded CRS name, correctly use this to set the QgsCoordinateReferenceSystem description | not reported | [Commit 9a35b27630982d63101c57c3e3440dcbf1a7786f](https://github.com/qgis/QGIS/commit/9a35b27630982d63101c57c3e3440dcbf1a7786f) | Possible after further user testing |
| Big speed up for scripts which fire off many individual feature requests to a memory provider layer | not reported | [Commit 1d2bb41752c51e6c9b84124a1ce1599d3d42b41c](https://github.com/qgis/QGIS/commit/1d2bb41752c51e6c9b84124a1ce1599d3d42b41c) | Too risky |
| \[console\] Fix exception when running scripts | not reported | [Commit 5c8013df6129a2bc06d25a98ff20dbf27621bff5](https://github.com/qgis/QGIS/commit/5c8013df6129a2bc06d25a98ff20dbf27621bff5) | N/A |
| \[layouts\] Fix resizing multiline label items to adjust to the size of their text | not reported | [Commit 6829e6351e1dab18f1fa0c0443107eb7617794c7](https://github.com/qgis/QGIS/commit/6829e6351e1dab18f1fa0c0443107eb7617794c7) | Too risky |
| Improve appearance of PyQGIS documentation for functions which return multiple values | not reported | [Commit 0001ec27a43cbf4c99d1525c3c5f75183e96f5c3](https://github.com/qgis/QGIS/commit/0001ec27a43cbf4c99d1525c3c5f75183e96f5c3) | N/A |
| \[processing\] Don\'t raise a generic \"something went wrong\" exception when calling processing.run(), instead use proper descriptive exception | not reported | [Commit 2207c30a247e5907a12185165b4bd220e255bbdc](https://github.com/qgis/QGIS/commit/2207c30a247e5907a12185165b4bd220e255bbdc) | Too risky |
| \[processing\] Fix execution of \"Eliminate selection\" through Python | [#38808](https://github.com/qgis/QGIS/issues/38808) | [Commit ee7bea2305253fd276a69c25bb5d308942dcb190](https://github.com/qgis/QGIS/commit/ee7bea2305253fd276a69c25bb5d308942dcb190) | Too risky |
| \[3d\] Fix crash when line feature cannot be buffered | not reported | [Commit f6eed85729a8cbf913155ae16df7499f688ba0fa](https://github.com/qgis/QGIS/commit/f6eed85729a8cbf913155ae16df7499f688ba0fa) | [Commit d4c963e1c2fdc497dba038896caf2b3f975240ff](https://github.com/qgis/QGIS/commit/d4c963e1c2fdc497dba038896caf2b3f975240ff) |
| Fix custom stroke patterns incorrectly scale when data defined stroke width is set | [#39201](https://github.com/qgis/QGIS/issues/39201) | [Commit 03fdc0cd7992a7883183704cd68506f32afe9ca3](https://github.com/qgis/QGIS/commit/03fdc0cd7992a7883183704cd68506f32afe9ca3) | Too risky |
| Allow columns to be resized in datum transformation table | [#39169](https://github.com/qgis/QGIS/issues/39169) | [Commit 1cd5a3358b235f67b6b4d95331ce561e9f8cb715](https://github.com/qgis/QGIS/commit/1cd5a3358b235f67b6b4d95331ce561e9f8cb715) | N/A |
| Fix settings incorrectly show for wrong layer types in labeling dialog | [#39168](https://github.com/qgis/QGIS/issues/39168) | [Commit 2e948884c029c9f79639201943ec4bc36dba3573](https://github.com/qgis/QGIS/commit/2e948884c029c9f79639201943ec4bc36dba3573) | N/A |
| \[processing\] Fix error reporting from batch dialog | [#39197](https://github.com/qgis/QGIS/issues/39197) | [Commit 5243a8594cc39540f2c01201415633801a22ff43](https://github.com/qgis/QGIS/commit/5243a8594cc39540f2c01201415633801a22ff43) | N/A |
| \[processing\] Fix crash when renaming conditional branch in modeler | [#39053](https://github.com/qgis/QGIS/issues/39053) | [Commit ddae53b7b789467bf17b21d6f4b884e827fbd3c5](https://github.com/qgis/QGIS/commit/ddae53b7b789467bf17b21d6f4b884e827fbd3c5) | N/A |
| \[processing\] Fix crash in model designer when a child algorithm contains hidden parameters | not reported | [Commit f3c9f9bfbc2fc456c77965be4c1e65cc692bc0d0](https://github.com/qgis/QGIS/commit/f3c9f9bfbc2fc456c77965be4c1e65cc692bc0d0) | N/A |
| Ensure True/False are treated as Python keywords in Python code editor | not reported | [Commit 5f661045c078b7938550c2c9d0798664c6f65f5a](https://github.com/qgis/QGIS/commit/5f661045c078b7938550c2c9d0798664c6f65f5a) | N/A |
| Don\'t silently close QGIS with unsaved changes in the console script editors | [#38529](https://github.com/qgis/QGIS/issues/38529) | [Commit 9093bdfd1e46ba65af78c5fc01bcb4df1ed6a0e9](https://github.com/qgis/QGIS/commit/9093bdfd1e46ba65af78c5fc01bcb4df1ed6a0e9) | Too risky |
| Fix dropping processing script algorithm .py file on QGIS no longer triggers the algorithm to execute | not reported | [Commit 64bf347d7e1d664fc674c5ca602ce6c4bedecdf9](https://github.com/qgis/QGIS/commit/64bf347d7e1d664fc674c5ca602ce6c4bedecdf9) | N/A |
| Fix message log dock causes havoc with other docks placed in the same area | [#31955](https://github.com/qgis/QGIS/issues/31955) | [Commit 384f6a1d9257a05eaa58942921c94f1dd4941cd3](https://github.com/qgis/QGIS/commit/384f6a1d9257a05eaa58942921c94f1dd4941cd3) | Too risky |
| When restoring a custom CRS from XML, if the CRS does NOT match any of the existing user defined CRS\'s on the QGIS profile then still restore the previously saved name of the custom CRS | not reported | [Commit e6d316ace7031821e04ca625e35f7c2c4d57f639](https://github.com/qgis/QGIS/commit/e6d316ace7031821e04ca625e35f7c2c4d57f639) | Possible after further user testing |
| Don\'t refer to valid but custom CRSes as \"Unknown CRS\" and instead use \"Custom CRS\" phrasing | not reported | [Commit d3833fd8d6c4b4f0673c4c2337044c224675185f](https://github.com/qgis/QGIS/commit/d3833fd8d6c4b4f0673c4c2337044c224675185f) | Possible after further user testing |
| Improve performance of processing batch process dialog with a large number of files | [#38987](https://github.com/qgis/QGIS/issues/38987) | [Commit 776768eb9f4ee2a8d13909b4ced5c175a0d05b3d](https://github.com/qgis/QGIS/commit/776768eb9f4ee2a8d13909b4ced5c175a0d05b3d) | Too risky |
| Improve behavior of CRS selector and transformation widgets | not reported | many | N/A |
| \[layouts\] Use standard CRS selector widget for map grid CRS choice | [#26548](https://github.com/qgis/QGIS/issues/26548) | [Commit 4c7fbc0260ef95f7dd6dd4b6954ee2086ad3da70](https://github.com/qgis/QGIS/commit/4c7fbc0260ef95f7dd6dd4b6954ee2086ad3da70) | Too risky |
| \[layouts\] When selecting a CRS for a map item, don\'t show misleading no crs option at the top of the dialog | not reported | [Commit c3a26db4babbef46ae1b7904bb9d1f0ee9e273ad](https://github.com/qgis/QGIS/commit/c3a26db4babbef46ae1b7904bb9d1f0ee9e273ad) | Too risky |
| Fix \"layer has no CRS\" message incorrectly show at the top of many projection selection dialog boxes | not reported | [Commit c68d05cc40f8f2c828e5204e6e4f5f11e68b4a7c](https://github.com/qgis/QGIS/commit/c68d05cc40f8f2c828e5204e6e4f5f11e68b4a7c) | Too risky |
| Fix crash when editing style and opening a project | [#38920](https://github.com/qgis/QGIS/issues/38920) | [Commit 67ec244864ca6f9290e1f35a1a0c60b4888fe686](https://github.com/qgis/QGIS/commit/67ec244864ca6f9290e1f35a1a0c60b4888fe686) | [PR #38748](https://github.com/qgis/QGIS/pull/38748)/commits/ecf96231aefa5628539f0b63ca313ea8b20c9548 |
| Avoid qt warning when dragging a non-color object over color buttons | not reported | [Commit fd771bba68da84b1ce8023898b9662b5dc619693](https://github.com/qgis/QGIS/commit/fd771bba68da84b1ce8023898b9662b5dc619693) | N/A |
| Fix shift in geopdf feature positions when using geographic CRS at large scales | [#37755](https://github.com/qgis/QGIS/issues/37755) | [Commit 0b77f187ec5a14651457fd07f306cba2511fb854](https://github.com/qgis/QGIS/commit/0b77f187ec5a14651457fd07f306cba2511fb854) | [PR #38748](https://github.com/qgis/QGIS/pull/38748)/commits/b705d29c73e81fe87e2e301c7028e5e659d80364 |
| Fix constraint metadata is duplicated after opening layer properties | [#38916](https://github.com/qgis/QGIS/issues/38916) | [Commit 6a002573c00a8a8e11443eaca28b57a8ad6de4c0](https://github.com/qgis/QGIS/commit/6a002573c00a8a8e11443eaca28b57a8ad6de4c0) | [PR #38748](https://github.com/qgis/QGIS/pull/38748)/commits/49260b8f1f4b1ddd9a25c7160f32570221f3989e |
| Fix PDF export includes vector information outside of the area of interest | [#38878](https://github.com/qgis/QGIS/issues/38878) | [Commit f3f226aa69a19b31dd8a1b83c82319528e061cfe](https://github.com/qgis/QGIS/commit/f3f226aa69a19b31dd8a1b83c82319528e061cfe) | Too risky |
| \[layouts\] Fix legend symbol rendering doesn\'t respect linked map scale when symbol uses map unit based sizes | [#38326](https://github.com/qgis/QGIS/issues/38326) | [Commit 426ee2120b33a8613f3e476da3c2eba0a00f65d7](https://github.com/qgis/QGIS/commit/426ee2120b33a8613f3e476da3c2eba0a00f65d7) | N/A |
| Don\'t try to write empty rendered rings/geometries to GeoPDF outputs | not reported | [Commit 96753cfd1b9e986841158675bda365e585c48c27](https://github.com/qgis/QGIS/commit/96753cfd1b9e986841158675bda365e585c48c27) | Possible after further user testing |
| Correctly apply capitalization setting whenever QgsTextRenderer is used, not just in labeling | [#38898](https://github.com/qgis/QGIS/issues/38898) | [Commit e1ca83b2c24c51e7ff67a53278ffd2601c0459be](https://github.com/qgis/QGIS/commit/e1ca83b2c24c51e7ff67a53278ffd2601c0459be) | Too risky |
| Fix qgis_process list raises exception if processing algorithm provider is activated | [#38862](https://github.com/qgis/QGIS/issues/38862) | [Commit 772181bc16820d7dd5ee8d967355dbdfde5a8efe](https://github.com/qgis/QGIS/commit/772181bc16820d7dd5ee8d967355dbdfde5a8efe) | N/A |
| Dramatic speed up for calling some frequently used methods from PyQGIS | not reported | [Commit d4a2dddac5a2fd4fcf901cc3d50f70a6119ca1ca](https://github.com/qgis/QGIS/commit/d4a2dddac5a2fd4fcf901cc3d50f70a6119ca1ca) | Too risky |
| \[processing\] Fix certain characters show as HTML escaped in processing log | [#37934](https://github.com/qgis/QGIS/issues/37934) | [Commit 965595d25bd0a69875ba8a405d3b365bedfe2a12](https://github.com/qgis/QGIS/commit/965595d25bd0a69875ba8a405d3b365bedfe2a12) | N/A |
| Fix incorrect capitalization in title of new layout name dialog | not reported | [Commit 92d0ec59a1c26c4ac33d35b9e6c93344845eddca](https://github.com/qgis/QGIS/commit/92d0ec59a1c26c4ac33d35b9e6c93344845eddca) | N/A |
| Add a new capitalization option for \"Title Case\", and rename the confusing \"Capitalize First Letter\" option to Force First Letter to Capital | [#16539](https://github.com/qgis/QGIS/issues/16539) | [Commit 484ba6f979cdcaabffe823c72b35b57d1b1c7aad](https://github.com/qgis/QGIS/commit/484ba6f979cdcaabffe823c72b35b57d1b1c7aad) | N/A |
| Add a Legend category to the style selection widgets and allow legend settings to be stored and restored in QML | [#37683](https://github.com/qgis/QGIS/issues/37683) | [Commit f018252023275f95c167d7f308d05c8819d6db0b](https://github.com/qgis/QGIS/commit/f018252023275f95c167d7f308d05c8819d6db0b) | Too risky |
| Fix \[Style\] Export \--\> Save as QGIS Layer style File should allow to select style categories (and output format) | [#29145](https://github.com/qgis/QGIS/issues/29145) | [Commit 1ad2e78735e57cef218a7470d7eec645c2f45263](https://github.com/qgis/QGIS/commit/1ad2e78735e57cef218a7470d7eec645c2f45263) | Too risky |
| \[browser\] Correctly save expanded node state when closing QGIS | not reported | [Commit 2eff061bf3cdcb3f36956e43098adfcb0359b5eb](https://github.com/qgis/QGIS/commit/2eff061bf3cdcb3f36956e43098adfcb0359b5eb) | Too risky |
| \[browser\] Gpkg and other container types can be dragged to the map to allow layers to be added from them | not reported | [Commit 0234d4e9e10f3fbb5732f66e00eebd038f502ab0](https://github.com/qgis/QGIS/commit/0234d4e9e10f3fbb5732f66e00eebd038f502ab0) | Too risky |
| Don\'t prompt for CRS for annotation layers | [#38739](https://github.com/qgis/QGIS/issues/38739) | [Commit 15975c1d5191933311d81a494d87806f4e73ce57](https://github.com/qgis/QGIS/commit/15975c1d5191933311d81a494d87806f4e73ce57) | N/A |
| Fix reading saved color map file when an item\'s label contains a comma character | [#24112](https://github.com/qgis/QGIS/issues/24112) | [Commit 252149375c750d6a8f1ee281c1cc9d03de272170](https://github.com/qgis/QGIS/commit/252149375c750d6a8f1ee281c1cc9d03de272170) | Too risky |
| Fix diagram settings are not correctly restored when loading a QML file | [#35343](https://github.com/qgis/QGIS/issues/35343) | [Commit 4668927ce432b198b3c572535ff234343c5042f5](https://github.com/qgis/QGIS/commit/4668927ce432b198b3c572535ff234343c5042f5) | Too risky |
| Fix can no longer paste colors from text strings | not reported | [PR #39561](https://github.com/qgis/QGIS/pull/39561) | N/A |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Nyall Dawson](https://north-road.com/)

{{<content-end >}}
