---
HasBanner: false
draft: false
releaseDate: '2013-09-09'
section: project
sidebar: true
title: QGIS 2.0 の変更履歴
type: visual-changelog

---
{{<content-start >}}
# QGIS 2.0 の変更履歴{#changelog20 }
リリース日: 2013-09-09

{{<table-of-contents >}}
## 解析ツール
### 機能：プロセシングコマンダー
ジオプロセシング機能に素早くアクセスするために、単にプロセシングコマンダー（はCtrl + Alt + M）を起動し、あなたが探しているツールの名前を入力し始めます。コマンダーはあなたに利用可能なオプションを表示し、あなたのためにそれらを起動します。これ以上のツールを見つけるために、メニューを検索しません。彼らはあなたの指先に今あります。

![image1](images/processing_commander_2.png)
### 機能：ヒートマッププラグインの改善
ヒートマッププラグインは、ヒートマップのはるかに高速に作成して、その結果、多くの改良と最適化を見てきました。また、今、カーネル関数は、ヒートマップを作成するために使用されているのかを選択できます。

![image2](images/Selection_027.png)
### 機能：プロセッシングサポート
The SEXTANTE project has been ported to and incorporated into QGIS as core functionality. SEXTANTE has been renamed to \'Processing\' and introduces a new menu in QGIS from where you can access a rich toolbox of spatial analysis tools. The processing toolbox has incredibly rich functionality - with a python programming API allowing you to easily add new tools, and hooks to provide access to analysis capabilities of many popular open source tools such as GRASS, OTB, SAGA etc.

![image3](images/Selection_028.png)
### 機能: プロセシングモデラー
新しい処理フレームワークの大きな特徴の1つは、ツールをグラフィカルに組み合わせる機能です。** Processing Modeller **を使用すると、一連の小さな単一目的モジュールから複雑な分析を構築できます。これらのモデルを保存し、より複雑なモデルのビルディングブロックとして使用することができます。すばらしいパワーがQGISに統合され、使いやすい！

![image4](images/Processing_modeler_029.png)
## アプリケーションとプロジェクトのオプション
### 機能: デフォルトの起動プロジェクト指定とプロジェクトテンプレート
With QGIS 2.0 you can specify what QGIS should do when it starts: `New Project` (legacy behaviour, starts with a blank project), `Most recent` (when you start QGIS it will load the last project you worked on), `Specific` (always load a specific project when QGIS starts). You can use the project template directory to specify where your template projects should be stored. Any project that you store in that directory will be available for use as a template when invoking the `Project --> New from template` menu.

![image5](images/Screen_Shot_2013-09-12_at_11.23.02_PM.png)
### 機能：システム環境変数
Current system environment variables can now be viewed and many configured within the application Options dialog. Useful for platforms, such as Mac, where a GUI application does not necessarily inherit the user\'s shell environment. Also useful for setting/viewing environment variables for the external tool sets controlled by the processing toolbox, e.g. SAGA, GRASS; and, for turning on debugging output for specific sections of the source code.

![image6](images/changelog-2.0_sys-env-options.png)
### 機能：ユーザー定義のズーム縮尺
A listing of zoom scales can now be configured for the application and optionally overridden per project. The list will show up in the `Scale` popup combo box in the main window status bar, allowing for quick access to known scales for efficiently viewing and working with the current data sources. Defined scales can be exported to an XML file that can be imported into other projects or another QGIS application.

![image7](images/changelog-2.0_predefined-scales.png)
## ブラウザ
### 機能:アプリ内ブラウザパネルの改善
- ワイルドカードまたは正規表現でディレクトリをフィルタできます
- New `Project home` (parent directory of current project)
- View `Properties` of the selected directory in a dialog
- Choose which directories to `Fast scan`
- Choose to `Add a directory` directly to `Favourites` via filesystem browse dialog
- New `/Volumes` on Mac (hidden directory for access to external drives)
- New `OWS` group (collation of available map server connections)
- Open a second browser (`View -> Panels -> Browser (2)`) for drag-n-drop interactions between browser panels
- アイコンがアイテムグループタイプ（ファイルシステム、データベース、マップサーバ）でソートされました
- Layer `Properties` now have better visual layout

