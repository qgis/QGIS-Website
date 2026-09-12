---
HasBanner: false
draft: false
releaseDate: '2015-10-23'
section: project
sidebar: true
title: QGIS 2.12の変更履歴
type: visual-changelog

---
{{<content-start >}}
# QGIS 2.12の変更履歴{#changelog212 }
![image1](images/projects/3648539707d0789903fdfedac3705584f12fa6ac.png)

リリース日: 2015-10-23

これはQGISの次のリリースの変更ログです。バージョン2.12.0「Lyon」 - デベロッパーミートアップ2012年4月のホスト都市

**QGIS 2.12 \'Lyon\' の新機能**

これは4カ月ごとのリリースシリーズの次のリリースです。 これは、私たちが取り組んできた新機能へのアクセスを提供し、QGIS開発の「最先端」を表しています。

QGISの「Lyon」には、素晴らしい新機能が満載されています。 特別なハイライトは、ルールベースのラベル付け、属性テーブルのルールベースのスタイリング、高度なジオメトリチェッカーのサポート、カーブベースのジオメトリのデジタイジング、認証管理の向上などです。 QGIS 2.12には、多くのバグ修正と処理されたメモリリークがあります。 QGIS 2.12で提供される機能は、次のLTRリリース（2016年にリリース予定）に含まれているため、このリリースを使用すると、次のLTRに移行する新しい機能をテストする素晴らしい機会が提供されます。

