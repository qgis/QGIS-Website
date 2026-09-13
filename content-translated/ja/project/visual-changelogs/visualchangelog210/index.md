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

QGIS の次のリリース 2.10.0 \' Pisa\' の変更履歴。Pisa は2010年3月のディベロッパーミートアップの開催都市です。

**最新リリース**

これは4カ月ごとのリリースシリーズの次のリリースです。 これは、私たちが取り組んでいる新機能への早期アクセスを提供し、QGIS開発の「最先端」を表しています。 新しい機能をユーザーに展開することについてもっと慎重にしたい運用環境で作業している場合は、QGISのLTR（Long Term Release）バージョンも提供しています。 現在のLTRはバージョン2.8.2であり、 [download.qgis.org](http://download.qgis.org) から入手できます。 LTRリリースは、バックポートによるバグ修正を1年間サポートし、恒久的な機能凍結（新しい機能は追加されず、バグフィックスと簡単なアップデートのみ）になります。 QGIS 2.10 \'Pisa\' で提供される機能は、次のLTRリリース（2016年にリリース予定）に含まれる予定です。このリリースを使用すると、次のLTRに入り込む新しい機能をテストする絶好の機会が得られます。

**QGIS 2.10 \'Pisa\' の新機能**

QGIS 2.10.0には、最も人気のあるフリーデスクトップGISをさらに充実した機能にしてくれるように、多くの素晴らしい新機能、調整、改良が含まれています。 新しい機能がソフトウェアに追加されるたびに、新しいバグが発生する可能性があります。このリリースで問題が発生した場合は、 [QGISバグトラッカー](http://hub.qgis.org) にチケットを提出してください。

**謝辞**

私たちは、開発者、ドキュメント作成者、テスター、そして時間と労力をボランティアしている（あるいは人々に資金を提供する）多くの人々に感謝したいと思います。

QGISコミュニティはあなたがこのリリースを楽しんでいただけることを希望します！あなたが時間やお金を寄付したり、QGISをより素晴らしいものにすることに関与したいなら、[qgis.org](https://qgis.org) のサイトを見て手を貸してください！

最後に、このプロジェクトに提供した貴重な財政支援について、公式スポンサーに感謝したい。
- **ゴールドスポンサー:** [Asia Air Survey, Japan,](http://www.asiaairsurvey.com/)
- シルバースポンサー: [Sourcepole AG, Switzerland](http://www.sourcepole.com/)
- シルバースポンサー: [State of Vorarlberg, Austria](http://www.vorarlberg.at/)
- シルバースポンサー: [アイルランドの公共事業局、アイルランド](http://www.opw.ie/)
- シルバースポンサー: [AGH University of Science and Technology, Krakow, Poland](http://www.agh.edu.pl/en)
- ブロンズスポンサー: [www.molitec.it, Italy](http://www.molitec.it/)
- ブロンズスポンサー: [www.argusoft.de, Germany](http://www.argusoft.de)
- ブロンズスポンサー: [www.openrunner.com, France](http://www.openrunner.com)
- ブロンズスポンサー: [GKG Kassel,(Dr.-Ing. Claas Leiner), Germany](http://www.gkg-kassel.de/)
- ブロンズスポンサー: [Customer Analytics, USA](http://www.customeranalytics.com/)
- ブロンズスポンサー: [Urbsol, Australia](http://www.urbsol.com.au/)
- ブロンズスポンサー: [MappingGIS、スペイン](http://www.mappinggis.com/)
- ブロンズスポンサー: [Lutra Consulting, UK](http://www.lutraconsulting.co.uk/)
- ブロンズスポンサー: [ADLARES GmbH, Germany](http://www.adlares.com/)
- ブロンズスポンサー: [Avioportolano Italia, Italy](http://www.avioportolano.it/)
- ブロンズスポンサー: [GeoSynergy, Australia](http://www.geosynergy.com.au/)
- ブロンズスポンサー: [Gaia3D, South Korea](http://www.gaia3d.com/)
- ブロンズスポンサー: [Royal Borough of Windsor and Maidenhead, UK](http://www.rbwm.gov.uk/)
- ブロンズスポンサー: [Chartwell Consultants Ltd, Canada](http://www.chartwell-consultants.com/)
- ブロンズスポンサー [Trage Wegen vzw, Belgium](http://www.tragewegen.be/)
- ブロンズスポンサー: [GIS-Support, Poland](http://www.gis-support.com/)
- ブロンズスポンサー: [GIS3W, Italy](http://www.gis3w.it/)
- ブロンズスポンサー: [GFI - Gesellschaft fr Informations technologie mbH, Germany](http://www.gfi-gis.de/)
- ブロンズスポンサー: [Faculty of Geology, Geophysics and Environmental Protection, AGH, University of Science and Technology, Poland](http://www.wggios.agh.edu.pl/en)

プロジェクトに財政上の貢献を大小行った寄付者の現在のリストは、 [寄付者リスト](https://qgis.org/en/site/about/sponsorship.html#list-of-donors) にあります。公式プロジェクトスポンサーになって頂けるのでしたら、[スポンサーシップのページ](https://qgis.org/en/site/about/sponsorship.html#sponsorship) で詳細をご覧ください。QGISへの出資は、私たちが6ヶ月の開発者会議、プロジェクト基盤の維持、バグ修正作業に資金を供給するのに役立ちます。

QGIS はフリーのソフトウェアです。利用する上で金銭を支払う義務はありません。実際、私たちは利用者の財政状況や社会的地位にかかわらず、より多くの人に QGIS を利用して欲しいと思っています。私たちは地理空間的な意思決定ツールによって人々が力を持つことが、全人類の社会をより良くすると信じています。

{{<table-of-contents >}}
## 一般情報
### 機能：結合パラメータを編集できるようになりました
結合が作成された後で、結合パラメータ（結合接頭辞または結合する列など）を編集できるようになりました。この変更に先立って、結合全体を削除して再作成する必要がありました。

![image14](images/entries/bb09241b7b997dfa07942ee5172ad466ebb777f7.webp)
### 機能：結合のあるレイヤーをフィルタリングできるようになりました
バージョン2.10以前では、少なくともひとつの結合をもつレイヤーをフィルタリングできませんでした。フィルタリングは可能になりましたが、元のマスター表の列のみを使用します。

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

**この機能は次の人が開発しました:** [Jürgen Fischer (norBIT)](http://www.norbit.de/)

![image17](images/entries/c30c07afc9123db564b766339daefe53af3cd348.webp)
### 機能:新しいジオメトリエンジン
QGIS 2.10には新しいジオメトリエンジンが搭載されています。一般的に、ユーザーインターフェイスにはまだ多くの違いはありませんが、将来的にサポートできるようになる、より豊かな地理空間機能の基盤となります。新しい実装では、カーブしたジオメトリタイプをサポートしています（たとえば、交通の円形交差点を円に見えるように分割されたポリゴンではなく、円として表すことができます）し、ジオメトリの z/m 値のバックエンドサポートがあります。QGISで曲線を使用するには、PostGISまたは曲線のジオメトリを表現できる同様のデータストアを使用する必要があります。遊びをしたい場合は、PostGISデータベースで次のような簡単な演習を試すことができます:

    -- Table: curves DROP TABLE curves;
    CREATE TABLE curves (
       id bigserial NOT NULL,
       geometry geometry(CURVEPOLYGON, 4326),
       name text,
       CONSTRAINT p_key PRIMARY KEY (id)
       );
    
    INSERT INTO curves VALUES ( 1, st_geomfromtext(
       'CURVEPOLYGON(CIRCULARSTRING(1 1,1 2, 2 2, 2 1, 1 1))', 4326), 'test');
    
こうするとレイヤ `curves` をあなたのプロジェクトに追加できます.

**この機能は、以下によって開発されました：** [Marco Hugentobler (Sourcepole AG)](http://www.sourcepole.ch/)

**この機能は以下によって資金提供されました:** [KantonSolothurn, スイス](http://www.sogis.ch/)

![image18](images/entries/4f070e4075b4703edb40d8cb91d5fb527d1d3a93.webp)
## 解析ツール
### 機能：新しい統計要約ドックウィジェット
ベクターレイヤーまたは選択から、フィールドまたは式の要約統計量（平均値、標準偏差など）を表示できます。これは `ビュー -> パネル -> 統計` メニューから起動できる新しいドックパネルによって提供されます。作成できるのは **数値の列** を持つ **ベクターレイヤー** の統計だけであることに注意してください。

![image1](images/entries/7d52fdffac5546ea3f39ee4dac5dbe19f961703a.webp)
### 機能：ラスター計算機で対数関数を使用する
ラスター計算機（QGISメニューの `ラスター -> ラスター計算機` ）は、1つまたは複数のラスターレイヤーで行列演算を実行できるツールです。QGIS 2.10では、ラスター計算機で `LN` と `LOG10` を使うことができます。

![image2](images/entries/13c65100ab57ed8f97fa23b08704ca726a7c33da.webp)
### 機能：新しいゾーン統計機能
領域統計は、ポリゴンの基礎となるピクセルの集約値を抽出する方法を提供します。ゾーン統計ツールには、次の新機能が追加されました。
- 計算する統計を選択できるようになりました
- 余計な統計情報が追加されています（中央値、標準値、最小値、最大値、範囲値、少数値、
- 統計抽出に使用するラスタバンドを選択する機能

ゾーン統計は「コアプラグイン」（QGISインストーラに同梱されているプラ​​グイン）ですが、デフォルトでは無効になっています。プラグインマネージャでそれを有効にする必要があり、そうすると 「ラスタ」メニューにゾーン統計のメニュー項目が現れます。

![image3](images/entries/d86b8eb8a72d26a0fcb0bf043c9189e14a4ae125.webp)
## ブラウザ
### 機能:新しいブラウザプロパティウィジェット
QGISブラウザドックパネル（ `ビュー -> パネル -> ブラウザ` ）を使うと、ファイルシステムツリーの一番下にプロパティウィジェットを有効にすることができます。クリックするデータソースのプロパティは、このパネルに表示されます。これにより、選択したデータセットに関する基本情報をすばやく簡単に表示できます。プロパティビューを切り替えるには、ブラウザパネルの上部にある `i` アイコンを使うべきです。

![image4](images/entries/2f3fed9a32d761418704da2a7da378ba172164da.webp)
### Feature: New browser icon
QGISブラウザは、ファイルシステム、データベース接続、Webサービス接続などから利用可能なGISデータセットをブラウズして表示するための独立したスタンドアロンアプリケーションです。以前のリリースのQGISでは、多くのユーザーにとって混乱の原因となっていたQGISアプリケーション自体。間違ったアプリケーションを開く可能性を減らすために、QGISブラウザ用の新しいアイコンを作成しました。

![image5](images/entries/e76e98dffc99404f3cad540c42baebb434a696fe.webp)
## データプロバイダ
### 機能：DXFエクスポートの改善
最後の3つのQGISバージョンでは、DXFエクスポートが継続的に改善されました。 このバージョンでは、改良されたSVGやDXFブロック変換の簡単なマーカーが導入され、不完全な（判読不能な）DXFファイルとなるいくつかのバグや問題が修正されています。 スクリーンショットでは、左側のQGISの元のビューと、右側のAutodesk TrueViewでエクスポートされたDXFファイルのレンダリングを見ることができます。

[qgis.ch にあるこの記事](http://www.qgis.ch/en/projects/dxf-export) は、サポートされるものとされないものについて説明しています。

**この機能は次の人が開発しました:** [Jürgen Fischer (norBIT)](http://www.norbit.de/)

**この機能は、以下によって資金提供されました：** Morges、Uster、VeveyおよびSIGEのコミュニティ

![image6](images/entries/b5ee8bd7a3412e429782a5e56954dabee05c36ff.webp)
### Feature: PostGIS provider side expression filters
QGIS 2.10では、データベースサーバー側の機能をフィルタリングできるようになりました。サポートされている式のみがデータベースに送信されます。サポートされていない演算子や関数を使用した式は、ローカル評価に正常にフォールバックします。

この機能を利用するには、 `設定 -> オプション -> データソース` で有効にする必要があります。フィルタ式がPostgreSQL準拠の場合、自動的にサーバ側で実行されます。これらの呼び出しを使用する場合など、Python APIを使用する場合にもこの機能を使用することができます。

`QgsFeatureRequest().setFilterExpression( expression )`

または

`QgsVectorLayer::getFeatures( expression )`

![image7](images/entries/4d4076579ecc0b5aace30fa2743f616a9b691a02.webp)
## データマネジメント
### 機能:バーチャルフィールドが現在は更新可能です
バージョン2.8より前のバージョンでは、仮想フィールドの計算式を変更したい場合は、仮想フィールドを削除して再作成する必要がありました。2.10では、 `Fields` タブに行き、小さな `Expression` ボタンを押して式エディタを開き、仮想フィールドに使用されている式を更新することができます。

**この機能は、以下によって開発されました:** [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch/) 

**この機能は以下によって資金提供されました：** [Uster市、スイス](http://gis.uster.ch/)

![image8](images/entries/f45d5a4447f28d96a2c5c4cc6c27b84285096a02.webp)
### 機能：ValueRelation編集ウィジェットの自動補完機能付きライン編集
ベクターレイヤーの値関係編集ウィジェット（ `レイヤー -> プロパティ -> フィールド -> ウィジェットの編集 -> 値関係` ）をオートコンプリートに設定できるようになり、入力ボックスで入力を開始すると、地物フォーム上に作成します。

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
他の表からリンクされた項目を選択するには、関係参照ウィジェットを使用できます。リンクされた地物にジオメトリが添付されているか、リンクされたIDでエレメントを選択している場合は、地図で地物を選択することによって、エレメントをグラフィカルに選択できます。非空間選択を容易にするために、フィルタ（連鎖または非連鎖）で利用可能なオプションを絞り込むことが可能になりました。フィルタが非連鎖の場合、選択肢は「AND」と組み合わせて使用​​可能なオプションを定義します。連鎖がチェックされている場合、フィルタのドリルダウンモードがアクティブになり、各フィルタは前のフィルタに対応するエントリのみを表示します。これは City -\> Street  -\> Number のような階層的なデータから選択するのに便利です。

**この機能は、以下によって開発されました:** [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch/) 

** この機能は次の方の資金提供で開発されました:** [SIGE](http://www.sige.ch/)

![image11](images/entries/fd0d2e726135033e8e5a61b8a718535074a2ac0c.webp)
## ダイアグラム
### 機能:ダイアグラムの改善
QGISのダイアグラム機能により、小さな円グラフやヒストグラムを地図上の地物に重ね合わせできます。今回のリリースでは、ダイアグラムのサポートが次のように改善されました。
- ダイアグラムは設定を失うことなく無効にすることができます
- チェックボックスを追加すると、常にレイヤーの図が表示されます
- ダイアグラムのユーザーインターフェイスが更新され、ダイアログが簡素化され、ユーザーフレンドリーになりました
- 図のクラスがレイヤの凡例に表示されるようになりました

![image12](images/entries/cc5753de0538c89e3231f18c7ce62c7bc0afa5e8.webp)
## デジタイズ
### 機能：ジオメトリ回転ツールの改良
ジオメトリ回転ツールは、地物のジオメトリを任意に回転させる高度なデジタイジングツールです。回転ツールの改良点は次のとおりです:
- 回転マップツールで数値入力を使用できるようになりました
- 角度の設定にコンボボックスを利用できます
- 角度に対するスナッピングがサポートされました （ shift + click\`\` を `使う` と直接有効化されます）
- 回転のアンカーは `CTRL+click` で指定され、マウスの動きでは指定できません

![image13](images/entries/7ff32dd8c7ead358f9ffab4576dff33503154eb2.webp)
## ラベリング
### 機能: マルチラインラベル用の \"ポイントの周り\" 配置オプション
このモードに設定すると、ラベルのテキストの配置は、ポイントに対するラベルの最終的な配置に依存します。たとえば、ラベルがポイントの左に配置されている場合はラベルは右揃えになり、ポイントの右に配置されている場合はラベルが左揃えになります。これにより、ポイントレイヤの複数ラベルの外観が大幅に改善されます。

![image19](images/entries/851e7234a9509e2452dee69939d9de933a8bb90a.webp)
## マップコンポーザー
### 特長：スケールバーのサイズを希望のスケールバーの幅に合わせる
以前のQGISversionsでは、潜在的なスケールの範囲が大きかった場合、グラフィカルなスケールバーを使用することは困難でした。スケールバーは、すばやすぎるか狭すぎるかのいずれかであり、スケール変更後にセグメントサイズ（セグメントあたりの単位）を手動で適応させなければならなかった。また、グラフィカルなスケールバーは、Atlasのシリアル印刷や最終的な地図のスケールが不明なときにQGISserverで実際に使用することはできませんでした。QGIS2.10を使用すると、mm単位で1セグメント長の最小/最大サイズを設定できるようになり、QGISは丸め値を維持しながらセグメントごとに自動的に単位を適合させることになります。

スケールバーのアラインメントも設定することを忘れないでください。あなたはそれが中央寄せか右寄せであることを望むならば！

**この機能は、以下によって開発されました：** [Sandro Mani（Sourcepole AG）](http://www.sourcepole.ch/)

**この機能は以下によって資金提供されました：** [Kanton Glarus、Switzerland](http://geo.gl.ch/)

![image20](images/entries/d435d4f94cf3d70a97c8d373aa08c28f8685defd.webp)
## プログラマビリティ
### 特集：プログラマーのための改善
私たちは、開発者にとって興味深いいくつかの変更と改善を行いました。
- Qt4の最小要件をバージョン4.8に引き上げました。Qt4は、QGISを作成するために使用する主要なC ++ツールキット/ライブラリの1つです。
- 数値のリストから統計を計算する新しい `QgsStatisticalSummary` クラスです。
- ベクタレイヤのデータソース変更が許可されます.
- 暗黙的なクラスの共用 : `QgsField`, `QgsFields`, `QgsDataDefined`, `QgsFeature`, `QgsGeometry` 。
- プラグインは、 `QgsDataItemProvider` と `QgsDataItemProviderRegistry` という2つの新しいクラスを持つブラウザウィジェットに独自のエントリを作成できるようになりました。

![image21](images/entries/c702d89260cbab35323c052a15ab5c5728fc7115.webp)
## QGISサーバー
### 機能：WMS GetFeatureInfo要求の許容量パラメータのサポート
QGIS Serverが提供するWMSレイヤーを使用する場合、クリック起点のGetFeatureInfo要求がどのくらい離れているかを考慮する必要があります。これは、機能を正確に指すことが難しいモバイルデバイスにとっては重要です。この新機能が登場する以前は、QGISサーバーを搭載したモバイルデバイス上のポイントまたはラインの機能を特定することは事実上不可能でした。GetFeatureInfoリクエストに次のパラメータを追加できます。

FI_POINT_TOLERANCE=16&FI_LINE_TOLERANCE=8&FI_POLYGON_TOLERANCE=4

必要に応じて許容値（ピクセル単位）を変更します。

**この機能は、以下によって開発されました：** [Marco Hugentobler (Sourcepole AG)](http://www.sourcepole.ch/)

**この機能は以下によって資金提供されました：** [Uster市、スイス](http://gis.uster.ch/)

![image22](images/entries/29470cc51906dffe3a96d3e17a7e8c83b4504a18.webp)
## シンボロジ
### 機能:既存スタイルを使ったカテゴリマッチ
分類されたレンダラーの詳細メニューのオプションを追加して、スタイルライブラリまたはXMLスタイルファイルの名前と一致するシンボルにカテゴリを設定します。

![image23](images/entries/c3fe0d0389c267271cbd47b8c44f52ac079961d7.webp)
### 機能：段階的レンダラーを使用してシンボルサイズを変更する
レンダラーはQGISのサブシステムであり、データの豊富な地図表現を作成することができます。段階的レンダラーは、ベクターレイヤーの連続的に変化する値に基づいてシンボルを変化させる。QGISの以前のバージョンでは、色を変えることしかできませんでした（たとえば、カラーランプに沿って色を使用するなど）。QGIS 2.10では、目盛り付きのシンボルレンダラーでサイズ *または* 色を変更できるようになりました。ポイントレイヤーではポイントサイズを変えることができます。ラインではライン幅を変えることができます。ポリゴンレイヤーは色によって変化する能力しか保持しませんが、線幅はまだサポートされていません。

**この機能は、以下によって開発されました：** [Vincent Mora（Oslandia）](http://www.oslandia.com/)

**この機能は以下によって資金提供されました：** [Agence de l\'eau Adour-Garonne](http://www.eau-adour-garonne.fr/)

![image24](images/entries/1d170efe9ca0c76e971cfe0f1d0adb7c4e14f08f.webp)
### 機能：地物を地図範囲に自動的にクリッピングさせないための新しいオプション
このオプション（シンボルの詳細メニューの下にあります）は、線/ポリゴンのキャンバス範囲への自動クリッピングを無効にします。場合によっては、このクリッピングは好ましくないシンボロジ（例えば、重心が常に実際の地物の重心でなければならない重心を満たす）をもたらす。

![image25](images/entries/ecd30b6893fd93d65c95df8f069cc3c3e0fff7be.webp)
### 機能：詳細メニューからサイズのスケールと回転が削除されました
「Layer -> Properties -> Symbology tab -> Advanced Menu」 から `SizeScale` と `Rotation` を削除しました。式またはフィールドを使用して、*シンボルレイヤー単位* で回転を設定する必要があります。古いプロジェクトで使用された式は、シンボルレベルの **データ定義のサイズと角度** のプロパティに変換されます。

**この機能は、以下によって開発されました：** [Vincent Mora（Oslandia）](http://www.oslandia.com/)

**この機能は以下によって資金提供されました：** [Agence de l\'eau Adour-Garonne](http://www.eau-adour-garonne.fr/)

![image26](images/entries/2e02fb11f0f967b1ea17331d9af3d5a22a63fed1.webp)
### 機能：フォントマーカーのデータ定義プロパティ
フォントマーカのほとんどのプロパティは、マーカのサイズ、回転、文字など、定義されたデータにすることができます。

![image27](images/entries/9ffd9d3284adcc85d6434f0b97f2db8974a7f647.webp)
### 機能：ヒストグラムを使用して目盛レンダラーを視覚化して変更する
段階的レンダラーに新しいヒストグラムタブが追加され、割り当てられたフィールドまたは式からの値のインタラクティブなヒストグラムが表示されます。クラス区切りは、ヒストグラムを使用して移動または追加することができます。

**この機能は次の方の資金提供で作成されました:** [ADUGA](http://www.aduga.org)

**この機能は次の方によって開発されました:** [Nyall Dawson](http://nyalldawson.net/)

![image28](images/entries/b519e61b5b50de563203adf8ef35a7c037536332.webp)
### 機能：シンボルレベルでのサイズ、回転、ストローク幅の表現
サイズと回転は、マーカーを構成するすべてのシンボルレベルの式で定義できます。幅は、行を構成するすべてのシンボルの式で定義できます。

シンボルの場合、さまざまなサイズの凡例が生成されます。これにより、分類/段階分けした色の場合の多変量解析の凡例が可能になります。

アシスタント（プレビュー付）は、データ定義ボタンからアクセスして、ユーザーがサイズ表記を定義できるようにします。Flannery、Area、およびRadiusの3つの方法があります。

**この機能は、以下によって開発されました：** [Vincent Mora（Oslandia）](http://www.oslandia.com/)

**この機能は以下によって資金提供されました：** [Agence de l\'eau Adour-Garonne](http://www.eau-adour-garonne.fr/)

![image29](images/entries/30f4392583400a0ed2fbdae3468265b91f39e675.webp)
### Feature：レイヤーとシンボルレイヤーのライブレイヤーエフェクト
ライブレイヤエフェクトは、レンダリングチェーンにさまざまなレンダーエフェクトを追加する機能を追加することで、QGISの広範な地図作成機能を追加します。ライブエフェクトを使用すると、シンボルの下に影を落としたり、レンダリングされたシンボルを斜めにしたりせん断したりすることができます。また、エフェクトをプログレッシブ（つまりレンダリングされた状態に適用する）か離散（ソースジオメトリをレンダリングチェーンに再注入するか）を設定することもできます。

**注**これは上級者向けの機能です。この機能を過剰に使用するとレンダリング時間が大幅に遅くなることがあるので、レイヤーごとに異なるシンボルプロファイルを使用することを検討してください。 1つはドラフトモードです。

**この機能は次の方によって開発されました:** [Nyall Dawson](http://nyalldawson.net/)

**この機能は、次の方の資金提供で作成されました:** [クラウドファンディング イニシアティブ](https://www.kickstarter.com/projects/41633306/a-christmas-gift-for-qgis-live-layer-effects-for-q)

![image30](images/entries/2ce331bd884c14764989c1bc5e3c4d1f80ec588c.webp)

{{<content-end >}}
