---
HasBanner: false
draft: false
releaseDate: '2018-02-23'
section: project
sidebar: true
title: QGIS 3.0の変更履歴
type: visual-changelog

---
{{<content-start >}}
# QGIS 3.0の変更履歴{#changelog30 }
![image1](images/projects/8c7c6c5ded71fa7284d9e31144e2c0cdb02059ee.png)

リリース日: 2018-02-23

The greatest QGIS release ever! QGIS 3.0 is a huge overhaul and cleanup of our beloved Open Source GIS. QGIS 3.0 brings a massive list of new changes - the highlights of which we will try to cover here. As always can we remind you that QGIS is an open source project and if you are able to, consider supporting our work through [donations](http://www.qgis.org/en/site/getinvolved/donations.html?highlight=donate), [sponsorship](http://www.qgis.org/en/site/getinvolved/governance/sponsorship/sponsorship.html) or contributions to the code documentation, web site and so on.

**謝辞**

We would like to thank the developers, documenters, testers and all the many folks out there who volunteer their time and effort (or fund people to do so). From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

QGIS is supported by donors and sponsors. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become and official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

QGIS はフリーのソフトウェアです。利用する上で金銭を支払う義務はありません。実際、私たちは利用者の財政状況や社会的地位にかかわらず、より多くの人に QGIS を利用して欲しいと思っています。私たちは地理空間的な意思決定ツールによって人々が力を持つことが、全人類の社会をより良くすると信じています。

{{<table-of-contents >}}
## QGISバージョン3.0のスポンサー
{{<fund type="changelog" relativeImgPath=true >}}
### 機能：dxf2shpコンバータプラグインを削除する
この機能はOGRで利用可能であり、もはやこのタスクを実行する専用のQGISプラグインは必要ありません
### 機能：orphaned oracle raster pluginを削除する
### 機能：コアプロセッシングからTauDEMプロバイダを削除した
TauDEMはかなり特殊なツールセットであり、いくつかの追加ツールをインストールする必要があります。そこで、それを別のプロバイダにして、コードベースのコアサイズとメンテナンスの労力を削減することにしました。
### 機能：QGISヘルプファイルの場所を設定するためのより多くのヘルプと可能性
アルゴリズムとダイアログのその他のヘルプボタンが追加され、オンラインのQGISドキュメントが表示されます。

構成により、オンライン、組織のネットワークまたはローカルコンピュータに保存されたコンテキストヘルプにアクセスできます。また、異なるヘルプソースを組み合わせることもできます。

![image112](images/entries/7c17e43c0c6738c9588f3bef149ca7f3d8a13948.png.400x300_q85_crop.webp)

この機能はAlexander Bruyによって開発されました
### 機能：Photo、WebView、およびFileNameウィジェットを添付ファイルに移行する
![image113](images/entries/d2e949a9804de76d196af6e58996165d01350fec.jpeg.400x300_q85_crop.webp)
### 機能：otbおよびlidartoolsプロバイダをプロセッシングから削除しました。
新しいロジックは、外部ソフトウェアライフサイクルに従うことができるプラグインプロバイダを開発することです。
## ユーザーインタフェース
### 機能：タブ付きのフローティングドックを有効にする
For qt \> 5.6 builds, it is possible to drop several floating docks in the same floating window where they appear as tabs <https://woboq.com/blog/qdockwidget-changes-in-56.html>

![image66](images/entries/02137f3073c3f8a32bc505bd4916a8df751db79f.gif)
### 機能：細かい解像度のマウスホイールズームをサポート
一部のマウス/ポインターデバイス（特にMacの場合）には、より細かい解像度があります。それらは高い頻度で小さいデルタ値でマウスホイールイベントを送信します。このようなデバイスでのズーム操作は、高速ズーム操作では使用できませんでした。これは3.0で修正されています。

この機能はMatthias Kuhnによって開発されました
### 機能：ショートカットの設定ダイアログに検索バーを追加する
アクション名とショートカットによる検索をサポート

![image67](images/entries/5f9439417546fff26fe410b5a860a7680b07c53e.png.400x300_q85_crop.webp)

この機能はAlexander Bruyによって開発されました
### 機能：ロケータバー
ロケータバーは、QGISの左下隅に高速で常に準備が整った一般的なプラガブル検索機能です。

現在、アルゴリズム、アクション、レイヤー名を検索することができますが、属性値を入力することによって現在のアクティブなレイヤーの地物も選択できます。

It is \'easy\' extendable, so everybody can create a QgsLocatorFilter for his/her national geocoding service or other search online or database search facility.

![image68](images/entries/c5eba5f5e5a6745d1a81df88eb55f01a68fcc1ad.gif)

この機能はNyall Dawsonによって開発されました
### 機能：ノンブロッキング、インライン編集
- 地図単位での縮尺設定
- カラーブリュワーと限定ランダムランプエディタ
- スタイルパネルのインラインカラーリストで色を編集する
- コンポーザの色と記号のインライン編集

スタイルパネルのインライン表示
### 機能：ユーザーのカラースキームメニューを表示するオプションを追加する
これにより、ユーザーが作成したカラースキームをカラーボタンのドロップダウンメニューに表示するかどうかをユーザーが設定できるようになります。

It\'s accessed through the color picker dialog, on the lists tab. Just add a new color scheme, then from the scheme menu tick the new \"show in buttons\" option.

これは、一般的なパレットのセットを持っていて、カラーメニューから即座に使用できるようにしたい場合に便利です。

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### 機能：地図キャンバスの北の矢印の装飾のための色の設定
すべての地図キャンバスの北矢印の装飾の色設定が追加されました。

![image69](images/entries/6a3fa6fb065a02defaa42440f301847e8fbbeb75.jpg.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Feature: Improved map canvas\' save as image
The map canvas\' save as image function has been expanded and now offers users the possibility to tweak the scale, resolution, and extent on-the-fly. Extents can be restricted to a height-width ratio. A save as PDF function was also added to quickly export the map canvas into a resolution-independent PDF.

![image70](images/entries/a2adf1e9930f23fa739e68a6e2c55e1b553867b9.png.400x300_q85_crop.webp)

この機能は Andreas Neumann によって資金提供されました(partial funding)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### 機能：メインウィンドウで開いたパネルの表示を切り替えます
Accessible via: - View menu \> Toggle Panels Visibility - **Ctrl+Tab** keyboard shortcut

![image71](images/entries/68249b50c2813f4b204cb0305587b2850e7cd61e.gif)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### 機能：ユーザーインターフェイスの一貫性の向上
This work sponsored by the QGIS grant program on \"adding consistency to UI controls\" is now complete and merged into master. The following tasks were done as part of this work:
- **transparent / opacity / alpha** に関するすべてのAPIは、 **setOpacity()** および **opacity()** に標準化されました。このメソッドは、0（透明）と1（不透明）の間で2倍の値を取り、Qt APIとの一貫性を保ちます。
- **新しいウィジェットQgsOpacityWidget** が作成されました。これは、不透明度が設定されているUIを通じてどこでも使用されています。これにより、一貫性のある動作が保証され、どこでも不透明度コントロールが検索されます。
- **回転** はAPIとUIで標準化されているので、回転は常に時計回りに適用されます。-360〜360の値を受け入れるように、すべての回転ウィジェットが更新されました。
- 2.x回転とデータ定義の回転を使用したラベル付きプロジェクトは3.0で開くと透過的に **アップグレード** されます
- 縮尺APIは、QGIS API全体で一貫するようになりました。 **縮尺分母と実数縮尺の混乱がなくなりました** 、現在はすべてが縮尺分母で動作しています。すべての縮尺範囲コールの動作は、最小/最大縮尺（およびこれに関する明示的なAPIドキュメント）の共通の意味で標準化されています。
- すべての縮尺コントロールは、UI全体の一貫性のために標準縮尺ウィジェットを使用するようになりました
- ラベリングは残りのUIと同じ最小/最大縮尺の定義を使用し、既存のプロジェクトは3.0で開くと透過的にアップグレードされるようになりました。
- ルールベースの縮尺制限を破るバグを含む、縮尺使用に関する最も顕著なバグを修正

QGIS PSCとこのプロジェクトをスポンサーにして、それを進めることを可能にするプロジェクトドナーに感謝します！

この機能は、QGIS出資者とドナーによって資金提供されました

This feature was developed by [Nyall Dawson](https://north-road.com)
### 機能：単一のグループ内のレイヤーを開く
多くのサブレイヤーを開くと、凡例の同じグループ内でそれらをすべて開くことができます。

![image72](images/entries/a64155774fee81370dfb5a786cf7386bffb7a089.png.400x300_q85_crop.webp)

This feature was funded by [Kartoza](http://www.kartoza.com)

This feature was developed by [Etienne Trimaille](https://github.com/Gustry)
## 三次元機能
### 機能：3Dマップビューと地形生成
私たちは、QGISで真新しいネイティブ3D地図ビューを持っています！3D地図ビューでは、上の地形に2D地図（プロジェクトレイヤーからレンダリング）が表示されます。デフォルトでは地形は平面ですが、高さデータのソースとしてデジタル標高モデルを使用したラスターレイヤーを使用することは可能です。

Use menu View \> New 3D Map View to add a 3D view of the project. This will create a new dock widget with 3D map canvas. The 3D view uses the same controls like 2D map views to browse the map using mouse (drag map to move it around, mouse wheel to zoom) or keyboard arrow keys. In addition there are camera controls specific to 3D views: it is possible to rotate and tilt camera by one of the following ways:
- 中マウスボタンが押された状態でマウスをドラッグすることにより
- Shiftキーを押しながらマウスの左ボタンを押しながらマウスをドラッグすると
- Shiftキーを押しながら上/下/左/右キーを使用して

![image121](images/entries/86e6303419d84812266eada5327e74dbc6d507a4.jpg.400x300_q85_crop.webp)

This feature was funded by [QGIS.ORG](https://qgis.org/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### 機能：地図レイヤーの3Dレンダラー
デフォルト設定では、地図レイヤーは地形の上に2D地図画像にレンダリングされます。しかし、いくつかの地図レイヤーに3Dレンダラを設定することで、3Dワールドをより有効に活用できます。3Dレンダラでは、データを3Dビューで真の3Dオブジェクトとして表示できます。これは現在、ベクターレイヤー（すべてのジオメトリタイプ - ポイント、ラインまたはポリゴン）でサポートされています。これにより、次のような視覚化が可能になります。
- 建物のフットプリントを持つポリゴンを押し出して（おそらくデータ定義の高さで）3Dビューを実現できます
- ツリーポイントの位置を持つポイントは、ツリーの3Dシンボル（単純な幾何学的形状またはサポートされているファイル形式からロードされた既存の3Dモデル）でレンダリングできます。

3Dレンダラを設定するには、レイヤースタイリングドックウィジェットまたはベクターレイヤプロパティダイアログを使用します。3Dレンダラの設定用の新しいタブがあります。

![image122](images/entries/311f1b52d068ccca9ef74f9ea1dcba259c7ed674.png.400x300_q85_crop.webp)

This feature was funded by [QGIS.ORG](https://qgis.org/)

This feature was developed by [Martin Dobias, Peter Petrik (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
## 計算式
### 機能：新しい式変数
Adds `@project_crs` and `@project_crs_definition` variables for retrieving the current project CRS
### Feature: new global expression variable \@qgis_locale
QGISで使用される現在のロケールを返します。デフォルトでは、現在のシステムロケールです。ユーザーがQGIS設定でロケールオーバーライドを有効にすると、オーバーライドされたロケールが返されます。

![image63](images/entries/23e0bd2bc2cd560dad2d2a873e7d9ab98c532fb0.png.400x300_q85_crop.webp)

この機能はAlexander Bruyによって開発されました
### 機能：地図設定の新しい式変数
    - map_crs, map_crs_definition: retrieves crs details for map
    - map_units: retrieves units for map (eg 'meters','degrees')
    
This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### 機能：新しい式の関数
**アトラス式**
- **atlas_layerid** and **atlas_layername**: Returns layer ID and layer name of the current layer in the atlas.

**集計の式**
- **array_agg(expression, group_by, filter)**: Returns an array of aggregated values from a field or expression.

**配列の式**

New group that contains expression functions for the creation and manipulation of arrays (also known as list data structures). The order of values within the array matters, in contrary to the \'map\' data structure, where the order of key-value pairs is irrelevant and values are identified by their keys.
- **array(value1, value2, ...)** : Returns an array containing all the values passed as parameter.
- **array_append(array, value)**: Returns an array with the given value added at the end.
- **array_cat(array1, array2, ...)**: Returns an array containing all the given arrays concatenated.
- **array_contains(array, value)**: Returns true if an array contains the given value.
- **array_distinct(array)**: Returns an array containing distinct values of the given array.
- **array_find(array, value)**: Returns the index (0 for the first one) of a value within an array. Returns -1 if the value is not found.
- **array_first(array)**: Returns the first value of an array.
- **array_get(array, index)**: Returns the Nth value (0 for the first one) of an array.
- **array_insert(array, pos, value)**: Returns an array with the given value added at the given position.
- **array_intersect(array1, array2)**: Returns true if any element of array1 exists in array2.
- **array_last(array)**: Returns the last value of an array.
- **array_length(array)**: Returns the number of elements of an array.
- **array_prepend(array, value)**: Returns an array with the given value added at the beginning.
- **array_remove_all(array, value)**: Returns an array with all the entries of the given value removed.
- **array_remove_at(array, pos)**: Returns an array with the given index removed.
- **array_reverse(array)**: Returns the given array with array values in reversed order.
- **array_slice(array, start_pos, end_pos)**: Returns a portion of the array. The slice is defined by the start_pos and end_pos arguments.
- **array_to_string(array, delimiter, empty_value)**: Concatenates array elements into a string separated by a delimiter using and optional string for empty values.
- **regexp_matches(string, regex, empty_value)**: Returns an array of all strings captured by capturing groups, in the order the groups themselves appear in the supplied regular expression against a string.
- **string_to_array(string, delimiter, empty_value)**: Splits string into an array using supplied delimiter and optional string for empty values.

**色の式**
- **create_ramp(map, discrete)**: Returns a gradient ramp from a map of color strings and steps.

**日時式**
- **epoch(date)** ：Unixエポックと指定された日付の間の間隔をミリ秒で返します。

**一般的な式**
- **env(name)** ：環境変数を取得し、その内容を文字列として返します。変数が見つからない場合、NULLが返されます。
- **raster_statistic(layer, band, property)**: Returns statistics from a raster layer. Properties: min/max/avg/range/stdev/sum
- **with_variable(name, value, node)**: This function sets a variable for any expression code that will be provided as 3rd argument. This is only useful for complicated expressions, where the same calculated value needs to be used in different places.

ジオメトリの式
- **extend(geometry, start_distance, end_distance)**: Extends linestrings by a specified amount at the start and end of the line
- **hausdorff_distance(geometry a, geometry b, densify_fraction)**: Returns the Hausdorff distance between two geometries. This is basically a measure of how similar or dissimilar 2 geometries are, with a lower distance indicating more similar geometries.
- **inclination(inclination(point_a, point_b)**: Returns the inclination measured from the zenith (0) to the nadir (180) on point_a to point_b.
- **make_circle(center, radius, segment)**: Creates a circular, segmentized, polygon.
- **make_ellipse(center, semi_major_axis, semi_minor_axis, azimuth, segment)**: Creates an elliptical, segmentized, polygon.
- **make_regular_polygon(center, radius, number_sides, circle)**: Creates a regular polygon.
- **make_triangle()**: help still missing
- **minimal_circle(geometry, segment)**: Returns the minimal enclosing circle of a geometry. It represents the minimum circle that encloses all geometries within the set.
- **offset_curve(geometry, distance, segments, join, miter_limit)**: Returns a geometry formed by offsetting a linestring geometry to the side. Distances are in the Spatial Reference System of this geometry.
- **oriented_bbox(geom)**: Returns a geometry which represents the minimal oriented bounding box of an input geometry.
- **pole_of_inaccessibility(geometry, tolerance)**: Calculates the approximate pole of inaccessibility for a surface, which is the most distant internal point from the boundary of the surface. This function uses the \'polylabel\' algorithm (Vladimir Agafonkin, 2016), which is an iterative approach guaranteed to find the true pole of inaccessibility within a specified tolerance.
- **simplify(geometry, tolerance)** ：距離に基づく閾を使用してノードを削除することでジオメトリを単純化します（つまりDouglas Peuckerアルゴリズム）。このアルゴリズムは、ジオメトリの大きな偏差を保存し、ほぼ直線セグメントの頂点の数を減らします。
- **simplify_vw(geometry, tolerance)**: Simplifies a geometry by removing nodes using an area based threshold (the Visvalingam-Whyatt algorithm). The algorithm removes vertices which create small areas in geometries, e.g., narrow spikes or nearly straight segments.
- **smooth(geometry, iterations, offset, min_length, max_angle)**: Smooths a geometry by adding extra nodes which round off corners in the geometry.
- **single_sided_buffer(geometry, distance, segments, join, miter_limit)**: Returns a geometry formed by buffering out just one side of a linestring geometry. Distances are in the Spatial Reference System of this geometry.

**レイヤープロパティ**
- **crs_description** returns the CRS description of the layer.

**マップ式**

This group contains expression functions for the creation and manipulation of \'map\' data structures (also known as dictionary objects, key-value pairs, or associative arrays). One can assign values to given keys. The order of the key-value pairs in the map object is not relevant.
- **map(key1, value1, key2, value2, , ...)**: Returns a map containing all the keys and values passed as pair of parameters.
- **map_akeys(map)**: Returns all the keys of a map as an array.
- **map_avals(map)**: Returns all the values of a map as an array.
- **map_concat(map1, map2, ...)**: Returns a map containing all the entries of the given maps. If two maps contain the same key, the value of the second map is taken.
- **map_delete(map, key)**: Returns a map with the given key and its corresponding value deleted.
- **map_exist(map, key)**: Returns true if the given key exists in the map.
- **map_get(map, key)**: Returns the value of a map, given it\'s key.
- **map_insert(map, key, value)**: Returns a map with an added key/value.

**地図レイヤー**

現在のプロジェクトで使用可能な地図レイヤーのリストを含む新しいグループ。内部地図レイヤーIDを返します。これは地図レイヤーを参照する他の多くの式関数で使用されます。

**数式**
- **inclination(point_a, point_b)**: Returns the inclination measured from the zenith (0) to the nadir (180) on point_a to point_b.

**演算子**
- **\~:** Performs a regular expression match on a string value.

**レコードと属性の表現**

renamed from just \"Record\"
- **get_feature_by_id(layer, feature_id)**: Returns the feature with an id on a layer.
- **is_selected(feature, layer)**: Returns if a feature is selected. If called with no parameters checks the current feature.
- **num_selected(layer)**: Returns the number of selected features on a given layer. By default works on the layer on which the expression is evaluated.
- **represent_value(value, fieldName)**: Returns the configured representafftion value for a field value. It depends on the configured widget type. Often, this is useful for \'Value Map\' widgets.
- ** uuid（）**：Qt QUuid :: createUuidメソッドを使用して、各行に対してUniversally Unique Identifier（UUID）を生成します。各UUIDは38文字です。

**関係**

New group listing all available table relations in a project. Useful for relation_aggregate functions.

**廃止予定**
- **\$scale**: old variable to get current map scale. Replaced by **maps_scale**

**変更**
- **substr()** 関数での変更
  - support negative start value (e.g. substr(\'hello\',-2) returns \'lo\')
  - support negative length value (e.g. substr(\'hello\',3,-1) returns \'ll\')
  - length parameter now optional, defaults to end of string (e.g. substr(\'hello world\',7) returns \'world\')
- **strpos()** は現在、文字列検索内の単純な文字列に依存しています
- **regexp_match()** now returns pos of a matching regular expression

この機能は多数の開発者によって開発されました
### Feature: Expose \@parent variable in aggregate functions
This makes it possible to access attributes and geometry from the parent feature when in the filter of the \"aggregate\" expression function. With this in place aggregates can be calculated per feature.

    E.g. max "measurement" for each point_station per polygon_research_area.
    
地物をデジタイズするときのデフォルトの属性値

`aggregate(layer:='countries', aggregate:='max', expression:=\"code\", filter:=intersects( $geometry, geometry(@parent) ) )`

![image64](images/entries/7666e6f1fd7a95ec3e099c27c6bf9ef6b145c956.jpeg.400x300_q85_crop.webp)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](https://opengis.ch)
### Feature: Item_variables expression function inside compositions
This adds a new item_variables expression function when expressions are used inside a composition context.

この関数は、コンポジション内のアイテムのIDを1つの引数として取り、そのアイテムの変数名から値のマップを返します。これにより、コンポジション内の別のアイテムのプロパティを取得するラベルにテキストを挿入するなどの作業を行うことができます。

地図の縮尺をラベルに挿入する：

`map_get( item_variables( 'map'),'map_scale')`

地図中心のx座標をラベルに挿入する：

`x(map_get( item_variables( 'map'),'map_extent_center'))`

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
## 文書化
### 機能：プロセッシングアルゴリズムの拡張
プロセッシングアルゴリズムがレビューされ、文書化されました。[ヘルプ]ボタンをクリックすると、QGISのWebサイトが開き、アルゴリズムの説明に拡張されたドキュメントと画像が表示されます。

![image65](images/entries/ca710bbcb3e67a83217d5894ccccfcb5103b1bf4.png.400x300_q85_crop.webp)

この機能は、QGISグラント提案 によって資金提供されました

This feature was developed by [Matteo Ghetta (Faunalia), Alexander Bruy](http://www.faunalia.eu/)
## シンボロジ
### 機能：データ定義のシンボルレイヤーの可視性
Adds a data defined override to control a symbol layer\'s visibility. Allows users to disable drawing certain symbol layers for matching features.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### 機能：シングルバンド疑似カラーレンダリングに使用されるカラーランプの保存と復元
この機能はAlexander Bruyによって開発されました
### 機能：使用可能なシンボルユニットにポイントとインチを追加する
This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### 機能：新しいカラーランプボタンウィジェット
In QGIS 3.0, handling of color ramps has gotten much better via a newly introduced color ramp button widget. Improvements include: - custom color ramp settings are remembered when projects are re-opened - color ramp inversion is implemented within the widget, enabling this action across QGIS - quick access to \"favorite\" color ramps within the widget pop-up menu - interfacing with catalogs (cpt-city and ColorBrewer) is now much more pleasant

![image73](images/entries/547ffa26f79435ff28198820bb0d95dc495b4f13.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### 機能：スタイル管理の再作業とアップグレード
スタイル管理は大幅にアップグレードされました。改善点は次のとおりです。
- 新しいお気に入りのグループ化システムが追加されました。シンボルリストウィジェットはデフォルトで
- シンボルリストウィジェットで選択したタグ/スマートグループは、レイヤーを切り替えても（そしてセッションをまたいでも）持続するようになりました。
- ユーザーがカテゴリを追加／名前変更／削除すると、シンボルリストウィジェットは tag / smartgroup コンボボックスを更新します。
- ユーザーは、スタイルデータベースに保存しながら、直接タグ付けしたり、お気に入りに追加したりできます。
- スタイル管理を効率化するために、グループは削除され、完全にタグに置き換えられました
- タグがインポート/エクスポートのユーザーインターフェイスに統合されました

![image74](images/entries/bb43cc8a048018b0f54463674ebf2d11bb0abc21.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### 機能：ラスターレンダラーの複数項目の色と透明度の設定をサポート
It is now possible to change the color and transparency for multiple values at the same time for the singleband pseudocolor and the paletted renderers. Simply select values within the values\' list and right click to have a pop-up menu appear.

![image75](images/entries/dc60a3f5fdc3a6568e8f3b9bf635066fcde9926d.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### 機能：カラーボタンのドロップダウンメニューにアルファスライダを表示する
色のアルファに素早く調整できます

![image76](images/entries/669437f416c6ef5c18dd87ecdfc52772e0b597c7.png.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### 機能：疑似色レンダラに対するラスター範囲ツールバー・アクションのサポート
この機能はMathieu Pellerinによって開発されました
### 機能：paletted レンダラへの 透明度のサポート 
QGIS 3.0では、パレットレンダラの一意の値の透明度値を変更できるようになりました。

![image77](images/entries/603b73fbf8ad7db9cdb43689641eb70326c11bbf.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### 機能：キャンバス更新時のラスター自動stretching
see <https://lists.osgeo.org/pipermail/qgis-developer/2016-September/044393.html> follow up to raster pseudocolor updated extent auto classification.

この機能はEven Rouaultによって開発されました
### 機能：注記の内容のマージンを制御する
注記内のコンテンツの左/上/右/下余白を設定できます。

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### 機能：注記は塗りシンボルスタイルを使用してスタイル設定できます
This changes the rendering of annotation frames to use QGIS\' symbology engine, which means that all the existing fill styles can now be used to style annotation frames.

また、ペイント効果とデータ定義のシンボルパラメータ。

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### 機能：ポイントクラスターレンダラー
近くのポイントを1つのレンダリングされたマーカーシンボルにグループ化する新しいシンボルレンダラー。必要に応じて、ラベルに1つのシンボルに集約された地物の数が表示されます。

さらに、点変位レンダラーのいくつかの改良がなされました。具体的には次のとおりです。
- points are now assigned to the group which is \"nearest\" them, rather then just assigning them first group within the search distance. In some cases this was assigning features to a more distant cluster, resulting in less predictable cluster patterns
- 個々のポイントがそれぞれの選択状態で正しく表示されるようになりました
- 多くのコードクリーンアップ+ドキュメンテーション。

開発者向け：QgsPointDisplacementRendererは、クラスターの検出とポイントのグループ化を処理する新しい純粋な仮想QgsPointDistanceRenderer基本クラスに分割されています。新しいクラスターレンダラーは、コードの重複を避けるためにこの基本クラスを再利用します。

See the crowd [funding programme](https://north-road.com/qgis-cluster-renderer-crowdfunding/) for more details.

![image78](images/entries/a9a26b2c7154f918f8b218c2e01f3b38f599436a.png.400x300_q85_crop.webp)

この機能は、Andreas Neumann、Qtibia Engineering（Tudor Barascu）、Karl-MagnusJönsson、Geonesia（Nicolas Ponzo）、そして多数の匿名の後援者によって資金提供されました。

This feature was developed by [Nyall Dawson](https://north-road.com/qgis-cluster-renderer-crowdfunding/)
### 機能：QGIS 3.0の新しい地図彩色アルゴリズム
see <http://nyalldawson.net/2017/02/new-map-coloring-algorithms-in-qgis-3-0/>

![image79](images/entries/1a507363f0c35065d8c2751e167531b96600d700.png.400x300_q85_crop.webp)

この機能はNyall Dawsonによって開発されました
### Feature: New \"preset\" colors color ramp option
Allows use of a color ramp consisting of a list of selected colors. Currently there\'s no way in QGIS to classify a renderer using some list of colors you\'ve previously selected. So you can modify the colors manually after classifying, but that\'s a pain if you\'re regularly using the same color scheme. Basically, it\'s like the color brewer color ramp options but allowing users to pick their own preset list of colors to use (Because Cynthia Brewer isn\'t the only cartographic color expert!)

![image80](images/entries/ea1e2fe7215ea888b9de00329e230f6b665610a6.png.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### 機能：シンボルレイヤーを一時的に無効にする　
Adds a new checkbox at the bottom of each symbol layer\'s properties which allows you to control whether the layer is enabled or not. Disabled layers are not drawn, but are saved and can be enabled at a later stage. This makes it easier to tweak symbol appearance without having to totally delete a symbol layer.

![image81](images/entries/555204a38e13852e4717179a9981cb522244613a.png.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### 機能：離散ラスターの簡単なスタイル設定
In QGIS 3.0, the existing raster Paletted Renderer for rasters was adapted to allow for easy styling of discrete raster layers, such as landcover or boolean rasters. Now, users can select the renamed \"Paletted/Unique Values\" renderer and click the \"Add Unique Values\" button to load all unique raster values from the layer. These are automatically assigned a color using the selected color ramp.

ユニークな値の計算は、バックグラウンドスレッドで実行され、大規模な（またはリモートの）ラスターレイヤーに対応するUIを維持します。さらに、ユーザーは必要に応じて個々の新しいクラスを手動で追加し、既存のクラスの関連ピクセル値を編集できます。一度に複数のクラスを削除することもできます。同時に複数のクラスの色、透明度、ラベルを変更することもできます。　

カラーパレットは、ESRI clr / GDAL / GRASSカラーテーブル形式をサポートしたテキストファイルからロードできます。カラーパレットは、共有のためにclrテキストファイルに保存することができます。　

![image82](images/entries/536a7bce4d526e2d5fbeeb3189de6f60b2d79256.png.400x300_q85_crop.webp)

This feature was funded by Stéphane Henriod, Satelligence (<http://satelligence.com/>), Bird\'s Eye View (<https://www.birdseyeviewgis.com/>), other anonymous backers

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## ラベリング
### 機能：ラベルのフォントサイズをmm / pixels単位で許可する
This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### 機能：カスタムラベルツールバーが常に有効になりました
Thanks to the awesome **auxiliary data storage** and the editable joined table, the manual label customization is now always enabled. You do not need anymore to add dedicated fields in your datasource to change labels position, rotation, or any of the possible settings for labels to activate the toolbar. **No more copy of readonly datasources and so much faster labeling !** **Be warned**, labels are **only saved along with your project file** in a .qgd sqlite database, or inside the .qgz zipped project file if you chose that format. Don\'t forget to share that .qgd file if you want to share your project file.

And for power users, the old way of having data defined fields in your datasource is still there. Just define them in the layer\'s properties as before!

![image83](images/entries/546a77b230bf9b0b28bf61bb231b78cbb6bd5b5f.png.400x300_q85_crop.webp)

This feature was funded by [French ministry of Ecology and Sustainable Developpement](https://www.ecologique-solidaire.gouv.fr/)

This feature was developed by [OSLANDIA - Paul Blottiere](https://github.com/pblottiere)
## ダイアグラム
### 機能：データで定義されたプロパティ
より多くのデータ定義可能なプロパティのサポートをダイアグラムに追加する：
- 距離
- 優先度
- ZIndex
- IsObstacle
- Show
- AlwaysShow
- Diagram Start Angle

この機能は、QGISグラントプログラム によって資金提供されました

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
## レンダリング
### 機能：ライブレイヤーのサポート
QGIS 3.0はライブレイヤーをサポートするようになりました。これらのレイヤーは、決まった時間間隔で自動的に再レン​​ダリングされ、きれいでちらつきのない方法で再描画されます。ライブレイヤーは、車の艦隊、テレメトリデータを持っている鳥の群など、連続的に変化するデータを追跡するのに最適です。　

![image84](images/entries/5a9cd3df6f804b903fee30a08f7018887c1d8710.gif)

この機能はKartoza＆North Roadによって開発されました
### 機能：PostgreSQLのNOTIFYシグナルからレイヤー更新またはレイヤーアクションをトリガする
ライブレイヤー効果に続いて、QGISでQGISに通知する場合にのみ、QGISでアクションまたはレイヤーの更新をトリガすることができます。それは間隔で更新するよりも少ないリソースを必要とし、QGISでチャットアプリケーションをコード化することさえできます:)

See <https://vimeo.com/236604742>

<http://oslandia.com/en/2017/10/07/refresh-your-maps-from-postgresql/>

This feature was funded by [QGIS.org Grant application](https://qgis.org)

This feature was developed by [OSLANDIA - Vincent Mora](https://github.com/vmora)
### 機能：キャンバスを更新するときに不要な再描画を避けるためラベル付け結果をキャッシュ
この変更により、地図レンダリング後の画像にラベル付け結果をキャッシュすることができます。キャッシュされたラベルの結果画像を次のレンダリングで再利用できる場合は、ラベル付けの問題に関与するすべてのレイヤーを再描画し、ラベル付けソリューションを解決する必要はありません。基本的には、これは、 **非ラベルレイヤーへの変更の結果としてのキャンバス更新がずっと速くなる** ことを意味します。（ラベル付けソリューションの一部であるレイヤーを変更するには、すべてのラベル付きレイヤーを完全に再描画する必要があります）

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### 機能：点の移動のためのグリッドレンダラー
ポイント移動のグリッドレンダラー

![image85](images/entries/0247dfa555b6a80139f399b69071a2cc9bd278b3.png.400x300_q85_crop.webp)

This feature was developed by [Muhammad Yarjuna Rohmat (Kartoza)](http://www.kartoza.com)
## デジタイズ
### 機能：ノードツールの範囲頂点選択
この機能により、ある地物から **範囲の頂点** を選択できます。

**Shift + R** を押すとアクティブになります。その後、地物内の開始点と最終点をクリックする必要があります。これにより、2つの間のすべての頂点が選択されます。

範囲の選択は、右クリックまたはEscキーを押すことによっていつでもキャンセルできます。

For closed curves (polygons), it is possible to switch to the \"longer\" way around the ring by holding **Ctrl** while clicking the final point.

![image86](images/entries/b44524fe2864249a334cb7d21fd1a0c1d885ff15.gif)

This feature was funded by [French ministry in charge of ecology](https://www.ecologique-solidaire.gouv.fr/)

This feature was developed by [Martin Dobias (Lutra Consulting)](http://www.lutraconsulting.co.uk)
### 機能：デフォルトのZ値オプションを追加する
ジオパッケージ/シェイプファイルを作成する：Z値を持つオプションが追加されました

![image87](images/entries/80e8c78a1b38dfde5120144fac7354e800b9daff.png.400x300_q85_crop.webp)

この機能はAlexander Lisovenko / Paul Blottiereによって開発されました
### 機能：地物移動はアドバンストデジタル化のメリットを受けます
Just move a feature using the new \"click - click ergonomy\" and use the advanced digitizing panel and shortcut to constraint angles, distances, exact XY.

この機能は、Denis Rouzaud
### 機能: 地物を地物移動マップツールに複製/移動する機能の追加
これにより、選択した地物から地物を複製して一度に移動できます

![image88](images/entries/eea327329365ad80c7fc3363ad0fb455fc9d4335.png.400x300_q85_crop.webp)

この機能は、Denis Rouzaud
### 機能：オフセット付きトレース
添付の画像に示されているように、オフセット付きのトレースデジタイジングツールを使用できるようになりました。

![image89](images/entries/974604dc8908668c2d727e12975707560cffb493.gif)

This feature was funded by [d.b.g. Datenbankgesellschaft mbH](http://www.datenbankgesellschaft.de/)

This feature was developed by [Martin Dobias](http://www.lutraconsulting.co.uk)
### 機能：頂点ツールのオーバーホール
ノードツール（現在は頂点ツールに名前を変更）は、柔軟性を高めるために完全なリワークを経ています。より重要な変更のいくつかは次のとおりです。
1. ユーザーが最初に地物を選択してから2番目のステップで頂点を編集するように要求するのではなく、複数の地物を同時に処理できるようになりました。したがって、複数の地物から頂点を選択して一度に移動または削除することは簡単です。特定の地物だけに頂点の選択を制限する必要がある場合、選択ツールで地物を最初に選択できます。頂点ツールは、そのような場合に選択された地物の頂点でのみ機能します。
2. 現在選択されているレイヤーで作業するのではなく、編集モードにあるすべてのレイヤーで同時に作業できます。論理的には属しているが、異なるレイヤーにある地物の移動はずっと簡単です。それでも、頂点を選択するときに複数の選択肢がある場合、現在のレイヤーは尊重されます。
3. ユーザーがマウスポインタを上に移動すると、地物とその頂点が強調表示され、視覚的なフィードバックが向上します。
4. In QGIS 2.x the vertices would be moved by clicking a vertex, dragging it with the left mouse button still pressed and finally dropping them by releasing the mouse button. This behavior has been changed to \"click-click\" approach where user first clicks a vertex to pick it, then drag it without having any mouse buttons pressed and drop it by clicking again on the final destination. The arguments for this change were the following:
5. ノードを正確に配置する方が簡単です（マウスボタンに常に力を加える必要はありません）
6. ノードを誤って移動しません
7. 操作をキャンセルできます
8. ノードが移動されている間にスペースバーを押して地図をパンすることができます

See <https://github.com/qgis/QGIS-Enhancement-Proposals/issues/69> for more information.

![image90](images/entries/c2761555d13be6b8a1893da2bd3240dd6343c9a6.gif)

This feature was funded by [QWAT](http://qwat.org/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### 機能：頂点ツール：頂点を追加するための中間点マーカー
改良された頂点ツールは、地物の線分の中間点に余分なマーカーを表示するようになりました。このようなマーカーをクリックすると、新しい頂点が追加されます。セグメントをダブルクリックして頂点を追加する既存の方法は維持されています。

![image91](images/entries/b47f105d5ea3ecf5176a8296cc386c65bce21da7.gif)

This feature was funded by [QWAT](http://qwat.org/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### 機能：頂点ツール：ラインを続ける
頂点ツールを使用して線ストリングのジオメトリを編集する場合、マウスを最初または最後の頂点の方に移動すると、端点のすぐ隣に余分なマーカーが表示されます。マーカーをクリックすると、ジオメトリの最後に頂点が追加されます。

![image92](images/entries/b355e0701d6b395d25a965cc7d31b9f8acce49d7.gif)

This feature was funded by [QWAT](http://qwat.org/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### 機能：頂点ツール：高度なデジタイジングパネルのサポート
高度なデジタイジングパネルは、頂点ツールでも機能するようになりました。他の［デジタイジング］地図ツールと同様に、新しい頂点または既存の頂点の座標をパネルに入力することができます。

![image93](images/entries/297f18356a626066332b4c28e13ce4c94bb70166.gif)

This feature was funded by [QWAT](http://qwat.org/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
## データ管理
### 機能：属性テーブルの現在の地物にパンする
![image94](images/entries/2f488f086cb64fb0394d1848b4a41f28f80a2adf.gif)

この機能はMarco Hugentoblerによって開発されました
### 機能：プロジェクトプロパティのCRS範囲の地図
![image95](images/entries/d56d5d68aff5b7f10999751041490769b79e619d.png.400x300_q85_crop.webp)
### 機能: 補助ストレージ機能
補助記憶域を管理するために、ベクターレイヤプロパティで新しいタブを使用できます。

新しいアクション *プロジェクト内のデータをストアする* が、データ定義メニューで、プロパティの補助データを簡単に管理する方法が提供されています。

補助データはsqliteデータベースに格納され、データベースファイルを可能な限り小さく保つために、（spatialiteプロバイダの代わりに）OGRデータプロバイダのおかげで管理されます。このデータベースファイル（拡張子 *.qgd* ）は、プロジェクトファイルのすぐ隣に保存されるか、新しい *.qgz* 形式で直接埋め込まれます。

See the original [pull request](https://github.com/qgis/QGIS/pull/5086) and this article [which explains more](http://oslandia.com/en/2017/10/17/auxiliary-storage-support-in-qgis-3/)

![image96](images/entries/f0fded6f5276d4b7e51b11834bad3d615e2b4f2d.png.400x300_q85_crop.webp)

This feature was developed by [Paul Blottiere / Oslandia](http://oslandia.com/)
### 機能：メタデータのオーバーホール
QGISのメタデータシステムは、オーバーホールされました。QGIS 3.0では、QGISプロジェクトファイル形式とは別に独自の内部的なフォーマル化メタデータスキーマを導入しています。レイヤーのメタデータを読み書きするための新しいAPI機能を紹介します。メタデータの表示を編集から切り離し、新しいメタデータ編集ツールを追加しました。メタデータは現在プロジェクトファイルに保存されています。ファイルベースのレイヤーの横にXMLファイルとして保存することも、リモートレイヤーのためにローカルのsqliteデータベースに保存することもできます（PostGISなど）。

you can read more about the design considerations adopted in this work by referring to the QGIS Enhancement Proposal (QEP) - [QEP-92](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/91)

Please note this is the first phase in the development of a complete and standards compliant metadata infrastructure for QGIS. We are seeking further funding to implement a more complete implementation for the metadata system - see [this document](https://docs.google.com/document/d/1twE8J345Sz1rk1z34672eqlEiL2mJT4bZbuF5oRTCoM/edit?usp=sharing) for details of future planned work packages that need funding.

The specification for the QGIS metadata schema is [here](https://github.com/qgis/QGIS/blob/master/resources/qgis-resource-metadata.xsd).

The primary funder for this work was [The WorldBank/GFDRR](https://www.gfdrr.org) with supporting funding provided by [NINA](https://www.nina.no/english).

![image97](images/entries/a26adc99ea62733e65222769095537e3be3fb29a.png.400x300_q85_crop.webp)

This feature was funded by [WorldBank/GFDRR](http://gfdrr.org)

This feature was developed by [Kartoza and collaborators](http://kartoza.com)
### 機能：統合データソースマネージャダイアログ
データソースの管理とレイヤーの読み込みを処理する単一の統一されたダイアログ。

![image98](images/entries/3d6a40ee709ca4f18d8532291f3cbc97997f1932.gif)

この機能は、Boundlessによって資金提供されました

This feature was developed by [Alessandro Pasotti](https://www.itopen.it)
### 機能：OSM Downloaderツールが削除されました
QGIS 2.Xリリースで提供されていたOSMダウンローダツールは削除されています。QGIS 3.0に移植されたQuickOSMプラグインの利用をお勧めします。
## フォームとウィジェット
### 機能：個々の編集ウィジェットのラベルを制御できるようにする
ドラッグアンドドロップデザイナーでは、項目をダブルクリックすると、各項目ごとにラベルを個別に表示するかどうかを制御できます。

この機能はMatthias Kuhnによって開発されました
### 機能：リレーションエディタウィジェットのリンク/リンク解除機能ボタンの設定を許可する
この機能はMatthias Kuhnによって開発されました
### 機能：タブとグループボックスの条件付き可視性
これにより、タブとグループボックスをドラッグアンドドロップデザイナーフォームで条件付きで表示または非表示にするための新しい設定オプションが追加されました。設定は、フィールドコンフィグレーションインターフェイスのデザイナツリーでダブルクリックして行います。可視性を制御する式を入力できます。この式は、フォームの変更時に毎回値が再評価され、それに応じて表示/非表示のタブまたはグループボックスが再評価されます。

この機能はMatthias Kuhnによって開発されました
### 機能：スマートなデフォルトの編集ウィジェットをプラグインで選択
今では、ウィジェットはフィールドのタイプをどれほどうまく扱うことができるかのスコアを与えることができます。優れたデフォルトウィジェットに導く

さらに、プラグインを追加して外部情報の機能でウィジェットタイプを選択することもできます。そのうちの1つはPostgreSQLのテーブルを使用し、各フィールドに使用するウィジェットのタイプと設定を指定できます。

外部キーのRelationReferenceウィジェットを自動的に選択します。

この機能はPatrick Valsecchiによって開発されました
### 機能：フィールドの制約を適用するかどうか
強制されない制約は、ユーザーに警告を表示するだけですが、機能のコミットを妨げません。強制制約は、ユーザーが非準拠の機能をコミットするのをブロックします。だから我々は今や柔らかい警告を持っている！プロバイダによって検出された制約は常に強制されます。

![image99](images/entries/da468dc209eb7e7da3696ee26850af6b9017312c.png.400x300_q85_crop.webp)

この機能はOpenGIS.chによって資金提供されました

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### 機能：レイヤースコープのアクションを追加する
属性テーブル内には、個々の機能に基づいてではなく、レイヤー全体でアクションをトリガーする新しいボタンがあります。通常、すべての機能や選択に基づいてアクションを実行します。

この機能はMatthias Kuhnによって開発されました
### 機能：フォームフィルターモードでフィールド値をオートコンプリートで表示する
The autocompleter is nicely updated in the background so that the gui remains nice and responsive, even if there\'s millions of records in the associated table.

It\'s now used as a search widget for text fields, so can be seen in the browser window if you set the filter to a text field, or if you launch the form based select/filter by selecting a layer and pressing F3.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### 機能：機能にズームを追加し、フォームの選択ダイアログでショートカットをフラッシュする
フォーム内の基準に一致する機能の非常に迅速なナビゲーションと識別を可能にする

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### 機能：フォームの選択範囲内の数値フィールドの間に/間に追加
![image100](images/entries/4bfb34794edbff35e6336c165993278e9a515644.jpeg.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
## レイヤ凡例
### 機能：選択解除されたレイヤーを非表示にする
すべての選択解除されたレイヤーを素早く非表示にすることができます。これは非常に便利です。大規模なプロジェクトがあり、いくつかのレイヤーを除いてすべてをすばやく隠したい場合に便利です

![image101](images/entries/a8419d6027de9351afa6f8a99700509b24cc7418.png.400x300_q85_crop.webp)

This feature was funded by [SMEC (Surbana Jurong)](http://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### 機能：グループ内のレイヤーの可視性の人間工学的変化
- Checking/unchecking a group doesn\'t change the check state of its children. A node is visible if and only if it is checked and all its parents too.
- あるグループには半チェック状態がありません
- チェックされていないグループの **Ctrl+クリック** はグループとそのすべての子孫をチェックします。
- チェックされていないレイヤーのクリックはラガーとその親をすべてチェックします。
- チェックされたグループのCtrl +クリックは、グループとそのすべての子孫のチェックを外します。
- チェックされたレイヤーのCtrl +クリックは、レイヤーとそのすべての親のチェックを外します。
- これらのアクションは、ツリービューのコンテキストメニュー項目で使用できます。
- 彼らまたはその親がチェックされていないので、目に見えないレイヤーはグレー表示されます。

この機能はEven Rouaultによって開発されました
## マップコンポーザー
### 機能：コンポーザーテーブルグリッドの水平線と垂直線の描画を制御
これで、コンポーザテーブル項目の水平線と垂直線のレンダリングを独立して制御することが可能になりました。この追加された柔軟性は、このアイテムのスタイリングの可能性をQGIS内で直接費やします。

![image102](images/entries/ac1b2079c9e6c19747322d246d666df7e3c4ac0d.jpg.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### 機能：qptをQGISにドラッグしてテンプレートから新しいコンポーザを作成する
This feature was funded by [SMEC (Surbana Jurong)](http://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### 機能：コンポーザーの凡例項目ラベルの行間隔のカスタマイズを可能にする
This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### 機能：地図アイテムにCRSを選択できるようにする
これにより、地図項目のCRSがキャンバス/プロジェクトCRSと異なることができます。また、異なる地図アイテムが異なるCRSを持つこともできます。たとえば、概要地図を主地図とは異なるCRSに設定できます。

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### 機能：描画中にシフトを保持ポリライン/ポリゴンが線の角度を制限する
This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### 機能：より多くのデータ定義可能なコントロール
アイテム **フレーム** および **背景色**  データ定義 **コンポーザのピクチャアイテムのsvgの色とアウトラインの幅** （特に画像に北の矢印が表示されている場合に便利です）データ定義 **凡例のタイトルと列数** データ定義 **スケールバーの色と線幅**

この機能は、QGISグラントプログラム によって資金提供されました

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### 機能：Map Composerオーバーホール
これは、QGISのコードでコンポジションがどのように管理されるかを大きく変更したものです。

ハイライトは：
- コンポジションの保存とシリアライズ/デシリアライズに使用される新しいQgsLayoutManagerクラス。QgsLayoutManagerはQgsProjectに添付されています。これにより、コアコードはプロジェクトに添付されたコンポジションにアクセスできます。すべてのコンポジットの処理がアプリからコアに移りました。これにより、サーバ（および他のアプリではないアプリケーションのQField / roam？）が、脆弱なxml解析に頼らずにプロジェクト構成に簡単にアクセスできます。
- コンポーザウィンドウはオンデマンドで作成され、クローズ時に破棄されます。これにより、プロジェクトをロードするときに、すべてのコンポーザー項目のすべてのコンポーザーウィンドウとウィジェットを作成する必要がありません。 **これは、以前は構成が遅かったプロジェクトをロードする主な理由でした** 。現在、コンポーザウィンドウは、ウィンドウが開いているときにのみ作成され、ウィンドウが閉じられると破棄されます。コンポーザアイテム設定ウィジェットは、すべてのウィジェットを事前作成するのではなく、オンデマンド（アイテムが選択されている場合）でのみ作成されます。
- 終了時にコンポーザウィンドウを破壊することの副次的な利点は、コンポーザウィンドウでフローティングドックの使用をブロックしたQtバグ**に悩まされなくなったことです。これでitem / composition / etcパネルをフロートさせることができます！マルチモニター設定でのコンポジションでフルスクリーンで作業する方がはるかに優れています。　
- **Reworked API for working with composers through iface**. Since composer windows don\'t exist unless they are currently open, all the iface methods for interacting with composers have been redone to make it clear that they only apply to open windows. Additionally, a simple composer interface which provides a stable API for plugins and scripts to work with composer windows has been added. Very basic for now, but in future we can extend with more hooks to allow plugins to interact with composer windows.
- たくさんのコードのクリーンアップと削除

More info at <https://north-road.com/qgis-layout-and-reporting-engine-campaign/>

![image103](images/entries/fa298be4fea348f58b9bd2f4bea30f2e7f1c2ee5.png.400x300_q85_crop.webp)

この機能は、スイスのQGISユーザーグループが資金提供しました。

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## 分析ツール
### 機能：プロセッシングのためのラスター独自の値のカウント
<http://imhere-asia.com/blog/post/qgis-raster-layer-unique-values-count>

This feature was developed by <http://imhere-asia.com/>
## プロセシング
### 機能：ラインをオフセットする新しいアルゴリズム
This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### 機能：片面バッファ用の新しいアルゴリズム
This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### 機能：簡単化のための簡略化方法の選択肢を追加
この変更により、既存の距離ベース（Douglas Peucker）アルゴリズム、領域ベース（Visvalingam）アルゴリズム、およびグリッドにスナップするアルゴリズムの選択肢を使用して、単純化ジオメトリアルゴリズムの実行時に使用する方法を選択できます。

Visvigigamは、通常、標準的な距離に基づく方法よりも、より地図的に楽しい単純化をもたらす。

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### 機能：モデルでの出力ジオメトリタイプのサポート
モデルの子アルゴリズムの入力は、他の子アルゴリズムへの入力に対して適用可能なジオメトリタイプを生成するモデルにのみフィルタリングされるようになりました

この機能はAlexander Bruyによって開発されました
### 機能：滑らかなアルゴリズムのための角度閾値
QgsGeometry :: smoothにオプションを追加して、特定のしきい値よりも短いセグメントまたはしきい値を超える角度を持つ鋭いコーナーを滑らかにしない

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### 機能：Z / M寸法と曲線形状のより良いサポート
より多くのアルゴリズムがZ / M値を尊重し、この情報を破棄せず、多くのアルゴリズムがこれらのジオメトリを強制的にセグメント化せずにカーブしたジオメトリを正しく維持するようになりました。
### 機能：プロセシングに追加されたラスター解析アルゴリズム
「ラスター分析」プラグインからプロセッシングに次のアルゴリズムが追加されました。
- アスペクト
- 傾斜
- 粗度
- 陰影図
- レリーフ

これらのアルゴリズムはスクリプト、モデル、およびバッチ処理に使用できます。

![image104](images/entries/f5980f4840b9c822e5a228ec03da59168cd9c5e9.png.400x300_q85_crop.webp)

この機能はAlexander Bruyによって開発されました
### 機能：特定のノードを抽出する新しいアルゴリズム
このアルゴリズムを使用すると、ジオメトリから特定のノードを抽出できます。たとえば、ジオメトリの最初または最後のノードを抽出できます。

このアルゴリズムは、抽出するノードインデックスのコンマ区切りリストを受け入れます。たとえば、0 =最初のノード、1 = 2番目のノードなどです。負のインデックスを使用して、ジオメトリの最後からノードを抽出できます。例えば、-1 =最後のノード、-2 = 2番目の最後のノード。

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### 機能: ツールボックスのゾーン統計プラグインからのゾーン統計の公開
この機能はAlexander Bruyによって開発されました
### 機能: SpatiLiteのSQL実行アルゴリズムの追加
この機能はMathieu Pellerinによって開発されました
### 機能：ラインを拡張する新しいアルゴリズム
ラインの始点と終点の設定距離だけラインストリングを延長できます

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### 機能：表現アルゴリズムによる新しい抽出
入力レイヤーを式でフィルタリングする

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### 機能: SpatiLiteのSQL実行アルゴリズムの追加
この機能はMathieu Pellerinによって開発されました
### 機能：補間アルゴリズム
ツールボックスのInterpolationプラグインからIDWとTIN補間を公開する

補間プラグインが削除されました

この機能はAlexander Bruyによって開発されました
### 機能：式でジオメトリを計算する新しいアルゴリズム
このアルゴリズムは、QGIS式を使用して入力地物の既存のジオメトリを更新（または新しいジオメトリを作成）します。これにより、QGIS式エンジンのすべての柔軟性を利用して出力地物のジオメトリを操作および作成できる複雑なジオメトリの変更が可能になります。

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### 機能：レイヤーアルゴリズムにスナップジオメトリ
ジオメトリスナッパープラグインをプロセッシングに移植する

スナップジオメトリアルゴリズムを使用すると、他のレイヤータイプにスナップすることができ、ポイント/ラインレイヤーをサポートします

Snap to layer algorithm accepts a mode parameter. With a new option to prefer to snap to closest point on geometry. The old behaviour was to prefer to snap to nodes, even if a node was further from the input geometry than a segment. The new option allows you to snap geometries to the closest point, regardless of whether it\'s a node or segment.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### 機能：式の新しい入力タイプ
これは、式入力のための新しい入力タイプを追加します。式の入力は、ビルダーが正しいフィールドとレイヤー変数を表示できるように、親レイヤーにリンクできます。

It\'s designed to be used when an algorithm specifically requires an expression, eg Select by Expression and Extract by Expression.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### 機能：SplitWithLines
アルゴリズムの名前を変更するSplitLinesWithLinesをSplitWithLinesにするポリゴンも入力として受け入れる選択する線のみを使用する（プロセッシングが選択のみを使用するように設定されている場合）マルチジオメトリを分割しようとするとログメッセージが表示されるヘルプの更新

この機能はBernhardStröblによって開発されました
### 機能: 到達不能極アルゴリズム
Implements a processing algorithm to calculate the pole of inaccessibility for a surface, which is the most distant internal point from the boundary of the surface. This function uses the \'polylabel\' algorithm (Vladimir Agafonkin, 2016), which is an iterative approach guaranteed to find the true pole of inaccessibility within a specified tolerance. More precise tolerances require more iterations and will take longer to calculate.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### 機能：属性別に抽出するとnull / notnull値を抽出できます
属性値がnullまたはnullでない場合のフィルタリングのサポートを追加します。

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### 機能：属性インデックスアルゴリズムを作成する
より速い属性ベースのフィルタリングのために、レイヤー内の属性にインデックスを作成できるようにする

サポートは、レイヤーの基礎となるデータプロバイダに依存します

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: New \'drop geometries\' algorithm
入力レイヤーから任意のジオメトリを削除し、属性のみの地物を返します

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: New universal \'basic stats for field\' algorithm
Replaces the existing \'Basic Stats for Numeric Fields\' and \'Basic Stats for String Fields\' algorithms and adds support for date/time/datetime fields.

統合された単一のアルゴリズムを持つことにより、フィールドタイプが事前に分からない場合のより柔軟なモデルが可能になります。

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### 機能：ポートヒートマッププラグインから処理アルゴリズム
This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### 機能：ジオメトリを直交化するための新しいアルゴリズム
Adds a new algorithm which tries to make angles in geometries either right angles or straight lines

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### 機能：ネットワーク解析アルゴリズム
最短経路とサービスエリアアルゴリズムを処理に追加する

あるポイントからあるレイヤー内のすべてのポイントまで、またはレイヤー内のすべてのポイントから最短ポイントまでの最短パスも計算できます。また、レイヤー内のすべてのポイントのサービスエリアを作成します。

その結果、Roadgraphプラグインが削除されました。

この機能はAlexander Bruyによって開発されました
### 機能：PDF / SVGとしての処理モデルのエクスポート
処理モデルをビットマップ画像としてエクスポートするだけでなく、処理モデルを解像度に依存しないPDFやSVGとしてエクスポートすることも可能になりました。これにより、出版される論文や書籍に埋め込まれるモデルの高解像度の書き出しが可能になります。

![image105](images/entries/0ad81df99f01b91d2421263ad35fdc4430c483e0.jpg.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### 機能：テーブルを切り詰める新しいアルゴリズム
Irretrievably deletes all features from a table\... use with caution!

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: Added 'invalid feature handling' option
この機能はVictor Olayaによって開発されました
### 機能: ネイティブのmakeValid()実装を使用した不正なジオメトリを訂正するアルゴリズム
この機能はAlexander Bruyによって開発されました
### 機能: スクリプトのモデルの取得ダイアログへの検索の追加
この機能はAlexander Bruyによって開発されました
### 機能：一般重心アルゴリズム
非ポリゴンレイヤーを扱うリワーク重心アルゴリズム

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### 機能: ノード抽出アルゴリズムの改善
ノード抽出アルゴリズムは、ノードのインデックス、ノードに沿った線と角度に沿った距離を保存するようになりました

この機能はAndreas Neumannによって資金提供されました

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### 機能：ポイントを移動（移動）するための新しいアルゴリズム
ジオメトリをax / y変位だけずらすことができます

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### 機能：改良された処理モデラーウィンドウ
The processing modeler window has received a lot of attention for this release. Improvements include: - zoom controls in the window\'s toolbar - customization of inputs and algorithms panels\' location - panels can now float above the processing window

![image106](images/entries/d7d74d9113516f51289380755f1862324c83feb5.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### 機能：新しいラスター独自の値レポートアルゴリズム
指定されたラスターレイヤー内の各固有値の数と面積を返す処理に新しいアルゴリズムが追加されました。

![image107](images/entries/096af77b050265c85d7ee203c2ab4d974b8be126.jpg.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### 機能: コア処理からのTauDEMプロバイダの削除
処理からTauDEMプロバイダを削除しました。

![image108](images/entries/c48a25965a147b866502d10771bea3e831a4d28e.jpeg.400x300_q85_crop.webp)
### 機能：処理からファイルをダウンロードする
処理からファイルをダウンロードします。geojsonを取得するリモートAPIを照会する

This feature was developed by [Etienne Trimaille](https://github.com/Gustry)
### 機能：ジオメトリアルゴリズムに沿って最適化されたポイント
ポリゴンジオメトリをサポートし、ヌルジオメトリを処理し、元の線の角度と各点の距離を記録します。

![image109](images/entries/9b24dc337e4896a8be9b0e651e32b3dc9cb11593.png.400x300_q85_crop.webp)

この機能はAndreas Neumannによって資金提供されました

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### 機能：式アルゴリズムによる並べ替え
This feature was funded by [DFAT/DMI](http://dfat.gov.au/pages/default.aspx)

This feature was developed by [Etienne Trimaille (Kartoza)](http://www.kartoza.com)
## アプリケーションとプロジェクトのオプション
### 機能：新しいzip形式のプロジェクトファイル形式.qgz
A long time ago on the developper\'s mailing list, we discussed of a container storing the xml file and other ressources. This is now possible, though it remains optional. The auxiliary storage feature takes advantage of that by storing the associated .qgd sqlite database. We hope that in next versions land support for embedding other resources like SVG, color ramps, datasources, images, etc\...

![image110](images/entries/b954811defffce51a7375ae24c640e0d1dcf88da.png.400x300_q85_crop.webp)

This feature was funded by [French ministry of Ecology and Sustainable Developpement](https://www.ecologique-solidaire.gouv.fr/)

This feature was developed by [OSLANDIA - Paul Blottiere](https://github.com/pblottiere)
### 機能：ユーザープロファイルのサポートを追加する
すべてのユーザー設定/プラグインなどは、各プラットフォームのアプリケーションデータの場所からロードされ、.qgis3 / 2ではなくなりました。各プロファイルの設定とプラグインは、互いに分離されています。

これにより、テスト、プロード、デモなど、ユーザが必要とするものに応じて異なる実行時設定が可能になります。

プロファイルメニューでは、プロファイルの切り替えや新しいプロファイルの作成が可能です。

![image111](images/entries/82d90b2a02b84584279b5e2b75774631a0cd4a44.jpeg.400x300_q85_crop.webp)

This feature was developed by [Nathan Woodrow](https://github.com/NathanW2)
## ブラウザ
### Feature: Drag\'n\'drop layers from layer tree view to browser dock
簡単に、例えば一時的なレイヤーをPostGISに保存できます。

この機能はMartin Dobiasによって開発されました
### 機能：スタンドアロンのQGISブラウザアプリケーションが削除されました
QGIS 2.xに同梱されているスタンドアロンのQGISブラウザアプリケーションを削除しました。このアプリケーションはユーザーの受け入れが貧弱で、3.0コードベースで継続したくないメンテナンスオーバーヘッドを表していました。
## データプロバイダ
### Feature: New unified \'add layer\' dialog
単一のダイアログを使用して、多種多様なデータ形式をQGISに追加できるようになりました。

![image114](images/entries/d81a5fba0df198b53ef60293ade556125499e5e8.png.400x300_q85_crop.webp)

This feature was developed by [Alessandro Pasotti](https://www.itopen.it)
### 機能：ジオパッケージ
- 処理はデフォルトでpkgを使用します
- save asはデフォルトでpkgを使用します
- 新しいレイヤーを作成するとデフォルトでpkgが使用されます
- ブラウザのドラッグアンドドロップインポートレイヤー

この機能はAlessandro Pasottiが開発しました
### Feature: Support all GDAL writable raster formats for \'Save as\' dialog on raster layers
この機能はNyall Dawsonによって開発されました
### 機能：gpkg、spatialiteおよびメモリレイヤープロバイダにおけるZ / Mジオメトリのサポート
Support for Z dimension and M values was added to QGIS\' gpkg, spatialite and memory layer provider. the option to add Z and M dimensions has also been added to the \"create new layer\" dialogs

![image115](images/entries/63c518b689c749b106944c9d48826abba90887f0.jpg.400x300_q85_crop.webp)

This feature was funded by [QWAT group, http://www.imhere-asia.com/](http://www.qwat.org)

この機能は、 Mathieu Pellerin, Alexander Bury, Paul Blottiereによって開発されました
### 機能：一意と非null制約の処理
postgres、spatialite、ogrプロバイダに実装されたプロバイダ側の一意かつ非null制約の自動検出

クライアント側の一意かつ非NULL制約はQGISで設定できます。

固有の制約は属性形式で適用されます

この機能はOpenGIS.chによって資金提供されました

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### 機能：GeoNodeインテグレーション
[GeoNode](http://geonode.org) is an open source geospatial content management system that makes it easy to publish geospatial data on the web. QGIS 3.0 includes new functionality that will allow you to very easily add a GeoNode instance to the browser tree and add any layers from that site to your project as WMS, WFS or XYZ. There is no need to dig around trying to figure out WMS/WFS end points, QGIS will do everything for you. When using WMS and XYZ Tiled layers, the style of the published GeoNode layer will be used.

GeoNodeインスタンスがGeoServerバックエンドではなくQGISサーバーバックエンドを使用する場合は、サーバーからスタイルをコピー＆ペーストしてローカルレイヤーに適用することで、WFSレイヤーがサーバー上のものと正確にレンダリングされます（アニメーションここにGIF）。

There are also python bindings so that you can add GeoServer layers to QGIS from your plugins. If you are interested in running your own GeoNode with QGIS Server backend please see [this site](https://github.com/kartoza/kartoza-rancher-catalogue/blob/master/README.md) for details on how you can do that using docker and rancher.

![image116](images/entries/8f23a63a25a4ad14c8a35ccf52029aa8f8c96379.gif)

This feature was funded by [WorldBank/GFDRR](https://www.gfdrr.org)

This feature was developed by [Kartoza](http://kartoza.com)
### 機能：spatialiteプロバイダーのリテラルのデフォルト値を検出する
This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### 機能：spatialiteプロバイダのアトリビュートインデックスサポートを作成する
spatialiteレイヤーの属性インデックスの作成を可能にする

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### 機能：配列のサポートを追加する
Supported by postgres, spatialite

この機能はPatrick Valsecchiによって開発されました
### 機能：PostGISデータプロバイダにおけるHStoreのサポート
### 機能：PostgresQLの関係の自動発見を追加する
この機能はPatrick Valsecchiによって開発されました
### 機能：レイヤー間のデータ依存関係
This allows to declare data dependencies between layers. A data dependency occurs when a data modification in a layer, not by direct user manipulation may modify data of other layers. This is the case for instance when geometry of a layer is updated by a database trigger after modification of another layer\'s geometry.

この機能はHugo Mercierによって開発されました
### 機能：dxf export：サポート再投影
この機能は、Juergen E. Fischer
### 機能：GPKGとSpatialiteのデータベースにスタイルをロード/保存する
この機能はEven Rouaultによって開発されました
### 機能：デフォルト処理の改善
デフォルトの処理（プロバイダーのデフォルトの句、リテラルのデフォルト、QGISの式のデフォルト）を改善し、レイヤーの一意の値の制約を自動的に処理します

一意の値制約を持つフィールドは、そのフィールドに固有の値を持つことが保証されます。

これは、適用可能であれば、特定の編集操作（例えば、コピー・ペースト、地物分割など）後の属性をデフォルト値に設定することも意味します。

この機能は、ZugのCantonとQGEPプロジェクトによって資金提供されました

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
## QGISサーバー
### 機能：QGISサーバーのオーバーホール
As you may know, QGIS is jumping to a new major version (yes!). Doing so was made necessary because of the need to switch to python 3, QT5, but also because we needed to break the QGIS API in several places. (<http://blog.qgis.org/2016/02/10/qgis-3-0-plans/>)

1年前に、スイスの小さなトロルが愛のサーバーコードベースの必要性が強いという鐘を鳴らした。実際、APIはQGISサーバーの古いメソッドによってロックされていました。要するに、QGISサーバーはqgsプロジェクトファイルを独自の方法で再解析し、削除する必要のあるQGISの一部に依存関係を作成しました。

サーバーコードベースのアウトソーシングはオプションではなかったため、リファクタリングする必要がありました。関係者は、フランスのリヨン市でコードビジョンを共有し、ビジョンを共有し、作業を計画し、最終的に次のことをすべて実行することに専念することに決めました。

より高いレベルのリファクタリング

すべてのサービス（WMS GetMap、WFS GetFeature、GetLegendGraphics、WCS、GetPrintなど）が書き直されました。WMSのようなものは完全に書き直されました。デベロッパーへの誇り！

新機能
- デスクトップのようなマルチスレッドレンダリング
- レイヤーメタデータを信頼してプロジェクトの読み込みを高速化する新しいオプション
- WFS 1.1 support <https://github.com/qgis/QGIS/pull/5297>
- サーバーAPI用の完全なPythonバインディング
- プロバイダのようなプラグインとしてのサーバーサービス

深く複雑で未熟な仕事
- すべてのシングルトンコールを削除する
- すべての依存関係を古いQGISプロジェクトファイルパーサーにカットする
- 依存関係をGUIライブラリに最小限に抑えます。マップをレンダリングするにはフォントが必要なので、それらを完全に削除することは実現可能ではありませんでした。

インフラストラクチャタスク
- OGCコンプライアンスプラットフォームを構築し、継続的な統合プラットフォームに統合します。適合報告書がtests.qgis.orgにプッシュされるようになりました。
- Add unit tests \... and again more unit tests
- セキュリティリーク（SQLインジェクションやその他の悪意のある攻撃）に対するQGISサーバーのストレス
- プロファイリングとベンチマーキングのパフォーマンスを開始する。この作品はまだ達成するためにいくつかの愛と資金が必要です

プレゼンテーションはFOSS4G-EUで7月に行われました。

この機能は、QGIS.ORGドナーによって資金提供されました
### 機能：サーバ内の地物情報ジオメトリをセグメント化する可能性
Many web clients can\'t display circular arcs in geometries. To allow such clients to still display a feature\'s geometry (e.g. for highlighting the feature), a new per project QGIS server option was introduced (Menu \"Project\" -\> \"Project Properties\" -\> \"QGIS Server\") to segmentize the geometry before sending it to the client in a GetFeatureInfo response.

![image117](images/entries/c6e36e36b5dc6fb0f5534ef11cb773781db4bf8c.png.400x300_q85_crop.webp)

This feature was funded by [Kanton of Zug](https://geo.zg.ch/)

This feature was developed by [Marco Hugentobler](https://www.sourcepole.ch/)
## プラグイン
### 機能：Plugin Managerから信頼できるステータスを削除する
<https://github.com/qgis/QGIS/pull/5272>
### 機能：オフライン編集：選択した機能のみをコピーするフラグを追加
これにより、オフライン編集の可能性が拡張され、大きなレイヤーのサブセットでしか動作しません

この機能は、DB Fahrwegdienste GmbH によって資金提供されました

この機能はMatthias Kuhnによって開発されました
### 機能：GDALToolsを処理に移動しました
GDALToolsプラグインが削除されました。

GDALToolsプラグインを介して以前に利用可能だったすべての機能は、QGIS処理フレームワークに移動され、スクリプト、モデルでこれらのツールを使用し、バッチプロセスで実行できます。さらに、最新のGDALバージョンで導入された新しいパラメータでアルゴリズムを更新し、作成オプション、NODATA値設定などのいくつかの高度なパラメータを公開することで全体的なUI / UXを改善しました。

![image118](images/entries/ee1c51737225b6dac80a044f272319534fee2832.png.400x300_q85_crop.webp)

この機能はAlexander Bruyによって開発されました
### 機能：ローカルZIPパッケージからのプラグインのインストールを許可する
手動でプラグインをユーザプロファイルディレクトリに解凍することなく、プラグインを手動でインストールする方が簡単になりました。

![image119](images/entries/b0311613cf73564f4dc104772abfab551c391dad.jpg.400x300_q85_crop.webp)

この機能はAlexander Bruyによって開発されました
### 機能：プラグインは、Expressionウィンドウでカスタムヘルプを提供することができます
式を提供しているプラ​​グインは、HTML文字列で作成したカスタムヘルプを追加することができます。

![image120](images/entries/ef610ef1efd507e9bf0ee905d8f8d24a40c753e5.png.400x300_q85_crop.webp)

This feature was funded by [DFAT/DMI](http://dfat.gov.au)

This feature was developed by [Etienne Trimaille (Kartoza)](http://www.kartoza.com)
## プログラム可能
### 機能：ジオメトリクラスの更新
QGISのジオメトリクラスの大幅な見直しが行われました。古いクラスの名前が変更されました（下の表参照）。新しいジオメトリクラスは、ZおよびM属性があればそれを適切に保存します。

References [https://github.com/qgis/qgis3.0\\\_api/issues/11](https://github.com/qgis/qgis3.0\_api/issues/11)

これは最終的に、ジオメトリAPI内の名前付けに一貫した状態を戻します
### 名前の変更
| QGIS 2 | QGIS 3 |
| --- | --- |
| QgsPolygon | QgsPolygonXY |
| QgsMultiPoint | QgsMultiPointXY |
| QgsMultiPolyline | QgsMultiPolylineXY |
| QgsMultiPolygon | QgsMultiPolygonXY |
| QgsPolygonV2 | QgsPolygon |
| QgsMultiPointV2 | QgsMultiPoint |
| QgsMultiPolylineV2 | QgsMultiPolyline |
| QgsMultiPolygonV2 | QgsMultiPolygon |

See also <https://github.com/qgis/QGIS/pull/5491>

この機能はMatthias、Nyallなどによって開発されました
### 機能：タスクマネージャ
バックグラウンドタスクを作成するためのフレームワークを紹介します。バックグラウンドタスクは、集中管理者と相互作用します

Adds new classes: - QgsTask. An interface for long-running background tasks - QgsTaskManager. Handles groups of tasks - also available as a QgsApplication member for tracking application wide tasks

単純なpythonメソッドQgsTask.fromFunctionを追加すると、QgsTaskサブクラスを作成しなくても、関数からタスクを作成できます

依存するタスクのサポート

他の人が依存しているタスクをキャンセルすると、他のすべてのタスクもキャンセルされます。

従属レイヤーの処理をタスクマネージャに追加する

タスクに従属レイヤーが削除されようとしている場合、タスクは自動的にキャンセルされます

QgsTasksはサブタスクを持つことができます

ここで、QgsTaskは、 QgsTask::addSubTask を呼び出すことによってサブタスクQgsTasksを設定できます。サブタスクは、独自の一連の依存タスクを持つことができます。

サブタスクはユーザーには表示されず、ユーザーは親タスクの全体的な進行状況とステータスのみを表示します。

これにより多くの小さなコンポーネントタスクから構築されたタスクの作成が可能になります。タスクマネージャは、サブタスクの起動とスケジューリングを処理しますので、サブタスクは並行して実行できます（依存関係が許可されている場合など）。　

サブタスク自体にサブタスクを持たせることができます。

この変更は、アルゴリズムおよびモデラーアルゴリズムの処理概念をタスクマネージャーアーキテクチャーに直接変換できるように設計されています。

この機能は、QGISグラントプログラム によって資金提供されました

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: API to allow drag\'n\'drop of custom browser items
QgsDataItemの実装は、カスタム項目のドロップを処理するためにhasDragEnabled()、mimeUri()およびQgsCustomDropHandlerの実装を提供します。

この機能はMartin Dobiasによって開発されました

{{<content-end >}}
