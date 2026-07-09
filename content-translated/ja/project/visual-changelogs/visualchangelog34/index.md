---
HasBanner: false
draft: false
releaseDate: '2018-10-26'
section: project
sidebar: true
title: QGIS 3.4の変更履歴
type: visual-changelog

---
{{<content-start >}}
# QGIS 3.4の変更履歴{#changelog34 }
![image0](images/entries/splash34vs.webp)

リリース日: 2018-10-26

QGIS 3の最初の長期サポートリリース（LTR）です。QGIS 3.4がリリースされました。5回の安定化ポイントリリース（3.4.5）の後、2019年2月にパッケージリポジトリで以前のLTRと置き換えられます（ [リリーススケジュール]({{< ref "resources/roadmap#release-schedule" >}}) 参照）。これはプロジェクトにとって大きな飛躍です。3.xプラットフォームに基づく初めての長期リリースです。2.18 LTRから移行するユーザーにとっては、この新しいLTRバージョンには膨大な新機能と大きな変更があります。3.xプラグインは2.xプラグインと互換性がないため、プラグインの使用状況を慎重に確認し、可能であれば古いプラグインを新しいプラットフォームに移行する支援をしてください。まだ確認していない場合は、 [バージョン3.0 ](../visualchangelog30) と [バージョン3.2](../visualchangelog32) の変更履歴を参照して、3.4リリースの変更の全範囲を理解してください。

**謝辞**

We would like to thank the developers, documenters, testers and all the many folks out there who volunteer their time and effort (or fund people to do so). From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

QGISは寄付者およびサステイニングメンバーによって支えられています。プロジェクトに大小を問わず財政的な貢献をしてくださった寄付者の最新リストは [寄付者一覧]({{< ref "/funding/donate/donors.md" >}}) でご覧いただけます。公式のサステイニングメンバーになることをご希望の方は、詳細について [サステイニングメンバーページ]({{< ref "/funding/membership.md" >}}) をご覧ください。QGISへのご支援は、半年ごとの開発者ミーティングの開催、プロジェクトインフラの維持、およびバグ修正活動の資金として活用されます。現在のサポーターの完全なリストを以下に掲載します。すべてのサポーターの皆様に心より感謝申し上げます！
 
 
 

{{<fund type="active" >}}

QGIS はフリーのソフトウェアです。利用する上で金銭を支払う義務はありません。実際、私たちは利用者の財政状況や社会的地位にかかわらず、より多くの人に QGIS を利用して欲しいと思っています。私たちは地理空間的な意思決定ツールによって人々が力を持つことが、全人類の社会をより良くすると信じています。

![image1](images/projects/750d7d9b7e9dbd498202c4b1288a0cbceb1cd65b.png)

