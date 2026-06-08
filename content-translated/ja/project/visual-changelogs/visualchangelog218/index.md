---
HasBanner: false
draft: false
releaseDate: '2016-10-21'
section: project
sidebar: true
title: QGIS 2.18の変更履歴
type: visual-changelog

---
{{<content-start >}}
# QGIS 2.18の変更履歴{#changelog218 }
![image1](images/projects/ac3b0a08203e87505a823b0d8a0895d44489f916.png)

リリース日: 2016-10-21

これは2.xシリーズの最後のリリースです。現在のロングタームリリース（LTR）はバージョン2.14.xのままです。このリリースでは、以前のリリースよりも漸進的な改良が施されています。活動の大部分は、現在、2017年の第1四半期末に予定されている次世代リリースであるQGIS 3.0の開発に焦点を当てています。

**謝辞**

We would like to thank the developers, documenters, testers and all the many folks out there who volunteer their time and effort (or fund people to do so). From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

QGIS is supported by donors and sponsors. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become and official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

QGIS はフリーのソフトウェアです。利用する上で金銭を支払う義務はありません。実際、私たちは利用者の財政状況や社会的地位にかかわらず、より多くの人に QGIS を利用して欲しいと思っています。私たちは地理空間的な意思決定ツールによって人々が力を持つことが、全人類の社会をより良くすると信じています。

{{<table-of-contents >}}
## QGISバージョン2.18.0のスポンサー
私たちは毎年、私たちがやっていることを評価して、プロジェクトに取り込まれる持続的な開発努力を促進しようとしてくれる様々な組織からの支援を受けています。これらのスポンサーを感謝とともに以下に記します。

{{<fund type="changelog" relativeImgPath=true >}}
## 一般情報
### 機能：地物情報の中の自動リンク
Any `http` or `mailto` links within attribute values will now automatically be converted to clickable links within the identify results panel.

![image58](images/entries/eab95eb0acb92a68edeee71a13ea23d77b88d307.png.400x300_q85_crop.webp)

