---
HasBanner: false
draft: false
releaseDate: '2024-10-25'
section: project
sidebar: true
title: QGIS 3.40 の変更履歴
type: visual-changelog

---
{{<content-start >}}
# QGIS 3.40 の変更履歴{#changelog340 }
![](images/projects/83f1bc659777bc49e8e237625dfaa08f054e929c.png)

リリース日: 2024-10-25

QGISプロジェクトは、QGIS 3.40のリリースを喜んでお知らせします。このリリースは地理空間の専門家と愛好者の双方に向けてプラットフォームの機能を洗練させ、空間的発見のための革新的なツールでユーザーを支援するというコミットメントを強調するものです。

[QEP283](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/283) に記載されているように、このリリースではカラー管理機能に大きな進歩をもたらします。CMYKカラーサポートの導入と、さまざまなメディアタイプ間で正確な色の表現を確保するためのウィジェット、式、カートグラフィー指向のワークフローで使用するInternational Color Consortium（ICC）カラープロファイルの定義が含まれます。

また、QGISはQGISブラウザーからリモートデータソースへのアクセスを容易にするため、 [STAC](https://stacspec.org/en/) データソースとのネイティブ統合が追加されました。新しい機能により、カスタムのPyQGIS式とメソッドをプロジェクトファイルに直接保存できるようになり、データ処理においてより高い柔軟性が提供されます。この機能は自動化機能の向上にも新たな機会をもたらし、チームの生産性向上とよりシームレスなコラボレーションを促進するでしょう。

このリリースには、ラベリング、3Dビュー、ネットワーク、属性テーブルなど多数の改善を含む豊富な新機能も含まれています。

導入されたすべての新機能を手早く確認するには、 [YouTubeのハイライト動画](https://www.youtube.com/watch?v=2Pk-etS1HNo)  をご覧ください。

[![](https://img.youtube.com/vi/2Pk-etS1HNo/0.jpg)](https://www.youtube.com/watch?v=2Pk-etS1HNo)

QGISはコミュニティによる取り組みです。このリリースを実現するために時間と労力をボランティアで提供してくださった（または資金援助をしてくださった）開発者・ドキュメント作成者・テスター・その他多くの方々に心より感謝申し上げます。QGISコミュニティより、このリリースをお楽しみいただければ幸いです！QGISをさらに素晴らしいものにするために、時間・資金・その他の形でご貢献いただける方は、ぜひ [QGIS.ORG](https://qgis.org) をご覧いただき、お力をお貸しください！

QGISは寄付者およびサステイニングメンバーによって支えられています。プロジェクトに大小を問わず財政的な貢献をしてくださった寄付者の最新リストは  [寄付者一覧](https://qgis.org/en/site/about/sustaining_members.html#list-of-donors) でご覧いただけます。公式のプロジェクトサステイニングメンバーになることをご希望の方は、詳細について  [サステイニングメンバーページ](https://qgis.org/en/site/about/sustaining_members.html) をご覧ください。QGISへのスポンサーシップは、定期的な開発者ミーティングの開催、プロジェクトインフラの維持、およびバグ修正活動の資金として活用されます。現在のスポンサーの完全なリストを以下に掲載します。すべてのスポンサーの皆様に心より感謝申し上げます！

QGIS はフリーのソフトウェアです。利用する上で金銭を支払う義務はありません。実際、私たちは利用者の財政状況や社会的地位にかかわらず、より多くの人に QGIS を利用して欲しいと思っています。私たちは地理空間的な意思決定ツールによって人々が力を持つことが、全人類の社会をより良くすると信じています。
## ツール
### 機能: 識別結果でのレイヤー/プロジェクトの垂直基準の適用
ベクターレイヤーとプロジェクトに垂直基準が存在し、それらが異なる場合、識別された地物のプロジェクトの基準に変換されたZ値も含めるようになります。

![](images/entries/2249cc72d87c0b0542213451037df8bbefbad6ba.webp)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能: 情報ツールでの参照リレーションの表示
以前のQGISリリースでは、情報ツールで地物を探索する際に、参照先リレーション（現在の地物が指している関連地物）のみがユーザーに表示されていました。参照元リレーション（現在の地物が参照されている関連地物）の表示もサポートされ、任意のネスティングレベルでサポートされるようになりました。

また、識別ツールにおける関連地物の処理に対して以下を含む複数の更新が追加されました:
- 重複したリレーション参照の防止
- ノードの展開時にのみリレーションを読み込む（関連参照の読み込みの '爆発的増加' を防止）
- リレーション参照を有効または無効にする制御トグル
- ネストされた関連地物を識別ツールのコンテキストのルートに読み込むための "地物の識別" コンテキストメニューアイテム

![](images/entries/c9580e44b7f4f2ec945843c468b661ded749b8a5.webp)

This feature was developed by [Even Rouault](https://github.com/rouault)
## ユーザーインタフェース
### 機能:  属性テーブルを開く際にデフォルトですべての列を自動サイズ調整するオプション
オプションダイアログ（設定メニューから開く）のデータソースタブの新しいオプションにより、属性テーブルを開く際に常に列を内容に合わせてサイズ変更するようQGISを設定できます。

![](images/entries/eb2cc3cadf1ebb453de585e564fb0a56ff1c6ccf.gif)

This feature was developed by [Ben Wirf](https://github.com/benwirf)
### 機能: アクションダイアログの複製ボタン
レイヤープロパティのアクションダイアログに複製ボタンが追加されました。

![](images/entries/6f0479c9233e8193625e98494da97029a6d0d30b.webp)

この機能は [Speedrace4](https://github.com/Speedrace4)  によって開発されました
## シンボロジ
### 機能: ラスターレイヤーのスタイルカテゴリの提供
QGISが（以前のように単純に  `AllStyleCategories` の使用を強制するのではなく）ラスターレイヤー間のプロパティとスタイルのコピーのカテゴリをサポートするようになりました。現在、以下のラスターデータカテゴリが含まれています:
- `レイヤ設定`
- `時系列プロパティ`
- `標高属性`
- `地図のTips`
- `注意`
- `カスタムプロパティ`
- `シンボロジ`
- `レンダリング`

また、これらのスタイルはQML/SLDレイヤー定義およびスタイルファイルのインポートとエクスポート機能でもサポートされており、ラスターレイヤーの管理がベクターレイヤーのユーザーエクスペリエンスとより一貫したものになっています。

![](images/entries/0a6aeadd40690988d3560966b673045e568f86a7.webp)

この機能の開発は [Canton of Solothurn](https://so.ch/verwaltung/bau-und-justizdepartement/amt-fuer-geoinformation/) の資金提供で行われました

この機能は [Dave Signer (OPENGIS.ch)](https://opengis.ch) によって開発されました
### 機能: "線に関する参照点" シンボルレイヤータイプの追加
この新しいシンボルレイヤータイプにより、ライン上の一定間隔（または既存の頂点に対応する位置）にテキストラベルを配置できます。位置はデカルト距離を使用して計算するか、Z値/M値から補間することができます。

機能には以下が含まれます:
- ラベルは固定デカルト2D距離、ジオメトリのZ値またはM値を使用して計算した等間隔の線形補間間隔、または既存の頂点のいずれかを使用して配置できます。
- ラベルは累積距離または線形補間されたZ値/M値のいずれかを表示できます
- テキストレンダラーを使用してラベルを描画するため、ラベルに対してすべての機能（バッファー、シャドウなど）が利用できます。
- QGISの数値フォーマットクラスを使用して数値を文字列にフォーマットするため、ユーザーは小数点以下の桁数などのカスタマイズオプションを幅広く利用できます。
- オプションの "間引き間隔" 設定。設定すると、この値の倍数のラベルがスキップされます。これにより複雑なリファレンスラベルを構築できます。例えば、シンボルに2つの線形リファレンスシンボルレイヤーを持ち、1つは小さなフォントで100mごとにラベルを付け1000の倍数をスキップし、2つ目は大きな太字のフォントで1000mごとにラベルを付けるといった設定が可能です。
- ラベルはラインストリングを平均した角度を使用してレンダリングされるため、細かいギザギザによって見苦しいラベルの回転が発生しません。
- オプションとして、完全なQGISマーカーシンボルを使用してラインストリングの参照ポイントにマーカーを配置できます（これにより、例えばラベルが付いたポイントに "ルーラー" スタイルラインの交差ハッチを表示するといった使い方が可能です）。
- 配置間隔、倍数スキップ設定、マーカーの表示、平均角度計算長さのデータ定義制御

注意:
- 距離ベースの配置またはラベルを使用する場合、距離は元のレイヤーCRSに基づくデカルト計算を使用して2Dのみで計算されます。将来的には3Dデカルト距離や楕円体距離計算のオプションを公開するよう拡張できる可能性があります。

![](images/entries/ac3d8027aaa1dce55a600831bbe0a51d890f9206.webp)

この機能は [Swiss QGIS User Group](https://www.qgis.ch/de/) の資金提供で開発されました

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能: CMYKのカラーランプ補間の実装
この機能は Bordeaux Métropôle の資金提供で開発されました

This feature was developed by [Julien Cabieces](https://github.com/troopa81)
### 機能: CMYK カラープレビュー
CMYKカラーのカラープレビューは浮動小数点値のリストを使用してカラー値を表示します。

![](images/entries/bf96aab2e61c942bc43fbdab4f00d3f90ad5818d.webp)

This feature was funded by Métropôle de Bordeaux

This feature was developed by [Julien Cabieces](https://github.com/troopa81)
### 機能: 浮動小数点数によるカラーコンポーネントの選択
QGISカラーウィジェットで小数点以下2桁の浮動小数点値としてカラーコンポーネントを選択できるようになりました。

![](images/entries/ac91b68a5cbaf6376aa12091077f7b5133d2049b.webp)

この機能は Bordeaux Métropôle の資金提供で開発されました

This feature was developed by [Julien Cabieces](https://github.com/troopa81)
### 機能: バルーンコールアウトスタイルの終点マーカーシンボルの許可
バルーンコールアウトの終点の下にマーカーシンボルをレンダリングできます。バルーンコールアウトが古いアノテーションフレームワークアイテムと同じ視覚的外観を再現できるよう設計されています。

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能: マーカーシンボルのバッファー
QGISにマーカーシンボルの "バッファー" が追加されました。ラベルバッファーと同様に、マーカーバッファーはマーカーシンボルの周囲のハロー効果で、さまざまな背景に対してシンボルをより読みやすくするために設計されています。

バッファーはシンボルレベルで定義され（シンボルレイヤーごとではなく）、マーカー内のすべてのシンボルレイヤーの形状を使用して計算・描画されます。手動で同じ結果を得るには多くの重複シンボルレイヤーとそれらにまたがる重複設定が必要となるため、これにより設定が非常に簡単になります！

この変更は、ArcMapが数十年にわたってソリッドカラーマーカーの "ハロー" をサポートしてきたArcMapとQGISの間に残る（ごくわずかな！）大きなシンボロジーのギャップの1つを埋めるために設計されています。

![](images/entries/391b7def075a5dcdc026d0e625bb3f6483bc580a.webp)

This feature was funded by [North Road, thanks to SLYR](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能: QgsRasterTransparencyピクセル値のトレランスのサポート
指定されたRGB値からわずかに外れた色成分を持つピクセルも透明ピクセルとして扱えるようになります。

さまざまな色の値を透明にする必要がある写真や圧縮ラスターに役立ちます。

![](images/entries/73a7b62e6c22c27056a35c9d827f8ac3955f7b57.webp)

この機能は  [Middle Third Geological](https://www.linkedin.com/in/deryk-forster-44a415104/?original_referer=https%3A%2F%2Fwww%2Egoogle%2Ecom%2F&originalSubdomain=au) の資金提供で開発されました

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## 注記
### 機能: プロジェクト読み込み時のSVGおよびテキストアノテーションのアノテーションレイヤーアイテムへの自動アップグレード
古いアノテーションアイテムを持つプロジェクトのワークフローを改善しました。以前のQGISバージョンでは、古いアノテーションアイテム（テキスト、HTML、SVG、フォーム）が新しいフレームワークに移植されておらず、ワークフローに影響を与えていました。3.40では優先度の高いテキストとSVGのアイテムを対象とし、フレームワークが更新されて不足していた機能が追加されました。古いプロジェクトを読み込む際、古いSVGおよびテキストアノテーションは自動的に（通知なく）新しい画像および矩形テキストアノテーションアイテムタイプに変換されます。
- その過程でさまざまなバグが修正され、以下の追加機能が追加されました:
- ポイントのテキスト、矩形テキスト、画像アノテーションを含むアノテーションのコールアウト。
- "balloon" コールアウトスタイルの一部として描画されるマーカーシンボル
- アノテーション用 “visibility layer”  の関連付け
- ポイントのテキストと矩形テキストのHTMLコンテンツをインタラクティブに作成するためのリッチテキストエディターウィジェット
- UI の整理

この機能は [QGIS Grant Programme 2024](https://github.com/qgis/PSC/issues/60) の資金提供で開発されました

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能: ポイントテキスト、矩形テキスト、画像アイテムへのコールアウトサポートの追加
テキストをマップの位置にリンクするコールアウトライン（またはバブルコールアウト）を作成できます。コールアウトを作成するには、ユーザーはテキストアイテムを選択し、中央のxノードをドラッグして目的のコールアウト終点まで引き出します。

コールアウトスタイルはレイヤースタイリングパネルから変更できます。

![](images/entries/87e3c18cbb4eb5bdb2ee4a2a690ffbb1f6ae2bde.webp)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能: アノテーションレイヤーのリンクレイヤーオプションの追加
 [QEP\#269](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/269) に沿って、アノテーションレイヤーのレンダリングページに新しい "リンクレイヤー" 設定が追加されました。これにより、ユーザーはアノテーションレイヤーにリンクする表示レイヤーをオプションで設定できます。設定すると、リンクされたレイヤーがマップで表示されている場合にのみアノテーションが描画されます。

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能: ピクチャーアノテーションアイテムタイプの追加
SVGまたはラスター画像をアノテーションレイヤーのアイテムとしてレンダリングできます。以下のオプションがあります:
- ピクチャーのアスペクト比のロック
- 背景シンボルを使用した描画
- 枠線シンボルを使用した描画
- リンクまたは埋め込み画像
- スケール依存サイズまたは固定サイズでのレンダリング

![](images/entries/14d168314617843058d4cfe38b8c15abb96114b4.webp)

This feature was funded by [North Road](https://north-road.com)

この機能は [Nyall Dawson (North Road)] (https://north-road.com) によって開発されました
## ラベリング
### 機能: HTMLラベルでの水平配置のサポート
複数行のラベルで、以下のいずれかを使用できます:
- HTML アトリビュート
- CSS "text-align: xxx"
- HTML のテキストタグ

サポートされている配置は左揃え、右揃え、中央揃え、均等割り付けです。

水平配置はHTMLテキストがレンダリングされるすべてのコンテキストで使用できます。ただし曲線ラベルは除きます（1行テキストに制限されるため）。

この機能は City of Freiburg im Breisgau によって資金提供されました

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能: HTMLラベルでのHTMLヘッダーフォーマット
HTMLラベルでヘッダータグ（h1/h2/.../h6）および関連するフォーマットがサポートされるようになりました。

この機能は City of Freiburg im Breisgau によって資金提供されました

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能:  HTMLラベルでの word-spacing CSSのサポートの追加
HTMLラベルおよびHTMLテキストフォーマットが受け入れられるその他の場所で word-spacing CSSのサポートがQGISに追加され、"word-spacing: 12" のようなCSSルールを使用してHTMLテキストの一部の単語間隔を増やすことができるようになりました。単語間隔は常にポイント単位として扱われます。

この機能は City of Freiburg im Breisgau によって資金提供されました

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能: ラベリングエンジンルールの実装
[QEP\#299](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/299) に沿って、プロジェクトに高度なラベリングエンジンルールを設定するための新しいAPIフレームワークが実装され、4つの初期ルールタイプが実装されました:
- QgsLabelingEngineRuleMinimumDistanceLabelToFeature: 別レイヤーの地物にラベルが近づきすぎることを防ぎます。
- QgsLabelingEngineRuleMaximumDistanceLabelToFeature: 別レイヤーの地物からラベルが離れすぎることを防ぎます。
- QgsLabelingEngineRuleMinimumDistanceLabelToLabel: 別レイヤーのラベルにラベルが近づきすぎることを防ぎます。
- QgsLabelingEngineRuleAvoidLabelOverlapWithFeature: 別レイヤーの地物にラベルが重なることを防ぎます。

注意 最初の3つのルールはGEOS 3.10以上に基づくビルドが必要であり、古いGEOSビルドでは利用できません。

利用可能なルールクラスを保存するレジストリと、QGISプロジェクトでのルールと設定のシリアライズも実装されました。

![](images/entries/f65ac82ccaa14f9017904db8badb25afc6e87bc5.webp)

この機能は Rubicon Concierge Real Estate の資金提供で開発されました

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### 機能: HTMLラベルテキストでのimgタグのサポート
HTMLラベルコンテンツでimgタグの使用が可能になります。以下のロジックが適用されます:
- 画像パスは src="xxx" 属性で設定します。ローカル、HTTP、base64エンコードされたパスが許可されています。
- QGISが読み込める任意の画像フォーマットを使用できます。
- 画像サイズは width="\#\#" および height="\#\#" 属性で指定できます。幅または高さが指定されていない場合は、元の画像サイズから自動的に計算されます。
- 幅または高さが指定された場合、それらはポイント単位として扱われます。
-  CSSのwidth/height設定は無視されます（Qtの制限による）。
- 曲線テキストラベルでは画像はサポートされていません。
- 画像はインライン配置のみで、フローティング画像はサポートされていません。

この機能は City of Freiburg im Breisgau によって資金提供されました

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## ダイアグラム
### 機能:スタックダイアグラムの導入
スタックダイアグラムは、単一の地物に対して複数の隣接した（水平または垂直に）スタックされた "サブダイアグラム" を構造化する方法を提供し、人口ピラミッドなどの複雑なダイアグラムオブジェクトを作成するための方法を提供します。

この実装ではスタックダイアグラムとサブダイアグラムの設定のための複数の新しい設定が導入され、ダイアグラム設定のモーダルダイアログがスタイリングドックウィジェットに移行されました。

![](images/entries/798c8f7ffe9acd928e7df5820212b39f22ef42fd.webp)

この機能は [Landesamt für Vermessung und Geoinformation (LVG) Vorarlberg in collaboration with the QGIS user group Switzerland.](https://vorarlberg.at/-/landesamt-fuer-vermessung-und-geoinformation-l-1) の資金提供によって開発されました

This feature was developed by [Germán Carrillo](https://github.com/gacarrillor)
## メッシュ
### 機能: Quantized Meshレイヤーを追加するGUIの追加
QGISブラウザーパネルおよびデータソースマネージャーでQuantized Meshデータソースとレイヤーを読み込むための新しいGUI要素が提供されました。

![](images/entries/9873b9077c396a54266bed908c8b68a46e5ecd5c.webp)

この機能はスイスQGISユーザーグループによって資金提供されました

この機能は [David Koňařík](https://github.com/dvdkon) によって開発されました
## レンダリング
### 機能: ベクタータイルの複数ソースのサポート
単一のスタイル定義内に複数のソース/URLを含むベクタータイルを読み込むためのQGISの機能が拡張されました。

![](images/entries/c52b6dfb4751aed9c39b719d8d4c44c3eaec3a32.webp)

This feature was developed by [Denis Rouzaud](https://github.com/3nids)
## 三次元機能
### 機能: 3Dマップビューでのベクターレイヤーの垂直CRS設定の適用
プロジェクトに非地理的2D CRSと垂直CRSが設定されている場合、レイヤーレベルの垂直CRS設定が3Dマップビューで適用されます。

注 これは新しく作成された3Dマップビューにのみ影響し、既存の3Dマップビューのユーザーが変更できるCRS設定は現在公開されていません。

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能: 3Dシーンのクリップ距離
3Dビューで  `gl_clipistance` を設定する新しいオプションにより、指定した範囲外の地物頂点が適切にフィルタリングされ、複数の平面でビューを効果的にトリミングします。

この設定は `Qgs3DMapScene` オブジェクトの `enableClipping()` および `disableClipping()`メソッドで制御されます。

![](images/entries/4ec6126f373e56755809edbabc74b0cd5a5ee160.webp)

This feature was developed by [Jean Felder](https://github.com/ptitjano)
## 印刷レイアウト
### 機能: 手動テーブルでのセルの結合サポートの追加
レイアウトの手動テーブルアイテムで隣接するセルを結合できるようになります。

テーブルエディターで複数のセルを矩形状に選択し、テーブルメニューから "選択したセルを結合" をクリックします。結合されたセルは "選択したセルを分割" メニューアクションで元に戻すことができます。

![](images/entries/12309cc445c6d00d56ef0f724be0828bb3e094d0.webp)

この機能は FLYGHT7 の資金提供で開発されました

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能: 有効なPDF/X-4ファイルの生成
[QEP\#283](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/283) に沿って、カラースペースが設定されている場合、QGISは有効なPDF/X-4ファイルを生成します。

この機能は Bordeaux Métropôle の資金提供で開発されました

This feature was developed by [Julien Cabieces](https://github.com/troopa81)
### 機能: アイテムのジオスペシャルPDFグループ名を設定するオプションの追加
レイアウトアイテムの "レンダリング" セクションにあるこの新しい設定により、ジオスペシャルPDFエクスポートで使用するオプションの "グループ名" を設定できます。設定すると、エクスポートされたジオスペシャルPDFに対応するレイヤーツリーグループが作成され、このグループがチェックされている場合にのみアイテムが表示されます。

これにより、ジオスペシャルPDFの閲覧者がグループとしてコンテンツを選択的に表示できるようになります。例えば、説明ラベルや凡例などの追加レイアウトコンテンツをグループのレイヤーが表示されている場合にのみ表示させることができ、ジオスペシャルPDFのエクスポートをより柔軟なものにします。

![](images/entries/a0f64c99c2a62dee9681d01dec7a39d991377a85.webp)

This feature was funded by Rubicon Concierge Real Estate Services

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能: レイアウトのメインメニューへのページプロパティの追加
印刷レイアウトインターフェースのメインメニューにページプロパティを開くメニューオプションが追加されました。
 
 
 
 
 
 

![](images/entries/44407afcb40294680e8aad845bb2cf0060cfe034.webp)

この機能は [Vedran Stojnović](https://github.com/phidrho) によって開発されました
### 機能: レイアウトスケールバーのスケール方法オプションの追加
印刷レイアウトでのマップスケール計算方法をユーザーが定義して選択するための新しいオプションが提供されます。スケール計算のオプションが公開されます:
- 地図の下部分の縮尺
- 地図の中央の縮尺
- 地図の上部分の縮尺
- 上・中・下の縮尺の平均

デフォルトでは、新しいスケールバーは（以前使用されていた "地図の下部分の縮尺" の方法の代わりに）平均方法を使用します。これにより、マップの上部または下部のスケールが計算できないシナリオ（例：マップの上部または下部がマップCRSの有効エリア外に位置する場合）をより適切に処理できます。

![](images/entries/ff809eacb3e8701d38d43292ae3d5694cb16076d.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## 計算式
### 機能:  'カスタム式 ' 数値フォーマットの追加
この数値フォーマットにより、ユーザーが数値をフォーマットするカスタムQGIS式を作成できます。式では @value 変数を使用してフォーマットする値を取得し、標準のQGIS式関数を使用して任意の形式にフォーマットできます。

レイアウトスケールバー、標高プロット、レイアウトテーブル、カラーランプ凡例など、QgsNumericFormat が受け入れられる任意の場所で使用できます。

この機能はスイスQGISユーザーグループによって資金提供されました

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Add line\_interpolate\_point\_by\_m and line\_locate\_m expressions
Two new functions are provided to the expression engine to work with M values along line strings:
- `line_interpolate_point_by_m`: returns a point geometry of a matching m value interpolated along a line containing an m dimension.
- `line_locate_m`: returns a distance from the beginning of a line where a matching m value was found.

These functions are useful when working with temporal data (such as a linestring representing a GPS track, where the M value represents the epoch value), and can be used effectively alongside the temporal controller to create beautiful animations that were previously harder to unlock.

![](images/entries/43d4feab4f7d4fb0fe167c7120b19a7cae13fc47.webp)

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### Feature: Extended color value support
In line with [QEP\#283](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/283), new expression functions allow for the retrieval of colors that include:
- color\_rgbf
- color\_cmykf
- color\_hsvf
- color\_hslf

These functions differ from the existing color retrieval expression functions (e.g. color\_rgb) by returning color values with different internal data types. This improves performance and fidelity by avoiding unnecessary color conversions in specific contexts, such as writing PDFs with native CMYK colors derived from expression values.

この機能は Bordeaux Métropôle の資金提供で開発されました

This feature was developed by [Julien Cabieces](https://github.com/troopa81)
### Feature: Allow users to save expression functions in QGIS project file
A new `[Project Functions]` element is now available within the expression builder dialog, allowing QGIS to store custom user-defined functions embedded in the project file.

This reduces the need to manually share Python code snippets and copy them to the user profile directory or import them into the expression builder dialog.

Project functions are unloaded when a project is closed, and user functions are reloaded to avoid any potential overwrite by activated project functions.

For security reasons, the handling of whether to load or not load these functions on project startup is configurable in the user settings with the same rationale used for managing project macros.

![](images/entries/fb459ca9362a65771713ed9b571b12a265e0b45d.webp)

This feature was funded by [the QGIS user group Switzerland](https://qgis.ch)

This feature was developed by [Germán Carrillo](https://github.com/gacarrillor)
### Feature: Add info about usable "expression dialect" to filter dialog
The query builder used for entering filter expressions on vector layers now shows the supported expression dialect.

![](images/entries/1bd0096fbd0fac4d612b2ca98bc7ef86cedac36e.webp)

This feature was funded by WhereGroup GmbH.

This feature was developed by [Hannes](https://github.com/kannes)
### Feature: Add project\_color\_object and ramp\_color\_object functions
In line with [QEP\#283](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/283), new expression functions provide support for setting project and ramp colors using CMYK color values using expressions

This feature was funded by Bordeaux Metropole

This feature was developed by [Julien Cabieces](https://github.com/troopa81)
## デジタイズ
### Feature: Add circles intersection digitizing tool
A new advanced digitizing tool allows users to pick/ digitize a point at the intersection of two circles

To support this functionality, the QGIS API has been extended with a new abstract class for supporting similar "COGO" development in the future, as well as providing Python bindings for developing advanced digitization utilities and plugins.

![](images/entries/990ee4bd78f0d0732ca02562ce953bed4c9443a8.webp)

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### Feature: Visual construction guides for advanced digitizing
Visual construction guides have been added to the advanced digitizing dock widget, which builds on the existing CAD construction mode.

When recording construction guides, QGIS will render all construction steps taken as dashed lines which will remain visible for as long as advanced digitizing is enabled. The guides are snap-able, allowing for construction steps to begin mid-way into a previous set of steps too.

The construction guides are stored in a vector layer, which is exposed through the advanced digitizing dock widget, allowing for further customization of the guides via other application processes, such as Python plugins.

![](images/entries/d77759a3bc23a050b3e8e9cc5a5d3bb5cc91dff3.webp)

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
## データ管理
### Feature: Allow setting VSI credentials when loading OGR/GDAL layers
VSI credential options are now exposed for user control when adding OGR vector/GDAL raster layers from the Data Source Manager, allowing users to define credentials on a per-layer basis for layers retrieved from cloud services (rather than use a single set of credentials for an entire QGIS session using an environment variable or similar approach).

Requires GDAL 3.5+

![](images/entries/e824e2a5aef50de87656d6beced8ea0ae0f60e41.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## フォームとウィジェット
### Feature: Allow reordering fields in new vector layer dialogs
When creating a new vector layer, including scratch, shp, gpkg, and spatialite, users will now be able to reorder the field definitions.

![](images/entries/3623fff590c84705c9e75fa22c3e0cc9c537c9e0.webp)

This feature was funded by QGIS User Group Denmark

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Add metadata setting to override widget wrapper used for a parameter
While it was possible to add new widget wrappers for Processing parameters, it was not possible to override the standard widget wrappers defined for each parameter type.

A new parameter metadata setting for "widget\_type" has been added, which provides developers to override the standard widget wrapper for a parameter for more control of application dialogues.

`param.setMetadata( } )`

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
## プロセシング
### Feature: Open file or URL Algorithm
A simple native algorithm has been added to allow for the opening of local files using the corresponding system programs, or URLs in a web browser.

Useful in combination with the Download File Algorithm to open the resulting file, or to display results after models triggering external systems.

![](images/entries/2ab9a02e47e9d3dc7a0c4e1dc5f65d195244869b.webp)

この機能の開発は [Canton of Solothurn](https://so.ch/verwaltung/bau-und-justizdepartement/amt-fuer-geoinformation/) の資金提供で行われました

この機能は [Dave Signer (OPENGIS.ch)](https://opengis.ch) によって開発されました
### Feature: Add processing parameter types for Area and Volume
Adds dedicated parameter types for Area and Volume values.

Modeled closely off the existing Distance parameter type.

![](images/entries/8324f615ac89f6d617619f34f6cc37ee2ae55a2a.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Updated "Vector information" algorithms
The GDAL Processing algorithm for vector information has been modified to support additional command-line parameters, and a new **Vector information (JSON)** algorithm is provided that will use the [`-json`](https://gdal.org/programs/ogrinfo.html#cmdoption-ogrinfo-json) option of ogrinfo to create a JSON file output containing the layer or dataset information.

![](images/entries/b890a9ff0af7e1ef313c620c48150f871f1177f0.webp)

This feature was developed by [Andrea Giudiceandrea](https://github.com/agiudiceandrea)
### Feature: Allow adding Processing tools to Favorites
New 'Favorites' functionality has been added for Processing alogrithms, allowing users to statically pin their chosen algorithms to a dedicated section at the top of the toolbox for ease of access.

![](images/entries/2108d8a4104ef9d50f44a72171274469bde1e429.webp)

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
### Feature: Add creation options support to some native raster Processing algorithms
More raster creation options have been added to native Processing algorithms for more control of the output format (compression level, world file generation etc.). Affected algorithms include:
- セル統計量
- Constant raster
- Export mesh
- nodata値を内挿値で埋める
- Fuzzify raster
- 線密度
- ランダムラスタの出力
- DTMフィルタ（傾斜ベース）
- ラスタスタックの値の一致頻度
- Raster boolean AND/OR
- Raster stack position
- Reclassify
- Rescale
- Round

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
### Feature: Support drag and drop for multi-layer parameters
Allows dragging and dropping layers from either the QGIS browser or file explorer onto any multiple-layer parameter panel. Handy when you have to add many layers and it's simpler to make a selection outside of the processing dialog.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## アプリケーションとプロジェクトのオプション
### Feature: Smart cache size implementation
QGIS now has improved handling of its network disk cache by leveraging smart cache size logic currently utilized by modern web browsers.

This allows the cache to dynamically resize based on available storage space on the cache disk, and will result in most users getting a larger cache size (and improved network performance) by default as well as limiting loads to external providers and XYZ tile services.

Users can disable the smart cache size logic in favor of a static cache size using the updated Options dialog.

![](images/entries/80e1931b0152bfe035105520396a775b6f9bfbaf.webp)

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### Feature: Add vertical CRS selection widget to vector layer properties
Vector layers can now include discrete settings for configuring the vertical reference system.

Application behavior for the definition of vertical reference on a layer will follow the same behavior as the project settings, namely:
- If the layer has a 3D CRS set, then the widget is disabled with an explanatory note
- If the layer has a 2D CRS set, then the user can select the appropriate vertical CRS

An explanatory note is included which details the facets of the application where the vertical CRS settings are respected, along with a warning for users to note that plugins and other tools may not respect the layers' vertical CRS configuration.

![](images/entries/54fd7f19dfda59d13b32525efe28d75af4f72adc.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Project color mode properties widget
Project properties configuration widgets have been added for managing color modes and color profiles at the project level.

When loading an ICC profile, QGIS will enforce consistency between the color model and color space.

**The ICC profile widget part is not visible unless QGIS is built with Qt 6.8.0 or greater**

![](images/entries/c763da512666981c58d3fe8b5dbfa5982ff53d4b.webp)

This feature was funded by Bordeaux Métrôpole\*\*

This feature was developed by [Julien Cabieces](https://github.com/troopa81)
## Profile Plots
### Feature: Change elevation profile name
A "Change Profile Name" menu item in the Options sub-menu of the Elevation Profile widget has been added that allows the user to change the name of the profile window.

![](images/entries/81d350164ce88101c33692b9665063970ce72791.webp)

This feature was developed by [Simon](https://github.com/Simon-Lopez)
### Feature: Ensure vector layer elevation profiles respect layer/map vert datums
When the map and/or layer has a vertical reference (3D CRS) configured it will be respected within profile plots

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## ブラウザ
### Feature: add UX to load MVT layers from style URL only
If a tile vector layer is created with a style URL but not source, the style is fetched and sources are extracted from it.

Here is a demo with a layer having two sources: https://vectortiles.geo.admin.ch/styles/ch.swisstopo.lightbasemap.vt/style.json

https://github.com/user-attachments/assets/948db86c-e79f-40cd-9060-6bc84a31fc2a

This feature was developed by [Denis Rouzaud](https://github.com/3nids)
### Feature: Add duplicate functionality to Browser connection items
QGIS now includes a "Duplicate connection" action in the context menu of Browser connection items. This allows users to quickly make a copy of a connection to the same data source when only a few details differ (for example, a different PostGIS database on the same server).

![](images/entries/44b28c871c4d86b6f2c52b326fea88b7e8c1c24e.webp)

This feature was funded by [NaturalGIS](https://www.naturalgis.pt/)

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
### Feature: Adjust "Create Database" context menu actions on GeoPackage
In previous versions of QGIS, creating a new SpatiaLite database with this action would create an empty database and add a new connection to the browser, while the same action executed for GeoPackage files would generate a database with a layer.

New actions for "Create Database" and "Create Database and Layer" have been added for more explicit and consistent database creation options.

![](images/entries/0473ab08a8dd2cae040855020d570535088c4268.webp)

This feature was funded by [NaturalGIS](https://www.naturalgis.pt)

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
### Feature: Add connections to cloud storage providers to browser
QGIS now natively supports the storing and browsing cloud storage connections within the QGIS browser panel. GDAL supported vector and raster data sources can be loaded directly from cloud providers and all GDAL VSI cloud handlers are supported including (S3, Azure, Google Drive, etc.)

Connections can also be created, modified, removed, and exported/imported to/from XML files.

![](images/entries/e6758adb24f9db8651516fc25ae8eac0670988bd.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: STAC integration
Part one of the [QEP300](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/300) implementation has been completed, allowing users to handle STAC catalogs and elements natively within QGIS using the browser.

A new STAC entry on the browser allows users to connect to static catalogs and STAC API endpoints.

STAC Items that contain cloud-optimized assets (e.g. COG, COPC, EPT) can be added as map layers via the drag-and-drop action.

A Download Assets dialog is provided in the STAC context menu that allows saving items to local storage.

All Catalog, Collection, and Item properties can be examined using the STAC Object Details dialog.

![](images/entries/c6899bc85d87fc36edba1bb71c4613e4b68a6cbe.gif)

This feature was developed by [Stefanos Natsis](https://github.com/uclaros)
## データプロバイダ
### Feature: Support for polyhedral surface and TIN
QGIS now supports the `POLYHEDRALSURFACE` and `TIN` simple features by introducing new geometry types for `QgsPolyhedralSurface` and `QgsTriangulatedSurface`:
- `QgsPolyhedralSurface` inherits from `QgsSurface`
- `QgsTriangulatedSurface` inherits from `QgsPolyhedralSurface` as a special case which only contains triangles.

This functionality removes the need for previously used workarounds, such as: - TIN is now the multipart of a triangle - There is no need to convert a polyhedral surface or a TIN to a multipolygon when importing these data types from PostGIS.

This feature was funded by CEA/DAM, CP4SC, Oslandia

This feature was developed by [Jean Felder](https://github.com/ptitjano)
## QGISサーバー
### Feature: WFS title definition for layers
Implemented to service [\#55317](https://github.com/qgis/QGIS/issues/55317), layers now have an additional WFS Title server metadata property to allow users to differentiate between different layer collections on layers served via WFS with QGIS Server.

This feature was developed by [Jürgen Fischer](https://github.com/jef-n)
## プログラム可能
### Feature: Exceptions raised on QgsDistanceArea methods
A QgsCsException is now raised when errors occur within QgsDistanceArea methods to prevent misleading analysis results and properly handle error propagation throughout the application

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Convert QgsRasterLayer to NumPy Array
Developed in partial fulfillment of [QEP 227](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/227), QGIS now includes a new `as_numpy` method on `QgsRasterLayer` objects in PyQGIS which allow for the easy conversion of a raster layer to NumPy array for improved integration processes and improved analysis of raster data using NumPy (Note that the NumPy library is an optional dependency not shipped with the QGIS Application).

This feature was developed by [Till Frankenbach](https://github.com/merydian)
### Feature: Convert QgsGeometry to Shapely and NumPy
Developed in partial fulfillment of [QEP 227](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/227), QGIS now includes `as_numpy` and `as_shapely` methods on `QgsGeometry` objects in PyQGIS which allow for the easy conversion of a geometry to a (list of) NumPy array(s) or Shapely object(s) for improved integration processes (Note that the relevant libraries are optional dependencies not shipped with the QGIS Application).

This feature was developed by [Till Frankenbach](https://github.com/merydian)
## 注目すべき修正
### Feature: Bug fixes by Even Rouault (Spatialys)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.34 backport commit (GitHub) |
| --- | --- | --- | --- |
| Export of geopackage to File Geodatabase creates fid type real causing subsequent vector conversions to fail | [#58690](https://github.com/qgis/QGIS/issues/58690) | [PR #58705](https://github.com/qgis/QGIS/pull/58705) | N/A |
| In QGIS 3.38.2 when deleting an attribute from a gdb file, all the fields in the remaining attributes get deleted as well | [#58669](https://github.com/qgis/QGIS/issues/58669) | [PR #58733](https://github.com/qgis/QGIS/pull/58733) | [PR #58769](https://github.com/qgis/QGIS/pull/58769) |
| test_provider_ogr.py: do not alter source test data, to keep 'git status' clean | 未報告 | [PR #58734](https://github.com/qgis/QGIS/pull/58734) | N/A |
| GeoJSON: edits are not saved | [#58261](https://github.com/qgis/QGIS/issues/58261) | [GDAL PR 10794](https://github.com/OSGeo/gdal/pull/10794) | N/A |
| GeoJSON: edits are not saved | [#58261](https://github.com/qgis/QGIS/issues/58261) | [PR #58740](https://github.com/qgis/QGIS/pull/58740) | N/A |
| In Qgis 3.34.4 Saving vector Temporary Scratch Layer as GeoJSON - Newline Delimited leads to Unavailable Layer! error | [#58760](https://github.com/qgis/QGIS/issues/58760) | [PR #58768](https://github.com/qgis/QGIS/pull/58768) | [PR #58771](https://github.com/qgis/QGIS/pull/58771) |
| parquet file exported from QGIS causes crash when loaded into a project | [#58086](https://github.com/qgis/QGIS/issues/58086) | [GDAL PR 10815](https://github.com/OSGeo/gdal/pull/10815) | N/A |
| In Qgis 3.34.4 / 3.38.3 vector layer saved as KML does not allow deleting of polygon features | [#58780](https://github.com/qgis/QGIS/issues/58780) | [GDAL PR 10840](https://github.com/OSGeo/gdal/pull/10840) | N/A |
| Layer user notes only available for QgsVectorLayer when reading a project with flag QgsProject.FlagDontResolveLayers | [#58818](https://github.com/qgis/QGIS/issues/58818) | [PR #58835](https://github.com/qgis/QGIS/pull/58835) | N/A |
| QgsJsonExporter layer field with ValueMap | [#58861](https://github.com/qgis/QGIS/issues/58861) | [PR #58864](https://github.com/qgis/QGIS/pull/58864) | N/A |
| Geospatial PDF Export for Rasters does NOT work | [#58891](https://github.com/qgis/QGIS/issues/58891) | [PR #58895](https://github.com/qgis/QGIS/pull/58895) | [PR #58903](https://github.com/qgis/QGIS/pull/58903) |
| QGIS not recognizing CRS "EPSG:3301 - Estonian Coordinate System of 1997" in MapInfo mid/mif and tab formats | [#58283](https://github.com/qgis/QGIS/issues/58283) | [GDAL PR 10920](https://github.com/OSGeo/gdal/pull/10920) | N/A |
| Don't use the The Word Which Must Not Be Used | Unreported (well, through hostile channels) | [PR #59017](https://github.com/qgis/QGIS/pull/59017) | N/A |
| In Qgis 3.34.4 / 3.38.3 vector layer saved as KML does not allow deleting of polygon features | [#58780](https://github.com/qgis/QGIS/issues/58780) | [GDAL PR 10991](https://github.com/OSGeo/gdal/pull/10991) | N/A |
| [BUGFIX] [PostgreSQL] Properly take into account 'name' type | 未報告 | [PR #59147](https://github.com/qgis/QGIS/pull/59147) | TODO |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Even Rouault (Spatialys)](https://www.spatialys.com/)
### Feature: Bug fixes by Alessandro Pasotti (itOpen / qcooperative)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.34 backport commit (GitHub) |
| --- | --- | --- | --- |
| QGIS Server filter does not work as expected for intersection filters | [#58220](https://github.com/qgis/QGIS/issues/58220) | 再現できません |  |
| [Layout] Missing atlas layer attributes in expression "Fields and Values" group for fixed table item | [#58774](https://github.com/qgis/QGIS/issues/58774) | [PR #58778](https://github.com/qgis/QGIS/pull/58778) | No |
| Clearing the default value expression cannot be canceled / undone | [#58767](https://github.com/qgis/QGIS/issues/58767) | [PR #58787](https://github.com/qgis/QGIS/pull/58787) | No |
| PostgreSQL authentication gets back to basic if a layer is opened with "execute SQL" from QGIS explorer panel | [#58784](https://github.com/qgis/QGIS/issues/58784) | 再現できません |  |
| QGIS Server: fixed width of 200 px of cascaded WMS layer legends | [#57422](https://github.com/qgis/QGIS/issues/57422) | [PR #58790](https://github.com/qgis/QGIS/pull/58790) | No |
| Random Points in Polygons behaves unexpectedly | [#58737](https://github.com/qgis/QGIS/issues/58737) | [PR #58815](https://github.com/qgis/QGIS/pull/58815) | No |
| When using a computed or virtual field that refers to other layers's fields having the same name, the wrong value is returned | [#49469](https://github.com/qgis/QGIS/issues/49469) | [PR #58819](https://github.com/qgis/QGIS/pull/58819) | TODO |
| QGIS can't search for PostGIS elsewhere than in the public schema | [#58577](https://github.com/qgis/QGIS/issues/58577) | Not a bug (closed by OP) |  |
| Advanced digitizing using meters instead of ft if ft are set as default unit | [#58620](https://github.com/qgis/QGIS/issues/58620) | [PR #58844](https://github.com/qgis/QGIS/pull/58844) | queued |
| In layer Filter "lower" function not working with diacritical marks | [#58893](https://github.com/qgis/QGIS/issues/58893) | 再現できません |  |
| Delete expression in Default value + click on another field in the attribute form manager = Crash | [#58887](https://github.com/qgis/QGIS/issues/58887) | [PR #58911](https://github.com/qgis/QGIS/pull/58911) | N/A |
| Deleting "all other values" breaks categorised symbology | [#58875](https://github.com/qgis/QGIS/issues/58875) | [PR #58916](https://github.com/qgis/QGIS/pull/58916) | queued |
| SLD, Server - Service=WMS&Request=GetStyles: LabelPlacement/Displacement malfunction | [#58862](https://github.com/qgis/QGIS/issues/58862) | [PR #58945](https://github.com/qgis/QGIS/pull/58945) | queued |
| Creating table on MSSQL sets varchar and nvarchar column lengths as 1 regardless of UI input | [#58809](https://github.com/qgis/QGIS/issues/58809) | [PR #58955](https://github.com/qgis/QGIS/pull/58955) | queued |
| Unwanted unique constraint added when exporting to geopackage, if not null constraint is applied via default style | [#58431](https://github.com/qgis/QGIS/issues/58431) | [PR #58986](https://github.com/qgis/QGIS/pull/58986) | Risky? |
| Georeferencer is not using locale in GCP table | [#58765](https://github.com/qgis/QGIS/issues/58765) | [PR #59025](https://github.com/qgis/QGIS/pull/59025) | queued |
| Basic editing using "Automatic Transaction Groups" generates a critical error | [#58845](https://github.com/qgis/QGIS/issues/58845) | [PR #59076](https://github.com/qgis/QGIS/pull/59076) | queued |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Alessandro Pasotti (itOpen / qcooperative)](https://www.qcooperative.net/)
### Feature: Bug fixes by Julien Cabieces (Oslandia)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.34 backport commit (GitHub) |
| --- | --- | --- | --- |
| Repeated Crash when using Reshape Feature Tool | [#57225](https://github.com/qgis/QGIS/issues/57225) | [PR #58779](https://github.com/qgis/QGIS/pull/58779) | [PR #58792](https://github.com/qgis/QGIS/pull/58792) |
| pyqt5_to_pyqt6.py fails on infinite recursion | [#58659](https://github.com/qgis/QGIS/issues/58659) | [PR #58785](https://github.com/qgis/QGIS/pull/58785) | No |
| Legend in map atlas anchored to bottom left or bottom right will not correctly reposition in PDF | [#37566](https://github.com/qgis/QGIS/issues/37566) (Regression) | [PR #58798](https://github.com/qgis/QGIS/pull/58798) | [PR #58920](https://github.com/qgis/QGIS/pull/58920) |
| Calling several times waitForFinished on task would cause a deadlock | 未報告 | [PR #58799](https://github.com/qgis/QGIS/pull/58799) | No |
| Debian sid Qt6 compile fails on sip build, python bindings | [#57760](https://github.com/qgis/QGIS/issues/57760) | Now working with updated debian |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Julien Cabieces (Oslandia)](https://oslandia.com/)
### Feature: Bug fixes by Nyall Dawson (North Road)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.34 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fix rendering of line direction symbols in labels, cleanup label rendering code a bit | [#59107](https://github.com/qgis/QGIS/issues/59107) | [PR #59114](https://github.com/qgis/QGIS/pull/59114) | N/A |
| [gps] Be tolerant to talker IDs which don't start with 'G' | Reported privately | [PR #59124](https://github.com/qgis/QGIS/pull/59124) | N/A |
| Fix unsafe use of QgsProject::instance from vector layer classes | 未報告 | [PR #59118](https://github.com/qgis/QGIS/pull/59118) | Too risky |
| When excluding tests, only exclude exact matches | 未報告 | [PR #59116](https://github.com/qgis/QGIS/pull/59116) | N/A |
| When layout scalebar settings are invalid, show warning message | 未報告 | [PR #59088](https://github.com/qgis/QGIS/pull/59088) | N/A |
| Many cppcheck fixes to get CI green again | Mark all bool operators as explicit, associated fixes | [PR #59086](https://github.com/qgis/QGIS/pull/59086) | N/A |
| Fix random crashes | [#36125](https://github.com/qgis/QGIS/issues/36125) | [PR #59080](https://github.com/qgis/QGIS/pull/59080) | [PR #59087](https://github.com/qgis/QGIS/pull/59087) |
| Optimise grid decoration rendering | Reported privately | [PR #59044](https://github.com/qgis/QGIS/pull/59044) | N/A |
| Optimise text rendering for a common scenario | Reported privately | [PR #59037](https://github.com/qgis/QGIS/pull/59037) | N/A |
| Don't override cursor in pin labels map tool | [#59016](https://github.com/qgis/QGIS/issues/59016) | [PR #59033](https://github.com/qgis/QGIS/pull/59033) | [PR #59035](https://github.com/qgis/QGIS/pull/59035) |
| Fix hang when searching expressions using regular expressions | [#59002](https://github.com/qgis/QGIS/issues/59002) | [PR #59019](https://github.com/qgis/QGIS/pull/59019) | N/A |
| Fix aggregate function returns incorrect results | [#58221](https://github.com/qgis/QGIS/issues/58221) | [PR #59000](https://github.com/qgis/QGIS/pull/59000) | [PR #59085](https://github.com/qgis/QGIS/pull/59085) |
| Fix slow performance with layout table filtering with atlas point geom filter | [#58274](https://github.com/qgis/QGIS/issues/58274) | [PR #58999](https://github.com/qgis/QGIS/pull/58999) | [PR #59030](https://github.com/qgis/QGIS/pull/59030) |
| Add user-friendly warnings when built without webkit and opening layouts with html items | [#58975](https://github.com/qgis/QGIS/issues/58975) | [PR #58997](https://github.com/qgis/QGIS/pull/58997) | N/A |
| Fix edit/copy/paste symbol action for layers with inverted polygon renderer | [#55426](https://github.com/qgis/QGIS/issues/55426) | [PR #58967](https://github.com/qgis/QGIS/pull/58967) | [PR #59034](https://github.com/qgis/QGIS/pull/59034) |
| Non-default blend mode should force raster render of layer | [#55629](https://github.com/qgis/QGIS/issues/55629) | [PR #58966](https://github.com/qgis/QGIS/pull/58966) | [PR #59036](https://github.com/qgis/QGIS/pull/59036) |
| Only render main annotation layer in main map canvas or docked maps | [#58766](https://github.com/qgis/QGIS/issues/58766) | [PR #58964](https://github.com/qgis/QGIS/pull/58964) | N/A |
| Regenerate primary key when making layer permanent if layer property set | [#58942](https://github.com/qgis/QGIS/issues/58942) | [PR #58954](https://github.com/qgis/QGIS/pull/58954) | N/A |
| QgsMapLayer::setDataSource don't require layer name, provider | 未報告 | [PR #58953](https://github.com/qgis/QGIS/pull/58953) | N/A |
| Fix incompatibility between text wrapping and HTML text formatting | 未報告 | [PR #58952](https://github.com/qgis/QGIS/pull/58952) | N/A |
| Fix use of custom object values from QGIS expressions in virtual layers | [#58644](https://github.com/qgis/QGIS/issues/58644) | [PR #58939](https://github.com/qgis/QGIS/pull/58939) | N/A |
| [processing] Fix translation of elapsed strings | [#58635](https://github.com/qgis/QGIS/issues/58635) | [PR #58928](https://github.com/qgis/QGIS/pull/58928) | N/A |
| Fix deadlock when exporting atlas with legend via PyQGIS | [#58496](https://github.com/qgis/QGIS/issues/58496) | [PR #58927](https://github.com/qgis/QGIS/pull/58927) | [PR #58969](https://github.com/qgis/QGIS/pull/58969) |
| Fix clipped render when using geometry generator symbol in layout items | [#58909](https://github.com/qgis/QGIS/issues/58909) | [PR #58926](https://github.com/qgis/QGIS/pull/58926) | N/A |
| Show warning in help for algorithms for known issues or security risk | Reported privately | [PR #58925](https://github.com/qgis/QGIS/pull/58925) | N/A |
| [processing] Replace format for saving batch processing parameters | Reported privately | [PR #58923](https://github.com/qgis/QGIS/pull/58923) | N/A |
| Fix missing canvas variables in some expression editors | 未報告 | [PR #58907](https://github.com/qgis/QGIS/pull/58907) | [PR #58934](https://github.com/qgis/QGIS/pull/58934) |
| Don't restore corrupted sizes/positions when restoring layout items | [#55240](https://github.com/qgis/QGIS/issues/55240) | [PR #58906](https://github.com/qgis/QGIS/pull/58906) | [PR #59103](https://github.com/qgis/QGIS/pull/59103) |
| Add scale method option for layout scale bars | [#55240](https://github.com/qgis/QGIS/issues/55240) | [PR #58904](https://github.com/qgis/QGIS/pull/58904) | N/A |
| Avoid layout scalebar resizing to huge widths in extreme situations | [#55240](https://github.com/qgis/QGIS/issues/55240) | [PR #58794](https://github.com/qgis/QGIS/pull/58794) | N/A |
| QgsDistanceArea methods should raise QgsCsException when errors occur | 未報告 | [PR #58795](https://github.com/qgis/QGIS/pull/58795) | N/A |
| Don't apply reset-to-zero step size logic in spin boxes when no special value text is set | 未報告 | [PR #58836](https://github.com/qgis/QGIS/pull/58836) | N/A |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: Bug fixes by Loïc Bartoletti (Oslandia)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.34 backport commit (GitHub) |
| --- | --- | --- | --- |
| 2-Circle Point Intersection coordinate precision problem | [#59039](https://github.com/qgis/QGIS/issues/59039) | [PR #59155](https://github.com/qgis/QGIS/pull/59155) | N/A |
| Advanced Digitizing Split Tool zeroes M values in a PolyLineZ shapefile | [#49971](https://github.com/qgis/QGIS/issues/49971) | Do not fix (GEOS issue with M) |  |
| QGIS tools splitting curved polygons | [#57021](https://github.com/qgis/QGIS/issues/57021) | Do not fix (GEOS issue with Curve support) |  |
| Incorrect winding/orientation/order of polygon's vertices in Memory layers | [#58333](https://github.com/qgis/QGIS/issues/58333) | [PR #59156](https://github.com/qgis/QGIS/pull/59156) | Too risky? |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Loïc Bartoletti (Oslandia)](https://oslandia.com/)
### Feature: Bug fixes by Stefanos Natsis (LutraConsulting)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.34 backport commit (GitHub) |
| --- | --- | --- | --- |
| Layer order change does not update the 3D view | [#51291](https://github.com/qgis/QGIS/issues/51291) | [PR #59026](https://github.com/qgis/QGIS/pull/59026) | [PR #59187](https://github.com/qgis/QGIS/pull/59187) |
| Unwanted vertices when tracing | [#52935](https://github.com/qgis/QGIS/issues/52935) | [PR #59055](https://github.com/qgis/QGIS/pull/59055) | N/A |
| Extra vertices form to all layers when using tracing | [#59041](https://github.com/qgis/QGIS/issues/59041) | [PR #59055](https://github.com/qgis/QGIS/pull/59055) | N/A |
| QGIS drops extra byte fields from laz (char and unsigned char) | [#56945](https://github.com/qgis/QGIS/issues/56945) | [PR #59160](https://github.com/qgis/QGIS/pull/59160) | N/A |
| 3D view - completely flat MultiPolygonZ geometries don't show color correctly | [#52832](https://github.com/qgis/QGIS/issues/52832) | pending |  |
| Adding more than 250 files or a folder with many files and the Build virtual point cloud (VPC) Tool Fails | [#58894](https://github.com/qgis/QGIS/issues/58894) | [PR #59200](https://github.com/qgis/QGIS/pull/59200) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Stefanos Natsis (LutraConsulting)](https://www.lutraconsulting.co.uk/)
### Feature: Bug fixes by Jacky Volpes (Oslandia)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.34 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fix use of QgsReferencedGeometry in expressions | 未報告 | [PR #59180](https://github.com/qgis/QGIS/pull/59180) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Jacky Volpes (Oslandia)](https://oslandia.com/)
### Feature: Bug fixes by Mathieu Pellerin (OPENGIS)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.34 backport commit (GitHub) |
| --- | --- | --- | --- |
| Clipping of long WKT strings for geometry parameters by using our geometry widget | 未報告 | [PR #59209](https://github.com/qgis/QGIS/pull/59209) | N/A |
| Open Sans font installation failed | [#58988](https://github.com/qgis/QGIS/issues/58988) | [PR #59142](https://github.com/qgis/QGIS/pull/59142) | [PR #59152](https://github.com/qgis/QGIS/pull/59152) |
| Print Layout: with a rotated map, turning on Controlled by Atlas (atlasScalingMode = Auto by default) hangs Layout Manager and corrupts project file | [#58245](https://github.com/qgis/QGIS/issues/58245) | [PR #58749](https://github.com/qgis/QGIS/pull/58749) | N/A |
| Additional NoData value not stored correctly in Raster Layer Properties | [#58293](https://github.com/qgis/QGIS/issues/58293) | [PR #58748](https://github.com/qgis/QGIS/pull/58748) | [PR #58751](https://github.com/qgis/QGIS/pull/58751) |
| Do not copy a geometry column from non-geometry layers | [#58725](https://github.com/qgis/QGIS/issues/58725) | [PR #58746](https://github.com/qgis/QGIS/pull/58746) | [PR #58752](https://github.com/qgis/QGIS/pull/58752) |
| Attribute table: crash and weird behavior when a field has an empty name | [#58738](https://github.com/qgis/QGIS/issues/58738) | [PR #58745](https://github.com/qgis/QGIS/pull/58745) | [PR #58757](https://github.com/qgis/QGIS/pull/58757) |
| Bad styling of scrollbars in the plugin manager dialog | 未報告 | [PR #58713](https://github.com/qgis/QGIS/pull/58713) | [PR #58721](https://github.com/qgis/QGIS/pull/58721) |
| "Refresh layer at interval" settings are not saved to QML | [#58656](https://github.com/qgis/QGIS/issues/58656) | [PR #58686](https://github.com/qgis/QGIS/pull/58686) | [PR #58714](https://github.com/qgis/QGIS/pull/58714) |
| Unresponsive "Add record" button in non-geometry layer editing | [#55092](https://github.com/qgis/QGIS/issues/55092) | [PR #58680](https://github.com/qgis/QGIS/pull/58680) | [PR #58710](https://github.com/qgis/QGIS/pull/58710) |
| -- | [PR \#58747](https://github.com/qgis/QGIS/pull/58747) | -- | -- |
| Algorithms having an output directory parameter fail to execute if output directory is set to "Save to temporary folder" | [#58345](https://github.com/qgis/QGIS/issues/58345) | [PR #58619](https://github.com/qgis/QGIS/pull/58619) | [PR #58626](https://github.com/qgis/QGIS/pull/58626) |
| Text in message box 'Font Install Failed' is poorly legible in Night Mapping theme | [#57290](https://github.com/qgis/QGIS/issues/57290) | [PR #58618](https://github.com/qgis/QGIS/pull/58618) | [PR #58628](https://github.com/qgis/QGIS/pull/58628) |
| Bad plugin manager's look on dark themes | 未報告 | [PR #58606](https://github.com/qgis/QGIS/pull/58606) |  |
| Decorations are too small when exporting temporal controller images on Mac | [#58469](https://github.com/qgis/QGIS/issues/58469) | [PR #58605](https://github.com/qgis/QGIS/pull/58605) | [PR #58613](https://github.com/qgis/QGIS/pull/58613) |
| Layer with data defined symbology does not appear when QGIS opened | [#58508](https://github.com/qgis/QGIS/issues/58508) | [PR #58603](https://github.com/qgis/QGIS/pull/58603) | [PR #58615](https://github.com/qgis/QGIS/pull/58615) |
| QGIS (3.38.1) crashes when trying to show layer labels. QGIS died on signal 11. | [#58570](https://github.com/qgis/QGIS/issues/58570) | [PR #58602](https://github.com/qgis/QGIS/pull/58602) | N/A |
| Fix layout map item preview rendering of XYZ layers with known tile DPI | 未報告 | [PR #58543](https://github.com/qgis/QGIS/pull/58543) | [PR #58566](https://github.com/qgis/QGIS/pull/58566) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Mathieu Pellerin (OPENGIS)](https://www.opengis.ch/)
### Feature: Bug fixes by Jean Felder (Oslandia)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.34 backport commit (GitHub) |
| --- | --- | --- | --- |
| Remaining rubberband and plot data after clearing profile tool | [#50766](https://github.com/qgis/QGIS/issues/50766) | [PR #59181](https://github.com/qgis/QGIS/pull/59181) | N/A |
| Fix issue with vertical lines not visible in the elevation profile tool | 未報告 | [PR #58959](https://github.com/qgis/QGIS/pull/58959) | N/A |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Jean Felder (Oslandia)](https://oslandia.com/)
### Feature: Bug fixes by Germán Carrillo (OPENGIS)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.34 backport commit (GitHub) |
| --- | --- | --- | --- |
| Scale dependent visibility inconsistencies on scale interval edges (symbology, labeling, diagrams) | [#58150](https://github.com/qgis/QGIS/issues/58150) <br> [#42443](https://github.com/qgis/QGIS/issues/42443) | [PR #58968](https://github.com/qgis/QGIS/pull/58968) <br> [PR #59022](https://github.com/qgis/QGIS/pull/59022) | N/A |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

この機能は [Germán Carrillo (OPENGIS)](https://opengis.ch/) によって開発されました

{{<content-end >}}
