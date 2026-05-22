---
HasBanner: false
draft: false
releaseDate: '2019-02-22'
section: project
sidebar: true
title: QGIS 3.6 の変更履歴
type: visual-changelog

---
{{<content-start >}}
# QGIS 3.6 の変更履歴{#changelog36 }
![image1](images/projects/f335c2ee37b714ad6eec143246d947f09a5ff2f1.png)

Release date: 2019-02-22

今までで最も偉大なQGISリリースです! QGIS3.6では新しい変更点の莫大なリストがあります-そのハイライトについてはここで解説します。 QGISはオープンソースプロジェクトです。可能であれば、寄付、スポンサーシップ、またはコードドキュメントへの寄付、Webサイトなどを通じて私たちの仕事を支援することを検討してください。

ありがとうございます

私たちは開発者、文書作成者、テスターなどの時間や労力を提供してくれる数多くのボランティアの皆さん（また資金を提供してくれる方々）に感謝します。 QGIS コミュニティとして、このリリースを楽しんでいただきたいと思います。もし時間やお金を寄付したいと考えている場合や、 QGIS をもっと素晴らしいものにすることに参加したい場合は、 qgis.org を見て回って手を貸して下さい。

QGISは寄付者やスポンサーの支援を受けています。プロジェクトに多額の資金拠出を行った寄付者の現在のリストは寄付者リストをご覧ください。公式プロジェクトスポンサーになりたい場合、詳細はスポンサーシップのページをご覧ください。QGISへの出資は、半年毎の開発者会議に資金提供したり、プロジェクトインフラストラクチャを維持したり、バグ修正の取り組みに資金提供するのに役立ちます。現在のスポンサーの完全なリストは以下に掲載します。すべてのスポンサーの皆様に大変感謝しております！

{{<fund type="active" >}}

QGIS はフリーのソフトウェアです。利用する上で金銭を支払う義務はありません。実際、私たちは利用者の財政状況や社会的地位にかかわらず、より多くの人に QGIS を利用して欲しいと思っています。私たちは地理空間的な意思決定ツールによって人々が力を持つことが、全人類の社会をより良くすると信じています。

{{<table-of-contents >}}
## ツール
### タイトルラベルの装飾
新しい装飾機能ではマップキャンバス自体にタイトルを追加することができます。装飾機能では背景の色と透過度を設定できます。

