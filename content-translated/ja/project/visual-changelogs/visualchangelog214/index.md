---
HasBanner: false
draft: false
releaseDate: '2016-02-26'
section: project
sidebar: true
title: QGIS 2.14の変更履歴
type: visual-changelog

---
{{<content-start >}}
# QGIS 2.14の変更履歴{#changelog214 }
![image1](images/projects/596e7e353771d2802f065352548e512b8d902d83.png)

リリース日: 2016-02-26

This is the changelog for the next release of QGIS - version 2.14 \'Essen\'. Essen was the host city to our developer meet ups in October 2012 and 2014.

**長期サポート**

This is a special release since it is designated an \'LTR\' (Long Term Release). LTR releases will be supported with backported bug fixes for **one year**, and will be in permanent feature freeze (i.e. no new features will be added, only bug fixes and trivial updates). Note that we are in discussion to extend the term of our LTR releases to two years, but for technical reasons we will not do this until QGIS 3.2.

LTRリリースの目的は、1年に1回以上、ユーザースキルの更新、教材のトレーニングなどに対処したくない企業や組織に対して、安定した頻繁に変化するプラットフォームを提供することです。LTRの成功は、あなたのご愛顧いただいているユーザーにとって非常に重要です。バグ修正に資金を援助し、サポートプロバイダーとのサポート契約であなたのために行われたバグ修正がLTR支店私たちの通常の開発ブランチだけでなく、

LTRが重要な場合は、QGISプロジェクトを直接サポートすることも検討してください。また、LTRをエンタープライズソリューションの基盤として使用することを商用プロバイダに推奨し、安定したプラットフォームを継続的に改善し、洗練されたメリットを享受してください。フロンティアに住むことを希望するユーザーや組織にとって、定期的な4か月ごとのリリースは引き続き控えています。

**New Features in QGIS 2.14 \'Essen\'**

If you are upgrading from QGIS 2.8 (our previous LTR version) you will find a great many new features in this release. We encourage you to peruse the changelogs for the intermediate non LTR [2.10](../visualchangelog210/) and [2.12](../visualchangelog212/) releases as this QGIS 2.14 includes all features published in those releases too. Note that 2.14 first enters the regular package repositories and will not immediately replace 2.8 in the LTR package repositories. That will happen when 2.16 is released.

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

**謝辞**

We would like to thank the developers, documenters, testers and all the many folks out there who volunteer their time and effort (or fund people to do so). From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

QGIS is supported by donors and sponsors. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become an official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six-monthly developer meetings, maintain project infrastructure and fund bug fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

