---
HasBanner: false
draft: false
releaseDate: '2025-06-20'
section: project
sidebar: true
title: QGIS 3.44　変更履歴
type: visual-changelog

---
{{<content-start >}}
# QGIS 3.44　変更履歴{#changelog344 }
<img src="images/projects/3807b5d1851cc87bda040f637e1f4024bc11c58a.png" class="img-responsive img-rounded center-block" />

Release date: 2025-06-20

 QGISプロジェクトは、QGIS 3シリーズの集大成となる記念すべきリリース、QGIS 3.44を誇りを持って発表します。このリリースは、世界中のユーザーを支える活気あふれる拡大し続けるフリー＆オープンソースの地理空間ツール、ライブラリ、コミュニティサポートのエコシステムの中で登場します。過去のリリースの堅固な基盤の上に構築されたQGIS 3.44は、2025年10月に予定されている [QGIS 4.0](https://blog.qgis.org/2025/04/17/qgis-is-moving-to-qt6-and-launching-qgis-4-0/) のリリースに向けてプロジェクトが最新のQt6フレームワークへ移行する中、すべてのユーザーに安定した洗練された体験を提供します。

QGIS 3.xブランチの最後の機能リリースとして、このバージョンは既存のワークフローに信頼性の高い環境を提供します。QGIS 4.0では互換性対応の労力を最小化しエコシステムがコアアプリケーションとともに発展できるよう非推奨APIが維持されるため、プラグイン開発者はリリース間のスムーズな移行を期待できます。

安定性と洗練に重点を置きながらも、このリリースにはワークフローを改善し地理空間作業におけるユーザーの能力を高める注目すべき機能強化が多数含まれています。データベース管理と接続性の改善、データプロバイダーの柔軟性の向上、新しいプロジェクト設定などがその例として挙げられます。プロセッシングツールボックスやQGIS式などの長年親しまれてきた機能も充実した改善が加えられており、新しいラベリングとレイアウトの更新によりカートグラフィー機能も強化されています。

 導入されたすべての新機能を手早く確認するには、 [highlight reel video on YouTube](https://www.youtube.com/watch?v=5a02yaDKAiE) をご覧ください。

[![](https://img.youtube.com/vi/5a02yaDKAiE/0.jpg)](https://www.youtube.com/watch?v=5a02yaDKAiE)

QGISはコミュニティによる取り組みです。このリリースを実現するために時間と労力をボランティアで提供してくださった（または資金援助をしてくださった）開発者・ドキュメント作成者・テスター・その他多くの方々に心より感謝申し上げます。QGISコミュニティより、このリリースをお楽しみいただければ幸いです！QGISをさらに素晴らしいものにするために、時間・資金・その他の形でご貢献いただける方は、ぜひ [QGIS.ORG](https://qgis.org) をご覧いただき、お力をお貸しください！

QGIS is supported by donors and sustaining members. A current list of donors who have made financial contributions large or small to the project can be seen on our [list of donors](https://qgis.org/en/site/about/sustaining_members.html#list-of-donors). If you would like to become an official project sustaining member, please visit our [sustaining member page](https://qgis.org/en/site/about/sustaining_members.html) for more details. Sponsoring QGIS helps us to fund our regular developer meetings, maintain project infrastructure, and fund bug-fixing efforts. A complete list of current sponsors is provided below - our very big thank you to all of our sponsors!

QGIS はフリーのソフトウェアです。利用する上で金銭を支払う義務はありません。実際、私たちは利用者の財政状況や社会的地位にかかわらず、より多くの人に QGIS を利用して欲しいと思っています。私たちは地理空間的な意思決定ツールによって人々が力を持つことが、全人類の社会をより良くすると信じています。
## 時系列
### 機能: WMS-Tグループノードでの時間ディメンションの公開を可能に
WMS-Tレイヤーに、レイヤーツリーグループノードで時間ディメンションを公開できるようにする新しいオプションが追加されました。

WMSグループプロパティのチェックボックスにより、この時間ディメンションの計算をオン/オフできます。有効にすると、子レイヤーの時間ディメンションに基づいて時間ディメンションが再帰的に生成されます。

時間ディメンションの計算が無効になっているグループは、子レイヤーの時間ディメンションを親に伝播しません。

OGC WMSおよびISO8601標準に準拠した時間ディメンションの日付範囲も追加されました。

<img src="images/entries/4916ef1bc94c95cbcb5b66d83e4c4093fe411693" class="img-responsive img-rounded" />

この機能は Ifremer によって資金提供されました

This feature was developed by [Julien Cabieces](https://github.com/troopa81)
### 機能: ラスター時間モードへの固定日付/時刻の追加
ラスターレイヤーの時間プロパティで固定日付/時刻を選択できるようになり、単一の入力値から時間範囲の開始と終了を推定できるようになりました。

<img src="images/entries/d61699232fef2797a38e3fcbe18c65d889896308" class="img-responsive img-rounded" />

この機能は Ifremer によって資金提供されました

This feature was developed by [Julien Cabieces](https://github.com/troopa81)
## ユーザーインタフェース
### 機能:メッセージログパネルで特定のタブを開く
QGISのメッセージログパネルで特定のタブにメッセージを開けるようになりました。

これにより、例えば特定のプロバイダーやプラグイン向けのタブを直接開くことができます。

これは `openMessageLog` メソッドをタブ名をパラメーターとして受け付けるよう拡張することで実現されています。指定されたタブ名が見つからない場合、パネルは既存の状態で表示されます。

この変更にはifaceメソッド `iface.openMessageLog( tab_name )` の拡張も含まれています。

この機能は [City of Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html) の資金提供で開発されました

This feature was developed by [Germán Carrillo](https://github.com/gacarrillor)
## シンボロジ
### 機能: カテゴリ分類シンボルレンダラーウィジェットへの未使用カテゴリの削除オプションの追加
カテゴリ分類シンボルウィジェットに、ユーザーが未使用のカテゴリを一括削除できる新しいオプションが追加されました。

このオプションを使用すると、レイヤーのカテゴリ分類に使用している属性フィールドまたは式に一致しないカテゴリが自動的に特定・削除されます。

これは多数のカテゴリスタイルを引き継いだデータのクリップされたサブセットを使用する場合に特に役立ちます。

<img src="images/entries/85eb6c595a8e44e2fd6deb1586215bc523861dfd.png" class="img-responsive img-rounded" />

This feature was developed by [Ben Wirf](https://github.com/benwirf)
## ラベリング
### 機能: ラベル周囲の余白制御と重複ラベル防止の設定の追加
ベクターレイヤーのラベルに2つの新しい設定が導入されました:
- ラベル周囲の余白:レイヤーのラベル周囲に余白を設定できます。これにより、他のすべてのラベルがこの余白距離より近くに配置されることを防ぎます。
- 重複ラベルの防止:大文字と小文字を区別したマッチングを使用して、すべてのレイヤーにわたる最小距離内の重複するラベルを削除します。

これは、道路ネットワークデータなどの複雑な地理的状況のレンダリングでラベルの見栄えを向上させるために使用できます。片側2車線道路、側道、その他の要素により、同一のラベル要素が近接して多数表示されることがあります。

<img src="images/entries/efc5a69fe9fa346ba7b2d6b9c3ec2b6d57b731d0.png" class="img-responsive img-rounded" />

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## 三次元機能
### 機能: 断面図ツール
3Dシーンで断面図を作成する新しいツールが追加されました。ユーザーは2Dマップキャンバスで3点（始点、終点、断面図の厚さ）をクリックして対象領域を選択でき、3Dビューでは領域外のすべてが非表示になります。3DビューのカメラもROI（対象領域）を横から見る位置に移動します。

3Dビューの範囲設定と比較して、断面図ツールは動作が速く（断面図の有効/無効切り替え時にシーン全体の再読み込みが不要）、また回転した矩形領域にも対応しています。

<img src="images/entries/8034dbe7d55e297f052ef4d310beab10a56ddbb5.png" class="img-responsive img-rounded" />

この機能は Septima, Klimadatastyrelsen からの資金提供で開発されました

This feature was developed by [Matej Bagar](https://github.com/Withalion)
### 機能: 地球儀ビュー
投影座標系ベースの従来の3Dビューに加えて、3Dシーンに新しいモード　- 地球儀ビュー- が追加されました。

あらゆる種類のマップレイヤーを地球儀の2Dテクスチャとして使用でき、タイル化シーンレイヤーとポイントクラウドレイヤーの3Dレンダラーもサポートされています。

地球儀ビューはプロジェクトの楕円体を使用して地球儀メッシュを生成します。プロジェクトのCRSを適切に設定することで、火星や月などの他の天体も表示することができます。

詳細情報:
- [QEP \#301 - Large scenes and globe in QGIS 3D](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/301)
- [Cesium blog post](https://cesium.com/blog/2025/06/20/3d-globe-view-now-available-in-qgis/)

<img src="images/entries/b0ebe685540c3191ad07235d63e45176e9694551.png" class="img-responsive img-rounded" />

この機能は Cesium Ecosystem Grant の資金提供で開発されました

本機能は Lutra Consulting & North Road によって開発されました
### Feature: Large 3D scene support
In earlier versions of QGIS, 3D map views would not behave correctly with scenes larger than 50-100 kilometers due to numerical precision issues - the camera would move erratically (to the point of being unusable) or features would jitter when zoomed in. This has been fixed now - for both local scenes and globe scenes, as outlined in [QEP 301](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/301).

この機能は Cesium Ecosystem Grant の資金提供で開発されました

本機能は Lutra Consulting & North Road によって開発されました
## 点群
### Feature: Update pdal_wrench to v1.2
This provides:
- Improved support of Virtual Point Clouds (VPC) in processing algorithms
- The possibility to output directly to Cloud Optimized Point Cloud (COPC) for various formats

See the [pdal_wrench changelog](https://github.com/PDAL/wrench/releases/tag/v1.2) for more details on other improvements.

この機能は Landesamt für Vermessung und Geoinformation Vorarlberg によって資金提供されました

This feature was developed by [Jan Caha](https://github.com/JanCaha)
### Feature: Allow COPC output for PDAL Algorithms
By leveraging the upgraded pdal_wrench dependency, PDAL Algorithm outputs can be generated as Cloud Optimized Point Clouds

この機能は Landesamt für Vermessung und Geoinformation Vorarlberg によって資金提供されました

This feature was developed by [Jan Caha](https://github.com/JanCaha)
### Feature: Automatic utilization of COPC index files in processing tools
If a COPC file has an index available, QGIS will now automatically utilize it by default when performing processing operations. This will make some operations faster (e.g. clip).

この機能は Landesamt für Vermessung und Geoinformation Vorarlberg によって資金提供されました

This feature was developed by [Jan Caha](https://github.com/JanCaha)
### Feature: Point cloud editing
It is now possible to edit point cloud layers in the 3D map views. Users can pick which attribute to modify, the target value and then interactively select points that should be modified.

There are several map tools to select points for editing:
- ポリゴンによる選択
- ブラシによる選択
- Select Above/Below Line

Users can set up filtering of edited points using QGIS expressions, so that only some points get their attribute value modified.

<div class="col-lg-8 col-md-offset-1">

<div class="iframe">

<div id="player">

</div>

<div class="player-unavailable">

# An error has occurred.{#changelog344 }
<div class="submessage">

<a href="https://www.youtube.com/watch?v=TRxW-g0HYjU" target="_blank">Watch this video on www.youtube.com</a> or enable JavaScript if it is disabled in your browser.

</div>

</div>

</div>

</div>

この機能は Septima, Klimadatastyrelsen からの資金提供で開発されました

This feature was developed by Lutra Consulting
## 印刷レイアウト
### Feature: Add auto-wrap after setting for layout legends
The auto-wrap setting allows legend text to be automatically wrapped after a fixed line length (set in millimeters).

This can be used to prevent excessive widths on auto-generated legends.

<img src="images/entries/ec81517776eea3e38142ca38436789fbdb9e7f9a.png" class="img-responsive img-rounded" />

この機能は North Road, thanks to SLYR によって資金提供されました

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## 計算式
### Feature: Add repeat function and reverse variant for strings
New expressions include:
- A new 'repeat' function, which repeats a string a specified number of times
- A string variant for 'reverse' that allows the reversing of strings

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Expression functions to create CRS from string definition and to get authid from CRS
New expression functions have been added that support the management of coordinate reference systems, namely:
- **crs_from_text**: Creates a coordinate reference system from a string definition. The string definition can be represented using a CRS code in `auth:id` format, a WKT definition, or a PROJ string definition of the CRS.
- **crs_to_authid**: Returns the identifier string for a coordinate reference system in the format `authority:id`, e.g., `EPSG:4326`.

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
## デジタイズ
### Feature: Add merge policies
Similar to the already existing Split and Duplicate "policies", QGIS now supports Merge Policies, which can be configured to determine the initial values in the Merge Features dialog.

Policies can be set per field in the Attributes Form of the Layer Properties dialog, under the "Policies" section of the field configuration.

Policy methods include:
- Sum: (Numeric fields only) Sum of values
- Geometry Weighted: (Numeric fields only) Uses weighted average by geometry
- Default Value: Uses the default value set in QGIS
- Unset Field: Clears the field and uses the default value from the data provider (if it exists). If no value is specified, the value from the first feature is used (current default)
- Largest Geometry: Uses the value from the feature with the biggest geometry (determined by length (line types), area (polygon types), number of parts (multipoint types))
- Minimum Value: (Numeric fields only) Lowest value
- Maximum Value: (Numeric fields only) Highest value
- Set to Null: Sets the value of the field for the feature to NULL

<img src="images/entries/544229ddb1a9eb37b3deacd955241731f8aa4c59.png" class="img-responsive img-rounded" />

This feature was funded by the National Land Survey of Finland.

This feature was developed by [Juho Ervasti](https://github.com/JuhoErvasti)
## データ管理
### Feature: Use HEIGHT_AVERAGE from RPC when available
QGIS can now more accurately position satellite images, especially those from DIMAP / Pleiades NEO products.

This improvement means that these types of satellite images will be displayed in their correct geographical location with greater precision, even without additional elevation data.

<img src="images/entries/6dac68ebcbe251181b8b878ca25e96bee1bf2b33" class="img-responsive img-rounded" />

This feature was developed by [Even Rouault](https://github.com/rouault)
### Feature: Allow field customisation when importing db tables
The database table import dialog has been expanded to include a new field mapping section, which gives users control over the fields in the created table.

Users can rename, set the exact destination field types, and tweak the source expression for each output field.

Fields can also be excluded from the import, or new fields created that don't exist in the source table.

<img src="images/entries/100dca954811ba2396b0fa2fa7edbbaec32dadb0" class="img-responsive img-rounded" />

この機能は City of Canning によって資金提供されました

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Add optional extent, expression based filter when importing tables to database
When a table is imported to a database via the browser, the user now has an option to filter the copied records by extent or expression.

<img src="images/entries/ac84f4eff2203d0b08b4577eeafa37cff09a6db1" class="img-responsive img-rounded" />

この機能は City of Canning によって資金提供されました

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Add stored query support to Execute SQL window
The "Execute SQL" dialog now supports stored queries, replicating the functionality from the DB Manager in the new browser tools.

Users can insert stored queries into their current query, save new stored queries, and remove queries via a new toolbar action.

Queries can be stored in the current project or in the local user profile.

<img src="images/entries/b4d094f69e11aee5f1e2de7ad1ea40d3118b32fb.png" class="img-responsive img-rounded" />

この機能は City of Canning によって資金提供されました

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Saving/Loading SQL queries from Execute SQL/Update SQL dialogs
Support has been added to the Execute SQL dialog and Update SQL dialogs that allows users to save and load SQL queries to/from .sql text files. This replicates the functionality available in the DB Manager over to the core browser-based database connection facilities.

The UX has been designed to mimic the same functionality from other standard parts of QGIS, such as the Processing Script Editor with Toolbar actions for Save/Load as well as new actions for other standard operations, including copy, paste, undo, and redo.

<img src="images/entries/6f5e0b09c033f427fb7f9162d1b2be5a763d674c" class="img-responsive img-rounded" />

この機能は City of Canning によって資金提供されました

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Allow for extra OAuth2 token(s) to be added into headers
OAuth2 advanced configuration options can now attach extra tokens sent by the OAuth2 token endpoint as HTTP(S) request headers. This allows for more flexible handling of OAuth configurations, such as when certain providers append OpenID tokens to their token replies.

This change is integrated into the credential management and is available for all OAuth2 services.

<img src="images/entries/2a9dadb3cfbf35b2efea8c7cd9dd4fe49ffbc292" class="img-responsive img-rounded" />

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### Feature: Convert field name Casing when importing vector layers
The Import Vector dialog for migrating vector layers to data sources now supports the option to automatically transform all field names to lowercase or uppercase.

<img src="images/entries/dc2c1e575d451c7bd98fb6c3b0a7cebe2800fe04" class="img-responsive img-rounded" />

This feature was funded by Ocean Winds

This feature was developed by [Jan Caha](https://github.com/JanCaha)
### Feature: Import selected features only to database table
When importing layer features into a database table, a new dialog option allows for filtering the import to only the selected features. This option is only available if there is a current selection on the imported layer.

<img src="images/entries/4a0b7ca2843d5acb9b2c3b3b2a237d6f7e55a308" class="img-responsive img-rounded" />

This feature was funded by Ocean Winds

This feature was developed by [Jan Caha](https://github.com/JanCaha)
## フォームとウィジェット
### Feature: Switch between field names and field aliases in forms
In line with [QEP 401](https://github.com/qgis/QGIS-Enhancement-Proposals/blob/master/qep-401-overview-widget-types.md), the Vector Layer Properties has been switched to model-based tree views.

This has enabled new functionality, including the ability to switch between field names and field aliases in both the Available Widgets and Form Layout panels.

Additional enhancements include:
- Orphan fields are highlighted in the Form Layout, emulating the UX of broken relations.
- Improvements in broken relations: retain relation names when the relation is still available in the relation manager,

<img src="images/entries/5501d969ec51c06d6ecf49c691c484bec4d08b33.gif" class="img-responsive img-rounded" />

This feature was funded by [the QGIS user group Switzerland](https://qgis.ch/)

This feature was developed by [Germán Carrillo](https://github.com/gacarrillor)
### Feature: Add a search box to Atrributes Form Designer
In line with [QEP#401](https://github.com/qgis/QGIS-Enhancement-Proposals/blob/master/qep-401-overview-widget-types.md), the Drag and Drop form designer now includes a search box to filter items by name or alias, making it much easier to work with tables and datasets that include a lot of attribute fields.

This filter works across both the Available Widgets and the Form Layout panels.

<img src="images/entries/3fefddf7d32b70bf849e390847eca7904ca85ea0.png" class="img-responsive img-rounded" />

This feature was funded by [the QGIS user group Switzerland](https://qgis.ch)

This feature was developed by [Germán Carrillo](https://github.com/gacarrillor)
## 分析ツール
### Feature: Add input parameters to the toolbox in the modeler
A single "Toolbox" panel has been added to the Graphical Modeler, which merges the objects from the Input and Algorithm panels into a single panel. This simplifies the UX of the Graphical Modeler, allowing users to use the search filters rather than manage separate tabs for modeler tools.

<img src="images/entries/2372c98c1724436a5d872bab22bd356ab6bae5d8.png" class="img-responsive img-rounded" />

This feature was funded by [Hauts-de-France](https://www.hautsdefrance.fr/)

This feature was developed by [Valentin Buira](https://github.com/ValentinBuira)
## プロセシング
### Feature: Port SAGA "Fill Sinks Wang & Liu" to native tool
This highly in-demand tool seemed to be fragile and error-prone when run via the SAGA Processing Plugin.

A new native tool has been provided to provide an optimized out-of-the-box tool that is stable and effective.

Note that, as this implementation is a clone of the SAGA implementation, bugs present in the source will be present in the new native tool.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Add creation options UI to raster calculator
Raster creation options are now exposed in the raster calculator UI for both the native dialog and within the Processing Algorithm dialog.

<img src="images/entries/f95b1f5cf9163bbb300ce45564d4e1a7a0877271.png" class="img-responsive img-rounded" />

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
### Feature: Batch processing temporary output
Temporary output layers are now supported in the Batch processing utility, improving the ability to generate intermediate data sources or perform experiments more efficiently.

<img src="images/entries/6c4eab5ac90474f0d924f460586ff36b9c8df288.png" class="img-responsive img-rounded" />

This feature was funded by Ocean Winds

This feature was developed by [Jan Caha](https://github.com/JanCaha)
### Feature: Add basic drag and drop support in the model designer
The QGIS Graphical Modeler now supports independent sockets connected to model nodes, which can be interactively connected via drag and drop.

This allows users to quickly and easily connect an output from one node to a specified input on another without configuring each node's inputs individually.

<img src="images/entries/00050aa06ae1565769944d24e26b9d938da2df6c.png" class="img-responsive img-rounded" />

This feature was developed by [Valentin Buira](https://github.com/ValentinBuira)
### Feature: Processing raster rank algorithm
The new "Raster rank" algorithm takes a collection of rasters as input and creates an output with cell values matching the rank order of a list of cell values taken from the input collection of rasters.

For example, if the list of input values for a given cell is \[10,20,30,40\] and the rank is 2, the output value will be 20.

The algorithm also allows for a negative index rank. Given the same list of input values, \[10,20,30,40\], and using the rank value -2, the output value would be 30.

Finally, the algorithm offers to nodata handling behavior. By default, nodata values are excluded from the list, and a given output cell will only be set to nodata if the rank is greater than the values list size. Users can also pick an alternative behavior, whereas one or more nodata values for a given cell in the input layers will result in a nodata value for that output cell.

<img src="images/entries/8fe5df608b4c445246e6e0f4379304e062e20b88" class="img-responsive img-rounded" />

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
## アプリケーションとプロジェクトのオプション
### Feature: Add project setting for scale calculation, including new "scale at equator" method
A new project-level setting for the scale calculation method has been added, with choices for:
- at top of map
- at bottom of map
- at middle of map
- horizontal average
- scale at equator

Changing the scale method impacts numerous system behaviors, including:
- New layout scale bars will default to the project's scale calculation method
- The scale calculations will be adjusted, affecting project aspects including:
  - status bar widget map renders
  - `@map_scale` and similar scale-related API methods
  - scale based visibility of layers and symbols
- Processing algorithms which render maps will respect the project scale calculation method
- Scale method affects QGIS server map rendering

Note that symbology sizes determined in map units are NOT affected by this setting.

The new "scale at equator "scale calculation method always calculates the scale at the equator, regardless of the actual visible map extent. It can be used to provide a consistent, static scale for maps in geographic reference systems, regardless of the latitudes actually visible in the map. Note that this method is only applicable when calculating scales with a degree-based reference system.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Add multiple country codes filter to Nominatim Geocoder Locator
A new optional configuration value for the Nominatim Geocoder Locator allows filtering results to one or more countries by providing a comma-separated string of the [Two-letter country codes](https://wiki.openstreetmap.org/wiki/Nominatim/Country_Codes) a user would like to restrict their results to.

<img src="images/entries/ad98e211c26bc952c65e8c84b0323c866cc293f0" class="img-responsive img-rounded" />

This feature was funded by [level2](https://level2.si/)

This feature was developed by [Uroš Preložnik](https://github.com/uprel)
## Profile Plots
### Feature: Add support for subsections indicator
Profile plots now support the display of subsection indicators, which are rendered as vertical lines in the profile tool. This is based on outcomes from [QEP#260](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/260) and supports custom indicator symbology as well as providing subsection indicators on both the Elevation Profile view and Print Layout elements.

<img src="images/entries/4eb01abb7bde11412b39323f0dc89ac13958e050.png" class="img-responsive img-rounded" />

This feature was funded by BRGM

This feature was developed by [Jean Felder](https://github.com/ptitjano)
## ブラウザ
### Feature: Port SQL Query History to Browser
The database query history panel is now displayed in the Execute SQL dialog on the browser, in line with [QEP#332](https://github.com/qgis/QGIS-Enhancement-Proposals/blob/master/qep-332-sql-query-history.md).

This adds a new top-level action to open the query history window.

<img src="images/entries/0790aa10b23a8a21663586201234bb438b88bb21.png" class="img-responsive img-rounded" />

This feature was funded by QGIS grant program 2025

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Improved project management for PostgreSQL stored Projects
QGIS now includes options in the browser that allow manipulating QGIS Projects stored in a PostGIS database. New functionalities include the ability to:
- プロジェクト名を変更
- オブジェクトを削除
- オブジェクトを複製
- Move Project to Schema

<img src="images/entries/2ab1e23aae557053f6271e23db145fc791f425ee" class="img-responsive img-rounded" />

This feature was funded by Ocean Winds

This feature was developed by [Jan Caha](https://github.com/JanCaha)
### Feature: Show dialog when importing tables via browser and give users options to control import
A new dialog will prompt users for more comprehensive import configuration when dragging layers into data sources in the QGIS Browser, emulating functionality provided by the DB Manager Plugin for data imports.

Note that this only works when a single layer is selected, and using multiple selections will continue to execute an immediate import.

A new "Import Vector Table.." context menu item is also provided to allow importing directly from the current project layers into a target schema.

The dialog options include:
- Renaming the destination table
- Replace destination
- Set primary key
- Set geometry column
- Set destination CRS
- Set output table comment

This work entailed refactoring a number of internal architectural elements regarding the implementation of the QGIS Browser and data providers. It partly based on efforts by [@JanCaha](https://github.com/JanCaha) to port the DB Manager Postgres import functionality to the QGIS Browser.

Note that this feature does not currently support Oracle databases, due to legacy functionality leveraged by the oracle data provider.

<img src="images/entries/eedf110211aebb2acf61d89108d15ada41b616c8" class="img-responsive img-rounded" />

この機能は City of Canning によって資金提供されました

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Move table to another schema for PostgreSQL Provider
PostgreSQL Tables can now be moved to another schema directly in the QGIS Browser.

This feature was funded by Ocean Winds

This feature was developed by [Jan Caha](https://github.com/JanCaha)
### Feature: Enable field rename for PostgreSQL
QGIS now supports renaming fields for PostgreSQL tables directly in the QGIS Browser interface.

This feature was funded by Ocean Winds

This feature was developed by [Jan Caha](https://github.com/JanCaha)
## データプロバイダ
### Feature: Add a WFS parameter for featureMode
The WFS Provider URI and UI now support a "featureMode" parameter, which supports options for :
- default (Use the server default configuration)
- SimpleFeatures (Enable simplification on returned features)
- ComplexFeatures (Disable simplification on returned features)

This feature was developed by [Even Rouault](https://github.com/rouault)
### Feature: Add connection setting for restricting PostgreSQL Schema
This feature allows users to specify a single schema to limit a Postgres connection to, much like the equivalent Oracle provider setting.

When set, only tables from the matching schema will be included in the browser panel and data source select for the connection.

This can be used to limit the database work required to populate tables for a connection pointing to a large database store.

<img src="images/entries/14da725b2b420a05075ba1b09c83786bf5c839f3" class="img-responsive img-rounded" />

This feature was funded by Regiodata

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Add option to use POST requests for WFS connections
By default, connecting to a WFS server will be done using GET requests; however, users will now be able to switch specific WFS connections to utilize the POST HTTP method, allowing more flexibility in web service configurations.

<img src="images/entries/4a70618846a5eac6a459a0262887e3474bb1c091" class="img-responsive img-rounded" />

This feature was funded by Dorset Council

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Allow SQL queries as layer sources from SQL Server
QGIS now allows loading SQL Server queries as map layers from the browser and updating the SQL for existing query layers.

この機能は City of Canning によって資金提供されました

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## QGISサーバー
### Feature: Allow configuring the server project cache size
A new `QGIS_SERVER_PROJECT_CACHE_SIZE` environment variable has been added, which allows the configuration of the QCache cost, which was previously a hardcoded value.

This feature was developed by [Sandro Mani](https://github.com/manisandro)
### Feature: Add server properties on layer tree group
Users can now edit additional server properties on a layer tree group that will be returned in the GetCapabilities request. Available properties have been extended beyond the previous options of short name, title, and abstract to include:
- キーワード
- Data URL (with format)
- Attribution title and URL
- メタデータURL
- Legend URL and format (by default, one will be generated)

<img src="images/entries/41632eca99d103daf60c2d90b21ce9a543dfc53f.png" class="img-responsive img-rounded" />

この機能は Ifremer によって資金提供されました

This feature was developed by [Julien Cabieces](https://github.com/troopa81)
## プログラム可能
### Feature: Add method to convert shapely geometry to QGIS Geometry
In line with [QEP#227](This%20is%20part%20of%20https://github.com/qgis/QGIS-Enhancement-Proposals/issues/227), a new `QgsGeometry.from_shapely()` method for generating a QgsGeometry object from a shapely object has been provided to improve integration with the shapely geometry library, while keeping it an optional dependency.

This feature was developed by [Till Frankenbach](https://github.com/merydian)
### Feature: Expose QGIS GPS Tools to Python API and Plugins
The GPS tools class is now available in the PyQGIS API via a brand new `QgsAppGpsTools` class, accessed via `QgisInterface::gpsTools()`, so that plugins have more control on the QGIS GPS tracking session.

From QGIS 3.44 on, plugins can create a vector layer feature from the current GPS track, using the method `iface.gpsTools().createFeatureFromGpsTrack()`.

This also exposes additional functionalities, such as setting the GPS track line symbol by changing the corresponding setting in `QgsOptions` and updating the eventual current GPS track geometry accordingly, e.g. `iface.gpsTools().setGpsTrackLineSymbol( line_symbol )`

This feature was funded by [the Danish Nature Agency, Naturstyrelsen](https://naturstyrelsen.dk/)

This feature was developed by [Germán Carrillo](https://github.com/gacarrillor)
## 注目すべき修正
### Feature: Bug fixes by Even Rouault (Spatialys)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| CSV Import to Geopackage ( x/y data) ignores more than 5 Mio rows | [\#60966](https://github.com/qgis/QGIS/issues/60966) | Not reproducible |  |
| OGC API: Feature Creation Request Fails When Location Header is in Lowercase | [\#61729](https://github.com/qgis/QGIS/issues/61729) | [PR \#61814](https://github.com/qgis/QGIS/pull/61814) | [PR \#61835](https://github.com/qgis/QGIS/pull/61835) |
| \[Backport 3.40\] Pick missing commits | [mailing list](https://lists.osgeo.org/pipermail/qgis-developer/2025-May/067555.html) |  | [PR \#61843](https://github.com/qgis/QGIS/pull/61843) |
| Processing : unable to import non spatial table into PostGreSQL with OGR command with processing | [\#61655](https://github.com/qgis/QGIS/issues/61655) | [PR \#61868](https://github.com/qgis/QGIS/pull/61868) | [PR \#62023](https://github.com/qgis/QGIS/pull/62023) |
| Impossibility to save a Null value in a Interger64 field for geopackage files | [\#61787](https://github.com/qgis/QGIS/issues/61787) | can't reproduce |  |
| Error in GML handling in response to a GetFeature request in the WFS service | [\#60879](https://github.com/qgis/QGIS/issues/60879) | [PR \#61872](https://github.com/qgis/QGIS/pull/61872) | [PR \#61895](https://github.com/qgis/QGIS/pull/61895) |
| \[Tests\] Fix and unblock PyQgsLayerDefinition on QT6 |  | [PR \#61874](https://github.com/qgis/QGIS/pull/61874) | N/A |
| \[Tests\] Fix test_core_ogcutils on QT6 |  | [PR \#61876](https://github.com/qgis/QGIS/pull/61876) | N/A |
| \[Tests\] Fix PyQgsDelimitedTextProvider on QT6 |  | [PR \#61877](https://github.com/qgis/QGIS/pull/61877) | N/A |
| \[Tests\] Fix PyQgsSymbolLayerReadSld on QT6 |  | [PR \#61878](https://github.com/qgis/QGIS/pull/61878) | N/A |
| weird include paths including cmake keywords | [\#61887](https://github.com/qgis/QGIS/issues/61887) | [PR \#61894](https://github.com/qgis/QGIS/pull/61894) | N/A |
| QGIS Server GetProjectSettings doesn't output the EX_GeographicBoundingBox anymore for reverse axis projectsions | [\#61999](https://github.com/qgis/QGIS/issues/61999) | [PR \#62002](https://github.com/qgis/QGIS/pull/62002) | [PR \#62036](https://github.com/qgis/QGIS/pull/62036) |
| Spilhaus not displayed complete in QGIS 3.42.1 | [\#61318](https://github.com/qgis/QGIS/issues/61318) | [PR \#62002](https://github.com/qgis/QGIS/pull/62002) | [PR \#62036](https://github.com/qgis/QGIS/pull/62036) |
| QT6 tests: fix PyQgsServerAccessControlWFSTransactional |  | [PR \#62034](https://github.com/qgis/QGIS/pull/62034) | N/A |
| OAPIF: CQL layer filter expression is not used in request | [\#60092](https://github.com/qgis/QGIS/issues/60092) | [PR \#62156](https://github.com/qgis/QGIS/pull/62156) | [PR \#62186](https://github.com/qgis/QGIS/pull/62186) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Even Rouault (Spatialys)](https://www.spatialys.com/)
### Feature: Bug fixes by Alessandro Pasotti (QCooperative)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| Qgis server - Labels background get transparent based on layer transparency | [\#61801](https://github.com/qgis/QGIS/issues/61801) | Won't fix (not a bug) |  |
| Inconsistent contents in ogcapi openapi spec | [\#61848](https://github.com/qgis/QGIS/issues/61848) | [PR \#61903](https://github.com/qgis/QGIS/pull/61903) | [PR \#61922](https://github.com/qgis/QGIS/pull/61922) |
| QGIS Server does not list one layer in WMS GetCapabilities if datum transformation is used | [\#61293](https://github.com/qgis/QGIS/issues/61293) | フィードバック |  |
| QGIS server 3.40.4 - Invalid cache strategy | [\#60947](https://github.com/qgis/QGIS/issues/60947) | [PR \#61907](https://github.com/qgis/QGIS/pull/61907) | N/A |
| Server LTR: OAPIF/WFS3 describe collections malfunction - empty pg layer with UTM zone SRID | [\#60686](https://github.com/qgis/QGIS/issues/60686) | can't reproduce |  |
| Wrong rendering for HIGHLIGHT_LABEL_ROTATION above 89° | [\#54598](https://github.com/qgis/QGIS/issues/54598) | Old issue: asked the OP and put on feedback |  |
| CGIDIR default for UNIX is wrong (bin, should be libexec/cgi-bin or at least not bin) | [\#54424](https://github.com/qgis/QGIS/issues/54424) | Old issue: asked for feedback |  |
| Performance issue on editing large PostGIS layers. | [\#61879](https://github.com/qgis/QGIS/issues/61879) | Not enough info: put on feedback and recommended to hire a consultant |  |
| New HTTP (WMS & friends) connection dialog too tall | [\#61867](https://github.com/qgis/QGIS/issues/61867) | [PR \#61912](https://github.com/qgis/QGIS/pull/61912) | Not critical |
| Problems with \<NULL\> value in Value map | [\#61865](https://github.com/qgis/QGIS/issues/61865) | [PR \#61915](https://github.com/qgis/QGIS/pull/61915) | [PR \#61939](https://github.com/qgis/QGIS/pull/61939) |
| Expression constraint requires case-sensitive field names while form is open | [\#61740](https://github.com/qgis/QGIS/issues/61740) | [PR \#61928](https://github.com/qgis/QGIS/pull/61928) | [PR \#61949](https://github.com/qgis/QGIS/pull/61949) |
| JSON array attribute fields are not supported | [\#61728](https://github.com/qgis/QGIS/issues/61728) | [PR \#61938](https://github.com/qgis/QGIS/pull/61938) | Risky |
| WMS: The parser incorrectly assumes that PositionType contains only a single space (but multiple spaces may exist) | [\#61399](https://github.com/qgis/QGIS/issues/61399) | [PR \#61963](https://github.com/qgis/QGIS/pull/61963) | [PR \#61986](https://github.com/qgis/QGIS/pull/61986) |
| Graduated classification offers date/datetime fields but does not support them | [\#61767](https://github.com/qgis/QGIS/issues/61767) | [PR \#61964](https://github.com/qgis/QGIS/pull/61964) | [PR \#61987](https://github.com/qgis/QGIS/pull/61987) |
| Advanced Digitizing: Floater not working correctly | [\#61587](https://github.com/qgis/QGIS/issues/61587) | [PR \#61979](https://github.com/qgis/QGIS/pull/61979) | [PR \#62114](https://github.com/qgis/QGIS/pull/62114) |
| QGis Server quotes html maptip | [\#61380](https://github.com/qgis/QGIS/issues/61380) | won't fix (not a bug) |  |
| Hidden coverage layer option remains active after disabling atlas generation in layout | [\#61946](https://github.com/qgis/QGIS/issues/61946) | [PR \#61993](https://github.com/qgis/QGIS/pull/61993) | [PR \#62066](https://github.com/qgis/QGIS/pull/62066) |
| Distance/area user selected unit unwanted reset in processing tools | [\#61470](https://github.com/qgis/QGIS/issues/61470) | [PR \#61997](https://github.com/qgis/QGIS/pull/61997) | [PR \#62021](https://github.com/qgis/QGIS/pull/62021) |
| PG: Can't add/update feature when numeric field with numeric default is set to default | [\#61529](https://github.com/qgis/QGIS/issues/61529) | [PR \#62010](https://github.com/qgis/QGIS/pull/62010) | Risky |
| In Refactor Fields algorithm, field for "Source Expression" are loaded from the wrong layer when "selected features only" option is checked | [\#62019](https://github.com/qgis/QGIS/issues/62019) | [PR \#62124](https://github.com/qgis/QGIS/pull/62124) | [PR \#62235](https://github.com/qgis/QGIS/pull/62235) |
| Wrong timezone from default value when adding child feature | [\#62121](https://github.com/qgis/QGIS/issues/62121) | won't fix (not a bug) |  |
| Ellipsoidal measurement not working when the project is using a custom CRS | [\#61299](https://github.com/qgis/QGIS/issues/61299) | [PR \#62212](https://github.com/qgis/QGIS/pull/62212) | [PR \#62252](https://github.com/qgis/QGIS/pull/62252) |
| \[Processing\] "Select by Expression" doesn't works with some expressions | [\#62231](https://github.com/qgis/QGIS/issues/62231) | [PR \#62233](https://github.com/qgis/QGIS/pull/62233) | N/A |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Alessandro Pasotti (QCooperative)](https://www.qcooperative.net/)
### Feature: Bug fixes by Jacky Volpes (Oslandia)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| QgsOptions: Locale value is saved only if it is not empty | [\#52359](https://github.com/qgis/QGIS/issues/52359) | [PR \#62137](https://github.com/qgis/QGIS/pull/62137) | [PR \#62171](https://github.com/qgis/QGIS/pull/62171) |
| Extent not updated after digitizing features in a memory layer | [\#60830](https://github.com/qgis/QGIS/issues/60830) | [PR \#62159](https://github.com/qgis/QGIS/pull/62159) | [PR \#62189](https://github.com/qgis/QGIS/pull/62189) |
| Issue with the geometry combine and mergeLines | [\#61136](https://github.com/qgis/QGIS/issues/61136) | [PR \#62184](https://github.com/qgis/QGIS/pull/62184) |  |
| Atlas activation crash | [\#59610](https://github.com/qgis/QGIS/issues/59610) | [PR \#62260](https://github.com/qgis/QGIS/pull/62260) | [PR \#62288](https://github.com/qgis/QGIS/pull/62288) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Jacky Volpes (Oslandia)](https://oslandia.com/en/)
### Feature: Bug fixes by Jean Felder (Oslandia)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| QgsOptions: Locale value is saved only if it is not empty | [\#52359](https://github.com/qgis/QGIS/issues/52359) | [PR \#62137](https://github.com/qgis/QGIS/pull/62137) | [PR \#62171](https://github.com/qgis/QGIS/pull/62171) |
| Extent not updated after digitizing features in a memory layer | [\#60830](https://github.com/qgis/QGIS/issues/60830) | [PR \#62159](https://github.com/qgis/QGIS/pull/62159) | [PR \#62189](https://github.com/qgis/QGIS/pull/62189) |
| Issue with the geometry combine and mergeLines | [\#61136](https://github.com/qgis/QGIS/issues/61136) | [PR \#62184](https://github.com/qgis/QGIS/pull/62184) |  |
| Atlas activation crash | [\#59610](https://github.com/qgis/QGIS/issues/59610) | [PR \#62260](https://github.com/qgis/QGIS/pull/62260) | [PR \#62288](https://github.com/qgis/QGIS/pull/62288) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Jean Felder (Oslandia)](https://oslandia.com/en/)
### Feature: Bug fixes by Alexander Bruy (QCooperative)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| Better support for SQL and virtual layers as inputs in Processing | [\#39138](https://github.com/qgis/QGIS/issues/39138) | [PR \#61880](https://github.com/qgis/QGIS/pull/61880) | [PR \#61902](https://github.com/qgis/QGIS/pull/61902) |
| Using virtual layer gives error in GDAL processing algorithms | [\#59364](https://github.com/qgis/QGIS/issues/59364) | [PR \#61880](https://github.com/qgis/QGIS/pull/61880) | [PR \#61902](https://github.com/qgis/QGIS/pull/61902) |
| enable GdalAlgorithmsVectorTest on QT6 |  | [PR \#61882](https://github.com/qgis/QGIS/pull/61882) | N/A |
| fix PyQgsFloatingWidget test on Qt6 |  | [PR \#61885](https://github.com/qgis/QGIS/pull/61885) | N/A |
| fix PyQgsNetworkAccessManager test on Qt6 |  | [PR \#61886](https://github.com/qgis/QGIS/pull/61886) | N/A |
| enable QGIS algorithms tests (part 2) on Qt6 |  | [PR \#61888](https://github.com/qgis/QGIS/pull/61888) | N/A |
| Geopackage vocabulary harmonization | [\#60990](https://github.com/qgis/QGIS/issues/60990) | [PR \#61893](https://github.com/qgis/QGIS/pull/61893) | N/A |
| unbalanced QSettings.beginReadArray/endArray calls | [\#61373](https://github.com/qgis/QGIS/issues/61373) | [PR \#61904](https://github.com/qgis/QGIS/pull/61904) | [PR \#61923](https://github.com/qgis/QGIS/pull/61923) |
| Mesh styling, precision seems too small? | [\#50950](https://github.com/qgis/QGIS/issues/50950) | [PR \#61905](https://github.com/qgis/QGIS/pull/61905) | [PR \#61926](https://github.com/qgis/QGIS/pull/61926) |
| Inconsistency in PostgreSQL / PostGIS connection / layer dialog windows | [\#59886](https://github.com/qgis/QGIS/issues/59886) | [PR \#61908](https://github.com/qgis/QGIS/pull/61908) | N/A |
| Translate geometry does not create a 3D vector from 2D if deltaZ is an expression | [\#56495](https://github.com/qgis/QGIS/issues/56495) | [PR \#61906](https://github.com/qgis/QGIS/pull/61906) | [PR \#61933](https://github.com/qgis/QGIS/pull/61933) |
| After deleting the newly added XYZ layer...still exists | [\#53933](https://github.com/qgis/QGIS/issues/53933) | can't reproduce |  |
| TypeError: EnumType.**call**()... | [\#58312](https://github.com/qgis/QGIS/issues/58312) | can't reproduce |  |
| projects/anonymize\_\*\_projects doesn't affect projectMetadata.author | [\#42413](https://github.com/qgis/QGIS/issues/42413) | [PR \#61945](https://github.com/qgis/QGIS/pull/61945) | [PR \#61959](https://github.com/qgis/QGIS/pull/61959) |
| Inconsistencies in providers connection dialogs | [\#43951](https://github.com/qgis/QGIS/issues/43951) | [PR \#61948](https://github.com/qgis/QGIS/pull/61948) | N/A |
| Source manager and WMS configuration dialog too tall | [\#60477](https://github.com/qgis/QGIS/issues/60477) | [PR \#61948](https://github.com/qgis/QGIS/pull/61948) | N/A |
| New HTTP (WMS & friends) connection dialog too tall | [\#61867](https://github.com/qgis/QGIS/issues/61867) | [PR \#61948](https://github.com/qgis/QGIS/pull/61948) | N/A |
| duplicated objectName in the oracle dialog | 未報告 | [PR \#61944](https://github.com/qgis/QGIS/pull/61944) | N/A |
| "Save as" does not work... | [\#30130](https://github.com/qgis/QGIS/issues/30130) | [PR \#61960](https://github.com/qgis/QGIS/pull/61960) | N/A |
| Modifying project CRS...does not update coordinate CRS display | [\#61684](https://github.com/qgis/QGIS/issues/61684) | [PR \#61995](https://github.com/qgis/QGIS/pull/61995) | N/A |
| CRS selection widget not updated when project CRS changes | [\#56454](https://github.com/qgis/QGIS/issues/56454) | [PR \#61989](https://github.com/qgis/QGIS/pull/61989) | [PR \#62022](https://github.com/qgis/QGIS/pull/62022) |
| Choice for default/project styles missing... | [\#58653](https://github.com/qgis/QGIS/issues/58653) | [PR \#62012](https://github.com/qgis/QGIS/pull/62012) | N/A |
| Changing a new project's CRS does not change the annotation CRS | [\#48046](https://github.com/qgis/QGIS/issues/48046) | can't reproduce, already fixed |  |
| "editable" property misleading in JSON view | [\#47755](https://github.com/qgis/QGIS/issues/47755) | [PR \#62064](https://github.com/qgis/QGIS/pull/62064) | N/A |
| ‘Current CRS’ icon shows previous CRS | [\#53768](https://github.com/qgis/QGIS/issues/53768) | [PR \#62209](https://github.com/qgis/QGIS/pull/62209) | [PR \#62236](https://github.com/qgis/QGIS/pull/62236) |
| Crash when clicking on relation table node | [\#56481](https://github.com/qgis/QGIS/issues/56481) | can't reproduce |  |
| Documentation file grass7.txt is not up-to-date | [\#29140](https://github.com/qgis/QGIS/issues/29140) | [PR \#62210](https://github.com/qgis/QGIS/pull/62210) | N/A |
| AttributeError: 'NoneType' object has no attribute 'fields' | [\#62224](https://github.com/qgis/QGIS/issues/62224) | [PR \#62253](https://github.com/qgis/QGIS/pull/62253) | [PR \#62291](https://github.com/qgis/QGIS/pull/62291) |
| Selected field not cleared when changing layer in processing | [\#39351](https://github.com/qgis/QGIS/issues/39351) | [PR \#62241](https://github.com/qgis/QGIS/pull/62241) | [PR \#62305](https://github.com/qgis/QGIS/pull/62305) |
| pyqgis: QgsGraph | [\#56172](https://github.com/qgis/QGIS/issues/56172) | [PR \#62316](https://github.com/qgis/QGIS/pull/62316) | N/A |
| qgsidentifyresultsdialog.cpp: ‘best approach’ vs. ‘old fragile approach’ | [\#61499](https://github.com/qgis/QGIS/issues/61499) | can't reproduce |  |
| exporting to .dxf sets units to imperial inch | [\#50579](https://github.com/qgis/QGIS/issues/50579) | works for me, fixed upstream |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Alexander Bruy (QCooperative)](https://www.qcooperative.net/)
### Feature: Bug fixes by Stefanos Natsis (LutraConsulting)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| STAC client connection failing | [\#62232](https://github.com/qgis/QGIS/issues/62232) | [PR \#62258](https://github.com/qgis/QGIS/pull/62258) | N/A |
| \[browser\] Inappropriate menus in Postgres connection context menu | [\#62183](https://github.com/qgis/QGIS/issues/62183) | [PR \#62270](https://github.com/qgis/QGIS/pull/62270#discussion_r2149355232) | N/A |
| QGIS master crashes when trying to use reshape features tool | [\#55859](https://github.com/qgis/QGIS/issues/55859) | [PR \#62295](https://github.com/qgis/QGIS/pull/62295) | [PR \#62326](https://github.com/qgis/QGIS/pull/62326) |
| Reshape Features can't handle resulting exclaves | [\#24884](https://github.com/qgis/QGIS/issues/24884) | [PR \#62312](https://github.com/qgis/QGIS/pull/62312) |  |
| Reshape tool doesn't obey 'Avoid Overlaps' when a feature is selected. | [\#61720](https://github.com/qgis/QGIS/issues/61720) | [PR \#62312](https://github.com/qgis/QGIS/pull/62312) |  |
| Fix reshaping when snapping to segment | 未報告 | [PR \#62315](https://github.com/qgis/QGIS/pull/62315) |  |
| Unhandled GEOS exception when reshaping | 未報告 | [PR \#62322](https://github.com/qgis/QGIS/pull/62322) |  |
| Reshape returns Success instead of NothingHappened | 未報告 | [PR \#62323](https://github.com/qgis/QGIS/pull/62323) | [PR \#62336](https://github.com/qgis/QGIS/pull/62336) |
| Reshape tool tries to run with a single digitized point | 未報告 | [PR \#62324](https://github.com/qgis/QGIS/pull/62324) |  |
| Fix crash when undoing first digitized point in shape map tools | 未報告 | [PR \#62335](https://github.com/qgis/QGIS/pull/62335) |  |
| Fix crashing shape tools when not enough points digitized | 未報告 | [PR \#62338](https://github.com/qgis/QGIS/pull/62338) |  |
| Crash any time I try to modify a polygon with "Enable tracing" activated. | [\#60856](https://github.com/qgis/QGIS/issues/60856) | [PR \#62345](https://github.com/qgis/QGIS/pull/62345) |  |
| trace function on snap toolset causes QGIS to shutdown when initiated | [\#60978](https://github.com/qgis/QGIS/issues/60978) | [PR \#62345](https://github.com/qgis/QGIS/pull/62345) |  |
| Crash on vector digitizing with trace tool | [\#62163](https://github.com/qgis/QGIS/issues/62163) | [PR \#62345](https://github.com/qgis/QGIS/pull/62345) |  |
| QGIS 3.40.7 Bratislava crashes every time I try to use the tracing tool to create polygons | [\#62342](https://github.com/qgis/QGIS/issues/62342) | [PR \#62345](https://github.com/qgis/QGIS/pull/62345) |  |
| Misbehavior of advanced topology settings on independant layers | バグではない |  |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Stefanos Natsis (LutraConsulting)](https://www.lutraconsulting.co.uk/)
### Feature: Bug Fixes by Germán Carrillo (OPENGIS)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| Old relations in form (after exporting layer to new file and applied old style) can't be deleted | [\#44683](https://github.com/qgis/QGIS/issues/44683) | Can't reproduce |  |
| \[Processing toolbox\] Search box (result) not updated when list of providers change | [\#26435](https://github.com/qgis/QGIS/issues/26435) | [PR \#62162](https://github.com/qgis/QGIS/pull/62162) | No |
| 曖昧なJSONエラー | [\#42832](https://github.com/qgis/QGIS/issues/42832) | [PR \#62247](https://github.com/qgis/QGIS/pull/62247) | [PR \#62262](https://github.com/qgis/QGIS/pull/62262) |
| Disallow point layer as input to Oriented Minimum Bounding Box | [\#62126](https://github.com/qgis/QGIS/issues/62126) | [PR \#62300](https://github.com/qgis/QGIS/pull/62300) | [PR \#62330](https://github.com/qgis/QGIS/pull/62330) |
| When saving SLD to DB, make sure errors are reported to callers (like Package layers algorithm) | 未報告 | [PR \#62332](https://github.com/qgis/QGIS/pull/62332) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Germán Carrillo (OPENGIS)](https://opengis.ch/)
### Feature: Bug fixes by Mathieu Pellerin (OPENGIS)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| QGIS fails to import sprites from OpenStreetMap vector tile styles | 未報告 | [PR \#62175](https://github.com/qgis/QGIS/pull/62175) |  |
| Menu bar not respecting set font size on qt6 build | [\#62007](https://github.com/qgis/QGIS/issues/62007) | [PR \#62086](https://github.com/qgis/QGIS/pull/62086) |  |
| QGIS Qt6 the gui to select the Profile is not well visible | [\#61557](https://github.com/qgis/QGIS/issues/61557) | [PR \#62083](https://github.com/qgis/QGIS/pull/62083) |  |
| Clip by extent prints error on console | [\#61365](https://github.com/qgis/QGIS/issues/61365) | [PR \#62075](https://github.com/qgis/QGIS/pull/62075) | [PR \#62094](https://github.com/qgis/QGIS/pull/62094) |
| QGIS freeze/is not responding, big CPU usage when setting horizontal and vertical spacing units in "point pattern fill" to "meters at scale" | [\#53550](https://github.com/qgis/QGIS/issues/53550) | [PR \#62074](https://github.com/qgis/QGIS/pull/62074) | [PR \#62106](https://github.com/qgis/QGIS/pull/62106) |
| Project translation only happening for .qgs, not .qgz | [\#61485](https://github.com/qgis/QGIS/issues/61485) | [PR \#62070](https://github.com/qgis/QGIS/pull/62070) | [PR \#62101](https://github.com/qgis/QGIS/pull/62101) |
| Stuck in pan mode when using both middle mouse and space pan in model or layout | [\#61528](https://github.com/qgis/QGIS/issues/61528) | [PR \#62069](https://github.com/qgis/QGIS/pull/62069) | [PR \#62093](https://github.com/qgis/QGIS/pull/62093) |
| Unchecking "Include Z-dimension" still includes Z when Geometry Type is Automatic | [\#61554](https://github.com/qgis/QGIS/issues/61554) | [PR \#62068](https://github.com/qgis/QGIS/pull/62068) | [PR \#62092](https://github.com/qgis/QGIS/pull/62092) |
| Label font style reverts to Regular in non_english UI (LTR, Qt5) | [\#61660](https://github.com/qgis/QGIS/issues/61660) | [PR \#62067](https://github.com/qgis/QGIS/pull/62067) | [PR \#62080](https://github.com/qgis/QGIS/pull/62080) |
| Custom shortcuts are not replacing default ones when imported from XML | [\#61717](https://github.com/qgis/QGIS/issues/61717) | [PR \#62063](https://github.com/qgis/QGIS/pull/62063) |  |
| QGIS fails to handle of source containing a relative path to the root of the server hosting the style json | 未報告 | [PR \#62062](https://github.com/qgis/QGIS/pull/62062) | [PR \#62084](https://github.com/qgis/QGIS/pull/62084) |
| Can't save layers as gpkg.zip | [\#61773](https://github.com/qgis/QGIS/issues/61773) | [PR \#62049](https://github.com/qgis/QGIS/pull/62049) | [PR \#62185](https://github.com/qgis/QGIS/pull/62185) |
| appearance input attributes box do not appear checked | [\#61994](https://github.com/qgis/QGIS/issues/61994) | [PR \#62047](https://github.com/qgis/QGIS/pull/62047) | [PR \#62056](https://github.com/qgis/QGIS/pull/62056) |
| QGIS-Locator, Behavior changed between 3.22 and 3.4x | [\#62013](https://github.com/qgis/QGIS/issues/62013) | [PR \#62043](https://github.com/qgis/QGIS/pull/62043) | [PR \#62058](https://github.com/qgis/QGIS/pull/62058) |
| Various new connection dialog spacing and size issues | 未報告 | [PR \#62041](https://github.com/qgis/QGIS/pull/62041) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Mathieu Pellerin (OPENGIS)](https://opengis.ch/)
### Feature: Bug fixes by Julien Cabieces (Oslandia)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| Colours in PDF outputs appear washed out and don't render properly | [\#61674](https://github.com/qgis/QGIS/issues/61674) | [PR \#62091](https://github.com/qgis/QGIS/pull/62091) | [PR \#62107](https://github.com/qgis/QGIS/pull/62107) |
| \[Oracle\] Fix PyQgsProviderRegistry test | qt6 test failing | [PR \#62109](https://github.com/qgis/QGIS/pull/62109) | No |
| Model Designer - Python Converter not generating unique keys | [\#54150](https://github.com/qgis/QGIS/issues/54150) | [PR \#62261](https://github.com/qgis/QGIS/pull/62261) | [PR \#62329](https://github.com/qgis/QGIS/pull/62329) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Julien Cabieces (Oslandia)](https://oslandia.com/en/)
### Feature: Bug fixes by Nyall Dawson (North Road)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fix walk mode key handling | 未報告 | [PR \#62331](https://github.com/qgis/QGIS/pull/62331) | N/A |
| Increase QImageReader allocation limit for qt6 builds | 未報告 | [PR \#62320](https://github.com/qgis/QGIS/pull/62320) | N/A |
| Don't try to pass unset attributes to ArcGIS REST backends | [\#61673](https://github.com/qgis/QGIS/issues/61673) | [PR \#62061](https://github.com/qgis/QGIS/pull/62061) | [PR \#62249](https://github.com/qgis/QGIS/pull/62249) |
| Fix serious regression in boolean handling in expressions | [\#61072](https://github.com/qgis/QGIS/issues/61072) | [PR \#62217](https://github.com/qgis/QGIS/pull/62217) | [PR \#62248](https://github.com/qgis/QGIS/pull/62248) |
| Don't render effects which require rasterisation when forcing vector | [\#58230](https://github.com/qgis/QGIS/issues/58230) | [PR \#62218](https://github.com/qgis/QGIS/pull/62218) | N/A |
| Fix categorized symbol renderer feature counts for null values | [\#52690](https://github.com/qgis/QGIS/issues/52690) | [PR \#62174](https://github.com/qgis/QGIS/pull/62174) | [PR \#62203](https://github.com/qgis/QGIS/pull/62203) |
| Try to extract only polygons from Voronoi results | [\#62158](https://github.com/qgis/QGIS/issues/62158) | [PR \#62173](https://github.com/qgis/QGIS/pull/62173) | [PR \#62194](https://github.com/qgis/QGIS/pull/62194) |
| \[processing\] Fix show feature count option, output layer ordering | [\#61146](https://github.com/qgis/QGIS/issues/61146) | [PR \#62143](https://github.com/qgis/QGIS/pull/62143) | [PR \#62172](https://github.com/qgis/QGIS/pull/62172) |
| Don't finalize string stats after every value addition | [\#62122](https://github.com/qgis/QGIS/issues/62122) | [PR \#62170](https://github.com/qgis/QGIS/pull/62170) | [PR \#62192](https://github.com/qgis/QGIS/pull/62192) |
| Fix build with SIP \>= 6.11 | [\#61951](https://github.com/qgis/QGIS/issues/61951) | [PR \#62113](https://github.com/qgis/QGIS/pull/62113) | [PR \#62142](https://github.com/qgis/QGIS/pull/62142) |
| Use protected, not private virtual methods for map tool classes | 未報告 | [PR \#62097](https://github.com/qgis/QGIS/pull/62097) | [PR \#62112](https://github.com/qgis/QGIS/pull/62112) |
| Avoid corrupted overlapping docks when first changing from dialog to dock | 未報告 | [PR \#62102](https://github.com/qgis/QGIS/pull/62102) | N/A |
| Fix jumpy scroll area when using mouse wheel on qt6 builds | 未報告 | [PR \#62099](https://github.com/qgis/QGIS/pull/62099) | N/A |
| Fix comparators | [\#62045](https://github.com/qgis/QGIS/issues/62045) | [PR \#62081](https://github.com/qgis/QGIS/pull/62081) | [PR \#62118](https://github.com/qgis/QGIS/pull/62118) |
| \[processing\] Fix execution of nested models | [\#60883](https://github.com/qgis/QGIS/issues/60883) | [PR \#62079](https://github.com/qgis/QGIS/pull/62079) | [PR \#62100](https://github.com/qgis/QGIS/pull/62100) |
| Fix calculation of cost for speed strategy with null/negative values | [\#61667](https://github.com/qgis/QGIS/issues/61667) | [PR \#62044](https://github.com/qgis/QGIS/pull/62044) | [PR \#62059](https://github.com/qgis/QGIS/pull/62059) |
| Fix variables available for grid annotations missing for grid symbol | 未報告 | [PR \#61943](https://github.com/qgis/QGIS/pull/61943) | [PR \#61957](https://github.com/qgis/QGIS/pull/61957) |
| Add new enum for rasterised rendering policy | [\#58230](https://github.com/qgis/QGIS/issues/58230) | [PR \#61942](https://github.com/qgis/QGIS/pull/61942) | N/A |
| Fix blend modes ignored when label masking is enabled | [\#43141](https://github.com/qgis/QGIS/issues/43141) | [PR \#61901](https://github.com/qgis/QGIS/pull/61901) | N/A |
| Delimited text test can be run on qt6 now | 未報告 | [PR \#61900](https://github.com/qgis/QGIS/pull/61900) | N/A |
| Fix mesh layer labeling tests not actually run | 未報告 | [PR \#61899](https://github.com/qgis/QGIS/pull/61899) | [PR \#61909](https://github.com/qgis/QGIS/pull/61909) |
| \[ogr\] Handle auto addition of vsizip prefix for vsicurl archives | [\#61561](https://github.com/qgis/QGIS/issues/61561) | [PR \#61854](https://github.com/qgis/QGIS/pull/61854) | [PR \#61896](https://github.com/qgis/QGIS/pull/61896) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)

{{<content-end >}}
