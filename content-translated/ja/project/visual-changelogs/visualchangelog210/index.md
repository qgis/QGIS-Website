---
HasBanner: false
draft: false
releaseDate: '2015-06-26'
section: project
sidebar: true
title: QGIS 2.10の変更履歴
type: visual-changelog

---
{{<content-start >}}
# QGIS 2.10の変更履歴{#changelog210 }
リリース日: 2015-06-26

This is the change log for the next release of QGIS - version 2.10.0 \' Pisa\' - host city to our developer meet up in March 2010.

**最新リリース**

This is the next release in our 4-monthly release series. It gives you early access to the new features we have been working on and represents the \'cutting edge\' of QGIS development. If you are working in a production environment where you wish to be more conservative about rolling out new features to your users, we also provide a Long Term Release (LTR) version of QGIS. The current LTR is version 2.8.2 and is available at [download.qgis.org](http://download.qgis.org). LTR releases will be supported with backported bug fixes for one year, and will be in permanent feature freeze (i.e. no new features will be added, only bug fixes and trivial updates). The features provided in QGIS 2.10 \'Pisa\' will be included in the next LTR release (slated for release in 2016), so using this release provides you with an excellent opportunity to test new features that will make their way into the next LTR.

**New Features in QGIS 2.10 \'Pisa\'**

QGIS 2.10.0 includes many great new features, tweaks and enhancements to make the most popular Free desktop GIS even more feature filled and useful. Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

**謝辞**

私たちは、開発者、ドキュメント作成者、テスター、そして時間と労力をボランティアしている（あるいは人々に資金を提供する）多くの人々に感謝したいと思います。

From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

