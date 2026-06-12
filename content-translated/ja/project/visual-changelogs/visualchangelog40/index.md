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
### 機能: ポリゴンの面取りとフィレットを処理するマップツールの追加
面取りとフィレットを利用するための新しいデジタイジングマップツール。

<img src="images/entries/58ace0c2995032999b366d0171a78857e687d3c4.png" class="img-responsive img-rounded" />

この機能は [City of Frankfurt – Stadtplanungsamt と Oslandia](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html) の資金提供を受けてます

This feature was developed by [Benoit D.-M. - oslandia](https://github.com/benoitdm-oslandia)
## データ管理
### 機能: ラスターエキスポートにおける COG サポートの強化
ラスターのエクスポートと保存ダイアログが、出力をCloud Optimized GeoTiff最適化でエクスポートするための明示的なオプションをサポートするようになりました。追加のCOG固有のピラミッド機能も含まれており、以下の改善が含まれます:
- 進捗報告
- エラーハンドリング
- ピラミッド生成操作

これにはGDAL 3.13.0以上が必要であることに注意してください。

<img src="images/entries/60cec0aa212eb189e7749c242ba1ca49423ca845.png" class="img-responsive img-rounded" />

この機能は [QGIS-DE - Anwendergruppe Deutschland e.V.](https://qgis.de/) の資金提供で開発されました

This feature was developed by [Even Rouault](https://github.com/rouault)
### 機能: 生の属性値のコピー
QGISが属性テーブルと識別結果インターフェースの両方で生（オリジナル）の属性値を表示およびコピー可能にしました。 <br />以前のバージョンでは、データ値はロケール設定、式、または表示値（例：外部キー値）によって評価された"表現形式"でのみコピーされていました。<br />コンテキストメニューから利用できる新しい"生のセルコンテンツをコピー"オプションにより、ソースデータからクリップボードにリテラル値をコピーできるようになります。

<img src="images/entries/cbc449f46c49440ac88d7f89a36e490d4d1deb20.png" class="img-responsive img-rounded" />

この機能は Ct. Solothurn の資金提供で開発されました

This feature was developed by [signedav](https://github.com/signedav)
### 機能: PostgreSQLに保存されたQGISプロジェクトへのコメントの保存を可能に
PostgreSQLに保存されたQGISプロジェクトに追加情報を含むコメントを含めることができるようになりました。これはブラウザーでツールチップを使用して表示されます。

<img src="images/entries/fa9f5d8b4ba7be7475799d104df2c4e96cc26f71.png" class="img-responsive img-rounded" />

この機能開発には Ocean Winds の資金提供を受けました

この機能は [Jan Caha](https://github.com/JanCaha) によって開発されました
### 機能: 名前付きレイヤーを一時出力として使用可能に
この機能により、プロセッシングアルゴリズムの結果として生成される一時出力レイヤーに名前を付けることができるようになります。レイヤーが一時的であることは、ユーザー定義のレイヤー名の前に表示される一時的なアイコン（メモリチップ）で識別できます。

<img src="images/entries/3fec097dc50545f03ab62e3cff5688b719d23916" class="img-responsive img-rounded" />

この機能は QGIS DK user group の資金提供で開発されました

この機能は [Jan Caha](https://github.com/JanCaha) によって開発されました
### 機能:スクラッチレイヤーを保存する際のレイヤーパネルでのレイヤー名変更を可能にした
スクラッチレイヤーを新しい名前（レイヤーパネルの名前とは異なるファイル名）で永続的なレイヤーとして保存する際、メッセージバーが表示されます。<br />このメッセージバーでは、レイヤーパネルの名前を新しいレイヤー名に自動的に変更するかどうかを選択できます。このメッセージバーはレイヤーが新しい名前で保存された場合にのみ表示され、現在は一部のファイルタイプのみで機能します（GeoPackageでは機能しますが、シェープファイルでは機能しません）。

<img src="images/entries/f4d0c0c524eed26129c8c59c406018085e071220" class="img-responsive img-rounded" />

この機能は QGIS DK user group の資金提供で開発されました

この機能は [Jan Caha](https://github.com/JanCaha) によって開発されました
### 機能: レイヤーまたはグループをレイヤー定義ファイルとしてエクスポートする際のファイル名の提案
レイヤーまたはレイヤーグループをレイヤー定義ファイル（.qlr）として保存する際、ファイル名フィールドはデフォルトで空白のままでした。QGISはスタイルのエクスポートの摩擦を減らすために、ファイル名の候補としてレイヤーまたはグループの名前を自動入力するようになりました。

この機能は [pgipper](https://github.com/pgipper) によって開発されました
## フォームとウィジェット
### 機能: ベクターレイヤープロパティダイアログ内での属性フォームのプレビュー機能の追加
QGISがベクターレイヤープロパティダイアログ内で属性 フォームを設定しながらプレビューする機能を提供するようになりました。

<img src="images/entries/c0bb362e1f57600a820c2d185f77993abbd48318.png" class="img-responsive img-rounded" />

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### 機能: 最後の値の再利用の改善と記憶トグルの導入
QGIS属性フォームに、フォームでの "最後にキャプチャされた" 値の再利用を処理するための強化されたユーザーエクスペリエンスが追加されました。フォームのピンアイコンにより、フィールドの値が記憶されて再利用されるかどうかについての視覚的なフィードバックがユーザーに提供され、引き続き再利用するかどうかを制御するアクティブなトグルも提供されます。フォーム設定の追加の機能強化により、セッションレベルの再利用ポリシーの設定、再利用ポリシーのデフォルト動作（有効/無効）、およびレイヤーのすべてのフィールドにわたって再利用ポリシーを無効にする機能が可能になります。

<img src="images/entries/b06e53bc63de8ea4643beb74c69781076b613d07.png" class="img-responsive img-rounded" />

この機能は Funded by DB Fahrwegdienste GmbH の資金提供によって開発されました

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
## レイヤ凡例
### 機能: 自動印刷レイアウト凡例にレイヤーを含めるかどうかの制御の追加
レイヤープロパティの凡例タブ（ベクター、ラスター、メッシュ、ポイントクラウドレイヤー用）に "印刷レイアウト凡例アイテムに自動的に含める" の新しい設定が追加されました。 <br />この設定はデフォルトでチェックされています。ユーザーはチェックを外すことでそのレイヤーを印刷レイアウト凡例から除外できます。これはメッシュおよびポイントクラウドレイヤーの凡例ページにも追加されており、埋め込み凡例ウィジェットを制御する汎用設定も含まれています。

<img src="images/entries/798344535f33fdaf2047bfbd3070def6d28bb6fb.png" class="img-responsive img-rounded" />

この機能は [QGIS Danish User Group](https://qgis.dk/) の資金提供で開発されました

この機能は [North Road](https://north-road.com/) によって開発されました
### 機能:カスタム標高プロファイルソース
QGISが標高プロファイルのより強力なインタラクティブな動作を提供するようになりました。関連するキャンバスでのレイヤーの表示とレンダリング順序の変更、プロジェクトレイヤーツリーとプロファイルプロットソースのリンクなどが含まれます。 <br />この機能は  `QgsLayerTreeCustomNode`  クラスの導入によって有効になり、QGISレイヤーツリーにおけるアプリケーションオブジェクト（レイヤーとグループ以外）の表現が可能になります。

<img src="images/entries/8218225f95e403fe8e543f34b0427561371265b6.png" class="img-responsive img-rounded" />

This feature was funded by [the QGIS user group Switzerland](https://qgis.ch/)

This feature was developed by [Germap](https://github.com/gacarrillor)
## プロセシング
### 機能: ネイティブポリゴン方向アルゴリズム
プロセッシングアルゴリズムに  **ポリゴンを時計回りに強制**  (`native:forcecw`)  と  **ポリゴンを反時計回りに強制** (`native:forceccw`)  の新しいアルゴリズムが追加されました。 <br />ポリゴンを時計回りに強制は既存の "右手の法則を強制" 操作を再現し、ポリゴンジオメトリが外部リングが時計回りの方向に、内部リングが反時計回りの方向に向けられる慣例に従うよう強制します。<br />ポリゴンを反時計回りに強制はその逆を実行し、ポリゴンジオメトリが外部リングが反時計回りの方向に、内部リングが時計回りの方向に向けられる慣例に従うよう強制します。

<img src="images/entries/a0c4136c269a5cd474bdc29e15c26831baa8706f.png" class="img-responsive img-rounded" />

This feature was developed by [Andrea Giudiceandrea](https://github.com/agiudiceandrea)
### 機能: モーダルダイアログの代わりにインラインパネルを使用したモデルコンポーネントの設定
プロセッシングモデルデザイナーの右側にドッキングされた新しい設定パネルが追加されました。これによりモーダルダイアログなしでモデルコンポーネントを編集でき、レイヤースタイリングパネルのユーザーエクスペリエンスを再現します。これによりモデル編集のUXが向上し、モデルコンポーネントの編集中にモデル設定モーダルが他のQGIS要素とのユーザーインタラクションをブロックすることを防ぎます。アイテムをダブルクリックすることでダイアログに引き続きアクセスできます。

<img src="images/entries/c6368e5609a680adf719ca6cd1a95739278db0d2.png" class="img-responsive img-rounded" />

この機能は [City of Canning](https://www.canning.wa.gov.au/) の資金提供で開発されました

この機能は [North Road](https://north-road.com/) によって開発されました
### 機能: ネットワーク分析検証アルゴリズムの追加
ネットワークの検証に役立つ2つの新しいアルゴリズムが追加されました:
- ネットワークの検証
- ネットワーク端点の抽出

**ネットワークの検証**<br />このアルゴリズムはネットワークベクターレイヤーを分析して、ネットワーク分析ツール（最短経路など）に影響を与える可能性のあるデータとトポロジーエラーを特定します。オプションのチェックには以下が含まれます: 
1. 入力レイヤーのすべての方向フィールド値が設定された前方/後方/両方の値と一致することを確認するための '方向 ' フィールドの検証。方向フィールドの値がnullでなく、設定された値のいずれとも一致しない場合にエラーが報告されます。
2. ノード間の間隔のチェック。このチェックはネットワークグラフのノードの中で、指定したトレランス距離より他のノードに近いものを識別します。これは入力レイヤーでのスナップの失敗や短いセグメントを示すことがよくあります。ノードが複数の他のノードとこの条件に違反する場合、最も近い違反のみが報告されます。
3. ノードとセグメントの間隔のチェック: このチェックはラインセグメント（例：グラフエッジ）に接続されていないにもかかわらず、指定したトレランス距離よりも近いノードを識別します。ノードが複数の他のエッジとこの条件に違反する場合、最も近い違反のみが報告されます。

このアルゴリズムは2つのレイヤーを出力します:
1. 方向検証チェックに失敗したオリジナルのネットワークレイヤーの地物を含む出力。
2. エラーを説明する  'error ' フィールドを持つ問題のあるノードの位置を表す出力。これはラインレイヤーで、出力地物は問題のあるノードをトレランスチェックに失敗したノードまたはセグメントに接続します。

**ネットワーク端点の抽出**<br />このアルゴリズムはネットワークラインレイヤーから端点（ノード）を抽出します。端点を識別するための2つの定義が利用可能です:
1. すべて受信エッジのみまたはすべて送信エッジのみを持つノード: フローの方向に基づいて 'ソース' または 'シンク' ノードを識別します。これらはフローが開始（送信のみ）または停止（受信のみ）できるノードです。
2. 単一のエッジに接続されたノード: 方向性に関わらず、トポロジ的な  '行き止まり ' または  'ダングル ' を識別します。これはノードが1つの他の異なるノードのみに接続されているかどうかをチェックします。

<img src="images/entries/a26779141bcb3e43adeea67400b4666419f3a17f.png" class="img-responsive img-rounded" />

この機能は [City of Canning](https://www.canning.wa.gov.au/) の資金提供で開発されました

この機能は [North Road](https://north-road.com/) によって開発されました
### 機能: 特徴を保持するラスタースムージングアルゴリズムの追加
これはWhiteboxツールの同等アルゴリズムの移植版で、Lindsay, John et al (2019): LiDAR DEM Smoothing and the Preservation of Drainage Featuresに記載されているロジックを実装しています。　これは傾斜の変化点、河岸、または段丘崖などの鋭い特徴を大きく変えることなく、DEM（数値標高モデル）の表面の粗さを除去するのに効果的です。<br />これにより、しばしば明確な地形的特徴をぼかす標準的なローパスフィルター（平均、中央値、ガウスなど）や再サンプリングより優れています。<br />このアルゴリズムは3つのステップで機能します:
1. 各グリッドセルの表面法線3Dベクトルの計算。
2. 類似した表面法線を持つ隣接セルにより多くの重みを適用するフィルターを使用して法線ベクトルフィールドをスムージングします（エッジを保持）。
3. スムージングされた法線フィールドに一致するようにDEM内の標高を繰り返し更新します。

This feature was funded by [North Road](https://north-road.com/)

この機能は [North Road](https://north-road.com/) によって開発されました
### 機能: ネイティブラスターガウスぼかしアルゴリズムの追加
ラスターレイヤーにガウスぼかしを適用できます。

This feature was funded by [North Road](https://north-road.com/)

この機能は [North Road](https://north-road.com/) によって開発されました
### 機能:地形解析ライブラリのネイティブ総曲率アルゴリズムの追加
プロセッシングに総曲率アルゴリズムを追加します。総曲率フィルターは地形解析ライブラリに長年存在していましたが、GUIには公開されていませんでした。既存の地形解析フィルターとともにプロセッシングフレームワークに公開されました。

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
### 機能: 地形解析ツールの出力でNODATAとラスター作成オプションを公開
ネイティブラスター地形解析ツール（傾斜、向き、陰影起伏、粗度指数）で出力NODATAとラスター作成オプションを公開します。

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
### 機能: データセット識別GDALプロセッシングアルゴリズムの追加
新しいデータ識別アルゴリズムにより、GDALを使用したメタデータの自動抽出が可能になります。<br />このアルゴリズムは [gdal dataset identify](https://gdal.org/en/stable/programs/gdal_dataset_identify.html) の新しい機能を使用するため、GDAL 3.13.0以上が必要です。

<img src="images/entries/76dfc1189b899bedaa208692766fc765ccb76175.png" class="img-responsive img-rounded" />

この機能は [QGIS-DE - Anwendergruppe Deutschland e.V.](https://qgis.de/) の資金提供で開発されました

This feature was developed by [Even Rouault](https://github.com/rouault)
### 機能: プロセッシングアルゴリズム出力でのラスター形式を指定する方法の追加
この機能はGDAL設定フラグを使用してラスターの出力形式を指定できるようにします。主にCloud Optimized GeoTiff出力を強制するためのものです。 <br />以前のバージョンでは、出力形式はファイル形式の拡張子に基づいていましたが、GDAL GTiffとCOGドライバーの両方が `.tif/.tiff` の拡張子を使用するため、COGでは機能しませんでした。ユーザーは  `-of COG` を明示的に指定してCOGエクスポートを強制できるようになりました。

この機能は [QGIS-DE - Anwendergruppe Deutschland e.V.](https://qgis.de/) の資金提供で開発されました

This feature was developed by [Even Rouault](https://github.com/rouault)
### 機能: モデルデザイナー内でモデルを流れる地物数の表示
長年要望されていた、モデルを流れる地物数を表示する機能が追加されました。地物数はアルゴリズム間のリンクに付加され、ベクターレイヤーのみに適用されます。地物数の表示はビューメニューの "地物数を表示" オプションを使用して無効にできます。<br />注意: 地物数を表示するには、モデルを少なくとも1回実行する必要があります。

<img src="images/entries/468164c721e2407abaf86e0629d35377741dc2a6.png" class="img-responsive img-rounded" />

この機能は QGIS Switzerland user group の資金提供で開発されました

この機能は  [Valentin Buira](https://github.com/ValentinBuira) によって開発されました
### 機能:PDALのラスターへのエクスポート（TIN）アルゴリズムでmax-triangle-edge-lengthをサポート
PDALのラスターへのエクスポート（TIN）アルゴリズムにmax-triangle-edge-lengthパラメーターのサポートが追加されました。これにより、エッジの長さが指定したしきい値より大きいトライアングルを無視できるようになります。<br />この機能にはPDAL 2.6.0以上およびwrench 1.2.2以上が必要です。

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
### 機能: モデルデザイナーのアップデート
QGISモデルデザイナーに、ノード間の入出力値の処理方法に大幅な更新が適用され、より意味のある方法で視覚的なフィードバックを提供するようになりました。<br />ノード設定の個別パラメーターが公開され、ツールと変数からの値間の接続は、それぞれ入出力される特定のパラメーターでノードに接続されます。<br />パラメーター値はデータタイプ（整数や文字列などの汎用データタイプだけでなく、ベクターやラスターレイヤーなどのQGIS固有の複雑なタイプも含む）によってカラーコーディングされており、モデルを流れるデータ操作の視覚的なインデックスとトレーサビリティが向上します。

<img src="images/entries/92bf8916e1ddc8d0e44b31f130d2029ac93b438f.png" class="img-responsive img-rounded" />

この機能は [Géo2France](https://www.geo2france.fr/portal/public/overview) の資金提供で開発されました

この機能は [Jonathan Lurie](https://github.com/jonathanlurie) によって開発されました
### 機能: レイヤーの再投影アルゴリズムによるZ座標の変換を可能にしました
*レイヤーの再投影* アルゴリズムにZ座標の変換を可能にするオプションのboolパラメーターが追加されました。

<img src="images/entries/b93161af43e09fc6189680f8f8b323b86555d499.png" class="img-responsive img-rounded" />

This feature was developed by [Stefanos Natsis](https://github.com/uclaros)
### 機能: ディレクトリソースからCloud Optimized GeoTiffを作成するアルゴリズムの追加
専用フォルダーに提供された入力ラスターファイルのセットに対してCOGを作成し、GDALを使用して入力ファイルの一括変換を実行する、Cloud Optimized GeoTIFF作成の新しいアルゴリズムが追加されました。

<img src="images/entries/7a822b6086fbf156b8f3528499f78a5d83eb7b29.png" class="img-responsive img-rounded" />

この機能開発には Ocean Winds の資金提供を受けました

この機能は [Jan Caha](https://github.com/JanCaha) によって開発されました
### 機能: SFCGAL近似中心軸プロセッシングアルゴリズムの追加
新しく統合されたSFCGALバックエンドに基づく近似中心軸の新しいプロセッシングアルゴリズムが追加されました。<br />近似中心軸アルゴリズムは中心軸を近似することでシェイプの簡略化されたスケルトンを生成します。出力はシェイプの中央構造に沿ったラインのコレクションです。結果はノイズを無視しながら主要なトポロジーをキャプチャする細くて安定した曲線のセットです。このアルゴリズムはZ次元を無視します。ジオメトリが3Dの場合、近似中心軸はその2Dプロジェクションから計算されます。

<img src="images/entries/0804299923000a846f55b0b8fb0b50e19e3893d5.png" class="img-responsive img-rounded" />

この機能は [City of Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html) の資金提供で開発されました

This feature was developed by [Jean Felder](https://github.com/ptitjano)
### 機能: WM抽出のスケールと解像度設定
QGISが指定されたスケールでリクエストされたWMSと連携するラスター抽出アルゴリズムを有効にし、スケール依存のレンダリング（シンボロジー/ラベリング）が出力ラスターに保持されるようになりました。 <br />改善されたアルゴリズムは  ` 範囲でラスターをクリップ`   と ` マスクレイヤーでラスターをクリップ`  です。<br />これらのアルゴリズムのソースとして使用する際にWMSレイヤーに新しい詳細オプションパネルが提供され、以下のオプションが提供されます:
 
- **Reference scale**: WMSラスターをリクエスト/レンダリングするスケール。
- **Service resolution**: サーバーがWMSラスターをレンダリングするために使用する解像度（DPI単位、デフォルトは96 dpi）。 <br />これらの変更は `QgsProcessingRasterLayerDefinition` および `QgsWmsUtils` クラスの導入によって有効になりました。

<img src="images/entries/532bbcaddf65f8d815ecdddd48ed71b067cdb855.png" class="img-responsive img-rounded" />

この機能は [City of Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html) の資金提供で開発されました

この機能は [Germap](https://opengis.ch) によって開発されました
### 機能: 重複ジオメトリの削除アルゴリズムへの重複地物出力レイヤーパラメーターの追
この機能は "重複ジオメトリの削除" プロセッシングアルゴリズムを拡張し、削除された識別された重複地物を抽出して、さらなる分析のための別のファイルとして保存できるようにします。

<img src="images/entries/85ee1e8469a32c107d2bfc08ec468915399689a7.png" class="img-responsive img-rounded" />

This feature was developed by [Andrea Giudiceandrea](https://github.com/agiudiceandrea)
### 機能 長さ/面積でパーツをフィルタリングするアルゴリズムの追加
これらの新しいアルゴリズム "長さでパーツを削除" と "面積でパーツを削除" は、ベクターレイヤーからジオメトリのパーツをその面積または長さを最小サイズパラメーターと比較することでフィルタリングします。 <br />入力ジオメトリがマルチパートジオメトリの場合、パーツは個別のサイズでフィルタリングされます。必要な最小サイズを満たすパーツがない場合、地物はスキップされて出力レイヤーから除外されます。入力ジオメトリがシングルパートジオメトリの場合、ジオメトリのサイズが必要なサイズ未満の場合に地物はスキップされて出力レイヤーから除外されます。属性は変更されません。

<img src="images/entries/a3a539941a16aa0765fd05436e4e7228e3864553.png" class="img-responsive img-rounded" />

This feature was funded by [North Road](https://north-road.com/)

この機能は [North Road](https://north-road.com/) によって開発されました
### 機能: レイヤーのパッケージ化アルゴリズムへのオプションとして出力先CRSの追加
設定されている場合、レイヤーを特定の出力CRSに変換できます。

This feature was funded by [North Road](https://north-road.com/)

この機能は [North Road](https://north-road.com/) によって開発されました
### 機能: レイヤーのパッケージ化アルゴリズム - 指定した範囲と交差する地物のみをエクスポートする
レイヤーのパッケージ化アルゴリズムに `Extent`  のオプションパラメーターが追加されました。これにより、選択したすべてのレイヤーから指定した範囲と交差する地物のみをエクスポートできるようになります。特定の選択されたレイヤーのどの地物も指定した範囲と交差しない場合、レイヤーは引き続き作成され、出力GeoPackageでは空になります。

<img src="images/entries/33644c3a135003c6e8df79e9eda8878004b6ea28" class="img-responsive img-rounded" />

この機能は [City of Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html) の資金提供で開発されました

This feature was developed by [Germap](https://github.com/gacarrillor)
### 機能: モデルデザイナーのモデルキャンバスサイズを無制限にしました
以前のバージョンのQGISモデルデザイナーは固定キャンバスサイズが4000 x 4000で、新しいモデルはキャンバスの左上から開始されていたため、要素が範囲外になると不満が生じることがありました。QGISモデルビルダーはスクロールエリアを動的に管理し、はるかにスムーズなユーザーエクスペリエンスを提供するようになりました。

<img src="images/entries/6347778c8c50b9fa330e4985d19b980c2c8b676f.png" class="img-responsive img-rounded" />

この機能は Hauts-de-France region の資金提供で開発されました

この機能は  [Valentin Buira](https://github.com/ValentinBuira) によって開発されました
## アプリケーションとプロジェクトのオプション
### 機能: OAuth2 自動リフレッシュ
QGISにOAuth2接続の自動更新メカニズムが追加されました。<br />自動更新を停止するためのキャッシュクリーンアップは定期的に、およびプロジェクトからレイヤーが削除されたときにトリガーされます。これは未使用トークンの不必要で無限の更新を避けるために必要です。

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
### 機能: 埋め込みコード強化のためのプロジェクト信頼設定
QGISにプロジェクト内の埋め込みPythonコードの実行を許可または拒否するプロジェクトレベルの "信頼" メカニズムが追加されました。これは  [Trusted Projects and Folders QEP](https://github.com/qgis/QGIS-Enhancement-Proposals/blob/master/qep-336-trusted-projects-and-folders.md) に沿って実装されています。QEPで定義されているように、対象となる埋め込みコードタイプは以下の通りです:
- マクロ;
- 式 関数;
- アクション; と
- 初期化コードで作成された属性値

これにより、ユーザープロファイル設定のみで制限されたグローバル設定の代わりに、プロジェクトレベルで詳細なコード実行を許可する機能がユーザーに提供されます。<br />QGISはユーザーにプロジェクト信頼ダイアログを提供し、許可する機能に関する一般的な情報と対応するコードのプレビューを表示します。プロジェクトとパスレベルでの機能の実行を許可または拒否するグローバル設定が提供されます。

<img src="images/entries/8325ef4b8268626c5af3c9699370dbeb6faedcd4.png" class="img-responsive img-rounded" />

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### 機能: 標高プロファイルマネージャー
QGISがアプリの標高プロファイル処理を新しいプロジェクトレベルの標高プロファイルマネージャーにリンクするようになりました。これにより、プロジェクトに保存された標高プロファイルはプロジェクトを開いた後に再度開くことができ、プロファイルに加えられた変更はプロジェクトに保存されます。<br />また、プロジェクトから標高プロファイルを表示/名前変更/削除できる完全に機能する標高プロファイルマネージャーダイアログもあります。

この機能は [Erftverband](https://www.erftverband.eu/) の資金提供で開発されました

この機能は [North Road](https://north-road.com/) によって開発されました
### 機能: プロジェクト/レイヤー メタデータのローカライゼーションサポート
QGISのプロジェクト翻訳システムに、主要なプロジェクトとレイヤーのメタデータ値の翻訳サポートが追加されました。この機能強化により、プロジェクト翻訳がラベル、マップキャンバスデコレーションなどのレイアウトアイテムに関連するメタデータ値を使用できるようになります。 <br />*これはQFieldにローカライズされた/翻訳されたプロジェクトのサポートを追加するための継続的な取り組みを通じて資金提供されています。*

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### 機能: HTMLのGetFeatureInfoのマップチップのみモードを有効にするプロジェクト設定の追加
HTMLのGetFeatureInfoのマップチップのみモードを有効にするQGIS Serverの新しいプロジェクト設定が提供されます。<br />[これにより、QGISサーバーがWMSベンダーパラメーター ](https://docs.qgis.org/3.40/en/docs/server_manual/services/wms.html#with-maptip) `WITH_MAPTIP=HTML_FI_ONLY_MAPTIP` を使用し、HTMLのGetFeatureInfoレスポンスにマップチップのみを使用できるようになります。

<img src="images/entries/5cefab81d09c5bf0e1b757238d74940a2c9d9c55" class="img-responsive img-rounded" />

This feature was developed by [Björn Hinkeldey](https://github.com/pathmapper)
## Profile Plots
### 機能: 標高プロファイルレイヤーとプロジェクトレイヤーを同期するオプションの追加
この新しいオプションは標高プロファイルの設定メニューから "レイヤーをプロジェクトに同期" として利用できます。デフォルトではチェックされていませんが、チェックすると、標高プロファイルのレイヤーは常にグループとレイヤー順序を含むプロジェクトのメインキャンバスレイヤー構造と正確に一致します。 <br />グループは標高プロファイルで作成できません。メインプロジェクトのレイヤーツリーへの変更はすぐに標高プロファイルのレイヤー設定に反映されます。

 この機能は [Lutra](https://www.lutraconsulting.co.uk/) の資金提供で開発されました

この機能は [North Road](https://north-road.com/) によって開発されました
### 機能: ポイントクラウドを連続した標高ラインとしてレンダリングします
QGISのプロファイルプロットに、ポイントクラウドレイヤーの標高プロファイルを個々のポイントの代わりに連続した標高ラインとして表示する機能が追加されました。これにより、ポイントクラウドをベクターまたはラスターレイヤーと同様にレンダリングできるようになります。ユーザーはレイヤー全体を三角測量することなく、ビュー内にポイントが少なすぎる場合の結果を改善するためにトレランス設定を調整できます。

<img src="images/entries/ab52589956629cc34cb09bef22e63478a65a96bf.png" class="img-responsive img-rounded" />

この機能開発は [Danish Agency for Climate Data](https://www.klimadatastyrelsen.dk/) からの資金提供を受けました

この機能は [Dominik Cindric (Lutra Consulting)](https://github.com/ViperMiniQ) によって開発されました
### 機能: プロファイル設定メニューでの距離:標高スケール比の表示
標高プロファイルプロットの現在の距離:標高スケール比を表示するための新しいウィジェットが追加されました。このウィジェットは特定の比率を設定するためにも使用できます。プロットの "ロック" オプションが有効になっている場合、プロットのズームとナビゲーション時にデフォルトの1:1比率の代わりにこのスケール比率が使用されます。

<img src="images/entries/a4300b20ef89e4ad71f70a114af7438e4eff9cfb" class="img-responsive img-rounded" />

この機能は [Erftverband](https://www.erftverband.eu/) の資金提供で開発されました

この機能は [North Road](https://north-road.com/) によって開発されました
## ブラウザ
### 機能: データベース内の複数のテーブルを別のスキーマに移動できます
複数のテーブルを一度に指定したスキーマに移動できるようになりました。

この機能開発には Ocean Winds の資金提供を受けました

この機能は [Jan Caha](https://github.com/JanCaha) によって開発されました
### 機能: ブラウザーDBテーブルのコメント
QGISブラウザーに、この機能をサポートするデータベースの **テーブルコメント** を直接編集するオプションが追加されました。

<img src="images/entries/84b05ee5021e434fc16c6bc60bb1695584de7ecb.png" class="img-responsive img-rounded" />

この機能開発には Ocean Winds の資金提供を受けました

この機能は [Jan Caha](https://github.com/JanCaha) によって開発されました
### 機能: ブラウザーの管理メニューへの空間インデックスの作成または削除の追加
 サポートしているプロバイダーで空間インデックスを **作成** または **削除** するための新しいコンテキストメニューオプションが追加されました。

<img src="images/entries/797d36c2dd01a3e0120c3835d360861033d5b516.png" class="img-responsive img-rounded" />

この機能開発には Ocean Winds の資金提供を受けました

この機能は [Jan Caha](https://github.com/JanCaha) によって開発されました
## データプロバイダ
### 機能: OAPIFの地物フォーマットとしてのGMLサポートの追加
OGC API for Featuresのソース設定にGML出力のサポートが追加されました。サーバーが地物フォーマットとして公開している場合、 "Modify WFS Connection" ダイアログのコンボボックスで選択できます。<br />いくつかのシナリオがサポートされています:
 
- ソースはXMLスキーマの有無にかかわらずアクセスできます（rel=describedbyリンクを通じて）。WFSと同様に、XMLスキーマは選択した "Feature mode" に応じて、QGISの単純スキーマパーサーまたはGDAL GMASパーサーで確認できます。
- 地物はバルクダウンロードリンクの有無にかかわらず取得できます（rel=enclosureリンクを通じて提供）。

This feature was developed by [Even Rouault](https://github.com/rouault)
### 機能 OAPIFユーザーがGeoJSON以外の代替フォーマットで地物をダウンロードできるようにしました
接続URIの  `outputFormat` パラメーターを尊重するOGC API for Featuresソースから提供されるフィーチャーサービスは、地物を取得するための追加の出力フォーマット（FlatGeoBuf、GeoJSONなど）をサポートする必要があります。これにより、ユーザーはパフォーマンス、互換性、または拡張性の向上のために、サポートするソースからGeoJSON以外の地物取得オプションを選択できるようになります。.<br />サービス接続ダイアログでは、新しいコンボボックスを使用して希望の出力フォーマットを選択できます。さらに、"lastFeatureFormatEncoding" を設定するための新しいグローバル設定により、以前定義した値を新しい接続のデフォルトとして使用できます。

<img src="images/entries/3f0add13c921416314030ca3f9ff12118dd288b2.png" class="img-responsive img-rounded" />

この機能は [QGIS-DE - Anwendergruppe Deutschland e.V.](https://qgis.de/) の資金提供で開発されました

This feature was developed by [Even Rouault](https://github.com/rouault)
### 機能: GPKGのフィールドドメインの更新と削除を可能にしました
新しいメニューアイテムにより、GPKGデータソースのフィールドドメインを更新および削除できるようになります。GDAL 3.12以上が必要です。

<img src="images/entries/3e5c8b252b192ecd9022ac7a0a638307c46bc52f.png" class="img-responsive img-rounded" />

この機能開発には Ocean Winds の資金提供を受けました

この機能は [Jan Caha](https://github.com/JanCaha) によって開発されました
### 機能: ブラウザーからのQGISプロジェクトのPostgreSQLへの保存とインポート
QGISが現在のQGISプロジェクトをPostgreSQLデータベースに保存する機能と、フォルダーからPostgreSQLデータベースにQGISプロジェクトをインポートする機能をネイティブでサポートするようになりました。 <br />PostgreSQL接続の2つの新しいメニューエントリが追加されます:
- 現在開いているQGISプロジェクトをスキーマに直接保存するためのもの。
-  2番目のアイテムはプロジェクトをスキーマにバッチインポートできます。プロジェクト名は名前の衝突がチェックされ、プロジェクト名がスキーマにすでに存在する場合は自動インクリメントのサフィックス値（例： `_1`, `_2` など）が追加されます。

<img src="images/entries/b139e1711b8d62c9064db1df0e8bce5b242cea96.png" class="img-responsive img-rounded" />

この機能開発には Ocean Winds の資金提供を受けました

この機能は [Jan Caha](https://github.com/JanCaha) によって開発されました
### 機能: PostgreSQLプロバイダーへのレイヤープロパティ情報の追加
QGISがPostgreSQLレイヤーの **レイヤープロパティ** に以下を含む追加情報を表示するようになりました:
- テーブルに関するユーザーの権限
- 行数の推定
- 空間インデックスに関する情報

<img src="images/entries/37e33067b2665adbfd5202b1825df30a71b1ce37.png" class="img-responsive img-rounded" />

この機能開発には Ocean Winds の資金提供を受けました

この機能は [Jan Caha](https://github.com/JanCaha) によって開発されました
### 機能: Planetary Computerの認証方法の追加
Microsoft Planetary Computer STACカタログで使用するための新しい認証方法が提供されます。Planetary ComputerはほとんどのアセットのデータにアクセスするためにSAS署名トークンの使用を必要とします。これは古いSTACプラグインで実装されていましたが、コアSTAC実装では欠けていました。 <br />新しい認証方法には2つのモードがあります:
- 1つはPlanetary Computerのオープンバージョン用で、アセットのSAS署名を実行します。
- 2番目はPlanetary Computer Pro GeoCatalog用で、アセットのSAS署名に加えてOAuth2認証も必要です。<br />新しい認証方法はSTAC接続で使用するか、データソースがPlanetary Computer上にある個別のGDALまたはポイントクラウドレイヤーに直接適用できます。STACカタログからまたはデータソースマネージャーを使用して直接レイヤーを追加する際、QGISがネットワークリクエストにその設定を使用するよう `authcfg`  がURIに追加されます。Authcfgのエンコード/デコードもポイントクラウドレイヤーに追加されました。

<img src="images/entries/0ed79ce1c54933c720853f364cdd505ea4292261.png" class="img-responsive img-rounded" />

 この機能はMicrosoftの資金提供で開発されました

この機能は [Stefanos Natsis (Lutra Consulting)](https://github.com/uclaros) によって開発されました
### 機能: PostgreSQLにおけるQGISプロジェクトのバージョン管理
PostgreSQLに直接保存するQGISプロジェクトでは、自動バージョン管理を有効にすることができ、プロジェクトの過去のコピーを保存、読み込み、編集、復元できるようになります。このプロセスは主にPostgreSQLデータベースの関数とトリガー操作によって処理され、ユーザーがバージョン管理プロセスを詳細に制御できる複数の新しいメニューアイテムとダイアログが提供されています。

<img src="images/entries/e6362175a8d1662e590efecd2b1e48f62ec79c51.png" class="img-responsive img-rounded" />

この機能開発には Ocean Winds の資金提供を受けました

この機能は [Jan Caha](https://github.com/JanCaha) によって開発されました
### 機能: 利用可能な接続と既定の画像フォーマットの保存
WMS接続の優先フォーマットを設定に保存します。

サーバーが実際にアドバタイズするフォーマットを検出し、将来の使用のために設定に保存できるようになります。

<img src="images/entries/9736fdc6bcb34c3bbdf6d85cf3d9eaa567176313.png" class="img-responsive img-rounded" />

この機能は [QGIS-DE - Anwendergruppe Deutschland e.V.](https://qgis.de/) の資金提供で開発されました

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
## QGISサーバー
### 機能: 無効なプロジェクトレイヤーの再読み込みを試行
QGISサーバーには不正なレイヤーを無視するオプションがありますが、不正と識別されたレイヤーは後で利用可能になる場合があります（ネットワークサービスの復旧など：Webサーバー/データベースなど）。 <br />QGISサーバーに   `QGIS_SERVER_RETRY_BAD_LAYERS`  の新しいオプションが追加されました。このオプションがtrueに設定されている場合、サーバーは各リクエスト時に不正なレイヤーが再び利用可能かどうかを確認します。レイヤーが利用可能な場合、それは有効としてマークされ、サーバーによって使用されます。

この機能は Stadtwerke München (SWM) の資金提供で開発されました

This feature was developed by [mhugent](https://github.com/mhugent)
### 機能: メッシュレイヤーにおけるGetFeatureInfo の実装
QGIS Server では現在メッシュレイヤにおけるGetFeatureInfo リクエストに対する返答を提供しています。

<img src="images/entries/fd8d94bd934381d9c5670b78bba29159ddcfcf93.png" class="img-responsive img-rounded" />

この機能は [Jorge Gustavo Rocha](https://github.com/jgrocha) によって開発されました
### 機能: OAPIF URL ルートパス構成オプション
新しいサーバー設定を通じてOAPIFサービスのルートパスを設定可能にしました<br />QGIS_SERVER_API_WFS3_ROOT_PATH

デフォルトを “/wfs3”  から “/ogcapi” に変更しました。

この機能は [QGIS-DE - Anwendergruppe Deutschland e.V.](https://qgis.de/) の資金提供で開発されました

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
## プログラマビリティ
### 機能: area3D  のサポートを QgsGeometry に追加しました
QgsGeometry クラスがジオメトリの3次元表面積である `area3D` を含むよう拡張されました。
- ポイントまたはラインストリングの場合、常に0になります。
- ポリゴンの場合、外部リングの3D面積から内部リングの3D面積を引いた値になります。
- 多面体とTINの場合、すべてのパッチの3D面積の合計になります。
- ジオメトリコレクションの場合、すべてのジオメトリの3D面積の合計になります。

This feature was developed by [Jean Felder](https://github.com/ptitjano)
### 機能:QgsGeometryutilsのpointsAreCollinearメソッドへの3Dポイントのサポートの追加
以前のバージョンの  `QgsGeometryUtilsBase::pointsAreCollinear` メソッドは2Dポイントのみに対応していましたが、2Dおよび3Dポイントをサポートするよう拡張され、対応する  `QgsGeometryUtilsBase` 関数を呼び出すようになりました。3Dポイントに対応する新しい `QgsGeometryUtilsBase::points3DAreCollinear` も導入されました。

この機能は [City of Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html) の資金提供で開発されました

This feature was developed by [Jean Felder](https://github.com/ptitjano)
### 機能: QgsVectorLayer.as_geopandas() の実装
PyQGIS APIが QgsVectorLayer オブジェクトを属性を含むGeoPandasデータフレームにネイティブ変換するメソッドを提供するようになりました。これはQGIS環境にGeoPandasライブラリが依存関係として必要であることに注意してください。

<img src="images/entries/cf6f4588f8da7d899a519e10117847b68fcbe292.png" class="img-responsive img-rounded" />

この機能は [Till Frankenbach](https://github.com/merydian) によって開発されました
### 機能: PyQGIS APIへの3Dマップツールの公開
ユーザーは `Qgs3DMapTool` 基底クラスを使用して3Dマップキャンバスと対話するカスタムマップツールを作成できるようになりました。

本機能は [SIGNON Deutschland GmbH](https://signon-group.com/en) の資金提供で開発されました

This feature was developed by [Stefanos Natsis](https://github.com/uclaros)
### 機能: PyQGIS APIへの3Dマップキャンバスの断面モードの公開
3Dの "断面ツール" 機能がPyQGIS APIに公開されるようになりました。Pythonと3Dビューのマップ座標を使用して、3Dマップビューに4つのクリッピング平面を簡単に作成して適用できるようになりました。 

本機能は [SIGNON Deutschland GmbH](https://signon-group.com/en) の資金提供で開発されました

This feature was developed by [Stefanos Natsis](https://github.com/uclaros)
### 機能: レイキャスティングのリファクタリングとPyQGIS APIへの公開
重複していた  `Ray3D` クラスが削除され、欠落していたメソッドが追加された `QgsRay3D` が採用されました。`Qgs3DMapCanvas::castRay()`  のPyQGIS APIへの公開により、Pythonプラグインが3Dマップキャンバスでレイキャスティングを実行し、結果のヒットを管理できるようになります。

本機能は [SIGNON Deutschland GmbH](https://signon-group.com/en) の資金提供で開発されました

This feature was developed by [Stefanos Natsis](https://github.com/uclaros)
### 機能: 空白領域実装を有効にするTemplatedLineSymbolLayerの拡張
QGIS APIが [QEP \#345](https://github.com/qgis/QGIS-Enhancement-Proposals/pull/345) に沿った空白領域操作の実装をサポートするよう拡張されました。

この機能は [City of Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html) の資金提供で開発されました

This feature was developed by [Julien Cabieces](https://github.com/troopa81)
### 機能: HubディスタンスアルゴリズムのC++への移植
プロセッシングのハブディスタンスアルゴリズムがPythonからC++に移植されました。<br />このアルゴリズムは最近傍ハブへの距離（ポイント）と最近傍ハブへの距離（ラインからハブへ）アルゴリズムの2つのオプション出力を生成することから、これらのアルゴリズムを置き換えます。元のアルゴリズムは非推奨としてマークされています。

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
### 機能: SFCGALライブラリのサポートの追加
 [QEP \#340](https://github.com/qgis/QGIS-Enhancement-Proposals/pull/340)に沿って、高度な幾何計算ライブラリであるSFCGALのネイティブサポートがQGISに追加されました。 <br />この機能はQGIS APIに2つの主要な追加クラスを追加します:
- QgsSfcgalEngine: SFCGAL C APIをQGISに公開します。メモリとエラー管理も追加します。
- QgsSfcgalGeometry: QGISとSFCGAL間のジオメトリ変換を減らすためにSFCGALジオメトリ表現へのハンドルを保持します。<br />以下の支援のもとで開発されました:
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
## Nyall Dawson
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