QGIS is Free software and you are under no obligation to pay anything to use it - in fact we want to encourage people far and wide to use it regardless of what your financial or social status is - we believe empowering people with spatial decision making tools will result in a better society for all of humanity. If you are able to support QGIS, you can [![donate here](https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif)](https://qgis.org/en/site/getinvolved/donations.html)

{{<table-of-contents >}}
## QGISスポンサーのみなさま
{{<fund type="changelog" >}}
## 一般情報
### 機能: strpos 関数の挙動の変更
The strpos function behaviour has been altered, so that no match now results in a \"0\" value and a non-zero value means a match at the specified character position. In older QGIS versions, a \"-1\" value would mean no-match and other return values represented the character position - 1.

この変更を反映するために、以前のQGISバージョンのプロジェクトファイルを更新する必要があります。

![image47](images/entries/74ddb567a30e840405ca83656e76dd6476d00226.png.400x300_q85_crop.webp)

この機能はJürgenFischerによって開発されました
### 機能: 属性テーブルでの右クリックによる地物へのズーム
右クリックして地物にズームを選択することで、属性表内から任意の地物をズームすることができます（最初に選択する必要はありません）。

![image48](images/entries/7a400f577a7d554f309297f8a1af05a61e448a27.png.400x300_q85_crop.webp)
### 機能: 速度とメモリーの改善
- 大規模なレイヤーから **選択した地物のセットを保存する** ことははるかに高速になりました
- **フィールド計算機**を使用して選択した地物のみを更新する方が高速です
- **大きなレイヤーではより速いズーム**を選択
- Much faster `get_feature` expression function (especially when an indexed column in the referenced layer is used)
- `SelectByAttribute` and `ExtractByAttribute` processing algorithms are orders of magnitude faster, and can take advantage of database indices created on an attribute
- `PointsInPolygon` processing algorithm is many magnitudes faster
- **分類されたレンダラーのカテゴリをフィルタリングする** （たとえば、一部のカテゴリのみを表示し、他のカテゴリのチェックをはずすなど）、データプロバイダから一致する地物だけが取得されるので、はるかに高速です
- 大きなベクターレイヤーを開くために必要な **メモリの大幅な削減**

### 機能: 式の変数の追加
レンダリング中に新しい変数が使用可能になります：
- `@geometry_part_count`: The part count of the currently rendered geometry (interesting for multi-part features)
- `@geometry_part_num`: 1-based index of the currently rendered geometry part

これらは、マルチパート地物の異なる部分に異なるスタイルを適用する場合に便利です。
- `@map_extent_width`: The width of the currently rendered map in map units
- `@map_extent_height`: The height of the currently rendered map in map units
- `@map_extent_center`: The center point of the currently rendered map in map units

オペレーティングシステム環境に関連する変数も追加されました。
- `@qgis_os_name`: eg \'Linux\',\'Windows\' or \'OSX\'
- `@qgis_platform`: eg \'Desktop\' or \'Server\'
- `@user_account_name`: current user\'s operating system account name
- `@user_full_name`: current user\'s name from operating system account (if available)

![image49](images/entries/b2e29d9df21795416961b8b548f98078386eeecf.png.400x300_q85_crop.webp)

この機能は、Andreas Neumann（OSとユーザー関連の変数）によって資金提供されました。

この機能は、Nyall Dawson、Matthias Kuhn
### 機能: マップエレメントの配置機能の改善
QGIS 2.14は、メインの地図キャンバスにノースアロー、スケールバー、著作権表示を配置するより細かいコントロールを得ています。さまざまな単位（ミリメートル、ピクセル、パーセントを含む）を使用して、これらの要素の位置を正確に設定できるようになりました。

![image50](images/entries/e2390ce8f4bc93ebf00228e1545b192315d2cb57.png.400x300_q85_crop.webp)
### 機能: 資金援助されたバグ修正
各リリースに先立って、私たちは開発者に可能な限り多くのバグを解決するための資金を提供する有料のバグ修正プログラムを開催します。 私たちは、changelogレポートの一環として、有料バグ修正プログラムの報告書を追加することにしました。 このリストは **網羅的ではありません** 。
- Sandro Santilli: [Postgis Connection freeze if you press \"Set filter\" during loading of data](http://hub.qgis.org/issues/13141)
- Sandro Santilli: [db_manager is unable to load rasters from connections with no dbname specified](http://hub.qgis.org/issues/10600)
- Sandro Santilli: [Plugin layers do not work correctly with rotation](http://hub.qgis.org/issues/11900)
- Sandro Santilli: Crash in QgsGeomColumnTypeThread stopping connection scan [#14140](http://hub.qgis.org/issues/14140) [#13806](http://hub.qgis.org/issues/13806)
- Sandro Santilli: [Crash after bulk change of attribute value in shapefile](http://hub.qgis.org/issues/11422)
- Sandro Santilli: [KMZ causes QGIS application crash (Mac)](http://hub.qgis.org/issues/13865)
- Sandro Santilli: [QGIS 2.8.1 crash opening FileGDB (openGDB-Driver)](http://hub.qgis.org/issues/12416)
- Sandro Santilli: [QGIS crashes when removing vertex of a multipart geometry](http://hub.qgis.org/issues/14188)
- Sandro Santilli: [test -V -R qgis_analyzertest segfaults](http://hub.qgis.org/issues/14176)
- Sandro Santilli: [output/bin/qgis_diagramtest segfaults](http://hub.qgis.org/issues/14212)
- Sandro Santilli: Overflow on primary key with negative values; crashes QGIS when editing [#13958](http://hub.qgis.org/issues/13958) [#14262](http://hub.qgis.org/issues/14262)
- Sandro Santilli: [PyQgsPostgresProvider test hangs in absence of test database](http://hub.qgis.org/issues/14269)
- Sandro Santilli: [TestVectorLayerJoinBuffer hangs if database is not available](http://hub.qgis.org/issues/14308)
- Nyall Dawson: [BLOCKER: Crash when opening layer properties dialog for geometryless vector layer](http://hub.qgis.org/issues/14116)
- Nyall Dawson：OGR、Oracle、Spatialiteレイヤーのためのサーバー側の壊れたフィルタリング
- Nyall Dawson: [BLOCKER: Bad polygon digitizing in master](http://hub.qgis.org/issues/14117)
- Nyall Dawson: [BLOCKER: Heatmap with expression triggers segfault](http://hub.qgis.org/issues/14127)
- Nyall Dawson: [BLOCKER: unchecking one sub-layer of a categorized symbology leads to no features being drawn](http://hub.qgis.org/issues/14118)
- Nyall Dawson: [HIGH: A Multiband image(e.g. landsat5,7,8) cannot be displayed in windows8](http://hub.qgis.org/issues/13155)
- Nyall Dawson: [BLOCKER: CurvePolygons not drawn](http://hub.qgis.org/issues/14028)
- Nyall Dawson: [BLOCKER: \"Merge Attributes\" tool doesn\'t change values when they are typed](http://hub.qgis.org/issues/14146)
- Nyall Dawson: [HIGH: Filter legend by content is broken when renderer contains duplicate symbols](http://hub.qgis.org/issues/14131)
- Nyall Dawson：レンダラーをルールベースのレンダラーに変換してレンダラーが破損する問題を修正しました
- Nyall Dawson：修正された分類済みのレンダラーはソースシンボルに変更を保存しません
- Nyall Dawson: [HIGH: Avoid crash with raster calculator and huge raster inputs](http://hub.qgis.org/issues/13336)
- Nyall Dawson: [HIGH: \@value variable of simple symbol fill color wrongly gets modified in data-defined expression](http://hub.qgis.org/issues/14148)
- Nyall Dawson: [HIGH: Editing Composer legend while filtered does not work](http://hub.qgis.org/issues/11459)
- Nyall Dawson: [NORMAL: Deleting nodes - inconsistent behaviour](http://hub.qgis.org/issues/14168)
- Nyall Dawson：属性の時間値の処理を修正
- Nyall Dawson：ダイアログタブの順序の修正
- Nyall Dawson: [BLOCKER: crash when adding multiple files from browser panel](http://hub.qgis.org/issues/14223)
- Nyall Dawson: [HIGH: Merge selected features tool corrupts data when columns are defined as \"hidden\"](http://hub.qgis.org/issues/14235)
- Nyall Dawson：マージ属性ダイアログのLongLongフィールドを正しく処理する
- Nyall Dawson：測定ツールダイアログの計算の詳細の誤った表示を修正しました（多くのCRS /ユニットの組み合わせで誤解を招き、不正確でした）
- Nyall Dawson: [NORMAL: max value for option \"increase size of small diagrams\" not sufficient](http://hub.qgis.org/issues/14282)
- Nyall Dawson: [BLOCKER: Area not calculated correctly with OTF on](http://hub.qgis.org/issues/13209)
- Nyall Dawson: [NORMAL: Incoherent lat/lon coordinates in a projected coordinate system project](http://hub.qgis.org/issues/9730)
- Nyall Dawson: NORMAL: make the field calculator compute areas and lengths in units other than map units [#12939](http://hub.qgis.org/issues/12939) [#2402](http://hub.qgis.org/issues/2402) [#4857](http://hub.qgis.org/issues/4857)
- Nyall Dawson: [NORMAL: different built-in tools calculate inconsistent polygon areas](http://hub.qgis.org/issues/4252)
- Nyall Dawson: [NORMAL: In virtual fields \$area function computes always values using \"None/planimetric\" ellipsoid](http://hub.qgis.org/issues/12622)
- Martin Dobias：ゴミとして描かれたラスターレイヤー
- Martin Dobias: HIGH: Multi-threaded rendering and OTF reprojection issues [#11441](http://hub.qgis.org/issues/11441) [#11746](http://hub.qgis.org/issues/11746)
- Martin Dobias: [BLOCKER: Regression in \"save as\" dialog for shapefiles](http://hub.qgis.org/issues/14158)
- Martin Dobias：デバッグモードでの属性テーブルの読み込みが遅い
- Martin Dobias: [BLOCKER: Crash when changing renderer type](http://hub.qgis.org/issues/14164)
- Martin Dobias: [HIGH: Custom python renderer issues #1](http://hub.qgis.org/issues/14025)
- Martin Dobias: [HIGH: Custom python renderer issues #2](http://hub.qgis.org/issues/13973)
- Martin Dobias：2.5dレンダラーの修正
- Martin Dobias: [HIGH: Long freeze when initializing snapping](http://hub.qgis.org/issues/12578)
- Martin Dobias: [NORMAL: Loading of data-defined from xml](http://hub.qgis.org/issues/14177)
- Martin Dobias: Fix DB manager to work with SpatiaLite \< 4.2
- Martin Dobias: [NORMAL: Crash while rendering in debug mode](http://hub.qgis.org/issues/14369)
- Martin Dobias: BLOCKER: Fix selection / identification in spatialite views [#14232](http://hub.qgis.org/issues/14232) [#14233](http://hub.qgis.org/issues/14233)
- Martin Dobias: [BLOCKER: Fix drag&drop of spatialite tables](http://hub.qgis.org/issues/14237)
- Jürgen Fischer:[Zoom to layer works incorrectly while layer editing](http://hub.qgis.org/issues/3155)
- Jürgen Fischer:[Help viewer process running in the background with no help viewer (or even QGIS) open](http://hub.qgis.org/issues/8305)
- Jürgen Fischer:[Spatialindex include path missing in some components](http://hub.qgis.org/issues/13197)
- Jürgen Fischer:[compile fails attempting to generate qgsversion.h](http://hub.qgis.org/issues/13680)
- Jürgen Fischer:[Edit widget configuration is stored twice](http://hub.qgis.org/issues/13960)
- Jürgen Fischer:[Extra space in \"IS NOT\" operator makes the expression return wrong selection](http://hub.qgis.org/issues/13938)
- Jürgen Fischer:[QGIS greadily allocates memory and crashes when editing moderately large shapefiles with the node tool](http://hub.qgis.org/issues/13963)
- Jürgen Fischer:[French reprojection use ntf_r93.gsb (IGNF:LAMBE etc ..)](http://hub.qgis.org/issues/14101)
- Jürgen Fischer:[Digitizing: \"Reuse last entered attribute values\" should not overwrite primary key column](http://hub.qgis.org/issues/14154)
- Jürgen Fischer:[Issues in Case expression description](http://hub.qgis.org/issues/14189)
- Jürgen Fischer:[shapefile vector writer: datetime field saved as date resulting in data loss of time](http://hub.qgis.org/issues/14190)
- Jürgen Fischer:[Add help for some variable functions](http://hub.qgis.org/issues/14259)
- Jürgen Fischer:[Virtual layers not working in Processing](http://hub.qgis.org/issues/14313)
- Jürgen Fischer:[layer definition file load error](http://hub.qgis.org/issues/14340)
- Jürgen Fischer:[QgsGeometry::fromWkb fails if WKB is different endian representation](http://hub.qgis.org/issues/14204)
- Jürgen Fischer:[Debian build failure.](http://hub.qgis.org/issues/14248)
- Jürgen Fischer:[PyQgsPostgresProvider test hangs in absence of test database](http://hub.qgis.org/issues/14269)
- Jürgen Fischer:[wkb access out of bounds](http://hub.qgis.org/issues/14315)
- Jürgen Fischer:[QGIS under Windows netCDF import reverses Y axis, Linux doesn\'t](http://hub.qgis.org/issues/14316) [OSGeo4W #483](https://trac.osgeo.org/osgeo4w/ticket/483)
- Jürgen Fischer:[OSGEO4W: Running offline install crashes installer](https://trac.osgeo.org/osgeo4w/ticket/105)
- Jürgen Fischer:[OSGEO4W: Dependencies are not tracking on Windows Server 2003 x64](https://trac.osgeo.org/osgeo4w/ticket/117)
- Jürgen Fischer:[OSGEO4W: installation from local package don\'t check the dependencies](https://trac.osgeo.org/osgeo4w/ticket/151)
- Jürgen Fischer:[OSGEO4W: Setup starts downloading and installing packages before showing you a list to choose from](https://trac.osgeo.org/osgeo4w/ticket/262)
- Jürgen Fischer:[OSGEO4W: Using -a for Advanced selects two options (command line install)](https://trac.osgeo.org/osgeo4w/ticket/351)
- Jürgen Fischer:[OSGEO4W: Infinite license download during quite installation of szip](https://trac.osgeo.org/osgeo4w/ticket/486)
- JürgenFischer：Oracleのデッドロック
- ユルゲンフィッシャー：SAGAパス設定を修正

### Feature: Field calculator can be used to update feature\'s geometry
フィールド計算機を使用して、幾何学的表現の結果を使用して地物ジオメトリを更新することができます。これは、選択された地物のグループにバッファを適用するなどの操作を行うための便利なショートカットです。また、2.14の新しく追加されたジオメトリ関数とともに、ジオメトリを操作する非常に便利な方法になります。

![image51](images/entries/ba37e2e778a2349c7099e09fcf648238090d8af4.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### 機能: 新しい関数の追加（v2.14）
バージョン2.14には多くの新しい式関数が追加されています：
- `relate`: performs a DE-9IM geometry relation by either returning the DE-9IM representation of the relationship between two geometries, or by testing whether the DE-9IM relationship matches a specified pattern.
- the `make_point` function now accepts optional z and m values, and a new `make_point_m` function has been added for creation of PointM geometries.
- `m` and `z` functions for retrieving the m and z values from a point geometry
- new `make_line` and `make_polygon` functions, for creation of line and polygon geometries from a set of points
- `reverse`, for reversing linestrings
- `eval` function, which can evaluate a string as though it is an expression of its own
- `translate` function, for translating geometries by an x/y offset
- `darker` and `lighter` functions, which take a color argument and make it darker or lighter by a specified amount
- `radians` and `degrees`: for converting angles between radians and degrees
- `point_on_surface`: returns a point on the surface of a geometry
- `exterior_ring`: returns the exterior ring for a polygon geometry
- `is_closed`: returns true if a linestring is closed
- new geometry accessor functions: `geometry_n` (returns a specific geometry from within a collection), `interior_ring_n` (returns an interior ring from within a polygon)
- `num_geometries`: returns number of geometries inside a collection
- `num_rings`: returns number of rings in a polygon geometry object
- `num_interior_rings`: returns number of interior rings in a polygon
- `nodes_to_points`, for converting every node in a geometry to a multipoint geometry
- `segments_to_lines`, for converting every segment in a geometry to a multiline geometry
- `closest_point`: returns closest point in a geometry to a second geometry
- `shortest_line`: returns the shortest possible line joining two geometries

`nodes_to_points` and `segments_to_lines` are intended for use with geometry generator symbology, eg to allow use of m and z values for nodes/lines with data defined symbology.

その他の改善点:
- geometries and features can now be used in conditional functions. For instance, this allows expressions like `case when $geometry then ... else ...` and `case when get_feature(...) then ... else ...`

![image52](images/entries/98616590f44281e09aa24f6c30d7f668c8665c31.png.400x300_q85_crop.webp)
## 解析ツール
### 機能: 属性結合ツールで使える統計値の追加
マージ属性値または地物をマージツールのいずれかを使用する場合、結果の属性値を設定するために使用できる追加の要約統計があります。これには、Q1、Q3、四分位間の範囲、過半数および少数派の値、および固有の値の数などが含まれます。

![image27](images/entries/3820507f3bffdaab2bafe7285a8c51791f0b1fdb.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### 機能: 地物情報ツールにて Z/M 値が表示されるように
識別ツールでは、識別された地物に存在するzまたはm値を表示できるようになりました。地物がラインまたはポリゴンの場合、ツールは頂点番号と識別された点に最も近い頂点のx / y / z / mを表示します。識別ツールには、コレクションの部品数と部品番号も表示されるようになりました。

![image28](images/entries/c9813d351340f46e28e6a0cb576a4b2ca72466a9.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### 機能: 距離と面積の単位および座標形式の操作方法の統一
QGIS 2.14では、距離単位、エリア単位、座標表示に関するさまざまなオプションの処理が統一され、簡素化され、プロジェクトプロパティに移動されました。この変更により、次のような多くの利点がもたらされます。
- 識別ツールの結果やステータスバーの表示など、座標がユーザーに表示されるたびに、プロジェクトプロパティで指定された座標形式が一貫して使用されます。
- The setting for distance and area units in Project Properties is respected for all distance and area calculations, including the measure tool, identify results, and use of the `$area`, `$length` and `$perimeter` functions.
- 平方ヤード、エーカー、ヘクタールなどの追加の面積単位が追加されました。
- 角度測定ツールに追加の角度単位が追加されました。これには、回転、弧の分、弧の秒が含まれます。
- It\'s now possible to show the coordinates in latitude and longitude in the status bar even when using a projected CRS.

![image29](images/entries/b086f236720ecb5cac0aa8bb7383275799affff4.png.400x300_q85_crop.webp)

この機能は、QGISが支援するバグ修正プログラムによって資金提供されました

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
## ブラウザ
### 機能: ブラウザの改善
QGISブラウザはファイルシステムのOGC Webサービスとデータベース接続パネルで、前述のソースからマップキャンバス（またはDBマネージャウィンドウ）に任意のレイヤーを簡単にドラッグ＆ドロップできます。このリリースでは、2つの便利な新機能が追加されました。
- **パスはブラウザーパネルから選択的に非表示にすることができます**  - これはソースリストを宣言し、関連するディレクトリーにのみ集中するのに便利です。
- **ブラウザから直接プロジェクトをロードする**  - プロジェクト全体をQGISマップキャンバスにドラッグアンドドロップすると、ロードされます。

![image30](images/entries/8479ec7c4077c9602d6eacdb11d518bd55922074.png.400x300_q85_crop.webp)

この機能はNathan Woodrowによって開発されました
## データプロバイダ
### 機能: WMSケーパビリティのキャッシュ
QGIS will now cache WMS `GetCapabilities` requests so that on subsequent use response times will be quicker when using that service. By default the cache period is 24 hours, but you can adjust this in the `Network` tab of the QGIS Settings dialog.

![image31](images/entries/743840449ddf09f45251e9710e9666cf4da86081.png.400x300_q85_crop.webp)

この機能はJürgenFischerによって開発されました
### 機能: カーブしたジオメトリのサポート改善
The delimited text provider now supports curved WKT strings, and the memory provider (eg \"temporary scratch\" layers) has gained full support for curved geometries. Additionally, if QGIS has been built using GDAL versions 2.0 and up then QGIS will fully support curved geometries in supported file types (eg GML files).

![image32](images/entries/79f4b8256ab3507b192277c4f14d3bb04423dc52.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### 機能: time と datetime フィールドの操作改善
QGIS 2.14では、次のような時間フィールドタイプと日時フィールドタイプの処理が改善されました。
- PostgreSQLのタイムスタンプフィールドが正しく処理される
- 数式エンジンでは、時間フィールドを完全にサポートするようになりました
- 式ビルダーに、日付、時刻、日付時刻、および間隔の計算のプレビュー計算結果が表示されるようになりました
- タイムフィールドはベクターファイルレイヤー（ファイル形式に依存）、PostgreSQL、MS SQL Server、一時的なスクラッチレイヤーによって完全にサポートされています
- レイヤーをベクターファイルに保存すると、ベクターレイヤー形式（MapInfo .tabファイルなど）でサポートされている場合は、時間フィールドが保持されます。

![image33](images/entries/2511118cd31ca53892ef5764cf8e80d9491d131a.png.400x300_q85_crop.webp)

この機能はJürgenFischer、Nyall Dawson
### 機能: デリミティッドテキストプロバイダーにおける Z/M 値のサポート
The delimited text provider has gained support for WKT strings containing Z and M coordinates. For example you can express a point with z and measure elements like this : `POINT ZM (1 1 5 60)`.

![image34](images/entries/41d5c223ac43b4f8f392894109414e9d053c9136.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### 機能: postgres 編集におけるトランザクショングループ
トランザクション編集を可能にするための新しいオプションが導入されました。

このオプションを有効にすると
- 同じデータベースのすべてのレイヤーがトランザクショングループに入れられます
- グループの最初のレイヤーを編集モードにすると、他のすべてのレイヤーも自動的に編集モードに入ります
- レイヤーが編集されると、変更はすぐにデータベースに送信され、トリガーと制約がすぐに適用されます
- トランザクショングループ内の1つのレイヤがコミットされると、すべてのレイヤがコミットされます（データベーストランザクション）
- トランザクション・グループ内の1つのレイヤーがロールバックされると、すべてのレイヤーがロールバックされます（データベース・トランザクション）

This feature is currently **Experimental**. If you find any problems, please [report them](https://www.qgis.org/en/site/getinvolved/development/bugreporting.html).

これは現時点でpostgresデータベースに対してのみ実装されています。

![image35](images/entries/bb8a03f09c9675985409cf4360308509830d38d4.png.400x300_q85_crop.webp)

This feature was funded by [SIGE](http://www.sige.ch/)

This feature was developed by [Matthias Kuhn, OPENGIS.ch, based on work by Sourcepole](https://opengis.ch)
### 機能: Postgres プロバイダでのPKI認証
2.12で導入されたQGIS認証マネージャを使用する機能は、PostGISプロバイダに拡張されました。これにより、基本認証またはPKI認証を使用してPostgresに接続し、QGIS設定に認証情報を保存することができます。新しいPostgresプロバイダ認証は、DBマネージャでも使用できます。

![image36](images/entries/6e8f65042bd5981e585812ce2d957d0c6055ba3f.jpg.400x300_q85_crop.webp)

This feature was funded by [Boundless Spatial](http://boundlessgeo.com)

この機能はLuigi Pirelliによって開発されました
### 機能: 仮想レイヤ
レイヤーフォーマット自体にSQLクエリがサポートされていなくても、QGISがロードできるあらゆる種類のベクタレイヤで動的SQLクエリを使用できるようになりました。

A new kind of vector layer called \"virtual layer\" is now available for that purpose. These allow you to create a virtual layer by defining a query (including support for aggregates and joins) from other layers in your project. The resultant layer will be a live, dynamic view of the query result, so any changes to the source layers will be automatically and immediately reflected in the virtual layer!

サポートされているSQLダイアレクトは、SQLite with Spatialite関数です。クエリーでもQGIS式関数を使用できます。クエリーでは、さまざまなデータプロバイダの複数のレイヤーを含め、あらゆる種類のベクターレイヤーにアクセスして結合することができます。

Support for virtual layers has also been added to DB Manager as well as to the Processing toolbox where a new \'Execute SQL\' tool is available.

![image37](images/entries/58bc1a2fea31fe8d6ab70ff33c763c9ddac40ade.png.400x300_q85_crop.webp)

This feature was funded by [MEDDE (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr)

This feature was developed by [Hugo Mercier / Oslandia](http://oslandia.com)
### GDALおよびOGRプロバイダのファイル選択で利用可能なファイル拡張子の追加
ベクタおよびラスタファイルの場合、QGISはGDAL / OGRライブラリに依存します。つまり、GDALまたはOGRで開くことができるほぼすべてのファイル形式をQGISで直接開くことができます。今までは、GDALまたはOGRファイルセレクタにいくつかのファイル拡張子が追加されていなかったため、ユーザーはQGISがこれらのファイル形式を開いたり、処理したりできなかったと考えていました。この問題を最小限に抑えるために、GDALおよびOGRファイルセレクタフィルタにいくつかの新しい拡張機能が追加されました。

**ベクタファイル:**
- .thf EDIGEO French cadastre 形式
- .ods OpenDocument Spreadsheet LibreOffice 形式
- .xls Microsoft Excel 形式
- Microsoft Excel OpenXML形式の.xlsx
- .xml for NAS  -  ALKIS形式
- WAsP形式の.map
- PCIDSK形式の.pix
- GPSTrackMaker形式の.gtmと.zip
- VFK形式の.vfk
- OpenStreetMap形式の.osmおよび.pbf
- SUA形式の.sua
- OpenAir形式の.txt
- .xml for Planetary Data Systems TABLE format
- .htf for Hydrographic Transfer Format
- .svg for SVG format
- ARCGENのための.ge
- .sxf for Storage and eXchange Format
- 地理空間PDFベクトル形式の.pdf
- .sgy and .segy for SEG-Y format
- SEGUKOOA形式の.seg、.seg1、.sp1、.uko、.ukooa
- .ovf VRTベクトルファイル形式
- .kmz for compressed KML (KMZ) format
- .db3, .s3db, .sqlite3, .db3, .s3db, .sqlite3 for SQLite/Spatialite format
- .sl3 for SQLite Spatial (FDO) format
- CouchDB Spatial (via URL)

**ラスタファイル:**
- vrtラスタファイル形式の場合は.ovr

![image38](images/entries/7a628a66f2f63454bd65fbedda309ff5a7d25f1e.png.400x300_q85_crop.webp)

This feature was developed by [Médéric Ribreux](https://medspx.fr)
### Feature: Use ST_RemoveRepeatedPoints for server-side simplification with PostGIS 2.2 (or newer) layers
When using a PostGIS 2.2 instance, QGIS now uses the ST_RemoveRepeatedPoints function instead of the ST_SnapToGrid function to process server-side simplification, as described by [Paul Ramsey](http://blog.cartodb.com/smaller-faster/).

この方法は、QGISがサーバからダウンロードする必要があるジオメトリの頂点の数を減らし、QGISとPostgreSQLサーバの間でレンダリング速度を向上させ、帯域を節約します。

![image39](images/entries/bea701efeedd257314f507dfb2689fbf95403095.png.400x300_q85_crop.webp)

This feature was developed by [Michaël Douchin \@kimaidou](http://3liz.com)
## データマネジメント
### 機能: SPIT プラグインの削除
The \"SPIT\" plugin is no longer bundled with QGIS, as the plugin was unmaintained and has been surpassed by DB Manager and the processing database import algorithms.

![image40](images/entries/b496fc25b098575ece2a38ea5a601caf75bb51dc.png.400x300_q85_crop.webp)

この機能はNathan Woodrowによって開発されました
### 機能: DXFエクスポート: アプリケーションやサーバでのDXFレイヤ名の代わりにタイトルが使用可能に
![image41](images/entries/e09652676e15a883821ca9b269c03ab0239aacb3.png.400x300_q85_crop.webp)

This feature was funded by [City of Uster](http://gis.uster.ch/)

この機能はJürgenFischerによって開発されました
### 機能: ベクタの保存ダイアログにてジオメトリタイプの上書きが可能に
これにより、ジオメトリ・タイプの表をジオメトリ・タイプで保存するなどの作業を実行できるため、ジオメトリを手動で行に追加できます。これまでは、ダミー結合やその他の回避策を使用してQGISでしか実行できませんでした。

さらに、出力ファイルを強制的にマルチタイプにするオプションや、zディメンションを含むオプションも追加されています。

![image42](images/entries/886630cb835b72865c5442a73a79b46cc5a7b60f.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### 機能: QLOレイヤ定義ファイル内にベクタ結合が保存可能に
### 機能: 外部リソースウィジェット
A new form widget is now available. It is named \"External resource\" and it allows a more complete handling of attributes assigned to file paths storing. Here is a complete summary of the widget features:
- You can set an **extension filter** to force the storing of fixed file formats. If a filter is set, the file selector will only show file names that are relevant to the filter (it is still possible to select any file by using \'\*\' character in the search field). Filter syntax is the same than [Qt widget QFileDialog::getOpenFileName](https://doc.qt.io/qt-4.8/qfiledialog.html#getOpenFileName).
- You can set a **default path**. Each time a user triggers the widget, a file selector will open at the default path (if set). If no default path has been set, the file selector will use the last path selected from an \"External resource\" widget. If the widget has never been used, the file selector defaults to opening on the project path.
- **相対パス保存**を定義して設定することができます。相対パスの保存は、デフォルトパスの後（デフォルトパスが設定されている場合）または現在のプロジェクトパスの後にあるパスの一部だけを保存することを可能にします。これは、長いパスを限られたサイズの属性（254文字に制限されているシェイプファイルのテキスト属性など）に保存する場合や、配布用に独立したプロジェクトおよびデータファイルアーカイブを作成する場合に特に便利です。
- ウィジェットを使いやすくするもう1つの新機能は、**ファイルパスをハイパーリンク**として表示できるようにすることです。ハイパーリンクをクリックすると、QGISからリンクされたファイルが直接開きます。このオプションを設定すると、ファイルの絶対パスまたはファイル名のみを表示できます。ファイルは、オペレーティングシステムのファイル形式のデフォルトのハンドラを使用して開きます。
- **ファイルパス**の代わりにURLを使用することもできます。ウィジェットはそれをURLとして解釈し、デフォルトのWebブラウザで直接リンクされたWebページを開くことができます。
- **ファイルパス**の代わりにディレクトリパスを保存することができます。
- このウィジェットには、**統合ドキュメントビューア**があります。QGISに直接写真やWebページを表示することができます。統合されたビューアのファイル・チューザーは上記のすべてのオプションの恩恵を受けるでしょう。

設定オプションの詳細については、設定ダイアログボックスのツールヒントを使用してください。

The main aim of this new widget is to fix and improve the two existing \'File name\' and \'Photo\' widgets, and replace them with a single unified widget. For the moment, you can still use the old widgets but they will be deprecated and removed for QGIS 3.0. We recommend to switch your projects to use the new \'External Resource\' widget now.

**この機能は**によって開発されました：
- [Denis Rouzaud](https://github.com/3nids)
- Matthias Kuhn at [OPENGIS.ch](https://opengis.ch)
- [Médéric Ribreux](https://medspx.fr)

![image43](images/entries/d20edab2103d774f548a55552ca2dbe20ac39e67.png.400x300_q85_crop.webp)
### 機能: N:M リレーションの編集
これにより、N：M（多対多）関係で正規化されたリレーショナルデータベース上のデータを管理する可能性が追加されます。リレーションエディタのフォームでは、リレーションがN：Mリレーションとして視覚化されている場合、追加、削除、リンク、およびリンク解除のツールもリンクテーブルで機能します。

設定はフィールドタブで行います。ここでは、関係の2番目の関係を選択できます（リンクテーブルの2番目の関係で適切な関係がある場合）。

**制限:**

QGISはデータベース管理システムではありません。

基礎となるデータベースシステムに関する前提に基づいています。特に：
- it expects an `ON DELETE CASCADE` or similar measure on the second relation
- it does not take care of setting the primary key when adding features. Either users need to be instructed to set them manually or - if it\'s a database derived value - the layers need to be in transaction mode

![image44](images/entries/9f033883617b01432aae23c35be54070c1a9f5b3.png.400x300_q85_crop.webp)

この機能は、ヴヴェイ市のパリー市、ヌーシャテルの共和国と広州によって資金提供されました

This feature was developed by [Matthias Kuhn](http://opengis.ch)
## デジタイズ
### 機能: 設定可能なラバーバンドカラー
これで、デジタル化に使用するゴムバンドの幅と色を設定できるようになりました。

![image45](images/entries/40ef6c2f93c7697133ebede324fe9dafe40f42f0.png.400x300_q85_crop.webp)
### 機能: トレースデジタイジングツール
新しいトレースデジタイジングツールは、高度なデジタイジングツールです。このツールを使用すると、別のレイヤーの地物をトレースして、あるレイヤーの地物をデジタイズすることができます。

トレースツール：
- uses Dijkstra's shortest path algorithm to find traceable routes
- 複数の異なる機能にわたってルートをトレースできます
- 高度なデジタイザツール（例えば、再構成）で使用できます。
- キーボードの** T **を押してデジタル化している間に有効または無効にすることができます
- 高速で使いやすい

You can read more about this feature [here](http://www.lutraconsulting.co.uk/blog/2016/02/16/qgis-trace-digitising/) and with [this tutorial](http://www.lutraconsulting.co.uk/products/autotrace/TraceDigitising).

この機能の資金は、ウィンザーとメイデンヘッドのロイヤル・ボロー、ニース・ポート・タルボット・カウンティ・ボロー・カウンシル、ウジャヴァル・ガンディー、サリー・ヒース・ボロー・カウンシル、マティアス・アーノルド、ノーサンバーランド国立公園局、ブリューリュー・エステイツ・リミテッド、カントリースケープ

![image46](images/entries/357ff84cf7685a2686a019ebe42f0012b495f79a.png.400x300_q85_crop.webp)

This feature was developed by [Lutra Consulting](http://www.lutraconsulting.co.uk)
## ラベリング
### Feature: \"Cartographic\" placement mode for point labels
この配置モードでは、理想的な地図配置ルールに従ってポイントラベル候補が生成されます。たとえば、ラベル配置は次の順序で優先順位付けされます。
- 右上
- 左上
- 右下
- 左下
- 中央右
- 中央左
- やや右上
- やや左下

（Krygier and Wood（2011）および他の作図マスター作品のガイドラインを尊重する）

優先順位付けされたポジションのデータ定義リストを使用して、個々の地物に配置優先度を設定することもできます。これにより、特定のプレースメントだけを使用することもできます。たとえば、沿岸の地物の場合、土地の上にラベルが配置されないようにすることができます。

![image53](images/entries/23cdbb38f45b05ea930fbeec8ad461e2616ef2a9.png.400x300_q85_crop.webp)

この機能はAndreas Neumannによって資金提供されました

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### 機能: シンボル境界からのラベルまでの距離の使用
この設定が有効な場合、ラベルの距離は、ポイント自体ではなくポイントのレンダリングされたシンボルの境界から適用されます。これは、シンボルサイズが固定されていない場合、たとえばデータ定義サイズで設定されている場合や、分類されたレンダラで異なるシンボルを使用している場合に特に便利です。

この設定は、新しい地図点ラベルの配置モードでのみ使用できます。

![image54](images/entries/9469a985c317ec310e8506e27da5148cedbb93c0.png.400x300_q85_crop.webp)

この機能はAndreas Neumannによって資金提供されました

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### 機能: ラベル描画順序の制御
A new control for setting a label\'s \"z-index\" has been added to the labeling properties dialog. This control (which also accepts data-defined overrides for individual features) determines the order in which labels are rendered. Label layers with a higher z-index are rendered on top of labels from a layer with a lower z-index.

さらに、2つのラベルに一致するz-インデックスがある場合、ロジックは調整されています。
- 同じレイヤーからのものであれば、小さいラベルは常に大きいラベルの上に描画されます
- それらが異なるレイヤーからのものである場合、レイヤー自体と同じ順序でラベルが描画されます（つまり、凡例に設定された順序に従います）

ダイアグラムでは、ラベルや図の順序を制御できるように、Zインデックスを設定することもできます（データは定義しません）。

これは、他のレイヤーの地物の下にラベルを描くことを許可していません。地図上でラベルが描かれる順序を制御するだけです。

![image55](images/entries/52f3e941b047714fbaf81adc7a226e4808a82d09.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### 機能：描画されたシンボルを地物ラベルにて認識が可能に
以前は、ポイント地物自体がラベル候補の障害として扱われていました。ポイントに大きなシンボルまたはオフセットシンボルが使用された場合、障害物コストを発生させることなくラベルにこのシンボルが重なることが許可されました。

今、ラベルがポイント地物と衝突するかどうかを検出するときに、レンダリングされたシンボルの実際のサイズとオフセットが考慮されます。その結果、QGISはより多くの状況でポイントシンボル上にラベルを描画することを回避するようになりました。

![image56](images/entries/7d4d3117427f938ec3a5a4a1ed013e8e4445db60.png.400x300_q85_crop.webp)

この機能は、Uster City

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
## レイヤ凡例
### 機能: 複数の選択レイヤやレイヤグループへのスタイル貼り付けが可能に
この機能により、1つのレイヤーのスタイルをレイヤーグループまたは選択したレイヤーに貼り付けることができます。

![image57](images/entries/63fd1bfff18a108796c400edf127367f30f93c4b.png.400x300_q85_crop.webp)

この機能はSalvatore Larosaによって開発されました
### 機能: 条件式による凡例フィルタ
凡例の要素を式でフィルタリングすることが可能になりました。ルールベースまたは分類されたシンボルのフィルタリングを念頭に置いて設計されています。

凡例フィルタリングは、メインアプリケーションの凡例とQGISコンポーザの凡例コンポーネントで使用できます。

![image59](images/entries/8c957ae820bc98f0a23a7d660abd40264af6e31d.png.400x300_q85_crop.webp)

This feature was funded by [Agence de l\'Eau Adour-Garonne (Adour-Garonne Water Agency)](http://www.eau-adour-garonne.fr)

This feature was developed by [Hugo Mercier / Oslandia](http://oslandia.com)
## マップコンポーザー
### 機能: 凡例項目の新しいフィルタリングオプション
これにより、凡例要素をフィルタする2つの新しいオプションが導入されます。

最初の式でフィルタリングすると、ユーザーは凡例に表示される地物をフィルタリングするための式を設定できます。凡例には、一致する地物を持つシンボルのみが表示されます。

第2のフィルタオプションは、現在のアトラスポリゴンに含まれるアイテムのみを含むように、作曲者の凡例をフィルタリングすることを可能にする。

![image58](images/entries/cf32cc889370df205de51af684c4e683c3ec2dc4.png.400x300_q85_crop.webp)

This feature was developed by [Hugo Mercier (Oslandia)](http://oslandia.com/)
### 機能: コンポーザテンプレートへのパスの追加
You can now define custom paths that should be used for QGIS to find composer templates. This means that you can for example put a bunch of templates in a network share and give your users access to that folder in addition to the local ones that exist on their own system. To manage the composer template search paths, look in `Settings -> Options -> Composer`

![image60](images/entries/bd36891d76ee01ee79e516b0167f403a89fa49de.png.400x300_q85_crop.webp)

この機能はNathan Woodrowによって開発されました
### 機能: コンポーザ管理での複数選択
Composer Managerは、複数の曲を同時に管理するためのサポートを得ています。Ctrlキーを押しながらリストから複数のコンポジションを選択することで、一度に複数のコンポジションを開いたり、削除したりすることができます。

![image61](images/entries/2603b37c6a6ccec10f56f37951d9494cb44c8d0a.png.400x300_q85_crop.webp)

This feature was developed by [Médéric Ribreux](https://medspx.fr)
## プラグイン
### 機能: プラグインマネージャーでの認証システムのサポート
新しい認証システムのサポートがプラグインマネージャーに追加されました。これにより、ユーザーはプラグインリポジトリへの接続に認証設定を適用し、システム管理者はプラグインリポジトリおよび/またはプラグインのダウンロードパッケージへの認証アクセスを作成できます。

![image62](images/entries/7b66e68eb37b27b0ecabcab7d0656985e222e8c0.png.400x300_q85_crop.webp)

This feature was funded by [Boundless Spatial](http://boundlessgeo.com)

この機能はLarry Shafferによって開発されました
## プロセシング
### 機能: 新しいアルゴリズムの追加（v2.14）
#### QGISジオアルゴリズム:
- Smooth：線やポリゴンのレイヤーを平滑化します。
- 行方向を逆転させる。

#### GDAL/OGR ジオアルゴリズム
- gdal2tiles：TMSタイル、KML、シンプルなWebビューアでディレクトリを構築します。
- gdal_retile: retiles a set of tiles and/or build tiled pyramid levels.

### 機能: ユニットテスト Q/A
処理モジュールの長期安定性を保証するために、新しいテストフレームワークが導入されました。

ジオアルゴリズムの処理は、QGISソースコードに当たるすべての変更の後に実行され、その結果は正しい動作を保証するために制御データセットと比較されます。これは、可能性のある回帰についての即時のフィードバックを与える。

It is possible - and desired - that more tests are added. You can read more about [how to participate](https://www.opengis.ch/2016/02/04/increasing-the-stability-of-processing-algorithms/).

![image63](images/entries/4121e58bd51cfe5c8b2c0cd14d1420eaeb1f4473.png.400x300_q85_crop.webp)

This feature was funded by [The QGIS Project](https://www.qgis.org)

This feature was developed by [Matthias Kuhn, OPENGIS.ch](https://opengis.ch)
### 機能: ツールボックスの改善
簡素化されたインターフェイスが削除され、新しい使いやすい管理システムのシステムが追加されました。アルゴリズム検索機能は、現在アクティブではないプロバイダを検索し、アクティブにすることを提案します。

![image64](images/entries/2a135d5384f592e77938c59c0563cc2d0f6c3ebf.jpg.400x300_q85_crop.webp)

This feature was funded by [Boundless Spatial](http://boundlessgeo.com/)

この機能はVíctorOlayaによって開発されました
### 機能: バッチ処理インターフェイスでのバッチ処理の保存と呼び出し
![image65](images/entries/f8dec7fbc9e74dc3f4078f9710984d44b26c4fa3.jpg.400x300_q85_crop.webp)
### 機能: わかりやすいアルゴリズムダイアログの追加
アルゴリズムのパラメータとともに短い説明が表示され、アルゴリズムの目的を理解しやすくなりました。

Also, batch processes can be now started from the algorithm dialog, using the "Run as batch process..." button

![image66](images/entries/c4039a87ddc906921e5e3ce47f8c7aadc7ab2263.jpg.400x300_q85_crop.webp)
### 機能: GRASS7 v.net モジュール
QGIS 2.14 Processing now incorporates v.net GRASS modules (only for GRASS7). Those modules are a set of algorithms that perform on graph line vector layers (networks). [A graph](https://en.wikipedia.org/wiki/Graph_theory#Graph) is a set of vertices (or nodes or points) linked together with a set of edges (or arcs or lines). The set of edges is often called a network.

Thanks to v.net modules, you can easily calculate the shortest path between a set of nodes on the network or even compute the [isochrone map](https://en.wikipedia.org/wiki/Isochrone_map) from a set of central points. you can also easily solve [the complex travelling salesman problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem) from a network and a set of travel nodes.

v.netのアルゴリズムでは、（ネットワーク用の）線ベクターレイヤーと、計算に使用するノードを表すポイントレイヤーを使用することがよくあります。問題を避けるために、ネットワークレイヤーに真のグラフ線ベクターレイヤーを使用してください（辺間の交差なしに頂点に接続する必要があります）。コスト計算に任意のネットワークレイヤー属性を使用することもできます（属性の内容は、辺の移動コストを計算するために使用されます）。

処理に含まれているさまざまなアルゴリズムの概要を以下に示します。
- v.net.alloc：最も近いセンターからサブネットを割り当てます。
- v.net.allpairs：ネットワーク内のすべてのノードペア間の最短経路を計算します。
- v.net.arcs：点のファイルから円弧を作成します。
- v.net.articulation: Computes the [articulation points](https://en.wikipedia.org/wiki/Biconnected_component) in the network.
- v.net.bridge: Computes [bridges](https://en.wikipedia.org/wiki/Bridge_%28graph_theory%29) of the network.
- v.net.centrality：ネットワークの各ノードの度合い、中心性、中間度、近さおよび固有ベクターの中心性を計算します。
- v.net.components：ネットワーク内の強く弱く接続されたコンポーネントを計算します。
- v.net.connect：ポイント（ノード）をネットワークの最も近いアークに接続します（必要に応じてエッジを追加します）。
- v.net.connectivity：ネットワーク内の2つのノードセット間の頂点接続を計算します。
- v.net.distance：2組のノード間のネットワークを経由する最短経路を計算します。
- v.net.flow：ネットワーク内の2つのノードセット間の最大フローを計算します。
- v.net.iso：一連のノードからネットワークの等時性マップを計算します。
- v.net.nodes：ネットワーク/グラフレイヤーのノードを抽出します。
- v.net.nreports：ノードに関する情報を報告します。
- v.net.path：2つのノード間のネットワーク上の最短パスを検索します。
- v.net.report：ネットワークのエッジに関する情報を報告します。
- v.net.salesman: Computes the [travelling salesman path](https://en.wikipedia.org/wiki/Travelling_salesman_problem) from a set of nodes on the network.
- v.net.spanningtree: Computes the [Spanning tree](https://en.wikipedia.org/wiki/Spanning_tree) of the network.
- v.net.steiner: Creates [a Steiner tree](https://en.wikipedia.org/wiki/Steiner_tree_problem) for the network and given nodes.
- v.net.visibility：可視性グラフの作成を実行します。

Use the \"Help\" tab on each of the v.net Processing algorithm to read [the official GRASS7 documentation](https://grass.osgeo.org/grass70/manuals/topic_network.html) directly for more information.

![image67](images/entries/655bbfccc4997a5a3e3d1f5c709da5277eef6000.png.400x300_q85_crop.webp)

This feature was developed by [Médéric Ribreux](https://medspx.fr)
## プログラム可能
### 機能: 関数エディタの再設計
自動保存するように

![image68](images/entries/b42e959476310932713777f75f5eced4826df20a.png.400x300_q85_crop.webp)
### 機能: python init コードをプロジェクト内に保存
Adds an option and code editor to store python form init code into the project (and the DB, since it\'s in the style section)

![image69](images/entries/67bad1306d40aa9b32b64f4d025b77649ae2f775.png.400x300_q85_crop.webp)
### 機能: QgsFeatureRequest でのフィルタ・ソートオプションの追加
QgsFeatureRequestは、返される地物の数の上限を設定できるようになりました。多くの場合、この制限はプロバイダーに渡され、設定された数の地物だけが必要な場合には大幅なパフォーマンスの向上をもたらします。

Additionally, QgsFeatureRequest now supports setting ordering for returned features. Again, in many cases this ordering is delegated to the provider so that it is performed \"server side\" for optimal performance.

![image70](images/entries/6e136c8a4bdf4361b9307f88175369b62d4648d6.png.400x300_q85_crop.webp)
### 機能: Pythonコードオプションでの地物フォームのカスタマイズ
この機能により、Pythonコードのカスタム機能フォームにさらに多くのオプションが追加されます。
- load from file (with file picker widget)
- 環境からのロード（つまり、プラグインやPythonのinit関数）
- 入力ウィジェットにコードを直接入力する（新しいオプション）

ダイアログに入力されたカスタムPythonコードを含む設定オプションは、プロジェクトおよびスタイルQML設定に保存され、DBからエクスポート/復元できます。

![image71](images/entries/65e82ab529ee1287c631712127e1ac75f78d05c6.png.400x300_q85_crop.webp)

This feature was funded by [ARPA Piemonte](http://www.arpa.piemonte.gov.it/)

This feature was developed by [Alessandro Pasotti (ItOpen)](http://www.itopen.it)
### 機能: 新しい PyQGIS クラスの追加（v2.14）
### 新しいコアクラス
- [QgsAttributeEditorElement](https://qgis.org/api/classQgsAttributeEditorElement.html)
  - abstract base class for any elements of a drag and drop form
- [QgsAttributeEditorContainer](https://qgis.org/api/classQgsAttributeEditorContainer.html)
  
  \- container for attribute editors, used to group them visually in an attribute form
- [QgsAttributeEditorField](https://qgis.org/api/classQgsAttributeEditorField.html)
  - element for loading a field\'s widget onto a form
- [QgsAttributeEditorRelation](https://qgis.org/api/classQgsAttributeEditorRelation.html)
  - element for loading a relation editor widget onto a form
- [QgsEditFormConfig](https://qgis.org/api/classQgsEditFormConfig.html)
  - stores and sets configuration parameters for attribute editor forms
- [QgsFeatureFilterProvider](https://qgis.org/api/classQgsFeatureFilterProvider.html)
  
  \- provides an interface for modifying a QgsFeatureRequest in place to apply additional filters to the request
- [QgsTracer](https://qgis.org/api/classQgsTracer.html) - provides graph creation and shortest path search for vector layers
- [QgsTransactionGroup](https://qgis.org/api/classQgsTransactionGroup.html)
  - interface for grouping layers into single edit transactions
- [QgsUnitTypes](https://qgis.org/api/classQgsUnitTypes.html) -helper functions for various unit types and conversions between units (eg distance and area units)
- [QgsVirtualLayerDefinition](https://qgis.org/api/classQgsVirtualLayerDefinition.html)
  - class for manipulating the definitions of virtual layers
- [QgsVirtualLayerDefinitionUtils](https://qgis.org/api/classQgsVirtualLayerDefinitionUtils.html)
  - helper utilities for working with QgsVirtualLayerDefinition objects
- [Qgs25DRenderer](https://qgis.org/api/classQgs25DRenderer.html) -2.5D symbol renderer
- [QgsGeometryGeneratorSymbolLayerV2](https://qgis.org/api/classQgsGeometryGeneratorSymbolLayerV2.html)
  - geometry generator symbol layer
- [QgsFeatureRequest.OrderByClause](https://qgis.org/api/classQgsFeatureRequest_1_1OrderByClause.html)
  - class for specifying a field sort order for feature requests
- [QgsFeatureRequest.OrderBy](https://qgis.org/api/classQgsFeatureRequest_1_1OrderBy.html)
  - a prioritized list of order by clauses for sorting

### 新しいGUIクラス
#### 再利用可能なウィジェット：
- [QgsExternalResourceWidget](https://qgis.org/api/classQgsExternalResourceWidget.html)
  
  \- widget for displaying a file path with a push button for an \"open file\" dialog, and optional display of pictures or HTML files
- [QgsFileWidget](https://qgis.org/api/classQgsFileWidget.html) -widget for selecting a file or a folder
- [QgsLegendFilterButton](https://qgis.org/api/classQgsLegendFilterButton.html)
  
  \- tool button widget that allows enabling or disabling legend filter by contents of the map
- [QgsMapCanvasTracer](https://qgis.org/api/classQgsMapCanvasTracer.html)
  
  \- an extension of QgsTracer that provides extra functionality for interacting with map canvases
- [Qgs25DRendererWidget](https://qgis.org/api/classQgs25DRendererWidget.html)
  - widget for setting properties for a 2.5D renderer
- [QgsColorWidgetAction](https://qgis.org/api/classQgsColorWidgetAction.html)
  - widget action for embedding a color picker inside a menu

#### 再利用可能なダイアログ：
- [QgsStyleV2GroupSelectionDialog](https://qgis.org/api/classQgsStyleV2GroupSelectionDialog.html)
  - dialog for grouping selections in a style
- [QgsGroupWMSDataDialog](https://qgis.org/api/classQgsGroupWMSDataDialog.html)
  - dialog for setting properties for a WMS group
- [QgsOrderByDialog](https://qgis.org/api/classQgsOrderByDialog.html)
  - dialog for specifying sort ordering of fields

## QGISサーバー
### 機能: WFS GetFeature リクエストの STARTINDEX 変数
`` `STARTINDEX `` is standard in WFS 2.0, but it\'s an extension for WFS 1.0 implemented in QGIS Server.

`STARTINDEX` can be used to skip some features in the result set and in combination with `MAXFEATURES` provides for the ability to use WFS GetFeature to page through results. Note that `STARTINDEX=0` means start with the first feature, skipping none.

This feature was developed by [3Liz](http://3liz.com)
### Feature: GetLegendGraphic の showFeatureCount
Add non-standard parameter **showFeatureCount** to add feature count in the legend. To activate it,**showFeatureCount** can be set to *TRUE* or *1*.

この機能には偽のXサーバが必要です。

![image72](images/entries/95f13aa3a1f4cb4ca8cbf7ce30e6bb278e6b9cd8.png.400x300_q85_crop.webp)

This feature was developed by [3Liz](http://3liz.com)
### 機能: タイルエッジの不自然さの除去
![image73](images/entries/1ded32aa2bb962fde1b9f00b891b2a04406be621.png.400x300_q85_crop.webp)
### 機能: プロジェクトプロパティでの設定チェッカー
QGISサーバー用のプロジェクトの設定を支援するために、プロジェクトプロパティに新しい設定チェッカーが追加されました。

チェッカーは次のようなエラーをテストします。
- OWS名として使用される名前または短い名前を複製する
- 不正な OWS 名
- 欠落したベクトルレイヤのエンコーディング

![image74](images/entries/c548fc562785f400d3000e7ae1f61705c333026c.png.400x300_q85_crop.webp)

This feature was funded by [Ifremer](http://wwz.ifremer.fr/institut_eng/)

This feature was developed by [3Liz](http://3liz.com)
### 機能: WMS INSPIRE ケーパビリティ
プロジェクトのプロパティでは、以下のことが可能です。
- INSPIRE機能を有効にする
- 24のEU公式言語+ 5つの地域言語からサービスの言語を選択する
- サービスメタデータのシナリオを選択し、そのパラメータを指定します

WMS 1.3.0の機能は、INSPIRE構成を反映しています。

![image75](images/entries/4ee445bcb5e9eab3fb9bf2eda8f9b1b81bbe21c0.png.400x300_q85_crop.webp)

This feature was developed by [3Liz](http://3liz.com)
### 機能: レイヤ、グループ、プロジェクトへの略称の追加
多くの要素に** Name **と** Title **の両方があります。Nameは、マシンツーマシン通信に使用されるテキスト文字列であり、Titleは人間の利益のためのものです。たとえば、データセットにTitle * Maximum Atmospheric Temperature *という記述があり、省略名* ATMAX *を使用して要求することができます。

ユーザーはすでにレイヤーとプロジェクトのタイトルを設定できます。OpenGeospatial Web Services、OWS（WMS、WFS、WCS）の名前は、レイヤーツリーで使用される名前に基づいています。この名前は、機械対機械通信の名前よりも人間のためのラベルです。

ユーザーがMachine-to-Machine通信のテキスト文字列としてNameを定義する機能を追加するには、次の機能を追加します。
- 短い名前の行でレイヤのプロパティを編集する
- レイヤーツリーグループへのWMSデータダイアログ（短い名前、タイトル、要約）
- プロジェクトのプロパティへの短い名前行の編集
- add a regexp validator \"\^\[A-Za-z\]\[A-Za-z0-9.\_-\]\*\" to short name line edit accessible through a static method
- fullProjectSettingsにTreeName要素を追加する

レイヤー、グループ、およびプロジェクトに短い名前が設定されている場合は、レイヤー名としてQGISサーバーで使用されます。

![image76](images/entries/e2345455bda9f0ed3da5e1c2750d6e2239ab8a86.png.400x300_q85_crop.webp)

This feature was developed by [3Liz](http://3liz.com)
## シンボロジ
### 機能: ライン幅変更におけるサイズアシスタント
![image77](images/entries/1d891425b0e1b9927ced6aab3e0353aed92608de.png.400x300_q85_crop.webp)
### 機能: SVGカラー設定での透過のサポート
バンドルされていないSVGには、

`fill-opacity="param(fill-opacity)"`

and

`stroke-opacity="param(outline-opacity)"`

透明性のサポートを可能にする。

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### 機能: シンボルレイヤのコピーの簡略化
A new \"duplicate\" button has been added to the symbol properties dialog, which allows symbol layers to be easily duplicated.

![image78](images/entries/a6e2ad682852a2fb8b635395ec75f83ef584621d.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### 機能: 2.5D 表示
これにより、2.5Dの効果を得るために必要なすべての要素をまとめやすくするための構成インターフェースとレンダラーが追加されます。

それはスタイリングのいくつかを構成することを可能にし、使いやすいセットアップを作成するためのものです。

Since every part of the system is built around QGIS\' internal rendering and symbology engine, there is much to fine tune. To get all the possibilities, just change the renderer to a graduated, categorized or single symbol renderer upon creation and you will find full access to improve the style to your needs.

**この機能は**によって開発されました：
- Matthias Kuhn at [OPENGIS.ch](https://opengis.ch)

**この機能は**によって資金提供されました：
- ピカルディ地域評議会
- 調節します
- Ville de Nyon
- Wetu GIT cc

![image79](images/entries/8d66f8838011e7bc8fae540d56bf9ef6db20db68.jpg.400x300_q85_crop.webp)
### 機能: 地物の描画順序が定義可能に
地物を特定の順序でレンダリングする必要がある場合、これは任意の式を使用して指定できます。

This can be configured in the layer\'s symbology configuration dialog and can be a simple field or a complex expression.

昇順または降順の制御、NULLが最初か最後かを制御します。

可能であれば、要求はデータベースに送信されます（これは式の複雑さとレイヤーのプロバイダーによって異なります）。要求をデータベースに送信できない場合、注文はローカル・マシン上で実行されます。

This is used by the 2.5D renderer to render features based on their distance from the \"camera\".

これはプラグインでも利用できます：

    layer.getFeatures( QgsFeatureRequest().setOrderBy( 'name' ) ) -- alphabetical by name
    
**This feature was developed by**: Matthias Kuhn at [OPENGIS.ch](https://opengis.ch) **This feature was funded by**: Regional Council of Picardy, ADUGA, Ville de Nyon, Wetu GIT cc

![image80](images/entries/e06cf21a35e070a28ce5b3b98c92f2fb1c1b881d.png.400x300_q85_crop.webp)

This feature was developed by [Matthias Kuhn, OPENGIS.ch](https://opengis.ch)
### 機能: ジオメトリジェネレータシンボル
ジオメトリジェネレータシンボルを使用すると、式エンジンを使用してレンダリングする前にジオメトリを変更したり、地物属性に基づいてレンダリングしながら新しいジオメトリを作成することさ

これは、ソース内のデータを実際に変更することなく、レンダリングの属性のみに基づくパラメータを持つbuffer、translate、intersect、またはextrudeなどのあらゆる種類の空間演算子を使用できます。
### 例
#### ジオメトリの変換
2.5Dレンダラーの屋根に使用されます。

    translate( $geometry, 10, 10 )
    
#### ポリゴンの枠線の塗りつぶしスタイル
これにより、元のポリゴンの輪郭を表すポリゴンが生成されます（サンプル画像）

    difference( buffer( $geometry , 250 ), buffer( $geometry, -250 ) )
    
シンボルレイヤーごとに異なるジオメトリジェネレータを含めることができます。これにより、ジオメトリの異なるバージョンを同時に表示することができます。例として、2.5Dレンダラーがあります。

![image81](images/entries/b06b6bc93644c051c13de162b45d9486b7af769a.png.400x300_q85_crop.webp)

この機能は、ピカルディ地域評議会、ADUGA、Ville de Nyon、Wetu GIT cc

This feature was developed by [Matthias Kuhn, OPENGIS.ch](https://opengis.ch)
## ユーザーインタフェース
### 機能: 属性テーブルが更新可能に
属性テーブル内の属性をリロードするオプションが利用可能になりました。

![image82](images/entries/4623399cb1f63e2c6fa80c72a6aea17b6c63bb3e.png.400x300_q85_crop.webp)
### 機能: 凡例のコンテクストメニューから直接表示やシンボルカラーが設定可能に
メニューにカラーホイールウィジェットを表示するので、1つのダイアログを開く必要なしに、シンボルの色をインタラクティブに編集することができます。

![image83](images/entries/3159457a414ea61f8f40659af5c9561882a44fe1.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### 機能: レイヤツリーから直接凡例シンボルの編集が可能に
This adds a new \"edit symbol\" item to the right-click menu for a renderer child legend item (eg categories for the categorised renderer). Selecting it opens a symbol editor dialog which allows for directly editing the class\'s symbol. It\'s much faster than opening the layer properties and going through the style tab. You can also double-click on a child item to open the symbol editor immediately.

![image84](images/entries/e7b2447e329507f0b27e855111ffa038b1ccc353.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### 機能：コンテキストメニューからすべての凡例を表示/非表示
Allows toggling on/off all the symbol items for categorized/graduated/rule-based layers via the right click menu on an item. Previously you\'d have to toggle each item manually one-by-one.

![image85](images/entries/c526cf9c28c92dde193490a2707c1fe2e0a58ea6.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)

{{<content-end >}}