![image8](images/changelog-2.0_browser.png)
## データプロバイダ
### 機能：ラスターデータプロバイダーオーバーホール
The raster data provider system has been completely overhauled. One of the best new features stemming from this work is the ability to \'Layer -\> Save As\...\' to save any raster layer as a new layer. In the process you can clip, resample, and reproject the layer to a new Coordinate Reference System. You can also save a raster layer as a rendered image so if you for example have single band raster that you have applied a colour palette to, you can save the rendered layer out to a georeferenced RGB layer.

![image9](images/Selection_017.png)
### 機能：Oracle Spatialのサポート
QGIS 2.0にはOracle Spatialのサポートが追加されました。

![image10](images/oracle.png)
### 機能：ウェブカバレッジサービスプロバイダが追加されました
QGISはWeb Coverage Serviceレイヤーのネイティブサポートを提供します.WCSを追加するプロセスは、WMSレイヤーまたはWFSレイヤーを追加するプロセスに似ています。
### 機能：デフォルトでラスター2％累積カット
多くのラスター画像製品は、外見が洗い流された画像をもたらす多数の異常値を有する。QGIS 2.0では、画像の色空間を決定する際にデフォルトで2％〜98％の累積カットを使用するなど、ラスターのレンダリング動作に対して、より詳細な制御が可能です。ここの画像は、デフォルト設定で同じ画像をレンダリングするときのQGIS 1.8（左）対QGIS 2.0（右）を示しています。

![image11](images/Selection_023.png)
### 機能：フォーマットを識別するWMS
複数の既知のフォーマットがサーバーによってサポートされている場合、WMSレイヤーの識別ツールの結果のフォーマットを選択できるようになりました。サポートされるフォーマットは、HTML、地物（GML）、およびプレーンテキストです。地物（GML）フォーマットが選択されている場合、結果はベクターレイヤーと同じ形式になり、ジオメトリが強調表示され、属性とジオメトリを含む地物がクリップボードにコピーされ、別のレイヤーに貼り付けられます。

![image12](images/wms-identify.png)
### 機能: WMTS のサポート
QGISのWMSクライアントは、タイムスライスなどのサブデータセットの選択を含むWMTS（Web Mapping Tile Service）をサポートするようになりました。準拠しているサーバーからWMSレイヤーを追加する場合は、表示するタイムスライスを選択するよう求められます。

![image13](images/Selection_035.png)
## 一般情報
### 機能：Quantum GISは今や \'QGIS\' という名前のみ利用しています
「Quantum GIS」の「Quantum」は決して特別な意味を持ちませんでした。私たちのプロジェクトを「Quantum GIS」と「QGIS」の両方として引用することの二重性は混乱を招いていました。私たちはプロジェクトを合理化しており、そのプロセスの一環として正式に「クォンタム」という言葉の使用をやめています。以来、「QGIS」（大文字のすべての文字で綴られています）としてのみ知られています。これを反映するため、コードと広報資料をすべて更新します。

![image14](images/qgis.png)
## ラベリング
### 機能：新しいラベリングシステム
ラベリングシステムは完全に改良されました。これには、ドロップシャドウ、ハイウェイシールド、より多くのデータバインドオプション、さまざまなパフォーマンス強化など、多くの新機能が追加されました。私たちはゆっくりと「古いラベル」システムから離れており、このリリースでは機能的にまだ利用可能ですが、今後のリリースで消えると思ってください。

![image15](images/Layer_labeling_settings_003_1.png)
### 機能：式ベースのラベルプロパティ
ラベルのプロパティには、通常のラベルとルール式のフルパワーを使用できるようになりました。ほぼすべてのプロパティを式またはフィールド値で定義して、ラベル結果をより詳細に制御できます。式はフィールドを参照することができます（例えば、フォントサイズをフィールド \'font\' の値に設定することもできます）。より複雑なロジックを含めることもできます。

バインド可能なプロパティの例を次に示します。
- フォント
- 大きさ
- スタイル
- バッファサイズ

![image16](images/2013-09-05_09_44_59-qgis-dev-bin.png)
### 機能: 古いラベルエンジンは廃止されました
QGIS \<= 1.8で利用可能な古いラベル付けエンジンの使用は現在推奨されていません（つまり廃止予定です）。これは、ユーザーが既存のプロジェクトを古いラベル付けエンジンから新しいラベル付けエンジンに移行できるようにするためです。

以下のガイドラインはQGIS2.0で利用されている古いエンジン用です:
- 廃止予定のラベル付けタブは、新規プロジェクトまたはそのラベル付けエンジンを使用していない古い開いたプロジェクトの「ベクターレイヤープロパティー」ダイアログから削除されています。
- 古い開いたプロジェクトがひとつでもそれを使っていた場合、廃止予定のタブは有効なまま残り、そのプロジェクトが古いラベル付けエンジンを有効にするレイヤを持たない状態で保存しても無くなりません。

