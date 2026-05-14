---
HasBanner: false
draft: false
releaseDate: '2015-02-20'
section: project
sidebar: true
title: QGIS 2.8の変更履歴
type: visual-changelog

---
{{<content-start >}}
# QGIS 2.8の変更履歴{#changelog28 }
リリース日: 2015-02-20

This is the change log for the next release of QGIS - version 2.8 \' Wien\'. Wien is German for \'Vienna\' - host city to our developer meet up in November 2009 and again in March 2014.

**長期サポート**

This is a special release since it is designated an \'LTR\' (Long Term Release). LTR releases will be supported with backported bug fixes for one year, and will be in permanent feature freeze (i.e. no new features will be added, only bug fixes and trivial updates).

LTRリリースの目的は、1年に1回以上、ユーザースキルの更新、教材のトレーニングなどに対処したくない企業や組織に対して、安定した頻繁に変化するプラットフォームを提供することです。LTRの成功は、あなたのご愛顧いただいているユーザーにとって非常に重要です。バグ修正に資金を援助し、サポートプロバイダーとのサポート契約であなたのために行われたバグ修正がLTR支店私たちの通常の開発ブランチだけでなく、

LTRが重要な場合は、QGISプロジェクトを直接サポートすることも検討してください。また、LTRをエンタープライズソリューションの基盤として使用することを商用プロバイダに推奨し、安定したプラットフォームを継続的に改善し、洗練されたメリットを享受してください。フロンティアに住むことを望むユーザーや組織にとって、定期的な4つの月間リリースは引き続き控えています。

**新機能**

QGIS 2.8は、最も人気のあるフリーデスクトップGISをよりいっそう多くの機能が充実して役立つようにするために、非常に多くの新機能、改良、改良が含まれているため、特別リリースです。

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

**謝辞**

私たちは、開発者、ドキュメント作成者、テスター、そして時間と労力をボランティアしている（あるいは人々に資金を提供する）多くの人々に感謝したいと思います。

From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

