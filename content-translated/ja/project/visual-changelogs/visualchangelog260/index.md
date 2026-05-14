---
HasBanner: false
draft: false
releaseDate: '2014-10-31'
section: project
sidebar: true
title: QGIS 2.6の変更履歴
type: visual-changelog

---
{{<content-start >}}
# QGIS 2.6の変更履歴{#changelog26 }
リリース日: 2014-10-31

QGIS 2.6.0の次のリリースのログを変更します。私たちは、最も人気のあるフリーデスクトップGISをよりいっそう多くの機能が充実して役立つようにするために、多くの新機能、調整、拡張機能を追加しました。

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

私たちは、開発者、ドキュメント作成者、テスター、そして時間と労力をボランティアしている（あるいは人々に資金を提供する）多くの人々に感謝したいと思います。

From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

最後に、このプロジェクトに提供した貴重な財政支援について、公式スポンサーに感謝したい。
- **GOLD Sponsor: Asia Air Survey, Japan** <http://www.asiaairsurvey.com/>
- SILVER Sponsor: [Sourcepole AG, Switzerland](http://www.sourcepole.com/)
- SILVER Sponsor: [State of Vorarlberg, Austria](http://www.vorarlberg.at/)
- BRONZE Sponsor: [Lutra Consulting, UK](http://www.lutraconsulting.co.uk/)
- BRONZE Sponsor: [www.molitec.it, Italy](http://www.molitec.it/)
- BRONZE Sponsor: [www.argusoft.de, Germany](http://www.argusoft.de)
- BRONZE Sponsor: [www.openrunner.com, France](http://www.openrunner.com)
- BRONZE Sponsor: [GKG Kassel,(Dr.-Ing. Claas Leiner), Germany](http://www.eschenlaub.de/)

A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become an official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts.

If you enjoy using QGIS, please consider making a donation to support the project - either [financial](https://qgis.org/en/site/getinvolved/donations.html) or of [your time and skills](https://qgis.org/en/site/getinvolved/index.html)! Lastly we would like to also take a moment to encourage you to fund a [special campaign](http://blog.vitu.ch/10102014-1046/crowdfunding-initiative-automated-testing) by one of our QGIS developers to get a working test suite for QGIS so that we can improve out quality assurance process and deliver you the best possible releases.

QGIS はフリーのソフトウェアです。利用する上で金銭を支払う義務はありません。実際、私たちは利用者の財政状況や社会的地位にかかわらず、より多くの人に QGIS を利用して欲しいと思っています。私たちは地理空間的な意思決定ツールによって人々が力を持つことが、全人類の社会をより良くすると信じています。

{{<table-of-contents >}}
## 一般情報
### 機能: プロパティにおけるプロジェクトファイル名
プロジェクトプロパティダイアログで、QGISプロジェクトファイルの絶対パスを確認できるようになりました。

![](images/entries/8662dc4a69298f603dd9038d1199ab16fd25f786.webp)
### 機能：デル/バックスペースキーで測定中に最後のポイントを削除できるようにする
面積と距離を測定するときに、削除またはバックスペースキーを使用して不要な頂点を測定線から削除することができます。

![](images/entries/ed471908937cb068e2f004e7b3311f2bdf307042.webp)
### 機能：リレーション参照ウィジェットからキャンバス上の関連する地物を選択する
### 機能:エディターウィジェット
エディタウィジェットをいくつか改良しました。
- ヌル日付を設定できる日付/時刻用の新しい編集ウィジェット
- filter line edit
- Proper handling of NULL values for edit widgets
- 写真ウィジェットによるNULL値の保持
- ウェッブウィジェットによるNULL値の保持
- 属性テーブルでは0とNULLを識別することができます
- 範囲ウィジェットのサフィックスサポートを追加する

![](images/entries/78fd27b2cf736f37bdf97694a5018f29c609c6cb.webp)
### 機能：オプションで、結合されたレイヤーのフィールドのサブセットのみを使用する
ベクター結合の作成時に、関連フィールドのサブセットのみを使用できるようになりました。

![](images/entries/14023cf2ee768960d9c4a43da6e2a1624d10b3c3.webp)
### 機能:式フィールド(仮想フィールド)
Sometimes you want to have an attribute that is calculated and that is always \'fresh\' - reflecting the current state of the feature properties. Now you can add virtual fields to your table which are based on an expression.

![](images/entries/5fe53ad54b8d0cf8b7a22b90e733a421bb929506.webp)
### 機能:アクションは関連アイコンを持つことができるようになりました
ベクターレイヤーのカスタムアクションを作成するときに、アクションに使用するアイコンを定義できるようになりました。

![](images/entries/e7bd5b306e3a72cc111a81f86a053b42679aa2f8.webp)
### 機能：追加の式の種類とオプション
- Allow using `+` for string concatenation.
- New keyword: `attribute( feature, attribute_name )` - gets the specified attribute from a feature.
- New keyword: `$currentfeature` - returns the current feature.
- New keyword: `$atlasfeature` - returns the atlas feature.
- New keyword: `getFeature` - gets a matching feature from a layer.

![](images/entries/e2e079bec87be65ccc97055251fc2544be91aaab.webp)
### 機能：段階的レンダラーと分類されたレンダラー内のクラスを切り替えることができます
これで、段階的レンダラーと分類済みレンダラーの特定のクラスを実際に削除せずに無効にすることができます。

![](images/entries/84d11c6d978775d92f6a1902092795735d1f32b3.webp)
### 特集：凡例の改善
凡例/目次見直しの第2段階が完了しました。これも：
- API cleanup (開発者用)
- レイヤーツリー内のマップレイヤの可視性グループ。この新しいツールバーボタンを使用すると、表示するレイヤーのグループをすばやく変更できます。
- 凡例ツールバーからレイヤーグループを管理する機能
- 凡例ツールバーの新しい凡例フィルタオプションは、現在表示範囲にないクラスの凡例項目を削除します。これは、マップの凡例に現在マップビューにないアイテムのエントリが含まれていないことを保証するので、すばらしい改善点です。メインマップの凡例、マップコンポーザー、およびWMSレイヤーで使用できます。
- ルールベースのレンダラの凡例を疑似ツリーで表示できるようになりました

![](images/entries/363048a7d08ac76d35463abbef514c65031922e7.webp)
## データプロバイダ
### 機能：DXFエクスポートの改善
- ダイアログのレイヤアサイメントのツリービューと属性選択
- ポリゴンの塗りつぶしで/HATCH をサポートしました
- TEXTの代わりにMTEXTとしてのテキストを表現する（フォント、斜体、および太さを含む）
- support for RGB colors when there\'s no exact color match
- R12の代わりにAutoCAD 2000 DXF（R15）を使用する
- R18テストメソッドを削除する

![](images/entries/4f615505e3fd6ec0b619278e42ecc5a3e79ac827.webp)
## マップコンポーザー
### 機能：印刷物/輸出物から印刷コンポーザアイテムを隠すことを制御する
アイテムがコンポーザのエクスポート/プリントアウトから除外されているかどうかを制御するチェックボックスとデータ定義ボタンが追加されました。項目がチェックされていない場合は、コンポジションデザイン時にのみ表示されます。

![](images/entries/f334447d13ee49a6c4c5cb4322e3f12824643416.webp)
### 機能：空のコンポーザーフレームのページ印刷を制御する
テーブルまたはHTMLフレームの場合、チェックボックスは、フレームが空のときに、そのページをエクスポートするかどうかを制御するようになりました。

![](images/entries/1500ba6abdf5b314c760ebfc63e460731dcc5110.webp)
### 機能：アイテムツリーパネル
マップコンポーザーのアイテムツリーパネルでは、アイテムの選択、アイテムの非表示/表示、アイテムのロック状態の切り替え、アイテムIDのダブルクリックによる編集ができます。ドラッグアンドドロップを使用して項目を並べ替えることもできます。

![](images/entries/52b70bdf87d21a13c00798458bab6347dddd7910.webp)
### 機能：コンポーザーの矢印/広告申込情報の外観を詳細に管理
- ラインシンボルスタイルダイアログを使用して線をスタイルすることができます
- アローヘッドの塗りつぶしとアウトラインの色をユーザー定義することができます
- 矢印の頭の輪郭の幅はユーザ定義可能

![](images/entries/49757b3cc09839edb8af38f1cb1317458f279110.webp)
### 機能:コンポーザアイテムのデータによる制御
データバインディングを使用して、作曲者アイテムの多くのプロパティを制御できるようになりました。これらには、
- 透明度とブレンドモード。
- アイテムの回転
- 地図スケール, 領域と傾き.
- 地図帳地物マージン.
- アイテムのサイズと位置.
- ページサイズ,向きとページ番号

![](images/entries/9f321489cd9c90eb4d66e577680fc5467756e58e.webp)
### 機能：作曲者の画像をリモートURLとして指定することができます
マップコンポーザー内のピクチャアイテムは、ピクチャソースとしてリモートURLをサポートするようになりました。このソースは、データとして定義することもできます。

![](images/entries/05cd7008c231df3b3af874753b840669a605cb0f.webp)
### 機能:コンポーザテーブルの改善
- テーブルヘッダーとコンテンツフォントの色を設定できるようになりました。
- テーブルを複数のフレームに分割できるようになりました。これにより、コンテンツを列または異なるページに分散させることができます。
- 最初のフレーム、すべてのフレーム、またはフレームなしのオプションの表示ヘッダーを追加しました。
- 列の幅を手動で制御できます。
- リレーションからの現在のアトラス機能と子機能を含むテーブルソースの新しいオプション。
- 空のテーブルの動作を選択するには、テーブル全体を隠す、空のセルを表示する、またはテーブル本体にセットメッセージを表示するなどがあります。
- 現在の地図帳地物と交差するものにテーブル機能をフィルタするためのチェックボックスを追加しました。
- テーブルから重複行を削除するためのチェックボックスが追加されました。

既存のプロジェクトのテーブルは、これらの機能をサポートする新しいテーブル形式に自動的には更新されず、新しい設定を表示するには、テーブルをコンポジションに読み込む必要があります。

![](images/entries/9ccb75b2110daf0c95a3fba31ac18144c1345f0e.webp)
### 機能:コンポーザの改善
マップ・コンポーザー（印刷可能なマップ・コンポジションの作成に使用）は、QGIS 2.6でいくつかの改良を受けました。
- スケールバーの二次塗りの色を変更できるようになりました
- ライン/矢印の描画中にシフトを保持すると、描画は水平、垂直、または45度の角度に制限されます
- 他の新しいアイテムを描画中にシフトを保持すると、それらを四角に制限し、altの原因アイテムを中心から引き出します
- 右クリックはもはやアイテムをロック/ロック解除しません。これは新しいアイテムパネルによって処理されます。ロックされたアイテムはコンポーザのキャンバスから選択できなくなり、その下のアイテムとのやりとりが可能になります。
- カーソルキーを押しながらaltキーを押すとアイテムの動きが1ピクセルになります
- Removed the destructive \'Load from template\' menu item, replace with a new non-destructive \'Add items from template\' action

![](images/entries/a7267ed637121bc9be70c5fa0afd2a63f9790bc7.webp)
### 機能:アイテムスナッピングの改善
スナップしきい値がピクセル単位で設定されるようになりました。これにより、コンポジションにズームインしたときにアイテムを細かく移動したりサイズを変更することができます。グループ内の項目は、自動スナップ線では使用されなくなりました。

![](images/entries/8e43479380c28942345f3d9500dd956bd13f43e8.webp)
### 機能：地図アイテムの複数の概要
Sometimes it is useful to be able to show more than one overview frame for a map frame. For example if you want to show where your map is in local, regional and global context, using multiple overview maps can help you to achieve this. As of QGIS 2.6 you can now achieve this by assigning as many maps as you like to the \'overview\' role in your composition.

![](images/entries/88b55cc5f5e7cfb62486fe3b4867b7133ae66953.webp)
### 機能：HTML項目の改善
HTMLコンポーザー項目には、いくつかの便利な新しいオプションがあります。
- HTMLソースの手動入力オプション
- HTMLソース内のQGIS式は、HTMLコンテンツをレンダリングする前に評価することができます
- HTMLソースのURL指定データ
- ユーザ作成スタイルシートでHTMLスタイルを上書きすることの許可

![](images/entries/7ed388f0c775b738648b2bd6eb6be0a75fa5816a.webp)
### 機能：コンポーザ地図グリッドの改善
- You can now have multiple grids with different properties.
- 再投影されたグリッドと緯度/経度グリッドを混在させることができます。
- 標準のQGISシンボルグリッド線などを使用できます。
- 新しいフレーム/注釈のみのグリッドスタイルがあります。このスタイルを選択すると、マップ上にグリッド線やその他のマーキングがなく、フレームと注釈だけが描画されます。
- フレームが描画されるマップアイテムのどちら側を制御するかのオプションがあります。
- インナーティック、アウターティック、インナーとアウターティックの両方のオプションを持つ、フレーム用の新しいティックスタイルがあります。
- 注釈の新しい形式をはじめ、グリッド注釈の改良が行われました。
- グリッド注釈では、グリッド注釈のためにタイポグラフィックに正しいプライム記号とダブルプライム記号が使用されるようになりました。

![](images/entries/eeb61d7da3d3f95283b1bb47545cbdff9cc334ae.webp)
## プロセシング
### 機能：モデルとスクリプトのオンライン収集
モデルとスクリプトは、オンラインコレクションからダウンロードし、Processingインタフェースから直接インストールすることができます。コレクションは、Processingユーザーが提供する新しいスクリプトとモデルで拡張されます。

![](images/entries/23e357ca0e559a33a7872206b306c0b1fbdb4b7d.webp)
### 機能:新しいモデラーの改良
モデラーは書き直され、深さ制限のないネストされたモデルを許可するなどの特別な機能が追加されました。モデルはJSONファイルとして保存されるようになりました。下位互換性は維持されるため、すべてのモデルを引き続き使用できます。また、入力とアルゴリズムからモデラーグラフに項目をドラッグ＆ドロップすることもできます。

![](images/entries/72bb8beaf97133424d1e68da67ae6fe79ea6faf6.webp)
## プログラム可能
### 機能: QGIS ウィジェットAPIの変更
In order to normalise the naming of QGIS widgets, some minor API changes have been made. Almost all edit widgets were renamed by adding \"Wrapper\" at the end of their names. In particular this concerns:
- QgsCheckboxWidget -\> QgsCheckboxWidgetWrapper
- QgsClassificationWidget -\> QgsClassificationWidgetWrapper
- QgsColorWidget -\> QgsColorWidgetWrapper
- QgsEnumerationWidget -\> QgsEnumerationWidgetWrapper
- QgsFilenameWidget -\> QgsFilenameWidgetWrapper
- QgsHiddenWidget -\> QgsHiddenWidgetWrapper
- QgsPhotoWidget -\> QgsPhotoWidgetWrapper
- QgsRangeWidget -\> QgsRangeWidgetWrapper
- QgsTexteditWidget -\> QgsTexteditWrapper
- QgsUniquevalueWidget -\> QgsUniquevalueWidgetWrapper
- QgsUuidWidget -\> QgsUuidWidgetWrapper
- QgsValuemapWidget -\> QgsValuemapWidgetWrapper
- QgsValuerelationWidget -\> QgsValuerelationWidgetWrapper
- QgsWebviewWidget -\> QgsWebviewWidgetWrapper

## QGISサーバー
### 機能：GetFeatureInfoリクエストによる検索機能の強化
<https://github.com/qgis/QGIS/commit/8888c5f0c0e0ffdf23453a20addf6abaf125845d>
### 機能:GetfeatureInfoのジオメトリ属性で精度を設定する機能を追加しました
## シンボロジ
### 機能：より良いランダムカラー選択
私たちは、分類されたレンダラーのランダムカラーアルゴリズムを改良して、生成される色が互いに視覚的に明確になるようにしました。

![](images/entries/ec29c9d6eb23d01b4dbbae32a6e20fe0b1f48198.webp)
### Feature：Symbologyユーザインタフェースの改善
- 可能であれば、シンボルレイヤーのタイプを変更するときにシンボルレイヤーのプロパティが維持されます。
- シェイプバーストとグラデーションカラーランプの編集ボタンが追加されました。
- ラベルと隣接する境界範囲の自動更新.
- ルールベースのレンダラーに切り替えると、クラスは分類されたクラスと段階的なクラスから自動的に変換されます。
- 段階的レンダラーラベルに単位と小数点以下桁数を追加しました。
- GUIのカラーランプ、反転カラーランプ、その他のオプションの変更に対する応答性が向上しました。
- シンプル、卒業、分類、およびその他のレンダラーを切り替えるときは、シンボルを保持します。
- 標準偏差計算モードのラベリングが改善されました.

![](images/entries/08305d5131c28c45b400662267ff0d174ef9c8ce.webp)
## ユーザーインタフェース
### 機能：構文強調コードエディタ
pythonスクリプトエディタ向け,式ビルダ,フィルタウィンドウ,コンポーザのHTMLとCSSエディタ

![](images/entries/54b470a064d65d6d65aa66a8feece43ba8cbf6c4.webp)
### 機能:カラーパレット
QGISで使用する独自のカスタムカラーパレットを定義できるようになりました。
- カスタムユーザのグローバルカラーパレット（オプションダイアログ）
- プロジェクト毎のカラーパレット(プロジェクトプロパティダイアログ内).
- 色は、カラーボタンメニューと新しいカラーピッカーダイアログで表示されます。
- GPLパレットファイルから色のインポート/エキスポートができるようになりました

![](images/entries/a156f408d7a87fc930095c8fd68e9fba0fc0a817.webp)
### 機能:新しいカラーピッカーダイアログ
新しいQGISカラーピッカーダイアログです.次のような機能をもちます:
: - 色相、彩度、値、赤、緑、青の色成分のスライダー。
  - アルファスライダ.
  - htmlのカラーコードをコピー/ペーストするオプション(様々な形式で).
  - カラープレビューの前後に、アルファプレビューが表示されます。
  - インタラクティブ2Dカラーランプウィジェット。
  - 色相ホイール/三角ウィジェット.
  - 編集可能なカラーパレット：新しいパレットを作成したり、GPLパレットファイルにカラーをインポート/エクスポートしたりできます。
  - 設定された半径でサンプリングするオプション付きのライブカラーサンプラー（OSサポート依存）。
  - ドラッグ＆ドロップによる色の他のアプリケーションとのやりとりをサポートします（OSのサポートに依存）。
  - ダイアログを無効にし、代わりにネイティブピッカーダイアログを使用するオプション。

![](images/entries/7189c0fe2d1ff3fdc63c531a02f74b5d32b70bfd.webp)
### 機能：矩形で選択された単一選択地物ツール
単一選択ツールを長方形ツールにマージしました。単一の地物を選択する場合は、地物を四角形ツールを有効にして、地物をシングルクリック（長方形をドラッグするのではなく）します。

![](images/entries/f8a68fcdfcaa59e6162185acb5c92edb9145c881.webp)
### 機能：地図キャンバスの動作にレイヤーを追加する
In many of QGIS\' dialogs that generate a new layer, the \'Add layer to map canvas\' checkbox is now checked by default so that the new layer automatically gets added to the map.

![](images/entries/f36f5912d2422a439d67b1a743fe81588e709dfb.webp)
### 機能：アイコンサイズ48と64を追加
タッチデバイスでQGISを使用している場合（または大きな、ちょっとしたアイコンが好きな場合）、アイコンを最大64 x 64ピクセルのサイズに設定できるようになりました。

![](images/entries/3be3f51da2f54a8395f054f757f9fae1948a6103.webp)
### 機能：新しいカラーボタン
This is probably one of the most useful new features in QGIS 2.6 -especially if you are involved a lot in cartography work. The colour button used everywhere in QGIS has been enhanced, with drop down menus, colour swatches, default colours, etc. Click on the drop down item to the right of the colour button to see the quick options. Click on the button to the left of the colour widget to see a standard colour chooser dialog.

![](images/entries/54c211513bc86d00a5bce01a17476481937e0fbe.webp)
### 機能：識別ツールのコンテキストメニュー
識別ツールを使用する場合は、キャンバスを右クリックして、識別ツールをコンテキストモードで使用することができます。表示されるメニューでは、識別する地物タイプを定義できます（必要に応じてすべての地物タイプを定義できます）。

![](images/entries/c395c2ce4964826458a721a8a3f89cb7dc2853b5.webp)

{{<content-end >}}
