---
HasBanner: false
draft: false
releaseDate: '2026-03-06'
section: project
sidebar: true
title: QGIS 4.0  の変更履歴
type: visual-changelog

---
{{<content-start >}}
# QGIS 4.0  の変更履歴{#changelog40 }
<img src="images/projects/388120cc4ef54e6b606481e3c2b08ba3738b5c17.png" class="img-responsive img-rounded center-block" />

リリース日: 2026-03-06

お待たせしました！QGIS 4.0がついに登場！

 [QGIS](https://qgis.org) (<https://qgis.org>) は、世界で最も広く使われている（オープンソースの）デスクトップ地理情報システム（GIS）です。世界中の人々が空間データの閲覧・編集・分析・共有に活用しています。プロ品質の地図作成物を作成でき、数百種類の空間データ形式をサポートしています。QGISは、空間プラットフォームへのアクセスを民主化する Open Source Geospatial Foundation OSGeoのメンバープロジェクトです（https://osgeo.org）。

20年以上前の小さな出発点から、私たちのプロジェクトはソフトウェアの機能面でも、世界中でQGISを支え恩恵を受けている強固で多様な活気あるコミュニティの面でも、着実に成長を続けています。

QGISのコアをQt6フレームワークへ移行するという長年計画されてきた技術的移行の成功を集大成とした、新しいメジャーリリースQGIS 4.0を発表できることを大変嬉しく思います。

表面上は、既存のユーザーにとって従来のQGISリリースで親しんできたGIS体験とほぼ変わらない使い心地となっています。しかしその内部では、保守性と使いやすさに大きな変更が加えられています。これらの変更により、QGIS 4.0はコードベースに待望のパフォーマンスとセキュリティの改善をもたらしながら、最新のライブラリへのアクセスを拡充することが可能になっています。

活発なエコシステムへの円滑な移行を確保するため、プラグイン開発者がツールの更新に必要な作業を最小限に抑えられるよう、可能な限り非推奨APIを維持しています。一部のレガシーAPI（QGIS 2.xのプロセッシングAPIなど）についてはQGIS 4.xシリーズの存続期間を通じた将来のサポートおよび後方互換性が保証されない場合がありますが、既存プラグインをサポートしている開発者は [Qt6互換性ガイド](https://github.com/qgis/QGIS/wiki/Plugin-migration-to-be-compatible-with-Qt5-and-Qt6) を使用することで、プラグインが新しいリリースに対応していることを容易に確認できます。

QGIS 4.0への移行準備が進む中、開発者コミュニティはアプリケーション全体に100以上の新機能を追加し、QGISをより強力に、より柔軟に、よりセキュアに、そして全体的によりすばらしいものにしました。コードベースに関連する開発に加えて、成長著しいQGISユーザーコミュニティはプロジェクト、スタイル、スクリプトなどのリソースを共有し続けており、刷新された [QGIS Hub](https://hub.qgis.org/) および関連するコミュニティサイトの活発な成長期をもたらしています。

 リリースの詳細については、 [community sharing the announcement ](https://youtu.be/SQJZm5Y0EKs) もぜひご覧ください！
 
 
 
 

[![](https://img.youtube.com/vi/SQJZm5Y0EKs/0.jpg)](https://www.youtube.com/watch?v=SQJZm5Y0EKs)

今回のリリースで導入されたすべての新機能を手早く確認するには、 [YouTubeのハイライト動画](https://youtu.be/wTK1exokBA8) をご覧ください。新機能と改善点の詳細な説明については、このリリースの [ビジュアル変更履歴](https://qgis.org/project/visual-changelogs/visualchangelog40/) をご確認ください。

[![](https://img.youtube.com/vi/wTK1exokBA8/0.jpg)](https://www.youtube.com/watch?v=wTK1exokBA8)

QGISはコミュニティの共同作業によって成り立っています。このリリースを実現するために時間と労力をボランティアで提供してくださった（あるいは他の方々の活動を支援してくださった）開発者、ドキュメント作成者、テスター、そして多くの皆様に心より感謝申し上げます。QGISコミュニティを代表して、このリリースをお楽しみいただければ幸いです！

時間や資金の寄付、またはその他の形でQGISをさらにすばらしいものにする活動に貢献したい方は、ぜひ [QGIS.ORG](https://qgis.org/) にアクセスしてご協力ください！

QGISは寄付者およびサステイニングメンバーによって支えられています。プロジェクトに大小を問わず財政的な貢献をしてくださった寄付者の最新リストは [寄付者一覧](https://qgis.org/en/site/about/sustaining_members.html#list-of-donors) でご覧いただけます。公式のプロジェクトサステイニングメンバーになることをご希望の方は、詳細について [サステイニングメンバーページ](https://qgis.org/en/site/about/sustaining_members.html) をご覧ください。QGISへのスポンサーシップは、定期的な開発者ミーティングの開催、プロジェクトインフラの維持、およびバグ修正活動の資金として活用されます。現在のスポンサーの完全なリストを以下に掲載します。すべてのスポンサーの皆様に心より感謝申し上げます！

QGISはフリーソフトウェアであり、使用にあたって料金を支払う義務は一切ありません。むしろ、経済的・社会的な立場に関わらず、世界中の多くの方々に使っていただけるよう積極的に推進しています。空間的な意思決定ツールを人々に提供することが、全人類にとってより良い社会の実現につながると信じているからです。
## 時系列
### 機能：時間的値の表示モードへの「ピクセルの累積」設定の追加
ラスターレイヤーの時間モードが「時間的値を表示」に設定されている場合に利用できる、新しい「ピクセルの累積」オプションが追加されました。これは、地物の時間的状態が単一の日付/時刻フィールドで表現される場合に地物が時間とともに累積できるベクターレイヤーの同等機能を模したものです。<br /> ベクターレイヤーとラスターレイヤーを組み合わせた時間アニメーションのナビゲーションで特に役立ちます。

<img src="images/entries/bcb3022b31756fa9b9bb2a161bdc74633e53c515.png" class="img-responsive img-rounded" />

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
## ツール
### 機能: 空白セグメントを編集するマップツールの追加
[QEP \#345](https://github.com/qgis/QGIS-Enhancement-Proposals/pull/345)に記載されているように、空白セグメントを編集するための新しいマップツールが追加されました。<br /> テンプレート化されたラインシンボロジーに基づいて地物ごとに空白セグメントを定義し、これらのセグメント内にハッシュやマーカーが描画されることを防ぎます。<br /> 空白セグメントはデータ定義プロパティ（データフィールドまたは補助ストレージフィールド）に保存されます。このツールでユーザーができることは以下の通りです:
- ライン付近をクリックしてセグメントの作成を開始し、再度クリックして編集を終了します。
- セグメントを選択し、Delキーを押して削除します。
- 既存のセグメントの始点/終点をドラッグしてライン上で移動させ、セグメントを縮小/拡大します。

<img src="images/entries/05d17bd62aaa441e7756a5bf5970d4ddc90760da" class="img-responsive img-rounded" />

この機能は [City of Frankfurt – Stadtplanungsamt と Oslandia](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html) の資金提供を受けてます

This feature was developed by [Julien Cabieces](https://github.com/troopa81)
### 機能: ライン上に地物を配列状にコピーする
ポリゴン/ラインストリング/ポイントのジオメトリタイプで利用可能な、ライン上に地物を配列状にコピーするための新しいマップツールが追加されました。

<img src="images/entries/60adf287a322741a4f92f851fcfc369b068ed097.png" class="img-responsive img-rounded" />

この機能は [City of Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html) の資金提供で開発されました

This feature was developed by [Jacky Volpes](https://github.com/Djedouas)
## ユーザーインタフェース
### 機能: 新デザインのウェルカムページ
QGIS 4.0では、 [QEP 347](https://github.com/qgis/QGIS-Enhancement-Proposals/pull/351) に沿ったユーザー体験の向上を目的とした拡張可能なデザインを採用した、刷新されたウェルカムページが搭載されています。

<img src="images/entries/26a97dc32083858218bfe1bfd34d00af243b6bef.png" class="img-responsive img-rounded" />

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### Feature: Unlock shipping themes through plugins
QGISコアに新しいテーマ（Night MappingやBlend of Grayなど）を追加することは、メンテナンスコストが高く、また中立的・汎用的・アクセシブルである必要があるためテーマ作者の創造性が制限されていました。<br />QGISはプラグインAPIを通じてテーマをサポートできるように拡張され、コミュニティがQGISコアアプリケーションを変更することなくテーマやカスタムアプリケーションスタイルを適用できるようになりました。これによりQGISのUXにまったく新しい可能性が開かれます。

この機能開発は [free time, inspired by :)](https://github.com/qgis/QGIS/pull/64495) から資金提供を受けています

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### 機能: ユーザー定義のツールバーとメニューの作成
QGISでユーザー定義のメニューとツールバーを作成できるようになり、強力なカスタマイズオプションが提供されます。 <br />これは [QEP \#343](https://github.com/qgis/QGIS-Enhancement-Proposals/blob/master/qep-343-customized-toolbars-and-menus.md) を実装したものです。

<img src="images/entries/553f1a2b5712a2f02d6a5a038197c1baefe6c012" class="img-responsive img-rounded" />

この機能は [City of Frankfurt – Stadtplanungsamt と Oslandia](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html) の資金提供を受けてます

This feature was developed by [Julien Cabieces](https://github.com/troopa81)
### 機能: 属性をダブルクリックしてズームする
属性テーブルのアイテムをダブルクリックすることで、地物を即座に選択してその地物にズームできるようになりました。

<img src="images/entries/50fa542fa614721b36cac2efce700c9800a33c59.gif" class="img-responsive img-rounded" />

この機能は [Nass](https://github.com/lanckmann) によって開発されました
## シンボロジ
### 機能: レイヤ間でのすべてのスタイルのコピー/ペーストを可能にしました
レイヤーに複数のスタイルがある場合、レイヤーツリーのコンテキストメニューに新しい "すべてのスタイルをコピー" アクションが追加されました。 <br />これを実行すると、レイヤーのすべてのスタイルの定義がクリップボードにコピーされます。別のレイヤーのコンテキストメニューを開き、新しい "すべてのスタイルを貼り付け" 機能を使用することで、元のレイヤーのすべてのスタイルのコピーを対象レイヤーに貼り付けることができます。これにより、元のレイヤーの既存スタイルを手動で1つずつ確認してスタイルを貼り付ける必要がなくなります。

<img src="images/entries/76ce4e014c2eb3e29ac33b4b5708834c66961430.png" class="img-responsive img-rounded" />

この機能は City of Canning によって資金提供されました

この機能は [North Road](https://north-road.com/) によって開発されました
### 機能: コピー＆ペーストUIへのスタイルカテゴリのグループ化の追加
レイヤーツリーメニューのスタイルのコピー＆ペーストサブメニューに、グループ化されたカテゴリの新しいショートカットが追加されました。これにより、グループ化されたカテゴリのセットをレイヤー間で素早くコピー＆ペーストできるようになります。

<img src="images/entries/86c35bb07f30070746cfeed9bd533c786bba0df4.png" class="img-responsive img-rounded" />

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
## 注記
### 機能: 新しいアノテーション選択ツール
 アノテーションレイヤーのコピー・移動・回転機能の導入を目的とした [QEP \#344](https://github.com/qgis/QGIS-Enhancement-Proposals/pull/344) の実装の一環として、新しい選択ツールがアノテーションアイテムに対して以下のインタラクティブな操作を提供します:
- アノテーションアイテムの選択。Shiftキーを押しながら操作することで追加アイテムの選択をトグルできます。
- マウスおよびキーボードによる選択アイテムの移動
- 選択アイテムの削除
- マウスハンドラーを使用した選択アイテムのサイズ変更
- マウスハンドラーを使用した選択アイテムの回転

<img src="images/entries/db55791d9e7c92428f8165d661bc264fd09ae61c.png" class="img-responsive img-rounded" />

この機能は [City of Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html) の資金提供で開発されました

この機能は [Mathieu Pellerin](https://opengis.ch) によって開発されました
### 機能: 3D 地図ビューにおけるテキストアノテーションの表示
アノテーションレイヤーが3Dビルボードとしてレンダリングするよう設定されている場合、テキストアノテーションもビルボードとしてレンダリングされます。　<br />ライン/矩形テキストアノテーションの場合、ビルボードはライン/矩形の中心に配置されます。ユーザーは3Dビルボードに使用するテキスト形式を制御できます。元の2Dアノテーションのテキスト形式は無視されるため、<br />3Dテキスト専用の読みやすく適切なテキスト形式を設計することができます。

<img src="images/entries/ce930ee001993bd8bd7ecf0477aac6e5e9436da1.png" class="img-responsive img-rounded" />

この機能は [North Road](https://north-road.com/) によって開発されました
### 機能: アノテーションレイヤーのマーカーの3Dビルボードとしてのレンダリングをサポート
3Dマップでアノテーションレイヤーを表示するための新しいオプションが追加されました。アノテーションレイヤープロパティの3Dタブから、レイヤーを3Dビルボードとしてレンダリングするよう設定できます。有効にすると、レイヤーのすべてのマーカーが3Dマップの上に浮かぶビルボードシンボルとして表示されます（レイヤーのラインとポリゴンは無視されます）。　<br />ユーザーはビルボードの地形へのクランプとオフセット、および「コールアウト」ライン（ビルボードと地形表面の対応する位置を結ぶ垂直線）を表示するかどうかを制御できます。

<img src="images/entries/a74b316080040084674f70ed22492ad06da3c5be.png" class="img-responsive img-rounded" />

この機能は [North Road](https://north-road.com/) によって開発されました
## ラベリング
### 機能: ラベル衝突検出時の空白文字を無視するオプションの追加
この新しいオプション（曲線ラベル配置モードでのみ利用可能）は、2つのラベルが衝突するかどうか（またはラベルが障害物地物と衝突するかどうか）を判定する際に、QGISがラベルテキスト内の空白文字（スペースやタブ）をどのように扱うかを制御します。既存の（デフォルトの）動作では、スペースはテキスト文字と同様に扱われ、別のラベルのスペース部分への重なりは許可されません。<br /> 新しい「衝突検出時にラベルの空白を無視する」オプションをオンにすると、ラベルの重なり（または障害物との衝突）を確認する際にテキスト内の空白文字が無視されます。 <br />これは、長いライン地物にラベルを付ける場合に、単語間隔が大きく、ラベルの空白部分にテキストや他の地物を配置したいときに便利です（河川や道路のラベリングなど）。この設定はデータ定義が可能で、十分な長さの地物にのみ有効にするなど、式を使った高度な機能が利用できます。

<img src="images/entries/25ba4e122bd28db3d8cbf57717e1b4576dc790a5.png" class="img-responsive img-rounded" />

この機能開発には [LINZ](https://www.linz.govt.nz/) の資金提供を受けています

この機能は [North Road](https://north-road.com/) によって開発されました
### 機能: マルチパートジオメトリのラベリングの改善
"マルチパート地物のすべての部分にラベルを付ける"の既存チェックボックスが、マルチパート処理オプションを選択できるコンボボックスに変更されました。 <br />利用可能なオプションは以下の通りです:
- **Label largest part only**: 現在のデフォルト動作に対応します。つまり、ユーザーが"label every part" チェックボックスをオフにした状態です。
- **Label every part with same text**: ユーザーが "label every part" チェックボックスを手動でオンにした際の現在の動作に対応します。
- **Split label text lines over parts**: これはまったく新しい動作で、マルチジオメトリ地物のパート上にラベルテキストを分割して配置します。ラベルテキストは改行文字で分割され、各行が入力地物ジオメトリの対応するパートの上に個別に配置されます。分割は既存の  "Wrap on character" 設定が適用された後に行われるため、マルチパートジオメトリのラベル配置時にユーザーが設定したカスタム改行文字が尊重されます。マルチパートジオメトリのパート数がラベルテキストの行数より少ない場合、余分な行は無視されます。

<img src="images/entries/69d0f632877a1a7380e957dd0b4d7321906d7005.png" class="img-responsive img-rounded" />

この機能開発には [LINZ](https://www.linz.govt.nz/) の資金提供を受けています

この機能は [North Road](https://north-road.com/) によって開発されました
### 機能: 曲線ラベル配置の配置モード
 [QEP 404](https://github.com/qgis/QGIS-Enhancement-Proposals/blob/master/qep-404-curved-placement-modes.md) にしたがって曲線ラベルに使用できる新しい配置 "モード" が追加されました。 <br /> これらの追加モードは、ラインジオメトリタイプのレイヤーが曲線ラベル配置に設定されている場合に表示・有効化されるオプションとして公開されています。新しい曲線配置モードにはデータ定義のオーバーライドが利用可能で、1つのレイヤー内の地物に対して異なるモードを混在させて使用することができます。 <br />新しいモードには以下が含まれます:
- **Default**: 既存の動作、変更なし。グリフは曲線ラインジオメトリに沿って通常の文字間隔および単語間隔で配置されます。
- **Place characters at vertices**:  このモードを選択すると、ラベルテキストの各文字が曲線ラインジオメトリの対応する頂点に左ベースライン位置が来るように配置されます。つまり、最初の文字はラインの始点に、2番目の文字は2番目の頂点に、3番目の文字は3番目の頂点に配置されます。曲線ラインジオメトリの頂点数がラベルテキストの文字数より少ない場合、余分な文字は無視されてレンダリングされません。ラベルの “distance” 設定がゼロ以外の場合、文字は頂点位置からその距離だけ垂直方向にオフセットされます。文字は頂点でのラインの角度に沿って回転します。
- **Stretch character spacing to fit line**: このモードを選択すると、曲線ラインジオメトリの実際の長さ全体にテキストが収まるよう、各ラベルの文字間隔を増加（または減少）させます。
- **Stretch word spacing to fit line**: このモードを選択すると、曲線ラインジオメトリの実際の長さ全体にテキストが収まるよう、各ラベルの単語間隔を増加（または減少）させます。

<img src="images/entries/1c0ce144f536089eabaaf9066453d60a5ae2ca01.gif" class="img-responsive img-rounded" />

この機能開発には [LINZ](https://www.linz.govt.nz/) の資金提供を受けています

この機能は [North Road](https://north-road.com/) によって開発されました
## レンダリング
### 機能:選択的マスキングプリセットの導入
レイヤーのマスキングを設定する際に、マスクソースのドロップダウンから複数のプリセットを選択できるようになりました。複雑な管理を行わずに効率よくマスキングを適用できます。これは、多数の異なるレイヤーが同じ複雑なマスクソースのセットを参照する必要がある大規模プロジェクト、例えば多くのレイヤーが同じ特定のラベル付きレイヤーセットによってマスクされる場合などに特に便利です。　<br /> デフォルト値は "カスタム" で、既存のレイヤーごとのアドホック設定を再現しますが、ユーザーは必要に応じて選択的マスキングセットを作成・名前変更・削除でき、プリセットのチェック済みソースへの変更はそのプリセットにリンクされたすべてのレイヤーに自動的に適用されます。

<img src="images/entries/a73331ff4395c78b8152d289d1759a55aeafd04d.png" class="img-responsive img-rounded" />

この機能開発には [LINZ](https://www.linz.govt.nz/) の資金提供を受けています

この機能は [North Road](https://north-road.com/) によって開発されました
## 三次元機能
### 機能: 3Dシーンエクスポート時の地形エクスポートを無効にするオプションの追加
3Dシーンエクスポートのダイアログに、地形エクスポートを有効または無効にする新しいオプションが追加されました。地形のレンダリングが無効になっている場合でも、地形オプションは常に有効化されています。 `terrain resolution`  （地形解像度）オプションはDTMまたはオンライン地形にのみ適用されます。その他の地形タイプでは無効にする必要があります。

<img src="images/entries/45d755c8e01bb45c2b728dd1dc59dc6afabe8856.png" class="img-responsive img-rounded" />

この機能は [City of Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html) の資金提供で開発されました

This feature was developed by [Jean Felder](https://github.com/ptitjano)
### 機能: 3Dビューでの識別地物のハイライト表示
QGISが3DビューでのベクターFeatureのハイライト表示に対応しました。識別されたポリゴン地物は、2Dマップキャンバスのハイライト効果と同様に、一致する色と透明度で半透明のオーバーレイと太いシルエットラインを使用して3Dビューでハイライト表示されます。ハイライト効果は常に他のエンティティの上にレンダリングされます。現在の視点でハイライトされた地物が重なる場合、認識される外周に1つの集約されたシルエットがレンダリングされます。

<img src="images/entries/49c5a902146f5890162179a952c10a44757a8437.png" class="img-responsive img-rounded" />

この機能開発には [QGIS 3D for Open Source Digital Twins (crowdfunding campaign)](https://www.lutraconsulting.co.uk/crowdfunding/qgis-3d-for-open-source-digital-twins) から資金提供を受けました

この機能は [Stefanos Natsis (Lutra Consulting)](https://github.com/uclaros) によって開発されました
### 機能: 断面図：固定トレランス（幅）の使用と左右への微調整
断面図を定義する際、通常はユーザーが2つの端点を選択し、3回目のマウスクリックで断面の幅（トレランス）を指定します。新しいバージョンではトレランスをロックできるため、毎回幅（トレランス）を選択することなく2つの端点を選ぶだけで済みます。さらに、GUI上のトレランス値を編集することで、アクティブな断面図のトレランスを変更することも可能です。 <br />3Dマップビューでも、標高プロファイルウィジェットと同様の方法（メニューボタンまたはキーボードショートカット）でアクティブな断面図を左右に微調整できるようになりました。

<img src="images/entries/d6998552d0292c6f65ef77d8ad881abdd252e88f.png" class="img-responsive img-rounded" />

この機能開発は [Danish Agency for Climate Data](https://www.klimadatastyrelsen.dk/) からの資金提供を受けました

この機能は [Dominik Cindric (Lutra Consulting)](https://github.com/ViperMiniQ) によって開発されました
### 機能: 動的ベクターチャンキング
以前のバージョンのQGISでは、3Dビューでのベクターレイヤーのチャンキングは固定ズームレベルを使用していました。この動作がクワッドツリーの深さを動的に調整するよう変更され、各ズームレベルではユーザーが指定した "チャンクあたりの最大地物数" の値によって制限された最大数の地物のみが読み込まれます。これにより、ズームアウト時にすべての地物を読み込むことなく、より大きなレイヤーをレンダリングできるようになります。

<img src="images/entries/7d0ed17befd3fb5d351c9d3ea603ae1ea4741fdd.png" class="img-responsive img-rounded" />

この機能開発には [QGIS 3D for Open Source Digital Twins (crowdfunding campaign)](https://www.lutraconsulting.co.uk/crowdfunding/qgis-3d-for-open-source-digital-twins) から資金提供を受けました

この機能は [Stefanos Natsis (Lutra Consulting)](https://github.com/uclaros) によって開発されました
### 機能: 押し出しポリゴンの底面のレンダリング
ポリゴン3Dシンボルが地物のレンダリング時に底面を含めることができるようになりました。以前はこれが含まれておらず、ボックスとして体積データをレンダリングする際に下部が欠けてしまっていました。

<img src="images/entries/74053b5b39cc9e15d7175643786aa48edb459486.png" class="img-responsive img-rounded" />

この機能開発には [QGIS 3D for Open Source Digital Twins (crowdfunding campaign)](https://www.lutraconsulting.co.uk/crowdfunding/qgis-3d-for-open-source-digital-twins) から資金提供を受けました

この機能は [Dominik Cindric (Lutra Consulting)](https://github.com/ViperMiniQ) によって開発されました
### 機能: 2d地図オーバーレイ機能の追加
3Dマップビューの新機能により、3Dカメラの位置を中心とした2Dマップのオーバーレイを表示したり、オプションでカメラフラスタムを表示したりできるようになりました。

<img src="images/entries/0c322a45de5780379e95e0f0d7467482e1d6661a.png" class="img-responsive img-rounded" />

この機能は [City of Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html) の資金提供で開発されました

This feature was developed by [Jean Felder](https://github.com/ptitjano)
### 機能: Esri シーンレイヤー
ESRI I3S（"シーンレイヤー" /"シーンサーバー"とも呼ばれる）向けのタイル化シーンレイヤーの新しいデータプロバイダーが追加されました。データのレンダリングは2Dおよび3Dマップビューの両方で利用できます。 <br />I3Sデータの読み込み方法:
- ArcGIS RESTサーバーから - データソースマネージャーまたはブラウザードックから読み込めます（以前はシーンレイヤーが表示されていませんでしたが、現在は表示されます）。
- ローカルのSLPKファイルを開く - ファイルブラウザーからのドラッグ＆ドロップ、ブラウザードック、またはデータソースマネージャー（シーンタブ）から読み込めます。　<br />注意事項:
- サポート中 I3S \>= 1.7
- 3DObjectおよびIntegratedMeshレイヤータイプをサポート
- "グローバル"モード（EPSG:4326）と "ローカル" モード（任意の投影座標系）の両方のデータセットをサポート

<img src="images/entries/b7a22f419d8b99a1cdf1fcbeacf768021b3afe33.png" class="img-responsive img-rounded" />

この機能開発には [QGIS 3D for Open Source Digital Twins (crowdfunding campaign)](https://www.lutraconsulting.co.uk/crowdfunding/qgis-3d-for-open-source-digital-twins) から資金提供を受けました

この機能は [Martin Dobias (Lutra Consulting)](https://github.com/wonder-sk) によって開発されました
### 機能: 正射影カメラの動作の実現
3Dビューには以前からパースペクティブカメラの代わりに正射影カメラを使用するオプションがありましたが、長い間のリリースにわたってこのオプションは機能していませんでした。正射影カメラのサポートが使用できるようになり、断面図を使用する際に非常に実用的です。

<img src="images/entries/9caebdb681257fd8ef96886833d26f278da61ae8.png" class="img-responsive img-rounded" />

この機能開発には [QGIS 3D for Open Source Digital Twins (crowdfunding campaign)](https://www.lutraconsulting.co.uk/crowdfunding/qgis-3d-for-open-source-digital-twins) から資金提供を受けました

この機能は [David Konarik (Lutra Consulting)](https://github.com/dvdkon) によって開発されました
## 点群
### 機能: 仮想ポイントクラウド（VPC）構築アルゴリズムの拡張
仮想ポイントクラウド（VPC）構築アルゴリズムは、LASまたはLAZファイルがVPCの入力として含まれる場合に警告を表示します（このようなVPCは入力ファイルをCOPC形式に変換しないとQGISで完全に表示できません）。このアルゴリズムには入力ファイルをCOPC形式に変換するオプションも追加されており、すべての入力ファイル（LAS/LAZなど）を自動的にCOPCに変換し、VPCをQGISでの2D/3Dレンダリングに適した状態にします。

この機能開発は [Danish Agency for Climate Data](https://www.klimadatastyrelsen.dk/) からの資金提供を受けました

この機能は  [Jan Caha (Lutra Consulting)](https://github.com/JanCaha) によって開発されました
### 機能: 新しいプロセッシングアルゴリズム:ポイントクラウドの比較（M3C2）
2つのポイントクラウドレイヤーを比較するための新しいアルゴリズムが追加されました。 <br />M3C2アルゴリズム（マルチスケールモデル間クラウド比較）は、固定された投影方向を使用するのではなく、局所的に推定された表面法線に沿って2つの3Dポイントクラウド間の距離を計算します。複数のスケールで動作することで、表面の向きと符号付き距離の両方を精度高く推定し、岩面や河岸などの複雑な3D表面の変化検出に適しています。 <br /> 注意：このアルゴリズムはPDALの filters.m3c2 を使用するため、QGISのインストールにPDALバージョン2.10以上が含まれている場合にのみ動作します。

<img src="images/entries/d9a6459aac43a28b79857ac0c6a48870abbe1681.png" class="img-responsive img-rounded" />

この機能開発は [Danish Agency for Climate Data](https://www.klimadatastyrelsen.dk/) からの資金提供を受けました

この機能は [Jan Caha (Lutra Consulting) + PDAL implementation by Hobu Inc.](https://github.com/JanCaha) によって開発されました
### 機能: VPCが実際のポイントを表示するズームレベルの選択
VPCの2D/3Dスタイルプロパティに新しいコンボボックスが追加されました。これはQGISがタイル範囲または概観ポイントクラウドのレンダリングから、VPCにリンクされたデータファイルのポイントのレンダリングに切り替えるズームレベルを制御します。これにより、ポイントクラウドのレンダリングにおけるパフォーマンスと詳細度のトレードオフをより細かく制御できるようになり、以下のオプションが提供されます：
- Later
- Normal
- Earlier
- Much earlier

<img src="images/entries/a0c145b876b64361435d38986cdf8cef786d7857.png" class="img-responsive img-rounded" />

この機能開発は [Danish Agency for Climate Data](https://www.klimadatastyrelsen.dk/) からの資金提供を受けました

この機能は [Dominik Cindric (Lutra Consulting)](https://github.com/ViperMiniQ) によって開発されました
### 機能: 仮想ポイントクラウドのリモートデータセットサポートの追加
QGISがリモートサーバーでホストされている仮想ポイントクラウドを読み込めるようになりました。これにより大容量のポイントクラウドデータセットの配布における障壁が低くなります。QGISが自動的に処理するため、ユーザーは事前に.vpcファイルをダウンロードする必要がありません。

この機能開発には [QGIS 3D for Open Source Digital Twins (crowdfunding campaign)](https://www.lutraconsulting.co.uk/crowdfunding/qgis-3d-for-open-source-digital-twins) から資金提供を受けました

この機能は [Dominik Cindric (Lutra Consulting)](https://github.com/ViperMiniQ) によって開発されました
### 機能: 仮想ポイントクラウドの編集
仮想ポイントクラウド（VPC）内のポイントクラウドデータを編集できるようになりました。VPCおよびリンクされたデータファイルがローカルのCOPCファイルとして利用可能であること（リモートサーバーでホストされていないこと）が条件です。

この機能開発は [Danish Agency for Climate Data](https://www.klimadatastyrelsen.dk/) からの資金提供を受けました

この機能は [Dominik Cindric (Lutra Consulting)](https://github.com/ViperMiniQ) によって開発されました
### 機能: 新しいプロセッシングアルゴリズム：地上高
"地上高"アルゴリズムは、起伏のある地形全体での標高データの正規化に不可欠な、推定地表面からの各ポイントの垂直距離を計算します。建物の高さ抽出や植生高の推定などの用途に役立ちます。<br />アルゴリズムは同じポイントクラウドを出力し、計算された標高を含む新しい属性（"HeightAboveGround"）が追加されます。オプションで、計算された地上高でポイントのZ値を置き換えることもできます（3D可視化やさらなる処理に役立つ場合があります）。　<br />アルゴリズムには2つのバリアントがあります。基本バリアントは近くの地面ポイントから地表面を推定し、もう一方のバリアントは地面ポイントの三角測量を作成してそこから高さを推定します。<br />入力ポイントクラウドには、地面として分類されたポイント（classification=2）が一部含まれている必要があります。

この機能開発には [QGIS 3D for Open Source Digital Twins (crowdfunding campaign)](https://www.lutraconsulting.co.uk/crowdfunding/qgis-3d-for-open-source-digital-twins) から資金提供を受けました

この機能は  [Jan Caha (Lutra Consulting)](https://github.com/JanCaha) によって開発されました
### 機能: 新しいプロセッシングアルゴリズム:地上ポイントの分類
このアルゴリズムは、Simple Morphological Filter（SMRF）アルゴリズムを使用して地上ポイントを分類します。<br />SMRFは、LiDARポイントクラウドで植生や建物などの非地面ポイントから地面ポイントを分離するために段階的なモルフォロジー演算を使用する地面フィルタリングアルゴリズムです。増加するウィンドウサイズでの開演算と標高閾値を繰り返し適用することで、計算効率が高く、裸地デジタル地形モデルの生成に効果的です。

この機能開発には [QGIS 3D for Open Source Digital Twins (crowdfunding campaign)](https://www.lutraconsulting.co.uk/crowdfunding/qgis-3d-for-open-source-digital-twins) から資金提供を受けました

この機能は  [Jan Caha (Lutra Consulting)](https://github.com/JanCaha) によって開発されました
### 機能: 新しいプロセッシングアルゴリズム:ノイズのフィルタリング
ポイントクラウドのノイズフィルタリング用の新しいアルゴリズムが2つ追加されました（統計的手法または半径を使用）。 <br />ノイズフィルタリングアルゴリズムは、センサーエラー、マルチパス反射、または大気干渉によるポイントクラウド内の外れ値ポイントを特定して除去します。各ポイントの局所的な近傍を解析し、周囲から大きく外れたポイントにフラグを立てます。

この機能開発には [QGIS 3D for Open Source Digital Twins (crowdfunding campaign)](https://www.lutraconsulting.co.uk/crowdfunding/qgis-3d-for-open-source-digital-twins) から資金提供を受けました

この機能は  [Jan Caha (Lutra Consulting)](https://github.com/JanCaha) によって開発されました
### 機能: 新しいプロセッシングアルゴリズム：ポイントクラウドの変換
変換アルゴリズムは、ポイントクラウドレイヤーの形状を変えることなく、位置合わせのために移動・回転・スケーリングを適用します。　<br />これは既知の基準点や対応関係を使用して、測量間の系統的なオフセットを修正する際によく使用されます。

この機能開発には [QGIS 3D for Open Source Digital Twins (crowdfunding campaign)](https://www.lutraconsulting.co.uk/crowdfunding/qgis-3d-for-open-source-digital-twins) から資金提供を受けました

この機能は  [Jan Caha (Lutra Consulting)](https://github.com/JanCaha) によって開発されました
## 印刷レイアウト
### 機能: レイアウトマップグリッドアノテーションの水平配置コントロールの追加
レイアウトマップ上のグリッドアノテーションを常に左揃えにするのではなく、ユーザーが配置を選択できる新しいコントロールが追加されました。これは特に複数行のアノテーションで役立ちます。地図の左側で左揃えにすると見栄えが良くない場合があります。

この機能開発には [LINZ](https://www.linz.govt.nz/) の資金提供を受けています

この機能は [North Road](https://north-road.com/) によって開発されました
### 機能: レイアウト凡例の初期レイヤーセットと同期処理の改善
 [QEP 253](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/253) に沿って、印刷レイアウトの凡例にレイヤー同期モードが導入されました.<br />これにより既存のレイアウト凡例の "自動更新" チェックボックスが削除され、代わりに以下を含む凡例の表示モードを示すわかりやすいコンボボックスが導入されます:
- **Synchronize to All Project Layers**: このオプションは "自動同期" チェックボックスの現在の動作と一致します。選択すると、プロジェクトに追加されたすべての新しいレイヤーが凡例に即座に表示され、これらのレイヤーへの変更も即座に凡例に反映されます。
- **Synchronize to Visible Layers**: このオプションは、凡例アイテムにリンクされたマップ（凡例にマップがリンクされていない場合はメインのプロジェクトレイヤーツリー）で現在表示されているレイヤーを考慮します。このモードが有効な場合、マップで表示されるレイヤーセットへの変更は凡例レイヤーをその表示レイヤーセットに合わせます。このモードは既存の "Only show items in the linked map"  オプションとは異なります。"Synchronize to Visible Layers" モードはリンクされたマップの範囲をまったく考慮しません。レイヤーがチェックされてマップで表示されている場合、そのレイヤーのすべての地物が表示されているマップの範囲外にあるかどうかに関わらず、凡例に表示されます。"Synchronize to All Project Layers" オプションと同様に、メインのプロジェクトレイヤーツリーの名前やその他の凡例関連設定への変更は自動的にレイアウト凡例に反映されます。
- **Manual Layer Selection**: 凡例のすべての内容はユーザーが手動で制御でき、含まれるレイヤーの自動同期は適用されません。これは現在QGISで "auto update" オプションがオフの場合と同じ動作です

凡例の以前の "Update All" 操作が新しい "Reset" 機能に変更されました。<br />この変更には、オプション - レイアウトページに追加された新しいグローバル設定が含まれており、ユーザーは新しく作成される凡例のデフォルトモードを制御できます。デフォルトでは、大規模プロジェクトを持つユーザーにより良いすぐに使えるエクスペリエンスを提供するため、QGISは "Synchronize to Visible Layers" モードを使用します。ただし、ユーザーはこの設定を適宜変更することで以前のデフォルト動作に戻すことができます。

<img src="images/entries/3b47cf11887bdd0717b6cef55fdcb5f7b7ac0c13.gif" class="img-responsive img-rounded" />

この機能は QGIS Danish User Group の資金提供で開発されました

この機能は [North Road](https://north-road.com/) によって開発されました
### 機能: レイアウトマップグリッドアノテーションの表示のデータ定義制御と、グリッド用の追加式変数の追加
これにより、マップグリッドテキストの表示をアノテーションごとに制御できます。つまり、個々のグリッドアノテーションを選択的に非表示または表示にすることができます。式では  `@grid_axis` および `@grid_number`  式変数を使用できます。最初/最後のグリッドアノテーションを選択的に非表示にするなどの操作を容易にする新しい式変数も導入されました:
- @grid_count: 現在のグリッド軸で表示されているグリッド線の総数。
- @grid_index: 現在描画されているグリッド線のインデックス（最初のグリッド線を1として開始）。インデックスは現在のグリッド軸に固有のものです。

この機能開発には [LINZ](https://www.linz.govt.nz/) の資金提供を受けています

この機能は [North Road](https://north-road.com/) によって開発されました
### 機能: アトラスジオメトリによるマップアイテムのフレーム形状変更を可能になりました
新しいフレームクリップ機能が追加されました。有効にすると、レイアウトマップアイテムのフレームが現在のアトラス地物の（ポリゴン）ジオメトリに合わせて形状変更されます。これにより、アトラスアイテムでの柔軟なクリッピングとマスキングが可能になります。特にキャンバスの背景色がレンダリングの重要な要素となる場合（ベクタータイルのベースマップなど）に役立ちます。

<img src="images/entries/6cadd40d1ebfa64b6190c75334df0340c00a4d93.png" class="img-responsive img-rounded" />

この機能は [City of Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html) の資金提供で開発されました

この機能は [Mathieu Pellerin](https://opengis.ch) によって開発されました
### 機能: 新しい円グラフのプロットタイプ
QGISおよびそのレイアウトデザイナーで利用可能なプロットタイプに新しい円グラフが追加されました。

<img src="images/entries/ae30dae66281636965dbff50915b96b6ecbabacc.png" class="img-responsive img-rounded" />

この機能は [City of Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html) の資金提供で開発されました

この機能は [Mathieu Pellerin](https://opengis.ch) によって開発されました
### 機能: 印刷レイアウトチャートの実装
新しいレイアウトチャートアイテムが追加され、印刷レイアウトおよびアトラスレイアウトにチャートのレンダリングを活用できるようになりました。<br />チャートの設定は、プロパティパネルと複数のサブパネルで提供される豊富なプロパティセットを使用して定義します。チャートアイテムは、アイテムプロパティのデータソースグループを通じて設定されたソースレイヤーから取得したXおよびY値のデータ系列から可視化を構築します。各系列は、XおよびY値を評価する式と、ソースレイヤーをフィルタリングする機能を使用して定義され、各プロパティはサブパネルで設定します。ソースレイヤーの反復処理を並び替えることができ、棒グラフ/折れ線グラフではこの順序が考慮されます。

<img src="images/entries/65b7cdfcb7c7595f007a1911e51894e3cfab80dc.png" class="img-responsive img-rounded" />

この機能は [City of Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html) の資金提供で開発されました

この機能は [Mathieu Pellerin](https://opengis.ch) によって開発されました
### 機能: 現在の地物のみにカバレッジレイヤーのレンダリングを制限するアトラスオプションの追加
カバレッジレイヤー上の地物のレンダリングを現在の地物のみに制限する新しいアトラスオプションが追加されました。これにより、アクティブなアトラス地物を使用した複雑な式を記述することなく、他の地物を動的に除外できるようになります。

<img src="images/entries/7f1b58c91bf273f63b125dc5fe30327ae18068ed.png" class="img-responsive img-rounded" />

この機能は [City of Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html) の資金提供で開発されました

この機能は [Mathieu Pellerin](https://opengis.ch) によって開発されました
### 機能: マップアイテムのツールバーメニューへのレイヤーアイテムへの範囲設定の追加
レイアウトマップのツールバーに新しいメニューアクションが追加され、指定したマップアイテムの範囲をプロジェクト内の空間レイヤーの範囲に素早く合わせることができるようになりました。

<img src="images/entries/e4ba1fa83ed9a5601b434666eb8952eb270b970e" class="img-responsive img-rounded" />

この機能は [City of Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html) の資金提供で開発されました

この機能は [Mathieu Pellerin](https://opengis.ch) によって開発されました
### 機能: 新しいレイアウトアイテム回転ハンドル
選択したレイアウトアイテムに回転ハンドルが追加され、アイテムの回転を調整してレイアウトを完成させることができるようになりました。

<img src="images/entries/eaed49778b763c98749a2d37a9e4654602911616.png" class="img-responsive img-rounded" />

この機能開発には City of Frankfurt – Stadtplanungsamt からの資金提供を受けました

この機能は [Mathieu Pellerin](https://opengis.ch) によって開発されました
## 計算式
### 機能:  "equals" ジオメトリ関数の追加
2つのジオメトリの等価性を (`overlay_equals` と同様の方法で) テストする新しい `equals(geometry1, geometry2)`  ジオメトリ関数が追加されました。

<img src="images/entries/8bd21615869e1defb47183b43aa131ecb2dbab17.png" class="img-responsive img-rounded" />

This feature was developed by [Andrea Giudiceandrea](https://github.com/agiudiceandrea)
### 機能: 磁気モデルを扱うための式関数の追加
磁気モデルの詳細を扱うための新しい式が利用可能になりました。以下が含まれます::
- magnetic_declination: ある地点における磁場の偏角を北方向から東方向に向けた度数で返します。
- magnetic_inclination: ある地点における磁場の伏角を水平方向から下向きに向けた度数で返します。
- magnetic_declination_rate_of_change: ある地点における磁場の偏角の変化率を年あたりの度数で返します。
- magnetic_inclination_rate_of_change: ある地点における磁場の伏角の変化率を年あたりの度数で返します。

これは印刷レイアウトのメタデータとしてとても便利です

<img src="images/entries/54affd11032e735eee18b4ef94d8f654a8d7acf8.png" class="img-responsive img-rounded" />

この機能開発には [LINZ](https://www.linz.govt.nz/) の資金提供を受けています

この機能は [North Road](https://north-road.com/) によって開発されました
### 機能: extract_degrees, extract_minutes, extract_seconds 関数の追加
これらの関数は、十進度値の各構成要素（度・分・秒）を個別に抽出して書式設定（例：度数を太字で表示するなど）できるようにすることで、度数ベースのグリッドアノテーションの表示を簡単にカスタマイズできるよう設計されています
- extract_degrees: 十進度値から整数の度数を抽出します。分と秒の成分は無視されます。抽出された度数の値はゼロに向かって切り捨てられます（四捨五入ではありません）。
- extract_minutes: 十進度値から整数の分数を抽出します。度と秒の成分は無視されます。抽出された分の値はゼロに向かって切り捨てられ（四捨五入ではありません）、常に正の値となります。
- 十進度値から小数の秒数を抽出します。度と分の成分は無視されます。抽出された秒の値は常に正の値となります。

<img src="images/entries/afca4fe52738eae1b242ae2720e0bbbb97f119fe.png" class="img-responsive img-rounded" />

この機能開発には [LINZ](https://www.linz.govt.nz/) の資金提供を受けています

この機能は [North Road](https://north-road.com/) によって開発されました
### 機能: PostgreSQLのunaccentに基づくunaccent関数の追加
語素からアクセント（発音区別符号）を除去する新しい unaccent メソッドが提供されました。例：unaccent( "ï" )

<img src="images/entries/1d59428a063df21c5d83676b45e83771e56f5aca.png" class="img-responsive img-rounded" />

この機能は [Tudor Barascu](https://github.com/tudorbarascu) によって開発されました
### 機能: substr_count 式の追加
新しい `substr_count` 式により、文字列内の部分文字列の出現回数を簡単にカウントできるようになります。

<img src="images/entries/09cbb9e54d4b4326ced2b4bdcf8c93736960af0a.png" class="img-responsive img-rounded" />

この機能は [Tudor Barascu](https://github.com/tudorbarascu) によって開発されました
### 機能: いくつかのタイムゾーンに関係する式関数を追加しました。
式でタイムゾーンを扱うためのいくつかの関数を追加します:
- `timezone_from_id`: IANAタイムゾーンデータベースの文字列IDからタイムゾーンオブジェクトを作成します。
- `timezone_id`: IANAタイムゾーンデータベースのIDを使用してタイムゾーンオブジェクトのID文字列を返します。
- `get_timezone`: 日時値に関連付けられたタイムゾーンオブジェクトを返します。
- `convert_timezone`: 日時オブジェクトを別のタイムゾーンに変換します。
- `set_timezone`: 日付や時刻のコンポーネントを変更せずに、日時値に関連付けられたタイムゾーンオブジェクトを設定します。この関数は日時のタイムゾーンを置き換えるために使用できます。

<img src="images/entries/67fe7d4aa19caa1698e52c9d27e2dd954b809bb9.png" class="img-responsive img-rounded" />

This feature was funded by [North Road](https://north-road.com/)

この機能は [North Road](https://north-road.com/) によって開発されました
## デジタイズ
### 昨日: ベジェマップツール
NURBSカーブを使用したパーツデジタイズの新しいGUIコントロールとして、"poly-bézier" / "freeform"  カーブモードが追加されました。このモードは多くのグラフィックデザインツールと同様の方法でアンカーとハンドルを使用してカーブの形状を制御します。<br />ユーザーはクリック＆ドラッグでハンドル付きのポイントを追加でき、 `alt+click` でポイントのハンドルをリセットできます。

<img src="images/entries/584c6a12ea7a79081fa1fce9f86d9c7d80ecf31c.png" class="img-responsive img-rounded" />

この機能は [City of Frankfurt – Stadtplanungsamt と Oslandia](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html) の資金提供を受けてます

This feature was developed by [Loïc Bartoletti](https://github.com/lbartoletti)
### 機能: CADドックの面積および合計長さ/外周の浮動値の追加
高度デジタイズCADツールインターフェースに新しい浮動値が提供され、ユーザーの選択に基づいてデカルトまたは楕円体計算を使用して面積および合計長さ/外周値を表示するオプションが追加されました（CADツールはデジタイズにデカルト座標を使用するため、表示される楕円体値との差異が生じる場合があることに注意してください）。

<img src="images/entries/03e5d6b7b5c5ad9449f6abcb73c3dc21706b5ec5.png" class="img-responsive img-rounded" />

この機能は [QGIS Danish User Group](https://qgis.dk/) の資金提供で開発されました

この機能は [North Road](https://north-road.com/) によって開発されました
### Feature: Add Maptool to handle chamfer and fillet of polygons
A new digitizing Maptool allows users to chamfer or fillet polygons.

<img src="images/entries/58ace0c2995032999b366d0171a78857e687d3c4.png" class="img-responsive img-rounded" />

この機能は [City of Frankfurt – Stadtplanungsamt と Oslandia](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html) の資金提供を受けてます

This feature was developed by [Benoit D.-M. - oslandia](https://github.com/benoitdm-oslandia)
## データ管理
### Feature: Enhanced COG support for raster exports
The Raster Exports and Save dialogs now support explicit options to specify that the output should be exported with Cloud Optimized GeoTiff optimization, with additional COG-specific pyramid features, including improvements for:
- progress reporting
- error handling
- pyramid generation operations

Note that this requires GDAL \>= 3.13.0

<img src="images/entries/60cec0aa212eb189e7749c242ba1ca49423ca845.png" class="img-responsive img-rounded" />

This feature was funded by [QGIS-DE - Anwendergruppe Deutschland e.V.](https://qgis.de/)

This feature was developed by [Even Rouault](https://github.com/rouault)
### Feature: Copy raw attribute values
QGIS now makes the raw (original) attribute values visible and copyable in both Attribute tables and the Identify Result interface.<br />In previous versions, data values were copied only in their "represented" form, i.e., the values that are evaluated by locale settings, expressions, or display values (e.g, foreign key values).<br />The new "Copy Raw Cell Content" option, available from the context menu, will copy literal values from the source data to the clipboard.

<img src="images/entries/cbc449f46c49440ac88d7f89a36e490d4d1deb20.png" class="img-responsive img-rounded" />

This feature was funded by Ct. Solothurn

This feature was developed by [signedav](https://github.com/signedav)
### Feature: Allow storing Comments in QGIS Projects stored in PostgreSQL
QGIS projects stored in PostgreSQL can now include comments with additional information, which is displayed in the browser using a Tooltip.

<img src="images/entries/fa9f5d8b4ba7be7475799d104df2c4e96cc26f71.png" class="img-responsive img-rounded" />

この機能開発には Ocean Winds の資金提供を受けました

この機能は [Jan Caha](https://github.com/JanCaha) によって開発されました
### Feature: Allow named layers as temporary output
This functionality allows the user to name a temporary output layer that is the result of a processing algorithm. The fact that the layer is temporary is identifiable by the temporary icon (memory chip) displayed before the user defined layer name.

<img src="images/entries/3fec097dc50545f03ab62e3cff5688b719d23916" class="img-responsive img-rounded" />

This feature was funded by QGIS DK user group

この機能は [Jan Caha](https://github.com/JanCaha) によって開発されました
### Feature: Possibility to change the layer name in the layer panel when saving a scratch layer
When saving a scratch layer as a permanent layer with a new name (a different file name than the name in the layer panel), a message bar is shown. In this message bar, the user can choose to automatically change the name in the layer panel to the new layer name.<br />This message bar is only shown if the layer is saved with a new name, and currently, this only works for some filetypes (it works for geopackages but not for shapefiles).

<img src="images/entries/f4d0c0c524eed26129c8c59c406018085e071220" class="img-responsive img-rounded" />

This feature was funded by QGIS DK user group

この機能は [Jan Caha](https://github.com/JanCaha) によって開発されました
### Feature: Suggest a file name when exporting layer or group as layer definition file
When saving a layer or a layer group as a layer definition file (.qlr), the filename field was left empty by default. QGIS now populates the name of the layer or group as a suggestion for the filename to reduce friction for style exports.

This feature was developed by [pgipper](https://github.com/pgipper)
## フォームとウィジェット
### Feature: Add the ability to preview the attributes form within the vector layer properties dialog
QGIS now provides the ability to preview an attributes form while configuring it within the vector layer properties dialog.

<img src="images/entries/c0bb362e1f57600a820c2d185f77993abbd48318.png" class="img-responsive img-rounded" />

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### Feature: Refine reuse of last value and introduce remembrance toggle
QGIS Attribute Forms now include an enhanced user experience for handling the reuse of "last captured" values in forms. A pin icon on forms will give users visual feedback on whether a field's value will be remembered and reused, and provide an active toggle to control whether it should continue to be reused. Additional enhancements to the form configuration allow session-level reuse policies to be set, the default behavior for reuse policies (enabled/disabled), and the ability to disable reuse policies across all fields in a layer.

<img src="images/entries/b06e53bc63de8ea4643beb74c69781076b613d07.png" class="img-responsive img-rounded" />

This feature was funded by Funded by DB Fahrwegdienste GmbH

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
## レイヤ凡例
### Feature: Add control over whether layers are included in automatic print layout legends
A new setting has been added in the layer properties legend tab (for vector, raster, mesh, and point cloud layers) for "Include automatically in print layout legend items". This setting is checked by default. Users must uncheck to exclude that layer from print layout legends.<br />This has also been added to the legend page for mesh and point cloud layers, with the generic setting for controlling embedded legend widgets.

<img src="images/entries/798344535f33fdaf2047bfbd3070def6d28bb6fb.png" class="img-responsive img-rounded" />

この機能は [QGIS Danish User Group](https://qgis.dk/) の資金提供で開発されました

この機能は [North Road](https://north-road.com/) によって開発されました
### Feature: Custom Elevation Profile Sources
QGIS now includes more powerful interactive behaviors for Elevation Profiles, including changing the layer visibility and rendering order on related canvases and linking the project layer tree to the profile plot sources.<br />This functionality is enabled by the introduction of the `QgsLayerTreeCustomNode` class, which enables the representation of application objects (other than layers and groups) in QGIS layer trees.

<img src="images/entries/8218225f95e403fe8e543f34b0427561371265b6.png" class="img-responsive img-rounded" />

This feature was funded by [the QGIS user group Switzerland](https://qgis.ch/)

This feature was developed by [Germap](https://github.com/gacarrillor)
## プロセシング
### Feature: Native polygon orientation algorithms
New algorithms for **Force polygons clockwise** (`native:forcecw`) and **Force polygons counter-clockwise** (`native:forceccw`) have been added to processing algorithms.<br />Force polygons clockwise replicates the existing "Force right-hand-rule" operation, and forces polygon geometries to respect the convention where the exterior ring is oriented in a clockwise direction and the interior rings in a counter-clockwise direction.<br />Force polygons counter-clockwise performs the inverse, and forces polygon geometries to respect the convention where the exterior ring is oriented in a counter-clockwise direction and the interior rings in a clockwise direction.

<img src="images/entries/a0c4136c269a5cd474bdc29e15c26831baa8706f.png" class="img-responsive img-rounded" />

This feature was developed by [Andrea Giudiceandrea](https://github.com/agiudiceandrea)
### Feature: Configure model components using an inline panel instead of modal dialogs
A new configuration panel has been added, docked to the right-hand side of the Processing model designer, which allows editing of model components without the modal dialogs, and replicating the user experience from the Layer Styling Panel. This improves the UX for model editing and prevents model configuration modals from blocking user interaction with other QGIS elements while model components are being edited. Users can still access the dialogs when double-clicking an item.

<img src="images/entries/c6368e5609a680adf719ca6cd1a95739278db0d2.png" class="img-responsive img-rounded" />

This feature was funded by [City of Canning](https://www.canning.wa.gov.au/)

この機能は [North Road](https://north-road.com/) によって開発されました
### Feature: Add network analysis validation algorithms
Two new algorithms useful for validating networks have been added:
- ネットワークの検証
- Extract network endpoints

**Validate network**<br />This algorithm analyzes a network vector layer to identify data and topology errors that may affect network analysis tools (like shortest path). Optional checks include:
1. Validating the 'Direction' field to ensure all direction field values in the input layer match the configured forward/backward/both values. Errors will be reported if the direction field value is non-null and does not match one of the configured values.
2. Checking node-to-node separation. This check identifies nodes from the network graph that are closer to other nodes than the specified tolerance distance. This often indicates missed snaps or short segments in the input layer. In the case that a node violates this condition with multiple other nodes, only the closest violation will be reported.
3. Checking node-to-segment separation: This check identifies nodes that are closer to a line segment (e.g. a graph edge) than the specified tolerance distance, without being connected to it. In the case that a node violates this condition with multiple other edges, only the closest violation will be reported.

Two layers are output by this algorithm:
1. An output containing features from the original network layer that failed the direction validation checks.
2. An output representing the problematic node locations with an 'error' field explaining the error. This is a line layer, where the output features join the problematic node to the node or segment that failed the tolerance checks.

**Extract network endpoints**<br />This algorithm extracts the endpoints (nodes) from a network line layer. Two definitions are available for identifying endpoints:
1. Nodes with only all incoming or all outgoing edges: Identifies 'Source' or 'Sink' nodes based on the direction of flow. These are nodes where flow can start (only outgoing) or stop (only incoming).
2. Nodes connected to a single edge: Identifies topological 'dead-ends' or 'dangles', regardless of directionality. This checks if the node is connected to only one other distinct node.

<img src="images/entries/a26779141bcb3e43adeea67400b4666419f3a17f.png" class="img-responsive img-rounded" />

This feature was funded by [City of Canning](https://www.canning.wa.gov.au/)

この機能は [North Road](https://north-road.com/) によって開発されました
### Feature: Add feature preserving raster smoothing algorithm
This is a port of the Whitebox tool's equivalent algorithm, implementing the logic described in Lindsay, John et al (2019): LiDAR DEM Smoothing and the Preservation of Drainage Features.<br />It is effective at removing surface roughness from DEM) without significantly altering sharp features such as breaks-in-slope, stream banks, or terrace scarps.<br />This makes it superior to standard low-pass filters (e.g., mean, median, Gaussian) or resampling, which often blur distinct topographic features.<br />The algorithm works in three steps:
1. Calculating surface normal 3D vectors for each grid cell.
2. Smoothing the normal vector field using a filter that applies more weight to neighbors with similar surface normals (preserving edges).
3. Iteratively updating the elevations in the DEM to match the smoothed normal field.

This feature was funded by [North Road](https://north-road.com/)

この機能は [North Road](https://north-road.com/) によって開発されました
### Feature: Add native raster gaussian blur algorithm
Allows applying a gaussian blur to a raster layer

This feature was funded by [North Road](https://north-road.com/)

この機能は [North Road](https://north-road.com/) によって開発されました
### Feature: Add native total curvature algorithm from the terrain analysis library
Adds the Total curvature algorithm to Processing. The total curvature filter has existed in the terrain analysis library for years, but it was never exposed in the GUI. It is now exposed to the Processing framework alongside the existing terrain analysis filters.

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
### Feature: Expose NODATA and raster creation options for outputs in the terrain analysis tools
Expose output NODATA and raster creation options in the native raster terrain analysis tools (slope, aspect, hillshade, ruggedness index).

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
### Feature: Add Dataset Identification GDAL Processing Algorithm
A new Data Identification algorithm allows for the automated extraction of metadata using GDAL.<br />This algorithm requires GDAL \>= 3.13.0, as it uses the new capabilities of [gdal dataset identify](https://gdal.org/en/stable/programs/gdal_dataset_identify.html).

<img src="images/entries/76dfc1189b899bedaa208692766fc765ccb76175.png" class="img-responsive img-rounded" />

This feature was funded by [QGIS-DE - Anwendergruppe Deutschland e.V.](https://qgis.de/)

This feature was developed by [Even Rouault](https://github.com/rouault)
### Feature: Add a way to specify the raster format in processing algorithm outputs
This feature allows specifying the output format for rasters using GDAL configuration flags, primarily for enforcing Cloud Optimized GeoTiff outputs.<br />In previous versions, the output format was based on file format extension, which breaks for COG since both GDAL GTiff and COG drivers use the extension of `.tif/.tiff`. Users can now explicitly specify `-of COG` to enforce COG exports.

This feature was funded by [QGIS-DE - Anwendergruppe Deutschland e.V.](https://qgis.de/)

This feature was developed by [Even Rouault](https://github.com/rouault)
### Feature: Show the feature count flowing through a model inside the model designer
The long-requested ability to show the number of features flowing through the model has been added. The number of features is attached to the link going in and out between the algorithms, and it only applies to vector layers. The display of the feature count can be disabled using the "Show Feature Count" option in the view menu.<br />Note: To be able to display the feature count, the model needs to be run first at least once.

<img src="images/entries/468164c721e2407abaf86e0629d35377741dc2a6.png" class="img-responsive img-rounded" />

This feature was funded by the QGIS Switzerland user group

この機能は  [Valentin Buira](https://github.com/ValentinBuira) によって開発されました
### Feature: support max-triangle-edge-length in PDAL Export to raster (TIN) algorithm
Support for max-triangle-edge-length parameter has been added to the PDAL Export to raster (TIN) algorithm, so that triangles where the edge length is bigger than the specified threshold can be ignored.<br />This feature needs PDAL \>= 2.6.0 and wrench \>=1.2.2.

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
### Feature: Model designer update
The QGIS Model Designer has had a significant update applied to the way in which it handles the input and output values between nodes to provide visual feedback in much more meaningful ways.<br />Individual parameters for node configuration are now exposed, and the connections between values from tools and variables are connected to nodes at the specific parameters where they are input and output accordingly.<br />Parameter Values are color-coded by data type (including generic data types like integer and string, but also complex QGIS-specific types such as vector and raster layers), allowing for enhanced visual indexing and traceability of data operations as they flow through the model.

<img src="images/entries/92bf8916e1ddc8d0e44b31f130d2029ac93b438f.png" class="img-responsive img-rounded" />

This feature was funded by [Géo2France](https://www.geo2france.fr/portal/public/overview)

This feature was developed by [Jonathan Lurie](https://github.com/jonathanlurie)
### Feature: Allow Reproject Layer algorithm to transform Z coordinates
An optional bool parameter to the *Reproject layer* algorithm has been added that allows for the transformation of Z coordinates.

<img src="images/entries/b93161af43e09fc6189680f8f8b323b86555d499.png" class="img-responsive img-rounded" />

This feature was developed by [Stefanos Natsis](https://github.com/uclaros)
### Feature: Add algorithm to create Cloud Optimized GeoTiffs from directory source
A new algorithm for Create Cloud Optimized GeoTIFF has been added that allows the creation of COGs for a set of input raster files provided in a dedicated folder and uses GDAL to perform a bulk conversion of the input files.

<img src="images/entries/7a822b6086fbf156b8f3528499f78a5d83eb7b29.png" class="img-responsive img-rounded" />

この機能開発には Ocean Winds の資金提供を受けました

この機能は [Jan Caha](https://github.com/JanCaha) によって開発されました
### Feature: Add SFCGAL approximate medial axis processing algorithm
A new processing algorithm to approximate medial axis has been added which is based on the newly integrated SFCGAL backend.<br />The Approximate Medial Axis algorithm generates a simplified skeleton of a shape by approximating its medial axis. The output is a collection of lines that follow the central structure of the shape. The result is a thin, stable set of curves that capture the main topology while ignoring noise. This algorithm ignores the Z dimensions. If the geometry is 3D, the approximate medial axis will be calculated from its 2D projection.

<img src="images/entries/0804299923000a846f55b0b8fb0b50e19e3893d5.png" class="img-responsive img-rounded" />

この機能は [City of Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html) の資金提供で開発されました

This feature was developed by [Jean Felder](https://github.com/ptitjano)
### Feature: Scale and Resolution settings for WMS extraction
QGIS now enables Raster Extraction algorithms to work with WMSs requested at a given scale, so that scale-dependent rendering (symbology/labeling) is preserved in the output raster.<br />The improved algorithms are `Clip raster by extent` and `Clip raster by mask layer`.<br />A new advanced options panel is provided on WMS layers when used as a source in these algorithms, which provides options for:
- **Reference scale**: The scale at which the WMS raster should be requested/rendered.
- **Service resolution**: The resolution (in DPI) used by the server to render the WMS raster (by default 96 dpi).<br />These changes were enabled by the introduction of the `QgsProcessingRasterLayerDefinition` and `QgsWmsUtils` classes.

<img src="images/entries/532bbcaddf65f8d815ecdddd48ed71b067cdb855.png" class="img-responsive img-rounded" />

この機能は [City of Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html) の資金提供で開発されました

This feature was developed by [Germap](https://opengis.ch)
### Feature: Add duplicate features output layer parameter to Delete duplicate geometries Algorithm
This feature extends the "Delete duplicate geometries" processing algorithm so that the identified duplicate features that are deleted can be extracted and saved as a distinct file for further analysis.

<img src="images/entries/85ee1e8469a32c107d2bfc08ec468915399689a7.png" class="img-responsive img-rounded" />

This feature was developed by [Andrea Giudiceandrea](https://github.com/agiudiceandrea)
### Feature: Add algorithms to filter parts by length/area
These new algorithms, "Remove parts by length" and "Remove parts by area", filter out parts of geometries from a vector layer by checking their area or length against a minimum size parameter.<br />If the input geometry is a multipart geometry, then the parts will be filtered by their individual sizes. If no parts match the required minimum size, then the feature will be skipped and omitted from the output layer. If the input geometry is a singlepart geometry, then the feature will be skipped if the geometry's size is below the required size and omitted from the output layer. Attributes are not modified.

<img src="images/entries/a3a539941a16aa0765fd05436e4e7228e3864553.png" class="img-responsive img-rounded" />

This feature was funded by [North Road](https://north-road.com/)

この機能は [North Road](https://north-road.com/) によって開発されました
### Feature: Add optional destination CRS for Package Layers algorithm
Allows for layers to be transformed into a specific output CRS, if set.

This feature was funded by [North Road](https://north-road.com/)

この機能は [North Road](https://north-road.com/) によって開発されました
### Feature: Package Layers algorithm - only export features intersecting a given extent
An optional parameter for `Extent` has been added to the Package Layers algorithm, allowing users to only export features that intersect a given extent from all the selected layers. If none of the features of a specific selected layer intersect the given extent, the layer will still be created and will be empty in the output GeoPackage.

<img src="images/entries/33644c3a135003c6e8df79e9eda8878004b6ea28" class="img-responsive img-rounded" />

この機能は [City of Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html) の資金提供で開発されました

This feature was developed by [Germap](https://github.com/gacarrillor)
### Feature: Unlimited model canvas size in the model designer
Previous versions of the QGIS model designer had a fixed canvas size of 4000 x 4000, and new models were started at the top left of the canvas, which could lead to frustration when elements went out of bounds. The QGIS model builder will now dynamically manage the scroll area and enable a much smoother user experience.

<img src="images/entries/6347778c8c50b9fa330e4985d19b980c2c8b676f.png" class="img-responsive img-rounded" />

This feature was funded by Hauts-de-France region

この機能は  [Valentin Buira](https://github.com/ValentinBuira) によって開発されました
## アプリケーションとプロジェクトのオプション
### Feature: OAuth2 auto refresh
QGIS now includes an auto-refresh mechanism for OAuth2 connections.<br />A cache cleanup to stop the auto refresh is triggered periodically, and when a layer is removed from the project. This is required to avoid unnecessary, endless refreshing of unused tokens.

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
### Feature: Project trust for embedded code enhancement
QGIS now includes a project-level "trust" mechanism that grants or denies execution of embedded Python code within projects. This is implemented in line with the [Trusted Projects and Folders QEP](https://github.com/qgis/QGIS-Enhancement-Proposals/blob/master/qep-336-trusted-projects-and-folders.md).<br />As established in the QEP, the embedded code types covered are:
- macros;
- expression functions;
- actions; and
- attribute form init code

This gives users the ability to allow for granular code execution at the project level instead of global settings limited only by user profile configuration.<br />QGIS will provide users with a project trust dialog to offer the user generic information on what features to allow as well as preview code accordingly. Global settings are provided to allow or deny execution of features at project and path levels.

<img src="images/entries/8325ef4b8268626c5af3c9699370dbeb6faedcd4.png" class="img-responsive img-rounded" />

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### Feature: Elevation Profile Manager
QGIS now links the app handling of elevation profiles to a new project-level elevation profile manager. Now, elevation profiles stored in the project can be reopened after opening a project, and changes made to the profile will be stored in the project.<br />There is also a fully functional elevation profile manager dialog, which is able to display/rename/remove elevation profiles from the project.

This feature was funded by [Erftverband](https://www.erftverband.eu/)

この機能は [North Road](https://north-road.com/) によって開発されました
### Feature: Project/layer metadata localization support
Translation support has been added for some key project and layer metadata values to QGIS' project translation system. This enhancement ensures that project translation can use the relevant metadata values for layout items such as labels, map canvas decorations, etc.<br />*This is funded through an ongoing effort to add support for localized/translated projects into QField*

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### Feature: Add project setting to enable HTML GetFeatureInfo maptip-only mode
A new project setting for QGIS Server is provided to enable HTML GetFeatureInfo maptip-only mode.<br />[This allows QGIS Server to use the WMS vendor parameter](https://docs.qgis.org/3.40/en/docs/server_manual/services/wms.html#with-maptip) `WITH_MAPTIP=HTML_FI_ONLY_MAPTIP` and use only the maptip for the HTML GetFeatureInfo response.

<img src="images/entries/5cefab81d09c5bf0e1b757238d74940a2c9d9c55" class="img-responsive img-rounded" />

This feature was developed by [Björn Hinkeldey](https://github.com/pathmapper)
## Profile Plots
### Feature: Add option to sync elevation profile layers with project layers
This new option is available from an elevation profile's settings menu as "Synchronize Layers to Project". It is unchecked by default, but when checked, the elevation profile's layers will always exactly match the project's main canvas layer structure, including groups and layer orders.<br />Groups cannot be created in the elevation profile. Any changes made to the main project's layer tree will immediately be reflected in the elevation profile's layer setup.

This feature was funded by [Lutra](https://www.lutraconsulting.co.uk/)

この機能は [North Road](https://north-road.com/) によって開発されました
### Feature: Render point cloud as a continuous elevation line
QGIS profile plots now include the ability for the elevation profile of a point cloud layer to be displayed as a continuous elevation line instead of individual points, allowing point clouds to be rendered similarly to vector or raster layers. Users can adjust the tolerance setting to improve results when too few points are present within the view, without triangulating the entire layer

<img src="images/entries/ab52589956629cc34cb09bef22e63478a65a96bf.png" class="img-responsive img-rounded" />

この機能開発は [Danish Agency for Climate Data](https://www.klimadatastyrelsen.dk/) からの資金提供を受けました

この機能は [Dominik Cindric (Lutra Consulting)](https://github.com/ViperMiniQ) によって開発されました
### Feature: Show distance:elevation scale ratio in profile settings menu
A new widget has been added for the displaying of the current distance:elevation scale ratio for elevation profile plots. The widget can also be used to set a specific ratio. If the "lock" option is enabled for the plot, then this scale ratio will be used instead of the default 1:1 ratio when zooming and navigating the plot.

<img src="images/entries/a4300b20ef89e4ad71f70a114af7438e4eff9cfb" class="img-responsive img-rounded" />

This feature was funded by [Erftverband](https://www.erftverband.eu/)

この機能は [North Road](https://north-road.com/) によって開発されました
## ブラウザ
### Feature: Move multiple tables in Database to another Schema
Allow multiple tables to be moved into the specified schema at once.

この機能開発には Ocean Winds の資金提供を受けました

この機能は [Jan Caha](https://github.com/JanCaha) によって開発されました
### Feature: Browser DB Table Comment
The QGIS Browser now includes the option to directly edit **Table comment** for databases that support this functionality.

<img src="images/entries/84b05ee5021e434fc16c6bc60bb1695584de7ecb.png" class="img-responsive img-rounded" />

この機能開発には Ocean Winds の資金提供を受けました

この機能は [Jan Caha](https://github.com/JanCaha) によって開発されました
### Feature: Add create or delete Spatial Index to the Manage menu in Browser
A new context menu option has been added to **create** or **delete** Spatial Indexes on providers that support it.

<img src="images/entries/797d36c2dd01a3e0120c3835d360861033d5b516.png" class="img-responsive img-rounded" />

この機能開発には Ocean Winds の資金提供を受けました

この機能は [Jan Caha](https://github.com/JanCaha) によって開発されました
## データプロバイダ
### Feature: Add support for GML as a feature format for OAPIF
The OGC API for Features source configuration now includes support for GML outputs. Users may select it in the combo box in the "Modify WFS Connection" dialog if the server exposes it as a feature format.<br />Several scenarios are supported:
- Sources can be accessed with or without an XML schema available (through a rel=describedby link). As with WFS, the XML schema can be examined with the QGIS simple schema parser, or with GDAL GMLAS one, depending on the selected "Feature mode".
- Features can be retrieved with or without a bulk download link available (provided through a rel=enclosure link)

This feature was developed by [Even Rouault](https://github.com/rouault)
### Feature: Allow OAPIF users to select an alternate format than GeoJSON with which to download features
Feature Services served from OGC API for Features sources that honour the `outputFormat` parameter in connection URIs should support additional output formats for retrieving features (e.g., FlatGeoBuf, GeoJSON, etc.). This allows users to select feature retrieval options other than GeoJSON from sources that support it for improved performance, compatibility, or extensibility according to their needs.<br />In the service connection dialog, users can use the new combo box to select their preferred output format. In addition, a new global setting for configuring "lastFeatureFormatEncoding" allows the previously defined value as the default for new connections.

<img src="images/entries/3f0add13c921416314030ca3f9ff12118dd288b2.png" class="img-responsive img-rounded" />

This feature was funded by [QGIS-DE - Anwendergruppe Deutschland e.V.](https://qgis.de/)

This feature was developed by [Even Rouault](https://github.com/rouault)
### Feature: Allow update and delete for Field Domains in GPKG
New menu items allow users to update and delete Field Domains on GPKG data sources. Requires GDAL \>= 3.12

<img src="images/entries/3e5c8b252b192ecd9022ac7a0a638307c46bc52f.png" class="img-responsive img-rounded" />

この機能開発には Ocean Winds の資金提供を受けました

この機能は [Jan Caha](https://github.com/JanCaha) によって開発されました
### Feature: Save and import QGIS projects to PostgreSQL via Browser
QGIS now natively supports the ability to save the current QGIS project to a PostgreSQL database, as well as import QGIS projects from a folder into a PostgreSQL database.<br />Two new menu entries for PostgreSQL connections are added:
- One for saving the currently opened QGIS project directly to the schema.
- The second item allows batch import of QGIS projects to the schema. Project names are checked for name collisions, and autoincrementing suffix values (e.g. `_1`, `_2`, etc.) are added if the project name already exists in the schema.

<img src="images/entries/b139e1711b8d62c9064db1df0e8bce5b242cea96.png" class="img-responsive img-rounded" />

この機能開発には Ocean Winds の資金提供を受けました

この機能は [Jan Caha](https://github.com/JanCaha) によって開発されました
### Feature: Add Layer Properties info to PostgreSQL provider
QGIS includes additional information in the **Layer Properties** for PostgreSQL layers, including:
- Privileges for the user regarding the table
- Estimation of rows
- Information about spatial indexes

<img src="images/entries/37e33067b2665adbfd5202b1825df30a71b1ce37.png" class="img-responsive img-rounded" />

この機能開発には Ocean Winds の資金提供を受けました

この機能は [Jan Caha](https://github.com/JanCaha) によって開発されました
### Feature: Add auth method for Planetary computer
A new auth method is provided for use with the Microsoft Planetary Computer STAC catalog. The planetary computer requires using SAS sign tokens to access most assets' data, something that was implemented on the old STAC plugin but was missing from the core STAC implementation.<br />There are two modes for the new auth method:
- One is for the Open version of Planetary Computer, performing the SAS signing for assets
- The second is for Planetary Computer Pro GeoCatalogs, where, in addition to the SAS signing of assets, an OAuth2 authentication is also required<br />The new auth method can be used with STAC connections, or applied directly to individual gdal or point cloud layers whose data source is on the planetary computer. When a layer is added from a STAC catalog or directly using the data source manager, the `authcfg` will be appended to its URI so QGIS will use that config for the network requests. Authcfg encoding/decoding was also added to point cloud layers.

<img src="images/entries/0ed79ce1c54933c720853f364cdd505ea4292261.png" class="img-responsive img-rounded" />

This feature was funded by Microsoft

この機能は [Stefanos Natsis (Lutra Consulting)](https://github.com/uclaros) によって開発されました
### Feature: QGIS Project Versioning in PostgreSQL
For QGIS Projects that leverage the functionality to be stored directly in PostgreSQL, automatic version control can be enabled, which allows users to save, load, edit, and restore historic copies of their project. The process is mostly handled by a function and a trigger operation in the PostgreSQL Database, and multiple new menu items and dialogs have been provided to allow users granular control over the version management process.

<img src="images/entries/e6362175a8d1662e590efecd2b1e48f62ec79c51.png" class="img-responsive img-rounded" />

この機能開発には Ocean Winds の資金提供を受けました

この機能は [Jan Caha](https://github.com/JanCaha) によって開発されました
### Feature: Store connections available and default image format
Stores in the settings the preferred format for a WMS connection.

Allows to detect the formats actually advertized by the server and stores them in the settings for future use.

<img src="images/entries/9736fdc6bcb34c3bbdf6d85cf3d9eaa567176313.png" class="img-responsive img-rounded" />

This feature was funded by [QGIS-DE - Anwendergruppe Deutschland e.V.](https://qgis.de/)

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
## QGISサーバー
### Feature: Try to reload invalid project layers
In QGIS Server, there is an option to ignore bad layers; however, layers identified as bad may become available later on, such as a failed network service that recovers (web server/ database, etc.).<br />QGIS Server therefore has a new option for `QGIS_SERVER_RETRY_BAD_LAYERS`. If this option is set to true, the server checks upon each request if the bad layers are available again. If a layer is available, it is marked as valid and will be used by the server.

This feature was funded by Stadtwerke München (SWM)

This feature was developed by [mhugent](https://github.com/mhugent)
### Feature: Implement GetFeatureInfo for mesh layers
QGIS Server now provides responses for GetFeatureInfo requests on Mesh Layers.

<img src="images/entries/fd8d94bd934381d9c5670b78bba29159ddcfcf93.png" class="img-responsive img-rounded" />

This feature was developed by [Jorge Gustavo Rocha](https://github.com/jgrocha)
### Feature: OAPIF URL root path configuration option
Make the OAPIF service root path configurable through a new server setting<br />QGIS_SERVER_API_WFS3_ROOT_PATH

Change the default from “/wfs3” to “/ogcapi”.

This feature was funded by [QGIS-DE - Anwendergruppe Deutschland e.V.](https://qgis.de/)

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
## プログラム可能
### Feature: Add support for area3D to QgsGeometry
The QgsGeometry Class is extended to include `area3D`, which is the 3-dimensional surface area of the geometry.
- For a Point or a LineString, it is always equal to 0.
- For a Polygon, it is equal to the 3D area of the exterior ring minus the 3d area of the interior rings.
- For a Polyhedral and a TIN, it is equal to the sum of the 3d areas of all its patches.
- For a GeometryCollection, it is equal to the sum of the 3d areas of all its geometries.

This feature was developed by [Jean Felder](https://github.com/ptitjano)
### Feature: Add support for 3d points in pointsAreCollinear method of QgsGeometryutils
Previous versions of the `QgsGeometryUtilsBase::pointsAreCollinear` method only worked for 2D points; it has now been extended to support 2D and 3D points and calls the corresponding `QgsGeometryUtilsBase` function. A new `QgsGeometryUtilsBase::points3DAreCollinear` has also been introduced, which works for 3D points.

この機能は [City of Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html) の資金提供で開発されました

This feature was developed by [Jean Felder](https://github.com/ptitjano)
### Feature: Implement QgsVectorLayer.as_geopandas()
The PyQgis API now provides a method to natively convert QgsVectorLayer objects to Geopandas dataframes, including the attributes. Note that this requires the GeoPandas library as a dependency in the QGIS Environment.

<img src="images/entries/cf6f4588f8da7d899a519e10117847b68fcbe292.png" class="img-responsive img-rounded" />

この機能は [Till Frankenbach](https://github.com/merydian) によって開発されました
### Feature: Expose 3D map tools to PyQgis API
Users can now create custom map tools to interact with the 3D map canvas using the `Qgs3DMapTool` base class.

This feature was funded by [SIGNON Deutschland GmbH](https://signon-group.com/en)

This feature was developed by [Stefanos Natsis](https://github.com/uclaros)
### Feature: Expose 3D map canvas cross section mode to PyQgis API
The 3D *Cross section tool* functionality is now exposed to the PyQgis API. One can now easily create and apply the four clipping planes to a 3D map view using Python and a 3D view's map coordinates.

This feature was funded by [SIGNON Deutschland GmbH](https://signon-group.com/en)

This feature was developed by [Stefanos Natsis](https://github.com/uclaros)
### Feature: Refactor ray casting and expose to PyQgis API
The duplicated `Ray3D` class has been removed in favor of `QgsRay3D`, which has had missing methods added accordingly. The exposure of `Qgs3DMapCanvas::castRay()` to the PyQgis API will effectively allow Python plugins to perform ray casting in 3D map canvases and manage the resulting hits.

This feature was funded by [SIGNON Deutschland GmbH](https://signon-group.com/en)

This feature was developed by [Stefanos Natsis](https://github.com/uclaros)
### Feature: TemplatedLineSymbolLayer to enable blank areas implementation
The QGIS API was extended to support the implementation of blank area operations in line with [QEP \#345](https://github.com/qgis/QGIS-Enhancement-Proposals/pull/345).

この機能は [City of Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html) の資金提供で開発されました

This feature was developed by [Julien Cabieces](https://github.com/troopa81)
### Feature: Port Hub distance algorithm to C++
The Processing Hub distance algorithm has been ported from Python to C++.<br />This algorithm replaces Distance to nearest hub (points) and Distance to nearest hub (line to hub) algorithms as it produces two optional outputs as these two algorithms. The original algorithms are marked as deprecated.

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
### Feature: Add support for SFCGAL library
Native support for SFCGAL, an advanced geometric computations library, has been added to QGIS in line with [QEP \#340](https://github.com/qgis/QGIS-Enhancement-Proposals/pull/340).<br />This feature adds two primary additional classes to the QGIS API:
- QgsSfcgalEngine: Exposes SFCGAL C API to QGIS. Also adds memory and error management.
- QgsSfcgalGeometry: Keeps a handle to SFCGAL geometry representation to reduce geometry conversion between QGIS and SFCGAL<br />Developed with support from:
- CEA/DAM
- CP4SC/France Relance/European Union
- Stadt Frankfurt am Main
- Oslandia
- OPENGIS.ch

この機能は [City of Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html) の資金提供で開発されました

This feature was developed by [Benoit D.-M. - oslandia](https://github.com/benoitdm-oslandia)
## 注目すべき修正
### Feature: Bug fixes by Alessandro Pasotti (QCooperative)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.40バックポートコミット（GitHub） |
| --- | --- | --- | --- |
| QGIS Server won't render VRT in WMS requests | [\#64733](https://github.com/qgis/QGIS/issues/64733) | Not a bug: local issue with setting the environment |  |
| QGIS Server ignores MAP override when QGIS_PROJECT_FILE is set | [\#64723](https://github.com/qgis/QGIS/issues/64723) | Won't fix (not a bug) |  |
| Server: landingpage webapp only functions if built with server python plugins support | [\#64556](https://github.com/qgis/QGIS/issues/64556) | [PR \#64763](https://github.com/qgis/QGIS/pull/64763) | No |
| Raster calculator fails when OpenCL acceleration is turned on | [\#64574](https://github.com/qgis/QGIS/issues/64574) | [PR \#64779](https://github.com/qgis/QGIS/pull/64779) | No |
| Singleband Gray Shader should create 32 bit values not just 16 bit | [\#64560](https://github.com/qgis/QGIS/issues/64560) | Won't fix (not a bug) |  |
| Virtual raster provider memory leak - memory not released until QGIS closed | [\#64559](https://github.com/qgis/QGIS/issues/64559) | [PR \#64785](https://github.com/qgis/QGIS/pull/64785) | TODO |
| \[gdal\] Consider mask bands as a normal alpha band | [\#64642](https://github.com/qgis/QGIS/issues/64642) | [PR \#64795](https://github.com/qgis/QGIS/pull/64795) |  |
| Raster Attribute Table for S-102 does not display correctly | [\#64797](https://github.com/qgis/QGIS/issues/64797) | [PR \#64811](https://github.com/qgis/QGIS/pull/64811) | TODO |
| Arrow symbol layer data-defined properties not using defaults for NULL |  | [PR \#64680](https://github.com/qgis/QGIS/pull/64680), [PR \#64828](https://github.com/qgis/QGIS/pull/64828) |  |
| "Reuse last entered value" not applied when using PyQGIS | [\#64655](https://github.com/qgis/QGIS/issues/64655) | Won't fix (not a bug) |  |
| SpatiaLite provider returns wrong schema for views (caches columns from underlying joined tables instead of view definition) | [\#64742](https://github.com/qgis/QGIS/issues/64742) | [PR \#64902](https://github.com/qgis/QGIS/pull/64902) | TODO |
| Updated Canvas gives inconsistent Min / Max values and colour ranges for a local raster vs. the same raster in postgres | [\#64917](https://github.com/qgis/QGIS/issues/64917) | [PR \#64953](https://github.com/qgis/QGIS/pull/64953) | [PR \#64998](https://github.com/qgis/QGIS/pull/64998) |
| Bands get cleared after attribute table creation fails, causing rendering issues and crashes | [\#65040](https://github.com/qgis/QGIS/issues/65040) | [PR \#65052](https://github.com/qgis/QGIS/pull/65052) |  |
| \[ogr\]\[gpkg\] Fix wrong row count when attribute filter | [\#65067](https://github.com/qgis/QGIS/issues/65067) | [PR \#65097](https://github.com/qgis/QGIS/pull/65097) | No |
| \[ogr\] Add OGR_L_GetAttributeFilter | [\#65067](https://github.com/qgis/QGIS/issues/65067) | [PR \#14005](https://github.com/OSGeo/gdal/pull/14005) | N/A |
| visualizing GDAL raster with band scale and offset values will introduce very large histograms into the raster | [\#59461](https://github.com/qgis/QGIS/issues/59461) | [PR \#63294](https://github.com/qgis/QGIS/pull/63294) |  |
| Rendering of PostGIS rasters ignores Transparency NoData value setting | [\#63171](https://github.com/qgis/QGIS/issues/63171) | [PR \#63258](https://github.com/qgis/QGIS/pull/63258) | はい |
| Add additional QStringLiteral entries to SQLite utils | [\#50553](https://github.com/qgis/QGIS/issues/50553) | [PR \#63105](https://github.com/qgis/QGIS/pull/63105) |  |
| 'Fixed Interval' and 'Pretty Breaks' Graduated Renderers don't work when field has all the same values | [\#63277](https://github.com/qgis/QGIS/issues/63277) | [PR \#63298](https://github.com/qgis/QGIS/pull/63298) |  |
| Identify Features tool ignores Transparency NoData value setting on PostGIS rasters | [\#63133](https://github.com/qgis/QGIS/issues/63133) | [PR \#63321](https://github.com/qgis/QGIS/pull/63321) |  |
| Raise warning when trying to modify read-only layer with field calculator | [\#63111](https://github.com/qgis/QGIS/issues/63111) | [PR \#63337](https://github.com/qgis/QGIS/pull/63337) |  |
| QGIS Server does not list one layer in WMS GetCapabilities if datum transformation is used | [\#61293](https://github.com/qgis/QGIS/issues/61293) | Cannot reproduce (again) |  |
| QGIS Server Layer(s) not valid Exception with multiple projects using same WMS Layer | [\#62608](https://github.com/qgis/QGIS/issues/62608) | 再現できません |  |
| Adjusting min/max cumulative count cuts for rasters in layer styling panel | [\#63075](https://github.com/qgis/QGIS/issues/63075) | Cannot reproduce (feedback) |  |
| Refresh layer at interval has no effect after loading project | [\#63007](https://github.com/qgis/QGIS/issues/63007) | [PR \#63389](https://github.com/qgis/QGIS/pull/63389) |  |
| Browser not showing CurvePolygons in LTR or Latest |  | [PR \#63404](https://github.com/qgis/QGIS/pull/63404) |  |
| Copy one style category and paste it collectively to multiple layers removes the settings of the other style categories | [\#63167](https://github.com/qgis/QGIS/issues/63167) | [PR \#63408](https://github.com/qgis/QGIS/pull/63408) |  |
| Value relation widget does excessive calls to PostGIS database | [\#63410](https://github.com/qgis/QGIS/issues/63410) | [PR \#63418](https://github.com/qgis/QGIS/pull/63418) |  |
| Adding a network file vector layer ends with a lot of server calls for the same data | [\#63407](https://github.com/qgis/QGIS/issues/63407) | Cannot reproduce (feedback) |  |
| Sld export error with expression based labels | [\#63402](https://github.com/qgis/QGIS/issues/63402) | [PR \#63419](https://github.com/qgis/QGIS/pull/63419) |  |
| Selective pasting style does not change the ‘Automatically insert into print layout legend elements’ setting in raster layers | [\#63346](https://github.com/qgis/QGIS/issues/63346) | [PR \#63430](https://github.com/qgis/QGIS/pull/63430) |  |
| Value Relation with current_value() not updating when changes made outside of the attribute form | [\#63448](https://github.com/qgis/QGIS/issues/63448) | [PR \#63468](https://github.com/qgis/QGIS/pull/63468) |  |
| @current_feature VS @feature | [\#63488](https://github.com/qgis/QGIS/issues/63488) | Not a code bug (maybe documentation) |  |
| Qgis Desktop does not honor layer order in get capabilites in external wms | [\#62918](https://github.com/qgis/QGIS/issues/62918) | [PR \#63492](https://github.com/qgis/QGIS/pull/63492) |  |
| Using "Subset filter" from the "Execute SQL" dialog is not applied | [\#62542](https://github.com/qgis/QGIS/issues/62542) | [PR \#63605](https://github.com/qgis/QGIS/pull/63605) |  |
| SQL editor allow undo after clear | [mail thread](https://lists.osgeo.org/pipermail/qgis-developer/2025-October/067839.html) | [PR \#63621](https://github.com/qgis/QGIS/pull/63621) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Alessandro Pasotti (QCooperative)](https://www.qcooperative.net/)
### Feature: Bug fixes by Even Rouault (Spatialys)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.40バックポートコミット（GitHub） |
| --- | --- | --- | --- |
| qgis/gdal garbage collection causes segfault | [\#58724](https://github.com/qgis/QGIS/issues/58724) | [PR \#64766](https://github.com/qgis/QGIS/pull/64766) | No |
| NetCDF with EPSG:3416 misaligned is latest qgis ltr | [\#64873](https://github.com/qgis/QGIS/issues/64873) | [PR \#13886](https://github.com/OSGeo/gdal/pull/13886) | N/A |
| Bug in QgsVectorFileWriter when providing the name of the FID field | [\#63320](https://github.com/qgis/QGIS/issues/63320) | [PR \#64878](https://github.com/qgis/QGIS/pull/64878) | [PR \#64903](https://github.com/qgis/QGIS/pull/64903) |
| QgsVectorFileWriter: fix writing NurbsCurve to OGR, by converting them to LineString | 未報告 | [PR \#64906](https://github.com/qgis/QGIS/pull/64906) | N/A |
| Build issue on NixOS | [\#64937](https://github.com/qgis/QGIS/issues/64937) | 無効 |  |
| Float16 rasters do not render correctly | [\#64923](https://github.com/qgis/QGIS/issues/64923) | [PR \#64990](https://github.com/qgis/QGIS/pull/64990) | [PR \#65024](https://github.com/qgis/QGIS/pull/65024) |
| building master in pkgsrc; mostly ok! | [mail thread](https://lists.osgeo.org/pipermail/qgis-developer/2026-February/068072.html) | バグではない |  |
| Rasters with GCPs and overviews render incorrectly when zoomed out | [\#65011](https://github.com/qgis/QGIS/issues/65011) | [PR \#13968](https://github.com/OSGeo/gdal/pull/13968) | N/A |
| Huge Performance Regression using VRTs on Versions \> 3.40.6 | [\#63293](https://github.com/qgis/QGIS/issues/63293) | [PR \#13116](https://github.com/OSGeo/gdal/pull/13116) | N/A (GDAL fix) |
| Problème lecture shapefile | [\#63787](https://github.com/qgis/QGIS/issues/63787) | [PR \#4599](https://github.com/OSGeo/PROJ/pull/4599) | N/A (PROJ fix) |
| USE_PRECOMPILED_HEADERS related issue | [mail thread](https://lists.osgeo.org/pipermail/qgis-developer/2025-November/067871.html) | [PR \#63794](https://github.com/qgis/QGIS/pull/63794) | [PR \#63811](https://github.com/qgis/QGIS/pull/63811) |
| Crash trying to open a shapefile | [\#63826](https://github.com/qgis/QGIS/issues/63826) | [PR \#13350](https://github.com/OSGeo/gdal/pull/13350) | N/A (GDAL fix) |
| Replace all remaining uses of connect(,SIGNAL,,SLOT) in src/ | 未報告 | [PR \#63832](https://github.com/qgis/QGIS/pull/63832) | N/A |
| Crash with invalid WMS/WMTS source | [\#62372](https://github.com/qgis/QGIS/issues/62372) | [PR \#63833](https://github.com/qgis/QGIS/pull/63833) | [PR \#64016](https://github.com/qgis/QGIS/pull/64016) |
| JSON column from GeoPackage is not read correctly | [\#62377](https://github.com/qgis/QGIS/issues/62377) | No longer reproducible / likely fixed |  |
| Fix build warnings on Fedora | 未報告 | [PR \#63910](https://github.com/qgis/QGIS/pull/63910) | N/A |
| Fix cppcheck missingOverride and functionConst warnings | 未報告 | [PR \#63913](https://github.com/qgis/QGIS/pull/63913) | N/A |
| \[CI\] Port OGC tests to ubuntu:25.10 Qt6 | 未報告 | [PR \#64135](https://github.com/qgis/QGIS/pull/64135) | N/A |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Even Rouault (Spatialys)](https://www.spatialys.com/)
### Feature: Bug fixes by Julien Cabieces (Oslandia)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.40バックポートコミット（GitHub） |
| --- | --- | --- | --- |
| pyqt5_to_pyqt6.py: Some known incompatibilities do not lead to error exit code | [\#62559](https://github.com/qgis/QGIS/issues/62559) | [PR \#63526](https://github.com/qgis/QGIS/pull/63526) | No |
| \[PyQt5_to_PyQt6\] Fix all imports coming from Qt module | 未報告 | [PR \#63565](https://github.com/qgis/QGIS/pull/63565) |  |
| QgsLayoutExporter.exportToPdf() does not have the same return value type if an iterator is passed or not | [\#62501](https://github.com/qgis/QGIS/issues/62501) | Won't fix? |  |
| Broken themes in geospatial PDF | [\#62014](https://github.com/qgis/QGIS/issues/62014) | [PR \#63580](https://github.com/qgis/QGIS/pull/63580) | TODO |
| pyqt5_to_pyqt6.py produces broken syntax for imports | [\#64185](https://github.com/qgis/QGIS/issues/64185) | [PR \#64926](https://github.com/qgis/QGIS/pull/64926) | [PR \#64941](https://github.com/qgis/QGIS/pull/64941) |
| pyqt5_to_pyqt6.py does not catch "from PyQt5 import QtWidgets" etc | [\#63711](https://github.com/qgis/QGIS/issues/63711) | [PR \#64930](https://github.com/qgis/QGIS/pull/64930) | [PR \#64939](https://github.com/qgis/QGIS/pull/64939) |
| The "Session Role" function is not applied to loaded layers | [\#62930](https://github.com/qgis/QGIS/issues/62930) | 修正済み |  |
| set session role not working on creation of tables and schema | [\#63866](https://github.com/qgis/QGIS/issues/63866) | 複製に失敗する |  |
| Layout export to GeoPDF: incorrect layers' order when a "PDF Group" is set | [\#63475](https://github.com/qgis/QGIS/issues/63475) | [PR \#64983](https://github.com/qgis/QGIS/pull/64983) | TODO |
| pyqt5_to_pyqt6.py: Some suggestions reference wrong class | [\#64462](https://github.com/qgis/QGIS/issues/64462) | [PR \#64989](https://github.com/qgis/QGIS/pull/64989) | TODO |
| \[GeoPdfExport\] Avoid map theme contaminate non-map-theme items | Reported directly without issue | [PR \#65008](https://github.com/qgis/QGIS/pull/65008) | [PR \#65108](https://github.com/qgis/QGIS/pull/65108) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Julien Cabieces (Oslandia)](https://oslandia.com/en/)
### Feature: Bug Fixes by Denis Rouzaud (OPENGIS)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.40バックポートコミット（GitHub） |
| --- | --- | --- | --- |
| Attribute table forced to be dockable and non modal - Crash several times | [\#62416](https://github.com/qgis/QGIS/issues/62416) | [PR \#64954](https://github.com/qgis/QGIS/pull/64954) | [PR \#64954](https://github.com/qgis/QGIS/pull/64954) |
| \- | \- | [PR \#65055](https://github.com/qgis/QGIS/pull/65055) | ? |
| With composite foreign keys, all widgets are configured by default | [\#32048](https://github.com/qgis/QGIS/issues/32048) | [PR \#65059](https://github.com/qgis/QGIS/pull/65059) | いいえ |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Denis Rouzaud (OPENGIS)](https://opengis.ch/)
### Feature: Bug Fixes by Germán Carrillo (OPENGIS)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.40バックポートコミット（GitHub） |
| --- | --- | --- | --- |
| Project functions in editor, save doesn't really save...? | [\#62752](https://github.com/qgis/QGIS/issues/62752) | [PR \#63425](https://github.com/qgis/QGIS/pull/63425) |  |
| Diagram properties related to variables and expressions are not saved | [\#62936](https://github.com/qgis/QGIS/issues/62936) | [PR \#63479](https://github.com/qgis/QGIS/pull/63479) |  |
| Crash in layer styling panel when closing a project if DD Property Assistant is open | 未報告 | [PR \#63549](https://github.com/qgis/QGIS/pull/63549) |  |
| QGIS crashes when opening print layout | [\#64218](https://github.com/qgis/QGIS/issues/64218) | [PR \#64813](https://github.com/qgis/QGIS/pull/64813) | N/A |
| Fix custom node initialization for custom elevation profiles | [\#65058](https://github.com/qgis/QGIS/issues/65058) | [PR \#64762](https://github.com/qgis/QGIS/pull/64762) | N/A |
| Diagrams: histograms with only negative values don't render | [\#63980](https://github.com/qgis/QGIS/issues/63980) | [PR \#64992](https://github.com/qgis/QGIS/pull/64992) | [PR \#65211](https://github.com/qgis/QGIS/pull/65211) |
| Attributes Form is not the same when called via GUI or when called via PyQGIS | [\#65010](https://github.com/qgis/QGIS/issues/65010) | バグではない |  |
| Layers added using a .qlr file cannot be added to an open Elevation Profile View | [\#58533](https://github.com/qgis/QGIS/issues/58533) | 修正済み |  |
| Group title not updated in .qgs | [\#65085](https://github.com/qgis/QGIS/issues/65085) | Invalid bug, issue related to a plugin |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

この機能は [Germán Carrillo (OPENGIS)](https://opengis.ch/) によって開発されました
### Feature: Bug Fixes by Till Frankenbach (OPENGIS)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.40バックポートコミット（GitHub） |
| --- | --- | --- | --- |
| Tabbing to start of custom formatted Date/Time field in attribute form not working | [\#65022](https://github.com/qgis/QGIS/issues/65022) | [PR \#65023](https://github.com/qgis/QGIS/pull/65023) |  |
| Plugin manager shows changelog of current version, even for upgradable plugins | [\#64792](https://github.com/qgis/QGIS/issues/64792) | tbd |  |
| QGIS does not request default style for WMS layer when in group/container | [\#63754](https://github.com/qgis/QGIS/issues/63754) | [PR \#65081](https://github.com/qgis/QGIS/pull/65081) |  |
| Several issues with a temporal WMS (only one image is displayed using the Temporal Controller) I | [\#64099](https://github.com/qgis/QGIS/issues/64099) | [PR \#64925](https://github.com/qgis/QGIS/pull/64925) |  |
| Several issues with a temporal WMS (only one image is displayed using the Temporal Controller) II | [\#64099](https://github.com/qgis/QGIS/issues/64099) | [PR \#64863](https://github.com/qgis/QGIS/pull/64863) |  |
| \[mvt\] WMS raster sources are not working | [\#61040](https://github.com/qgis/QGIS/issues/61040) | [PR \#65087](https://github.com/qgis/QGIS/pull/65087) |  |
| Add unit tests for unzip function in pyplugin installer | Requested in [PR \#65051](https://github.com/qgis/QGIS/pull/65051) | [PR \#65119](https://github.com/qgis/QGIS/pull/65119) |  |
| Fix WMTS-T layers temporal capabilities resourceURL selection | [\#54043](https://github.com/qgis/QGIS/issues/54043) | [PR \#65190](https://github.com/qgis/QGIS/pull/65190) |  |
| Set selected section to the first section on focus in QgsDateTimeEdit | [\#65022](https://github.com/qgis/QGIS/issues/65022) | [PR \#65023](https://github.com/qgis/QGIS/pull/65023) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Till Frankenbach (OPENGIS)](https://opengis.ch/)
### Feature: Bug fixes by Stefanos Natsis (LutraConsulting)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.40バックポートコミット（GitHub） |
| --- | --- | --- | --- |
| 'Identify' function in a 'QgsMapToolIdentify' descendant crashes | [\#61372](https://github.com/qgis/QGIS/issues/61372) |  |  |
| VPC Virtual Point Cloud - Do not show the point cloud or really lately in Vue2D | [\#59793](https://github.com/qgis/QGIS/issues/59793) |  |  |
| Curl SSL error | [\#33](https://github.com/PDAL/wrench/issues/33) |  |  |
| VPC Virtual Point Cloud - Error when creating VPC from HTTPS/URI sources | [\#59802](https://github.com/qgis/QGIS/issues/59802) | [PR \#66](https://github.com/PDAL/wrench/pull/66) |  |
| LAS/LAZ file without CRS fails to load | [\#50438](https://github.com/qgis/QGIS/issues/50438) |  |  |
| PDAL prevents LAS/LAZ 1.4 from opening if global_encoding set as 1 | [\#51862](https://github.com/qgis/QGIS/issues/51862) |  |  |
| Fix 3d view shortcuts | 未報告 | [PR \#63523](https://github.com/qgis/QGIS/pull/63523) |  |
| Fix zooming with right mouse button in 3D views | 未報告 | [PR \#63537](https://github.com/qgis/QGIS/pull/63537) |  |
| Fix 3d point lights | 未報告 | [PR \#63525](https://github.com/qgis/QGIS/pull/63525) |  |
| 3D map view does not update on layer filter changes | [\#62925](https://github.com/qgis/QGIS/issues/62925) | [PR \#63477](https://github.com/qgis/QGIS/pull/63477) | [PR \#63511](https://github.com/qgis/QGIS/pull/63511) |
| Fix 2d rendering of remote COPC files in virtual point clouds | [comment](https://github.com/qgis/QGIS/issues/59793#issuecomment-3351352812) | [PR \#63471](https://github.com/qgis/QGIS/pull/63471) |  |
| 3D Tiles in 3D View: Loading 2 tiles | [\#63340](https://github.com/qgis/QGIS/issues/63340) | [PR \#63469](https://github.com/qgis/QGIS/pull/63469) |  |
| 3.44.1 hangs after exporting 256 images of 3D animation | [\#62959](https://github.com/qgis/QGIS/issues/62959) | [PR \#63469](https://github.com/qgis/QGIS/pull/63469) |  |
| Update untwine to 1.5.1 |  | [PR \#63543](https://github.com/qgis/QGIS/pull/63543) |  |
| Update pdal_wrench to 1.2.2 from upstream |  | [PR \#63544](https://github.com/qgis/QGIS/pull/63544) |  |
| Update MDAL to 1.3.2 from upstream |  | [PR \#63546](https://github.com/qgis/QGIS/pull/63546) |  |
| \[3D\] Avoid clamping vertices to actual nodata value | 未報告 | [PR \#64845](https://github.com/qgis/QGIS/pull/64845) |  |
| Data corruption using "Split Features" on a LineStringZ in GeoJSON | [\#63581](https://github.com/qgis/QGIS/issues/63581) | [PR \#64986](https://github.com/qgis/QGIS/pull/64986) | 保留中 |
| Changing styling of a VPC layer resets the previous styling | [\#59419](https://github.com/qgis/QGIS/issues/59419) | [PR \#64988](https://github.com/qgis/QGIS/pull/64988) | [PR \#65020](https://github.com/qgis/QGIS/pull/65020) |
| Fix sip_include.sh after pyqt5 removal | 未報告 | [PR \#64974](https://github.com/qgis/QGIS/pull/64974) | N/A |
| Make the extent widget hold the full precision of the chosen extent | 未報告 | [PR \#64919](https://github.com/qgis/QGIS/pull/64919) |  |
| Fix endless terrain levels generation | 未報告 | [PR \#64875](https://github.com/qgis/QGIS/pull/64875) |  |
| Always check pointer initialized inside if initializer | 未報告 | [PR \#64871](https://github.com/qgis/QGIS/pull/64871) |  |
| No "Style manager" tab for point clouds in Layer styling panel | [\#64789](https://github.com/qgis/QGIS/issues/64789) | [PR \#64868](https://github.com/qgis/QGIS/pull/64868) |  |
| Tidy includes in point clouds and 3d code | 未報告 | [PR \#64820](https://github.com/qgis/QGIS/pull/64820) |  |
| Remove code for QT version \< 6.6 | 未報告 | [PR \#64809](https://github.com/qgis/QGIS/pull/64809) |  |
| Plugin installer can leave a plugin in a broken state on failed upgrade | [\#64790](https://github.com/qgis/QGIS/issues/64790) | [PR \#64807](https://github.com/qgis/QGIS/pull/64807) | TODO |
| Avoid module wide QtConcurrent imports | 未報告 | [PR \#64775](https://github.com/qgis/QGIS/pull/64775) |  |
| Avoid crash when edit-in-place layer is removed | 未報告 | [PR \#65107](https://github.com/qgis/QGIS/pull/65107) | Topo |
| 3D Map View crashes QGIS when project uses UTM projection | [\#41171](https://github.com/qgis/QGIS/issues/41171) | No longer reproducible |  |
| Simple lines rendered incorrectly in 3D | [\#51286](https://github.com/qgis/QGIS/issues/51286) | No longer reproducible |  |
| Some feature are not rendered in a 3d map view when using rule based renderer | [\#47581](https://github.com/qgis/QGIS/issues/47581) | 修正済み |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Stefanos Natsis (LutraConsulting)](https://www.lutraconsulting.co.uk/)
### Feature: Bug fixes by Jean Felder (Oslandia)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.40バックポートコミット（GitHub） |
| --- | --- | --- | --- |
| qgs3daxis: Fix axis label visibility in qt6 | 未報告 | [PR \#63585](https://github.com/qgis/QGIS/pull/63585) |  |
| qgs3daxis: Fix cube picking in qt6 when clicking on a label | 未報告 | [PR \#63585](https://github.com/qgis/QGIS/pull/63585) |  |
| \[3D\] fix terrain obj export | 未報告 | [PR \#63173](https://github.com/qgis/QGIS/pull/63173) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Jean Felder (Oslandia)](https://oslandia.com/en/)
### Feature: Bug fixes by Alexander Bruy (QCooperative)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.40バックポートコミット（GitHub） |
| --- | --- | --- | --- |
| PDAL processing are not exposed if QGIS is build without PDAL support | [\#63106](https://github.com/qgis/QGIS/issues/63106) | [PR \#63181](https://github.com/qgis/QGIS/pull/63181) |  |
| Georeferencer: "Trasformation Settings" window is too tall and it disappears when trying to resize it | [\#63157](https://github.com/qgis/QGIS/issues/63157) | [PR \#63192](https://github.com/qgis/QGIS/pull/63192) |  |
| Vector "Layer Properties -\> Legend" window is too tall and it disappears when trying to resize it | [\#63159](https://github.com/qgis/QGIS/issues/63159) | [PR \#63204](https://github.com/qgis/QGIS/pull/63204) | [PR \#63290](https://github.com/qgis/QGIS/pull/63290) |
| Unclear message for incompatible plugins in Plugin Manager | [\#62606](https://github.com/qgis/QGIS/issues/62606) | [PR \#63205](https://github.com/qgis/QGIS/pull/63205) |  |
| ExecuteSQL algorithm does not allow input layers without geometry | [\#63218](https://github.com/qgis/QGIS/issues/63218) | [PR \#63229](https://github.com/qgis/QGIS/pull/63229) | [PR \#63237](https://github.com/qgis/QGIS/pull/63237) |
| Import Geotagged Photos tool not reading HEIC EXIF data | [\#60853](https://github.com/qgis/QGIS/issues/60853) |  |  |
| Casting point geometry of a feature to QgsPointXY crashes Qgis 3.40 | [\#60963](https://github.com/qgis/QGIS/issues/60963) |  |  |
| qgis renders single band paletted image with valid data mask as multiband | [\#61283](https://github.com/qgis/QGIS/issues/61283) | [PR \#63254](https://github.com/qgis/QGIS/pull/63254) | [PR \#63363](https://github.com/qgis/QGIS/pull/63363) |
| "No" notification when activating "GRASS GIS Processing Provider" without GRASS installed | [\#61672](https://github.com/qgis/QGIS/issues/61672) | [PR \#63303](https://github.com/qgis/QGIS/pull/63303) |  |
| Fix handling of tiled scene and vector tile layers in Processing | 未報告 | [PR \#63323](https://github.com/qgis/QGIS/pull/63323) | [PR \#63343](https://github.com/qgis/QGIS/pull/63343) |
| Processing "Output folder" parameter seems unreliable if left to default value | [\#61965](https://github.com/qgis/QGIS/issues/61965) | [PR \#63328](https://github.com/qgis/QGIS/pull/63328) | [PR \#63396](https://github.com/qgis/QGIS/pull/63396) |
| No layer name in "force by selected geometries" contextual menu if overlapping vector features | [\#50049](https://github.com/qgis/QGIS/issues/50049) | [PR \#63342](https://github.com/qgis/QGIS/pull/63342) |  |
| Temporary layers are invisible in canvas QGIS 3.28+ | [\#52149](https://github.com/qgis/QGIS/issues/52149) |  |  |
| QGIS GUI not displaying IAU codes in UI when in PROJ.db | [\#54514](https://github.com/qgis/QGIS/issues/54514) |  |  |
| Better control the scope of the "Run sipify" action | [\#62313](https://github.com/qgis/QGIS/issues/62313) | [PR \#63403](https://github.com/qgis/QGIS/pull/63403) |  |
| "Recent fonts" list is always empty | [\#52169](https://github.com/qgis/QGIS/issues/52169) | [PR \#63423](https://github.com/qgis/QGIS/pull/63423) | [PR \#63485](https://github.com/qgis/QGIS/pull/63485) |
| Copy-pasting a "label settings" item turns it into a "text format" item | [\#40217](https://github.com/qgis/QGIS/issues/40217) | [PR \#63440](https://github.com/qgis/QGIS/pull/63440) | [PR \#63490](https://github.com/qgis/QGIS/pull/63490) |
| Project Settings Panel - Can't Reach Dialog Buttons For Large Font Sizes | [\#58290](https://github.com/qgis/QGIS/issues/58290) |  |  |
| "Data source encoding" dropdown not shown in layer properties for delimited text layer | [\#55443](https://github.com/qgis/QGIS/issues/55443) | [PR \#63478](https://github.com/qgis/QGIS/pull/63478) | [PR \#63552](https://github.com/qgis/QGIS/pull/63552) |
| Addition of an option to select favourite tools in the processing menu | [\#56806](https://github.com/qgis/QGIS/issues/56806) |  |  |
| Undo/redo in Styling panel does not refresh canvas with labelling change | [\#60250](https://github.com/qgis/QGIS/issues/60250) | [PR \#63493](https://github.com/qgis/QGIS/pull/63493) | [PR \#63506](https://github.com/qgis/QGIS/pull/63506) |
| Check geometry (angle) does not check whether feature ID is unique | [\#61398](https://github.com/qgis/QGIS/issues/61398) | [PR \#63304](https://github.com/qgis/QGIS/pull/63304) |  |
| Building master (63a8d7b) fails on "call of overloaded (... QByteArray ...) is ambiguous" | [\#63560](https://github.com/qgis/QGIS/issues/63560) | [PR \#63574](https://github.com/qgis/QGIS/pull/63574) | [PR \#63606](https://github.com/qgis/QGIS/pull/63606) |
| Optional "Gap errors" output not really optional | [\#63614](https://github.com/qgis/QGIS/issues/63614) | [PR \#63616](https://github.com/qgis/QGIS/pull/63616) |  |
| Fix crash and wrong coordinate order in the WCS source widget | 未報告 | [PR \#63615](https://github.com/qgis/QGIS/pull/63615) | [PR \#63632](https://github.com/qgis/QGIS/pull/63632) |
| Fix several issues with geometry check algorithms | 未報告 | [PR \#63304](https://github.com/qgis/QGIS/pull/63304) |  |
| WCS Request fails due to wrong BBox using "Map Canvas Extent" or "Draw on Canvas" | [\#62528](https://github.com/qgis/QGIS/issues/62528) | [PR \#63542](https://github.com/qgis/QGIS/pull/63542) | TODO |
| wcs spatial extent uses wrong projection | [\#50432](https://github.com/qgis/QGIS/issues/50432) |  |  |
| String aggregate-related functions treat NULL and empty strings interchangeably | [\#35433](https://github.com/qgis/QGIS/issues/35433) | [PR \#63324](https://github.com/qgis/QGIS/pull/63324) | TODO |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Alexander Bruy (QCooperative)](https://www.qcooperative.net/)
### Feature: Bug fixes by Nyall Dawson (North Road)
## ニールドーソン
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.40バックポートコミット（GitHub） |
| --- | --- | --- | --- |
| Fix nothing happens when zooming to very small line feature extent | 未報告 | [PR \#65215](https://github.com/qgis/QGIS/pull/65215) | [PR \#65274](https://github.com/qgis/QGIS/pull/65274) |
| Don't immediately validate child algorithms in models | 未報告 | [PR \#65183](https://github.com/qgis/QGIS/pull/65183) | N/A |
| \[browser\] Don't permit renaming tables which are open in the current project | 未報告 | [PR \#65182](https://github.com/qgis/QGIS/pull/65182) | N/A |
| Extend timeout for processing executable tests | 未報告 | [PR \#65161](https://github.com/qgis/QGIS/pull/65161) | [PR \#65224](https://github.com/qgis/QGIS/pull/65224) |
| Downgrade thread safety check to non-fatal | 未報告 | [PR \#65148](https://github.com/qgis/QGIS/pull/65148) | N/A |
| Fix network fetching tasks triggered by rendering of map layers using raster marker symbol layer never complete | [\#65137](https://github.com/qgis/QGIS/issues/65137) | [PR \#65147](https://github.com/qgis/QGIS/pull/65147) | Too risky, potential backport after 3.44.10? |
| \[server\] Fix completely broken service url setting handling | 未報告 | [PR \#65117](https://github.com/qgis/QGIS/pull/65117) | [PR \#65226](https://github.com/qgis/QGIS/pull/65226) |
| Fix broken value range when calling deprecated setComponentValue int variant | 未報告 | [PR \#65115](https://github.com/qgis/QGIS/pull/65115) | [PR \#65135](https://github.com/qgis/QGIS/pull/65135) |
| \[wms\] Fix regression in encode/decodeUri | 未報告 | [PR \#65114](https://github.com/qgis/QGIS/pull/65114) | N/A |
| Fix a bunch of python tests weren't actually run on CI | 未報告 | [PR \#65113](https://github.com/qgis/QGIS/pull/65113) |  |
| Fix assert triggered on qt6 builds | 未報告 | [PR \#65079](https://github.com/qgis/QGIS/pull/65079) | N/A |
| \[gdal\] Fix openfilegdb raster path decoding/encoding | 未報告 | [PR \#65078](https://github.com/qgis/QGIS/pull/65078) | [PR \#65096](https://github.com/qgis/QGIS/pull/65096) |
| Fix mdb files not shown in browser for non-windows platforms | 未報告 | [PR \#65077](https://github.com/qgis/QGIS/pull/65077) | [PR \#65098](https://github.com/qgis/QGIS/pull/65098) |
| Fix failing dock widget test on newer Qt versions | 未報告 | [PR \#65073](https://github.com/qgis/QGIS/pull/65073) | N/A |
| \[browser\] Prevent deletion or rename of fields when table is open in project | 未報告 | [PR \#64958](https://github.com/qgis/QGIS/pull/64958) | Not suitable |
| Fix strict curved label anchoring when placement is on line | 未報告 | [PR \#64736](https://github.com/qgis/QGIS/pull/64736) | [PR \#64801](https://github.com/qgis/QGIS/pull/64801) |
| Move to QGIS4 settings storage, add migration from QGIS3 | [\#61636](https://github.com/qgis/QGIS/issues/61636) | [PR \#64752](https://github.com/qgis/QGIS/pull/64752) | N/A |
| Ensure QString and Qt::StringLiterals namespace are present when needed | 未報告 | [PR \#64724](https://github.com/qgis/QGIS/pull/64724) | N/A |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)

{{<content-end >}}
