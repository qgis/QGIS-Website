---
HasBanner: false
draft: false
releaseDate: '2018-06-22'
section: project
sidebar: true
title: QGIS 3.2の変更履歴
type: visual-changelog

---
{{<content-start >}}
# QGIS 3.2の変更履歴{#changelog32 }
![image1](images/projects/8f04d904f903b8bff930e6c968fe46928e6cc012.png)

Release date: 2018-06-22

The greatest QGIS release ever! QGIS 3.2 brings a massive list of new changes - the highlights of which we will try to cover here. As always can we remind you that QGIS is an open source project and if you are able to, consider supporting our work through [donations]({{< ref "/funding/donate.md" >}}), [sustaining memberships]({{< ref "/funding/membership.md" >}}) or contributions to the code documentation, web site and so on.

**謝辞**

We would like to thank the developers, documenters, testers and all the many folks out there who volunteer their time and effort (or fund people to do so). From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

QGIS is supported by donors and sustaining members. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list]({{< ref "/funding/donate.md" >}}). If you would like to become an official sustaining member, please visit [our sustaining members page]({{< ref "/funding/membership.md" >}}) for details. Supporting QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts. A complete list of current sustaining members is provided below - our very great thank you to all of our supporters!

QGIS はフリーのソフトウェアです。利用する上で金銭を支払う義務はありません。実際、私たちは利用者の財政状況や社会的地位にかかわらず、より多くの人に QGIS を利用して欲しいと思っています。私たちは地理空間的な意思決定ツールによって人々が力を持つことが、全人類の社会をより良くすると信じています。

{{<table-of-contents >}}
## QGISバージョン3.2のスポンサー
A special thanks to all our [sustaining members, sponsors and donors]({{< ref "/funding/membership.md" >}}) for helping us to make this release possible!
## 一般情報
### 機能：新しいzip形式のプロジェクトファイル形式.qgzがデフォルトの形式になりました
QGZは3.0でオプションのフォーマットとして追加されました。このフォーマットをデフォルトのフォーマットとすることで、SVG、GPKG内のオフラインデータ、カラーランプ、プラグイン、スクリプトなどのリソースを埋め込むことができるコンテナにたどり着くことができます。

![image29](images/entries/15e0d291ccc9722a61ed5d2611d3ac4c0eef3685.png.400x300_q85_crop.webp)

