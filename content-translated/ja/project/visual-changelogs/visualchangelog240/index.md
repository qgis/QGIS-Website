---
HasBanner: false
draft: false
releaseDate: '2014-06-27'
section: project
sidebar: true
title: QGIS 2.4の変更履歴
type: visual-changelog

---
{{<content-start >}}
# QGIS 2.4の変更履歴{#changelog24 }
リリース日: 2014-06-27

QGIS 2.4.0の次のリリースのログを変更します。このリリースは、磨きとパフォーマンスに非常に重点を置いています。ユーザーインターフェースの一貫性とプロフェッショナルな使い方（使い勝手の良さ）を高めるために、多くの新機能、改良、強化が加えられました。コンポーザ（印刷準備マップを作成するために使用）は、大きな地図作成出力を作成するためのより実行可能なプラットフォームにするために多くの作業を行ってきました。

新しい機能がソフトウェアに追加されるたびに、新しいバグが発生する可能性があります。このリリースで何か問題が発生した場合は、 [QGISバグトラッカー](http://hub.qgis.org) にチケットを提出してください。

私たちは、開発者、ドキュメント作成者、テスター、そして時間と労力をボランティアしている（あるいは人々に資金を提供する）多くの人々に感謝したいと思います。

QGISコミュニティはあなたがこのリリースを楽しんでいただけることを希望します！あなたが時間やお金を寄付したり、QGISをより素晴らしいものにすることに関与したいなら、[qgis.org](https://qgis.org) のサイトを見て手を貸してください！

最後に、このプロジェクトに提供した貴重な財政支援について、公式スポンサーに感謝したい。
- ゴールドスポンサー: [Asia Air Survey, Japan](http://www.asiaairsurvey.com/)
- シルバースポンサー: [G.A.I.A. mbH, Germany](http://www.gaia-mbh.de/)
- シルバースポンサー: [State of Vorarlberg, Austria](http://www.vorarlberg.at/)
- ブロンズスポンサー: [www.molitec.it, Italy](http://www.molitec.it/)
- ブロンズスポンサー: [www.argusoft.de, Germany](http://www.argusoft.de)
- ブロンズスポンサー: [www.openrunner.com, France](http://www.openrunner.com)
- ブロンズスポンサー： [www.eschenlaub.de、ドイツ](http://www.eschenlaub.de)

プロジェクトに大小問わず財政的な貢献をしてくださった寄付者の最新リストは、 [寄付者リスト](http://qgis.org/ja/site/about/sponsorship.html#list-of-donors) でご覧いただけます。

寄付をすることや、プロジェクトを支援することを希望される方は、詳細について [スポンサーシップページ](https://qgis.org/en/site/about/sponsorship.html#sponsorship) をご覧ください。QGISはフリーソフトウェアであり、あなたにそうする義務はありません。QGISへのご支援は、半年ごとの開発者会議の開催、プロジェクトインフラの維持、バグ修正活動の資金として滑油尾されます。

{{<table-of-contents >}}
## 一般情報
### 機能: NetCDF EXTRA_DIM を使ったバンド名の生成
NetCDFは余分な寸法情報を提供した。この情報は、各バンドのメタデータを提供します。これらのメタデータは、各バンドの名前を説明するために使用できます。たとえば、あるNetCDFファイルのバンドは、指定された深さの温度を表します。ユーザにとっては、バンド番号だけではなく、深さ情報を使ってバンドを選択する方が簡単です。

![image1](images/entries/becafd815f152b53503b33048beb8bc95cdfdaf6.webp)
### 機能：ラスターデータにスケールとオフセットを適用する
いくつかのラスターデータソースでは、データは、メタデータ内にスケールとオフセットを持つインタージェクタとして格納されます。スケールとオフセットを使用して適切なデータを得ることができます。QGISは、その凡例、ヒストグラム、および識別のために、ラスターデータをプロバイダーにユーザーに適切な情報を適用します。

![image2](images/entries/9ec1681e4318f92a886405cf8215ec98068cf8ba.webp)
### Feature: Quick field field calc bar in attribute table
ベクター属性テーブルの計算フィールドを扱う人には、新機能があります。新しい高速計算バーを使用すると、属性テーブルの列の値をすばやく簡単に更新できます。

![image3](images/entries/386f372e4b7be45426a62005813c8d58a9a2cb43.webp)
### 機能:コンポーザと地図キャンバスにおけるカラープレビューモード
2.4に追加された、本当に革新的な機能は、グレースケールと色盲のプレビューのサポートです。これにより、色覚障害者の地図作成や地図のレイアウト、またはグレースケールで印刷された場合の地図の表示方法を視覚化することができます。この新機能の詳細は [ここ](http://nyalldawson.net/2014/05/colour-blindness-and-grayscale-previews-in-qgis-2-4/) で読むことができます。

![image4](images/entries/d3d6193f1a37c8201c9be786ef798c5419eb4c79.webp)
### 機能：QLR QGISレイヤーファイル
QGISレイヤー定義ファイルまたは単にQLRのサポートが追加されました（<http://nathanw.net/2014/03/12/qgis-qlr/> を参照）。QLRファイルは、データを指し示すファイルであり、すべてのスタイリングおよびその他の情報を含む。このファイルを追加するだけで、他のすべての魔法を実行できます。QLRを使用すると、同じレイヤーを複数のマップドキュメントに簡単に追加できます。また、設定されているすべてのプロパティを継承し、QGISでサポートされているレイヤーで動作し、特別なプラグインレイヤーが必要です。
### 機能：新しい式の関数
式ビルダーに新しい機能を追加しました.
- バウンディングボックス(境界)
- バウンディングボックスの幅と高さ（bounds_width/bounds_height）
- 最小/最大x / y座標（xmin / xmax / ymin / ymax）
- 最大/最小文字数にラップされた文字列を返す新しいwordwrap関数

![image5](images/entries/b8f4b0adf2c8f7ba8303f5aa6df8d2294a0b4c7b.webp)
### 機能：色をコピー、ペースト、ドラッグアンドドロップ
QGISの任意のカラー入力ウィジェット間で色をコピー、ペースト、ドラッグ＆ドロップできます。この新しい機能がどのように働くかについての詳細は、 この [記事](http://nyalldawson.net/2014/05/colour-shortcuts-in-qgis-2-4/) を参照してください。16進数のカラーコードとrgb文字列をカラーボタンに貼り付けて、QGISの外部からカラーをインポートすることもできます。

![image6](images/entries/d2e1cdce5ed643c88f1630fa36b667e53ec8e4de.webp)
### 機能：マルチスレッドレンダリング
これは、単にスクリーンショットで十分な評価ができない機能です - QGISはマルチスレッドレンダリングをサポートするようになりました！ つまり、地図を描くとき、QGISはCPU内のすべてのコア間で描画作業を分割し、プロセスの効率と応答性を高めます。 **応答性** とは、地図の表示が更新されるのを待つ必要がなく、再度パンまたはズームできることを意味します。 また、地図表示が段階的に更新され、図面が早期に配置されているかどうかを確認できます。 マルチスレッドレンダリングシステムのより詳細な概要は [この記事](http://www.lutraconsulting.co.uk/casestudies/qgis-multi-threaded-rendering) を見てください。 QGISの設定ダイアログには、マルチスレッドレンダリングの動作を管理できるオプションがいくつかあります。

![image7](images/entries/ebcacf7c2623f7ea3e87c929d77bfe4113c75549.webp)
## ラベリング
### 機能：複数のラベル機能
長い線（等高線や道路など）は、定期的に繰り返しラベルを付けることができるようになりました。繰り返し間隔を指定するにはmm単位と地図単位を選択できます。リリース時点では、「重複を避けるために接続された行をマージする」という設定にはまだ問題があります。

![image8](images/entries/4b996cdf33f0d18a5266e6b6053ab88d4dca9372.webp)
## マップコンポーザー
### 機能：コンポーザの写真アイテムの改良
The image item in composer is now \'atlas friendly\' - you can use an **expression to define which image** should be shown for each atlas page. You can also now set the **resize mode** (zoom, clip, stretch etc.) for the image in relation to its frame size and dimensions. You can also specify the placement of the image relative to its frame using the new **placement** item property.

![image9](images/entries/59c029be33ba4cbdf7fb48879350e699cf5f9897.webp)
### 機能:地図帳における事前定義スケールモード
When working with atlas map items, you can now specify a predefined scale mode for the map. It will use the best fitting option from the list of predefined scales in you your project properties settings (see Project -\> Project Properties -\> General -\> Project Scales to configure these predefined scales).

![image10](images/entries/45aa708b7c1ba7dd42bd71e3ee293349262853f7.webp)
### 機能:コンポーザにおける属性テーブルの改善
私たちは、コンポーザのレイアウトに表を表示する機能をいくつか改良しました。
- テーブル内の列を並べ替えるためのサポートが追加されました
- 式ベースの列のサポートが追加されました
- You can now set the alignment of individual table columns, and also specify the alignment for the table\'s header cells
- 表の内容は式でフィルタリングできます

![image11](images/entries/e39937a4b6533c14856b12d4a1064425eac52a31.webp)
### 機能：コンポーザの一般的な改善
マップコンポジションモードで作業している間、快適に過ごせるように、マップコンポーザーにはいくつかの追加があります。
- メインマップキャンバス内の現在の地図アイテムの範囲を表示するためのボタンが追加されました
- レイヤーを持つコンポーザーからSVG画像をエクスポートする機能
- スケールバーのライン結合とキャップスタイルを設定する
- アイテムフレームのライン結合スタイルの設定のサポート

![image12](images/entries/cff24f3259e286e405ca13c94fcf5e19dbe98c64.webp)
### 機能:HTMLフレームの改良
コンポーザのHTMLフレームが改良されました。複数のリンクされたフレームを手動で作成するために使用できる新しい **フレームの追加** ボタンがあります。また、改ページロジックを改良して、HTMLフレームの改ページ時にテキスト行の途中で改ページすることが少なくなるようにしました。

![image13](images/entries/792d6c3cfc682d2132caec8b6be0ce30c855e39f.webp)
## プラグイン
### 機能:メタサーチカタログクライアントプラグイン
MetaSearchは、Web（CSW）標準のOGCカタログサービスをサポートするメタデータカタログサービスと対話するためのQGISプラグインです。このプラグインは、QGIS内のメタデータカタログを検索するための簡単で直感的なアプローチとユーザーフレンドリーなインターフェイスを提供し、QGISコア製品でデフォルトで出荷されます。

![image14](images/entries/a80155cfd652a9e83c5f2564e371357a92ae115f.webp)
## シンボロジ
### 機能：シェイプバーストの塗りつぶしスタイル
We have a great new render in QGIS 2.4. The shapeburst renderer will allow you to fill polygons with a gradient extending from the line edge towards the polygon interior. You can read more about **shapeburst** [here](http://nyalldawson.net/2014/06/shapeburst-fill-styles-in-qgis-2-4/?utm_source=rss&utm_medium=rss&utm_campaign=shapeburst-fill-styles-in-qgis-2-4).

![image15](images/entries/1d85daf70119e7a58d5ef18ae5a0ac2daf18ff4f.webp)
### 機能：マーカー線の配置を移動するオプション
When using a marker line along a line or polygon edge, you can now specify an **offset** so that the marker line starts a set distance from the beginning of the line. If a marker line is set to \"first vertex\" or \"last vertex\" mode, than this offset will control how far along the line from the vertex the marker is placed.

![image16](images/entries/884f1735cee30abc7024f6fc21756b8609770173.webp)
### 機能:新しい反転ポリゴンレンダラ
ポリゴン地物に新しいレンダラが追加されました。 **ポリゴンの外部に** スタイルを適用することができます。これは、領域の強調表示や地図作成用マスクの作成に役立ちます。新しいシェイプバーストスタイルで使用すると、このエントリの画像のような出力を作成できるようになりました。

**注：** プラグインマスクの新しいバージョンは、現在選択されているマスクレイヤーを簡単に作成し、それらのエリアにラベルを付け、地図帳地図生成で自動マスクを生成するのに役立ちます。

![image17](images/entries/b58dd06d363524d112de7a40748f599730c4276e.webp)
### 機能：Spatialiteレイヤーによるスタイルの保存と復元
In the previous version was possible to save style with postgres layers, now will be possible for Spatialite layers too. This functions allow to embed different styles inside a spatialite container simplifying sharing data and their presentation. A video tutorial of this funcionality can be found here <http://pvanb.wordpress.com/2014/05/15/saving-layer-styles-to-your-spatialite-database/>

![image18](images/entries/b52c9d3fab8a6281c0e8869702328521a2445994.webp)

{{<content-end >}}