{{<table-of-contents >}}
## 一般情報
### 機能: Flatpak
QGIS is now available as a flatpak application on [flathub](https://flathub.org/apps/search/qgis) Flatpak (formerly xdg-app) is a software utility for software deployment, package management, and application virtualization for Linux desktop computers. It allows users to install different QGIS versions on linux without having to recompile or use Docker. It is a full package with all libraries included, and it uses its own user profile locations. So you\'ll need some disk space and new habits working with flatpak, but it rocks!

[![image28](images/entries/48295bdab734a17ef03ea6bacf182708618e0980.webp)](images/entries/48295bdab734a17ef03ea6bacf182708618e0980.webp)

This feature was funded by [Aleix Pol](https://github.com/aleixpol)

This feature was developed by [Aleix Pol](https://github.com/aleixpol)
### 機能:SVGファイルはプロジェクトとシンボルに埋め込みできるようになりました
シンボロジ、ラベル等に利用するSVGイメージを直接プロジェクトファイルに埋め込むことができるようになりました(またQMLスタイルやQPT印刷テンプレートも埋め込めます）ここではsvgを 標準的なbase64でエンコーディングしたもので埋め込みをしています。

追加機能で、埋め込まれたファイルはプロジェクトから解凍されてシンボルとディスク上のSVGファイルとして戻すことができます。

This feature was funded by [SMEC/SJ](http://smec.com)

This feature was developed by [Nyall Dawson](https://north-road.com)
### 機能: OpenCL を使ったアクセラレーション
This feature was funded by [QGIS.org](https://qgis.org)

This feature was developed by [Alessandro Pasotti](https://qgis.org)
## 計算式
### 機能: 新しい式用関数と変数
多くの新しい式用関数はQGIS3.4では追加されました。これらには配列やマップ（辞書）オブジェクトを操作する便利な関数が含まれています。
- **json_to_map**: Converts a JSON encoded string value to a map (dictionary) type object
- **map_to_json**: Converts a map (dictionary) type object to a JSON encoded string value
- **hstore_to_map**: Converts a hstore value to a map (dictionary) type object
- **map_to_hstore**: Converts a map (dictionary) type object to a hstore value
- **array_foreach** : Loops over an array and executes an expression on each item in the array, returning a new array containing each calculated value
- **array_filter** : Filters an array according to an expression
- **raster_value**: Returns a value sampled from a raster layer at a specified point
- **to_dms**: Converts a numeric value to a Degrees, Minutes, Seconds formatted string
- **to_dm**: Converts a numeric value to a Degrees, Minutes formatted string
- **line_substring**: Returns the portion of a line (or curve) geometry which falls between the specified start and end distances (measured from the beginning of the line). Z and M values are linearly interpolated from existing values.
- **generate_series(start,stop,step)**: Creates an array containing a sequence of numbers.

さらに、いくつかの新しい変数もQGIS式内で使用できるようになりました:
- **\@canvas_cursor_point**: Contains a point value representing the current position of the mouse cursor within the main map canvas
- **\@map_layers**: Contains an array of all layers which are visible within the map
- **\@map_layer_ids**: Contains an array of all layer IDs for layers visible within the map

[![image2](images/entries/ced45b9dd1f58c80aef504344f515a28e33e9e4a.webp)](images/entries/ced45b9dd1f58c80aef504344f515a28e33e9e4a.webp)

This feature was developed by [Etienne Trimaille, Matteo Ghetta, Matthias Kuhn, Mathieu Pellerin, Nyall Dawson](https://qgis.org)
### 機能: 式ビルダにおけるコード補完機能
式エディタにおけるコードの自動保管機能。
- 変数,関数名とフィールド名は式を書いている時に提案と自動挿入が行われます。
- 関数のパラメータはそれらが書き込みされる間表示されます

[![image3](images/entries/df385d837684dcb42633c66b5c566925803f3406.gif)](images/entries/df385d837684dcb42633c66b5c566925803f3406.gif)

This feature was funded by [OPENGIS.ch](https://www.opengis.ch/)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](https://www.opengis.ch/)
## ツール
### 機能:既存ポリゴンを利用した地物の同定または選択機能
Often it is useful to select/identify features that are covered by an existing polygon. For this, users can use \"Select Features by Polygon\" and \"Identify Features by Polygon\" tools, but it was necessary to manually trace the polygon of interest. This new feature allows user to right click on the map and pick an existing polygon feature at that location from popup menu - that polygon will be used as input for selection or identification.

[![image4](images/entries/ee07ddaa42114f923a4fae5429bd8d2f93e66ce5.webp)](images/entries/ee07ddaa42114f923a4fae5429bd8d2f93e66ce5.webp)

この機能は Leicestershire County Council によって資金提供されました

This feature was developed by [Peter Petrik (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
## ユーザーインタフェース
### 機能: ファイルマネージャーにおけるエキスポートファイルの自動選択
Whenever a message bar item links to a created file (e.g. after exporting a layout or map layer), the link will now directly open the folder containing this file within the operating system file browser AND pre-select the created file. It\'s a super-handy shortcut speeding up file operations after an export from QGIS!

[![image5](images/entries/0ccd6bdae5b0df6d65c259ef08f38032fe4ee34f.gif)](images/entries/0ccd6bdae5b0df6d65c259ef08f38032fe4ee34f.gif)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: New \"Open Directory\" option for disabled welcome page projects
この新機能ではディレクトリの変更，喪失，名前を変更によってウェルカムページから開くことができなくなってしまったファイルに対し，もとのディレクトリに最も近いパスを右クリックから開くことが可能になりました。

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能: スクラッチレイヤUXの向上
Temporary Scratch Layers in QGIS can be very handy when a \"throw-away\" layer is needed, such as when pre-processing data in multiple steps. However, they can be a trap for uniformed users who may not realise that the contents of the layer will be permanently lost when the current QGIS project is closed. Accordingly, a new indicator icon has been added which shows up next to any temporary scratch layers in the layer tree, making it immediately clear which layers are temporary only.

It\'s also much easier to transition these temporary layers to permanent disk-based formats. You can either click the new indicator icon or select \"Make Permanent\" from the layer context menu. QGIS will then prompt for a location to save the temporary layer to, then replaces it in place (keeping the same layer ID, style, form settings, etc).

[![image6](images/entries/135600d5ba3c15dd0b4b6386cdd5cbf5a59ce3c2.webp)](images/entries/135600d5ba3c15dd0b4b6386cdd5cbf5a59ce3c2.webp)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能: タスクマネージャーの向上
The QGIS task manager widget (shown in the status bar whenever a background task is running) now shows an estimated time remaining and completion time for long-running background tasks. This Estimated Time of Arrival is calculated using a simple linear interpolation based on the task\'s elapsed time and current progress, and allows users to know whether they\'ve only got time to make an instance coffee in the office kitchen or walk round the block for a proper barista made coffee before that long processing task completes\...

Additionally, QGIS uses the standard operating system progress reporting mechanisms on more platforms and occasions in QGIS 3.4. Some long running tasks (which don\'t run in the background) such as atlas exports now show their progress via the operating system mechanism, and throw up handy completion notifications.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能: ローカルのベクタとラスタデータセットのハイパーリンクを情報パネルに表示しました
For local vector and raster datasets, the Information tab within the layer properties dialog now features source file path hyperlinks. Upon clicking on the hyperlink, the system\'s file navigator will open and automatically highlight the dataset.

[![image7](images/entries/6891c502c6506b88398e9bfb3e266598823c5765.webp)](images/entries/6891c502c6506b88398e9bfb3e266598823c5765.webp)

This feature was funded by [iMhere Asia](https://www.imhere-asia.com/)

This feature was developed by [Mathieu Pellerin](https://www.imhere-asia.com/)
### 機能: スタイルマネージャの改良
QGISスタイルマネージャダイアログ(ユーザが独自のシンボルライブラリやカラーランプを管理できます)は現在ノンモーダルモードで開くのでメインQGISウインドウと一緒に開いて利用できます(レイアウトマネージャダイアログやプリントレイアウトデザインウィンドウと同様です)。

We\'ve also improved the preview of symbols within the Layer Styling dock, adding a toggle to switch between a large icon view and a detailed list view of symbols. Hovering over symbols (and colors!) now shows a large preview of the symbol. Finally, we\'ve made symbol lists more hi-dpi friendly.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能:ブラウザパネルのインターフェースと操作性を洗練させました
このリリースではブラウザパネルユーザーインターフェースと操作性の改良に多くの作業が行われました。そこには高解像度の修正,圧縮されたベクタ/ラスタデータセットの改良とアイコンセットのリフレッシュが含まれます。

機能の追加されています。そこにはブラウザコンテキストメニューから新しいディレクトリを作成する機能も含みます。ブラウザではSQL Server接続オプションについてさらに完璧な領域に進化しています。それらはすでに他のデータベース接続では利用可能なオプションです。

[![image8](images/entries/579042fca8a22be300449c3b55629fced75316b8.webp)](images/entries/579042fca8a22be300449c3b55629fced75316b8.webp)

この機能はMathieu Pellerin (iMHere Asia), Nyall Dawson (North Road) によって開発されました
### 機能: QML チャートとドローイングウィジェット
属性を利用したチャートやテクニカルドローイングのような魅力的で対話型のアイテムを表示するための新しいタイプのベクタレイヤフォームウィジェットがQGIS3.4で追加されました。ウィジェットは柔軟に設定ができテンプレートの例と式をサポートします。

[![image9](images/entries/1bc81f284db61667934e9a7e0969303f59fe06d2.gif)](images/entries/1bc81f284db61667934e9a7e0969303f59fe06d2.gif)

この機能は [QGIS Project](https://qgis.org/) から資金提供を受けています

この機能は [David Signer and Matthias Kuhn (OPENGIS.ch)](https://www.opengis.ch) によって開発されました
## シンボロジ
### 機能: メッシュレイヤスタイリング
- プロパティパネルでメッシュレイヤにデータセットを追加できます
- プロパティパネルに情報とソースパネルができました
- アクティブデータセットの選択(プロパティまたはスタイリングパネル)
- コンター/スカラーのスタイル(プロパティまたはスタイリングパネル)
- メッシュフレームのスタイリング(プロパティまたはスタイリングパネル)
- ベクタ矢印のスタイリング(プロパティまたはスタイリングパネル)

This feature was funded by [Lutra Consulting](https://www.lutraconsulting.co.uk/)

この機能は [Peter Petrik (Lutra Consulting)](https://www.lutraconsulting.co.uk/blog/2018/10/18/mdal/) によって開発されました
### 機能:段彩レンダラにおける対称分類
This feature was funded by <https://github.com/pierreloicq>

This feature was developed by <https://github.com/pierreloicq>
### 機能: 部分的なQMLのエクスポートとインポート
When exporting and importing styles to and from `.qml` files it is now possible to select a subset of sections. This allows to save and restore parts of a layer configuration while omitting others. For example, it\'s possible to export only the symbology of a layer and when importing this QML style file into a layer, any configuration on the forms and widgets or other properties are unaffected. It is also possible to only handle single sections of a style when using copy/paste.

[![image10](images/entries/93836361649c4b182b46e143014d7f30be674187.webp)](images/entries/93836361649c4b182b46e143014d7f30be674187.webp)

This feature was funded by [qwat group](http://qwat.org/)

This feature was developed by [Denis Rouzaud (OPENGIS.ch GmbH)](https://www.opengis.ch)
## デジタイズ
### 機能: GPSトラッキングの改良
QGIS 3.4 extends the inbuilt GPS tracking support, adding \"acquisition interval\" and \"distance threshold\" parameters. These options can be used to keep the cursor stationary when the receiver is in static conditions.

This feature was funded by [Andrea Rossi](https://github.com/rossia)

This feature was developed by [Andrea Rossi](https://github.com/rossia)
### 機能: 先進的なデジタイズドックにおけるスナップ対応共通角の追加
コンストラクションモード時のスナップに5/10/15/18/22.5°のオプションが追加されました。

[![image11](images/entries/7c32c14544fb2f45646ea03f794e5124b4d4f9be.webp)](images/entries/7c32c14544fb2f45646ea03f794e5124b4d4f9be.webp)

This feature was funded by [lbartoletti](https://github.com/lbartoletti)

This feature was developed by [lbartoletti](https://github.com/lbartoletti)
### 機能:頂点ツールがカレントレイヤのみで動作可能になりました
The new vertex is a lot more productive now. It can move vertices of all editable layers at once, which is great to preserve cross layers topology. However in many cases, many of us don\'t want to modify all layers at once. We added a variation of the vertex map tool just for that.

[![image12](images/entries/7c03fe883ce1558385fdc922797ab3a7342136d0.webp)](images/entries/7c03fe883ce1558385fdc922797ab3a7342136d0.webp)

This feature was funded by [Oslandia](https://oslandia.com)

This feature was developed by [Paul Blottiere (Oslandia)](https://oslandia.com/en/home-en/)
### 機能: 反転ラインマップツールの追加
A long awaited feature ! No more external plugin or algorithm to reverse a line\'s direction!

[![image13](images/entries/988902221b0384cd96f880633f9d822faaad6903.webp)](images/entries/988902221b0384cd96f880633f9d822faaad6903.webp)

This feature was funded by [OSLANDIA](https://oslandia.com)

This feature was developed by [Loïc Bartoletti](https://github.com/lbartoletti)
### 機能: ジオメトリの精度
ベクタレイヤに精度管理オプションができました。精度は位置のノードを保存する精度を定義します。新規または編集中のそれぞれのノードはこの解像度でグリッドにスナップされます。デジタイズ中にはこのグリッドがユーザにガイドとして表示されます。

[![image14](images/entries/4dc31694598d9c507be8ed1110c0c4a494b997ec.gif)](images/entries/4dc31694598d9c507be8ed1110c0c4a494b997ec.gif)

This feature was funded by [Kanton Solothurn](https://www.so.ch/verwaltung/bau-und-justizdepartement/amt-fuer-geoinformation/)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](https://www.opengis.ch)
### 機能:重複するノードの自動削除
ベクタレイヤでジオメトリの追加または編集を行っている時にQGISでは自動的に重複するノードをジオメトリから削除することができるようになりました。このオプションはベクタレイヤのデジタイジングタブで設定することができます。

This feature was funded by [Kanton Solothurn](https://www.so.ch/verwaltung/bau-und-justizdepartement/amt-fuer-geoinformation/)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](https://www.opengis.ch)
### 機能:ジオメトリの妥当性チェック
このオプションが有効な場合新規または編集されるそれぞれのジオメトリの妥当性がチェックできます。この機能によって利用している編集セッションでエラーがあるジオメトリが生成された場合ユーザと明瞭に対話できます。

[![image15](images/entries/f5eee0b5a59923d41b427c9acc432b4c4f86da01.webp)](images/entries/f5eee0b5a59923d41b427c9acc432b4c4f86da01.webp)

This feature was funded by [Kanton Solothurn](https://www.so.ch/verwaltung/bau-und-justizdepartement/amt-fuer-geoinformation/)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](https://www.opengis.ch)
### 機能: 編集中のトポロジーチェック
トポロジーチェックは1レイヤーに対して実行できます。新規に追加されたまたは編集されたジオメトリに対し処理を実行します。この処理は対象レイヤ保存されたときとジオメトリバリデーションパネルのトポロジーチェックのボタンがクリックされた時に実行されます。

下記のチェックができます。
- ギャップ
- オーバーラップ
- 近傍のポリゴンの消失してしまった頂点

This builds on top of the functionality of the geometry checker plugin which was implemented by [Sourcepole](https://sourcepole.ch).

[![image16](images/entries/a706012a7afb489573f08133f5885fe5bc1a3660.gif)](images/entries/a706012a7afb489573f08133f5885fe5bc1a3660.gif)

This feature was funded by [Kanton Solothurn](https://www.so.ch/verwaltung/bau-und-justizdepartement/amt-fuer-geoinformation/)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](https://www.opengis.ch)
## データ管理
### 機能:QGISプロジェクトの翻訳
Like QGIS and the plugins, the projects are translated with the Qt translation process. Means, it makes the translation according to a Qt Compiled Translation Source File (`.qm` file). When the user opens a project, QGIS checks for a `.qm` file laying in the same folder like the `.qgs` file, having the same name like the `.qgs` file and having the language-code as postfix of the users language (the language configured in the QGIS settings). To create the translation, in the project settings, there is an option to generate the `.ts` file, that can edited by programs like Qt Linguist or Transifex.

More information in [this blog post](https://new.opengis.ch/2018/09/11/qgis-speaks-a-lot-of-languages/)

This feature was funded by [QGIS Usergroup Switzerland and QGEP Project](https://www.qgis.ch/en)

This feature was developed by [David Signer (OPENGIS.ch)](https://www.opengis.ch/)
### 機能: 属性テーブルのドックモードを場合によって切り替えできます
A button has been added to the Attribute Table toolbar for switching between docked and window mode on demand. Previously users had to change an option in the settings dialog and open a new table in order to switch between docked/undocked mode, but that\'s painful if you decide *after* a table is already open that you\'d like to dock/undock it\...!

[![image17](images/entries/2ed512377b90aed08dc73bb7b3ea17ae5c9f4708.gif)](images/entries/2ed512377b90aed08dc73bb7b3ea17ae5c9f4708.gif)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能:全てのレイヤを縦断して検索するための新しいロケータフィルタ
A new locator filter has been added which allows users to search across *all* layers in their project, by the layer\'s display expression.

The filter can be activated by using the prefix \'af\', or by making it a default search via QGIS options -\> Locator -\> Features In All Layer. Display expressions are defined in the vector layer properties under the display tab. Individual layers can be marked as not searchable in the Project Properties dialog, under the Data Sources tab.

[![image18](images/entries/0e99950042f20317f1974b5f2f999cbd9233b47c.webp)](images/entries/0e99950042f20317f1974b5f2f999cbd9233b47c.webp)

This feature was funded by [Opengis.ch](https://www.opengis.ch/)

This feature was developed by [Denis Rouzaud](https://www.opengis.ch/)
### 機能: レイヤツリーで削除不可(必須) レイヤを強調表示します
A new indicator \"locked\" icon is shown for any layers marked as \"required\" within the current project. This icon gives users instant feedback that a particular layer cannot be removed from the project.

必須レイヤはプロジェクトプロパティダイアログのデータソースタブで指定できます。

[![image19](images/entries/43cff3e927cdbacf08d61f979891030e48f9a451.webp)](images/entries/43cff3e927cdbacf08d61f979891030e48f9a451.webp)

This feature was funded by [Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) within ERIKUS project](https://www.arpa.piemonte.it/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk) and [Faunalia](https://www.faunalia.eu)
### 機能:既存のGeopackageにラスタレイヤを追加できます
When saving a raster layer to GeoPackage database, it\'s now possible to append the layer to an existing file.

[![image20](images/entries/7417555bb52774a5b522ec6d3034d6fd22077732.webp)](images/entries/7417555bb52774a5b522ec6d3034d6fd22077732.webp)

This feature was funded by [Borys Jurgiel](https://github.com/borysiasty)

This feature was developed by [Borys Jurgiel](https://github.com/borysiasty)
## フォームとウィジェット
### 機能:QGIS値のリレーションウィジェット内の(ドリルダウン(カスケーディング）フォーム
New functions and logic in QGIS "Value Relation Widgets", allowing the implementation of complex, dynamic filters within QGIS attribute forms. The functionality can be used to implement "drill-down" forms within QGIS, where the values available in one field depend on the values of other fields:

[![image21](images/entries/5990ff168d5b6b41176de4fa487964b97c32fafc.gif)](images/entries/5990ff168d5b6b41176de4fa487964b97c32fafc.gif)

This feature was funded by [QGIS community through crowd-funding](https://north-road.com/drill-down-cascading-forms/)

この機能は Alessandro Pasotti (with North Road) によって開発されました
## マップコンポーザー
### 機能: 3Dマップアイテム
これは3Dのマップビューをプリントレイアウトへ追加する機能です。

[![image22](images/entries/413f4a9377731af02f3fe815bf3b7e70ac508d1c.webp)](images/entries/413f4a9377731af02f3fe815bf3b7e70ac508d1c.webp)

This feature was funded by [QGIS community through crowd-funding](https://www.lutraconsulting.co.uk/crowdfunding/more-qgis-3d/)

This feature was developed by [Lutra Consulting](https://www.lutraconsulting.co.uk/)
## プロセシング
### Feature: New \"Edit in place\" mode
Thanks to a large number of [generous backers](https://north-road.com/edit-features-in-place-using-qgis-spatial-operations-campaign/), a crowdfunded \"edit in place\" mode was added to Processing for 3.4. When a vector layer is active and editable, this mode allows users to execute suitable algorithms directly on the features from the layer, modifying their attributes and geometries in-place. All edits are added to the layer's "edit buffer", so you can easily undo and redo the changes before saving them back to the data source.

For those power users who perform frequent data edits, this functionality is also exposed via QGIS 3.0's "Locator bar" (that "type to locate" bar which sits in the bottom-left corner). Typing 'ef' ("edit features") followed by the name of the corresponding operation allows you to perform the edits directly via the keyboard. E.g.
- 多数のライン地物を選択します
- Ctrl + K を押します (ロケータバーをアクティブにします)
- Type "ef reverse"
- Press enter -- the selected line features will be reversed immediately!

[![image23](images/entries/bdfd9b4a3d367378786fd358e13c475e7fb05816.gif)](images/entries/bdfd9b4a3d367378786fd358e13c475e7fb05816.gif)

This feature was funded by [Crowdfunding campaign](https://north-road.com/edit-features-in-place-using-qgis-spatial-operations-campaign/)

This feature was developed by [North Road](https://north-road.com)
### 機能:モデルをプロジェクトに保存する
Some Processing models are so intrinsically linked to the logic inside a particular project that they have no meaning (or are totally broken) outside of that project (e.g. models which rely on the presence of particular map layers, relations, etc). Accordingly, from QGIS 3.4, Processing models can be stored inside QGIS project files. Any models stored within a project are made available as soon as that project is opened. This also avoids cluttering up the \"global\" model provider with models which make no sense, and makes it easier to distribute a single project all relevant models included.

Models are stored inside projects by clicking the new \"Embed in Project\" button in the Modeler dialog toolbar. Models can be removed from a project from the model\'s right click menu in the toolbox.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能: ラスタ値のサンプル
ラスタレイヤのある1点の値をサンプリングする新しいアルゴリズムを追加しました。

[![image24](images/entries/835925fb7c793d7e56a8c21a49408cd2542c973c.webp)](images/entries/835925fb7c793d7e56a8c21a49408cd2542c973c.webp)

This feature was funded by [Faunalia](https://www.faunalia.eu)

This feature was developed by [Matteo Ghetta (Faunalia)](https://www.faunalia.eu)
### Feature: New \'Raster pixels to polygons\' algorithm
このアルゴリズムはラスタレイヤをベクタレイヤに変換します。ラスタレイヤの各ピクセルを1つのポリゴンとみなし，ラスターの持つバンドの値をひとつのフィールドに変換します。

This feature was funded by [SMEC/SJ](http://smec.com)

This feature was developed by [Nyall Dawson](https://north-road.com)
### 機能: K平均クラスタリングアルゴリズム
QGIS 3.4 adds a native \"k-means clustering\" algorithm. Based on a port of PostGIS\' ST_ClusterKMeans function, this algorithm adds a new cluster ID field to a set of input features which identifies the feature\'s cluster based on a k-means clustering approach. If non-point geometries are used as input, the clustering is based off the centroid of the input geometries.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能: DBSCANクラスタリングアルゴリズム
このネイティブアルゴリズムは2Dのポイント地物に対するクラスターアプローチを基盤としてDBSCAN密度の最適化を実装したものです。

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能:アルゴリズムの改良
既存のプロセッシングアルゴリズムに対する以下のような改良があります:
- *逆方向ラインの検出* アルゴリズムではマルチラインジオメトリを入力に利用できるようになりました
- *ラインの拡張*: ダイナミック(データで定義された)な開始と終了の距離指定がサポートされました
- *オフセットライン*: ダイナミックなオフセット距離がサポートされました
- *フィールド値による結合* と *場所による結合* アルゴリズムではオプションでマッチしないレコードの出力が可能になりました
- *フィールド値による結合* ではマッチ/アンマッチした地物の数をレポートします

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能: Mを利用した頂点フィルタとZを利用した頂点フィルタアルゴリズム
MまたはZの値を使ってライン/ポリゴンの頂点をフィルタする２つの新しいアルゴリズムができました。M/Zの値の最小と最大を入力できます、もし頂点の値がその範囲の外の場合は出力ジオメトリからその頂点は除去されます。フィルタの最小値と最大値はデータで定義することも可能です。ですからフィルタは地物毎に変えることができます。

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: \"Array of Translated Features\" algorithm
この新しいアルゴリズムはあるレイヤ中の地物のコピーを作成します。コピーは地物の複数の座標変換(オフセット）単位に作成されます。それぞれのコピーはx/y/z/m軸のプリセットの合計だけ移動します。

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: \"Array of offset (parallel) lines\" algorithm
このアルゴリズムは、入力レイヤの線からバッファ距離だけ離れたオフセット線を複数作成します。各線は、指定されたステップ距離で順次離れたものです。

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能:度/不明な距離への単位選択機能
アルゴリズムが距離パラメータをメートル/フィート/etc(例.ジオグラフィックでない距離)で持っている場合コンボボックスが追加され単位の選択ができます。

(QGIS doesn\'t (and should **never**) expose this for distances in degrees \-- it\'s up to users in this situation to choose a suitable local projection and reproject their data to match.)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson](https://north-road.com)
### Feature: \"Drape features to z/m\" algorithms
ジオメトリの頂点に z または m の値を設定する新しい２つのアルゴリズムです。その値はラスタバンドから取得されます。オプションで値は（データ定義可能な)スケール値を使ってスケールできます。

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: \"Raster pixels to points\" algorithm
A new \"pixels to points\" algorithm was added in QGIS 3.4, which creates a point feature at the center of every pixel. nodata pixels are skipped.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能: 部分ライン切り出しアルゴリズム
この新しくて非常に要望が多かったアルゴリズムはライン（またはカーブ）の始点と距離(ラインの先頭から計測された）指定でラインの一部分を返します。ZとMの値は既存の値から線形補間されます。

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: \"Interpolate point on line\" algorithm
この新しいアルゴリズムは線（またはポリゴンの外周線)ジオメトリにそって指定距離ごとにポイントジオメトリを作成します。曲線ジオメトリの入力もサポートされています。ZまたはMの値は既存の値を基にして線形補間されます。

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能:k-neighbour 凹包
This feature was funded by <https://qgis.org>

This feature was developed by [Detlev Neumann, Rudi von Staden](https://qgis.org)
### 機能:アルゴリズムをインプリメントしたPythonスクリプトををドラッグアンドドロップとブラウザダブルクリックで実行できます
適切な時にスクリプトはプロセッシングダイアログを起動するでしょう:
- Pythonスクリプトをメインウインドウの上にドラッグしてドロップしてください
- Using the browser panel\'s right-click run script action

[![image25](images/entries/06f359ac4e92e415c502bc5def413563b755d8e8.webp)](images/entries/06f359ac4e92e415c502bc5def413563b755d8e8.webp)

This feature was funded by [iMhere Asia](https://www.imhere-asia.com/)

This feature was developed by [Mathieu Pellerin](https://www.imhere-asia.com/)
### Feature: New GDAL\'s rearrange band algorithm
A new GDAL provider \'Rearrange band\' algorithm was added to the processing toolbox. The algorithm allows to output rasters continuing a subset of a given input raster\'s bands, and offers the possibility to re-order the bands.

[![image26](images/entries/989a55b259fe6fd44640151cf4e2b0f0bb34573b.webp)](images/entries/989a55b259fe6fd44640151cf4e2b0f0bb34573b.webp)

This feature was funded by [iMHere Asia](https://www.imhere-asia.com/)

This feature was developed by [Mathieu Pellerin](https://www.imhere-asia.com/)
### Feature: \"Precalculated\" values for model algorithm parameters
A new option is present for all parameters of using a \"precalculated expression\". This expression is evaluated once before the child algorithm is executed and used during the execution of that algorithm.

This feature was funded by [QGIS](https://qgis.org)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: \"Categorize a layer using a style XML file\" algorithm
This new algorithm sets a vector layer\'s renderer to a categorized renderer using matching symbols from a style database.

A specified expression (or field name) is used to create categories for the renderer, with QGIS creating a category for each unique value within the layer. Each category is individually matched to the symbols which exist within the specified QGIS XML style database. Whenever a matching symbol name is found, the category\'s symbol will be set to this matched symbol.

マッチングはデフォルトで大文字小文字を区別しません。しかし必要があれば大文字小文字を区別するように設定可能です。オプションでカテゴリと描画定義のマッチングで非アルファベット文字を無視するように設定できます。この機能によってカテゴリと描画定義のマッチングの許容度を増やすことができます。

必要があれば描画定義とマッチしなかったカテゴリのリストやカテゴリとマッチしなかった描画定義のリストを出力することができます。

[![image27](images/entries/dbf5d7f496eadfefae1bc300f763e991206fb694.webp)](images/entries/dbf5d7f496eadfefae1bc300f763e991206fb694.webp)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能:スナップジオメトリアルゴリズムの新モード
The new mode \"Snap to anchor nodes (single layer only)\" makes sure that any two vertices of the vector layer are at least at distance given by the threshold value.

このアルゴリズムは、座標が互いに非常に近い場合に数値誤差によって引き起こされる可能性のある位相誤差を防ぐために、交差、ユニオン、差などのベクトルオーバーレイ操作を行うときに便利です。 アルゴリズムを実行した後、以前に有効だったジオメトリが不正になる場合があるため、後でジオメトリ修正アルゴリズムを実行すると便利な場合があります。

This feature was funded by [InaSAFE DFAT](https://www.dfat.gov.au/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
## データプロバイダ
### 機能: OAuth2認証メソッドプラグイン
- 認可コードフロー、インプリシットフローとリソースオーナーグラントフローに対応
- デフォルトの位置から読み出す事前設定を使用した接続が可能です
- QGISを再起動してもアクセストークンが得られるキャッシュ機能を提供します
- 設定のセーブ/ロード

This feature was funded by [Monsanto Company](https://monsanto.com/)

This feature was developed by [Larry Shaffer, Alessandro Pasotti](https://qgis.org)
### 機能: メッシュレイヤ: 新しい形式への対応
メッシュレイヤは、追加要素 (時間やベクトル等)を持つ可変サイズのグリッド上のデータを表現します。MDALの導入で、ユーザは次に挙げるフォーマットをQGISに直接ダウンロードでき、また、他の全ての要素を探索することができます。
- GRIB
- XMDF
- Netcdf

[![image29](images/entries/767a26455fb1a8ad8cab663a52832ef575954483.gif)](images/entries/767a26455fb1a8ad8cab663a52832ef575954483.gif)

This feature was funded by [Lutra Consulting](https://www.lutraconsulting.co.uk/blog/2018/10/18/mdal/)

This feature was developed by [Lutra Consulting](https://www.lutraconsulting.co.uk/)
### 機能: メッシュレイヤ: メッシュレイヤ上の値の識別機能
このAPIで、開発者は、メッシュ要素を調べ、時空間的に値を取得することができます。例えば、メッシュレイヤから時系列プロットを作成することができます。

[![image30](images/entries/45c0ea5d14157275da7153ac31cc41987319e5eb.webp)](images/entries/45c0ea5d14157275da7153ac31cc41987319e5eb.webp)

This feature was funded by [Lutra Consulting](https://www.lutraconsulting.co.uk/)

This feature was developed by [Lutra Consulting](https://www.lutraconsulting.co.uk/)
### 機能: メッシュレイヤー: 異なるベクタとスカラデータセットの選択が可能に
メッシュレイヤーに複数の数量を持っている場合があります。気象情報を持つnetCDFやGRIBがその代表例です。これらの数量はさらに複数の構成要素により成り立っています。例えば、風のデータは風向（スカラ）と風速（グリッド）を持っています。このオプションでは異なる数量であるスカラとグリッドを重ね合わせることが可能です。下の図では温度（グリッド）と風（スカラ）を例示しています。

[![image31](images/entries/74ce47f09e8644a2ce6a8daeae2e37e13615b956.gif)](images/entries/74ce47f09e8644a2ce6a8daeae2e37e13615b956.gif)

This feature was funded by [Lutra Consulting](https://www.lutraconsulting.co.uk/)

This feature was developed by [Lutra Consulting](https://www.lutraconsulting.co.uk/)
### 機能: メッシュレイヤ: ユーザ指定のグリッドでベクタ/矢印の描画が可能になりました
スカラデータが、通常はメッシュ要素の中心か格子で生成されます。スカラデータ表示時には、矢印が薄く見え、しばしば全般の傾向が見えなくなることがあります。このオプションで、矢印がユーザ指定のグリッドで表示できます。拡張スカラ値は実行中に補間が行われ、ユーザ定義のグリッド上に置かれます。

[![image32](images/entries/9eaa1430fee8b738a79936d7df104270e0b7f2a8.webp)](images/entries/9eaa1430fee8b738a79936d7df104270e0b7f2a8.webp)

This feature was funded by [Lutra Consulting](https://www.lutraconsulting.co.uk/)

This feature was developed by [Lutra Consulting](https://www.lutraconsulting.co.uk/)
### 機能: JSON/JSONB型への対応
The reading of PostgreSQL JSON types is supported. JSON Data can be displayed in the widgets as \"Key/Value\" (maps), as \"List\" (arrays) or as text.

[![image33](images/entries/94f82c582268d7966bb1fa140893b63af207dca3.webp)](images/entries/94f82c582268d7966bb1fa140893b63af207dca3.webp)

This feature was funded by [Kanton Solothurn](https://www.so.ch/verwaltung/bau-und-justizdepartement/amt-fuer-geoinformation/)

This feature was developed by [David Signer (OPENGIS.ch)](https://www.opengis.ch)
### 機能: ESRIトークン認証対応
Support has been added to QGIS\' Authentication system for ESRI\'s temporary token based authentication. This allows for connection to ArcGIS Feature and Map Servers via an allocated temporary token.

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能: SQLサーバ - 不正なジオメトリの処理
Recent versions of QGIS have switched to a safer approach to reading SQL Server layers, which automatically checks for geometry validity and repairs geometries when needed. This workaround is required to avoid issues with the design of SQL Server\'s geometry handling, where encountering any rows with invalid geometries can silently abort a request without returning all the features from a layer. Unfortunately, the workaround comes at a significant performance cost.

In QGIS 3.4 a new setting was added to allow users to manually turn off QGIS\' SQL Server invalid geometry handling. Turning on the \"Skip invalid geometry handling\" setting under a SQL Server connection\'s properties causes QGIS to skip all the expensive geometry validation processing, but firmly places the responsibility for ensuring that all features on the database have valid geometries back upon the user/database administrator. **This is a \"use at your own risk\" setting. Improperly enabling this option can lead to missing features and data loss.**

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## QGISサーバー
### 機能: サーバキャッシュがプラグインで管理できるようになりました
デフォルトでは、QGISサーバはWMS GetCapabilities文書をメモリにキャッシュするだけでした。WMTS実装では、タイルをキャッシュする方法を持つことが重要です。しかし、キャッシュマネージャはタイルのキャッシュ以外のためにも開発しています。

キャッシュマネージャ プラグインは、次にあげるもののキャッシュに使われます。
- WMS, WFS, WCS, WMTS GetCapabilities文書
- WFS DescribeFeatureType文書
- WCS DescribeCoverage文書
- WMTS GetTile画像
- WMS GetLegendGraphic画像

次にPythonのキャッシュマネージャクラスを示します。ただし、このクラスはQGISプロジェクトが変更されたかの確認を行いません。

    class PyServerCache(QgsServerCacheFilter):
    
        """ Used to have cache control """
    
        def __init__(self, server_iface):
            super(QgsServerCacheFilter, self).__init__(server_iface)
    
            self._cache_dir = os.path.join(tempfile.gettempdir(), "qgs_server_cache")
            if not os.path.exists(self._cache_dir):
                os.mkdir(self._cache_dir)
    
            self._tile_cache_dir = os.path.join(self._cache_dir, 'tiles')
            if not os.path.exists(self._tile_cache_dir):
                os.mkdir(self._tile_cache_dir)
    
        def getCachedDocument(self, project, request, key):
            m = hashlib.md5()
            paramMap = request.parameters()
            urlParam = "&".join(["%s=%s" % (k, paramMap[k]) for k in paramMap.keys()])
            m.update(urlParam.encode('utf8'))
    
            if not os.path.exists(os.path.join(self._cache_dir, m.hexdigest() + ".xml")):
                return QByteArray()
    
            doc = QDomDocument(m.hexdigest() + ".xml")
            with open(os.path.join(self._cache_dir, m.hexdigest() + ".xml"), "r") as f:
                statusOK, errorStr, errorLine, errorColumn = doc.setContent(f.read(), True)
                if not statusOK:
                    print("Could not read or find the contents document. Error at line %d, column %d:\n%s" % (errorLine, errorColumn, errorStr))
                    return QByteArray()
    
            return doc.toByteArray()
    
        def setCachedDocument(self, doc, project, request, key):
            if not doc:
                print("Could not cache None document")
                return False
            m = hashlib.md5()
            paramMap = request.parameters()
            urlParam = "&".join(["%s=%s" % (k, paramMap[k]) for k in paramMap.keys()])
            m.update(urlParam.encode('utf8'))
            with open(os.path.join(self._cache_dir, m.hexdigest() + ".xml"), "w") as f:
                f.write(doc.toString())
            return os.path.exists(os.path.join(self._cache_dir, m.hexdigest() + ".xml"))
    
        def deleteCachedDocument(self, project, request, key):
            m = hashlib.md5()
            paramMap = request.parameters()
            urlParam = "&".join(["%s=%s" % (k, paramMap[k]) for k in paramMap.keys()])
            m.update(urlParam.encode('utf8'))
            if os.path.exists(os.path.join(self._cache_dir, m.hexdigest() + ".xml")):
                os.remove(os.path.join(self._cache_dir, m.hexdigest() + ".xml"))
            return not os.path.exists(os.path.join(self._cache_dir, m.hexdigest() + ".xml"))
    
        def deleteCachedDocuments(self, project):
            filelist = [f for f in os.listdir(self._cache_dir) if f.endswith(".xml")]
            for f in filelist:
                os.remove(os.path.join(self._cache_dir, f))
            filelist = [f for f in os.listdir(self._cache_dir) if f.endswith(".xml")]
            return len(filelist) == 0
    
        def getCachedImage(self, project, request, key):
            m = hashlib.md5()
            paramMap = request.parameters()
            urlParam = "&".join(["%s=%s" % (k, paramMap[k]) for k in paramMap.keys()])
            m.update(urlParam.encode('utf8'))
    
            if not os.path.exists(os.path.join(self._tile_cache_dir, m.hexdigest() + ".png")):
                return QByteArray()
    
            img = QImage(m.hexdigest() + ".png")
            with open(os.path.join(self._tile_cache_dir, m.hexdigest() + ".png"), "rb") as f:
                statusOK = img.loadFromData(f.read())
                if not statusOK:
                    print("Could not read or find the contents document. Error at line %d, column %d:\n%s" % (errorLine, errorColumn, errorStr))
                    return QByteArray()
    
            ba = QByteArray()
            buff = QBuffer(ba)
            buff.open(QIODevice.WriteOnly)
            img.save(buff, 'PNG')
            return ba
    
        def setCachedImage(self, img, project, request, key):
            m = hashlib.md5()
            paramMap = request.parameters()
            urlParam = "&".join(["%s=%s" % (k, paramMap[k]) for k in paramMap.keys()])
            m.update(urlParam.encode('utf8'))
            with open(os.path.join(self._tile_cache_dir, m.hexdigest() + ".png"), "wb") as f:
                f.write(img)
            return os.path.exists(os.path.join(self._tile_cache_dir, m.hexdigest() + ".png"))
    
        def deleteCachedImage(self, project, request, key):
            m = hashlib.md5()
            paramMap = request.parameters()
            urlParam = "&".join(["%s=%s" % (k, paramMap[k]) for k in paramMap.keys()])
            m.update(urlParam.encode('utf8'))
            if os.path.exists(os.path.join(self._tile_cache_dir, m.hexdigest() + ".png")):
                os.remove(os.path.join(self._tile_cache_dir, m.hexdigest() + ".png"))
            return not os.path.exists(os.path.join(self._tile_cache_dir, m.hexdigest() + ".png"))
    
        def deleteCachedImages(self, project):
            filelist = [f for f in os.listdir(self._tile_cache_dir) if f.endswith(".png")]
            for f in filelist:
                os.remove(os.path.join(self._tile_cache_dir, f))
            filelist = [f for f in os.listdir(self._tile_cache_dir) if f.endswith(".png")]
            return len(filelist) == 0
    
QGISサーバのキャッシュマネージャにこれを追加する方法は次の通りです。

`servercache = PyServerCache(server_iface) server_iface.registerServerCache(servercache, 100)`

This feature was funded by [Ifremer](https://wwz.ifremer.fr/)

This feature was developed by [3Liz](https://3liz.com)
### 機能: WMTS 1.0.0対応
QGISサーバ 3.4はOGC標準のWMTS 1.0.0に対応しています。

QIGSプロジェクトプロパティでは、ユーザは次の通り定義できます。
- プロジェクトのどの部分がWMTS標準を通して発行されなければならないか (プロジェクト全体、レイヤグループ、またはレイヤ)
- タイルの最小スケール

QGISサーバはWMSで定義されたCRS定義をWMTSに再使用します。

タイルキャッシュの管理のために、QgsServerCacheFilterクラスを持つQGISサーバプラグインがインストールされていなければならず、かつ、QGISサーバにロードされていなければなりません。

[![image34](images/entries/d0d72b47494e231b98bf3169fcbe34ca22d0624d.webp)](images/entries/d0d72b47494e231b98bf3169fcbe34ca22d0624d.webp)

This feature was funded by [Ifremer](https://wwz.ifremer.fr/)

This feature was developed by [3Liz](https://3liz.com)
### 機能: WMTSの最小スケールの定義機能の追加
This feature was funded by <https://github.com/rldhont>

This feature was developed by <https://github.com/rldhont>
### 機能: QGISサーバの標準エラー出力へのログ出力対応
It\'s now possible to configure QGIS Server to make it write its logs to stderr. This is done by setting the QGIS_SERVER_LOG_FILE env var to the special value \"stderr\".

This feature was funded by [OSLANDIA](https://oslandia.com)

This feature was developed by [Eric Lemoine](https://github.com/elemoine)
## プラグイン
### 機能: プラグインマネージャ内の暗号化ZIPへの対応
プラグインマネージャはローカルのZIPファイルから、暗号化されていてでも、インストールできます。

[![image35](images/entries/1bfc11325b9afa06d3196603749e1786f7922ffd.webp)](images/entries/1bfc11325b9afa06d3196603749e1786f7922ffd.webp)

This feature was funded by [Borys Jurgiel](https://github.com/borysiasty)

This feature was developed by [Borys Jurgiel](https://github.com/borysiasty)
### 機能: GeoPackageのオフライン編集
オフライン編集機能で、エクスポートでSpatiaLiteかGeoPackageファイルをオフライン使用のために作成するかどうかを選択できるようになりました。

This feature was funded by [Oester Messtechnik](https://messtechnik.ch/)

This feature was developed by [David Signer (OPENGIS.ch)](https://www.opengis.ch)
## プログラマビリティ
### 機能: QgsSpatialIndexKDBush
A very fast static spatial index for 2D points based on a flat KD-tree, using <https://github.com/mourner/kdbush.hpp>

Compared to QgsSpatialIndex, this index: - supports single point features only (no multipoints) - is static (features cannot be added or removed from the index after construction) - is much faster! - supports true \"distance based\" searches, i.e. return all points within a radius from a search point

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能: ラスタの与えられたポイントでの効率的なサンプリングに使われるQgsRasterDataProvider::sampleメソッド
This is an alternative to the `QgsRasterDataProvider::identify` method, which is less efficient but more powerful

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能: 曲線サブストリングを返す新しいジオメトリAPI
ラインストリング/曲線ジオメトリから部分線を検索するのが容易となる新しいPyGIS APIが追加されました。

`QgsCurve::curveSubstring - Returns a new curve representing a substring of a curve, from a start distance and end distance.`

If z or m values are present, the output z and m will be interpolated using the existing vertices\' z or m values. The method also handles curved geometries without loss or segmentation.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能: sipモジュールAPIの変更
Due to upstream changes within the PyQt/sip library, the recommended way to import this module has changed in QGIS 3.4. For maximum portability, instead of directly calling: `import sip` plugins should instead use: `from qgis.PyQt import sip` Using this newer style import will ensure that the code works correct across all platforms and remains functional in future QGIS versions.
### 機能: ベクタデータプロバイダ
ピュアPythonで、ベクタデータプロバイダの生成を可能にするAPIとサンプルプロバイダとテストの開発です。

[![image36](images/entries/dbae71a0ccad069280a263fabddf3452b8165ca3.webp)](images/entries/dbae71a0ccad069280a263fabddf3452b8165ca3.webp)

この機能はGood willが資金提供しました

この機能はAlessandro Pasottiが開発しました
## 三次元機能
### 機能: ナビゲーションの改良
This will update camera\'s view center as the camera moves around. Before the view center would be always at the zero elevation, which means that with terrain further away from zero elevation tilting and rotation of camera would feel weird due to the center point being far away.

ページアップ/ダウンキーでカメラを上/下に移動できるようになりました

Ctrl+方向キー/マウスで姿勢を保持したカメラの移動

[![image37](images/entries/a1b22a29fc363ffc90be8f98a991913148164ef2.gif)](images/entries/a1b22a29fc363ffc90be8f98a991913148164ef2.gif)

This feature was funded by [QGIS community through crowd-funding](https://www.lutraconsulting.co.uk/crowdfunding/more-qgis-3d/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### 機能: アニメーション
キーフレーム (特定時刻のカメラ姿勢)の集合に基づいたアニメーションを作成できるようになりました。キーフレーム間のカメラの位置/回転は補完されます。

キーフレームの作成には、まず、カメラの回転、ズーム、移動によるシーン設定を行います。次にフレームに任意の時刻を割り当てます。キーフレーム間の補間には複数のメソッドがあります。

[![image38](images/entries/006592e0cf0245a829d451988d178c5f07ce5560.gif)](images/entries/006592e0cf0245a829d451988d178c5f07ce5560.gif)

This feature was funded by [QGIS community through crowd-funding](https://www.lutraconsulting.co.uk/crowdfunding/more-qgis-3d/)

This feature was developed by [Martian Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### 機能: 3次元ラインストリングのシンプル描画
この3次元ライン描画モードでは、ラインにバッファリングをかけてポリゴンに変換してメッシュとして描画するのでなくOpenGLライン描画が使われます。

The advantage is that the 3D lines do not loose their Z coordinate which is the case currently with \"ordinary\" 3D rendering after buffering.

The disadvantage is that the lines cannot be wide (supported in Qt3D only since 5.10, but even then their rendering won\'t have nice joins/caps) and only ambient color is used from the material.

[![image39](images/entries/d28d6a8023fa5fbd306f6b31f0545ff71112009f.webp)](images/entries/d28d6a8023fa5fbd306f6b31f0545ff71112009f.webp)

This feature was funded by [Lutra Consulting](https://www.lutraconsulting.co.uk/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### 機能: 3次元ビュー用マップ識別ツール
3次元地図に新しい識別ツールを導入しました。このツールを使うと、3次元シーンから地物を調査することができます。

[![image40](images/entries/88fc4584f5ec10e1112813c133bf40f481af9e88.gif)](images/entries/88fc4584f5ec10e1112813c133bf40f481af9e88.gif)

This feature was funded by [Department of Environment, Land and Infrastructure Engineering (DIATI)](https://www.faunalia.eu/en/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk) and [Faunalia](https://www.faunalia.eu)
### 機能: 試験的なPython API
QGIS 3次元のクラスの一部は、Python開発者が利用できるようになりました。地図レイヤの3次元描画と、マテリアルカラーのような3次元シンボルの読み取り/書き込みプロパティとを、参照または変更できるようになりました。現時点ではAPI は実験的なもので、将来の3. xで変更されるかも知れませんのでご注意下さい。

This feature was funded by [Lutra Consulting](https://www.lutraconsulting.co.uk/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)

{{<content-end >}}