![image2](images/entries/400e617d8059eddcd1228f3ce6861d6087f65794.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### 機能: 装飾アイテムの上部/下部での中央揃え
マップキャンバスの著作権表示と今回新規に追加されたタイトルラベルについて、マップの上部または下部の中央に配置することができます。

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### 機能: ノードツールの修正と改善
注：下記の項目はすべてLTRにバックポートされているため、QGIS 3.4.5にも反映されます。
### Select (\"lock\") feature before editing
In QGIS 2.18 you always had to select a feature first before editing it. In QGIS 3 there was no such thing - editing would be done on any feature any time. Now we are making the selection of feature (\"lock\") available again - using **right click**.

以前のQGIS 3バージョンでは、地物を右クリックすると小さなポップアップメニューが表示され、頂点エディタが表示されました。 **今は、地物を右クリックするとすぐに頂点エディタが表示され、他の地物の編集は無効になります。**

When a feature is \"locked\", it can be again unlocked by clicking on it or by clicking on an empty area - this will bring us back to the default mode when multiple features can be edited.

**1つのマウス位置に複数の地物がある場合は、右クリックを繰り返すとそれらがループします** - 右クリックするたびに、異なる地物にロックされます。最後に、すべての地物が提供されると、地物はロックされず、さらに右クリックするとループが再開されます。

The locking is possible when clicking a feature\'s vertex, edge or interior (for polygons).
### 既存の地物に新しい頂点を追加
新しい位置に配置せずに新しい頂点を追加するために **Shift +ダブルクリックを使用することが可能になりました** 。ユーザーが既存のセグメントに追加の頂点を追加したいときに、これは便利なことがあります。
### \"Current layer\" mode is now the default
From the two modes of vertex tool, \"all layers\" used to be the default one. But from the user feedback that seemed like less common case and users prefer to have \"current layer\" as the default.

This feature was funded by [German QGIS user group](http://qgis.de/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### 機能: トリム/エクステンド
多くのソフトウェアとは異なり、このツールを使用すると、（マルチ）ラインと（マルチ）ポリゴンを変更できます。さらに、必ずしも関係するラインの端である必要はなく、ジオメトリの任意のセグメントを修正できます。反面、これは無効なジオメトリにつながる可能性があり、それはユーザーの責任です。

このツールでは、他のセグメントを延長またはトリミングする制限（セグメント）を選択するように求めてきます。ノードツールとは異なり、チェックはそのレイヤーが編集されていることだけを修正するため行われます。

両方のセグメントが3Dの場合、ツールはZを返すためにリミットセグメントに対して内挿を実行します。

トリムの場合は、クリックして短くする部分を選択する必要があります。

This feature was funded by [Mairie de Megève](https://www.megeve.fr/)

この機能は [Loïc Bartoletti (Oslandia)](https://www.oslandia.com) によって開発されました
### 機能:3点からの長方形作成(投影されたデータ)
四角形を最初の点と二番目の点の間の長さとし、二番目の長さは三番目と二番目の点の間の距離に等しい3点で四角形を作る方法はすでにあります。

この新しい方法では、3点で長方形を作成できます。2番目の長さは、点と線分（またはその延長線）に垂直に投影された点の間の距離です。

この機能は [Loïc Bartoletti (Oslandia)](https://www.oslandia.com) によって開発されました
### 機能: メッシュレイヤの識別ツール
識別ツールがメッシュレイヤで機能するようになりました。現在の時刻におけるメッシュのスカラ成分とベクタ成分の値を表示します。

![image3](images/entries/62a172172d717af1b5399af4006db1ee0e82c7f5.png.400x300_q85_crop.webp)

この機能はLutra Consultingによって資金提供されました。

This feature was developed by [Peter Petrik (Lutra Consulting)](https://www.lutraconsulting.co.uk)
## 計算式
### 機能: 新しい関数
- `force_rhr`: forces polygons to follow the right hand rule, in which the area that is bounded by a polygon is to the right of the boundary. In particular, the exterior ring is oriented in a clockwise direction and the interior rings in a counter-clockwise direction.
- `decode_uri`: takes a layer parameter and an optional uri part parameter. It will return details about the data source of the layer. The available details depend on the data provider. If called with only a layer parameter, a map will be returned with all the available information. If the part is also specified, only the value for the requested part will be extracted from the map.
- `path` has been added as an option for the `layer_property` expression function
- `array_sort`: sorts an array of elements
- `nullif`
- sqlite_fetch_and_increment
- `make_rectangle_3points`: Make a rectangle from 3 points. There is two options for make the rectangle by the distance or a projection. Option distance: Second distance is equal to the distance between 2nd and 3rd point. Option projected: Second distance is equal to the distance of the perpendicular projection of the 3rd point on the segment or its extension.
- `make_square`: Creates a square from a diagonal.
- from_json
- to_json

### 機能: マップ配列の要素へのアクセスを簡単にするための角括弧
次の式が使用できるようになります。
- array(1,2,3)\[0\] -\> 1
- array(1,2,3)\[2\] -\> 3
- array(1,2,3)\[-1\] -\> 3 (Python style, negative indices count from end of array)
- array(1,2,3)\[-3\] -\> 1
- map(\'a\',1,\'b\',2)\[\'a\'\] -\> 1
- map(\'a\',1,\'b\',2)\[\'b\'\] -\> 2

本機能はNyall Dawson, Mathieu Pellerinが開発しました。
### 機能: 新しいマップ式変数
- \@map_crs_description: name of the coordinate reference system of the map.
- \@map_crs_acronym: acronym of the coordinate reference system of the map.
- \@map_ellipsoid_acr: acronym of the ellipsoid of the coordinate reference system of the map.
- \@map_crs_proj4: Proj4 definition of the coordinate reference system.
- \@map_crs_wkt: WKT definition of the coordinate reference system.

この機能は Alexis Roy-Lizotte によって開発されました。
### 機能: エラーを検出する新しい try() 関数
新しいtry()関数は式を試し、エラーがなければその値を返します。式がエラーを返す場合は、指定されているときは代替値が返されます。それ以外の場合にはこの関数はnullを返します。

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
## ユーザーインタフェース
### Feature: A new grayscale theme: \"Blend of Gray\"
A brand new UI theme has made its way into QGIS named \"Blend of Gray\". In addition, hundreds of fixes, tweaks, and refinements were applied to the preexisting \"Night Mapping\" theme.

![image4](images/entries/32e743ea5bf84c96b86ea31160b1677b6362eacf.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### 機能: コードエディター/フィールド計算機における複数行の選択と編集
QGISのフィールド計算機とPythonスクリプトエディターで、ctlキーを押したままテキストの複数行ブロックを選択し、同時に編集することができます。

This feature was developed by [Nyall Dawson ()](https://north-road.com)
## シンボロジ
### 機能: .XMLスタイルライブラリの取り扱い方法の改善
ブラウザパネルにQGISスタイルのxmlライブラリが表示され、これらのファイルをQGISウィンドウにドラッグアンドドロップすることもできます。これにより、ユーザーがスタイルライブラリを閲覧したり、ライブラリからQGISインストールにスタイルをインポートしたりできるダイアログが開きます。

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能: ポリゴンシンボルへの右手の法則の適用
This new option, available under the \"Advanced\" button for fill symbols, allows forcing rendered polygons to follow the standard \"right hand rule\" for ring orientation (where exterior ring is clockwise, and interior rings are all counter-clockwise).

向きの修正はレンダリング中にのみ適用され、元の地物ジオメトリは変更されません。

これにより、レンダリングされるデータセットや個々の地物のリングの向きにかかわらず、一貫した外観の塗りつぶしシンボルを作成できます。

この機能は、QGIS User Group Germanyの資金提供によって開発されました。

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### 機能: 外周の内側または外側のみシンプルラインまたはマーカーラインの塗りつぶオプション
This new option is shown whenever a simple line symbol or marker line symbol is used as part of a fill symbol for rendering polygons. The default behavior is to render both interior and exterior rings, but this new setting allows users to set the symbol layer to render only for the exterior ring OR only for interior rings. This allows for symbolisation which wasn\'t directly possible before, such as a marker line with markers for interior rings angled toward the interior of the polygon.

この機能は、QGIS User Group Germanyの資金提供によって開発されました。

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### 機能: ラスターイメージマーカー
新しいラスターイメージマーカーシンボルタイプがQGISに追加され、ユーザーはラスター、つまりビットマップイメージファイルを使用してマーカーとして表示できます。ラスターイメージマーカーシンボルにより、幅、高さ、イメージ比、回転、および不透明度をカスタマイズできます。

データ定義の画像ソースを使用することで、この新しいシンボルは、地理参照画像を地図キャンバスに表示するための優れた方法になります。

![image5](images/entries/511ac83d3b841be6ae81db5f5d0f319e07e9656e.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### 機能：ラスター塗りつぶしでリモートURLまたは埋め込み画像に画像を設定できます
SVGやラスタ画像マーカーと同様に、ラスタ塗りつぶしはHTTPのURLを使用するように設定したり、ファイルをシンボル自体の内部に直接埋め込むことができます。

この機能はMathieu Pellerinによって開発されました
### 分類されたレンダリングでの代表値の使用
When a field is configured with a value relation, value map or other \"representable value\" and the field is used as the source for a classification renderer, the represented values will be taken to label the categories.

この機能はMatthias Kuhnによって開発されました
### 機能: 分類レンダラでカテゴリをマージするオプション
この変更により、ユーザーは既存の複数のカテゴリーを選択し、それらを単一のカテゴリーにグループ化できます。これは、選択からの任意の値に適用されます。

これにより、多数のカテゴリを持つレイヤをより簡単にスタイル設定できます。この場合、多数の異なるカテゴリを複数の値に適用される、より小さく、管理しやすいカテゴリにまとめることができます。

このオプションは、複数のカテゴリが選択されているときはいつでも、カテゴリリストビューの右クリックコンテキストメニューから利用できます。

![image6](images/entries/159eb5270ab436adbbddba1c92799d8621a0b8e5.png.400x300_q85_crop.webp)

This feature was funded by [SMEC/SJ](http://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能: 
This adds a new \"Project Colors\" section in data defined buttons which are linked to a color value. The color menu contains all colors defined as part of the current project\'s Project Color Scheme (which is defined through project properties).

ボタンからプロジェクトの色を選択すると、プロパティはその色にリンクされます。プロジェクトのプロパティを介して行われると、それは自動的に将来の色の変更に従います。

This allows users to define common colors for a project once, and then \"bind\" symbol, label, layout, etc colors to these preset colors. The link is live, so you change it once, and the change is reflected EVERYWHERE. Sure beats updating a color 100 times when it\'s use has been scattered throughout a project\'s symbols, labels, etc\...

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能: スタイルマネージャーダイアログの改善
スタイルマネージャーダイアログでは多くの改善が施されました。
- A new \"list view\" mode has been added
- An \"all\" tab has been added, which shows all matching symbols (regardless of the symbol type)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能: ラスタースタイルのSLDエクスポート
QGIS is now able to export raster styling to sld, for example to be used in Geoserver. See: <https://docs.geoserver.org/latest/en/user/styling/qgis/index.html#exporting-raster-symbology>

![image7](images/entries/7ab383dfaa0a0dbc9651168a56f44e2275b8c2df.png.400x300_q85_crop.webp)

この機能はOSGeo UK, GeoServer PSC, Brad Hardsの資金提供を受けています。

This feature was developed by [Luigi Pirelli and GeoSolutions](https://www.geo-solutions.it/)
## デジタイズ
### 機能: ジオリファレンサの機能強化
- GCPポイントにdX, dYと残差を追加
- GCPポイントをラスタ修正パスに自動的に保存するオプションを追加

![image8](images/entries/2d6278e2e65be30ceb12ff30f26d34dae6196e42.png.400x300_q85_crop.webp)

This feature was developed by [Faneva Andriamiadantsoa](https://github.com/Fanevanjanahary)
### 機能: ポイント追加の時にジオリファレンサが最小化するのを避ける新しいオプション
ユーザは、マップキャンバスから新しいコントロールポイントを追加するときに発生する自動ジオリファレンスウィンドウの最小化を避けることができます。この動作は、ポイントを追加しながら両方のウィンドウを表示させることが望ましい場合があるマルチモニタ設定では厄介です。

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## データ管理
### 機能: データベースマネージャのコメントオプション
This feature was developed by [Corentin Falcone (SIRS)](https://www.sirs-fr.com/sirs/fr/)
## フォームとウィジェット
### 機能: バイナリ (BLOB) フィールドの新しいフォームウィジェット
このウィジェットはバイナリフィールドでのみ利用可能です（そしてこれはバイナリフィールドに使用されるデフォルトウィジェットです）。BLOBフィールドが空かどうかを示すラベルを表示し、空でない場合はコンテンツサイズ（バイト/ kb / etc単位）を示します。

ドロップダウンメニューボタンを使用すると、ユーザーはフィールドの現在のバイナリコンテンツをディスクベースのファイルに保存したり、BLOBフィールドのコンテンツを消去したり、システムからファイルを選択してバイナリコンテンツを埋め込むことができます。

This feature was funded by [SMEC/SJ](http://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## マップコンポーザー
### 機能: グリッドフレームの改善
Users can now set a margin for the grid frames in layout map items. Additionally, new \"Zebra (Nautical)\" and \"Line border (Nautical)\" frame styles have been added, which show nautical-style blocks in the grid corners when a margin is set for the grid.

この機能はkonstによって開発されました
### 機能: 文字とラベルのエクスポート処理の改善
印刷レイアウトをPDFまたはSVG形式にエクスポートするときに、そのレイアウト内のテキストとラベルをどのようにエクスポートするかをユーザーが選択できるようになりました。使用可能なオプションは、すべてのテキストをアウトライン/曲線に変換するか（以前のデフォルト）、テキストとラベルをテキストオブジェクトのままにすることです。

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能: マップのラベル機能の改善
レイアウト地図項目内のラベルのレンダリング方法に関して、いくつかの改善が行われました。
- A new setting allows per-map control of how close labels are permitted to be placed to the map item\'s edges. Sizes can be set using mm/inches/pixels/etc, and data defined label margins are allowed.
- 新しい設定により、部分ラベルをマップに表示するかどうかをマップごとに制御できます。レイアウトは常に最高品質のカートグラフィック出力を生成する設定にする必要があるため、これはデフォルトではオフになります（新しいプロジェクトではデフォルトでtrueになるキャンバス設定とは異なります）。

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能: 地図アイテムの範囲/縮尺のショートカットの改訂
現在の地図ビューと一致するようにレイアウト地図アイテムを設定するためのボタン（およびその逆）が、地図アイテムプロパティウィンドウの新しいツールバーに移動されました。

New actions have also been added to set the map item\'s scale to match the main canvas scale, and to set the main canvas scale to match the selected layout map\'s scale. These mirror the existing settings for setting the extent from the canvas and pushing the extent TO the canvas.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Layout items can \"block\" map labels
This feature allows other layout items (such as scalebars, north arrows, inset maps, etc) to be marked as \"blockers\" for the map labels in a map item. This prevents any map labels from being placed under those items - causing the labeling engine to either try alternative placement for these labels (or discarding them altogether).

This allows for more cartographically pleasing maps \-- placing labels under other items can make them hard to read, yet without this new setting it\'s non-trivial to get QGIS to avoid placing the labels in these obscured areas.

The blocking items are set through a map item\'s properties, under the label settings panel. The setting is per-map item, so you can have a scalebar block the labels for one map in your layout and not others (if you so desire!)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能: エクスポートでの警告
印刷レイアウトをエクスポートするとき、QGISは自動的に一般的な間違いがないかどうかレイアウトをチェックし、見つかったときにユーザーに警告します。
- 地図アイテムにリンクされていないスケールバー
- パスが壊れているか見つからない、または判読できない画像ファイルにリンクされている画像アイテム
- 地図の概要が有効な地図アイテムにリンクされなくなりました

This feature was funded by [SMEC/SJ](http://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能: 地図オーバビュー範囲の上下位置の制御
QGIS allows overview extents to be drawn below map labels (the new default), but in 3.6 choices have been added for drawing them below all map layers, or above/below a specific map layer. This allows users to control exactly where in the map item\'s layer stack the overview will be placed, e.g. allowing them to draw a overview extent below some feature layers such as roads whilst drawing it above other background layers.

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能: 凡例アイテム用の新しい数式変数
次のような、レイアウトの凡例項目のデータ定義式で使用するための新しい式変数が追加されました。
- \@legend_title
- \@legend_column_count
- \@legend_split_layers
- \@legend_wrap_string
- \@legend_filter_by_map
- \@legend_filter_out_atlas

If the legend is linked to a map, then expressions used in that legend will also have access to the linked variables, including \@map_scale, \@map_extent, etc.

さらに、凡例の一部としてレンダリングされたシンボルは、凡例に使用可能な完全な表現コンテキストを使用するようになりました。これは、シンボルが現在の地図帳地物のような変数にアクセスできることを意味します。

この機能は Alexis Roy-Lizotte によって開発されました。
### 機能: 凡例アイテムのテキスト内の数式
This feature allows for expressions to be embedded directly inside legend item text (e.g. group, subgroup and item text). The expressions are evaluated at render time, with full knowledge of the legend\'s expression context (so can utilise variables from the layout/layout item/etc)

There\'s no UI for this yet (that will come in 3.8), but expressions are entered using the standard \[% 1 + 2 %\] format.

例えば次のような文字列があったとします。

    My layer (rendered at 1:[% @map_scale %])
    
これは次のように出力されます。

    My layer (rendered at 1:1000)
    
This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## 分析ツール
### 機能: ラスタ計算機のハードウェアアクセサレーション
OpenCLアクセラレーションは、ラスタ計算機の操作でデフォルトで利用可能になりました。

この機能は Alessandro Pasotti - ItOpen によって資金提供されました

This feature was developed by [Alessandro Pasotti](https://www.itopen.it)
### 機能: メッシュ計算機
ラスタ計算機と同様に、メッシュ計算機はメッシュレイヤで動作します。一般的な機能に加えて、メッシュ計算機は時間集約機能も提供します。たとえば、1か月にわたる毎日の気温のnetcdfがある場合、各セルのその月の平均気温を計算できます。出力は、タイムスパンまたは空間的範囲によってフィルタリングできます。

この機能はLutra Consultingによって資金提供されました。

This feature was developed by [Peter Petrik (Lutra Consulting)](https://www.lutraconsulting.co.uk)
## プロセシング
### Feature: New algorithm \"Remove duplicates by attribute\"
この機能では入力地物の１つの（あるいは複数の）フィールドにおいて属性値が重複する地物を削除します。オプションとして削除された（重複していた）地物を別途、保存する機能があります。

![image9](images/entries/ae0544826b7d16479b2e48ba97f1f530c80bbd42.png.400x300_q85_crop.webp)

This feature was funded by [SMEC/SJ](http://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能: HStore分割アルゴリズム
This algorithm creates a copy of an input layer and adds a new field for every unique key found in a HStore type field. For instance, a HStore field is often present in an OSM dataset (\"other_tags\").

![image10](images/entries/304c29f7cc6d26aa823001b67a46744deec3c2dd.png.400x300_q85_crop.webp)

This feature was developed by [Etienne Trimaille](https://github.com/Gustry)
### 機能: 右手ルールの強制
この新しいアルゴリズムは、ポリゴンのジオメトリに右手ルールを強制します。右手ルールとは、ポリゴンの境界線の右手側が必ず内側になることで、外側の輪郭線は時計回りに描かれ、ポリゴンの穴の輪郭線は反時計回りに描かれます。（シェープファイルなどは右手ルールです）

![image11](images/entries/16db7b4b5931c9d96eba053701641defc6f52290.png.400x300_q85_crop.webp)

この機能は、QGIS User Group Germanyの資金提供によって開発されました。

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能: バイナリフィールド抽出アルゴリズム
この機能で、バイナリフィールドをファイルに抽出でます。

![image12](images/entries/6715290eac02e216394b3f24045da0b982069c7d.png.400x300_q85_crop.webp)

This feature was funded by [SMEC/SJ](http://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能: 最大長による線分割アルゴリズム
このアルゴリズムは入力（複数）ライン（または曲線）レイヤを取り、指定された最大長よりも長い部分がないように各地物を複数の部分に分割します。

データ定義の最大長プロパティをサポートし、インプレース編集操作を行います。

![image13](images/entries/13c8c2fedfa76ff8decbc4d7e6d683d01bab1126.png.400x300_q85_crop.webp)

この機能はNyall Dawson、Nathan Woodrowによって開発されました。
### 機能: 認証設定用の新パラメータ型
処理アルゴリズム用の新しいパラメータタイプQgsProcessingParameterAuthConfigが追加され、利用可能な認証設定からの選択（および新しい設定の作成）が可能になりました。

It allows creation of processing algorithm which can fully take advantage of QGIS\' mature authentication handling, avoiding the need to use insecure string parameters for users to input sensitive logon credentials.

QgsProcessingParameterAuthConfigパラメータは、選択された認証設定IDを返すQgsProcessingAlgorithm.parameterAsString()を使用して評価されます。

This feature was funded by [SMEC/SJ](http://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能: gdaladdoアルゴリズムにおけるリサンプリングとフォーマットのオプション
この機能は Alex Bruy によって開発されました
### 機能: ラスタのゾーン統計アルゴリズム
This algorithm calculates statistics for a raster layer\'s values, categorized by zones defined in another raster layer.

![image14](images/entries/014272dcac2a228f8d8cc7a1587ac9b07865bc1f.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能: Z値とM値の抽出アルゴリズム
これらのアルゴリズムを使用すると、地物のジオメトリに存在するz値またはm値をレイヤ内の属性に変換できます。

デフォルトでは地物の最初の頂点からのz / m値が抽出されますが、オプションとして、ジオメトリからのすべてのz / m値について統計を計算できます（例：z値の平均/最小/最大/合計など）。

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能: 180度子午線での測地線分割
このアルゴリズムは、線分が子午線を横切るとき（経度±180度）に、線を複数の測地線分に分割します。反子午線で分割すると、投影図の線を視覚的に表示するのに役立ちます。返されるジオメトリは常にマルチパートジオメトリになります。

このアルゴリズムは、日付変更線（東経180度線＝西経180度線）をまたぐ場合、測地線を複数のセグメントに分割します。
これによって、ある種の投影法を使うと表示が乱れることを防ぐことができます。生成されるジオメトリは常にマルチパートです。

入力レイヤの線のジオメトリが日付変更線をまたぐ場合、回転楕円体上で測地線と日付変更線が交差する点で２つのセグメントに分割します。回転楕円体はプロジェクトの設定が使われます。

ジオメトリがZ値、M値を含む場合、切断点で線形内挿（補間）されます。

入力ジオメトリにMまたはZの値が含まれている場合、これらは逆子午線で作成された新しい頂点に対して線形補間されます。

"その場で編集" モードにも対応しています。

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Geodesic mode for \"Join by Lines (Hub lines)\" algorithm
これにより、希望するなら測地線の生成が可能になります。測地線は、回転楕円体上におけるポイント間の最短距離を表現する線です。

測地線モードを使用すると、作成した線分を逆子午線（経度±180度）で分割できます。これにより、線分のレンダリングが向上します。さらに、頂点間の距離も指定できます。距離が短いほど、線が密で正確になります。

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Raster Surface Volume algorithm
SAGAラスタサーフェスボリュームは、ネイティブのQGISアルゴリズムに移植されました。このアルゴリズムのSAGAバージョンは、計算された量がSAGA端末出力にのみ埋め込まれるため、QGISでの使用には制限があります。これにより、ファイルがファイルに保存されたり、モデル内で後のモデルステップへの入力として再利用されたりするのを妨げます。したがって、このアルゴリズムはネイティブのQGIS c ++アルゴリズムに移植されています。このアルゴリズムはSAGAアルゴリズム1：1を複製しますが、体積（および面積）をHTMLレポートまたはベクタテーブルのいずれかに出力します。さらに、出力はアルゴリズムから数値出力としてエクスポートされるため、モデル内で再利用できます。

![image15](images/entries/e0a8089ec0653cf5628636354ec80ef317e68565.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Resurrected model to Python script functionality
Processingモデルを同等のPythonスクリプトに直接変換する2.xの機能が復活し、3.x Processing API用に更新されました。

![image16](images/entries/42b342e04b54d5e106ba1051b210d83af8712dd8.png.400x300_q85_crop.webp)

This feature was funded by [Solspec](http://solspec.io)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## アプリケーションとプロジェクトのオプション
### 機能: オプションの詳細タブから設定を削除
This change adds a new right click menu to the settings shown in the \"Advanced\" tab in the settings dialog, which allows users to remove that setting (or group of settings).

![image17](images/entries/6b012542ef9ca282ba6f9087758f85d818dd5ec9.png.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## ブラウザ
### Feature: Add \"export to file\" options for raster and vector layers within the browser
実際にそれらを最初にプロジェクトにロードする必要なしに、これらのファイルを（例えば、異なるフォーマット、crsなどに）直接エクスポートすることを可能にします。

![image18](images/entries/d939594c84d7aa186fe5f18f46ed7ad0c89d8c67.png.400x300_q85_crop.webp)

This feature was funded by [Nyall Dawson (North Road)](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能: ネイティブのファイル／フォルダプロパティ
You can now right click on a file or folder within the browser, and select \"File Properties\" or \"Directory Properties\" to open the native file/folder properties dialog for that entry. This allows rapid access to operating system file or folder properties, such as file permissions and sharing options.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能: レイヤと属性をプレビュー
QGIS 3.6 brings back the functionality from the old 2.18 standalone \"browser\" application to preview layers and their attributes. This functionality has been moved to the inbuilt browser panel, and is available by right-clicking on a layer and selecting \"properties\" (or by clicking the \"enable properties widget\" button in the browser toolbar).

![image19](images/entries/5058aa9a701e417271b0cbf0869669177a7f0fe4.png.400x300_q85_crop.webp)

This feature was funded by [SMEC/SJ](http://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能: ブラウザでQGS/QGZプロジェクトを探索
以前のバージョンのQGISでは、QGS / QGZプロジェクトファイルがブラウザに表示され、新しいアクティブプロジェクトとして開くことができました。QGIS 3.6では、この機能が拡張され、プロジェクトファイルをブラウザ内で直接探索できるようになりました。プロジェクトは拡張可能な項目になり、それらを拡張するとグループとレイヤの完全なプロジェクト構造が表示されます。その後、任意のレイヤを現在のプロジェクトにドラッグアンドドロップできます。

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能: Geopackageとシェープファイルを直接生成
Right clicking a directory in the browser panel now shows a \"New\" menu, containing items for creating a new Geopackage, Shapefile, or subdirectory under the selected directory.

![image20](images/entries/2bc8475b95a8413285b3c88a9a070f02f43cf5b9.png.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能: パスでターミナルを開く
そのディレクトリで新しい端末ウィンドウを開くために、ブラウザパネルのディレクトリ項目に新しいコンテキストメニューエントリが追加されました。

Windowsでは、この新しい端末はQGIS環境を継承しているので、PyQGISコマンドを使用するGDALコマンドとPythonスクリプトは、それ以上の環境設定を必要とせずに機能します。

ターミナルハッカーは喜びます！

![image21](images/entries/623ef55ae3918f72faa7ec796bbac01bf5063464.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## 一般情報
### Feature: Improved \"missing layer\" handling on project load
![image22](images/entries/8e3fbce280478d8e88cab7e24b489b783c83fc13.png.400x300_q85_crop.webp)

This feature was funded by [A.R.P.A. Piemonte](http://www.arpa.piemonte.it/)

This feature was developed by [Alessandro Pasotti](http://www.itopen.it)
### 機能：バージョンチェックの設定
A new setting, \"allowVersionCheck\" has been added to the QGIS configuration ini file. If set to true (the default), users may control whether the version check is enabled or disabled through the QGIS settings dialog. When this setting is set to false, no version checking will be performed AND users will NOT have an option to enable this check in the settings dialog.

この設定は、QGISバージョン管理が一元管理されているエンタープライズインストールでの使用を目的としています。

This feature was funded by [SMEC/SJ](http://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能: ベクタレイヤの凡例アイテムにトグル動作を追加
![image23](images/entries/f3b822b5591367b7d246fbdd5173763a1633b9ec.png.400x300_q85_crop.webp)

This feature was funded by [A.R.P.A. Piemonte](http://www.arpa.piemonte.it)

This feature was developed by [Alessandro Pasotti](https://www.itopen.it)
## データプロバイダ
### 機能: ArcGISフィーチャサーバーレイヤのサービス情報を開く
ArcGIS Feature Serverレイヤのブラウザパネルに新しい右クリックメニューオプションがあり、ユーザは選択したレイヤのサービス情報Webページを直接開くことができます。

This feature was funded by [SMEC/SJ](http://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Binary blob support for OGR providers
バイナリフィールドを切り捨てられた文字列に変換する代わりに、これらの値は元のバイナリコンテンツとして取得できるようになりました。これにより、プラグインやスクリプトは、その内容の抽出など、バイナリフィールドを利用することができます。

Additionally, new binary fields can be created for compatible data sources.

This feature was funded by [SMEC/SJ](http://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: ArcGIS Feature Server picture marker and picture fill support
画像マーカーまたは画像塗りつぶしシンボルを使用してFeature Serverレイヤーをロードすると、QGISは自動的にESRI画像マーカーと塗りつぶしシンボルを変換し、それらをレイヤーのデフォルトスタイルとして使用します。

This feature was funded by [SMEC/SJ](http://www.smec.com/en_au)

本機能はNyall Dawson, Mathieu Pellerinが開発しました。
### Feature: ArcGIS Feature Server labeling support
Feature Serverレイヤーにサーバーによって定義されたラベル付けがある場合、これらのラベル付け設定は、レイヤーをQGISにロードするときにデフォルトで自動的に使用されます。

この機能はMathieu Pellerinによって開発されました
### Feature: Boolean and binary field support for memory layers
Memory (\"Temporary scratch\") layers can now use binary and boolean (true/false) field types.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: JSON Support for GeoPackage
Support for JSON allows to store structured data inside a single field in GeoPackage files.

JSONとして保存されたデータは、以下で表現および編集できます：
- ValueRelation widgets with allow multiple selection activated
- KeyValue widgets
- List widgets
- or the [QML widget which also supports visualizing JSON data](https://www.opengis.ch/2018/11/13/visualize-postgres-json-data-in-qml-widgets/)

This feature was funded by [Kanton Zug, Amt für Geoinformation](https://geo.zg.ch/)

This feature was developed by David Signer (OPENGIS.ch)
### Feature: Postgres provider: save primary key selection
When a view loaded from Data Source Managers\'s PostgreSQL tab you can select the key columns of the view (by default the first column is used, which can be wrong). This commit stores that selection in the settings, so that it doesn\'t have to be reselected on subsequent loads. This stored selection is also used when adding the loading from the browser.

この機能はJürgenFischerによって開発されました
### Feature: ArcGIS Feature Server multi-field unique value support
QGIS can now display a Feature Server layer with a multi-fiend unique value renderer setup.

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
## QGISサーバー
### Feature: Possibility to set ATLAS_PK in GetPrint request to print atlas sheet(s)
The new GetPrint parameter accepts the primary key(s) for which atlas sheets should be printed, separated by comma,

Such a request would look like:

    https://yourserver.name/path/to/qgisproject?SERVICE=WMS&REQUEST=GetPrint
    &TEMPLATE=A4&FORMAT=pdf&ATLAS_PK=1,3,7
    
One can also provide an asterisk (\*) for ATLAS_PK to request all features of an atlas. To protect the server against requesting too many features, it is possible to restrict it to a defined maximum of features that can be requested at one time (see attached screenshot).

どのテンプレートに地図帳があり、どの属性がカバレッジレイヤの主キーであるかクライアントにはわからないので、この新しい機能はこの情報をWMSサービスのGetProjectSettingsレスポンスにも追加します。

![image24](images/entries/6a4648e447531099dfd8d5e113c2a79c8420df06.png.400x300_q85_crop.webp)

This feature was funded by [Kanton Zug, Amt für Geoinformation](https://geo.zg.ch/)

この機能はMarco Hugentoblerによって開発されました
### Feature: WMTS tile matrices configuration
QGISサーバー3.4では、EPSG：3857とEPSG：4326を除いてタイルマトリックスが計算されるWMTS APIが追加されました。

この変更により、プロジェクトで使用するタイルマトリックスを選択し、タイルマトリックスの左上隅と最後のレベルを設定する機能が追加されました。EPSG：3857およびEPSG：4326の場合、ユーザーはタイルマトリックスの最後のレベルのみを選択できます。

この機能は Ifremer によって資金提供されました

この機能は 3liz によって開発されました
### 機能: WMS GetFeatureInfoリクエストにJSON形式を追加
Thanks to this new feature, the FORMAT parameter of GetFeatureInfo for the WMS service may take \'application/json\' or \'application/geo+json\' values. In this case, the document returned by the server looks something like this:

    {"type": "FeatureCollection",
        "features":[
        {
           "type":"Feature",
           "id":"testlayer",
           "geometry":
           {"type": "Point", "coordinates": [913204.9128, 5606011.4565]},
           "properties":{
               "id":3,
               "name":"three",
               "utf8nameè":"three"
           }
        }]
    }
    
This feature was funded by [Veolia](https://www.veolia.com)

This feature was developed by [Paul Blottiere (Oslandia)](http://oslandia.com/)
## プラグイン
### 機能:DBマネージャ:外部SQLファイルの読み込みと保存ボタンの追加
このボタンでは外部SQLファイルのクエリーの読み込みと保存ができます。

![image25](images/entries/7d8fbe3054bd3d8b311d26d9343a20041f3fb809.png.400x300_q85_crop.webp)

この機能は [Loïc Bartoletti (Oslandia)](https://www.oslandia.com) によって開発されました
## プログラム可能
### 機能: 新クラス QgsExifTools
Contains utilities for retrieving the geotag from images and for setting an image\'s geotag.

（このクラスより前の）ジオタグを扱うのは非常に面倒で手間がかかり、コマンドラインツールの解析またはどこにもない標準的でないPythonライブラリに依存しているため、特定のプラットフォームのユーザにとってインストールして正常に動作させるのが非常に困難です。

このクラスを使えば、普遍的なジオタグ取得/設定のための安定したメソッドがあり、プラグインやスクリプトで安全に使用することができます。

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能: QgsGeometryの単一パートに対する反復
This new PyQGIS API allows easy iteration over all the parts of a geometry, regardless of the geometry\'s type. E.g.

    geometry = QgsGeometry.fromWkt( 'MultiPoint( 0 0, 1 1, 2 2)' )
    for part in geometry.parts():
      print(part.asWkt())
    
    geometry = QgsGeometry.fromWkt( 'LineString( 0 0, 10 10 )' )
    for part in geometry.parts():
      print(part.asWkt())
    
利用可能なイテレータは2つあります。 QgsGeometry.parts() は、constでないイテレータを提供し、その部分をその場で修正することを可能にします：

    geometry = QgsGeometry.fromWkt( 'MultiPoint( 0 0, 1 1, 2 2)' )
    for part in geometry.parts():
       part.transform(ct)
    
For a const iteration, calling .const_parts() gives a const iterator, which cannot edit the parts but avoids a potentially expensive QgsGeometry detach and clone

    geometry = QgsGeometry.fromWkt( 'MultiPoint( 0 0, 1 1, 2 2)' )
    for part in geometry.const_parts():
       print(part.x())
    
This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能: QgsLineString PyQGIS APIの機能向上
QgsLineString API に機能が追加されました。
- len(QgsCurve) は曲線における点の数を返します。
- pointN, xAt, yAt, zAt, mAt, setXAt, setYAt, setMAt, setZAt が不正な頂点インデックスの時、IndexErrors を返すようになりました。
- Add \[\] getter for retrieving specific vertices, eg. ls\[0\] returns QgsPoint(\...)
- Add \[\] setter for setting specific (existing) vertices, e.g. ls\[1\] = QgsPoint(1,2)
- Add del support for removing vertices, e.g. del ls\[1\] removes the second vertex

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: PyQGIS Geometry Collection API improvements
ジオメトリコレクションを扱うためのPyQGIS APIが改良されました：
- Calling removeGeometry with an invalid index will now raise an IndexError
- Calling collection\[0\] will return the first geometry in the collection, collection\[1\] the second, etc. And negative indices return from the end of the collection, so collection\[-1\] returns the last geometry in the collection.
- Geometries can be deleted by calling `del collection[1]` (deletes the second geometry from the collection). Also supports negative indices to count from the end of the collection.

さらに、コレクション内のジオメトリを簡単に繰り返すことができるようになり、次のようなコードが可能になります：

    gc = QgsGeometryCollection()
    gc.fromWkt('GeometryCollection( Point(1 2), Point(11 12), LineString(33 34, 44 45))')
    for part in gc:
      print(part.asWkt())
    
This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Easier Processing algorithm creation via \@alg decorator
カスタムクラスを実装しなくても、次のものが処理スクリプトを定義できるようにします：

from qgis.processing import alg

| \@alg(name=\"test2\", label=\"test 2\", group=\"test\", groupid=\"test\") | \@alg.input(type=alg.STRING, name=\"IN1\", label=\"In string\") | \@alg.input(type=str, name=\"IN2\", label=\"In string 1\", optional=True) | \@alg.input(type=str, name=\"IN3\", label=\"In string 2\") | \@alg.input(type=alg.SINK, name=\"SINK\", label=\"Sink it!\") | \@alg.output(type=str, name=\"OUT\", label=\"WAT\") | \@alg.output(type=alg.MAPLAYER, name=\"OUT2\", label=\"WAT\") | \@alg.output(type=alg.VECTOR_LAYER, name=\"VECTOR_LAYER\", label=\"WAT\") | def testalg(instance, parms, context, feedback, inputs): | \"\"\" | This is a test function that does stuff | \"\"\" | feedback.pushInfo(\"We got these inputs!!\") | feedback.pushInfo(inputs\[\'IN1\'\]) | feedback.pushInfo(inputs\[\'IN2\'\]) | feedback.pushInfo(inputs\[\'IN3\'\]) | return { | \"OUT2\": \"wat\" | }

この機能はNathan Woodrowによって開発されました
### Feature: Blocking (non-async) network requests
SAFEブロックリクエストを実行するための新しいPyQGIS APIが追加されました。これはスレッドセーフで、QGISプロキシと認証設定を完全にサポートしています。

    reply = QgsNetworkAccessManager.blockingGet(...)
    reply = QgsNetworkAccessManager.blockingPut(...)
    
このAPIは、ブロッキングネットワーク要求が必要なときはいつでも使用する必要があります。   QApplication::processEvents() や QEventLoop の作成に依存する実装とは異なり、このクラスは完全にスレッドセーフで、メインスレッドまたはバックグラウンドスレッドのどちらでも問題なく使用できます。

リダイレクトはクラスによって自動的に処理されます。

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Feature: Custom validity checks on layout exports
See <https://north-road.com/2019/01/14/on-custom-layout-checks-in-qgis-3-6-and-how-they-can-do-your-work-for-you/>

This feature was funded by [SMEC/SJ](http://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### 機能: 測地線計算のためのAPI
測地線計算のために成熟したgeographiclibライブラリを利用するQgsDistanceAreaに測地線（楕円上の最短距離）を計算するための新しいPyQGIS APIが追加されました。
- QgsDistanceArea.geodesicLine：2点間の測地線を計算します
- QgsDistanceArea.latitudeGeodesicCrossesAntimeridianは、2点を結ぶ測地線が反経線と交差する緯度を計算します。
- QgsDistanceArea.splitGeometryAtAntimeridian：測地線を使用して反子午線上で分割が行われる正確な点を計算して、（複数の）折れ線を反子午線で分割します。

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### 機能: 新しいクラス QgsQuadrilateral
QgsRectangleは、その役割が範囲に対するものであるため、方向またはZのサポートを提案しません。 4つの頂点ポリゴンを管理するためのQgsQuadrilateralという新しいクラスが作成されます。今のところ、長方形しかありませんが、後で他の形状を追加することも可能です。

This refactoring simplifies maptools and allows you to use the QgsQuadrilateral class in other tools.

さらに、それは3点で長方形のZのより良い管理を可能にします。今日では最初のZが使用され、今度は点がZを持ち、4番目の点が平面上に投影されます。

この機能は [Loïc Bartoletti (Oslandia)](https://www.oslandia.com) によって開発されました
## 三次元機能
### 機能: 地形のシェーディング
地形のレンダリング方法を選択する新しいオプションが追加されました: -シェーディング無効 -  地形の色はマップテクスチャのみで決定されます - シェーディング有効 -  地形の色はPhongシェーディングモデルを使用して決定され、マップテクスチャ、テレインの法線ベクトル、シーンのライト、テレインマテリアルのアンビエント+スペキュラーカラーおよびシャイネスが考慮されます

オプションとして、地形をプリセットのマップテーマを使用してシェーディングすることもできます。

この機能は、 Martin Dobias (Lutra Consulting) によって開発されました
### 機能 3Dマップシーンのライト設定
この機能は、3Dシーンでポイントライトを定義するためのセクションを追加します。最大8つの光がサポートされています（材料の実装による制限）。光ごとに、位置、強度、色、および減衰を設定できます。

この機能は、 Martin Dobias (Lutra Consulting) によって開発されました
### 機能: ルールベース3Dレンダラー
![image26](images/entries/0825fbe986d774f7f2d5a0bdfdbc2487453ef49c.png.400x300_q85_crop.webp)

この機能開発は QGIS community によって資金提供されました

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk)
### 機能: 3Dでのメッシュレイヤー（フェイス）のサポート
この機能により、3Dシーンでメッシュレイヤーを使用することができます。

![image27](images/entries/82a388b33e8fb96df43fb32b9bc5ef013be0459c.jpg.400x300_q85_crop.webp)

この機能はLutra Consultingによって資金提供されました。

This feature was developed by [Peter Petrik (Lutra Consulting)](https://www.lutraconsulting.co.uk)
## 注目すべき修正
### 機能: Alessandro Pasotti によるバグ修正
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| QGIS Server: WFS issue using the EXP_FILTER parameter | [#20927](https://issues.qgis.org/issues/20927) | [PR #8924](https://github.com/qgis/QGIS/pull/8924) | 終了 |
| GetFeatureInfo response empty for child relation table in QGIS Server 3 | [#20801](https://issues.qgis.org/issues/20801) | Cannot reproduce with 3.5 |  |
| QGIS Server WFS DescribeFeatureType not following TYPENAME parameter | [#20198](https://issues.qgis.org/issues/20198) | [PR #8948](https://github.com/qgis/QGIS/pull/8948) | 終了 |
| QGIS Server 3.4 can\'t reset numeric field using WFS Update | [#20961](https://issues.qgis.org/issues/20961) | [PR #8958](https://github.com/qgis/QGIS/pull/8958) | 終了 |
| WFS provider shows numeric NULL fields with 0 instead of NULL | [#20961](https://issues.qgis.org/issues/20961) | [PR #8958](https://github.com/qgis/QGIS/pull/8958) | 終了 |
| OWS project title in project properties cannot be set to blank/empty | 未報告 | [PR #8958](https://github.com/qgis/QGIS/pull/8958) | 終了 |
| Form Value relation based on WFS layer | [#21077](https://issues.qgis.org/issues/21077) | [PR #8970](https://github.com/qgis/QGIS/pull/8970) | 終了 |
| データベーススタイルマネージャダイアログのボタン位置 | [#21068](https://issues.qgis.org/issues/21068) | [PR #8971](https://github.com/qgis/QGIS/pull/8971) | 終了 |
| raster calculator in processing does not work with Aspect raster | [#21011](https://issues.qgis.org/issues/21011) | Cannot reproduce with 3.5 |  |
| Error opening network KML page: Range downloading not supported by this server! | [#21091](https://issues.qgis.org/issues/21091) | [PR #8985](https://github.com/qgis/QGIS/pull/8985) | 終了 |
| Can\'t add a virtual field or update a existing field of a WFS layer using the field calculator | [#21086](https://issues.qgis.org/issues/21086) | [PR #8990](https://github.com/qgis/QGIS/pull/8990) | 終了 |
| Opening shapefiles in ZIP gives Invalid Datasource | [#21097](https://issues.qgis.org/issues/21097) | Cannot reproduce with 3.5 |  |
| spatialite, edit table in dbmanager is broken in master Fault: no such table: pg_description | [#21151](https://issues.qgis.org/issues/21151) | [PR #9086](https://github.com/qgis/QGIS/pull/9086) | N/A |
| Delimitedtext layer saves absolute path when project in relative path mode | [#21150](https://issues.qgis.org/issues/21150) | [PR #9099](https://github.com/qgis/QGIS/pull/9099) | 終了 |
| field calculator doesn\'t load values for gpkg containing blank spaces or n dash (hypen) in field names | [#21100](https://issues.qgis.org/issues/21100) | [PR #9071](https://github.com/qgis/QGIS/pull/9071) | 終了 |
| Can\'t open feature form when when the primary key of Spatialite layer is created in text type | [#21176](https://issues.qgis.org/issues/21176) | [PR \#](https://issues.qgis.org/projects/qgis/repository/revisions/7f61dc495491752fd26c7f3bad56adc1f8950e3f) | No (deferred) |
| Geopackage layer rename in DB Manager does not update f_table_name values in the layer_styles table or the Triggers | [#21227](https://issues.qgis.org/issues/21227) | [PR #9164](https://github.com/qgis/QGIS/pull/9164) | Not possible because it relies on the new rename feature implemented in browser |
| Layer Properties \> Load Style \> From database \> \'Other styles \...\' \> Description column contains Name text, should contain Description text (it is a geopackage layer) | [#21254](https://issues.qgis.org/issues/21254) | [PR #9170](https://github.com/qgis/QGIS/pull/9170) | 終了 |
| Comments in SQL query in DB Manager breaks the query | [#21271](https://issues.qgis.org/issues/21271) | [PR #9180](https://github.com/qgis/QGIS/pull/9180) | N/A |
| Bug with multiple Else items in rule-based style | [#21281](https://issues.qgis.org/issues/21281) | [PR #9181](https://github.com/qgis/QGIS/pull/9181) | 終了 |
| GetFeatureInfo not send Geometry when set into project | [#21172](https://issues.qgis.org/issues/21172) | Cannot reproduce with 3.5 | N/A |
| Geometry Checker Crashes | [#21259](https://issues.qgis.org/issues/21259) | [PR #9191](https://github.com/qgis/QGIS/pull/9191) | 終了 |
| createInstance()がQgsProcessingAlgorithmサブクラスで誤ったコンストラクターを使用するとQGISがクラッシュする | [#21270](https://issues.qgis.org/issues/21270) | [PR #9193](https://github.com/qgis/QGIS/pull/9193) | 終了 |
| pasting features is very slow | [#21305](https://issues.qgis.org/issues/21305) | [PR #9203](https://github.com/qgis/QGIS/pull/9203) | No (deferred) |
| Attribute forms do not show anymore constraints messages | [#21266](https://issues.qgis.org/issues/21266) | いくつかのテストとGiovanni Manghiとの協議の後、無効として閉鎖されました。 | N/A |
| OGR provider returns an empty set for GPKG uniqueValues(0) | [#21311](https://issues.qgis.org/issues/21311) | [PR #9203](https://github.com/qgis/QGIS/pull/9203) | No (deferred) |
| \"default value\" is not applied when pasting features | [#21304](https://issues.qgis.org/issues/21304) | [PR #9203](https://github.com/qgis/QGIS/pull/9203) | No (deferred) |
| Postgis very noticeable slowdown when opening the attributes table if the table has a large number of columns | [#21303](https://issues.qgis.org/issues/21303) | [PR #9219](https://github.com/qgis/QGIS/pull/9219) | No (deferred) |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

This feature was developed by [Alessandro Pasotti](https://www.itopen.it/)
### 機能: Alexander Bruyによるバグ修正
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| gdal buildvrt missing an important param | [#20586](https://issues.qgis.org/issues/20586) | [PR #8927](https://github.com/qgis/QGIS/pull/8927) | [PR #8944](https://github.com/qgis/QGIS/pull/8944) |
| gdal:warpreproject missing old \'extra\' param | [#20721](https://issues.qgis.org/issues/20721) | [PR #8930](https://github.com/qgis/QGIS/pull/8930) | [PR #8944](https://github.com/qgis/QGIS/pull/8944) |
| Points inside polygons | [#20798](https://issues.qgis.org/issues/20798) | Cannot reproduce with 3.5 |  |
| IDW interpolation on csv point layer not working | [#20490](https://issues.qgis.org/issues/20490) | [PR #8942](https://github.com/qgis/QGIS/pull/8942) | [PR #8947](https://github.com/qgis/QGIS/pull/8947) |
| \[Processing\] Field calculator algorithm does not use the selected layer as default layer input | [#19686](https://issues.qgis.org/issues/19686) | [PR #8945](https://github.com/qgis/QGIS/pull/8945) | [PR #8949](https://github.com/qgis/QGIS/pull/8949) |
| v.surf.rst NOT WORKING IN QGIS 3.2.0 BONN | [#19472](https://issues.qgis.org/issues/19472) | [PR #8959](https://github.com/qgis/QGIS/pull/8959) | [Direct commit](https://github.com/qgis/QGIS/commit/c2465fc4a66425c296ffedb491d220a3db8ba453) |
| SVM Classification, SupportVectorMachineClassification(OpenCV)-Vector Field | [#20796](https://issues.qgis.org/issues/20796) | [PR #8960](https://github.com/qgis/QGIS/pull/8960) | [Direct commit](https://github.com/qgis/QGIS/commit/e0a8de477b04a6aa355d934c25ba37257bc63584) |
| GDAL/OGR Dissolve algorithm not properly working with point/multipoint layers | [#20025](https://issues.qgis.org/issues/20025) | [PR #8972](https://github.com/qgis/QGIS/pull/8972) | [PR #8981](https://github.com/qgis/QGIS/pull/8981) |
| Build Virtual Vector tool: file created fails to load correctly | [#14374](https://issues.qgis.org/issues/14374) | Cannot reproduce with 3.5 |  |
| \"Convert map to raster\" algorithm does not export with transparent background despite the option | [#19866](https://issues.qgis.org/issues/19866) | [PR #8965](https://github.com/qgis/QGIS/pull/8965) | [PR #8981](https://github.com/qgis/QGIS/pull/8981) |
| \[GUI\] Disable edit tools when no layer is selected/available nor selected layer is in edit mode | [#18141](https://issues.qgis.org/issues/18141) | [Direct commit](https://github.com/qgis/QGIS/commit/ab3adc663c37b3da589cf6bae56d733fcbc4feb3) | [Direct commit](https://github.com/qgis/QGIS/commit/38051a95afc190d3c65ca243fd505fb2a14b1622) |
| \"Add Rectangle From 3 Points\" is enabled on a new project | [#20333](https://issues.qgis.org/issues/20333) | [Direct commit](https://github.com/qgis/QGIS/commit/ab3adc663c37b3da589cf6bae56d733fcbc4feb3) | [Direct commit](https://github.com/qgis/QGIS/commit/38051a95afc190d3c65ca243fd505fb2a14b1622) |
| v.buffer processing algorithm fails when using option \"Name of column to use for buffer distances\". | [#19377](https://issues.qgis.org/issues/19377) | [PR #8973](https://github.com/qgis/QGIS/pull/8973) | [PR #8981](https://github.com/qgis/QGIS/pull/8981) |
| Problem with URLs to exclude from network settings | [#20933](https://issues.qgis.org/issues/20933) | [PR #8995](https://github.com/qgis/QGIS/pull/8995) | [PR #9022](https://github.com/qgis/QGIS/pull/9022) |
| Truncated decimals in raster data set pixel size | [#21023](https://issues.qgis.org/issues/21023) | [PR #8996](https://github.com/qgis/QGIS/pull/8996) | [PR #9022](https://github.com/qgis/QGIS/pull/9022) |
| Embedded layer style and labels properties can be modified within the layer styling panel | [#16339](https://issues.qgis.org/issues/16339) | [PR #9006](https://github.com/qgis/QGIS/pull/9006) | [PR #9022](https://github.com/qgis/QGIS/pull/9022) |
| processing: \"default output vector layer extension\" not respected by some tools | [#20557](https://issues.qgis.org/issues/20557) | [PR #8997](https://github.com/qgis/QGIS/pull/8997) | [PR #9022](https://github.com/qgis/QGIS/pull/9022) |
| Unable to stop executing GDAL algorithm | [#20441](https://issues.qgis.org/issues/20441) | [PR #9026](https://github.com/qgis/QGIS/pull/9026) | [PR #9043](https://github.com/qgis/QGIS/pull/9043) |
| Add option to control export features without categories in Processing GRASS algorithms | 未報告 | [PR #9003](https://github.com/qgis/QGIS/pull/9003) | [PR #9043](https://github.com/qgis/QGIS/pull/9043) |
| Processing: v.net tools (GRASS) return empty outputs | [#19904](https://issues.qgis.org/issues/19904) | [PR #9046](https://github.com/qgis/QGIS/pull/9046) | [PR #9058](https://github.com/qgis/QGIS/pull/9058) |
| v.net.salesman sequence HTML output | [#21142](https://issues.qgis.org/issues/21142) | [PR #9046](https://github.com/qgis/QGIS/pull/9046) | [PR #9058](https://github.com/qgis/QGIS/pull/9058) |
| v.net.report and v.net.nreport algorithms failed | 未報告 | [PR #9046](https://github.com/qgis/QGIS/pull/9046) | [PR #9058](https://github.com/qgis/QGIS/pull/9058) |
| Unable to add WCS - bad WCS Request | [#21045](https://issues.qgis.org/issues/21045) | [PR #9005](https://github.com/qgis/QGIS/pull/9005) | [PR #9098](https://github.com/qgis/QGIS/pull/9098) |
| GeoNode API requests require a stronger minor version parsing | [#21093](https://issues.qgis.org/issues/21093) | [PR #9117](https://github.com/qgis/QGIS/pull/9117) | [PR #9141](https://github.com/qgis/QGIS/pull/9141) |
| Check Boxes + Setting Flags in Python in Ubuntu | [#20910](https://issues.qgis.org/issues/20910) | Cannot reproduce with 3.5 |  |
| SAGA openCV and processing tools | [#19540](https://issues.qgis.org/issues/19540) | Cannot reproduce with 3.5 |  |
| Error copying records between tables | [#21154](https://issues.qgis.org/issues/21154) | [PR #9065](https://github.com/qgis/QGIS/pull/9065) | [PR #9185](https://github.com/qgis/QGIS/pull/9185) |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

この機能はAlexander Bruyによって開発されました
### Feature: Bug fixes by Jürgen Fischer
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| Attribute table will not allow letter \'N\' to be entered | [#21019](https://issues.qgis.org/issues/21019) | [Direct commit](https://github.com/qgis/QGIS/commit/99904f1f5e7b86a92f3ff50132fd89750fe858e7) | [Direct commit](https://github.com/qgis/QGIS/commit/3d4c6c4e3f3f270d46a419787eb20bd02f8e16d3) |
| Editing Oracle Spatial view in QGIS | [#20109](https://issues.qgis.org/issues/20109) | [Direct commit](https://github.com/qgis/QGIS/commit/855b3b4e26377647de5c5f9d38485f9f00bc9257) | [Direct commit](https://github.com/qgis/QGIS/commit/1b6329c3c03a07e46d9b1c53ccd7bc3b42b3b247) |
| Missing CP949 (Korean) encoding at Export Project to DXF menu | [#20838](https://issues.qgis.org/issues/20838) | [Direct commit](https://github.com/qgis/QGIS/commit/4e74c8b5480ac28aabc3c0b3eba2609d1a762e8a) | [Direct commit](https://github.com/qgis/QGIS/commit/c7a6b773f2a557b4f2082d0ef114edcd043def74) |
| GeoPackage Raster WEBP support | [#21083](https://issues.qgis.org/issues/21083) |  |  |
| Grass algorithms doesn\'t work from Processing Toolbox level (grass-7.7.svn folder problem) | [#21114](https://issues.qgis.org/issues/21114) | [Direct commit](https://github.com/qgis/QGIS/commit/febbc4f0b9e6f1e1c74c18bcb117148d6587ff87) | [Direct commit](https://github.com/qgis/QGIS/commit/3221b1c83fc00d4f292b2b767a27e4bfcef0f88b) |
| Fix substr help | [#21192](https://issues.qgis.org/issues/21192) | [Direct commit](https://github.com/qgis/QGIS/commit/2bed7ab0018696dba76d2c8053d22633a271486e) | [Direct commit](https://github.com/qgis/QGIS/commit/eb8e36c27dad5413936218893393031e7d0a9915) |
| \[OSGeo4W\] introduce with spatialindex 1.9 | fix in spatialindex | [Direct commit](https://github.com/qgis/QGIS/commit/29d44964529defd0aac94c89e747eee095a89f3a) | [Direct commit](https://github.com/qgis/QGIS/commit/af723c4942427fdce5b935560abd242c5c90ef0a) |
| osgeo4w: fix b6293f23c8c | [#21210](https://issues.qgis.org/issues/21210) | [Direct commit](https://github.com/qgis/QGIS/commit/eea4eda6a35f1a06f84f198249b51b169144c46f) |  |
| Expand ZipItem in foreground | [#21268](https://issues.qgis.org/issues/21268) | [Direct commit](https://github.com/qgis/QGIS/commit/407adc761ebe224a2d72df65551cdcf2addf1735) |  |
| dwg import: catch spline misinterpretation | [#20392](https://issues.qgis.org/issues/20392) | [Direct commit](https://github.com/qgis/QGIS/commit/3aa2d9ff9bc673a6c11456524bb7bfb6532556a7) | [Direct commit](https://github.com/qgis/QGIS/commit/3a0f7363087bce639f4429d9099dac48a708ac69) |
| dwg import: support dxf encoding | [#15999](https://issues.qgis.org/issues/15999) | [Direct commit](https://github.com/qgis/QGIS/commit/e1562a7f1339952be186e924bf96241ce2d826bd) | [Direct commit](https://github.com/qgis/QGIS/commit/3a0f7363087bce639f4429d9099dac48a708ac69) |
| dwg import: force polyline and hatch/ring continuity | [#21330](https://issues.qgis.org/issues/21330) | [Direct commit](https://github.com/qgis/QGIS/commit/b8c727f1d293b64d80c6d1cf29107e0477af3d42) | [Direct commit](https://github.com/qgis/QGIS/commit/3a0f7363087bce639f4429d9099dac48a708ac69) |
| dwg/dxf import: fix angle and alignment handing of (m)texts | [#21330](https://issues.qgis.org/issues/21330) | [Direct commit](https://github.com/qgis/QGIS/commit/92e7faab665d1853191227c8aeb6c13a04c43537) | [Direct commit](https://github.com/qgis/QGIS/commit/3a0f7363087bce639f4429d9099dac48a708ac69) |
| dwg import: fix exception | [#21177](https://issues.qgis.org/issues/21177) | [Direct commit](https://github.com/qgis/QGIS/commit/355deb5905861f263ae7bb03d2bc6fcea4ce5096) | [Direct commit](https://github.com/qgis/QGIS/commit/3a0f7363087bce639f4429d9099dac48a708ac69) |
| dwg import: support nested blocks | [#20392](https://issues.qgis.org/issues/20392) | [Direct commit](https://github.com/qgis/QGIS/commit/d84c34e0b0ca3586543604a600f939c9024ca99a) | [Direct commit](https://github.com/qgis/QGIS/commit/3a0f7363087bce639f4429d9099dac48a708ac69) |
| dwg import: handle wrong hatch interpretation | [#20392](https://issues.qgis.org/issues/20392) | [Direct commit](https://github.com/qgis/QGIS/commit/fd15c3e5b6253c2898dd23dd561121ac1874396c) | [Direct commit](https://github.com/qgis/QGIS/commit/3a0f7363087bce639f4429d9099dac48a708ac69) |
| dxf export: fix svg scaling | not on redmine | [Direct commit](https://github.com/qgis/QGIS/commit/4b55dbef0b60349c74e40d9fd0109f33bca19510) | [Direct commit](https://github.com/qgis/QGIS/commit/23c01de492546e119d5c1c98f97694f470dbd817) |
| dxf export: fix output of closed 3d polylines | [#20242](https://issues.qgis.org/issues/20242) | [Direct commit](https://github.com/qgis/QGIS/commit/56ec47328b9e24951b51c00144221c95f88c6c83) | [Direct commit](https://github.com/qgis/QGIS/commit/db823175cf5c89bc066621e34a8d922c2f80eb87) |
| dxf export: don\'t label invisible features | [#19604](https://issues.qgis.org/issues/19604) | [Direct commit](https://github.com/qgis/QGIS/commit/c389fad1ad0396cf9914dedc8d2e9a9c303cd8f8) | [Direct commit](https://github.com/qgis/QGIS/commit/87c9e18e5677d0d6e2c43d7ecb36afab84ff31fb) |
| support polyline width and generic line width | [#21330](https://issues.qgis.org/issues/21330) | [Direct commit](https://github.com/qgis/QGIS/commit/6bf2d9d4500977c65630add31bb2246f063e20e8) | [Direct commit](https://github.com/qgis/QGIS/commit/c10969e562eda37c0cb78d3ec6db4c1cd68b1106) |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

This feature was developed by [Jürgen Fischer](https://www.norbit.de/)
### 機能: Peter Petrik によるバグ修正
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| Crash when adding existing field to vectorlayer | [#18954](https://issues.qgis.org/issues/18954) | [PR #8982](https://github.com/qgis/QGIS/pull/8982) | [PR #9042](https://github.com/qgis/QGIS/pull/9042) |
| Colour bars in colour chooser UI are rendered with interleaved stripes \[MAC\] | [#15984](https://issues.qgis.org/issues/15984) | [PR #9009](https://github.com/qgis/QGIS/pull/9009) | [PR #9020](https://github.com/qgis/QGIS/pull/9020) |
| Impossible to rename a layer style from the Styling Panel | [#17652](https://issues.qgis.org/issues/17652) | [PR #9021](https://github.com/qgis/QGIS/pull/9021) | [PR #9041](https://github.com/qgis/QGIS/pull/9041) |
| ods tables are not loaded correctly in QGIS 3.4 | [#20588](https://issues.qgis.org/issues/20588) | upstream: <https://github.com/OSGeo/gdal/issues/1243> |  |
| QGIS 3.4.2 crush at QgsApplication.initQgis() on Mac | [#20712](https://issues.qgis.org/issues/20712) | Cannot reproduce with 3.5 |  |
| QGIS freezes on MacOS 10.14 when launched from Launch Services (works ok when launched from terminal) | [#20381](https://issues.qgis.org/issues/20381) | caused by Qt 5.11 used in official MacOS package. Packages must be recreated with Qt 5.12 |  |
| 32 bit floating geotiff showing as black. worked in 2.18 and 3.0 - not working 3.4 | [#20493](https://issues.qgis.org/issues/20493) | [PR #9035](https://github.com/qgis/QGIS/pull/9035) | [PR #9056](https://github.com/qgis/QGIS/pull/9056) |
| python error when running GRASS 7.6 tools in processing on mac OS | [#21269](https://issues.qgis.org/issues/21269) | problem in official MacOS package, workaround/fix suggested in the comment |  |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

This feature was developed by [Peter Petrik](https://www.lutraconsulting.co.uk/)
### 機能: Julien Cabiecesによるバグ修正
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| QGis 3.4 reproducible crash while in idle state | [#20581](https://issues.qgis.org/issues/20581) | [PR #8988](https://github.com/qgis/QGIS/pull/8988) and [PR #9019](https://github.com/qgis/QGIS/pull/9019) | [PR #9027](https://github.com/qgis/QGIS/pull/9027) and [direct commit](https://github.com/qgis/QGIS/commit/9ea7f1efa44c47d4070a1623b18059014e658017) |
| crash at processing\....qgis:snapgeometries | [#18497](https://issues.qgis.org/issues/18497) | [PR #8966](https://github.com/qgis/QGIS/pull/8966) | [PR #9010](https://github.com/qgis/QGIS/pull/9010) |
| QgsExternalResourceWidgetWrapper crashes | [#20140](https://issues.qgis.org/issues/20140) | 重複 |  |
| Crash on vector edit (that has the 4326 CRS) is reprojected in CRS 3857 | [#19579](https://issues.qgis.org/issues/19579) | [proposed a libspatialindex PR](https://github.com/libspatialindex/libspatialindex/pull/126) |  |
| Adding new features in postgis fails with attribute window popup | [#20523](https://issues.qgis.org/issues/20523) | Works for me |  |
| Can\'t remove a constraint set on a field once saved | [#20516](https://issues.qgis.org/issues/20516) | [PR #9032](https://github.com/qgis/QGIS/pull/9032) | [PR #9229](https://github.com/qgis/QGIS/pull/9229) |
| QGIS 3.5 not loading or saving multi-dimensional arrays properly from PostGIS layers | [#20872](https://issues.qgis.org/issues/20872) | [PR #9048](https://github.com/qgis/QGIS/pull/9048) | TODO |
| Attribute Table refresh issue when deleting features from shapefile | [#18421](https://issues.qgis.org/issues/18421) | [PR #9152](https://github.com/qgis/QGIS/pull/9152) | [PR #9214](https://github.com/qgis/QGIS/pull/9214) |
| QgsVectorLayer from spatialite featureid problem | [#20633](https://issues.qgis.org/issues/20633) | Works in 3.5 and 3.4 branch (not in 3.4.4) |  |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

This feature was developed by [Julien Cabieces](https://oslandia.com/)
### 機能: Loïc Bartoletti によるバグ修正
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| Snapping tooltip doesn\'t works when Advanced Digitizing tool is activate | [#18441](https://issues.qgis.org/issues/18441) | Cannot reproduce with 3.5 |  |
| Remove old settings for vertex markers | [#17366](https://issues.qgis.org/issues/17366) | Works as intended |  |
| Snapping options in meters rounded to integers | [#20829](https://issues.qgis.org/issues/20829) | [PR #9168](https://github.com/qgis/QGIS/pull/9168) |  |
| Add the possibility to return a shp if ogr is not compiled with gpkg | 未報告 | [PR #9037](https://github.com/qgis/QGIS/pull/9037) |  |
| fix qgsRound for negative numbers | [#20861](https://issues.qgis.org/issues/20861) | [PR #9030](https://github.com/qgis/QGIS/pull/9030) and [PR #9025](https://github.com/qgis/QGIS/pull/9025) |  |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

This feature was developed by [Loïc Bartoletti](https://oslandia.com/)
### 機能: Victor Olayaによるバグ修正
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| algorithm create grid: reference point problem for calculating Y coordinates | [#20966](https://issues.qgis.org/issues/20966) | [Direct commit](https://github.com/qgis/QGIS/commit/e3516ab1b46137db36f3b7dbf4e4f2ee2df1eb70) |  |
| Error in Processing modeller | [#20609](https://issues.qgis.org/issues/20609) | Not an issue anymore. Cannot reproduce. Ticket has been closed by original reporter |  |
| Do not allow file input for tables or vctor layers if there are dependent fields | [#21055](https://issues.qgis.org/issues/21055) | [Direct commit](https://github.com/qgis/QGIS/commit/6eaa511eed775ce36328a3e1465c32dfb82507aa) |  |
| Deactivating/uninstalling plugin causes Python error when trying to edit a Processing model | [#19607](https://issues.qgis.org/issues/19607) | [PR #8957](https://github.com/qgis/QGIS/pull/8957) |  |
| Postgis DB selector for outputs fails to list schemas in selected DB | [#21099](https://issues.qgis.org/issues/21099) | [PR #9004](https://github.com/qgis/QGIS/pull/9004) |  |
| Regression: outputs of processing models are not assigned the specified styles | [#20573](https://issues.qgis.org/issues/20573) | [Direct commit](https://github.com/qgis/QGIS/commit/eb47288fac06692748c7017f6f125a1fc66e9561) |  |
| QGIS3: SagaUtils.py fails when comman contains non-latin characters | [#18617](https://issues.qgis.org/issues/18617) | [PR #8968](https://github.com/qgis/QGIS/pull/8968) |  |
| \[processing\] Wrong management of locale in output result path | [#19351](https://issues.qgis.org/issues/19351) | [PR #8968](https://github.com/qgis/QGIS/pull/8968) |  |
| \[processing\] SAGA algorithms cannot produce non-shp output | [#21089](https://issues.qgis.org/issues/21089) | [PR #9002](https://github.com/qgis/QGIS/pull/9002) |  |
| Extent selector shows layers with no spatial component (geometryless tables) | [#21129](https://issues.qgis.org/issues/21129) | [PR #9034](https://github.com/qgis/QGIS/pull/9034) (updated by Nyall in [PR #9038](https://github.com/qgis/QGIS/pull/9038)) |  |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

この機能はVictor Olayaによって開発されました
### 機能: Even Rouault によるバグ修正
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| 32 bit floating geotiff showing as black. worked in 2.18 and 3.0 - not working 3.4 | [#20493](https://issues.qgis.org/issues/20493) | [GDAL master commit](https://github.com/OSGeo/gdal/commit/e261b7ff4fa15e762f7f3a73ff3dbc965181d991) and [GDAL 2.4 commit](https://github.com/OSGeo/gdal/commit/0a3d241f96e83b86073efc86b51376c7cd5f6e4f) | - |
| ods tables are not loaded correctly in QGIS 3.4 | [#20588](https://issues.qgis.org/issues/20588) | [GDAL master commit](https://github.com/OSGeo/gdal/commit/ee6278f8dd1be7064db87be87fe31fa8943730ec) and [GDAL 2.4 commit](https://github.com/OSGeo/gdal/commit/4e84cd44868e3b91def41057b7adf28767b4c273) | - |
| attributes in attribute table don\'t match attribute in identify results/labels with WFS layer | [#20865](https://issues.qgis.org/issues/20865) | [PR #9105](https://github.com/qgis/QGIS/pull/9105) | [PR #9113](https://github.com/qgis/QGIS/pull/9113) |
| KML loading bug | [#20173](https://issues.qgis.org/issues/20173) | [GDAL master commit](https://github.com/OSGeo/gdal/commit/467b088edd18f90744bccac9ff6d83a6a5d92d93) and [GDAL 2.4 in](https://github.com/OSGeo/gdal/commit/ec4bd32cd591b672274383f7c06da1d58a2a3500) | - |
| Zoom to Layer does not respond to filtered WFS | [#20742](https://issues.qgis.org/issues/20742) | [PR #9118](https://github.com/qgis/QGIS/pull/9118) | [Direct commit](https://github.com/qgis/QGIS/commit/8834ec78207c091175cb0f48b518b6d2988f337d) |
| Processing time for GeoJSON 10 times slower in 3.4 | [#21085](https://issues.qgis.org/issues/21085) | [GDAL master commmit](https://github.com/OSGeo/gdal/commit/bd668db37eb6f176226ebbe7efe34cfac86a3cf6a) and [GDAL 2.4 commit](https://github.com/OSGeo/gdal/commit/d6c38adfa28f75da0630f3e3ac26dbb501fc361e) |  |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

This feature was developed by [Even Rouault](http://www.spatialys.com/)
### Feature: Bug fixes by Martin Dobias
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| \[vertex tool\] Fix issue with hidden layers being editable | [#18434](https://issues.qgis.org/issues/18434) | [PR #8992](https://github.com/qgis/QGIS/pull/8992) | [Direct commit](https://github.com/qgis/QGIS/commit/2ad47198c446a1f541dca195439bb432da0dce6a) |
| \[vertex tool\] Fix vertex addition to polygon\'s first segment | [#20774](https://issues.qgis.org/issues/20774) | [PR #9024](https://github.com/qgis/QGIS/pull/9024) | [Direct commit](https://github.com/qgis/QGIS/commit/4423caff0994de64185fcc7b3acb5058ca047c14) |
| \[vertex tool\] Misleading message when deleting all nodes of a ring or a part | [#17754](https://issues.qgis.org/issues/17754) | not fixed! needs quite involved fix to make |  |
| \[vertex tool\] Improvements to the right-click behavior to pick locked feature | N/A | [PR #9052](https://github.com/qgis/QGIS/pull/9052) | [PR #9161](https://github.com/qgis/QGIS/pull/9161) |
| \[vertex tool\] right-click to loop through editable features | N/A | [PR #9087](https://github.com/qgis/QGIS/pull/9087) | [PR #9161](https://github.com/qgis/QGIS/pull/9161) |
| \[vertex tool\] misc small UX improvements | N/A | [PR #9116](https://github.com/qgis/QGIS/pull/9116) | [PR #9161](https://github.com/qgis/QGIS/pull/9161) |
| \[vertex tool\] two more UX fixes | N/A | [PR #9130](https://github.com/qgis/QGIS/pull/9130) | [PR #9161](https://github.com/qgis/QGIS/pull/9161) |
| \[vertex tool\] Few more UX improvements | [#21283](https://issues.qgis.org/issues/21283) | [PR #9222](https://github.com/qgis/QGIS/pull/9222) | [PR #9227](https://github.com/qgis/QGIS/pull/9227) |

This feature was funded by [QGIS user group Germany](https://www.qgis.de/)

This feature was developed by [Martin Dobias](https://www.lutraconsulting.co.uk/)
### 機能: Nyall Dawsonによるバグ修正
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| \[postgis\] Fix creation of new Z/M enabled, curved geometry type layers | N/A | [Direct commit](https://github.com/qgis/QGIS/commit/07746dbc0e5b34e31e85e944fc6f53113721a696) | [Direct commit](https://github.com/qgis/QGIS/commit/a61abe5bb3b4c1b633f2f76b69a7f274abeb33d3) |
| \[categorized\] Fix blank layers when using categorized renderer | [#21188](https://issues.qgis.org/issues/21188) | [Direct commit](https://github.com/qgis/QGIS/commit/7714bfbfbe6acec1c193365a173c822cb72c4361) | N/A |
| Fix invalid data source message is always shown after dragging and dropping vector layers to QGIS window | N/A | [Direct commit](https://github.com/qgis/QGIS/commit/a1d8d9ae5d8ff5130e3ccd179617b1e9c0bf4062) | N/A |
| \[processing\] Buffer algorithm should always export multipolygon layers | [#21191](https://issues.qgis.org/issues/21191) | [Direct commit](https://github.com/qgis/QGIS/commit/f22f182bcfd7b7f5b5d8f782f3df08ee9d705115) | [Direct commit](https://github.com/qgis/QGIS/commit/f4866402f7ecf759598e652d5d640dd1fdc48c50) |
| \[processing\]\[gdal\] Fix polygonize field name is ignored | N/A | [Direct commit](https://github.com/qgis/QGIS/commit/06d5b996bfc37f2877ecbf708af608952420ed45) | [Direct commit](https://github.com/qgis/QGIS/commit/ae21d07d4b082ede7b56941aaa1ce57fad8cdb9a) |
| \[processing\] Allow matrix parameters to be correctly set for model child algorithms | [#20914](https://issues.qgis.org/issues/20914) | [Direct commit](https://github.com/qgis/QGIS/commit/eeff02fc14b96a6d3f95ac2122d1d82654dcf268) | [Direct commit](https://github.com/qgis/QGIS/commit/d5900557bdb25f4e285638bf1de85f43430ba15d) |
| \[processing\]\[gdal\] Ensure that GDAL algs output the CORRECT generated filename for outputs | N/A | [Direct commit](https://github.com/qgis/QGIS/commit/c93775f6b177ab2f64bd347c9a6f78896cee78dd) | [Direct commit](https://github.com/qgis/QGIS/commit/93c135f97cad06a1ff703ae1839397f14cb82b3d) |
| \[processing\]\[gdal\] Fix incorrect definition of gdal_warp extra_param parameter | N/A | [Direct commit](https://github.com/qgis/QGIS/commit/f54f5a4fe70792f4d7ea376e28edad88c4d35d4a) | N/A |
| Allow for exact calculation of symbol sizes with mixed layer units | [#21143](https://issues.qgis.org/issues/21143) | [Direct commit](https://github.com/qgis/QGIS/commit/867e39947b3f24d0b7714cd44e28126b61769340) | [Direct commit](https://github.com/qgis/QGIS/commit/33987fa5505ebc4cb9d83c195c49e5938f7c1f73) |
| Fix hang when WMS credentials requested | [#20826](https://issues.qgis.org/issues/20826) | [Direct commit](https://github.com/qgis/QGIS/commit/c9e761649820f8444a41da5e18850061b207c09c) | [Direct commit](https://github.com/qgis/QGIS/commit/ad6e1566a70d4f1a9d959a4de9f18bcae9dbd566) |
| Fix misc deadlocks/crashes in network requests, especially when SSL errors or timeouts occur | Multiple | Multiple | N/A \-- too intrusive |
| \[processing\]\[saga\] Fix definition of Multiple regression points/grids alg | [#21146](https://issues.qgis.org/issues/21146) | [Direct commit](https://github.com/qgis/QGIS/commit/4f8e2317d796881f942bbc6bdcbe60f3470f48fe) | [Direct commit](https://github.com/qgis/QGIS/commit/1916a7fd7ae4a3d5bb767bde76f3042dfd0a7474) |
| \[processing\] do not show geometryless layers in extent selector | [#21129](https://issues.qgis.org/issues/21129) | [Direct commit](https://github.com/qgis/QGIS/commit/5bfec27938ff95cd65c1cf5b88cc13ce26ca1d5d) | [Direct commit](https://github.com/qgis/QGIS/commit/06ee13263d842ea0d7e188107cb9033893b6c75f) |
| \[layouts\] Add checkbox to disable raster tiling for PDF/SVG exports | [#19500](https://issues.qgis.org/issues/19500) | [Direct commit](https://github.com/qgis/QGIS/commit/60b8d05278cd8133e1c06108ba875960d56e90e5) | N/A \-- too intrusive |
| Fix empty strings in proxy exclude list results in proxy being skippe\\d for ALL hosts | [#20213](https://issues.qgis.org/issues/20213) | [Direct commit](https://github.com/qgis/QGIS/commit/cf1cf0fe455a42edf6db4ab9fa07c1ad641b16cb) | [Direct commit](https://github.com/qgis/QGIS/commit/34625110327c5bec4969c2a42cfa8c210bd3b630) |
| Avoid project being marked dirty as soon as its opened | N/A | [Direct commit](https://github.com/qgis/QGIS/commit/394e5d8d76480c1235c49e46d52f5f4a277cf824) | N/A |
| Fix loss of project when saving to QGZ format and path contains non-ascii chars | [#19567](https://issues.qgis.org/issues/19567) | [Direct commit](https://github.com/qgis/QGIS/commit/7d7462c33334a501167813d720fb2589d3c579ec) | [Direct commit](https://github.com/qgis/QGIS/commit/bfef851b1ca98a2c45117a2b1f911f7f1b7155b1) |
| Fix evaluation of data defined properties for subsymbols of subsymbols | [#18384](https://issues.qgis.org/issues/18384) | [Direct commit](https://github.com/qgis/QGIS/commit/9cf2ff31d86e6b7671aaca137a60a7b7a975ef62) | [Direct commit](https://github.com/qgis/QGIS/commit/7e25cea7e939248c8816d2739ccd44a31c606f11) |
| Fix shortest path algorithm can \"shortcut\" when using network in geographic coordinates | [#20997](https://issues.qgis.org/issues/20997) | [Direct commit](https://github.com/qgis/QGIS/commit/e75a88825665e7bb43c6c3cd1b2c22037cd29784) | [Direct commit](https://github.com/qgis/QGIS/commit/a3428e5f92b8b98cc753de0e9366f36e7ecc018e) |
| Fix project loading task never completes when project has embedded layers | [#21012](https://issues.qgis.org/issues/21012) | [Direct commit](https://github.com/qgis/QGIS/commit/7ad4b05112af0c35bd9a8e0526e8823a6b695335) | [Direct commit](https://github.com/qgis/QGIS/commit/6584fb295aed03c3167d056e1bac59a808a1abb5) |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

This feature was developed by [Nyall Dawson](https://north-road.com/)
### Feature: Bug fixes by Hugo Mercier
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| Qgis 3.4.1 crashes when accessing methods of feature | [#20752](https://issues.qgis.org/issues/20752) | closed |  |
| Bad size request with a georeferenced raster | [#8272](https://issues.qgis.org/issues/8272) | Can\'t reproduce anymore in 3.5 |  |
| Postgresql: empty SAVEPOINTS | http://issues.qgis.org/issues/17535 | not applicable anymore |  |
| Range widget does not honor default value on not null column | [#20831](https://issues.qgis.org/issues/20831) | [PR #9033](https://github.com/qgis/QGIS/pull/9033) and [PR #9033](https://github.com/qgis/QGIS/pull/9033) |  |
| Range widget gives NULL value in Attributes Form/Table | [#21125](https://issues.qgis.org/issues/21125) | [PR #9033](https://github.com/qgis/QGIS/pull/9033) | [PR #9192](https://github.com/qgis/QGIS/pull/9192) |
| QGIS 3.4.1 advanced modification and snap block QGIS | [#20568](https://issues.qgis.org/issues/20568) | closed |  |
| Vertex markers not displayed properly for MultiPolygon features | [#19909](https://issues.qgis.org/issues/19909) | [PR #9036](https://github.com/qgis/QGIS/pull/9036) | [PR #9192](https://github.com/qgis/QGIS/pull/9192) |
| Cascading controls in forms | [#11264](https://issues.qgis.org/issues/11264) | triage, closed |  |
| \$length incorrect in expressions | [#19355](https://issues.qgis.org/issues/19355) | [PR #9063](https://github.com/qgis/QGIS/pull/9063) | [PR #9192](https://github.com/qgis/QGIS/pull/9192) |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

This feature was developed by [Hugo Mercier](https://oslandia.com/)

{{<content-end >}}
