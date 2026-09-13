---
HasBanner: false
draft: false
releaseDate: '2016-07-08'
section: project
sidebar: true
title: QGIS 2.16の変更履歴
type: visual-changelog

---
{{<content-start >}}
# QGIS 2.16の変更履歴{#changelog216 }
![image1](images/projects/b4bbe21d5002a4b73ba27f5abf4e4aaea61d161f.png)

リリース日: 2016-07-08

This is the log for the next release of QGIS - version 2.16.0 \'Nødebo\'. The Department of Geoscience and Natural Resource Management Forest and Landscape College in Nødebo were hosts to the First International QGIS conference and developer meeting in May 2015.

**これは長期サポートのリリースではありません**

このリリースは、長期リリース（LTR）として指定されていません。少なくとも1年間は変更されずにバグ修正を受けるQGISのバージョンを希望するユーザーは、現在のLTRリリース2.14（QGIS 2.16のリリースでは公式のLTRになりました）を使用するように招待されます。

**New Features in QGIS 2.16 \'Nødebo\'**

If you are upgrading from QGIS 2.14 you will find a great many new features in this release. We encourage you to peruse the changelogs for [previous releases](https://www.qgis.org/en/site/forusers/visualchangelogs.html) as this QGIS 2.16 release includes all features published in those releases too.

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

[![Introducing Nødebo](images/pronouncingnodebo.png)](http://www.youtube.com/watch?v=GKg2SHmBExs)

Pronouncing Nødebo\...

**謝辞**

We would like to thank the developers, documenters, testers and all the many folks out there who volunteer their time and effort (or fund people to do so). From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

QGIS is supported by donors and sponsors. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become an official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

QGIS is Free software and you are under no obligation to pay anything to use it -in fact we want to encourage people far and wide to use it regardless of what your financial or social status is - we believe empowering people with spatial decision making tools will result in a better society for all of humanity. If you are able to support QGIS, you can [![donate here](https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif)](https://qgis.org/en/site/getinvolved/donations.html).

{{<table-of-contents >}}
## QGISバージョン2.16.0のスポンサー
私たちは毎年、私たちがやっていることを評価して、プロジェクトに取り込まれる持続的な開発努力を促進しようとしてくれる様々な組織からの支援を受けています。これらのスポンサーを感謝とともに以下に記します。

{{<fund type="changelog" >}}
## 一般情報
### 機能：GeoJSON形式での地物のコピー
The previous setting for include WKT when copying features has been replaced with a choice of copying features as \"Plain text, attributes only\", \"Plain text, WKT geometry\" and a new \"GeoJSON\" option. When set to \"GeoJSON\", copying features in QGIS will place a GeoJSON text representation of the features on the clipboard for easy pasting into other applications/JavaScript code. These settings can be found in the `Settings -> Options -> Data Sources -> Copy features as`.

![image95](images/entries/826068a22b7e7d472720f2404e293fc81de32850.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### 機能：空間ファイルのブックマークをプロジェクトファイルに保存する
空間的なブックマークを作成する場合は、アクティブなプロジェクトファイルにブックマークを保存することができます。ブックマークパネルをスクロールして、この機能を有効にするチェックボックスを見つけます。

![image96](images/entries/fe01b36ab39b8cc21e6ec875c4baadc890cf6519.png.400x300_q85_crop.webp)

This feature was developed by [Stéphane Brunner](http://www.camptocamp.com/)
### 機能：GNSS GNRMCメッセージのサポート
QGIS can now handle GLONASS satellite data (\$GN\* lines) to get a more precise Position from external GPS/GNSS Receivers.

![image97](images/entries/9d13c0c632da1e70199f035ce5a186c018da2cef.png.400x300_q85_crop.webp)

この機能はOndřejFibichによって開発されました
### 機能：GeoJSONの機能をQGISに直接ペーストする
QGISクリップボードハンドラは、GeoJSON地物コレクションのネイティブサポートを含む多くの追加のテキストフォーマットを解析できるようになりました。これにより、GeoJSON文字列を直接コピーしてQGISに貼り付け、QGISの地物とジオメトリに自動的に変換させることができます。

![image98](images/entries/b649df59dc031b26896e9bba2e20c8380081b741.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### 機能：マップのヒントの改善
- Maptipの可視性がセッション間で保存されるようになりました
- Maptipsは画像、動画、URLリンクなどのHTMLコンテンツを表示できるようになりました

![image99](images/entries/96467c2c86ede6392190f021d266ee0e7ed6cbb5.png.400x300_q85_crop.webp)

This feature was funded by [OPENGIS.ch GmbH](http://www.opengis.ch)

This feature was developed by [Marco Bernasocchi (OpenGIS.ch)](http://www.opengis.ch)
### 機能：QGISファイルタイプのデスクトップMIMEアイコン
It\'s now easier to recognise and differentiate QGIS\'s file types on your operating system files manager. There are now desktop MIME Icons for the following file types:
- \*.qgs - QGISプロジェクトファイル
- \*.qml - レイヤー設定ファイル
- \*.qlr - レイヤー定義ファイル
- \*.qpt - コンポーザテンプレート ファイル

![image100](images/entries/9161a4c36a0149b32cd18119954ac32ce42788a6.PNG.400x300_q85_crop.webp)

This feature was developed by [Alexandre Neto](https://gisunchained.wordpress.com/)
## ユーザーインタフェース
### 機能：地図キャンバスの拡大鏡
拡大鏡ツールがQGISに追加されました。これにより、指定された縮尺で地図を拡大することができます。これにより、地図の縮尺を変えずにマップを拡大することができ、ラベルやシンボルの位置を簡単に微調整することができます。さらに、デフォルトの倍率値を設定で定義することができます。これは、高解像度のスクリーンに非常に便利です！

![image41](images/entries/4991ffccebf8da94cd01acc1139f52d389731549.gif)

This feature was funded by [the QWAT project](https://github.com/qwat)

This feature was developed by [Paul Blottiere (Oslandia)](http://oslandia.com/)
### 機能：地図のズーム機能の改善
QGIS 2.16では、マップキャンバスをズームイン/ズームアウトする方法が改善されました。
- Holding down `Ctrl` while using the mouse wheel to zoom in or out now results in a finer zoom. This behavior brings canvas into line with composer.
- Pressing `Ctrl++` or `Ctrl+-` performs an immediate zoom in/out on the map canvas
- When certain map tools are active, you can perform a web-map style zoom by holding down `Shift` and dragging a rectangle on the map to zoom to that area. This is enabled for the map tools which are not selection tools (since they use shift for adding to selection), and edit tools.

![image42](images/entries/5817785cf3d18db78669c2eb2c2be0cf606c3783.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### 特長：インタラクティブなグラデーションエディタを再設計
グラデーションランプエディタは、グラデーションを簡単に操作できるインタラクティブコントロールで再加工されました。ダイアログには、カラーHSVまたはRGB値を使用してグラデーションストップを変更するためのインタラクティブなプロットも含まれています。新しいエディタの特徴：
- ドラッグしてカラーストップを移動する
- ダブルクリックして新しい停止点を追加する
- 削除を押すと選択したストップが削除されます
- 矢印キーを押すと選択したストップが移動し、カーソルキーを押しながらシフトを続けると移動が大きくなります
- ウィジェットに色をドラッグ＆ドロップして新しい停止点を追加する

![image43](images/entries/dca557436392cf51e05a0c77fa915b5e94013d2c.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Feature：属性ダイアログのデフォルトビューの選択
以前のQGISのバージョンでは、属性ダイアログは常にテーブルビューで開かれていました。これで、ダイアログを常にテーブルビュー、フォームビューのいずれかにデフォルト設定するか、または最後に使用したビューを覚えておくことができます。

![image44](images/entries/53f72a9cf1bf32d73eb5174c37e54c60002b9707.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### 機能：カレンダーポップアップの改善
Today\'s date is now highlighted in calendar popup widgets, making it easier to select a date relative to the current day.

![image45](images/entries/83b0414698c309c7afacb9da1b01370cff94497d.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### 機能：改良されたカラーピッカー
カラーボタンのドロップダウンメニューにカラーホイールが表示され、色を非常に迅速に調整できます。

![image46](images/entries/1f485fa58f218aa481acf0c118907a1cd60fd682.gif)

This feature was developed by [Nathan Woodrow](http://nathanw.net)
### 機能：セルの内容を属性テーブルからコピーする
A new context menu item called `Copy cell content` is now available in the menu opened by a right click on a cell within the attribute table. When this button is clicked, the content of the cell is copied in the clipboard, whatever the kind of widget.

![image47](images/entries/968170742ce1d075c6ab1c462e682ea4fd8c5225.png.400x300_q85_crop.webp)

This feature was developed by [Paul Blottiere (Oslandia)](http://oslandia.com/)
### 特長：HiDPIサポートの強化
HiDPI画面のユーザーは、SVG画像に依存するようにアイコンをアップグレードする作業が増えているため、ユーザーインターフェイスが向上しています。QGIS 2.16以降、すべてのツールバーはHiDPIと互換性があります。

![image48](images/entries/e60e55de87e8d2558134f9c9552ef41295642217.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### 特長：マップ選択ツールの動作を改善
マップベースの選択ツールの動作は洗練され、以下の変更が加えられました。

クリックアンドドラッグの選択肢：
- holding `Shift` = add to selection
- holding `Ctrl` = subtract from selection
- holding `Ctrl+Shift` = intersect with current selection
- holding `Alt` (can be used with `Shift`/`Ctrl` too) = change from \"intersects\" to \"fully contains\" selection mode

シングルクリックの選択：
- holding `Shift` or `Ctrl` = toggle whether feature is selected (i.e. either add to current selection or remove from current selection)

この変更により、キャンバスの動作が他のデザインアプリやコンポーザーの動作と一致します。

![image49](images/entries/4688ab87c97f9c773a62e3c1d5ceaa615cab8b0e.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## マニュアルの更新
### 機能：QGIS 2.14ドキュメント
QGISの新機能ごとにドキュメンテーションリポジトリにチケットを自動的に作成する方法があるので、私たちはすべての新機能がドキュメントに含まれていることを確信しています。

ドキュメンテーションチームは、QGISの3つのリリース（2.10,2.12、2.14）を執筆しましたので、QGISの現在のロングタームリリースのドキュメントが最新です。これは4ヶ月で文書化された約180の新機能です。

ドキュメントに欠落している機能がいくつかあると思われる場合は、新しいチケットを追加したり、小さなテキストを書いたり、投稿をよりよくプッシュしたりしてください。

The documentation team has also worked on improving the documentation guidelines in order to ease contribution\'s process for new doc writers and help translators.

ドキュメンテーションチームは、QGISの現在の安定版（2.16）を文書化するために、次の数か月間厳しい作業を行うようになります。

![image51](images/entries/3d6aea22a76278945fcbaebcb6e959c6f4f8790e.png.400x300_q85_crop.webp)

2.10、2.12、および2.14マイルストーンをチェックして、行われたすべての文書作業を確認してください。
- <https://github.com/qgis/QGIS-Documentation/milestone/5>
- <https://github.com/qgis/QGIS-Documentation/milestone/4>
- <https://github.com/qgis/QGIS-Documentation/milestone/3>

### Feature: Authentication system\'s documentation in users manual
The authentication system features introduced in earlier versions of QGIS (2.12 and 2.14) are now fully documented in the Users manual, and will be a great contribute to the system\'s understanding and adoption.

![image50](images/entries/2408c7661583ab3114123624225f8f8422c634a3.png.400x300_q85_crop.webp)

This feature was funded by [Boundless](http://boundlessgeo.com/)

この機能はLarry Shafferによって開発されました
## シンボロジ
### 機能：矢印シンボルレイヤー
The \"arrow\" symbol layer is a symbol layer allowing to draw straight or curved arrows from a line layer.

カーブモードでは、このシンボルレイヤが適用される線レイヤのノードが円弧の制御点として使用されます。QGISがサポートしている既存の塗りつぶしスタイルがあれば、矢印を塗りつぶすことができます。オプションでは、矢印のタイプ（1つまたは2つのヘッド、プレーンまたはハーフ）、幅（可変でもよい）、およびヘッドのサイズを選択することもできます。

![image52](images/entries/000cc7827fe96aa72aedb646e6497cc69a050396.png.400x300_q85_crop.webp)

This feature was funded by [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/) and Andreas Neumann

This feature was developed by [Hugo Mercier](http://oslandia.com/)
### Feature: New \"Filled marker\" symbol layer type
A \"filled marker\" is similar to the simple marker symbol layer, except that it uses a fill sub symbol to render the marker. This allows use of all the existing QGIS fill (and outline) styles for rendering markers, eg gradient or shapeburst fills.

![image53](images/entries/6107e2a6192e6d459fce2f0a1d9da99680dc53b0.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### 機能：新しいアクセシビリティと低視力シンボル
Additional accessibility and low visions symbols are now available in QGIS\' SVG symbols collection.

![image54](images/entries/7f6fc338b6f85fb59cd6e5e79b27899724e1c33e.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### 機能：新しい単純なマーカー記号
- 半円、三分の一、四分円
- ハーフトライアングルマーカー
- 十字マーカーと六角マーカー
- diamond ellipse marker

![image55](images/entries/e5f7ea942c155a0a8dff05c60aca0f299907ee02.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### Feature: \"No symbol\" renderer
Using the new \"No symbol\" renderer in QGIS 2.16 no symbol will be drawn for features, but labeling, diagrams and other non-symbol parts will still be shown.

キャンバス内のレイヤーでも選択を行うことができ、選択された地物はデフォルトのシンボルでレンダリングされます。編集中の地物も表示されます。

This is intended as a handy shortcut for layers which you only want to show labels or diagrams for, and avoids the need to render symbols with totally transparent fill/border to achieve this. It may not sound useful from the title - but it\'s quite a handy shortcut!

![image56](images/entries/4e02691b64446f5a36f4faf3cc4906726cf57aad.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### 機能：セントロイドの塗りつぶしポイントレンダリングをより詳細に制御
マーカーがマルチ地物のすべてのパーツまたは単一のパーツに描画されるかどうかを制御するオプションが追加されました。

![image57](images/entries/1a5e1daeefff5beb028c3230fffd86624974acea.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### 機能：フォントマーカーシンボルのアウトライン設定
フォントマーカー記号にアウトラインを付けることができます。アウトラインバッファーの色を追加することで、このような記号の可視性を高めることができます。絵文字が有効なフォント文字は、太い輪郭で使用すると素晴らしいマーカーとして機能します。

![image58](images/entries/be266e3dace9cc7011bfea6bab34ee8e4ade414e.jpeg.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### 機能：シンプル、楕円、フォントマーカーのアウトライン結合スタイルを制御
シンプル、楕円、フォントマーカーのアウトラインの結合スタイルを変更して、シンボルを微調整することができます。

![image59](images/entries/c6b3a2f051a8c4e3f82c5cb6a995ae150acccb4b.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### Feature：ポイントシンボルオフセットをインタラクティブに設定する新しいマップツール
Allows for setting a point\'s offset if it is bound to a field using data defined overrides. The offset field should be a text field. The map tool to interactively set the offset is in the `Advanced digitizing` toolbar in the icon group with the `Rotate Point Symbols` tool. See the attached animation for an example. Note that when making subsequent adjustments to the offset, you should drag from the original point vertex marker, not the current position of the symbol as rendered on the map.

![image60](images/entries/56a9953a6923d6b9b481b099a5a9dfec0146ba90.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### 機能：スタイルドック
The style dock is a new, far more efficient, way to manage layer styles in QGIS. It supports a live preview of style changes as they are made, full undo / redo support and a less distracted workflow as you prepare your map cartography. For a comprehensive overview of the style dock\'s features, please see [style dock part 1](https://nathanw.net/2016/06/25/improving-you-styling-with-the-qgis-style-dock-part-1/) and [style dock part 2](https://nathanw.net/2016/06/29/qgis-style-dock-part-2-plugin-panels/).

![image61](images/entries/92389e4750d63c3842286fa43fe5ef2214f7c6dd.gif)

This feature was developed by [Nathan Woodrow](https://nathanw.net/)
## ラベリング
### Feature：マップツールのラベリングは、ルールベースのラベリング
以前のバージョンのQGISでは、ルールベースのラベリングが行われていたときに、ラベリングマップツールを使用してインタラクティブにラベル位置を配置して回転することはできませんでした。これは現在サポートされています。

![image62](images/entries/fffc27648a04732d7d051734705ccef544b24fba.gif)

この機能はMartin Dobiasによって開発されました
## ダイアグラム
### 機能：図サイズの凡例エントリ
A new \"legend\" tab has been added to diagram properties, allowing both the existing attribute legend and a new size legend to be enabled/disabled. The size legend has a configurable marker symbol.

![image63](images/entries/eb51ab12f096acf0422786510fc15324060fe9e1.png.400x300_q85_crop.webp)

This feature was funded by [ADUGA](http://www.aduga.org/)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### 機能：アウトライン幅の単位選択
アウトライン幅単位の選択が可能になりました。これにより、地図の単位の大きさの図が、マップの縮尺に基づいて拡大縮小され、固定されたミリメートルの輪郭幅を維持することが可能になる。

![image64](images/entries/932c792c43a94b8236ea803ae334c1a3d9f447ef.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### 機能：ダイアグラムはラベルのように動作し、ツールバーから管理できます
もともと、ラベルのためのツールバーがありました：
- 現在のレイヤのラベルにラベル設定オプションを設定する
- 固定されたラベルを強調表示します。強調表示は編集可能なレイヤーでは緑、それ以外の場合は青色になります。
- ピンまたはピンを固定しないラベル
- ラベルの移動、表示、非表示

この新しい機能を使用すると、ラベルツールバーに新しいツールが表示され、現在のレイヤーの図のプロパティを設定できます。さらに、上で述べた各ツールは、図でも完全に使用できるようになりました。

![image65](images/entries/eb337b7d02cd7ecb923134de80a63aa62c3e8bb8.png.400x300_q85_crop.webp)

This feature was funded by [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/)

This feature was developed by [Paul Blottiere (Oslandia)](http://oslandia.com/)
## レンダリング
### 機能：オンザフライでの簡略化のための新しいオプション
ジオメトリを高速に描画するためにローカル側の簡略化を実行するときに、使用するアルゴリズムを選択できます。現在、QGISは3つのアルゴリズムを提供しています。
- 距離（既定のアルゴリズム、および以前のQGISリリースで利用可能な唯一のオプション）
- グリッドにスナップ
- 全能者

This change also moves the local \"on-the-fly\" simplification from the provider and iterator classes to the rendering code. This avoids cases where simplification changes the geometry fetched from vector data providers, possibly affecting rule based and other expression based symbology. This is important when you have expressions that use the feature geometry (e.g. calculation of area) - we want to be sure that these calculations are done on the original geometry, not on the simplified ones.

![image66](images/entries/9460e7d5f10a8c89697cef1f80674ca30d1c3aef.jpg.400x300_q85_crop.webp)

This feature was developed by [Alvaro Huarte](https://es.linkedin.com/in/alvarohuarte)
### 機能：ラスターレイヤのQuantileベースの分類
This option can be found for single band pseudocolor rasters in the classification `mode` dialog.

![image67](images/entries/844d12273c1d3d42e5f1b20367e92bc1144b77fe.png.400x300_q85_crop.webp)

この機能はPiers Titus van der Torrenによって開発されました
### Feature：ライブシェイプレンダラー
QGIS 2.16には、デジタル標高モデルから陰影モデルを動的に作成する新しいラスターレンダラーがあります。

![image68](images/entries/62f9492d1949677e316625b415ec732e63fcd3ec.gif)

この機能は、Asger Skovbo PetersenとNathan Woodrowによって開発されました
## デジタイズ
### Feature: \"Repeating\" locking mode for constraints
When enabled, repeating locks are not automatically cleared when a new point is added. They are handy when the same constraint must be repeated for multiple points (eg adding vertices which are always 50 meters apart). This functionality is available in the `Advanced Digitizing Panel`.

![image69](images/entries/f7dced55540bf500c4d9ca5a0efa9bef617c86e5.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### 機能：変形ツールで線ストリングの形状を拡張する
The reshape tool now allows you to extend linestrings, by starting a reshape at either a line\'s start or end point.

![image70](images/entries/52726f3b8cd8b62d63a32b9628dd8d3cef53172c.gif)

この機能はMartin Dobiasによって開発されました
### 機能：セグメンテーションの許容誤差
Support was added to set the segmentation tolerance (maximum angle or maximum difference). This setting controls the way circular arcs are rendered. The smaller maximum angle (in degrees) or maximum difference (in map units), the more straight line segments will be used during rendering. You can find this option in `Settings -> Options -> Rendering -> Curve Segmentation`.

![image71](images/entries/c86e3cd9ebab19e1581568eb5804c69ba279787d.png.400x300_q85_crop.webp)

この機能はMarco Hugentoblerによって開発されました
## データ管理
### Feature：属性テーブルの新しい設定オプション
- Allow reordering the attribute table columns (via right click on field name header \--\> \"Organize Columns\" dialog; drag and drop to reorder)
- 選択した機能に基づいてアクションをトリガーするためのボタンを保持するために、属性テーブルに新しい列を追加できるようにする
- カラムは属性テーブルから非表示にすることができます（フィールド名ヘッダを右クリックして）
- QGISは、サイズ変更された列の幅を記憶するようになりました

![image72](images/entries/4ac86473163c0b1e322343de1e4013262c2492ce.gif)

This feature was funded by [Canton of Zug, Switzerland](http://geo.zg.ch/) and [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/)

This feature was developed by [Stéphane Brunner (Camptocamp)](http://www.camptocamp.com/) and [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch/)
### 機能：属性フォームの複数の列
ドラッグアンドドロップデザイナーを使用する場合、ユーザーは、フィールドの分配する列の数を指定できます。

To enable multiple columns in the \"Fields\" tab of the layer properties:
- ドラッグ＆ドロップデザイナーフォームモードを使用していることを確認してください
- タブまたはグループなどのグループコンテナをダブルクリックします。
- 列の数を選択できる小さなダイアログが表示されます

順序は、最初の列、2番目の列、n番目の列、次の行などになります。

![image73](images/entries/f8297ba9ee600c3d41114db96f56b00bb278ba4e.gif)

This feature was funded by [Canton of Zug, Switzerland](http://geo.zg.ch/)

This feature was developed by [Matthias Kuhn](http://www.opengis.ch/)
### 機能：ベクターレイヤーを保存するときにエクスポートする属性を制御する
Checkboxes have been added so that you can select which attributes you want included in the export, and you also now have the option to write \"displayed\" values rather than raw values. This option is useful for layers with relations, where you\'d like a literal value included rather than a numeric identifier.

Depending on the data format, the \"displayed value\" is enabled by default, e.g. for export to spreadsheet formats (ODF, XLSX, CSV/Text).

![image74](images/entries/1c9b2b234c1ccb7a1b92af1f5856817f65dc70f1.png.400x300_q85_crop.webp)

This feature was partially funded by [Canton of Zug, Switzerland](http://geo.zg.ch/)

この機能はJürgenFischer、Even Rouault
### 機能：フォームビュー：サイドカラムがソート可能
QGIS属性テーブルのフォームモードには、特定の機能に直接ジャンプするために使用できるサイドカラムがあります。このリリースまで、この側面図はソートできませんでした。ソートのためには、テーブルモードにジャンプしてからフォームモードに戻らなければなりませんでした。サイドパネルの地物属性プレビューで、サイドカラムの上にある式のドロップダウンボタンでソート機能を選択することで、地物を直接ソートできます。

![image75](images/entries/3d6b97523db9d4389e5dbac8f0befb10d9d8f020.png.400x300_q85_crop.webp)

This feature was funded by [Canton of Zug, Switzerland](http://geo.zg.ch/)

This feature was developed by [Matthias Kuhn (OpenGIS)](http://www.opengis.ch/)
### 機能：リレーション参照ウィジェット：新しい値を追加するためのショートカット
The relation reference widget was enhanced to allow quicker extensions of related value lists. If the checkbox \"Allow adding new features\" is enabled in the widget properties (access through \"Fields\" tab in layer properties), a green plus button will appear to the right of the widget. After pressing the \"Plus\" button, the dialog of the related table will open in \"new record\" mode where one can add an additional entry.

![image76](images/entries/5788b370bc8535629699d8b69656335974ca6feb.png.400x300_q85_crop.webp)

This feature was funded by [Canton of Zug, Switzerland](http://geo.zg.ch/)

This feature was developed by [Matthias Kuhn (OpenGIS)](http://www.opengis.ch/)
### 機能：DXFエクスポートの改善
ルールベースのラベリングや回転シンボルのサポート、3Dジオメトリの出力がサポートされています。

![image77](images/entries/8a21b400f4e417df6e25f32c8b23191f1ff83628.png.400x300_q85_crop.webp)

この機能はJürgenFischerによって開発されました
### 機能：ドラッグ＆ドロップデザイナーのトップレベルウィジェット
ドラッグアンドドロップデザイナーを使用してフォームに直接ウィジェットを配置することが可能になりました。したがって、ドラッグ・アンド・ドロップのデザイナー・フォームはタブなしで存在することができます。

![image78](images/entries/720df275d40a2d527f2492bde7db4dcdc94fc3da.png.400x300_q85_crop.webp)

This feature was developed by [Matthias Kuhn](http://www.opengis.ch)
### 機能：フォームベースの選択とフィルター
In QGIS 2.16 a new mode was added to the attribute table dialog for searching and filtering features. When activated (using a button on the toolbar or by pressing `CTRL+F`), the dialog will switch to form view and all widgets are replaced with their search widget wrapper variant.

Alongside each widget is a tool button with options for controlling the search/filter behaviour for that field, eg \"equal to\", \"not equal to\", \"is null\", \"greater than\", etc.., with the options presented matching themselves to the corresponding field and widget type.

フォームの下部に新しいボタンが表示され、一致する地物を選択するか（選択範囲の追加/選択範囲からの選択/現在の選択範囲内での選択）、または表内の地物のフィルタリング（現在のフィルターに地物を追加するオプション、現在のフィルタ）。

You can also access this mode with the new \"Select by Value\" option, or by pressing F3 with a layer selected.

![image79](images/entries/481596921dd3e432cb4414b42e17fce6e7d9e84c.gif)

この機能は、SIGE、Uster市、Morges

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Feature：GeoPackageレイヤーを作成する
The [GeoPackage](http://www.geopackage.org) format is an open standard for geospatial data that should be on your radar as a replacement for the ESRI Shapefile format. It addresses many shortcomings with the shape file format including limitations in the number and width of fields. In QGIS 2.16 it is now easy to create a new GeoPackage as it has been integrated into the `Layer` toolbar and `Layer -> Create Layer` menu.

![image80](images/entries/34cfb4a4532464ab1983e561228a9a16d16dfd54.png.400x300_q85_crop.webp)

この機能はEven Rouaultによって開発されました
### 機能：ウィジェットの制約
In previous QGIS versions there was no way to check the validity of values entered by a user for a feature\'s attributes. Now, a user can specify a constraint on each widget in a layer\'s attribute form. Constraints are created using QGIS\' expressions, eg `"min_population" > 50000`. A \"Not Null\" checkbox is also available to indicate that a value must be entered for the field. Additionally, descriptive text can be added to give the user helpful feedback when a constraint fails.

Constraints are evaluated on the fly while a user is modifying a feature. A tooltip is available on any field having a constraint, showing the constraint\'s expression, the result of the evaluation and a description of the constraint. A message bar will also displayed at the top of the form summarizing any fields which do not meet the constraint criteria.

![image81](images/entries/ab562b71015b29b17a6b86e8e3c5f71838e25d50.png.400x300_q85_crop.webp)

This feature was funded by [the QWAT project](https://github.com/qwat) and the [Canton of Zug, Switzerland](http://geo.zg.ch/)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch) and [Paul Blottiere (Oslandia)](http://oslandia.com/)
### 機能：複数の地物の属性を同時に編集する
This change allows the attributes of multiple features to be edited simultaneously. It is enabled when the attribute table dialog is in \"form mode\", via a new \"multi edit\" button on the toolbar. There\'s also a shortcut to edit multiple selected features by using `Edit -> Modify Attributes of Selected Features`.

このモードでは、選択したすべての機能に属性値の変更が適用されます。新しいウィジェットが各エディタウィジェットの横に表示され、現在の複数編集状態を表示し、フィールドごとに変更をロールバックすることができます。

変更は1つの編集コマンドで行われるため、Undoを押すと選択したすべての地物の属性変更が一度にロールバックされます。

Multiedit mode is only available for auto generated and drag and drop forms -it is not supported by custom ui forms.

![image82](images/entries/d0d864bec8d2ec5bd1fa12e48ad7268a30455c82.gif)

This feature was funded by [Kanton Basel Stadt](http://www.geo.bs.ch/)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## レイヤ凡例
### Feature: New option to zoom to a layer\'s visible scale range
可視スケール範囲が設定されているレイヤーの場合、このオプションを選択すると、自動的にレイヤーが表示される最も近いスケールにスケールが設定されます。さらに、スケール範囲外で隠れているレイヤーがレイヤーツリーでグレー表示されるように、インターフェイスが調整されています。

![image83](images/entries/e15880a6d0d095c8be69eec510f8563b569e5342.gif)

This feature was funded by [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/)

This feature was developed by [Patrick Valsecchi (Camptocamp)](http://www.camptocamp.com/)
## マップコンポーザー
### 機能：ポリゴンとポリラインを描画するための新しいツール
ノードに基づいた2つの新しいタイプのコンポーザシェイプアイテムが、マップコンポーザーで使用できるようになりました。これらを使用すると、数回のクリックでコンポジション内のポリゴンまたはポリラインを描画できます。

ノードの編集（ノードの移動や削除）を可能にし、既存のシェイプに新しいノードを追加するための新しいツールも追加されました。Composerポリゴンとポリラインアイテムは、ラインレイヤーとポリゴンレイヤーで使用できるすべてのシンボルスタイルを使用してスタイリングすることもできます。

![image84](images/entries/52e5ebd093c119ee882b1c354fefc97f5e823ffc.png.400x300_q85_crop.webp)

This feature was funded by [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/)

This feature was developed by [Paul Blottiere (Oslandia)](http://oslandia.com/)
### 機能：コンポーザラベルの相対リンク
Now labels and HTML boxes can contain relative URLs. If we don\'t have a base URL, the project file will be used as a base URL.

![image85](images/entries/5efabc11a312d90df04591a62cbafbb85b0ffc4d.png.400x300_q85_crop.webp)

This feature was funded by [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/)

This feature was developed by [Patrick Valsecchi (Camptocamp)](http://www.camptocamp.com/)
### 機能：GeoJSONをソースとしてコンポーザのHTMLソースに地図帳の機能を埋め込む
This change makes the current atlas feature (and additionally all attributes of related child features) available to the source of a composer HTML item, allowing the item to dynamically adjust its rendered HTML in response to the feature\'s properties. An example use case is dynamically populating a HTML table with all the attributes of related child features for the atlas feature.

To use this, the HTML source must implement a \"setFeature(feature)\" JavaScript function. This function is called whenever the atlas feature changes, and is passed the atlas feature (and all related attributes) as a GeoJSON Feature.

![image86](images/entries/15b7c338bb2fa76444929f3c7ae6fd6614018032.png.400x300_q85_crop.webp)

This feature was funded by [Canton of Zug, Switzerland](http://geo.zg.ch/)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com/)
### 機能：コンポーザーSVG画像のパラメーター化されたSVGサポート
This change makes it possible to change an SVG files fill and outline colors, and outline width when using parameterised SVG files such as those included with QGIS. For more details on parameterised SVG files see [this article](http://blog.sourcepole.ch/2011/06/30/svg-symbols-in-qgis-with-modifiable-colors/).

![image87](images/entries/f9766e2ad952c9a3d4a7fe2ddbdfa20d63b2aff4.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### 機能：ラベルにHTMLを簡単に使用する
In QGIS 2.16, the base stylesheet of composer labels will automatically set the label font and margins to match the label\'s settings. This allows interactive choice of font, margins and colors and avoids the need to manually set these with CSS within the label HTML code.

![image88](images/entries/d078efbe63f71e8bdf28d476f9da0396f4b7dc0a.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### 機能：コンポーザからのジオリファレンス出力（PDFなど）
QGIS 2.16では、マップコンポーザーが出力を自動的にジオリファレンスします（出力フォーマットでこれを可能にする場合、TIFやPDFなど）。

ワールドファイルを作成する既存のオプションは、地理参照のためのマップ選択から分離されています。新しい動作は、常に出力をジオリファレンスすることです。そのオプションがチェックされている場合は、別のワールドファイルのみを作成します。

![image89](images/entries/e05ee773025d69f028f01ffa15521578be7d3dc3.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### 機能：コンポーザ地図はプリセットで自動更新されるようになりました
コンポーザーマップがスタイルプリセットに従うように設定されている場合は、スタイルが変更されるたびに自動的に更新されます。

A new option has been added in composer map properties: \"Follow visibility preset\" with a combo box to choose the active preset. This is an alternative to \"lock layers\" (and \"lock layer styles\") functionality which just copy a preset\'s configuration, while this new option creates a link to the preset.

The difference is that when a preset is updated, composer map will automatically pick the new configuration when following the preset, while there is no update if \"lock layers\" (and \"lock layer styles\") option is used.

![image90](images/entries/6ef5520185d80b38adcbba6c54e4fbdb6c2584fc.gif)

この機能はMartin Dobiasによって開発されました
## 分析ツール
### 機能：式の名前付きパラメータ
In QGIS 2.16 the expression engine now supports use of named parameters. This means that instead of writing the cryptic expression: `clamp(1,2,3)` you can use: `clamp( min:=1, value:=2, max:=3)`. This change also allows arguments to be switched, eg: `clamp( value:=2, max:=3, min:=1)`.

名前付きパラメータを使用すると、式関数の引数が参照するものを明確にすることができます。これは、後で式を解釈しようとするときに役立ちます。

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### 機能：遠距離ユニット
距離単位の選択肢が広がり、キロメートル、ヤード、マイルなどの新しいオプションが追加されました。これらのユニットを使用すると、手動で距離を変換する必要がなくなります（例：フィートをマイルに変換）。

![image91](images/entries/a550363f123d3bf08bd53fef79dc92559ae8965d.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Feature: Changes to expressions
- Support `date + time` = datetime calculations
- Support for `date - date`, `time - time` and `datetime - datetime` type calculations which return an interval.
- New `char()` function for returning a matching character by unicode value

### 機能：文字列と日付フィールドの統計
統計サマリードックは、文字列と日付フィールドの集計統計を計算できるようになりました。

![image92](images/entries/819559c98282bcf044fae47ddcc00908be3adf69.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### 機能：インフォメーションツールでカーブポイントの半径を表示
インフォツールを使用して曲線をクリックすると、QGISはインフォツールに半径を表示します。

![image93](images/entries/70f085e8494b3f65fd801b79fe6e15fe4ec7f012.png.400x300_q85_crop.webp)

この機能はMarco Hugentoblerによって開発されました
### 機能：式の集約サポート
QGIS 2.16では、いくつかのタイプの集約のサポートがエクスプレッションエンジンに追加されています。これらには、
1. Aggregates within the current layer, eg `sum("passengers")` Supports sub expressions (ie `sum("passengers"/2)` ), group by ( `sum("passengers", group_by:="line_segment")` ), and optional filters ( `sum("passengers", filter:= "station_class" > 3 )` )
2. Relational aggregates, which calculate an aggregate over all matching child features from a relation, eg `relation_aggregate( 'my_relation', 'mean', "some_child_field" )`
3. A summary aggregate function, for calculating aggregates on other layers. Eg `aggregate('rail_station_layer','sum',"passengers")`. The summary aggregate function supports an optional filter, making it possible to calculate things like: `aggregate('rail_stations','sum',"passengers", intersects(@atlas_geometry, $geometry ) )` for calculating the total number of passengers for the stations inside the current atlas feature

すべての場合、計算は式コンテキスト内にキャッシュされるため、式評価の各セットに対して1回計算する必要があります。

This feature was funded by [Canton of Zug, Switzerland](http://geo.zg.ch/)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### 機能：fToolsプラグインが処理アルゴリズムに置き換えられました
fTools is a core plugin that for many years has provided the tools found in the `Vector` menu in QGIS. With the advent of the QGIS processing framework, the fTools began to represent a duplication of effort, and many of the tools have been improved in their Processing equivalents. To address, the fTools plugin has been removed from QGIS and equivalent menu entries have been added to the vector menu, pointing to the Processing framework tools that achieve the same thing.

![image94](images/entries/99f9e994013dd63cdbba44a765ae5b5a0595d533.png.400x300_q85_crop.webp)

この機能は Alex Bruy によって開発されました
## プロセシング
### 機能：キャンバスをクリックしてポイントの位置を設定する
ポイントキャンバス上の場所をクリックすると、ポイントの位置を予期する処理パラメータを設定できるようになりました。以前は、座標を手動で入力する必要がありました。

この機能は Alex Bruy によって開発されました
### 機能：式と変数のサポート
アルゴリズムダイアログの入力と出力は、QGISの式と変数をサポートするようになりました。

この機能はVictor Olayaによって開発されました
### 機能：あらかじめ設定されたアルゴリズム
所定のプロセスのショートカットとして、事前に設定されたパラメータを持つアルゴリズムを処理ツールボックスに追加できるようになりました。

この機能はVictor Olayaによって開発されました
### 機能：ツールボックスからスクリプトベースのアルゴリズムを使用してプラグインを作成する
以前は、Processingに新しいアルゴリズムを追加したQGISプラグインを作成する唯一の方法は、これらのアルゴリズムを手動で開発し、新しいアルゴリズムプロバイダを作成することでした。アルゴリズムは単純な処理スクリプトとして記述でき、それらを含むプラグインはProcessing Toolboxから直接作成することができます。そのプラグインは通常のプラグインとして配布することができ、アクティブなときに処理を拡張します。

この機能はVictor Olayaによって開発されました
### 機能：PostGIS関連アルゴリズムにおける認証マネージャーの使用
PostGIS関連のアルゴリズムでは、QGIS認証マネージャを使用してPostGISデータベースの認証情報を取得します。
- PostGIS接続時に認証方法が設定されている場合は、マスターパスワードを尋ねられます。
- 接続時に認証方法が設定されていない場合、資格証明は資格証明キャッシュから取得されます。存在しない場合は、ユーザーに依頼し、資格証明キャッシュに保存して後で使用します。

これにより、PostGIS関連のアルゴリズムを使用するために、接続設定にクリアパスワードを格納する必要がなくなりました。

This feature was funded by [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/)

This feature was developed by [Arnaud Morvan (Camptocamp)](http://www.camptocamp.com/)
### 機能：ジオメトリを持たない表の作成をサポート
OutputVectorアルゴリズムでは、ジオメトリレステーブルの作成がサポートされるようになりました。

今のところ、これはRefactor Fieldsアルゴリズムにのみ適用されていますが、他の属性関連アルゴリズムにも容易に拡張できます。

This feature was funded by [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/)

This feature was developed by [Arnaud Morvan (Camptocamp)](http://www.camptocamp.com/)
### 機能：処理中の追加のGRASSアルゴリズム
For this release, QGIS Processing now includes every [vector](https://grass.osgeo.org/grass70/manuals/vector.html), [raster](https://grass.osgeo.org/grass70/manuals/raster.html) and [imagery](https://grass.osgeo.org/grass70/manuals/imagery.html) algorithms from GRASS7. Now, there are more than 300 algorithms for you to use directly from the QGIS interface. You have all the power of GRASS7 directly incorporated into QGIS and you can mix GRASS7 algorithms with all other Processing algorithms without having to use a GRASS7 database.

いくつかのアルゴリズムでは、ユニットテスト（主にラスター画像アルゴリズム用）が含まれているため、バグの検出が処理しやすくなりました。

現時点では、GRASS7処理アルゴリズムはシェープファイルベクターレイヤーとGeoTiffラスターのみを使用して生成できます。ラスターレイヤーを一時ディレクトリに複製するGRASS7ラスターアルゴリズム（カラーテーブルを操作するすべてのアルゴリズム）には制限があります。ソースラスターのサイズによっては、それらを処理するためのディスクスペースが必要になることがあります。

この機能は [Médéric Ribreux](https://medspx.fr) によって開発されました
## データプロバイダ
### 機能：OGRデータセットは既定で読み取り専用モードで開きます
QGISとMapInfoの両方でシェイプファイルとタブファイルを同時に編集できます。

This feature was funded by [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/)

この機能はEven Rouaultによって開発されました
### PostgresのDOMAIN型フィールドの扱いが改善されました。
QGIS now shows the correct domain type as field type name, and is able to correctly determine the length and precision of domain types. See the PostgreSQL [documentation](https://www.postgresql.org/docs/9.1/static/sql-createdomain.html) to find more information about DOMAIN types.

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### 機能：プロジェクトで設定可能なベクターレイヤのreadOnlyモードを作成する
Using this option, you can prevent users from inadvertently editing layers. Go to `Project properties -> Identify layers` to configure which layers should be presented as read only.

![image101](images/entries/9fce381bdf92bd039a26282a93579d5d5ef22e92.png.400x300_q85_crop.webp)

This feature was developed by [Matthias Kuhn](http://www.opengis.ch/)
### 機能：DB2データベースのサポート
この機能はDavid Adlerによって開発されました
### 機能：PostgresのDBマネージャでのマテリアライズドビューのリフレッシュ
### 機能：OGR FID属性が表示されます
QGISは、例えばGPKGや他のデータベースベースのドライバのように、OGR FIDを意味があるときは最初の属性として公開するようになりました。

この機能はEven Rouaultによって開発されました
### Feature: ArcGIS Map and Feature REST services
QGISはArcGIS RESTサービスに接続できるようになりました。

ArcGIS Featureサービス（ESRIではWFSに相当）とArcGIS Mapサービス（WMSに相当）に接続できます。プロバイダを使用すると、それらのサービスからマップおよびベクターレイヤーを読み取ることができます。

この機能は、既にプライベートまたはパブリックマップサービスで構築したものを失うことなく、ESRI GISスタックから切り替えたいユーザにとっては非常に便利です。ESRIが提供する公共サービスにも接続できます。

This feature was funded by [Sourcepole QGIS Enterprise](http://qgisenterprise.com/)

This feature was developed by [Sandro Mani, Sourcepole](https://www.sourcepole.com/)
### 機能：MS SQLおよびOracleデータベースのスタイルを保存する
この機能は、JürgenFischerとChristian Frugardによって開発されました
### 機能：レイヤー内のフィールドの名前を変更する
QGIS 2.16では、レイヤプロパティウィンドウのフィールド名をダブルクリックすることで、Postgres、Oracle、OGR、およびメモリレイヤのフィールドの名前を変更できるようになりました。

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### 機能：Oracle Workspace Managerの基本サポート
Oracle Providerを使用する場合、Oracle Workspace Managerのサポートが追加されました。

See <https://github.com/qgis/QGIS/commit/d161612bd216d36dc23ab2307636cf1bc0a36192>

This feature was funded by [ENEL](https://www.enel.com)

This feature was developed by [Jürgen Fischer for Faunalia](http://faunalia.it)
### WFSプロバイダの大幅な改善
QGIS 2.16は、WFSプロバイダのオーバーホールをもたらします。
- バージョンの自動検出
- ダウンロードした機能のオンディスクキャッシュ
- バックグラウンドダウンロードとプログレッシブレンダリング
- WFS 1.1および2.0のサポート
- WFS 2.0 GetFeatureページング
- プロバイダテストを追加する
- WFS 2.0結合のサポート
- sqlにSELECT / FROM / JOIN / WHERE / ORDER BY句を含むURIパラメータ
- 日付時刻フィールドの処理
- Enable \"Only request features overlapping the view extent\" by default (and memorize the settings)
- 追加/混合ジオメトリタイプのサポート（CurvePolygon、CompoundCurve）
- 適合していないWFSサーバーに対する許容量の増加

![image102](images/entries/d69f2cc2fcc59b26d830bb84c82d5e6c9d89beae.png.400x300_q85_crop.webp)

This feature was funded by [Land Information New Zealand and Canton of Zug, Switzerland](http://www.linz.govt.nz/)

This feature was developed by [Even Rouault](http://www.spatialys.com/)
### Feature: Generation of default values on Postgres layers \"just in time\"
postgresデータベースのフィールドのデフォルト値を生成するために使用される式は、現在、地物フォームに出力されています。

    nextval('serial')
    
A new option in the \"project properties\" (tab \"Data Sources\") allows evaluating the expression before opening the form and will directly print the new value in the feature form.

    23
    
この改善の主な利点は、機能を保存する前に主キーが既に存在するため、関連するテーブルのレコードを直接作成してリンクすることができることです。

![image103](images/entries/6d4b378f46ee1338b7aa80f15adf2ea8e510909e.png.400x300_q85_crop.webp)

This feature was funded by [Canton of Zug, Switzerland](http://geo.zg.ch/)

This feature was developed by [Matthias Kuhn](http://www.opengis.ch/)
## QGISサーバー
### 機能：GetMapとGetPrintでのレッドラインサポート
この機能はゾーロトゥルンの資金提供を受けています

This feature was developed by [Marco Hugentobler, Sourcepole](https://www.sourcepole.com/)
### 機能：サーバのデフォルトのデータ変換
Will have to dig through <https://github.com/qgis/QGIS/commit/70863ecaf0ccfcb538e3892af4b528304b21a0a2> to find details

This feature was developed by [Marco Hugentobler (Sourcepole)](https://www.sourcepole.com/)
## プラグイン
### Feature：Refreshed globe plugin
- OsgEarth 2.8へのアップデート
- QGISグローブタイルドライバのリライト
- 2Dと3D間の同期ロジックの書き換え
- 新しいジオメトリカーネルへの移行
- 複数の背景レイヤのサポート
- 地球儀ウィンドウに埋め込まれたメニュー
- グローブの独立レイヤー選択
- QGIS 2.1 / OsgEarth 2.4のMathias Kuhns卒業論文執筆

![image104](images/entries/f709cc02852b833f459f30431f38f868d69ebfad.jpg.400x300_q85_crop.webp)

This feature was funded by [Sourcepole QGIS Enterprise](http://qgisenterprise.com/)

This feature was developed by [Sandro Mani, Sourcepole](https://www.sourcepole.com/)
### 機能：グローブ：押し出しオブジェクト
オブジェクトを3次元に押し出すことができます。

固定値または属性または式のいずれか。

This feature was developed by [Matthias Kuhn](http://www.opengis.ch)
### Feature：API：ベクターレイヤのプロパティにページを追加する
ベクターレイヤのプロパティダイアログにページを追加できるようにします。

これにより、より適切なユーザーエクスペリエンスのために、プラグインが提供するレイヤー関連オプションの設定を直接どこに所属させるかを設定できます。

This feature was developed by [Matthias Kuhn](http://www.opengis.ch)
### 機能：グローブ：ベクターサポート
グローブ上にレイヤーを表示するときは、ベクターデータを保持します。

この機能はMaster Thesis UZHによって資金提供されました

This feature was developed by [Matthias Kuhn](http://www.opengis.ch)
### 機能：地球儀：DTMのための垂直方向の強調
Because sometimes it\'s just nice to exaggerate about the size.

This feature was developed by [Matthias Kuhn](http://www.opengis.ch)
## プログラマビリティ
### 機能：レイヤーツリー内の組み込みウィジェット
これにより、レイヤプロパティダイアログ（新しい凡例タブ内）で個々のレイヤのレイヤツリーに埋め込まれたウィジェットを定義することができます。このアイデアは、レイヤーでよく使用されるいくつかのアクションに素早くアクセスする方法を持つことです。

実装には透過ウィジェットが付属しています。将来は、フィルタリング、選択、スタイルなどの設定を行うなど、より標準的なウィジェットが提供される可能性があります。APIを使用すると、プラグインは独自のウィジェットを登録できます。これにより、さまざまなドメイン固有のプラグインが、カスタムウィジェットを管理するレイヤーに割り当てることができます。

![image105](images/entries/f6cd05f9d927a47543b0c3b1fba740d86a226076.png.400x300_q85_crop.webp)

この機能は、Martian Dobiasによって開発されました
### 機能：プラグインは、ページをベクターレイヤのプロパティに追加できます
This feature was developed by [Sandro Mani (Sourcepole)](https://www.sourcepole.com/)
### Feature: New PyQGIS classes in 2.16
### 新しいコアクラス
- [QgsComposerNodesItem](https://qgis.org/api/classQgsComposerNodesItem.html) -an abstract base class for composer items which provides generic methods for nodes based shapes such as polygons or polylines
- [QgsComposerPolygon](https://qgis.org/api/classQgsComposerPolygon.html) - a composer item for polygon shapes
- [QgsComposerPolyline](https://qgis.org/api/classQgsComposerPolyline.html) -a composer item for polyline shapes
- [QgsGroupUngroupItemsCommand](https://qgis.org/api/classQgsGroupUngroupItemsCommand.htmll) -a composer undo command class for grouping / ungrouping composer items
- [QgsConstWkbSimplifierPtr](https://qgis.org/api/classQgsConstWkbSimplifierPtr.html) -WKB reader which simplifies geometries on the fly
- [QgsAction](https://qgis.org/api/classQgsAction.html) - a utility class that encapsulates an action based on vector attributes
- [QgsActionManager](https://qgis.org/api/classQgsActionManager.html) - stores and manages actions associated with a layer
- [QgsAggregateCalculator](https://qgis.org/api/classQgsAggregateCalculator.html) -a utility class for calculating aggregates for a field (or expression) over the features from a vector layer
- [QgsAttributeTableConfig](https://qgis.org/api/classQgsAttributeTableConfig.html) -a container for configuration of the attribute table for a vector layer
- [QgsDateTimeStatisticalSummary](https://qgis.org/api/classQgsDateTimeStatisticalSummary.html) -calculator for summary statistics and aggregates for a list of datetimes
- [QgsInterval](https://qgis.org/api/classQgsInterval.html) - a representation of the interval between two datetime values
- [QgsJSONExporter](https://qgis.org/api/classQgsJSONExporter.html) - handles exporting QgsFeature features to GeoJSON features
- [QgsJSONUtils](https://qgis.org/api/classQgsJSONUtils.html) - helper utilities for working with JSON and GeoJSON conversions
- [QgsRuntimeProfiler](https://qgis.org/api/classQgsRuntimeProfiler.html) -simple profiler for timing code paths during execution
- [QgsSQLStatement](https://qgis.org/api/classQgsSQLStatement.html) - utility class for parsing SQL statements
- [QgsStringStatisticalSummary](https://qgis.org/api/classQgsStringStatisticalSummary.html) -calculator for summary statistics and aggregates for a list of strings
- [QgsHillshadeRenderer](https://qgis.org/api/classQgsHillshadeRenderer.html) - a renderer for generating live hillshade models
- [QgsArrowSymbolLayer](https://qgis.org/api/classQgsArrowSymbolLayer.html) -line symbol layer used for representing lines as arrows
- [QgsNullSymbolRenderer](https://qgis.org/api/classQgsNullSymbolRenderer.html) -a renderer which draws no symbols for features by default, but allows for labeling and diagrams for the layer
- [QgsSimpleMarkerSymbolLayerBase](https://qgis.org/api/classQgsSimpleMarkerSymbolLayerBase.html) -abstract base class for simple marker symbol layers. Handles creation of the symbol shapes but leaves the actual drawing of the symbols to subclasses.
- [QgsFilledMarkerSymbolLayer](https://qgis.org/api/classQgsFilledMarkerSymbolLayer.html) -filled marker symbol layer, consisting of a shape which is rendered using a QgsFillSymbolV2

### 新しいGUIクラス
#### 再利用可能なウィジェット：
- [QgsMultiEditToolButton](https://qgis.org/api/classQgsMultiEditToolButton.html) -a tool button widget which is displayed next to editor widgets in attribute forms, and allows for controlling how the widget behaves and interacts with the form while in multi edit mode
- [QgsSearchWidgetToolButton](https://qgis.org/api/classQgsSearchWidgetToolButton.html) -a tool button widget which is displayed next to search widgets in forms, and allows for controlling how the widget behaves and how the filtering/searching operates
- [QgsLayerTreeEmbeddedConfigWidget](https://qgis.org/api/classQgsLayerTreeEmbeddedConfigWidget.html) -a widget to configure layer tree embedded widgets for a particular map layer
- [QgsLayerTreeEmbeddedWidgetProvider](https://qgis.org/api/classQgsLayerTreeEmbeddedWidgetProvider.html) -provider interface to be implemented in order to introduce new kinds of embedded widgets for use in layer tree
- [QgsLayerTreeEmbeddedWidgetRegistry](https://qgis.org/api/classQgsLayerTreeEmbeddedWidgetRegistry.html) -registry of widgets that may be embedded into layer tree view
- [QgsAttributeFormEditorWidget](https://qgis.org/api/classQgsAttributeFormEditorWidget.html) -a widget consisting of both an editor widget and additional widgets for controlling the behaviour of the editor widget depending on a number of possible modes
- [QgsComposerItemComboBox](https://qgis.org/api/classQgsComposerItemComboBox.html) -a combo box which displays items of a matching type from a composition
- [QgsCompoundColorWidget](https://qgis.org/api/classQgsCompoundColorWidget.html) -a custom QGIS widget for selecting a color, including options for selecting colors via
- 色相ホイール、カラースウォッチ、カラーサンプラー
- [QgsDockWidget](https://qgis.org/api/classQgsDockWidget.html) - QDockWidget subclass with more fine-grained control over how the widget is closed or opened
- [QgsFocusWatcher](https://qgis.org/api/classQgsFocusWatcher.html) - an event filter for watching for focus events on a parent object
- [QgsGradientStopEditor](https://qgis.org/api/classQgsGradientStopEditor.html) -an interactive editor for previewing a gradient color ramp and modifying the position of color stops along the gradient
- [QgsMapLayerConfigWidget](https://qgis.org/api/classQgsMapLayerConfigWidget.html) -a panel widget that can be shown in the map style dock
- [QgsMapLayerConfigWidgetFactory](https://qgis.org/api/classQgsMapLayerConfigWidgetFactory.html) -factory class for creating custom map layer property pages
- [QgsPanelWidget](https://qgis.org/api/classQgsPanelWidget.html) - base class for any widget that can be shown as a inline panel
- [QgsPanelWidgetWrapper](https://qgis.org/api/classQgsPanelWidgetWrapper.html) -inline panel wrapper widget for existing widgets which can\'t have the inheritance tree changed, e.g dialogs
- [QgsPanelWidgetStack](https://qgis.org/api/classQgsPanelWidgetStack.html) -a stack widget to manage panels in the interface
- [QgsShortcutsManager](https://qgis.org/api/classQgsShortcutsManager.html) -a class that contains a list of QActions and QShortcuts that have been registered and allows their shortcuts to be changed
- [QgsTableWidgetItem](https://qgis.org/api/classQgsTableWidgetItem.html) -this can be used like a regular QTableWidgetItem with the difference that a specific role can be set to sort
- [QgsHillshadeRendererWidget](https://qgis.org/api/classQgsHillshadeRendererWidget.html) -renderer widget for configuring the hill shade renderer
- [QgsRasterTransparencyWidget](https://qgis.org/api/classQgsRasterTransparencyWidget.html) -widget for controlling a raster layer\'s transparency and related options
- [QgsArrowSymbolLayerWidget](https://qgis.org/api/classQgsArrowSymbolLayerWidget.html) -renderer widget for configuring arrow symbol layers

#### 再利用可能なダイアログ：
- [QgsOrganizeTableColumnsDialog](https://qgis.org/api/classQgsOrganizeTableColumnsDialog.html) -dialog for organising (hiding and reordering) columns in the attributes table
- [QgsConfigureShortcutsDialog](https://qgis.org/api/classQgsConfigureShortcutsDialog.html) -dialog for allowing users to configure shortcuts contained in a QgsShortcutsManager
- [QgsNewGeoPackageLayerDialog](https://qgis.org/api/classQgsNewGeoPackageLayerDialog.html) -dialog to set up parameters to create a new GeoPackage layer
- [QgsSourceSelectDialog](https://qgis.org/api/classQgsSourceSelectDialog.html) -generic widget class for listing layers available from a remote service

## 注目すべき修正
### 特集：QGISの有料バグ修正プログラム
私たちは、バグ修正のもう一つのラウンドを行いました（スポンサーとドナーのおかげで！）。参加した開発者の作業概要を以下に示します。
### Nyall Dawson
Here\'s the full list (sorted by priority):
- ジオレフェレーターで破損した射影変換を修正（＃14551  - 厳しい）
- 半径による地物の選択が失敗する（＃14748  - 重大）
- ポリゴンの不正確な面積計算を修正しました（＃14675  - 重大ですが、発生はほとんどありませんが、このエッジケースをカバーするためにユニットテストが追加されました）
- ドックウィジェットのレイアウトを修正（＃15011  - 厳しい）
- 矢印シンボルレイヤのクラッシュを修正（未報告）
- 無効な結合（報告されていない）を作成するときにクラッシュを修正しました。
- コンポーザーの矢印項目に表示されていないパラメータ化されたSVGを修正しました（＃14997  - 高）
- Classifications on joined fields should only consider values which are matched to layer\'s features (#9051 - high)
- 文字列フィールドの式では常に文字列比較を使用します（＃13204  - 高）
- ホームディレクトリがデフォルトのSVGとテンプレートパスとして追加されるように修正しました（＃14662、＃14652、＃14883  - 高）
- ヒートマップレンダラーで逆ポリゴンを使用するとクラッシュする問題を修正しました（＃14968  - 高）
- ラスタシンボル値を完全精度で保存する（＃14950  -  normal）
- レイヤーをデフォルトのスタイル（＃13910  -  normal）で読み込むと、アクションは有効になりません
- Remove \"attribute table\" text from dialog title (#14959 - normal)
- フィックスはカスタマイズウィジェットキャッチャーを非アクティブ化できません（＃9732  - 正常）
- 矢印シンボルのレイヤーヘッドの幅/高さを反転させて修正（＃15002  - 正常）
- プロジェクトを不良レイヤーでロードするときに修正結合が再作成されない（＃10500  - 正常）
- レイヤーが変更されたときに結合キャッシュを無効にする（＃11140  - 正常）
- 仮想フィールドを使用して結合を正しくサポートする（＃14820  -  normal）
- 他の仮想フィールドに依存する修正仮想フィールドは、状況によっては計算されない場合があります（＃14939  - 正常）
- Pythonの式関数を使用するときに表示されないルールベースのラベルを修正しました（＃14985  -  normal）
- スタイルドックでシンボルレベルが変更されたときの自動リフレッシュ（＃14861  -  normal）
- ドック状態に同期されていない固定スタイルのドックボタンを修正（＃14862  - 正常）
- SVGをテキストで描画する問題を修正しました（＃14644、＃14794  -  normal）
- データ定義ボタンの表示フィールドが常に最新であることを確認する（＃14809  - 正常）
- 修正はズームインのショートカットを設定できません（＃14958  - 通常）
- Fix inverted polygons and displacement renderer don\'t allow right click on legend items (#14966 - normal)
- Fix inverted polygon & displacement renderer don\'t show colour wheel in legend menu (#14967 - normal)
- 凡例チェックの動作に欠けているプロキシを逆ポリゴンレンダラーと置換レンダラーのサブレンダラーに追加する（未報告）
- Fix joined attributes can\'t be used in filter expressions (#13176 - low)
- ベクターレイヤーのメタデータにWKBタイプを表示する（報告されていない）
- 不足している機能文字列をレイヤーメタデータに追加する（未報告）
- 25Dジオメトリレイヤを使用した場合のデバッグノイズを修正（未報告）
- いくつかのステータスバーウィジェットをカスタマイズして非表示にすることができない問題を修正しました（未報告）
- スタイリングウィジェットを生かして設定を保存する（未報告）
- Don\'t show constraint messages when form is in search mode (unreported)
- 地物情報として属性フォームのスクロールバーを表示する（未報告）
- スタイルドックにするApplyボタンは常に有効（未報告）
- スタイルドックからいくつかの欠落している自動更新を修正（未報告）

I also forward ported a bunch of fixes from Sourcepole\'s fork.
### Even Rouault
QGIS 2.16のバグ修正のために割り当てられた時間中に彼が処理したチケットはここにあります。

**重度/高：**
- <https://issues.qgis.org/issues/15006>: Crashes in standalone browser
- <https://issues.qgis.org/issues/14876>: WFS client broken in QGIS master
- <https://issues.qgis.org/issues/13762>: Error accessing external WMS server \--WMS provider: Cannot calculate extent
- <https://issues.qgis.org/issues/14927>: Attribute table sorting problem with qgis-rel-dev (2.14.X regression)
- <https://issues.qgis.org/issues/15064>: QGIS crashes on OGR layers with wkbUnknown25D, wkbUnknownM/Z/ZM layer geometry type
- <https://issues.qgis.org/issues/14844>: Oblique Mercator projection hanging when rendering map
- <https://issues.qgis.org/issues/15047>: ASSERT failure in QVector\[HTML_REMOVED\]::at: \"index out of range\" in qgis_attributetabletest (TestQgsAttributeTable)
- <https://issues.qgis.org/issues/15087>: Crash when deleting the last segment of a compoundcurve

**Normal**
- <https://issues.qgis.org/issues/14965>: wfs provider copies features when zooming in and out
- <https://issues.qgis.org/issues/14928>: WMS request without BBOX
- <https://issues.qgis.org/issues/14999>: Spatialite provider does not support alphanumeric primary keys (backport in 2.14)
- <http://hub.qgis.org/issues/15061>: Cannot add WFS layer
- <https://issues.qgis.org/issues/15065>: Failed detection of geometry type in some conditions
- <https://issues.qgis.org/issues/15066>: OGR: Sublayers detected sometimes when not relevant (Polygon/CurvePolygon)
- <https://issues.qgis.org/issues/15067>: DXF export creates invalid file
- <https://issues.qgis.org/issues/15081>: Impossible to clear geometry of feature from a shapefile
- unreported \[Geometry\] Fix various issues related to Wkb/Wkt import

**その他：**
- <https://issues.qgis.org/issues/14981>: Import of Shapefile to Geopackage-Database in DB-Manager fails (analysis)
- <https://issues.qgis.org/issues/15011>: Browser panel is unusable (bisection & analysis)
- <https://issues.qgis.org/issues/14909>: regression: QGIS crashes when closing docked attribute table (analysis)
- <https://issues.qgis.org/issues/13353>: QGIS and gdal 2.0.0 (closed: no further action needed)
- <https://issues.qgis.org/issues/15053>: WMS with EPSG:31255 is shifted (datum=hermannskogel) (analysis. probably outdated proj.4 version)

### サンドロサンティリ
- <http://hub.qgis.org/issues/14262>: Overflow on primary key with negative values; cannot save edits
- <http://hub.qgis.org/issues/12228>: Deadlock from parallel rendering
- <http://hub.qgis.org/issues/11371>: Map Composer: group + move + ungroup + undo = crash
- <http://hub.qgis.org/issues/14976>: Repository files modified by \"make check\"
- <http://hub.qgis.org/issues/13635>: Different handling of invalid geometries between LTR and master version
- <http://hub.qgis.org/issues/13952>: QGIS node tool causes snapping another feature randomly

### Martin Dobias
- Digitizing: \"Simplify Feature\" should not open a dialog when no feature is clicked
- Digitizing: how to abort \"Simplify Feature\" or \"Rotate Feature\" tool is not that obvious
- ベクターレイヤを追加すると1つの道路が欠落します！
- オートトレースはジオメトリの円弧で失敗する
- WMSがマスターa625eeb（2.15.0-80）で動作していません
- 事前設定されたアルゴリズムの処理Pythonエラー
- GPS don\'t record geometry point, but only attribute values\...
- スタイルドック：透明パネル（グローバル透明度、透明ピクセルなど）は、陰影レンダリングでは機能しません
- スタイルベースのドック：ルールベースのラベルルールの編集時に戻るボタンとブレッドクラムが表示されない
- スタイリングドックのルールベースレンダラー/ラベリングの取り消し/やり直しを修正
- スタイリングパネルでアンドゥウィジェットのアップデートを修正
- style dock: hillshade renderer\'s global transparency value resets after changing symbology settings
- style dock: values of raster\'s layer rendering options not properly restored

### Matthias Kuhn
- QgsMapLayerRegistryの安定性を改善する
- Processing: Difference algorithm: don\'t ignore invalid geometries by default
- Python 3の互換性の問題を修正
- osxテストを再度有効にする作業（2.16リリース後に統合）
- APIドキュメント
- startup.pyが2回実行される
- UXの修正点：
  - 属性表：常に列ヘッダー番号を表示する
  - リレーション参照ウィジェット：機能が設定されている場合にのみフォームボタンを有効にする
  - 属性テーブルのツールチップに機能IDを表示する
  - 信任状ダイアログの初期ウィジェットフォーカス
  - メッセージバー項目のデフォルトのタイムアウト
  - Add button\" state in postgis source select dialog
- 不足しているヘッダファイルをインストールする
- 出口でクラッシュする
- ネットワークキャッシュディレクトリ
- Windows上のメインウィンドウの後ろに隠された機能フォーム
- オフライン編集：相対パスを尊重する
- オフライン編集：変更された属性が間違った機能で終了する
- Offline editing: Don\'t crash with raster layers
- 関係フォームは無限に成長する
- レイヤプロパティでスタイルを読み込む際にクラッシュを修正しました。
- ドッキングされた属性テーブルを閉じるときのクラッシュを修正
- デフォルトで設定されていないgpsbabelパスを修正
- ジオメトリが必要なルールで正しい地物数を表示する
- 互換性のないレイヤーで2.5Dレンダラーを使用するとクラッシュする問題を修正しました。

{{<content-end >}}