新しい機能がソフトウェアに追加されるたびに、新しいバグが発生する可能性があります。このリリースで問題が発生した場合は、 [QGISバグトラッカー](http://hub.qgis.org) にチケットを提出してください。 新しい機能をユーザーに展開することについてもっと慎重にしたい運用環境で作業している場合は、QGISのLTR（Long Term Release）バージョンも提供しています。 現在のLTRはバージョン2.8.3であり、 [download.qgis.org](http://download.qgis.org) から入手できます。

**謝辞**

私たちは、開発者、ドキュメント作成者、テスター、そして時間と労力をボランティアしている（あるいは人々に資金を提供する）多くの人々に感謝したいと思います。

QGISコミュニティはあなたがこのリリースを楽しんでいただけることを希望します！あなたが時間やお金を寄付したり、QGISをより素晴らしいものにすることに関与したいなら、[qgis.org](https://qgis.org) のサイトを見て手を貸してください！

最後に、このプロジェクトに提供した貴重な財政支援について、公式スポンサーに感謝したい。
- **ゴールドスポンサー:** [Asia Air Survey, Japan,](http://www.asiaairsurvey.com/)
- シルバースポンサー: [AGH University of Science and Technology, Krakow, Poland](http://www.agh.edu.pl/en)
- シルバースポンサー: [State of Vorarlberg, Austria](http://www.vorarlberg.at/)
- シルバースポンサー: [アイルランドの公共事業局、アイルランド](http://www.opw.ie/)
- シルバースポンサー: [Sourcepole AG, Switzerland](http://www.sourcepole.com/)
- ブロンズスポンサー: [Lutra Consulting, UK](http://www.lutraconsulting.co.uk/)
- ブロンズスポンサー: [WhereGroup GmbH & Co. KG, Germany](http://wheregroup.com/)
- ブロンズスポンサー: [Nicholas Pearson Associates, UK](http://www.npaconsult.co.uk/)
- ブロンズスポンサー: [QGIS Poland, Poland](http://qgis-polska.org/)
- ブロンズスポンサー: [www.terrelogiche.com, Italy](http://www.terrelogiche.com/)
- ブロンズスポンサー: [GeoSynergy, Australia](http://www.geosynergy.com.au/)
- ブロンズスポンサー: [Gaia3D, South Korea](http://www.gaia3d.com/)
- ブロンズスポンサー: [Royal Borough of Windsor and Maidenhead, UK](http://www.rbwm.gov.uk/)
- ブロンズスポンサー: [Chartwell Consultants Ltd, Canada](http://www.chartwell-consultants.com/)
- ブロンズスポンサー [Trage Wegen vzw, Belgium](http://www.tragewegen.be/)
- ブロンズスポンサー: [GFI - Gesellschaft fr Informations technologie mbH, Germany](http://www.gfi-gis.de/)
- ブロンズスポンサー: [GKG Kassel,(Dr.-Ing. Claas Leiner), Germany](http://www.gkg-kassel.de/)
- ブロンズスポンサー: [GIS-Support, Poland](http://www.gis-support.com/)
- ブロンズスポンサー: [ADLARES GmbH, Germany](http://www.adlares.com/)
- ブロンズスポンサー: [www.molitec.it, Italy](http://www.molitec.it/)
- ブロンズスポンサー: [www.argusoft.de, Germany](http://www.argusoft.de)
- ブロンズスポンサー: [Customer Analytics, USA](http://www.customeranalytics.com/)
- ブロンズスポンサー: [Avioportolano Italia, Italy](http://www.avioportolano.it/)
- ブロンズスポンサー: [Faculty of Geology, Geophysics and Environmental Protection, AGH, University of Science and Technology, Poland](http://www.wggios.agh.edu.pl/en)
- ブロンズスポンサー: [Urbsol, Australia](http://www.urbsol.com.au/)
- ブロンズスポンサー: [MappingGIS、スペイン](http://www.mappinggis.com/)
- ブロンズスポンサー: [GIS3W, Italy](http://www.gis3w.it/)

プロジェクトに財政上の貢献を大小行った寄付者の現在のリストは、 [寄付者リスト](https://qgis.org/en/site/about/sponsorship.html#list-of-donors) にあります。公式プロジェクトスポンサーになって頂けるのでしたら、[スポンサーシップのページ](https://qgis.org/en/site/about/sponsorship.html#sponsorship) で詳細をご覧ください。QGISへの出資は、私たちが6ヶ月の開発者会議、プロジェクト基盤の維持、バグ修正作業に資金を供給するのに役立ちます。

QGIS はフリーのソフトウェアです。利用する上で金銭を支払う義務はありません。実際、私たちは利用者の財政状況や社会的地位にかかわらず、より多くの人に QGIS を利用して欲しいと思っています。私たちは地理空間的な意思決定ツールによって人々が力を持つことが、全人類の社会をより良くすると信じています。

{{<table-of-contents >}}
## 一般情報
### 機能: 新しいようこそ画面
空のプロジェクトやキャンバスの代わりに、QGISでの最近のプロジェクトをリストで表示すると共にサムネイル画像出すことで、最後に実施していたプロジェクトに素早く簡単に戻れるようになります。

**この機能の開発者:** [OPENGIS.ch](http://www.opengis.ch) の Matthias Kuhn

![image11](images/entries/30f2ab32f4ae0d135a26b6a6ddb6705f0f6dd74a.webp)
### 機能：コード品質の継続的改善
アドレスサニタイザライブラリの使用により、何百ものメモリリークが特定され、修正されています。Coverity Scanを使用した自動コードスキャンは潜在的な問題の特定に定期的に使用されており、Coverityの欠陥密度は1000行のコードあたりわずか0.02個の欠陥で非常に低くなりました。自動化された単体テストのライブラリも2.12の間に大幅に増加し、より多くの回帰が特定され、直ちに修正されました。2.12では、OSXでの継続的なテストも追加したので、すべてのコミットがLinuxとOSXの両方のプラットフォームでユニットテストスイートに対してテストされました。

![image12](images/entries/774d1839283f357009c64811bd000e2f8ad97c7a.webp)
### 機能: 高度な設定エディタ
設定ダイアログに新しいパネルが追加されました。このパネルでは、あなたのプロフィールですでに定義されているオプションを編集できます。これは、あなたが何をしているのかを完全に理解することなくこれらの設定を変更すると、QGISで予期しない動作が発生する可能性があるため、パワーユーザーのみを対象としています。

**この機能の開発者:** [OPENGIS.ch](http://www.opengis.ch/) の Matthias Kuhn

![image13](images/entries/6d59988bf11726192579915cff18f2b81e3f9c8f.webp)
### 機能：相互に排他的なレイヤーツリーグループ
この機能を使用すると、グループ内の1つのレイヤだけがいつでも表示できるレイヤーグループを作成できます。この機能は、レイヤーツリービューのコンテキストメニューでグループごとに個別に切り替えることができます。

**この機能は以下によって開発されました：** [Gut3W](http://www.gis3w.it/) への下請けの [Lutra Consulting](http://www.lutraconsulting.co.uk/) の Martin Dobias

**この機能は以下によって資金提供されました：** トスカーナ地方（イタリア） -  SITA（CIG：63526840AE）

![image14](images/entries/5c68a4deab4d6058d05d3129fec89c6f9abb8530.webp)
### 機能：式ウィジェット内のフィールド値のフィルタリング
フィールドの値を使用する式を作成するときに、フィールド値プレビューパネルをフィルタリングできるようになりました。

**この機能は、によって開発されました：** Salvatore Larosa

![image15](images/entries/5d41174bdf2a059d41824590520857002a70a056.webp)
### 機能: ユーザインターフェースのテーマ変更をサポート
QGIS 2.12は、ウィンドウの背景、ボタンなどの外観をカスタマイズするために使用できるユーザーインターフェイステーマサポートをサポートしています。デフォルトでは、**Default** および **Night mapping** の2つのテーマが出荷されます。後者は、明るいテーマが目の緊張を引き起こすことが分かっている人が好むかもしれない暗いテーマです。ちょっとしたCSSを知っているなら、あなた自身のカスタムテーマをかなり簡単に作成することもできます\...

テーマサポートの詳細については、 [Nathan Woodrowのブログ記事](http://nathanw.net/2015/08/29/ui-theme-support-now-core-in-qgis/) を参照してください。

**この機能は、以下によって開発されました：** [Nathan Woodrow](http://nathanw.net/>)

![image16](images/entries/2ec302b12a3b0db8e7a66465afccb227bc543a3e.webp)
### 機能: 新しい関数の追加（v2.12）
「ファジーマッチング」のための一連の関数が追加されました。これらの関数には、2つの文字列の類似性を検索する機能と文字列間の発音的な一致を行う機能があり、指定された文字列に「ほぼ一致する」レコードのフィルタを実行できます。

さらに多くのジオメトリベース機能が追加されました.以下のものがあります:
- `num_points(geom)` ジオメトリ内のノード数を計算する
- `area(geom)`、 `length(geom)` および `perimeter(geom)` は、あらゆるジオメトリオブジェクトの面積、長さ、および周長を計算します。以前は、現在の地物のジオメトリの面積、長さ、および周囲の計算のみが可能でした。
- `start_point(geom)`、 `end_point(geom)`、 `point_n(geom, n)` は、ジオメトリの先頭、末尾、そして番号付けしたポイントを取得します
- `make_point(x,y)` は、手動でポイントジオメトリを作成します
- `x(geom)`、 `y(geom)` 関数は、ポイントジオメトリの x と y 座標、または、非ポイントジオメトリの重心 x/y を返す 

A new `project_color` function has been added, which allows you to retrieve a color from the project\'s color scheme by name. This lets you create \'linked colors\', where the color of symbol or labeling components can be bound to a color in the project\'s color scheme. Update the color in the scheme, and all the linked colors will be automatically refreshed to match!

さらにいくつかのとても便利な式が expressions+プラグインから移植されました。以下のものです:
- `color_part`: allows retreival of a specific color component (eg red, hue, alpha) from a color
- `set_color_part`: allows a specific color component to be overridden, eg alter the alpha value (opacity) of a color
- `day_of_week`: returns the day of week as a number from a date

さらに、表現機能の文脈ヘルプは、読みやすくするために改善されています。

![image17](images/entries/b56f529af78b2d970f057c2c25ba89b87a85ce85.webp)
### 機能: 式の中で使用する変数
式で使用するカスタム変数を定義できるようになりました。変数は、アプリケーションのグローバルレベル、プロジェクトレベル、レイヤレベル、およびコンポジションレベルで定義できます。CSSのカスケード規則と同様に、変数は上書きすることができます。たとえば、プロジェクトレベルの変数は、アプリケーションレベルの変数を上書きします。これらの変数を使用して、テキスト文字列やその他のカスタム式を構築できます。たとえば、このコンテンツを含むラベルを作成するコンポーザーでは、次のようになります。

`This map was made using QGIS [% @qgis_version %].` `The project file for this map is: [% @project_path %]`

Will render the label like this:

`This map was made using QGIS 2.12.` `The project file for this map is: /gis/qgis-user-conference-2015.qgs`

You can manage global variables from the `Settings -> Options` menu, and project level variables from `Project properties` (including adding your own custom variables).

**この機能は次の方によって開発されました:** [Nyall Dawson](http://nyalldawson.net/)

![image18](images/entries/19aca1d680543a4013c53ba80406bdd5ebff88c5.webp)
## 解析ツール
### 機能：識別ツールの派生フィールドに頂点数を追加
ライン地物で識別ツールを使用すると、地物の頂点の数が追加の派生属性として表示されるようになりました。
### 機能：ラスター整列ツール
This new tool in qgis_analysis library is able to take several rasters as input and:
- 同じCRSに再投影する
- 同じセルサイズにリサンプルし、グリッド内でオフセットする
- 関心のある領域をクリップします
- 必要に応じて値を再スケールする

**この機能は、以下によって開発されました：** [Kutoza](http://kartoza.com/) に下請けした [Lutra Consulting](http://www.lutraconsulting.co.uk/) `のMartin Dobias

** この機能は以下の方の資金提供で開発されました:** [DFAT](http://dfat.gov.au) の [InaSAFE プロジェクト](http://inasafe.org/)

![image2](images/entries/c613bb210ba0e85eb3b479ab79cd895827c22602.webp)
### 機能: Geometry CheckerプラグインとGeometry Snapperプラグイン
2つの新しいプラグイン（プラグインマネージャーで手動で有効にする必要があります）は、ジオメトリの検証と修正に使用できます。**ジオメトリチェッカー**プラグイン（右図）は、さまざまなタイプのシステマティックエラーのベクタデータセットをチェックして修正し、それらを解決しようとします。エラーを解決した後で、エラーリストを自動的に更新することにより、あるエラーを修正しても他のエラーも解決すると、すべてのエラーが問題リストから削除されます。

**ジオメトリスナッパー**ツールを使用すると、1つのベクターレイヤーのエッジと頂点を、ユーザー定義の許容差を使用して2番目のレイヤーのエッジと頂点に揃えることができます。

**この機能は以下によって開発されました：** [Sourcepole AG](http://www.sourcepole.ch/) の Sandro Mani

**この機能は以下によって資金提供されました：** [SolothurnのCanton](http://www.sogis.so.ch/)

![image3](images/entries/319136e65a51c7a8d76adac7aef89806db170c2e.webp)
## アプリケーションとプロジェクトのオプション
### 機能:暗号化パスワードの管理
QGIS 2.12 introduces a new authentication system (see [PR 2330, QEP 14](https://github.com/dakcarto/QGIS-Enhancement-Proposals/blob/auth-system/qep-14-authentication-system.rst)). Here\'s what is included:
- SQLiteデータベースに保存されたマスターパスワードで暗号化された認証設定
- 認証メソッドプラグインアーキテクチャ(データプロバイダに似ている仕組み)
- 基本認証メソッドプラグイン
- 基本プラグインにPostGISとOWSプロバイダ接続が統合されています
- PostGISとOWSの開発者と連携したベーシックな統合プラグイン
- SSLサーバー接続の設定（SSL接続エラーの例外またはカスタム設定を保存する）

PKI認証関連：
- 余分な認証局、中間証明書発行者、個人識別バンドルをインポートする
- Firefoxのような証明書コンポーネントを管理する
- ディスク上のPEMおよびPKCS＃12バンドル用の認証メソッドプラグイン、および保存された個人識別情報用のプラグイン
- OWS接続プロバイダが統合されました(PostGISと他のデータベースについてはも少し作業が必要です)

ネットワークドライブのセットアップを含む共有プロジェクトのシナリオでは、認証構成（authcfg）IDをユーザー間で共有されるものに編集できます。

authcfg IDはプロジェクトファイルに埋め込まれているので、各ユーザーはそのリソースのために、彼らの特定の資格情報を持つauth configを作る必要があるだけです。次に（configの作成時または後に）そのIDをそのプロジェクトファイルにあるのと同じIDになるように編集します。すると、使用される認証方法でそれぞれの資格情報が使われるだけで、リソースがロードされるときに誰のQGISでも同じ設定がクエリされます。

「バッド・レイヤーの処理」ダイアログでは、ダイアログ内でauth configsを追加/編集/削除し、一致するようにデータ・ソースURIを更新できます。したがって、共有プロジェクトのシナリオでは、ユーザーは、プロジェクトのロード時に、適切な新しいauth configをすぐに追加することができます（正確には、authcfg IDを使用する必要があります）。

Currently, the master password auto-set can be set via Python, or by way of a custom C++ plugin, on launch setups using a call to `QgsAuthManager::instance()->setMasterPassword( "mypassword", true )`, or by QGIS_AUTH_PASSWORD_FILE environment variable to set the path to a file with the master password.

**Note:** for Server, you can also use QGIS_AUTH_DB_DIR_PATH to set the path to a qgis-auth.db directory and QGIS_AUTH_PASSWORD_FILE to set the path to a file with the master password on the server.

PKI example docs: <https://github.com/dakcarto/QGIS-Enhancement-Proposals/blob/auth-system/extras/auth-system/pkiuser.rst>

**この機能は次の方によって開発されました:** Larry Shaffer

**この機能は次の方の資金提供で開発されました:** [Boundless Spatial, Inc.](http://boundlessgeo.com/)

![image4](images/entries/d6c9305a8dcaea3a5a6c039dec40d50e0caf23ff.webp)
## ブラウザ
### 機能：ブラウザでのPostGIS接続の改善
QGISブラウザでは、**スキーマの作成、名前変更、削除**、レイヤの名前の変更と切り捨て**、およびあるスキーマから別のスキーマへのテーブルのコピー**など、PostGIS接続の追加機能がサポートされています。 。

**この機能は次の方によって開発されました:** [Nyall Dawson](http://nyalldawson.net/)

** 次の方がテーブルをコピーしました:** Jürgen Fischer [norBIT GmbH](http://www.norbit.de/)

![image5](images/entries/00820dbcf67c97b61154e7e1f41af0397009b548.webp)
## データプロバイダ
### 機能:PostGISプロバイダの改良
PostGISプロバイダに次のような改善が加えられました。
- PostGISレイヤのルールベース描画機能のパフォーマンス改善
- ビューにおける複合キーのサポートが追加されました

**複合キーは次の方が開発しました:** Jürgen Fischer [norBIT GmbH](http://www.norbit.de/)

![image6](images/entries/bc56564581d97034137956cd27e945b3d3ceb3df.webp)
## データマネジメント
### 機能:DBManagerの改良
DBマネージャーツールにはたくさんの改善点があります。
- DBマネージャーでは、以前のバージョンで使用可能だったShapefileのみではなく、OGRでサポートされているデータ形式にデータをエクスポートできるようになりました。
- Oracle SpatialはDBManagerでサポートされるようになりました
- テーブルにデータをインポートする際には、新しいものをインポートする機能**を選択するだけで、インポートする項目を制限することができます。
- 新しいクエリウィンドウがタブとして作成され、ダイアログの数が削減されました

![image7](images/entries/daa22cc4517b58f2457d78781d4dbab12663ce9d.webp)
### 機能：属性テーブルセルの条件付き書式設定
This is a major improvement to QGIS\'s attribute table rendering support. You can now style table cells according to rules. For example you can colour all cells with a population of less than 50 000 in red. The option is enabled via a new icon on the table toolbar at the top right of the attribute table window. You can read more about this feature on [Nathan Woodrow\'s blog article](http://nathanw.net/2015/08/20/mixing-a-bit-of-excel-into-qgis-conditional-formatted-table-cells/).

**この機能は、以下によって開発されました：** [Nathan Woodrow](http://nathanw.net/>)

![image8](images/entries/ae9afefda043d31ef7718528d506d98e90e7a1f7.webp)
### 機能:ウィジェット内での相対パスのサポート
次の編集ウィジェットタイプの場合：
- ファイル名
- 写真
- ウェブビュー

ファイルブラウザで選択されたパスが.qgsプロジェクトファイルと同じディレクトリにある場合、パスは相対パスに変換されます。これにより、マルチメディア情報が添付されたQGISプロジェクトの移植性が向上します。

**この機能の開発者:** [OPENGIS.ch](http://www.opengis.ch/) の Matthias Kuhn

**This feature was funded by:** [Alta ehf](http://www.alta.is/)

![image9](images/entries/fcf703990b5cb743ffa5cc7778cb151022ff2d20.webp)
## デジタイズ
### 機能：デジタル化の改善
In QGIS 2.10 we mentioned that there is a new geometry architecture for QGIS but that not all features were supported in the digitising tools. With QGIS 2.12 we now have editing support for the **creation of curves / \'circular strings\`**. Note again that you need to be using a data provider (e.g. PostGIS, GML or WFS) that supports curves. These improvements to the digitising tools were also added in QGIS 2.12:
- 2点と半径を持つ円形の文字列を追加するツール
- 開始点,カーブポイント,終了点を指定して円形の文字列を追加するツール
- 新しい機能の描画をキャンセルするエスケープを許可する
- ノードツールを使用して編集するときにノードテーブルを表示します。ノードの正確なx座標とy座標、z値とm値（レイヤータイプに応じて）を手動で入力できます。

さらに、zまたはm次元を含むレイヤーで正しく機能するように、より多くのジオメトリの編集および修正ツールが更新されました。

**This feature was developed by:** Marco Hugentobler at [Sourcepole AG](http://www.sourcepole.ch/)

**この機能は以下によって資金提供されました：** [SolothurnのCanton](http://www.sogis.so.ch/)

![image10](images/entries/215ead2dd5e43e394d47169a7fd82aa5cc08b6b6.webp)
## ラベリング
### 機能: \"ポイントの周り\" モード時のデータ定義による象限
ポイントラベルがポイントの周り配置モードに設定されているときにデータ定義による象限を指定できるようになりました。これにより、特定のラベルの象限配置を手動で変更し、残りのラベルは自動配置になるようにできます。

詳細は [こちらの記事](http://nyalldawson.net/2015/07/recent-labelling-improvements-in-qgis-master/) を参照して下さい。

**この機能は次の方によって開発されました:** [Nyall Dawson](http://nyalldawson.net/)

![image19](images/entries/27a58b65cf449505c92cc6c8470a93d1f09893a1.webp)
### 機能：ポリゴンの内側に収まるラベルのみを描く
ポリゴンのレイヤーにオプションが追加され、ポリゴンの地物内に完全に収まるラベルのみが描画されます。

**この機能は次の方によって開発されました:** [Nyall Dawson](http://nyalldawson.net/)

![image20](images/entries/5c8461abe3aa5483c3243c0f145940b0d5fd1310.webp)
### 機能：ラベルの障害の優先順位を制御する
2.12では、ラベルの障害物の優先順位を指定できるようになりました。これにより、ラベルを他のレイヤーではなく特定のレイヤーから地物をオーバーラップさせることができます。優先度もデータ定義によることができ、特定の地物が他のものよりカバーされやすくなるようにすることができます。データ定義式またはフィールドを使用して、レイヤー内の特定の地物がラベルの障害物として機能するかどうかを制御することもできます。

**この機能は次の方によって開発されました:** [Nyall Dawson](http://nyalldawson.net/)

![image21](images/entries/f07a082bd4e62f059788c18a9de353107b8bdc44.webp)
### Feature：ポリゴンレイヤーが障害物となる様子を制御する新しいオプション
ポリゴンレイヤーの地物に重ならないようにラベルを配置する方法を制御する新しいオプションが追加されました。オプションは、ポリゴンの内側にラベルを配置したり、ポリゴンの境界上に配置したりしないようにすることです。境界線上にラベルを配置することを避けることは、地物が領域全体をカバーする地域境界レイヤーに役立ちます。この場合、これらの地物内にラベルを配置することは避けられず、代わりに地物の境界上にラベルを配置することを避ける方がよほど良いです。その結果、この状況におけるラベルの地図作成上の配置が向上します。

詳細は [こちらの記事](http://nyalldawson.net/2015/07/recent-labelling-improvements-in-qgis-master/) を参照して下さい。

**この機能は次の方によって開発されました:** [Nyall Dawson](http://nyalldawson.net/)

![image22](images/entries/e37943c654080e33219acb5e519970cf748c87bf.webp)
### 機能：ラベル優先度に対するデータ定義制御
頻繁に要求されるこの機能により、ユーザーは個々のラベルの優先順位を設定できます。過去のリリースでは、QGISではレイヤー全体のラベル優先度を設定できましたが、レイヤー内の地物の優先度を制御するオプションはありませんでした。これで、データ定義の式またはフィールドを使用して、ある地物をレイヤー内の他の地物に優先付けすることに優先順位を付けることができます。

詳細は [こちらの記事](http://nyalldawson.net/2015/07/recent-labelling-improvements-in-qgis-master/) を参照して下さい。

**この機能は次の方によって開発されました:** [Nyall Dawson](http://nyalldawson.net/)

![image23](images/entries/bd185cde38420f50fb540d742d178768d28ac577.webp)
### 機能:障害物のみのレイヤ用オプション
これによりユーザーは、自身のラベルをレンダリングしないで、他のレイヤーのラベルの障害物になるだけのレイヤーを設定することができます。これは、ラベル付けされていないレイヤーが他のレイヤーのラベルの障害物として機能できることを意味し、障害物レイヤーの地物にラベルを描くのをやめ、他のレイヤのラベルと地物の重なりを防止してラベルの自動配置を改善します。

スクリーンショットでは、Streetsに「他のラベルがこのレイヤの地物に被らないようにする」オプションが有効になっていることが分かります。 このように、ポリゴンジオメトリから得られた赤のラベルは、通りの軸と交差しないように配置されます。 適切な結果を得るには、ポリゴンレイヤーで「水平」または「フリー」を有効にする必要があります。

ラベル設定の「レンダリング」タブで、「ラベルが地物に被らないようにする」チェックボックスを有効にすることによって、レイヤーにラベルを付けることも、障害物のレイヤーとして機能させることも可能であることに注意してください。

詳細は [こちらの記事](http://nyalldawson.net/2015/07/recent-labelling-improvements-in-qgis-master/) を参照して下さい。

**この機能は次の方によって開発されました:** [Nyall Dawson](http://nyalldawson.net/)

![image24](images/entries/de1eae1359ce92045d51c6fa9bc3f014a3f3ae67.webp)
### 機能：ルールベースのラベリング
ラベルの配置やスタイリングをさらに細かく制御できるように、規則を使用して地物上のラベルのスタイルを設定できるようになりました。 規則に基づく地図作成と同様に、ラベル付け規則をネストすることで、非常に柔軟なスタイル設定オプションを使用できます。 たとえば、レンダリングされる地物のサイズに基づいてラベルをレンダリングできます（スクリーンショットに示すように）。

詳細は [`blogpost](http://www.lutraconsulting.co.uk/blog/2015/10/25/rule-based-labeling/) を参照してください。

**この機能は以下によって開発されました：** [Gut3W](http://www.gis3w.it/) への下請けの [Lutra Consulting](http://www.lutraconsulting.co.uk/) の Martin Dobias

**この機能は以下によって資金提供されました：** トスカーナ地方（イタリア） -  SITA（CIG：63526840AE）

![image25](images/entries/8846f57f0395e7f6b2543a92a5c55b67e8b19923.webp)
## マップコンポーザー
### 機能：アトラスナビゲーションの改善
フィールドまたは式を地図帳の「ページ名」として設定できるようになりました。地図帳ツールバーにページ番号のコンボボックスが追加されました。そこには利用可能なページ番号と名前のリストが表示されます。これにより、地図帳内の特定のページに直接ジャンプすることができます。

ページ名は、シンボル名やラベル式内でも使用でき、ページ名に基づいてアトラス機能の高度なスタイリングを可能にします。

**この機能は次の方によって開発されました:** [Nyall Dawson](http://nyalldawson.net/)

![image26](images/entries/bbf6147ef8be9d209fa188d6c524bce9d13d5ba8.webp)
### 機能：グリッドアノテーションのカスタムフォーマット
Composerのマップグリッドアノテーションは、エクスプレッションエンジンを使用して評価されるカスタムフォーマットでフォーマットできるようになりました。今あなたはマップが必要とするどんな難解なグリッドの番号付けフォーマットを利用しますか？

**この機能は次の方によって開発されました:** [Nyall Dawson](http://nyalldawson.net/)

![image27](images/entries/a6cd03594ca802015ef4a5bf7806cc1ce291214b.webp)
### 機能：コンポーザー属性テーブルの複数行テキスト処理と自動テキスト折り返し
Composer属性テーブルには、複数行の文字列を完全にサポートするようになりました。特定の文字にテキストを折り返すオプションや、列のサイズに合わせてテキストの折り返しを自動的に計算するオプションとともに、セル内のテキストの垂直方向の配置の制御も追加されました。自動行の高さで自動テキスト折り返しを適用するには、列幅を固定サイズに設定します。

**この機能は次の方によって開発されました:** [Nyall Dawson](http://nyalldawson.net/)

**この機能は以下によって資金提供されました：** [ウスター市](http://gis.uster.ch/)

![image28](images/entries/db66b56f79949779ea32126bd22f2f1c9d4b55e6.webp)
### 機能：セルの背景色の高度なカスタマイズ
この変更により、ユーザーは、コンポーザー属性テーブル内の行と列、最初/最後の行/列、ヘッダー行を交互に変える色を設定できます。

**この機能は次の方によって開発されました:** [Nyall Dawson](http://nyalldawson.net/)

**この機能は以下によって資金提供されました:** [Ville de Morges](http://www.morges.ch/)

![image29](images/entries/68266f6b11599dfa226952455ca150448a5d082a.webp)
### 機能：コンテンツにフィットするページを追加するオプションとコンテンツへのエクスポートをトリミングするオプション
コンポジションパネルに新しいオプションが追加され、コンポジションの内容に合わせてサイズを変更し、必要に応じて追加の余白を追加しました。

コンポーザの書き出しは、その内容に切り取ることもできます。このオプションを選択すると、コンポーザが出力する画像に、コンテンツ付きのコンポジションの領域のみが含まれます。必要に応じて、項目境界の周りに余白を追加するオプションもあります。

コンポジションに1つのページが含まれている場合は、コンポジションにすべての内容を含めるように出力がサイズ調整されます。複数ページのコンポジションの場合、各ページはクロップされ、そのページの項目だけが含まれます。

これを容易にするための新しい画像書き出しオプションダイアログが追加されました。これには、印刷解像度や書き出した画像のサイズをオーバーライドするための便利なショートカットも含まれています。

**スポンサー:** [NIWA](https://www.niwa.co.nz/)

**この機能は次の方によって開発されました:** [Nyall Dawson](http://nyalldawson.net/)

![image30](images/entries/38572cf4aa662cc4463c2a29f3d5ca38aa382632.webp)
### 機能：ベクターレイヤーをラスター画像としてレンダリングする
ベクタレイヤを強制的にラスタとしてレンダリングする新しいオプションがレイヤープロパティのレンダリングタブの下に追加されました。コンポーザーはすべてのノードをエクスポートされるファイルに含めるため、極端に細かいレイヤー（ノード数が多いポリゴンレイヤーなど）は、PDF/SVG形式で巨大なエクスポートをする原因になることがあります。これにより、生成されたファイルの処理や、外部プログラムで開く速度が非常に遅くなることもあります。これで、これらのレイヤーをレイヤー単位で強制的にラスタライズすることができ、エクスポートされたファイルにこれらのレイヤーに含まれるすべてのノードを含める必要がなくなります。最終的には、ファイルサイズが小さくなり、PDF / SVGが開きやすくなります。

**この機能は次の方によって開発されました:** [Nyall Dawson](http://nyalldawson.net/)

![image31](images/entries/0127fe10ecae31dbcd133492c93f33b0d569dcba.webp)
### 機能：地図レイヤーとスタイルプリセットのデータ定義コントロール
マップレイヤーとスタイルプリセットがコンポーザーマップに表示されるように、新しいデータ定義コントロールが追加されました。マップレイヤのデータ定義式は\ |になります。マップに表示されるレイヤー名の区切り（パイプ）区切りリスト、またはスタイルプリセットデータ定義式は、既存のスタイルプリセットの名前になります。

Using this control over map layers allows for \"layer-based\" atlases, where the map layers should change between atlas pages instead of or in combination with the map extent changing. An example could be an atlas looping over different administrative units and at the same time looping over several historic maps or aerial images.

**この機能は次の方によって開発されました:** [Nyall Dawson](http://nyalldawson.net/)

**この機能は以下によって資金提供されました：** [ウスター市](http://gis.uster.ch/)

![image32](images/entries/a8dc3b35df4020897e39c81bd22a469ab5ea6225.webp)
### 機能：ビューを非表示にするオプション/エクスポート
There\'s now an option to hide the display of pages while editing and exporting compositions. This option is useful for compositions which aren\'t intended for print and are not bound by any preset page sizes. You can hide the pages, then add and resize items in any way you desire without the visual distraction of page boundaries!

**スポンサー:** [NIWA](https://www.niwa.co.nz/)

**この機能は次の方によって開発されました:** [Nyall Dawson](http://nyalldawson.net/)
## プラグイン
### 機能:GRASS プラグインのアップデート
GRASSプラグインは、GRASS 7のサポートを有効にするように更新されました。GRASSレイヤーは、QGISブラウザまたはブラウザパネルからブラウズしてロードできます。GRASSベクターデータはQGIS内で直接編集できます。このプロジェクトには、次の作業パッケージが含まれています。
- プラグインライブラリのアップグレードとマルチバージョンビルド
- QGISブラウザとブラウザパネルの統合
- データ解析を可能にするマップセット、モジュール、シェルのサポート
- ベクター編集

GRASS 6とGRASS 7の両方のユーザーにとって、GRASSとQGISの統合はずっとシームレスです。QGISブラウザパネルで直接GRASSレイヤーを作成し、標準のQGISスタイリングツールを使用してGRASSベクターレイヤーをスタイル設定し、使い慣れたQGISデジタイジングツールを使用して、新しいベクタージオメトリをGRASS地図セットに作成できます。

[QGIS GRASS Plugin Upgradeプロジェクトページ](http://www.gissula.eu/qgis-grass-plugin-crowdfunding/) と [progress report](http://www.gissula.eu/qgis-grass- plugin-crowdfunding/progress.html) も参照してください

**この機能は次の方によって開発されました:** [Radim Blazek](http://www.gissula.eu/)

**This feature was funded by:** Crowd funding, see [project page](http://www.gissula.eu/qgis-grass-plugin-crowdfunding/)

![image33](images/entries/fb9ac25e9ca6c5e4030167e289435e995f5af8f5.webp)
## プログラマビリティ
### 機能: マップツールが app-\>gui に移動しました
この変更により、PyQGISスクリプトやPythonプラグインからマップツールを再利用することができます。

**この機能の開発者:** [OPENGIS.ch](http://www.opengis.ch/) の Matthias Kuhn

**This feature was funded by:** [SIGE](http://www.sige.ch/)
### 機能: \`with edit(layer):\`  を利用した編集
例:

    from qgis.core import edit
    
    with edit(layer):
       f=layer.getFeatures().next()
       f[0]=5
       layer.updateFeature(f)
    
これにより、最後に自動的にcommitChanges（）が呼び出されます。例外が発生すると、すべての変更がロールバック（）されます。

**この機能の開発者:** [OPENGIS.ch](http://www.opengis.ch/) の Matthias Kuhn
### 機能: ラベリングエンジン用新API(QgsLabelingEngineV2)
考え方は、エンジンをQgsPalLabelingの実装と比較してより柔軟にすることです。
> - エンジン自体からのテキストラベル/図の抽象的な扱い
> - レイヤーごとに複数のタイプのラベルを許可する
> - カスタムラベルプロバイダをサポートします（たとえば、プラグインによって実装されます）
> - ラベリングエンジンをマップレンダリングエンジンから独立させる
> - ラベリングエンジンとそのコンポーネントの自動テストを容易にする

詳細は [`blogpost](http://www.lutraconsulting.co.uk/blog/2015/10/25/rule-based-labeling/) を参照してください。

**この機能は以下によって開発されました：** [Gut3W](http://www.gis3w.it/) への下請けの [Lutra Consulting](http://www.lutraconsulting.co.uk/) の Martin Dobias

**この機能は以下によって資金提供されました：** トスカーナ地方（イタリア） -  SITA（CIG：63526840AE）
### 機能: 外部エディタによるスクリプトのオープン
Pythonistasは喜んでいます。コンソールに追加された新しいボタンを使用して、外部エディタでスクリプトを開くことができます。

**この機能は、以下によって開発されました：** [Nathan Woodrow](http://nathanw.net/>)

![image34](images/entries/78acf0058f4306bf408a58df3762dff5986633a7.webp)
### 機能:PyQGISプログラム用の新しいクラス
PygGISスクリプトが2.12で追加された新しいファジーマッチングアルゴリズムを利用できるようにする新しいクラスQgsStringUtilsが追加されました。これらの関数には、2つの文字列間のLevenshtein編集距離を検索し、文字列のsoundex音声表現を計算する関数が含まれています。これらのアルゴリズムはパフォーマンスのために高度に最適化されているため、数百万の文字列にわたってファジーマッチングを開始する準備ができています。

**この機能は次の方によって開発されました:** [Nyall Dawson](http://nyalldawson.net/)
## QGISサーバー
### 機能:QGISサーバPython API
QGIS Serverは、初期（しかし成長している）APIとPythonバインディングを持つライブラリとしてパックされています。新しいAPIを使用して、サーバーのメインコンポーネントとサーバープラグインの一連のPythonテストを行います。Pythonからサーバを呼び出すのは簡単です：

    from qgis.server import QgsServer
    headers, body =  QgsServer().handleRequest(my_query_string)
    
For more information see [this article](http://www.itopen.it/qgis-server-binding-news/)

**This work has been developed and funded by**: Alessandro Pasotti at [ItOpen](http://www.itopen.it/)
### 機能:dxf形式におけるgetMap
GetMap WMSリクエストの結果をDXF形式で取り出すことができるようになりました。QGISデスクトップで使用できるのと同じ機能とオプションをサポートしています。同じ制限があります。

| Sample URL: | `http://yourserver.org/cgi-bin/qgismapserver.fcgi?` | `map=/path/to/your/projectfile.qgs&` | `SERVICE=WMS&` | `VERSION=1.3.0&` | `REQUEST=GetMAP&` | `FORMAT=application/dxf&` | `FORMAT_OPTIONS=SCALE:500;MODE:SYMBOLLAYERSYMBOLOGY&` | `FILE_NAME=youroutputfilename.dxf&` | `CRS=EPSG:EPSG:21781&` | `BBOX=695558.73070825,244430.77224034,697158.88528251,245722.25976142&` | `WIDTH=1042&` | `HEIGHT=841&` | `LAYERS=yourdxfexportlayers`

See also [QGIS as OGC data server](http://docs.qgis.org/2.18/en/docs/user_manual/working_with_ogc/ogc_server_support.html#dxf-export) for all the available options.

スクリーンショットでは、左側にQGIS Web Clientが表示され、DXFエクスポート機能（QGISサーバーを利用）と同じエクステントが右側のAutodesk TrueViewで表示されます。

**This feature was developed by:** Marco Hugentobler [Sourcepole AG](http://www.sourcepole.ch/)

**この機能は以下によって資金提供されました：** [ウスター市](http://gis.uster.ch/)

![image35](images/entries/beb2e9c00102c67ae703eac097ffba8866379609.webp)
## シンボロジ
### 機能：スタイルマネージャからサムネイルをエクスポートする
スタイルマネージャーでは、選択したスタイルサムネイルをSVGまたはPNG画像として書き出すことができます。

**この機能は、以下によって開発されました：** [Nathan Woodrow](http://nathanw.net/>)

![image36](images/entries/8861a040751804f6c2691ee4d93d410efd6d99ac.webp)
### 機能：地図単位のサイズを使用する際のサイズをmm単位で制限する新しいオプション
以前は、マップユニットサイズのスケール範囲を制限するオプションのみが使用できました。これで、対応するレンダリングサイズをmmで制限することもできます。

![image37](images/entries/b822235ddb09b4184b926bf2e0acc5c892147d0b.webp)
### 機能：変位レンダラの改善
- ディスプレースメントレンダリングの許容誤差（mm /ピクセル）を許容
- 色の透明度の設定を許可する
- 同心円配置モード（リングのみよりもコンパクトな表示が可能）

**この機能は次の方によって開発されました:** [Nyall Dawson](http://nyalldawson.net/)

![image38](images/entries/33b5f15429279a7ec75dd1f6a2e01b1a7df789ca.webp)
### 機能：すべてのカラーランプを編集できるようになりました
In QGIS 2.12 \"edit\" buttons have been added next to every color ramp choice. This allows you to easily edit an existing color ramp without having to create a new ramp and overwrite the existing one.

![image39](images/entries/6ca1426e6e9bfd5500b08fb2185ae50a77258892.webp)
### 機能：SVGマーカーアウトラインの処理が改善されました。
QGIS 2.12では、SVGマーカーおよびSVG塗りつぶしシンボル内のアウトラインの処理に関するいくつかの問題が修正されています。

QGISの以前のバージョンでは、アウトラインがセットよりもかなり小さいサイズでレンダリングされ、マップ単位のアウトラインサイズの描画SVGが破損していました。

These issues have been fixed in QGIS 2.12, but as a result you may need to update your project symbology if you\'ve previously set oversized outlines for your symbols to overcome these bugs. In the image you see QGIS 2.12 vs QGIS 2.10 SVG markers in the symbol layer dialogs.

![image40](images/entries/a678d22393345b4fcc07b5bd023babe383151b46.webp)
### 機能：すべてのシンボルサイズユニットの選択肢のオプションとしてピクセルを追加する
For all size input widgets there is now a third option \"pixel\", next to \"mm\" and \"map units\". This concerns symbol sizes, stroke widths, dash sizes, offsets, etc. This may help, if you design for screens and not for print output.

**この機能は次の方によって開発されました:** [Nyall Dawson](http://nyalldawson.net/)

![image41](images/entries/cbc683061bcc06764361ab79874f1020ccfe8eb7.webp)

{{<content-end >}}