最後に、このプロジェクトに提供した貴重な財政支援について、公式スポンサーに感謝したい。
- **GOLD Sponsor:** [Asia Air Survey, Japan,](http://www.asiaairsurvey.com/)
- SILVER Sponsor: [Sourcepole AG, Switzerland](http://www.sourcepole.com/)
- SILVER Sponsor: [State of Vorarlberg, Austria](http://www.vorarlberg.at/)
- SILVER Sponsor: [Office of Public Works, Ireland, Ireland](http://www.opw.ie/)
- SILVER Sponsor: [AGH University of Science and Technology, Krakow, Poland](http://www.agh.edu.pl/en)
- BRONZE Sponsor: [www.molitec.it, Italy](http://www.molitec.it/)
- BRONZE Sponsor: [www.argusoft.de, Germany](http://www.argusoft.de)
- BRONZE Sponsor: [www.openrunner.com, France](http://www.openrunner.com)
- BRONZE Sponsor: [GKG Kassel,(Dr.-Ing. Claas Leiner), Germany](http://www.gkg-kassel.de/)
- BRONZE Sponsor: [Customer Analytics, USA](http://www.customeranalytics.com/)
- BRONZE Sponsor: [Urbsol, Australia](http://www.urbsol.com.au/)
- BRONZE Sponsor: [MappingGIS, Spain](http://www.mappinggis.com/)
- BRONZE Sponsor: [Lutra Consulting, UK](http://www.lutraconsulting.co.uk/)
- BRONZE Sponsor: [ADLARES GmbH, Germany](http://www.adlares.com/)
- BRONZE Sponsor: [Avioportolano Italia, Italy](http://www.avioportolano.it/)
- BRONZE Sponsor: [GeoSynergy, Australia](http://www.geosynergy.com.au/)
- BRONZE Sponsor: [Gaia3D, South Korea](http://www.gaia3d.com/)
- BRONZE Sponsor: [Royal Borough of Windsor and Maidenhead, UK](http://www.rbwm.gov.uk/)
- BRONZE Sponsor: [Chartwell Consultants Ltd, Canada](http://www.chartwell-consultants.com/)
- BRONZE Sponsor: [Trage Wegen vzw, Belgium](http://www.tragewegen.be/)
- BRONZE Sponsor: [GIS-Support, Poland](http://www.gis-support.com/)
- BRONZE Sponsor: [GIS3W, italy](http://www.gis3w.it/)
- BRONZE Sponsor: [GFI - Gesellschaft fr Informations technologie mbH, Germany](http://www.gfi-gis.de/)
- BRONZE Sponsor: [Faculty of Geology, Geophysics and Environmental Protection, AGH, University of Science and Technology, Poland](http://www.wggios.agh.edu.pl/en)

A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become and official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts.

QGIS はフリーのソフトウェアです。利用する上で金銭を支払う義務はありません。実際、私たちは利用者の財政状況や社会的地位にかかわらず、より多くの人に QGIS を利用して欲しいと思っています。私たちは地理空間的な意思決定ツールによって人々が力を持つことが、全人類の社会をより良くすると信じています。

{{<table-of-contents >}}
## 一般情報
### 機能：結合パラメータを編集できるようになりました
結合が作成された後で、結合パラメータ（結合接頭辞または結合する列など）を編集できるようになりました。この変更に先立って、結合全体を削除して再作成する必要がありました。

![image14](images/entries/bb09241b7b997dfa07942ee5172ad466ebb777f7.webp)
### 機能：結合されたレイヤーをフィルタリングできるようになりました
Prior to version 2.10 a layer couldn\'t be filtered if it had at least one join. Now it is still filterable, but only using columns of the original master table.

![image15](images/entries/a2a93d4e621c1a2cfd976f3b0ec9673739aafda3.webp)
### 機能:全般の改善
下記の多数の項目と同様に、以下の改善がなされました：
- PostGISのPointCloudレイヤーのサポート
- ドッキング可能なウィジェットのアイコンバーとアイコンが改善され、スクリーンの不動産を占有し、OSXの外観を改善
- GRASSプラグイン/プロバイダの改善
- 湾曲したラベル用の非ラテンスクリプトのサポート
- 大幅に改善された、より堅牢なラスタ計算機および地理参照ツール
- データ定義のラベルプロパティウィンドウのUIとワークフローの改善

![image16](images/entries/db0cb94196fd524d93236131418f6e5f3bbf6f25.webp)
### 機能：潜在的なプロジェクトファイルの上書き処理の改善
QGIS 2.10は、ロードされたプロジェクトの最終変更日が変更された場合、プロジェクトを保存しようとすると警告を表示します。これは、複数のユーザーまたはセッションが同じプロジェクトファイルを開いていて、両方がプロジェクトファイルに編集内容を保存しようとしている場合に便利です。

**This feature was developed by:** [Jürgen Fischer (norBIT)](http://www.norbit.de/)

![image17](images/entries/c30c07afc9123db564b766339daefe53af3cd348.webp)
### 機能:新しいジオメトリエンジン
QGIS 2.10 has a new geometry engine. In general you won\'t see many differences on the user interface yet, but this lays the foundation for a much richer set of geospatial capabilities that we will be able to support in the future. The new implementation supports curved geometry types (so for example you can represent a traffic roundabout as a circle rather than a segmented polygon made to look like a circle) and has backend support for z/m values in geometries. To use curves in QGIS you will need to use PostGIS or a similar datastore that is able to express curvilinear geometries. If you want to have a play you can try a simple exercise like this in your PostGIS database:

    -- Table: curves DROP TABLE curves;
    CREATE TABLE curves (
       id bigserial NOT NULL,
       geometry geometry(CURVEPOLYGON, 4326),
       name text,
       CONSTRAINT p_key PRIMARY KEY (id)
       );
    
    INSERT INTO curves VALUES ( 1, st_geomfromtext(
       'CURVEPOLYGON(CIRCULARSTRING(1 1,1 2, 2 2, 2 1, 1 1))', 4326), 'test');
    
Then add the layer `curves` to your project.

**This feature was developed by:** [Marco Hugentobler (Sourcepole AG)](http://www.sourcepole.ch/)

**This feature was funded by:** [KantonSolothurn, Switzerland](http://www.sogis.ch/)

![image18](images/entries/4f070e4075b4703edb40d8cb91d5fb527d1d3a93.webp)
## 解析ツール
### 機能：新しい統計要約ドックウィジェット
Can display summary statistics (e.g. mean, standard deviation, \...) for a field or expression from a vector layer or selection. This is provided by means of a new dock panel that you can activate from the `View -> Panels -> Statistics` menu. Please note that you will only be able to generate statistics on **vector layers** that have a **numeric column**.

![image1](images/entries/7d52fdffac5546ea3f39ee4dac5dbe19f961703a.webp)
### 機能：ラスター計算機で対数関数を使用する
The raster calculator (`Raster -> Raster Calculator` in the QGIS menu) is a tool that allows you to perform matrix operations on one or more raster layers. With QGIS 2.10 you can now use `LN` and `LOG10` functions in the raster calculator.

![image2](images/entries/13c65100ab57ed8f97fa23b08704ca726a7c33da.webp)
### 機能：新しいゾーン統計機能
領域統計は、ポリゴンの基礎となるピクセルの集約値を抽出する方法を提供します。ゾーン統計ツールには、次の新機能が追加されました。
- 計算する統計を選択できるようになりました
- 余計な統計情報が追加されています（中央値、標準値、最小値、最大値、範囲値、少数値、
- 統計抽出に使用するラスタバンドを選択する機能

Note that zonal stats is a \'core plugin\' (a plugin that ships with your QGIS installer), but is disabled by default. You need to enable it in the plugin manager and then a menu entry for zonal statistics will appear in the `Raster` menu.

![image3](images/entries/d86b8eb8a72d26a0fcb0bf043c9189e14a4ae125.webp)
## ブラウザ
### 機能:新しいブラウザプロパティウィジェット
When using the QGIS Browser dock panels (`View -> Panels -> Browser`), you and now enable a properties widget at the bottom of the file system tree. Any data source that you click on will have its properties shown in this panel. This makes it quick and convenient to see basic information about the dataset you have selected. To toggle the properties view, you should use the `i` icon at the top of the browser panel.

![image4](images/entries/2f3fed9a32d761418704da2a7da378ba172164da.webp)
### Feature: New browser icon
QGISブラウザは、ファイルシステム、データベース接続、Webサービス接続などから利用可能なGISデータセットをブラウズして表示するための独立したスタンドアロンアプリケーションです。以前のリリースのQGISでは、多くのユーザーにとって混乱の原因となっていたQGISアプリケーション自体。間違ったアプリケーションを開く可能性を減らすために、QGISブラウザ用の新しいアイコンを作成しました。

![image5](images/entries/e76e98dffc99404f3cad540c42baebb434a696fe.webp)
## データプロバイダ
### 機能：DXFエクスポートの改善
最後の3つのQGISバージョンでは、DXFエクスポートが継続的に改善されました。 このバージョンでは、改良されたSVGやDXFブロック変換の簡単なマーカーが導入され、不完全な（判読不能な）DXFファイルとなるいくつかのバグや問題が修正されています。 スクリーンショットでは、左側のQGISの元のビューと、右側のAutodesk TrueViewでエクスポートされたDXFファイルのレンダリングを見ることができます。

See also [this article on qgis.ch](http://www.qgis.ch/en/projects/dxf-export) explaining what is supported and what not.

**This feature was developed by:** [Jürgen Fischer (norBIT)](http://www.norbit.de/)

**この機能は、以下によって資金提供されました：** Morges、Uster、VeveyおよびSIGEのコミュニティ

![image6](images/entries/b5ee8bd7a3412e429782a5e56954dabee05c36ff.webp)
### Feature: PostGIS provider side expression filters
QGIS 2.10では、データベースサーバー側の機能をフィルタリングできるようになりました。サポートされている式のみがデータベースに送信されます。サポートされていない演算子や関数を使用した式は、ローカル評価に正常にフォールバックします。

To make use of this feature you need to enable it in `Settings -> Options -> data sources`. If your filter expression is PostgreSQL compliant it will automatically be run on the server side. You can also make use of this feature when using the python API for example when using these calls.

`QgsFeatureRequest().setFilterExpression( expression )`

または

`QgsVectorLayer::getFeatures( expression )`

![image7](images/entries/4d4076579ecc0b5aace30fa2743f616a9b691a02.webp)
## データマネジメント
### 機能:バーチャルフィールドが現在は更新可能です
Prior to version 2.8 you had to delete and recreate virtual fields if you wanted to change the expression for calculating the virtual field. In 2.10 you can now go to the `Fields` tab and press the small `Expression` button to open the expression editor and update the expression used for the virtual field.

**This feature was developed by:** [Matthias Kuhn (OpenGIS)](http://www.opengis.ch/)

**This feature was funded by:** [City of Uster, Switzerland](http://gis.uster.ch/)

![image8](images/entries/f45d5a4447f28d96a2c5c4cc6c27b84285096a02.webp)
### 機能：ValueRelation編集ウィジェットの自動補完機能付きライン編集
The value relation edit widget for vector layers (`Layer -> Properties -> Fields -> Edit Widget -> Value Relation`) can now be set to autocomplete as you start typing in the input box it creates on the feature form.

![image9](images/entries/4610dc0ab64a85ae020aeb22b4cbfcc8d45d0df3.webp)
### 機能:DBマネージャの改良
DBマネージャには２つの新しい機能があります:

**レイヤーとしてのクエリはもはやユニークな整数列を必要としません**

一意の整数列を持つ列は、SQLクエリをQGISレイヤーとしてロードするためには必要ありません。自動的にインクリメントされた値が使用されます。

** SQLクエリービルダーの統合**

DB Managerの新しいウィンドウは、テーブル名、カラム名、関数をユーザが選択できるウィジェットを使用してSQLクエリを作成するのに役立ちます。これはQSpatialiteプラグインから移植され、PostGISおよびSpatialiteプロバイダで動作します。

** これらの機能は次の方の資金提供で作成されました **: MEDDE (French Ministry of Sustainable Development)

**  これらの機能は次の方によって開発されました **: Hugo Mercier / Oslandia

![image10](images/entries/f5ad9f81ac37ff4dcfa754f83d23c2700ad4c9f8.webp)
### 機能：リレーション参照ウィジェットのフィルタ連鎖
To select linked entries from other tables one can use the relation reference widgets. One can either select elements graphically by selecting them in the map, if the linked feature has a geometry attached or choose an element by the linked id. To facilitate the non-spatial selection it is now possible to narrow the available options with filters (chained or unchained). If the filters are unchained their choices are combined with \"AND\" to define the available options. If chained is checked, a drill-down mode for the filters is activated so each filter only shows the entries which correspond to the previous filter. This is useful for selecting from hierarchical data like City -\> Street -\> Number.

**This feature was developed by:** [Matthias Kuhn (OpenGIS)](http://www.opengis.ch/)

**This feature was funded by:** [SIGE](http://www.sige.ch/)

![image11](images/entries/fd0d2e726135033e8e5a61b8a718535074a2ac0c.webp)
## ダイアグラム
### 機能:ダイアグラムの改善
QGISのダイアグラム機能により、小さな円グラフやヒストグラムを地図上の地物に重ね合わせできます。今回のリリースでは、ダイアグラムのサポートが次のように改善されました。
- ダイアグラムは設定を失うことなく無効にすることができます
- チェックボックスを追加すると、常にレイヤーの図が表示されます
- ダイアグラムのユーザーインターフェイスが更新され、ダイアログが簡素化され、ユーザーフレンドリーになりました
- Diagram classes are now shown in the layer\'s legend

![image12](images/entries/cc5753de0538c89e3231f18c7ce62c7bc0afa5e8.webp)
## デジタイズ
### 機能：ジオメトリ回転ツールの改良
The geometry rotation tool is an advanced digitising tool that allows you to arbitrarily rotate a feature\'s geometry. The following improvements have been made to the rotation tool:
- 回転マップツールで数値入力を使用できるようになりました
- 角度の設定にコンボボックスを利用できます
- added support for snapping to angles (directly enabled when `using`shift + click\`\`)
- rotation anchor is defined on `CTRL+click` and not on mouse move

![image13](images/entries/7ff32dd8c7ead358f9ffab4576dff33503154eb2.webp)
## ラベリング
### Feature: \"Follow point\" alignment for multiline labels
このモードに設定すると、ラベルのテキストの配置は、ポイントに対するラベルの最終的な配置に依存します。たとえば、ラベルがポイントの左に配置されている場合はラベルは右揃えになり、ポイントの右に配置されている場合はラベルが左揃えになります。これにより、ポイントレイヤの複数ラベルの外観が大幅に改善されます。

![image19](images/entries/851e7234a9509e2452dee69939d9de933a8bb90a.webp)
## マップコンポーザー
### 特長：スケールバーのサイズを希望のスケールバーの幅に合わせる
In previous QGISversions it was hard to use graphical scalebars when the range of potential scales was big. The scalebar would either be quickly too wide or too narrow and one had to manually adapt the segment sizes (units per segment) after each scale change. It also meant that graphical scalebars couldn\'t be really used in Atlas serial printing or with QGISserver when the final map scale was unknown. With QGIS2.10 one can now set min/max sizes for one segment length in mm and QGISwould automatically adapt the units per segment while still keeping round values.

Don\'t forget to also set the alignment of the scalebar, esp. if you want it to be centered or right-aligned!

**This feature was developed by:** [Sandro Mani (Sourcepole AG)](http://www.sourcepole.ch/)

**This feature was funded by:** [Kanton Glarus, Switzerland](http://geo.gl.ch/)

![image20](images/entries/d435d4f94cf3d70a97c8d373aa08c28f8685defd.webp)
## プログラマビリティ
### 特集：プログラマーのための改善
私たちは、開発者にとって興味深いいくつかの変更と改善を行いました。
- Qt4の最小要件をバージョン4.8に引き上げました。Qt4は、QGISを作成するために使用する主要なC ++ツールキット/ライブラリの1つです。
- New `QgsStatisticalSummary` class for calculating statistics from a list of numbers.
- ベクタレイヤのデータソース変更が許可されます.
- Implicit sharing of classes : `QgsField`, `QgsFields`, `QgsDataDefined`, `QgsFeature`, `QgsGeometry`.
- Plugins can now create their own entries in the browser widget with two new classes : `QgsDataItemProvider` and `QgsDataItemProviderRegistry`.

![image21](images/entries/c702d89260cbab35323c052a15ab5c5728fc7115.webp)
## QGISサーバー
### 機能：WMS GetFeatureInfo要求の許容量パラメータのサポート
QGIS Serverが提供するWMSレイヤーを使用する場合、クリック起点のGetFeatureInfo要求がどのくらい離れているかを考慮する必要があります。これは、機能を正確に指すことが難しいモバイルデバイスにとっては重要です。この新機能が登場する以前は、QGISサーバーを搭載したモバイルデバイス上のポイントまたはラインの機能を特定することは事実上不可能でした。GetFeatureInfoリクエストに次のパラメータを追加できます。

FI_POINT_TOLERANCE=16&FI_LINE_TOLERANCE=8&FI_POLYGON_TOLERANCE=4

必要に応じて許容値（ピクセル単位）を変更します。

**This feature was developed by:** [Marco Hugentobler (Sourcepole AG)](http://www.sourcepole.ch/)

**This feature was funded by:** [City of Uster, Switzerland](http://gis.uster.ch/)

![image22](images/entries/29470cc51906dffe3a96d3e17a7e8c83b4504a18.webp)
## シンボロジ
### 機能:既存スタイルを使ったカテゴリマッチ
分類されたレンダラーの詳細メニューのオプションを追加して、スタイルライブラリまたはXMLスタイルファイルの名前と一致するシンボルにカテゴリを設定します。

![image23](images/entries/c3fe0d0389c267271cbd47b8c44f52ac079961d7.webp)
### 機能：段階的レンダラーを使用してシンボルサイズを変更する
レンダラーはQGISのサブシステムであり、データの豊富な地図表現を作成することができます。段階的レンダラーは、ベクターレイヤーの連続的に変化する値に基づいてシンボルを変化させる。QGISの以前のバージョンでは、色を変えることしかできませんでした（たとえば、カラーランプに沿って色を使用するなど）。QGIS 2.10では、目盛り付きのシンボルレンダラーでサイズ *または* 色を変更できるようになりました。ポイントレイヤーではポイントサイズを変えることができます。ラインではライン幅を変えることができます。ポリゴンレイヤーは色によって変化する能力しか保持しませんが、線幅はまだサポートされていません。

**This feature was developed by:** [Vincent Mora (Oslandia)](http://www.oslandia.com/)

**This feature was funded by:** [Agence de l\'eau Adour-Garonne](http://www.eau-adour-garonne.fr/)

![image24](images/entries/1d170efe9ca0c76e971cfe0f1d0adb7c4e14f08f.webp)
### 機能：地物を地図範囲に自動的にクリッピングさせないための新しいオプション
This option (located under the symbol advanced menu) disables the automatic clipping of lines/polygons to the canvas extent. In some cases this clipping results in unfavourable symbology (eg centroid fills where the centroid must always be the actual feature\'s centroid).

![image25](images/entries/ecd30b6893fd93d65c95df8f069cc3c3e0fff7be.webp)
### 機能：詳細メニューからサイズのスケールと回転が削除されました
We have removed `SizeScale` and `Rotation` from `` `Layer -> Properties -> Symbology tab -> Advanced Menu ``. You should rather set rotation on a *per-symbol layer basis* using an expression or field. The expressions used in old projects are converted to symbol level **data defined size and angle** properties.

**This feature was developed by:** [Vincent Mora (Oslandia)](http://www.oslandia.com/)

**This feature was funded by:** [Agence de l\'eau Adour-Garonne](http://www.eau-adour-garonne.fr/)

![image26](images/entries/2e02fb11f0f967b1ea17331d9af3d5a22a63fed1.webp)
### 機能：フォントマーカーのデータ定義プロパティ
フォントマーカのほとんどのプロパティは、マーカのサイズ、回転、文字など、定義されたデータにすることができます。

![image27](images/entries/9ffd9d3284adcc85d6434f0b97f2db8974a7f647.webp)
### 機能：ヒストグラムを使用して目盛レンダラーを視覚化して変更する
段階的レンダラーに新しいヒストグラムタブが追加され、割り当てられたフィールドまたは式からの値のインタラクティブなヒストグラムが表示されます。クラス区切りは、ヒストグラムを使用して移動または追加することができます。

**This feature was funded by:** [ADUGA](http://www.aduga.org)

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image28](images/entries/b519e61b5b50de563203adf8ef35a7c037536332.webp)
### 機能：記号音量レベルでのサイズ、回転、ストローク幅の表現
サイズと回転は、マーカーを構成するすべてのシンボルレベルの式で定義できます。幅は、行を構成するすべてのシンボルの式で定義できます。

シンボルの場合、さまざまなサイズの凡例が生成されます。これにより、分類/卒業した色の場合の多変量解析の凡例が可能になります。

アシスタント（プレビュー付）は、データ定義ボタンからアクセスして、ユーザーがサイズ表記を定義できるようにします。Flannery、Area、およびRadiusの3つの方法があります。

**This feature was developed by:** [Vincent Mora (Oslandia)](http://www.oslandia.com/)

**This feature was funded by:** [Agence de l\'eau Adour-Garonne](http://www.eau-adour-garonne.fr/)

![image29](images/entries/30f4392583400a0ed2fbdae3468265b91f39e675.webp)
### Feature：レイヤーとシンボルレイヤーのライブレイヤーエフェクト
ライブレイヤエフェクトは、レンダリングチェーンにさまざまなレンダーエフェクトを追加する機能を追加することで、QGISの広範な地図作成機能を追加します。ライブエフェクトを使用すると、シンボルの下に影を落としたり、レンダリングされたシンボルを斜めにしたりせん断したりすることができます。また、エフェクトをプログレッシブ（つまりレンダリングされた状態に適用する）か離散（ソースジオメトリをレンダリングチェーンに再注入するか）を設定することもできます。

**注**これは上級者向けの機能です。この機能を過剰に使用するとレンダリング時間が大幅に遅くなることがあるので、レイヤーごとに異なるシンボルプロファイルを使用することを検討してください。 1つはドラフトモードです。

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

**This feature was funded by:** [a crowd-funding initiative](https://www.kickstarter.com/projects/41633306/a-christmas-gift-for-qgis-live-layer-effects-for-q)

![image30](images/entries/2ce331bd884c14764989c1bc5e3c4d1f80ec588c.webp)

{{<content-end >}}