This feature was developed by [OSLANDIA - Paul Blottiere](https://github.com/pblottiere)
### 機能：クエリビルダのフィールド値のフィルタリング
クエリビルダで新しい式フィルタを作成するときに、フィールド値のプレビューパネルをフィルタ処理できるようになりました。

![image30](images/entries/731d930d07ca6d35f6bff727ef94a6322fcf21d0.gif.400x300_q85_crop.webp)

This feature was developed by [Salvatore Larosa](https://github.com/slarosa)
### 機能：Ctrl-Shift-Tabによるフルスクリーンマップ
Ctrl-Tabの他に、Ctrl-Shift-Tabを使用して、マップを表示し、マップのみを表示するようになりました。ツールバーやボタンは表示されません（ウィンドウタイトルがなくても、F11と組み合わせて）。 Beamerまたは大画面でのフルスクリーンマップ投影に最適です。ズームとパンもまだできます！ （Mathieu Pellerinの作品に基づく）

![image31](images/entries/e05bfa8d423465a0ec6697fac1d21dfeee177aea.png.400x300_q85_crop.webp)

この機能はRichard Duivenvoordeによって開発されました
## ツール
### 機能：地図ツールを簡素化して地物をスムーズにできるようになりました
The Simplify Features map tool has been renamed to \"Simplify/Smooth Features\", and now supports interactive smoothing of features.

![image2](images/entries/eca7851f8710661b929a99722afd28707f5926b3.png.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能：追加オプション付き識別ツール
新しい改善で、ユーザーは、複数の地物を確認するために、[選択]に類似したツールを使用できるようになりました。

この機能は、レスターシャー州評議会とイーストハンプシャー地区協議会によって資金提供されました

This feature was developed by [Martin Dobias and Viktor Sklencar](https://www.lutraconsulting.co.uk)
### 機能：地図のノードの展開/折りたたみ状態も保存
各地図テーマは、どのレイヤー、グループ、凡例項目が展開されているかを記録します。地図テーマを選択すると、展開/折りたたみ状態がレイヤーツリーに適用されます。

![image3](images/entries/0cfc7d80448436d67a4b1e92773e66eda5900a57.PNG.400x300_q85_crop.webp)

This feature was funded by [Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) within ERIKUS project](https://www.arpa.piemonte.it/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk) and [Faunalia](https://www.faunalia.eu)
### Feature: Auto \"Zoom to Selection\" mode for new map views
新しい地図ビューを設定すると、現在の選択範囲に自動的にズームできます。この例のように異なる地図主題と組み合わせできます。

![image4](images/entries/17848d809ce5a999115619ace229b6f07dba272a.PNG.400x300_q85_crop.webp)

This feature was funded by [Technology One](https://www.technologyonecorp.com/)

This feature was developed by [Nathan Woodrow](https://nathanw.net/)
### 機能：地図作成ツールの簡略化のための簡略化方法の選択
This allows different techniques to be used for simplification in the interactive simplify map tool, including the more cartographically pleasing \"Visvalingam\" simplification algorithm.

![image5](images/entries/085ad891fdc2b416a89603a6962544d165f2cef1.PNG.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能：フォーム内の関連する地物へのズームを追加
関連するテーブルで1つ以上のレコードが選択されると、新しいボタンが地物属性のサブフォームに表示されます。ジオメトリがある場合、ボタンは地図をこれらの地物にズームします。

![image6](images/entries/697d671bf6227445e10f9c899c0740b4225c1e7f.PNG.400x300_q85_crop.webp)

この機能はJürgenFischerによって開発されました
### 機能：地物情報のデカルト座標での面積/長さ/周長
QGIS 3.2では、楕円体およびデカルトの両方で面積、長さ、および周長を、地物情報パネル内に別々に表示します。2つの異なる測定値を見ることで、不正確な射影または楕円体の選択に起因する領域または距離計算における潜在的な問題をよりよく理解できます。

![image7](images/entries/28e185f928be7d08fd2971828a1daed53c224394.png.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## 計算式
### 機能：新しい式の関数
- color_grayscale_average()
- color_mix_rgb()
- flip_coordinates()
- wedge_buffer()
- tapered_buffer()
- buffer_by_m()

新規変数：
- \@project_home
- \@project_author
- \@project_abstract
- \@project_creation_date
- \@project_identifier
- \@project_keywords

この機能はMathieu Pellerin, Nyall Dawsonによって開発されました
### 機能：より有用な式ビルダ
式ビルダーは、QGIS内で式を簡単に作成できるようになりました。
- ビルダーでは、式からの期待値の範囲を含むデータ定義値の説明が表示されるようになりました
- 現在の式でCtrl +クリックすると、その関数のヘルプが自動的に開きます
- 式のエラーのある部分に印が表示されるようになりました
- これは、式の解析から得られたエラーメッセージの完全なリストを示します

![image8](images/entries/a296b411a0950f6bbd9af3c3cffec90b509b6e78.png.400x300_q85_crop.webp)

This feature was funded by [Technology One](https://www.technologyonecorp.com/)

This feature was developed by [Nathan Woodrow](https://nathanw.net/)
## ユーザーインタフェース
### 機能：レイヤーパネル：フィルターされた地図レイヤーのインジケーター
The main window\'s layer tree view (ToC) gets support for indicators that are shown when a vector layer has a filter applied. This makes it easier for users to understand that they are looking at a subset of all data. Clicking the indicator\'s icon brings up query builder.

これはレイヤーとグループ名の隣のレイヤーツリービューに余分なアイコンを表示するためのミニフレームワークを追加します。ツールチップのテキストをインジケータに関連付けると、インジケータの追加のコンテキストを提供できます。さらに、ユーザーがインジケーターをクリックしてカスタムアクションを定義できるときに信号が発信されます。アイデアは、情報のさまざまなビットを微妙に報告するために、将来インジケータを使用できることです。たとえば、次のようになります。
- 無効なジオメトリを持つ地図レイヤー
- その場で再投影の例外を使用した地図レイヤー
- 地図レイヤーにデータソースがありません
- 無効なCRSを持つ地図レイヤー

![image9](images/entries/ff2206aa7147ca68357ea4e3a1354bc231fb49cc.png.400x300_q85_crop.webp)

This feature was funded by [Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) within ERIKUS project](https://www.arpa.piemonte.it/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk) and [Faunalia](https://www.faunalia.eu)
### 機能：ロケータフィルタのプリフィックスをカスタマイズできるようにする
Prefixes of locator filters can now be customized under the application settings in the \"Locator\" tab

![image10](images/entries/d45b0ff62c8013eed8171c3bc42c9cdacc7dac10.png.400x300_q85_crop.webp)

This feature was funded by [QGIS User Group Switzerland](https://qgis.ch)

この機能は [Denis Rouzaud, OPENGIS.ch](https://opengis.ch) によって開発されました
### 機能：HTTP（S）、FTP、またはクラウドサービスに格納されたベクターとラスターのオープン
In 3.2, the data source manager\'s vector and raster panels have been updated to simplify opening of vector and raster datasets stored on HTTP(S), FTP, or cloud services. Basic HTTP(S) authentication support included.

![image11](images/entries/06e06201fb4db385ae14d6932353ce0b0b035e83.jpg.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### 機能：ロケータ検索バーの高速計算機
QGIS 3.2 allows evaluation of simple expressions (well, actually ANY QGIS expression\... so you could use aggregates and the like if you really wanted!) by entering \"= \" followed by an expression into the locator bar. If a valid expression is entered, users are given an option to copy the result to the clipboard.

E.g. entering \"= 10/3\" shows a locator entry \"Copy \'3.3333333\' to clipboard\".

![image12](images/entries/873ea8846c5f2f2cea56e8d4602bb41ac0567d7d.png.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能：パネルを切り替えるためのショートカット
Ctrl + {いいえ}ショートカット

This feature was funded by [Technology One](https://www.technologyonecorp.com/)

This feature was developed by [Nathan Woodrow](https://nathanw.net/)
### 機能：ロケータでのブックマーク検索
空間的なブックマークを検索できます。検索結果をダブルクリックすると、ブックマークが拡大表示されます。

Short video: <https://www.youtube.com/watch?v=ymW4TU8QWy4>

The new filter presents itself with a prefix of \"b\" and with tr( \"Spatial bookmarks\" ) as displayname.

この機能はKlavsPihlkjærによって開発されました
### 機能：プロジェクトのアクションを閉じるおよび元に戻す
Two new actions have been added to the \"Project\" menu
- \"Close\": Closes the active project, returning the QGIS window to the \"Recent Projects\" list
- \"Revert\": Restores the active project to the last saved state, discarding all unsaved changes

![image13](images/entries/3801ee06f51aa6517fd1c4a5de5eafffd4114f71.png.400x300_q85_crop.webp)

この機能はNathan Woodrow, Nyall Dawsonによって開発されました
### 機能：タイトルバーの未保存の変更インジケータ
QGIS 3.2 now follows the standard UI approach of indicating that the current project has unsaved changes by adding a \"\*\" prefix to the project name in the application title bar. This makes it easy to see if you have unsaved changes at a single glance!

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能：設定可能な地図のヒントの遅延
この機能はjduggeによって開発されました
### 機能：レイヤーまたはグループをレイヤーパネルの最上部に移動する
選択したレイヤーまたはグループをレイヤーパネルの上部に移動します。

この機能はMie Winstrupによって開発されました
### 機能：統計情報パネルのコンテンツをクリップボードにコピーボタン
It is now possible to copy the statistics panel\'s output table into the clipboard.

![image14](images/entries/0d1f4be90052251c05a1fc351dd099aaa92c65f7.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### 機能：ロケータからの検索設定、オプション、およびプロジェクトのプロパティページ
Short video: <https://www.youtube.com/watch?v=duB2YekUmV0>

The new filter presents itself with a prefix of \"s\" and with tr( \"Settings\" ) as displayname.

この機能はKlavsPihlkjærによって開発されました
### 機能：埋め込みレイヤーとグループのインジケーター
Embedded project layers and groups are now flagged by a handy \"embedded\" indicator, making it immediately clear to users which layers and groups have been embedded inside a project.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## シンボロジ
### 機能：新しいレイヤーのためのより良い色
The \"random\" colors assigned to new map layers are no longer \"random\" but instead randomly selected from a preset palette of \"visually pleasing\" colors. Say goodbye to ugly baby puke green layers!

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## レンダリング
### 機能：地図の著作権表示の改良
- 著作権テキストの表現のサポート。
- 影、輪郭、背景などのテキスト書式のオプションが改善されました。

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### 機能：メインウィンドウのスケールバーのフォントサイズとファミリをカスタマイズできます
This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### 機能：北矢印の装飾のカスタムSVGパスとサイズ
This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
## データ管理
### 機能：マテリアライズド・ビューを更新する
ブラウザから、マテリアライズド・ビューを右クリックすると、それを更新できるようになりました。

![image15](images/entries/125ee6837700d992fb8b6452ab1b346ba96c5cce.png.400x300_q85_crop.webp)

This feature was developed by [Etienne Trimaille](https://github.com/Gustry)
### 機能：オフライン編集のZおよびMサポート
オフライン編集では、Z座標とM座標のレイヤーもサポートされるようになりました。

This feature was funded by [Oester Messtechnik](https://messtechnik.ch/)

This feature was developed by [Matthias Kuhn, OPENGIS.ch](https://opengis.ch)
### 機能：QGISプロジェクトのメタデータ
QGIS 3.0で開始されたメタデータの作業を続けると、3.2ではQGISプロジェクトのメタデータがサポートされるようになりました。これにより、抄録、キーワード、連絡先の詳細、リンクなど、プロジェクトのプロパティに詳細なメタデータを設定できます。

![image16](images/entries/eb1394b46bf05e8a9b6be480cac4382c2f22a865.png.400x300_q85_crop.webp)

この機能は、ERIKUSプロジェクト内のArpa Piemonte（地質災害学科）によって資金提供されました

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com) and [Faunalia](https://www.faunalia.eu)
## フォームとウィジェット
### 機能：複数選択の値のリレーションウィジェットの複数列レイアウト
複数選択が可能な値のリレーションウィジェットは、複数の列に対応するようになりました。これにより、水平方向の画面スペースをより有効に使用できます。

![image17](images/entries/5fb9e551ed835b45161f3a2e9a94320dc50d5b97.gif.400x300_q85_crop.webp)

This feature was funded by [Grundbuch- und Vermessungsamt des Kanton Zug](https://www.zg.ch/behoerden/direktion-des-innern/grundbuch-und-vermessungsamt/gis-fachstelle)

This feature was developed by [David Signer, OPENGIS.ch](https://opengis.ch)
### 機能：カスタム属性フォーム（UIファイル）にURLを使用できるようにする
UIファイルは、最初の使用時にすべてのセッションでダウンロードされます。これにより、更新されたUIファイルをクライアントに容易に配布することが可能になる。

This feature was funded by [SIRS](http://www.sirs-fr.com)

この機能は [Denis Rouzaud, OPENGIS.ch](https://opengis.ch) によって開発されました
### 機能：ドリルダウン（カスケード）フォーム
QGIS 3.2 introduces drill-down (cascading) form support, where the values available in one field depend on the values of other fields. This feature allows users to create "value-relation" expressions based on the current value of another field in the same form. When the user modifies a field's value, the choices available in all related fields are filtered to match the new value -- allowing a hierarchical filtering strategy (drill-down, or cascading) inside a form.

![image18](images/entries/5990ff168d5b6b41176de4fa487964b97c32fafc.gif.400x300_q85_crop.webp)

この機能は、Grant Boxer、NaturalGIS、TudorBărăscu、NotioGIS、Républiqueet Canton deNeuchâtel、Arpa Piemonte、Nelson Silva、QGISデンマークユーザーグループ、Bo Victor ThomsenとLene Fischer、North River Geographicによって資金提供されました

This feature was developed by [Alessandro Pasotti (North Road)](https://north-road.com)
## レイヤ凡例
### 機能：ベクターレイヤーのシンボルの上にオプションのテキスト
この機能により、ユーザーは凡例のシンボルに余分な情報を追加できます。

![image19](images/entries/2e1e6a3c4b154c35642096a4c2235c2b2d706200.png.400x300_q85_crop.webp)

This feature was funded by [Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) within ERIKUS project](https://www.arpa.piemonte.it/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk) and [Faunalia](https://www.faunalia.eu)
### 機能：QGISプロジェクトから別のグループ/レイヤーにコピー＆ペーストします。
プロジェクトやプロファイル間でグループやレイヤーをコピー＆ペーストできます。

This feature was developed by [Salvatore Larosa](https://github.com/slarosa)
## マップコンポーザー
### 機能：属性テーブル項目のデータ定義テーブルソース
When an attribute table is set to a \"Layer features\" source, this new feature allows the underlying vector layer from which to source features to be data defined.

既存のテーブル属性（列設定）はすべてそのまま残されているため、データ定義テーブルを異なるフィールドを持つレイヤーに設定すると、テーブルに空の列が作成されます。

This feature was funded by [Kartoza/InaSAFE](http://kartoza.com/en/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能：レイアウトエクスポートに埋め込まれたプロジェクトメタデータ
SVG、PDF、または画像に印刷レイアウトを保存すると、作成されたファイルにプロジェクトメタデータが埋め込まれます。異なるメタデータ要素のサポートは、個々のエクスポート形式によって異なります。

この機能は、ERIKUSプロジェクト内のArpa Piemonte（地質災害学科）によって資金提供されました

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能：スケールバーテキストの書式の改善
QGIS 3.2では、バッファ、シャドウ、背景のようなスケールバーのテキスト内で、あらゆる種類のテキスト書式設定オプションを使用できます。

読めないスケールバーのテキストは過去のものです！

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## プロセシング
### Feature: Improved \'Join by attribute table\' algorithm
The \'Join by attribute table\' algorithm has been upgraded to support one-to-many joins (i.e. create separate features for each matching feature) as well as an option to discard records which could not be joined. Additionally, an optional prefix for joined fields can now be specified.

![image20](images/entries/93dd2a52ae3ed2b7a3842f6379d033fabc7932fe.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin, Nyall Dawson](http://www.imhere-asia.com/)
### 機能：テンプレートからスクリプトを読み込む
カスタムテンプレートから処理スクリプトを読み込むための新しいオプション

![image21](images/entries/fce801da5d7b82a1038f19d603d64046e6a399a0.gif.400x300_q85_crop.webp)

This feature was developed by [Matteo Ghetta (Faunalia)](http://www.faunalia.eu/)
### 機能：モデルを処理するための地物フィルタアルゴリズム
処理モデラー用の新しい地物フィルタアルゴリズムを追加します。式に基づいてソースの地物をフィルタリングし、一致する地物を最終出力として別の出力に送信したり、後で処理するために異なるアルゴリズムパイプラインを送信したりできます。

Read this [blog post for more information](http://www.opengis.ch/2018/05/28/how-to-filter-features-in-qgis-using-the-graphical-processing-modeler/).

![image22](images/entries/3b1e5e0d5b1874d2e3f0cbb8070eb82dedd89a4e.png.400x300_q85_crop.webp)

This feature was funded by [QGIS User Group Switzerland](https://qgis.ch)

This feature was developed by [Matthias Kuhn, OPENGIS.ch](https://opengis.ch)
### 機能：ゾーンヒストグラム
この新しいアルゴリズムは、ポリゴンとして定義されたゾーン内に含まれるラスターレイヤーからの各固有値のカウントを表すフィールドを追加します。

![image23](images/entries/577c3ed7ed7875d51e968a135bfd532f97d692c8.jpg.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### 機能：結び、差分および交わりのアルゴリズムをC ++へと移植
QGISネイティブのジオプロセシングアルゴリズムは、PythonからC ++に移植されました。このアップデートで、パフォーマンスの向上に加えて、いくつかのバグが修正されました。

This feature was funded by [InaSAFE DFAT](https://www.dfat.gov.au/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk)
### Feature: \'Project points (cartesian)\' algorithm
この新しい処理アルゴリズムは、指定された距離と方位（方位角）だけ入力点レイヤーからのポイントを投影します。フィールド値や式から距離と方位を取ることができるように、距離と方位の動的パラメータをサポートしています。

This feature was funded by [Nyall Dawson (North Road)](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能：より多くのアルゴリズムに対する動的パラメータ値
QGIS 3.2 extends the work begun in 3.0 to allow \"dynamic\" parameters for selected Processing algorithms. Dynamic parameters allow users to use expressions or field values to specify the value of a parameter while the algorithm executes, so e.g. the buffer size can be dynamically calculated for each individual feature buffered.

3.2では、次のアルゴリズムが動的パラメータをサポートするようになりました。
- 穴を削除する
- 重複する頂点を削除する
- 簡略化する
- スムース
- グリッドにスナップ
- 細分化
- トランセクト
- 翻訳

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能：マルチリングバッファ（一定距離）アルゴリズム
This new algorithm computes multi-ring (\'donuts\') buffer for all the features in an input layer, using a fixed or dynamic distance and rings number.

この機能は Alex Bruy によって開発されました
### Feature: New \"segmentize\" algorithms
QGIS 3.2では、カーブしたジオメトリをセグメント化するための2つの新しいアルゴリズムがプロセシングに追加されました。

\"Segmentize by maximum distance\": The segmentization is performed by specifying the maximum allowed offset distance between the original curve and the segmentized representation.

\"Segmentize by maximum angle\": The segmentization is performed by specifying the maximum allowed radius angle between vertices on the straightened geometry (e.g the angle of the arc created from the original arc center to consective output vertices on the linearized geometry).

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能：すべてのポリゴンパーツにポイントを作成するオプション
The \"Centroid\" and \"Point on surface\" algorithms have a new option to create points for every individual part of input geometries.

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### 機能：地物回転アルゴリズム
This new algorithm allows rotation of features by a set angle. The rotation can occur around a preset point or each individual feature\'s centroid.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Line sinuosity in \"Add Geometry Attributes\"
The \"Add Geometry Attributes\" algorithm now calculates line sinuosity and straight distance for line layers.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能：ジオタグ付きの写真をインポートする
In QGIS 3.2 a new \"Import geotagged photos\" algorithm has been added to Processing. It allows selection of a folder which it will scan for jpg files which have been geotagged and creates a PointZ layer with the result, with attributes for photo path, altitude, direction and timestamp.

必要に応じてスキャンを再帰的に行うことができ、読み込めなかったジオタグや欠落していた写真のオプションテーブルを作成することもできます。

このアルゴリズムは、外部リソースウィジェットを使用してリンクされた写真を属性フォームに表示するように出力テーブルを自動的に設定します。

![image24](images/entries/399ace1f3d437044b9fb478afb820372195b79d8.png.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能：x / y座標値入れ替えアルゴリズム
このアルゴリズムは、入力ジオメトリのX座標値とY座標値を入れ替えます。誤って緯度と経度の値を逆にしたジオメトリを修復するために使用できます。

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Sort order option for \"Add Incremental Field\"
この変更により、オプションで、増加フィールドの追加アルゴリズムで値を割り当てるときに使用するソート順を設定できます。以前は、元の地物順序を使用して常に値が追加されていました。この変更により、ユーザーは地物に値が割り当てられる順序を制御できます。

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能：距離パラメータユニットのインジケータ
When an algorithm uses a \"distance\" type parameter, the units will now be shown next to the parameter. This avoids the confusion when running algorithms which use distances where the unit depends on a layer or CRS parameter - e.g. the distance parameter in the buffer algorithm gives the distance in layer units\... so now in QGIS 3.2 we show those units directly within the dialog. Hopefully this leads to less user confusion and accidental \"1000 degree buffers\"!

さらに、単位が度の場合、パラメータの隣に小さな警告アイコンが表示されます。このアイコンのヒントは、ユーザーがデータを適切な投影ローカル座標系に再投影するように指示します。

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能：アルゴリズムのログを保存/クリア/コピーすることができます
アルゴリズム実行ダイアログでは、現在のログを（テキストまたはHTMLファイルに）保存し、ログの内容をクリップボードにコピーし、ログをクリアするための新しいボタンが追加されました。

この機能は、SMEC/SJによって資金提供されました

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能：ウェッジバッファアルゴリズム
この新しいアルゴリズムは、入力点からくさび形のバッファを作成します。

方位角パラメータは、ウェッジの中央が指す角度（度）を示します。バッファ幅（度）はwidthパラメータで指定します。ウェッジは、方位角方向のいずれかの角度幅の半分に伸びることに注意してください。バッファの外側半径は外側半径で指定され、オプションで内側半径も指定できます。

このアルゴリズムは、方位角、幅、および半径の動的パラメータをサポートしています。

このアルゴリズムのネイティブ出力はCurvePolygonジオメトリですが、これらは出力フォーマットに応じて自動的にポリゴンにセグメント化できます。

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能：可変幅バッファ
新しい処理アルゴリズムが追加され、テーパーバッファ（指定された開始および終了直径を持つ）およびラインストリングm値からの可変幅バッファを含む可変幅バッファが作成されました。

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能：ラスターアルゴリズムを再分類する
2つの新しいQGISラスター再分類アルゴリズムがプロセッシングに追加されました。これらは使いやすく、しかも高速かつ安定していて、QGISでサポートされている任意のラスターレイヤータイプに対応しています！
- レイヤーごとに再分類する：ベクターテーブルから最小/最大/値フィールドで指定された範囲を使用してラスターを再分類する
- テーブルによって再分類する：アルゴリズムダイアログでユーザーが入力した固定テーブルを使用してラスターを再分類する

この機能は、SMEC/SJによって資金提供されました

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能：単一レイヤーのユニオンアルゴリズム
The union algorithm can be now run with just a single input layer in order to resolve any overlaps among the layer\'s features. For example, if an area is covered by three features, that area will be cut out from those features and three new features will be added, copying attributes of the original features.

![image25](images/entries/a32fa9ccc63bd3f91e6696ee8f9aef32f61b4691.png.400x300_q85_crop.webp)

This feature was funded by [InaSAFE DFAT](https://www.dfat.gov.au/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
## アプリケーションとプロジェクトのオプション
### 機能：プロジェクトの必須レイヤー
必須レイヤーはプロジェクトから削除することはできません。これにより、不要と考えるレイヤーを削除することからプロジェクトユーザーを保護するための安全性がさらに高まります（たとえば、結合、関係、式で使用されます）。

![image26](images/entries/b65c47d1a41ab4a7ad545696b4985ebd7edb9f75.png.400x300_q85_crop.webp)

This feature was funded by [Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) within ERIKUS project](https://www.arpa.piemonte.it/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk) and [Faunalia](https://www.faunalia.eu)
### 機能：PostgreSQLデータベースでのプロジェクトの保存と読み込み
Users can now save their projects within a PostgreSQL database. Project can be saved in menu **Projects \> Save To \> PostgreSQL** and loaded using menu **Projects \> Load From \> PostgreSQL**. Projects saved in database can be loaded also through the browser dock (projects show up under the schema where they were saved, together with other layers).

Saving/loading QGIS projects must be explicitly enabled in PostgreSQL connection settings: there is a new option \"Allow saving/loading QGIS projects in the database\" which is disabled by default.

New API has been introduced that allows creation of custom project storage implementations (may be used by plugins). Related QEP: <https://github.com/qgis/QGIS-Enhancement-Proposals/issues/118>

This feature was funded by [Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) within ERIKUS project](https://www.arpa.piemonte.it/)

This feature was developed by [Martin Dobias, Peter Petrik (Lutra Consulting)](https://www.lutraconsulting.co.uk) and [Faunalia](https://www.faunalia.eu)
## ブラウザ
### 機能：XYZタイルの接続を保存/読み込みする
ブラウザパネルから、XYZタイルのエントリをXMLファイルにエクスポート/インポートすることができます。

![image27](images/entries/678a1f4686de353f4a04fc83877e27c18d2fca7d.png.400x300_q85_crop.webp)

This feature was developed by [Salvatore Larosa](https://github.com/slarosa)
### 機能：プロジェクトのホームパスを手動で設定できます
This new feature in QGIS 3.2 allows the project home path (which is used by the browser to create the \'Project Home\' item) to be set by users for a project, instead of always matching the location where the project is saved.

This allows users to set the project home to a folder which contains data and other content, and is especially useful for organisations where QGIS projects are not stored in the root folder of a organisational \'project\'.

プロジェクトのホームパスを相対パスに設定することもできます。この場合、プロジェクトの保存場所との相対パスになります。

The path can be set through the Project Properties dialog, or by right-clicking on the Project Home browser item and selecting \'Set Project Home\'.

![image28](images/entries/db297eb148a7d62dd58aab40dca32ee91d148831.png.400x300_q85_crop.webp)

この機能は、SMEC/SJによって資金提供されました

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## データプロバイダ
### 機能：メッシュレイヤーのサポート
ラスターおよびベクターレイヤーに加えて、構造化または非構造化メッシュ（グリッド）上のデータの表示をサポートするメッシュレイヤーを導入するための初期の作業が行われました。これはまだ進行中の作業であり、QGIS 3.4で完全に準備が整う予定です。これまでの作業では、さまざまな形式のメッシュベースのデータを処理するための新しいライブラリMDALが作成され、新しいAPIが導入されましたが、ユーザーインターフェイスはまだ実装されていません。

詳細については、以下を参照してください。

<https://github.com/qgis/QGIS-Enhancement-Proposals/issues/119>

and

<https://github.com/lutraconsulting/MDAL>

![image32](images/entries/91c7bf725bc4afecc9efbeaedc8e98ad153b73b4.png.400x300_q85_crop.webp)

This feature was developed by [Peter Petrik and Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk)
### 機能：ArcGIS Feature Serverレイヤーのレイヤーのデフォルトスタイルを自動的に設定する
Feature ServerのレイヤーがQGIS 3.2にロードされると、レイヤーがArcGISにロードされたときのレイヤーの外観に合わせて、サーバー上のそのレイヤーに指定されているのと同じスタイルが自動的に適用されます。

この機能は、SMEC/SJによって資金提供されました

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能：Oracleのクエリの高速化
地物の大文字と小文字を区別しない値の一致など、Oracleのレイヤーでは、特定の操作が大幅に高速化されます。

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能：プリセットされたスキーマへのOracleデータベース接続のテーブル・リストを制限する
この変更により、Oracleデータベース接続の接続プロパティにスキーマを設定できます。設定されている場合、そのスキーマ内のテーブルのみがスキャンされ、接続用にリストされます。

Previously the option existed to restrict the scan to tables which belong to the user, but this option does not support the use case where a connection must access tables from a different user, and the default \"scan everything\" setting is too expensive (since it often takes multiple minutes to perform, especially when geometryless tables are shown).

This feature was funded by [Open Spatial](http://www.openspatial.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能：カーブしたOracleジオメトリの読み取り専用サポート
以前は、これらのジオメトリは黙って破棄されました。

This feature was funded by [Open Spatial](http://www.openspatial.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## プラグイン
### 機能：DBマネージャにクエリ履歴を追加する
3.2では、SQLクエリを格納することができます。クエリ履歴は、DBマネージャプラグインの[SQLウィンドウ]タブで使用できます。

![image33](images/entries/9c6074aaf1e989c460833535788d0b396a677e34.png.400x300_q85_crop.webp)

This feature was developed by [Salvatore Larosa](https://github.com/slarosa)
### 機能：バックグラウンドでのDBマネージャSQL実行
この機能はPaul Blottiereによって開発されました
## 三次元機能
### 機能：3Dポリゴン：オプションで背面を生成
3Dポリゴンを持つデータセットでは、頂点の順序が一貫していない（時計回りと反時計回り）場合があり、3Dビューで最適な結果が得られない場合があります。背面のカリングを有効にするとポリゴン（壁）裏面のカリングが無効になっていると、一部のポリゴンが正しく陰影付けされません。新しいオプション **バック面を追加** を有効にすると、テッセラは両方向（前面と背面）に三角形を生成し、そのようなデータセットのレンダリング品質を大幅に改善します。

The only downside when using this option is that more graphical memory is used (double amount of vertex data). Make sure to set culling mode to \"Back\" when using this option, otherwise there would be no visible difference as the scene would still render polygons with incorrect shading.

この画像には自由に利用可能なプラハ3D建物のデータセットが含まれています。

![image34](images/entries/875e423e7a857a509812da6f46d468486fb7fd99.png.400x300_q85_crop.webp)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)

{{<content-end >}}