非推奨のラベリングタブは、現在のプロジェクトでPythonコンソールコマンドを使用して有効/無効にすることができます。

    >>> QgsProject.instance().writeEntry('DeprecatedLabels', '/Enabled', True | False)
    # or
    >>> QgsProject.instance().removeEntry('DeprecatedLabels', '/')
    
**注意**：QGISの次の安定リリースの前に廃止予定のラベルエンジンが完全に削除される可能性が非常に高い* *があります。古いプロジェクトを移行してください。

![image17](images/changelog-2.0_labels-deprecated.png)
## レイヤ凡例
### 特集：凡例のビジュアルフィードバックとオプション
- レイヤー内の地物とシンボルごとの合計数
- 編集モードのベクターレイヤーには、コミットされていない（保存されていない）編集を示す赤い鉛筆が表示されるようになりました
- アクティブレイヤーには下線が引かれ、マルチレイヤーの選択や選択がない場合に表示されます
- 非リスト項目の空白をクリックすると、選択項目がクリアされるようになりました
- `Right-clicks` はコンテキストメニューを表示する前に `left-clicks` として扱われ、2回ではなく1回のクリックで可能です
- グループとレイヤーは、オプションで太字のフォントスタイルにすることができます
- このようなレンダリングが遅いかもしれないプロジェクトでは、ラスターレイヤーで生成されたプレビューアイコンをオフにできるようになりました

![image18](images/changelog-2.0_visual-options.png)
### 機能：既存の地図レイヤーを複製する
地図レイヤーの凡例で、選択したベクターレイヤーとラスターレイヤーを複製します。同じデータソースを別のレイヤーとして再度インポートするのと同様に、スタイルとシンボル属性をコピー/貼り付けます。

![image19](images/changelog-2.0_dup-layer_1.png)
### 機能：マルチレイヤー編集コマンドの切り替え
凡例で複数のレイヤーを選択できるようになり、編集モードのベクタレイヤーのいずれかがある場合は、現在のコミットされていない編集を保存、ロールバック、またはキャンセルすることを選択できます。ユーザーは、選択に関係なく、すべてのレイヤーでこれらのアクションを適用することもできます。

![image20](images/changelog-2.0_current-edits.png)
## マップコンポーザー
### 機能: HTML マップアイテム
html要素をマップに配置できるようになりました。

![image21](images/Composer_1_006.png)
### 機能：複数ページのサポート
単一のコンポーザウィンドウは現在は複数のページを持つことができます.

![image22](images/2013-09-08_22_31_33-Composer_1.png)
### 機能:コンポーザラベルで式を利用できるようになりました
1.8のコンポーザラベル項目はかなり限定されており、 \$CURRENT_DATE という単一のトークンしか使用できませんでした。2.0では完全な式のサポートが追加され、最終ラベルのパワーとコントロールが大きくなりました。

次のような式を持つラベル。

    This was printed on: [% format_date( $now, 'dd.MM.yyyy')%]
    