最後に、このプロジェクトに提供した貴重な財政支援について、公式スポンサーに感謝したい。
- **GOLD Sponsor: Asia Air Survey, Japan** <http://www.asiaairsurvey.com/>
- SILVER Sponsor: [Sourcepole AG, Switzerland](http://www.sourcepole.com/)
- SILVER Sponsor: [State of Vorarlberg, Austria](http://www.vorarlberg.at/)
- SILVER Sponsor: [Office of Public Works, Ireland, Ireland](http://www.opw.ie/)
- BRONZE Sponsor: [GIS3W, Italy](http://www.gis3w.it/)
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
- BRONZE Sponsor: [Faculty of Geology, Geophysics and Environmental Protection, AGH, ​University of Science and Technology, Poland](http://www.wggios.agh.edu.pl/en)

A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become an official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts.

If you enjoy using QGIS, please consider making a donation to support the project - either [financial](https://qgis.org/en/site/getinvolved/donations.html) or of [your time and skills](https://qgis.org/en/site/getinvolved/index.html)! Lastly we would like to also take a moment to encourage you to fund a [special campaign](http://blog.vitu.ch/10102014-1046/crowdfunding-initiative-automated-testing) by one of our QGIS developers to get a working test suite for QGIS so that we can improve out quality assurance process and deliver you the best possible releases.

QGIS はフリーのソフトウェアです。利用する上で金銭を支払う義務はありません。実際、私たちは利用者の財政状況や社会的地位にかかわらず、より多くの人に QGIS を利用して欲しいと思っています。私たちは地理空間的な意思決定ツールによって人々が力を持つことが、全人類の社会をより良くすると信じています。

{{<table-of-contents >}}
## 一般情報
### 機能:式をスピンボックスで入力する
When editing attributes in the **attribute table or forms**, you can now enter expressions directly into spin boxes, e.g. `5 * 2.5` and they will be automatically evaluated.

![](images/entries/e094287244ee1fe161c8ca95951c2d11ca1e6cdd.webp)
### 機能：ブックマークのインポート/エクスポートが可能
ブックマークをファイルに保存/読み込むことが可能になりました。これにより、ブックマークされた場所を簡単に共有したり、コンピュータ間で簡単に移動することができます。

**この機能は、によって開発されました：** Salvatore Larosa

![](images/entries/e3d35c32da659821bc0c657b8e7ba40587a1bfb2.webp)
### 機能：式の改良
- **Integer division produces a double when required**: Previously dividing two integers in an expression would always result in an integer value, i.e. `5 / 2 = 2`. Now the result will always be double when required, so `5 / 2 = 2.5`, which is much more expected for users. A new integer divide operator - `//` has been added to mimic the old behaviour, i.e. `5 // 2 = 2`.
- **New \'if()\' function**: There is now a new `if(cond, true, false)` expression
- **表現の遅延評価**
- **Added get and transform geometry**: These new keywords can be used with `getFeature` for some geometry tests like intersects, crosses, contains, etc.
- `geometry` - returns the feature\'s geometry
- `transform` - returns the transformed geometry

![](images/entries/ec56f9b8331e619ad1a44970fde655b68125f9d8.webp)
### 機能：継続的なテストフレームワークとQAの改善
In our ongoing quest to improve the stability and quality of QGIS, every commit is now tested against a growing test suite to identify regressions automatically. In the image on the right you can see the list of incoming pull requests on our GitHub page are now automatically annotated with a check or cross based on whether our test suite successfully ran on [Travis.ci](https://travis-ci.org/qgis/QGIS) when the pull request is made or updated.

また、QGISコードベースのCoverityスキャンも定期的に行っています。その結果、メモリリークや潜在的なクラッシュなど、1000を超えるフラグ付きの問題を特定して修正しました。QGISの欠陥密度は0.01であり、同様のサイズのプログラムの平均は約1.0である。

![](images/entries/4ec86080ff150743f1bdc88d3ac7881a6cd405de.webp)
## 解析ツール
### 機能：計測ダイアログの改善
測定ツールが改良され、測定ダイアログで使用する単位を選択できるようになりました。ダイアログには、測定計算中にどの設定が使用されているかを示す新しい情報セクションもあります。

![](images/entries/67a001d3d800feec8805de698ed364e91d00daab.webp)
## ブラウザ
### よりレスポンシブなブラウザ
In the QGIS Browser items are now expanded in their own threads, speeding up the load time of the browser and making the browser more responsive. Navigating PostGIS sources is now much faster in the browser. The animated snapshot to the right (click image to see the animation) shows the loading of two slow WMS servers in parallel . The browser\'s state (tree expansion) is restored on startup.

** この機能は次の方によって開発されました:** Radim Blazek

![](images/entries/c8df646572084b8f12027fd54c1210f14c80c8e1.gif)
## データプロバイダ
### 機能：コンテキストによるWMS凡例グラフィックのサポート
If your WMS server supports contextual legends, you can make use of them in QGIS now too. Contextual legends are getLegendGraphic requests which return only the relevant legend for your current view extent, and thus do not include legend items for things you can\'t see in the current map.

**This feature was funded by:** [Regione Toscana](http://www.regione.toscana.it/)

**This feature was developed by:** [Faunalia](http://www.faunalia.eu/)

![](images/entries/e516a25492b547113c487d00475cfe07bc7b131e.webp)
## データマネジメント
### 機能：結合のカスタム接頭辞
レイヤプロパティダイアログの結合マネージャでカスタムプレフィックスを定義できるようになりました。 接頭辞を使用する場合、属性表inには、優先接頭辞と結合された属性名が表示されます。

![](images/entries/372e6561a4db3ed3ca3d418c946f81bce0d0d134.webp)
### 機能：一時的なメモリレイヤの作成をサポート
This release add support for creating new temporary scratch layers within QGIS core. Scratch layers can be created in the `Layer --> Create layer --> New Temporary Scratch Layer` menu option.

![](images/entries/bddbbd6cb55e9a19441ea564275dd480661e61de.webp)
### 機能：選択した行の計算をサポート
アトリビュートテーブルでは、フィールドの電卓バーに追加された新しいボタンのおかげで、選択した行の計算を行うことができます。

![](images/entries/1b7ead001901ed4242d26556abac055834e367b2.webp)
## デジタイズ
### 機能:高度なデジタイズツール
QGISでラインを正確に平行または直角にデジタル化したり、ラインを特定の角度にロックしたりしたいと思ったことがありましたら、今すぐ可能です。高度なデジタイジングツールはCADinputプラグインのポートであり、新しいパネルをQGISに追加します。新しいジオメトリまたはジオメトリパーツをキャプチャするときにパネルがアクティブになります

![](images/entries/50f726e5899eb72dcec76e4bed1936bcf957e75f.webp)
### 機能：改良されたツールの簡略化
シンプル化ツールは次のように改良されました。
- OTFの再投影サポート
- ユーザーは正確な許容値を指定することができます（非センスの相対値だけでなく）
- tolerance can be specified either in map units or layer units or pixels
- 許容値の設定が設定のなかにできました
- 一度に複数の地物を単純化する（クリックするだけではなく四角形をドラッグする）
- マルチパート機能のサポート
- 頂点数減少についての統計

**This feature was funded by:** [Tracks for Africa](http://tracks4africa.com/)

**This feature was developed by:** [Lutra Consulting](http://www.lutraconsulting.co.uk/) in cooperation with [Kartoza](http://kartoza.com/)

![](images/entries/20b7f96ffc7d37b8c2ae09189d7957a929a716e5.webp)
### Feature: Snapping improvements
There is a new snapping mode : **snap to all layers** which makes it quick to enable snapping between all layers. Also the underlying snapping architecture of QGIS has been overhauled making snapping much faster on large projects and improving the precision with which snapping takes place. ​There's also less confusion with snapping tolerances being to map units or layer units, so those anticipated 1 metre tolerances don't become 1 degree tolerances without you knowing.

**This feature was funded by:** [Ville de Vevey, SITNyon](http://www.vevey.ch/) and [QGIS Usergroup Switzerland](http://www.qgis.ch/)

**This feature was developed by:** [Lutra Consulting](http://www.lutraconsulting.co.uk/)

![](images/entries/8454af2743154585eb82325ab2694e50e7d9efcd.webp)
## レイヤ凡例
### Feature: Show rule-based renderer\'s legend as a tree
Advanced users who leverage QGIS\'s rule based renderer system will be pleased to see that the rules are now presented as a tree in the legend. Better still, each node in the **tree** can be **toggled on/off** individually providing for great flexibility in which sublayers get rendered in your map.

**This feature was funded by:** [SIGE](http://www.sige.ch/)

**This feature was developed by:** [Lutra Consulting](http://www.lutraconsulting.co.uk/) in cooperation with [Kartoza](http://kartoza.com/)

![](images/entries/0d39448aa0893d7a71c5241aa2181750535e62c3.webp)
## マップコンポーザー
### 機能：コンポーザGUI の改善
- View menu option to **hide bounding boxes**. This allows users to hide the bounding boxes for selected items within a composition. It\'s a handy feature for allowing interaction with items while previewing exactly how they will look when the composition is exported, without large boxes blocking the view.
- **コンポーザーのフルスクリーンモード**
- Option to **toggle display of panels** in composer, available by both the `view menu`, using the shortcut `F10` and by pressing `Tab` when the composer canvas is selected. It\'s useful for maximising the space when planning a map layout.

![](images/entries/10677c6e1612a4392e8bca0a9cbe31126426becf.webp)
### Feature: Grid improvements
コンポーザでは、フレームと注釈の表示をより細かく制御できます。以前は、回転されたマップまたは再投影されたグリッドの場合、コンポーザーはすべてのマップ側のすべての座標を描画していました。その結果、緯度/経度と経度/ x座標が混在していました。これで、すべての座標、緯度のみ、または各マップフレーム側の経度のみを制御することができます。同様のオプションが、マップグリッドフレームの分割方法を制御するために追加されました。

アノテーションの新しい垂直降順方向。この変更により、マップグリッド注釈の新しい降下垂直方向モードが追加されます。これまで、垂直注釈では昇順のテキストのみがサポートされていました。

![](images/entries/288d533cbed1f6beeef17004897060c8639bbbb4.webp)
### 機能：アイテムの余白にラベルを付ける
- ラベル**アイテムの水平と垂直の両方の余白を制御できるようになりました。これまでは、水平マージンと垂直マージンの両方に単一のマージン設定しか適用されませんでした。この変更により、ユーザーは異なる水平および垂直マージンを指定できます。
- You can now specify negative margins for label items, **allowing text to be drawn slightly outside of a label item\'s bounds**. This is desirable for aligning label items with other items while allowing for optical margin alignment for the label type.

![](images/entries/7f4905d74ca140ed369bea8866357b9d952ee212.webp)
## プラグイン
### 機能：Pythonコンソールの改善
You can now drag and drop python scripts into QGIS window and they will be executed automatically. We also added a toolbar icon to the plugins toolbar and a shortcut ( `Ctrl-Alt-P` ) for quick access to the python console.

![](images/entries/03be8f30ce341816bd3bcd1a58f3b913ddcea07c.webp)
## プロセシング
### 機能:新しい幾何的述語パラメータタイプ
**この新しいパラメータタイプを使用すると、場所で選択、場所で抽出**および**場所によって属性を結合する**アルゴリズムで、使用する空間演算子を正確に選択できます。

**This feature was funded by:** [French Ministry of Ecology, Sustainable Development and Energy](http://www.developpement-durable.gouv.fr/)

**This feature was developed by:** [Camptocamp](http://www.camptocamp.com)

![](images/entries/cd198b98cf28e611f5c2e3be93bc5ec90dd0a5b4.webp)
### 機能：新しいアルゴリズム
処理フレームワークには、いくつかの新しいアルゴリズムが追加されています。
- **レギュラーポイント**アルゴリズム（アドレス＃5953）
- **相違点**アルゴリズム（アドレス＃5953）
- **ベクトルスプリット**アルゴリズム（アドレス＃5953）
- **ベクタグリッド** アルゴリズム (addresses #5953)
- **ハイプロメトリック曲線**計算アルゴリズム
- **ラインを分割する**
- ** フィールドのリファクタ ** 属性操作アルゴリズム

![](images/entries/b2403fae20cd24cfb1883d24e97de6fc51e40c88.webp)
## プログラム可能
### 機能：式にコメント機能を追加する
Comments can now be added to expressions using an SQL style `--` prefix.

![](images/entries/e1579eec6d8ab74330fb2f784c68ed16c83bb79d.webp)
### 機能:カスタム式機能エディタ
You can now define custom expression functions in the expression widget. See [this blog post](http://nathanw.net/2015/01/19/function-editor-for-qgis-expressions/) for more details.

![](images/entries/503dd9dadec4fb85ee5ab6335e4f03979a8e7d77.webp)
### 機能:Qt5サポート
QGISはQt5ライブラリを使用して構築できます。現在、ほとんどのバイナリはデフォルトでQt4を使用しています。

![](images/entries/c702d89260cbab35323c052a15ab5c5728fc7115.webp)
### 機能:空間インデックスのバルクロード
APIでは、空間インデックスの一括読み込みのサポートが追加されました。これは空間インデックスを初期化するよりはるかに高速です。Pythonからは次のように簡単です：

`index = QgsSpatialIndex( layer.getFeatures() )`

メモリレイヤーに50Kポイントの簡単なテストから：

**bulk loading \~ 100 ms**

inserting features \~ 600 ms

索引ツリーは、理論的にもより良く構築されなければならず、より高速なルックアップをもたらす可能性がある。

![](images/entries/80cea18c68b7885cb71c1682ca3777caa048ff9e.webp)
### 機能: SQLクエリの選択した部分のみを実行する機能
In the DB Manager SQL editor, it is now possible to highlight a portion of the SQL and only that portion will be executed when you press `F5` or click the `run` button

![](images/entries/0d1343e84aa0946becab1e37880a58ceeffbd491.webp)
## QGISサーバー
### 機能:サーバpythonプラグイン
PythonプラグインによるQGISサーバーのサポートにより、Pythonのパワーがサーバー側にもたらされ、新しい機能の迅速かつ効率的な開発と展開が可能になります。

**This feature was developed by:** [Alessandro Pasotti (ItOpen)](http://www.itopen.it/)
### 機能: レイヤスタイルのサポート
- QGIS Serverは、GetMapリクエストで定義済みのレイヤースタイルをサポートするようになりました。
- QGIS ServerはGetStylesリクエストで複数のスタイルをサポートするようになりました（下記のシンボルセクションを参照）

### 機能：WMSにDescribeLayerメソッドを追加する
** WebマップサービスのStyled Layer Descriptorプロファイル：DescribeLayer **

<http://www.opengeospatial.org/standards/sld>

ユーザー定義のスタイルを定義するには、シンボル化されている地物、または少なくともその地物/カバレッジタイプに関する情報が必要です。ユーザー定義のスタイルは名前付きレイヤーに適用できるため、クライアントが名前付きレイヤーの地物/カバレッジタイプの情報を取得するためのメカニズムが必要です。これは、レイヤーとスタイルのWMSコンセプトと、地物タイプやカバレッジレイヤーなどのWFS / WCSコンセプトのギャップを埋める別の例です。これを可能にするために、WMSは任意に **DescribeLayer** 要求をサポートすることができる。

DescribeLayerメソッドは、WMS機能ドキュメントのオーバーロードよりも優れたアプローチと考えられています。`

それぞれの名前付きレイヤーについては、実際に機能データに基づいているかどうかを示す記述がなければならず、そうであればWFS / WCS（URLプレフィックス）と機能/カバレッジタイプを示す必要があります。この方法で名前付きレイヤーを記述できないことは完全に有効であることに注意してください。
## シンボロジ
### 機能：ラスター画像の塗りつぶしタイプ
この新しいシンボルレイヤータイプでは、ポリゴンを（タイル付きの）ラスター画像で塗りつぶすことができます。

オプションには、ファイル名、不透明度、画像サイズ（ピクセル単位、mm単位または地図単位）、座標モード（地物またはビュー）、回転など（データ定義済み）が含まれます。

![](images/entries/3c372b247f1f5583768532c2be96f169dcff1e8f.webp)
### Feature：ライブヒートマップレンダラー
新しいヒートマップベクターレイヤーレンダラーでは、ポイントレイヤのライブの動的ヒートマップが可能です。

オプションには、ヒートマップ半径（ピクセル単位）、mm単位またはマップ単位の指定、カラーランプの選択、フィールドごとの重み付けポイント、レンダリング速度と品質のトレードオフを選択するスライダが含まれます。

![](images/entries/a13862e4cf8707ec70ddb37a8e3e824db6af883d.webp)
### 機能：レイヤーごとに複数のスタイル
It is now possible to set multiple styles for a layer and then easily toggle between them. This functionality is available in the `legend context menu --> styles sub-menu` where it is possible to add/remove styles and quickly switch between them. Layer sets remember styles, and different styles can also be applied to individual composer map items. The multiple styles defined are also available when the project is served via QGIS Server as a WMS layer. For more information on this see also this [blog post](http://www.lutraconsulting.co.uk/blog/2015/02/19/towering-qgis-release/).

**This feature was funded by:** [Regione Toscana](http://www.regione.toscana.it/)

**This feature was developed by:** [Gis3W](http://www.gis3w.it/), [Lutra Consulting](http://www.lutraconsulting.co.uk/)

![](images/entries/e6d0058bbae51c52fb9fffc79d4cc459fbaf853b.webp)
### 機能：より多くのデータ定義シンボル設定
データ定義のシンボル設定のユーザインタフェースが改善されました。データ定義可能な各プロパティの横にデータ定義オプションを移動します（ラベルプロパティなどのQGISの他の部分に合わせて）。また、多くの新しい特性が記号のために定義可能なデータにされている。このユーザーインターフェイスの改善により、データ定義のオーバーライドが定義されているかどうか、およびデータ定義の設定へのアクセスが容易かどうかをすぐに確認することもできます。

![](images/entries/1af9b133ea80a4469e9be81107449b0e22df442b.webp)
### 機能: DXF エキスポート: マーカーシンボルエキスポートの改善
DXFファイルのエクスポータ機能が改善され、元のQGISシンボルにエクスポートされたマーカシンボルの忠実度が向上しました。
### 機能:キャンバスでの地図回転,コンポーザでの回転が改善されました
このリリースでは、マップキャンバスでの回転の予備的なサポートが含まれています。ステータスバーの新しい回転ウィジェットを使用してキャンバスを回転させることができます。ローテーションのサポートが地図作成者にも拡張され、ラベルや記号などを正しく処理できるようになりました。

**This feature was funded by:** [Japan Space Imaging Corporation (JSI)](http://www.spaceimaging.co.jp/)

**This feature was developed by:** [Faunalia](http://www.faunalia.eu/)

![](images/entries/b655549a3336c2fb16eef87f6f30fe50f5abe9f9.webp)
## ユーザーインタフェース
### 機能: 投影選択の改良/整合性
すべてのダイアログで一貫した投影選択ウィジェットが使用され、最近使用されたプロジェクト/標準プロジェクト/ QGIS投影から素早く選択できます。

![](images/entries/7a9b103d6b537f8fd6d2c53b81dc4f9a2e3f736c.webp)

.

{{<content-end >}}