This feature was developed by [Sandro Mani (Sourcepole)](https://sourcepole.ch/)
### 機能：マウスホイールをカラーダイアログのスライダーに重ねる
QGIS 2.18では、カラーピッカーダイアログ内のいずれかのスライダ上でマウスホイールをスクロールして、値を少しずつ増やすことができます。これは、色のコンポーネントを微調整するための便利なショートカットです。

![image59](images/entries/ab472e2c8270ba64bee64bbbf8c9f5104edc79de.gif)

This feature was funded by [Nyall Dawson (North Road)](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### 機能：カスタムカラースキームをカラーボタンドロップダウンメニューに追加する
QGIS 2.18 adds the ability for users to set whether a user created color scheme should show up in the color button drop-down menus. This setting is controlled through the color picker dialog, on the lists tab. Just add a new color scheme, then from the scheme menu tick the new \"show in buttons\" option. It\'s a handy shortcut if you have sets of common palettes and want them to be instantly available through the color menu.

![image60](images/entries/9453954d199c4950d7aecf153b6d5e53f820ff19.PNG.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## シンボロジ
### 機能：レイヤースタイルのパネルにカラーピッカーが埋め込まれました
QGIS 2.18では、レイヤースタイルパネル内のカラーボタンをクリックすると、別のダイアログとしてではなく、スタイルパネル自体でカラーピッカーダイアログが開きます。これにより、色をインタラクティブに変更して結果を即座にプレビューできます。

![image42](images/entries/3af7533f5148810d0c26a221d7acdccaf1d7a835.png.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## ラベリング
### 機能：ラベル付けの代替リストサポート
ラベルテキストに適用するテキスト置換のリストを指定する機能を追加します。例：通りの種類を省略します。

ユーザーは代替品のリストをエクスポートおよびインポートして、再利用および共有を容易にすることができます。

![image43](images/entries/a73aec5fad4c5e39800e462bbac6dd2597f98cba.png.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### 機能：改良されたラインラベル配置アルゴリズム
ラインレイヤーのパラレルラベリングモードは大幅に改善されました。新しいアルゴリズムにより、地物ジオメトリのジグザグ部分にラベルを配置することはありません。

![image44](images/entries/5b77d12263e0dabfb0649f27d92188613796f409.png.400x300_q85_crop.webp)

この機能はAndreas Neumannによって資金提供されました

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### 機能：周囲に沿って曲線ラベルを使用してポリゴンにラベルを付ける
これにより、ポリゴンの外周に曲線ラベルを使用してラベルを付ける新しいモードが追加されます。

![image45](images/entries/c7a28cf09a0f1646210faaae85a56c2209ee15e9.PNG.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## レンダリング
### 機能：ラスタータイルのプレビュー（WMTSおよびXYZレイヤー）
QGISの以前のバージョンでは、結果の地図を表示するために、レイヤーのすべてのタイルのダウンロードが完了するまで待つ必要がありました。これは今修正され、地図のキャンバスにタイルがダウンロードされるとすぐに表示され、何かが表示されるまでの時間を大幅に短縮することでユーザーエクスペリエンスが向上します。さらに、より低い解像度またはより高い解像度からの以前にダウンロードされたタイルは、正しい解像度を有するタイルがまだダウンロードされていない領域のプレビュー機能に使用されてもよい。

![image46](images/entries/007bf6d09a1f67e0c0c4ee71d48081185c0c5c84.gif)

This feature was funded by [Land Information New Zealand](http://www.linz.govt.nz/)

This feature was developed by [Martin Dobias (Lutra Consulting)](http://www.lutraconsulting.co.uk/)
### 機能：ラスター（WMS、WMTS、WCS、XYZレイヤー）のキャンセル可能なレンダリング
この機能強化により、リモートサーバーからのラスターレイヤーを操作する際のユーザーエクスペリエンスが向上します。以前は、ユーザーインターフェースがその間に凍っていたので、地図を再びズームまたはパンできるように、ダウンロードが完全に完了するまで待つ必要がありました。これは、ラスターレイヤーのレンダリングがいつでもキャンセルできるという事実によって修正されています。

This feature was funded by [Land Information New Zealand](http://www.linz.govt.nz/)

This feature was developed by [Martin Dobias (Lutra Consulting)](http://www.lutraconsulting.co.uk/)
## データ管理
### 機能：選択した機能のみをコピーするフラグを追加する
オフライン編集プラグインは、QGISに同梱されているデフォルトのプラグインで、リモートデータセット（データベースなど）をオフライン化してフィールドで編集し、オフィスに戻ったときに再同期化することができます。これにより、オフライン編集の可能性が拡張され、大きなレイヤーのサブセットでしか動作しません。

![image47](images/entries/ec977674f356d5376d19be49534818a4cc830c64.png.400x300_q85_crop.webp)

この機能は、DB Fahrwegdienste GmbH によって資金提供されました

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch/)
## フォームとウィジェット
### 機能：個々の編集ウィジェットのラベルを制御できるようにする
フォーム内の個々の編集ウィジェットのラベルを制御できるようにする。ドラッグアンドドロップデザイナーでは、項目をダブルクリックすると、各項目ごとにラベルを個別に表示するかどうかを制御できます。

In addition it is possible to configure if the link/unlink buttons are shown in relation reference widget, which is useful to hide in 1:n relations where a child can\'t exist without its parents.

![image48](images/entries/6d827c6b286f137ec9de1d97a15c745764494d0a.png.400x300_q85_crop.webp)

This feature was funded by [Kanton Zug, GIS-Fachstelle](http://geo.zg.ch/)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch/)
### 機能：タブとグループボックスの条件付き可視性
これにより、タブとグループボックスをドラッグアンドドロップデザイナーフォームで条件付きで表示または非表示にするための新しい設定オプションが追加されました。

設定は、フィールドコンフィグレーションインターフェイスのデザイナツリーでダブルクリックして行います。

可視性を制御する式を入力できます。この式は、フォームの変更時に毎回値が再評価され、それに応じて表示/非表示のタブまたはグループボックスが再評価されます。

![image49](images/entries/8adda1d639ba9b46b15f8a70b38c6cfd407d2515.png.400x300_q85_crop.webp)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch/)
### 機能：クライアント側のデフォルトのフィールド値
Allows an expression to be set for a vector layer field which is used to evaluate a default value for this field. Default value expressions can utilise properties of the feature which exist at the time of calling, such as digitized geometries. Expression variables can also be used in default value expressions, making it easy to eg insert a user\'s name, the current datetime, project path, etc.

![image50](images/entries/49a9d8a5c38f04d96cf37ad190a97dd4dc4b5025.png.400x300_q85_crop.webp)

この機能は、DB Fahrwegdienste GmbH によって資金提供されました

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## マップコンポーザー
### 機能：真北矢印
QGIS 2.18 adds support for orienting north arrows in the composer to True North. Previously all arrows were aligned to grid north, which is unsuitable for polar regions or non-north up projections (such as some South African projection systems). Now, you can choose to orient arrows to either grid north or true north. There\'s also an optional offset angle, which can be used to specify a grid convergence to make your arrows orient to magnetic north!

![image51](images/entries/b36b83066c2361e4a9647ee830b55b01a04ce4c5.png.400x300_q85_crop.webp)

This feature was funded by [Norwegian Polar Institute\'s Quantarctica project](http://quantarctica.npolar.no)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## プロセシング
### 機能：表面上のポイントアルゴリズム
This new algorithm is similar to the centroids algorithm, but where a centroid may fall outside its corresponding feature the \'Point on surface\' algorithm is guaranteed to create a point which is inside the corresponding polygon feature (or touching the corresponding line feature for line layers).

![image52](images/entries/133a854441e2ade7bec91a48e9a1f1d4b1d012ac.png.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### 機能：処理ディゾルブアルゴリズムは複数のフィールドを受け入れます
ディゾルブアルゴリズムでは、複数のフィールド値に基づいてディゾルブできるようになりました。以前のQGISのバージョンでは、ディゾルブは地物を単一のフィールド値でグループ化することしかできませんでした。

![image53](images/entries/a75b372f431c98592bdaccbc0bf4e90654969fa2.PNG.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### 機能：最適化処理クリップアルゴリズム
処理クリップアルゴリズムは、一般的な使用シナリオに対して最適化されており、結果としてクリッピング操作のスピードアップが大幅に向上しました。例えば：

**2つのポリゴンに対して100万行の道路レイヤをクリッピングする**

| **Earlier versions:** 5 mins 30 seconds | **QGIS 2.18:** 10 seconds

**2つのポリゴンに対して500万ポイントのアドレスレイヤをクリッピングする**

| **Earlier versions:** 50 minutes | **QGIS 2.18:** 30 seconds

![image54](images/entries/f975cb641b319e952264dc1e706deafdfd2b7496.png.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### 機能：バウンディングボックスアルゴリズム
この新しいアルゴリズムは、入力レイヤーの各地物のバウンディングボックス（エンベロープ）を計算します。

![image55](images/entries/398557f0cfe897a227fea70ceef700f9ab048e2d.png.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### 機能：連結線アルゴリズムをマージする
このアルゴリズムは、MultiLineStringジオメトリのすべての接続部分を単一のLineStringジオメトリに結合します。入力されたMultiLineStringジオメトリのいずれかの部分が接続されていない場合、合成ジオメトリは、マージ可能な線や接続されていない線部分を含むMultiLineStringになります。

![image56](images/entries/7ebf10a71a1c3f28d48a2c19f7ad1f08ca75bf80.PNG.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### 機能：幾何境界アルゴリズム
この新しいアルゴリズムは、入力ジオメトリ（すなわちジオメトリのトポロジカル境界）のコンビナトリアル境界のクロージャを返します。たとえば、ポリゴンジオメトリにはポリゴンの各リングの線ストリングで構成される境界があり、線のジオメトリには線の開始点と終了点からなる境界があります。このアルゴリズムはポリゴンまたはラインレイヤーにのみ有効です。

![image57](images/entries/907b7b5c36af36547f10f33f65e9655a5cbe5a67.png.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## データプロバイダ
### 機能：XYZタイルレイヤーのネイティブサポート
XYZ形式のラスタータイルがWMSデータプロバイダ内でネイティブにサポートされ、QuickMapServicesやOpenLayersなどのサードパーティのプラグインを使用しなくても、他のソースからのベースマップを表示できます。

To add connections to XYZ layers, just open browser dock widget, look for item called \"Tile Server (XYZ)\" and right click it to get a popup menu with \"New connection\" action. You will be asked for URL, in which `{x}`, `{y}`, `{z}` will be replaced by the actual tile numbers according to the current map view. For example, to add OpenStreetMap base map, one may use this URL: `http://c.tile.openstreetmap.org/{z}/{x}/{y}.png`

The data provider also supports encoding of XYZ tile numbers into \"quadkeys\" used by Bing. Simply use `{q}` instead of `{x}`, `{y}` and `{z}` in the URL.

![image61](images/entries/f69a3601e9201e38f9a561d40807512035da2298.gif)

This feature was funded by [Lutra Consulting](http://www.lutraconsulting.co.uk/)

This feature was developed by [Martin Dobias (Lutra Consulting)](http://www.lutraconsulting.co.uk/)
## QGISサーバー
### 機能：サーバ内の地物情報ジオメトリをセグメント化する可能性
Necessary for geometries that contain curves (CircularArc, CompoundCurve, CurvePolygon), but the web client (e.g. QGIS Web Client) can\'t handle the display of these geometry types.

This feature can be enabled in the \"OWS server\" tab in the \"Project Properties\" dialogue.

![image62](images/entries/f4b9cf3ba10669b933eb3f3a5c401f675ad76533.png.400x300_q85_crop.webp)

この機能はAndreas Neumannによって資金提供されました

This feature was developed by [Marco Hugentobler (Sourcepole)](http://www.sourcepole.ch/)
## プラグイン
### 機能：DBマネージャー：SQLレイヤーを更新する機能を追加する
With this feature the user can update the layer datasource if it\'s based on an SQL request.

This feature was funded by [Ifremer](http://wwz.ifremer.fr)

This feature was developed by [3Liz](http://3liz.com)
## プログラマビリティ
### 機能：GEOS線形参照関数をQgsGeometryに公開する
A new function `QgsGeometry::lineLocatePoint()` has been added for retrieving the distance along a linestring to the nearest position on the linestring to a given point.

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## 機能：2.18の新しいPyQGISクラス
### 新しいコアクラス
- [QgsAnnotation](https://qgis.org/api/classQgsAnnotation.html) - an interface for annotation items which are drawn over a map
- [QgsFeedback](https://qgis.org/api/classQgsFeedback.html) - a base class for feedback objects to be used for cancellation of something running in a worker thread
- [QgsOptionalExpression](https://qgis.org/api/classQgsOptionalExpression.html) - an expression with an additional enabled flag

### 新しいGUIクラス、再利用可能なウィジェット
- [QgsExpressionLineEdit](https://qgis.org/api/classQgsExpressionLineEdit.html) - includes a line edit for entering expressions together with a button to open the expression creation dialog. This widget is designed for use in contexts where no layer fields are available for use in an expression and space is constrained.
- [QgsTabWidget](https://qgis.org/api/classQgsTabWidget.html) - similar to QTabWidget but with additional methods to temporarily hide/show tabs

## 機能：新しい式の関数
QGIS 2.18には、角度/距離補間の関数を含むいくつかの新しい式関数が追加されています。
- `line_merge`: merges a MultiLineString geometry into connected LineStrings
- `boundary`: returns a geometry\'s topological boundary, ie for polygons this is a MultiLineString representing the polygon\'s rings
- `angle_at_vertex`: returns the average (bisector) angle to a geometry at a specified vertex index
- `distance_to_vertex`: returns distance along geometry to a specified vertex index
- `line_interpolate_angle`: calculates the angle parallel to a geometry at the specified distance along the geometry
- `line_interpolate_point`: returns a point on line at distance
- `line_locate_point`: returns distance along line to nearest line location closest to specified point

この機能はAndreas Neumannによって資金提供されました

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)

{{<content-end >}}