印刷時間(と表示時間）は調べられて以下の表示があります:

    This was printed on: 06.09.2013
    
地図帳の生成が有効になっている場合、現在アクティブな地物の属性値には次のような式を使用できるようになります：

    Asset ID [% "ID" %] and the Tree Type is [% "TreeType" %]
    
![image23](images/2013-09-06_09_53_30-Composer_1.png)
### 機能：自動スナップ線
すばらしい印刷地図を作成するには、マップ項目をきちんと整列させることが重要です。自動スナップ線が追加され、オブジェクトを別のオブジェクトの近くにドラッグするだけで、コンポーザーオブジェクトを簡単に整列させることができるようになりました。

![image24](images/2013-09-05_10_05_01-Composer_1.png)
### 機能：手動スナップ線
時には、オブジェクトを特定の距離で整列させる必要があります。新しい手動スナップ線を使用すると、共通のアライメントを使用してオブジェクトを整列させることができる、手動スナップ線を追加することができます。トップまたはサイドルーラーからドラッグして新しいガイドラインを追加するだけです。

![image25](images/2013-09-05_10_09_41-Composer_1.png)
### 機能：地図シリーズ生成
これまで地図シリーズを生成する必要がありましたか？もちろんあります。コンポーザには、地図帳機能を使用した地図シリーズ生成機能が組み込まれています。カバレッジレイヤーはポイント、ライン、ポリゴンにすることができ、現在の地物属性データは、その場で値置換のためのラベルで使用できます。

![image26](images/Picture1.png)
### 機能：地図フレームでの自動概要サポート
メインの地図フレームの現在のエリアをより小さなオーバービューウィンドウに表示する必要があります。さあ、できます。マップフレームには、他の範囲を表示する機能が含まれており、移動すると更新されます。これをアトラス世代の特徴と共に使用することで、コンポーザの中核はいくらか滑らかなマップ生成を可能にします。概要フレームスタイルは、通常のマップポリゴンオブジェクトと同じスタイリングを使用しており、創造性は決して制限されません。

![image27](images/Picture1_1.png)
### 機能:レイヤの混合
レイヤブレンドを使用すると、レイヤを新しくてエキサイティングな方法で組み合わせることができます。古いバージョンでは、レイヤーを透明にするだけでしたが、「乗算する」、「暗くなるだけ」などのより高度なオプションを選択できるようになりました。

ブレンドは、通常のマップビューやプリントコンポーザーで使用できます。プリントコンポーザーでブレンドを使って背景画像を最大限に活用する方法についての短いチュートリアルについては、[QGISを使ったビンテージマップデザイン](http://anitagraser.com/2013/07/29/vintage-map-design-using-qgis/) を参照してください。

![image28](images/printcomposer_blending_1.png)
### 機能:HTMLラベルサポート
HTMLサポートには、マップ・コンポーザーのラベル項目が追加され、最終的なマップをさらに詳細に制御できます。HTMLラベルはCSSスタイルシート、html、さらにはjavascriptをサポートしています。

![image29](images/html.png)
### 機能:コンポーザの凡例でマルチカラムのサポート
コンポーザーの凡例は複数の列をサポートするようになりました。多くのクラスを持つ単一のレイヤーを複数の列に分割することはオプションです。単一シンボルレイヤーは、デフォルトでは単一のラインアイテムとして追加されるようになりました。レイヤー/グループタイトルにグループ、サブグループ、または非表示の3種類のスタイルを割り当てることができます。タイトルスタイルはアイテムの任意の視覚的なグループ分けを可能にする。例えば、1つのシンボルレイヤーを1つのラインアイテムまたはレイヤータイトル（1.8のように）で表示し、複数のレイヤーからのシンボルを1つのグループ（タイトルを隠す）にグループ化することができます。

![image30](images/multicolumn-legend.png)
### 機能：マップ・コンポーザー管理の更新
マップコンポーザの管理に次のような改善が作成されました:
- コンポーザの名前は作成時に指定できます,オプションで他のコンポーザ名からの選択もできます
- コンポーザを多重化できます
- `テンプレートから新規作成` と `指定` (コンポーザマネージャー内) を使うとファイルシステムのどこかにあるテンプレートを使ってコンポーザを作成することができます
- 親プロジェクトをコンポーザの作業スペースから直接保存できるようになりました
- すべてのコンポーザの管理作業は、コンポーザの作業スペースから直接アクセスできるようになりました

![image31](images/changelog-2.0_composer-mngmnt.png)
## プラグイン
### 機能：プラグインマネージャの再構築
QGIS 1.xではプラグインの管理に2つのインターフェイスがあって混乱していました。ひとつはすでにインストールされているプラ​​グインを管理するためのものであり、もうひとつはプラグインリポジトリからPythonプラグインを取得するためのものです。QGIS 2.0では、**新しい統合されたプラグインマネージャー** を導入し、プラグインをダウンロード、有効/無効、一般的な管理をする *ワンストップショップ* を提供しました。ええ、ユーザーインターフェイスもサイドタブと分かりやすいアイコンで豪華になりました！

![image32](images/Plugin_Manager_024.png)
## プログラマビリティ
### 機能:新しいPythonコンソール
新しいPythonコンソールはさらに強力な機能を提供します。今では、自動完全サポート、構文の強調表示、調整可能なフォント設定を備えています。サイドコードエディタを使用すると、QGISセッションでPythonファイルを開いて実行できるように、より大きなコードブロックを簡単に入力できます。

![image33](images/pyconsole.png)
### 機能：より多くの式関数
表現エンジンは、式ベースのラベルやシンボルのようなものを可能にするためにQGISをますます使用していますが、より多くの関数が式ビルダーに追加されており、式ビルダーを通してすべてアクセス可能です。すべての機能には、使いやすさのための包括的なヘルプと使用ガイドが含まれています。

![image34](images/2013-09-06_09_10_49-Expression_based_label.png)
### 機能:特別な式の関数
式エンジンに必要な機能がない場合。心配無用。新しい関数は、単純なPython APIを使用してプラグインを介して追加することができます。

![image35](images/2013-09-06_09_14_58-untitled__routing_-_Sublime_Text_UNREGISTERED.png)
### 機能:新しくより洗練された Python API
Python APIは、より洗練され、よりパイソニックなプログラミング体験を可能にするように改良されました。QGIS 2.0 API は SIP V2 を使用しています。この V2 は、値を扱う際に必要とされる乱雑な toString（）、toInt（）ロジックを削除します。型は、はるかに良い API を作るネイティブの Python 型に変換されました。属性へのアクセスは、単純なキールックアップを使って地物自身に対して行われ、索引ルックアップと属性マップはもう使用されません。

    >>> feature['mycolumn'] = 10
    >>> feature['mycolumn']
    10
    
地物をレイヤーから読み取る方法も改良されており、将来のバージョンではマルチスレッドが可能です。

    for feature in layer.getFeatures():
           print feature['mycolumn']
    
![image36](images/2013-09-06_09_28_08-untitled__routing_-_Sublime_Text_UNREGISTERED.png)
### 機能:バージョン1.xリリースとのコード互換性
これはメジャーリリースであるため、以前の1.xリリースと完全に互換性のあるAPIではありません。 ほとんどの場合、あなたのコードを移植するのはかなり簡単です。使い始めるには [このガイド](https://github.com/qgis/QGIS/wiki/Python_plugin_API_changes_from_18_to_20) を使うことができます。 さらに詳しいヘルプが必要な場合は、開発者メーリングリストを使用してください。

![image37](images/Selection_021.png)
### 機能:Pythonプロジェクトマクロ
project.qgsファイルに保存されたPythonモジュールをロードして、次のプロジェクトイベントで特定の関数を実行できます。
- `openProject()`
- `saveProject()`
- `closeProject()`

マクロを実行するかどうかは、アプリケーションオプションで設定できます。

![image38](images/changelog-2.0_project-macros_w-setttings.png)
## シンボロジ
### 機能：データで定義されたプロパティ
新しいデータ定義プロパティでは、シンボルのタイプ、サイズ、色、回転、およびその他の多くのプロパティを地物属性を使用して制御できます。

![image39](images/datadefinedproperties2.png)
### 機能：シンボルレイヤー管理の改善
新しいシンボルレイヤの概要では、すべてのシンボルレイヤに簡単かつ迅速にアクセスできる明確なツリー構造のレイアウトが使用されています。

![image40](images/symbollayertree.png)
### 機能：カラー定義の透過率のサポート
色を選択するほとんどの場所で、QGISではアルファチャンネルを指定できるようになりました（その色がどのくらい透明であるかが決まります）。これにより、見栄えの良い地図を作成したり、ユーザーに見せたくないデータを簡単に隠すことができます。

![image41](images/Layer_Properties_-_nat_026_1.png)
### 機能：ラスターレイヤーのカラーコントロール
QGIS 2.0では、ラスターレイヤの表示方法を正確に精密に制御することができます。ラスターレイヤーの輝度、コントラスト、彩度を完全に制御できるようになりました。ラスターをグレースケールで表示したり、指定した色で色付けすることもできます。

![image42](images/Layer_Properties_-_blue_marble_032.png)
### 機能：レイヤー間でシンボロジをコピーする
1つのレイヤーから別のレイヤーにシンボロジをコピーするのがとても簡単になりました。いくつかの類似したレイヤーで作業している場合は、あるレイヤーで単純に `右クリック` してコンテキストメニューから `コピースタイル` を選び、次に別のレイヤーで `右クリック` して `ペーストスタイル` を選んでください。

![image43](images/Selection_034.png)
### 機能：データベースにスタイルを保存する
データベースベクタデータストアを使用している場合は、レイヤスタイル定義を直接データベースに格納できます。これにより、エンタープライズまたはマルチユーザー環境でスタイル付きレイヤーを簡単に共有できます。

![image44](images/Selection_037.png)
### 機能：カラーランプのサポート
QGISのシンボロジ設定の多くの場所でカラーランプが使用可能になり、豊富で拡張可能なカラーランプセットが搭載されたQGISが出荷されます。また、自分でデザインすることもできますし、「箱から出したままの」QGIS には既に多くの [cpt-city](http://soliton.vm.bytemark.co.uk/pub/cpt-city/) テーマが含まれています。カラーランプは透過率を完全にサポートしています。

![image45](images/Selection_038.png)
### 機能：すべてのレイヤータイプのカスタムデフォルトスタイルを設定する
QGISは、新しいレイヤーが既存の定義された `.qml` スタイルを持たないときの描画方法を制御できるようになりました。新しいレイヤーのデフォルトの透明度レベルと、シンボルにランダムな色を割り当てる必要があるかどうかを設定することもできます。

![image46](images/Screen_Shot_2013-09-12_at_11.18.52_PM.png)
## ユーザーインタフェース
### 機能：新しいアイコンテーマ
私たちはQGISのユーザーインターフェイスに一貫性とプロフェッショナリズムのレベルを向上させる「GIS」テーマを使用するためのアイコンテーマを更新しました。

![image47](images/Selection_001_1.png)
### 機能：サイドタブ、折りたたみ可能なグループ
私たちは、タブのレイアウトを標準化し、折り畳み可能なグループボックスを多くのダイアログに導入し、さまざまなオプションをより簡単にナビゲートし、画面の不動産をより有効に活用しました。

![image48](images/Selection_005.png)
### 機能：ソフト通知
多くの場合、あなたに何かを伝えたくても、あなたの仕事を止めたり、足手まといになりたくありません。新しい通知システムでQGISはマップキャンバスの上部に表示される黄色のメッセージバーを介して重要な情報を知らせることができますが、何か他のことで忙しいときに、それに対処することを強いません。プログラマも Python API を使用して（プラグインなどから）これらの通知を作成できます。

![image49](images/Selection_030.png)
### 機能：アプリケーションのカスタムフォントとQtスタイルシート
アプリケーションのユーザーインターフェイスに使用されるシステムフォントを設定できるようになりました。QGIS GUIアプリケーションの子であるか、アプリケーションのGUIスタイルシートをコピー/適用した C++ または Python プラグインは、そのスタイルを継承することができます。これは、プラットフォームをまたいだ GUI 修正や、 `QgsCollapsibleGroupBox` などのカスタム QGIS Qt ウィジェットを使用する場合に便利です。

現在のプラットフォーム用に生成されたQGIS GUIアプリケーションスタイルシートは、（PyQGISで）起動した後にアクセスできます。

    qgis.utils.iface.mainWindow().styleSheet()
    
![image50](images/changelog-2.0_app-font.png)
### 機能:ライブカラー選択ダイアログとボタン
インターフェイス全体で色選択ボタンが更新され、現在の色が透明か、「アルファ」コンポーネントを持っているかを視覚的にフィードバックするようになりました。新しい色ボタンで開かれた色選択は、常にオペレーティングシステムのデフォルトになりました。ユーザが `オプション -> 一般情報 -> アプリケーション` の下で `Live-updating 色選択ダイアログを使用する` をチェックしている場合、色選択での変更は、すぐにカラーボタンに表示され現在編集中の項目がある場合は適用されます。

![image51](images/changelog-2.0_live-color-dlgs.png)
### 機能:SVG注記
QGIS 2.0を使用すると、マップキャンバス上の特定の場所または相対位置に固定されたSVGアノテーションをマップに追加できるようになりました。

![image52](images/Screen_Shot_2013-09-14_at_9.39.11_AM.png)
### 機能：ドラッグアンドドロップフォームビルダ
QGIS 2.0は、データ入力フォームを作成するためのすばらしい新しいシステムをサポートしています。ドラッグ＆ドロップフォームデザイナーを使用すると、スマートな外観のフォームをタブで作成して、共通フィールドをまとめてグループ化することができます。これで、ユーザーのデータ入力の操作を簡単に制御できます。

![image53](images/Screen_Shot_2013-09-14_at_2.17.27_PM.png)
### 機能：デフォルトのアクションツール
ベクターレイヤーアクションのユーザー（地物をクリックしたときに実行できる小さなタスク）は、ツールバーの新しいアクションツールが好きになります。それを使用するとアクティブなアクションを選択でき、次にそのアクションを呼び出すために地物をクリックします。

![image54](images/Screen_Shot_2013-09-14_at_2.27.03_PM.png)

{{<content-end >}}
