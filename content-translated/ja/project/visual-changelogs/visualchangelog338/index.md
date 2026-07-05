---
HasBanner: false
draft: false
releaseDate: '2024-06-21'
section: project
sidebar: true
title: QGIS 3.38 の変更履歴
type: visual-changelog

---
{{<content-start >}}
# QGIS 3.38 の変更履歴{#changelog338 }
![](images/projects/77e273e90ec2f1953a8c0b5b0097a235c85f2425.png)

リリース日: 2024-06-21

QGISプロジェクトは、空間的発見の旅におけるユーザーの能力向上を目的とした進歩に満ちた画期的なアップデート、QGIS 3.38 Grenobleのリリースを誇りを持って発表します。このリリースにはデータフィルタリング機能の強化と、プロジェクトの異なる要素間でのフィルター基準の緊密な統合が含まれており、ユーザーのデータ探索プロセスの洗練を支援するための拡張されたコントロールを提供します。

新しい標高コントローラーやプロジェクトの垂直CRSを明示的に宣言する機能など、標高管理のさまざまな改善が提供されています。  [QGIS Enhancement Proposal 267](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/267) に概説されているように、以前のリリースでは技術的な理由により垂直CRS情報が積極的に削除されていましたが、空間データ管理のこの重要な側面がQGISプロジェクトに再導入されています。

これらのコアとなる改善に加えて、QGIS 3.38はさまざまなユーザビリティ向上、CMYKカラーサポート、改善された検索機能、DXF、メッシュ、SensorThingsなどのデータタイプの新機能を含む豊富な機能強化と使い心地の改善を誇っています。

 導入されたすべての新機能を手早く確認するには、  [YouTubeのハイライト動画](https://www.youtube.com/watch?v=oktjj7xBZ54) をご覧ください。

[![](https://img.youtube.com/vi/oktjj7xBZ54/0.jpg)](https://www.youtube.com/watch?v=oktjj7xBZ54)

QGISはコミュニティによる取り組みです。このリリースを実現するために時間と労力をボランティアで提供してくださった（または資金援助をしてくださった）開発者・ドキュメント作成者・テスター・その他多くの方々に心より感謝申し上げます。QGISコミュニティより、このリリースをお楽しみいただければ幸いです！QGISをさらに素晴らしいものにするために、時間・資金・その他の形でご貢献いただける方は、ぜひ [QGIS.ORG](https://qgis.org) をご覧いただき、お力をお貸しください！

QGISは寄付者およびサステイニングメンバーによって支えられています。プロジェクトに大小を問わず財政的な貢献をしてくださった寄付者の最新リストは [寄付者一覧](https://qgis.org/en/site/about/sustaining_members.html#list-of-donors) でご覧いただけます。公式のプロジェクトサステイニングメンバーになることをご希望の方は、詳細について [サステイニングメンバーページ](https://qgis.org/en/site/about/sustaining_members.html)  をご覧ください。QGISへのスポンサーシップは、定期的な開発者ミーティングの開催、プロジェクトインフラの維持、およびバグ修正活動の資金として活用されます。現在のスポンサーの完全なリストを以下に掲載します。すべてのスポンサーの皆様に心より感謝申し上げます！

QGIS はフリーのソフトウェアです。利用する上で金銭を支払う義務はありません。実際、私たちは利用者の財政状況や社会的地位にかかわらず、より多くの人に QGIS を利用して欲しいと思っています。私たちは地理空間的な意思決定ツールによって人々が力を持つことが、全人類の社会をより良くすると信じています。
## 時系列
### 機能: 新しい時間モード:ピクセル値を時間的な日時として
各ピクセルを日時値として解釈するラスターレイヤーの新しい時間モードが提供されました。

その時間モードを使用してラスターレイヤーをレンダリングする際、ピクセルはレンダリングコンテキストに関連付けられた時間範囲の外にある場合に非表示になります。

興味深い時間的ユースケースの例には以下が含まれます:
- 森林減少などの土地利用変化の表示
- 時間経過による洪水の表示
- 移動コストの表示 (例 GRASS' `r.walk`)

![](images/entries/e9349bf2255cb4e027d1f91460eb4fea9710c4c1.webp)

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
## ツール
### 機能: 2Dマップで垂直データをフィルタリングするための標高コントローラーの追加
新しい標高コントローラーにより、ユーザーが2Dマップで垂直データをフィルタリングできるようになります。 [QEP 201](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/201) に沿って、データの標高Z範囲スライシングのためのテンポラルコントローラーと同等の操作性を提供します。

この機能はビューメニューの新しい "データフィルタリング" サブメニューからアクセスでき、テンポラルコントローラーの新しいメニューアイテムも追加されました。

コントローラーはマップの左側に範囲スライダーとして表示されます。プロジェクトの標高範囲を設定する設定アクションがあり、これによりウィジェットから利用可能な範囲が決定されます。

![](images/entries/09e8196d117fbd9dc521e59ed5e206ced16e14ab.gif)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能: マップキャンバス/マップ設定アイテムへのZ範囲サポートの追加
マップキャンバスで標高フィルタリングがサポートされるようになりました。

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### 機能: 標高コントローラーの固定標高スライス幅を設定するオプションの追加
標高コントローラーの設定メニューに、固定した標高スライス幅を設定できる新しいオプションが提供されました。

特定の標高範囲幅が必要な場合、または範囲が常にゼロ幅であるべき場合に使用できます。

![](images/entries/89ac87d5ec596dbd04f45be17dac9532d4a120b4.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## ユーザーインタフェース
### 機能: 正規表現ベースの検索のための検索オプションの追加
コードエディターの更新された検索機能で実装されているように、高度な検索オプションのための新しいオプションの正規表現モードが公開されました。

![](images/entries/2ab6a0a0e6837a51cf7e50a7104359fc063ced7e.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能: データ定義オーバーライド:中クリックで式ビルダーダイアログウィンドウを開く
## 説明
データ定義オーバーライドアイコンの中クリックで式ビルダーダイアログウィンドウが開きます。右クリックしてから編集メニューアイテムを左クリックするための便利なショートカットです。

![](images/entries/f44815b85558f76d7a6e6791370f683def53d51d.gif)

This feature was developed by [Andrea Giudiceandrea](https://github.com/agiudiceandrea)
## シンボロジ
### 機能: ラスターの新しい単一カラーレンダラー
ラスターレイヤーに新しい単一カラーシンボロジーが追加されました。これにより単一の色を使用してラスターをレンダリングするための非常にシンプルでわかりやすい方法が提供されます。

![](images/entries/73049b50b1c9d2e2c0c22fbfdd00db58d4ffc5c0.webp)

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### 機能: メッシュベクターデータセットのウィンドバーブレンダリングのサポートの追加
ウィンドバーブは地図上で風の強さと方向を表示するための一般的な方法であり、新しいウィンドバーブシンボロジータイプにより、ユーザーがメッシュベクターデータセットにこの強力な可視化スタイルを簡単に使用できるようになります。

ウィンドバーブは風速をノット（海里/時）でエンコードするため、ユーザーは正しく表示するためにデータの関連データ単位を明示的に選択するか、カスタム乗数を使用して値をノットに変換する必要があります。

![](images/entries/1f5b158227f114192f411835adfb8dd40d0a8900.webp)

This feature was developed by [Stefanos Natsis](https://github.com/uclaros)
## ラベリング
### 機能: ポイントラベルの最大距離設定の追加
"ポイントの周囲" および "カルトグラフィック" 配置モードに地物からのラベルの最大距離を指定するための新しいオプション設定が追加されました。既存の距離設定と組み合わせて使用し、ラベルを対応するポイント地物から配置できる距離の範囲を定義します。

これによりこれらのレイヤーの配置に柔軟性が加わり、最終的に混み合った地図により多くのラベルを配置できるようになります。

レイヤーが "ポイントの周囲" モードに設定されている場合、ポイントに近いラベル候補は常に遠いものより優先されます。

レイヤーが "カルトグラフィック" モードに設定されている場合、デフォルトの動作も近いラベルを優先します。新しいコンボボックスにより、ユーザーは優先度を制御でき、位置順序の優先オプションが提供されます。このオプションが設定されると、ポイントからの距離に関わらず対応する位置（例：左上）の候補が優先され、最大ラベル距離まで配置できない場合にのみ代替位置にフォールバックします。

![](images/entries/cf8223309d9bf77cf5634a7166706e3b9841bda9.webp)

この機能は Rubicon Concierge Real Estate Services の資金提供で開発されました

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能: カルトグラフィックラベルモードへの 'ポイントの上 ' 配置オプションの追加
A new option for label placement has been added for "O" = "over point" when the label placement mode is set to the "cartographic" mode.
ラベル配置モードが "カルトグラフィック" モードに設定されている場合、"O" = "ポイントの上" のラベル配置の新しいオプションが追加されました。

地物のデータ定義配置優先度にこの新しい 'O' オプションが含まれる場合、ラベルを対応するポイントの真上に配置できます。

![](images/entries/25c00222d0e6f17efda6784e8ce9a577275618a8.webp)

この機能は Rubicon Concierge Real Estate Services の資金提供で開発されました

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## レンダリング
### 機能: ヒートマップの半径と最大値のデータ定義制御の追加
これにより、ユーザーは現在のマップスケール、現在の印刷アトラス地物、現在の時間範囲など、現在の状況に適した値として半径と最大値を定義できるようになります。

これには地物レンダラーレベルでのデータ定義プロパティに必要な基本的な変更も含まれており、他のベクターレンダラークラス（例：ポイントクラスター/変位）の拡張に役立つ可能性があります。

この機能は Rubicon Concierge Real Estate Services の資金提供で開発されました

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## 印刷レイアウト
### 機能: QgsTextFormatおよびQgsTextRendererでのタブ文字サポート
 [リグレッション](https://github.com/qgis/QGIS/issues/56981)  により、QGISがタブ文字を削除し、凡例での文字配置など特定のコンテキストでタブ文字を使用する機能が制限されていました。

![](images/entries/b8934ab8ad907adbc628a9e168fcbd9c88af83ee.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能: コンポーザーグリッドのコピー
印刷コンポーザーに選択したグリッドをコピー（複製）するボタンが追加されました。

これにより、既存のグリッドとわずかな違いしかない新しいグリッドを作成したり、既存のグリッドをテンプレートとして使用したりするプロセスが簡素化されます。

![](images/entries/bad634a873669247fe13d334d080b0b1cb6e1363.webp)

この機能は [NaturalGIS](https://naturalgis.pt/) の資金提供で開発されました

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
### 機能: レイアウトマップのZ範囲フィルターオプションの追加
レイアウトマップアイテムの新しい設定により、既存の時間フィルター設定と同様に、2Dレイアウトマップのフィルタリングのための特定の標高/Z範囲を設定できるようになりました。

設定すると、2D Z範囲フィルタリングをサポートするマップレイヤーがこの範囲内のコンテンツのみを表示するようフィルタリングされます。

さらに、Zフィルタリングの範囲はデータ定義が可能で、データ駆動の地物プロパティに基づいてアトラスまたはレポートの地物に異なるZ範囲を設定できます。

![](images/entries/c7f2cc35cfaf4a101ee2be654688142fb83ac055.gif)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能: レイアウト凡例ツリーの展開または折りたたみボタンの追加
印刷レイアウト内の凡例ツリーを簡単に展開または折りたたむための新しいボタンが追加されました。

![](images/entries/e3ada0021b7137123133b645093168bd483530a7.webp)

This feature was developed by [Harrissou Sant-anna](https://github.com/DelazJ)
## 計算式
### 機能: 地図のZ範囲値を反映する @map\_z\_range 変数の追加
マップキャンバスのZ範囲値を反映する `@map_z_range_lower` および `@map_z_range_upper` r の現在値を取得するための新しい変数がQGIS式に追加されました。

![](images/entries/ab7a53d114337665cded7fd178658144222d1962.gif)

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
## データ管理
### 機能: 地物複製時のフィールドの複製ポリシー
地物（およびその子）を複製する際、QgsField オブジェクトで新しい複製ポリシーが利用可能になります。

この動作はレイヤーの地物フォーム定義のポリシーインターフェースを使用して設定できますが、地物がコピーされるたびに汎用マップツールを使用して複製された任意の地物にアクティブに定義されたポリシーが実装されます（例："移動してコピー" デジタイズ、またはキャンバスや属性テーブルからのコピー＆ペースト）。
 
 
 
 
 
 

現在、3つのポリシーオプションが利用可能です:
- **値の複製** （デフォルトモード）: ソース地物の属性値のコピーを作成します。
- **デフォルト値** : デフォルトモードと混同しないでください。デフォルト値設定は新しい地物をフォームデザイナーで定義された地物フォームのデフォルト（通常はQGIS式）にリセットします。
- **値の削除** : フィールド値を設定解除して削除します（NULL）。

![](images/entries/76e7f27309a07b9bb7e61a074efa81c1340bfbed.webp)

This feature was developed by [signedav](https://github.com/signedav)
### 機能: ラスター時間制御への "バンドごとの固定時間範囲" モードの追加
このモードはラスターレイヤーの各バンドが固定時間範囲に関連付けられている場合（例：NetCDFファイル）に使用できます。

ユーザーはラスターの各バンドの開始日/終了日を手動でテーブルに入力するか、日時値を返すQGIS式を使用してテーブルを構築できます。

![](images/entries/7075b0b60ec0f0d4e5901e4d94452fa187b9a787.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能: ラスターレイヤーへの固定標高範囲の導入
ラスターレイヤーと標高の関連付け方法を指定するための新しいオプションが導入されました。レイヤーに固定標高範囲を設定することができ、レイヤーが単一の固定標高または標高値の範囲（スライス）を持つ場合に使用できます。

ユーザーはレイヤーの下限と上限の標高範囲、および下限または上限が包括的か排他的かを設定できます。

有効にすると、標高フィルタリングが有効な2Dマップでは、レイヤーの範囲がマップのZ範囲に含まれている場合にのみレイヤーが表示されます。

![](images/entries/64a2386154517472b58a41f2551b0d8d30951770.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能: メッシュレイヤーの固定標高範囲を導入
メッシュレイヤーに新しい固定標高範囲モードが追加されました。これはラスターレイヤーの固定標高範囲モードと同等のもので、メッシュレイヤーに関連する標高の指定方法として新しいオプションを提供します。このモードでは、レイヤーに固定の標高範囲を設定することができます。レイヤーが単一の固定標高または標高値の範囲 (スライス) を持つ場合に使用できます。

ユーザーはレイヤーの下限と上限の標高範囲、および下限または上限が包括的か排他的かを設定できます。

有効にすると、標高フィルタリングが有効な2Dマップでは、レイヤーの範囲がマップのZ範囲に含まれている場合にのみレイヤーが表示されます。

![](images/entries/88a53a76a505418c2ed776f70fb56cd5bd85031b.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能:ラスター用 "バンドごとの固定範囲" を標高モードを追加
この新しいモードでは、ラスターの各バンドに固定の標高範囲を関連付けることができます。

これは、バンドで標高関連データを公開するデータソース向けに設計されています（例：異なる海洋深度の温度データを持つNetCDFラスター）。

レンダリング時には、最上位に一致するバンドが選択されてレイヤーのデータに使用されます。レンダラー設定は一致するバンドに関わらず変更されずに維持されるため、ユーザーはすべてのバンドのデータをカバーする代表的な範囲を使用してレイヤーのレンダリングオプションを設定する必要があります。

レイヤー設定は下限値と上限値を持つラスターバンドのユーザー編集可能なテーブルとして公開されます。ユーザーは下限値と上限値を手動で入力するか、QGIS式を使用してすべてのバンド値を自動的に入力できます。

式に基づく値の定義により、ユーザーはバンド名自体（例："Band 001: depth=-5500 (meters)"）など、他の方法では操作が困難なファイルメタデータから有用な情報を抽出できる式を設計できるようになります。

![](images/entries/9622032fd646ac79cc63e48ed30eca1841c9993b.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能：ラスターへの"バンドごとの動的標高範囲"モードの追加
ラスターバンドの標高範囲をレイヤーの標高範囲の下限と上限のためのQGIS式のペアを使用して計算するラスター標高設定の新しい動的モードが提供されます。

このモードでは、ユーザーは @band、@band\_name、@band\_description のような変数を標準のQGIS式の値、グローバル変数、プロジェクト変数と組み合わせて使用して、ラスターバンドに対応する下限値と上限値のQGIS式を指定できます。

For example:

    @band * 100
    
これは各バンドがデータの100m垂直スライスを表す場合に使用できます。

式は各バンドに対応する実際の標高範囲を決定するために必要に応じて評価されます。

これはユーザーが各バンドの標高を個別に手動で入力する必要がある "バンドごとの固定標高範囲" モードとは異なり、これらの値は定数として扱われます。そのモードはバンド標高値に不規則なステップを持つラスターに最も適しており、動的モードは各バンドにわたって規則的な標高ステップを含むデータに適しています。

![](images/entries/d40450a1bcc9d3d2d3c5565681228b1d52256b69.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能：メッシュレイヤーへのデータセットグループごとの固定標高範囲モードの追加
メッシュレイヤーのデータセットグループごとに固定標高範囲を設定する追加機能は、ラスターレイヤーの新しい "バンドごとの固定範囲" モードを模倣しますが、メッシュレイヤーのデータセットグループごとの標高範囲を設定できます。

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能：dxfエクスポートでの最小幅ですべてのラインをエクスポートするオプションの追加
dxfエクスポートに最小幅0（ヘアライン）ですべてのラインを書き込むことができるオプション設定が追加されました。

幅がゼロのDXFファイル内のラインは、ズームレベルに関わらずCADでは通常最小限に維持されるため、この機能は特にデータ密度が高い場合に他のソフトウェアで編集されたエクスポートされたDXFとの互換性にかなり役立ちます。

![](images/entries/1c7a18b41d42049e6c6ab7538d74d69406b837bb.webp)

この機能は [Stadtwerke München](http://www.swm.de/) の資金提供で開発されました

This feature was developed by [mhugent](https://github.com/mhugent)
### 機能：DXFにエクスポートされるレイヤー名のオーバーライドをユーザーに許可
プロジェクトエクスポート、レイヤーエクスポート、およびレイヤーをDXFにエクスポートするプロセッシングアルゴリズムのDXFエクスポートダイアログに新しい設定オプションが追加され、エクスポートされた個々のレイヤーの出力名を上書きできるようになりました。

![](images/entries/83f65d9f8afbd45ecc0fa6b2804a7981f6192e7e.webp)

この機能は [the QGIS user group Switzerland](https://qgis.ch/) の資金提供で開発されました

This feature was developed by [Germán Carrillo](https://github.com/gacarrillor)
### 機能：データ定義プロパティを持つポイントシンボルのDXFブロックの作成
特に複雑なデータ定義プロパティに対して、DXF内での参照の利用能力に追加機能が加えられ、繰り返されるポイントシンボルを含む複雑なレイヤーのDXF出力がはるかに小さくなります。

属性ハッシングのプロセスを使用してパフォーマンスを最適化し、すべての可能な属性の組み合わせを考慮します。多くの組み合わせが一意である場合、各ブロックはほぼ1回しか使用されず、大きな出力ファイルになります。このような場合を管理するため、"プロジェクトをDXFにエクスポート" ダイアログに、シンボルレイヤーごとのブロック数を制限するための新しい設定オプションが追加されました（-1は制限なしを意味します）。制限が整数値（例：5）に設定されている場合、参照数が最も多い5つのブロックのみが作成され、他のシンボルはインラインで書き込まれます。

![](images/entries/5de078fe33adb052f1177d7359432e69c84d81fa.webp)

この機能は [Stadtwerke München](http://www.swm.de) の資金提供で開発されました

This feature was developed by [mhugent](https://github.com/mhugent)
### 機能：DXFエクスポートに 'Use only selected features'  オプションの追加
DXFエクスポートダイアログに、現在の選択でアクティブな地物のみをエクスポートできる新しいオプションが追加されました。

デフォルトでは、この設定はfalseに設定されます。

![](images/entries/28e6ac14aac9b118efadc23167f795da2bc0c19c.webp)

この機能は [the QGIS user group Switzerland](https://www.qgis.ch/) の資金提供で開発されました

This feature was developed by [Germán Carrillo](https://github.com/gacarrillor)
### 機能：’DXFエクスポート" ダイアログ設定のインポート/エクスポートの追加
ユーザーがDXFエクスポートダイアログのGUI設定を保存および復元でき、再利用性を向上させるまたはコラボレーションを強化するために同僚と共有するための任意の数の設定をエクスポートできるようになります。

設定はXMLファイルにエクスポートされ、既存の設定値を上書きしてDXFエクスポート設定インターフェースに読み込むことができます。

![](images/entries/7f343b6a090823e6a090f4a33423cdd52fb655a8.webp)

この機能は [the QGIS user group Switzerland](https://qgis.ch/) の資金提供で開発されました

This feature was developed by [Germán Carrillo](https://github.com/gacarrillor)
## フォームとウィジェット
### 機能：カラーウィジェットへのCMYKサポートの追加
[CMYK QEP](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/283) に沿って、カラーウィジェットにCMYKカラーサポートが追加されました。

![](images/entries/b5572a60bcc06b580b55f42d2b87f6825daa5774.webp)

この機能は Métropôle de Bordeaux によった開発されました

This feature was developed by [Julien Cabieces](https://github.com/troopa81)
### 機能:リレーションエディターウィジェットを通じて子地物を追加/編集する際の親地物スコープの追加
属性フォームのリレーションエディターウィジェットを通じて子地物を追加および編集する際に、 current\_parent\_\* スコープが提供されるようになりました。

これはキャプチャされた地物または値が同時にキャプチャされている親エンティティに依存している可能性がある状況で非常に役立ちますが、親地物がまだキャプチャされていない場合、属性とジオメトリを取得できません。

この機能は [Hansestadt Herford](https://www.herford.de/) の資金提供で開発されました

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### 機能:値リレーションウィジェットのオートコンプリーターへの "一致を含む" の追加
以前は、オートコンプリート機能は文字列の先頭からのみ一致していましたが、新しいチェックボックスオプションにより、ユーザーが文字列全体内の含まれる値と一致させることができるようになりました。

古い動作は引き続きオートコンプリートのデフォルトであるため、この設定はオプトイン操作になります。

![](images/entries/3834e0b22600cce776ac149910fd9246bda6bd9c.webp)

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
### 機能:値リレーションのグループ化機能の実装
値リレーションエディターウィジェットにグループ化機能が追加され、ユーザーがアイテムを値のバケツに再グループ化できるようになりました。ユーザーはコンボボックスとテーブルウィジェットでグループ値をグループヘッダー名として表示するオプションも与えられています。

![](images/entries/3ef4fa48ee89cc91babb736dd477a1db6b66bcbc.webp)

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
## レイヤ凡例
### 機能: ベクターヒートマップレイヤーのカラーランプ凡例の表示
これらのレイヤーの凡例を表示しない代わりに、QGISはカラーランプをグラジェントバーとして表示するようになりました。

ユーザーは最小値/最大値ラベルのテキスト、バーの方向、フォント設定を制御できます

この更新はベクターレンダラーの内部APIへの変更も導入し、レンダラーが `QgsSymbolLegendNodes` 以外の他の種類の凡例ノードを作成する柔軟性を持ち、既存のレンダラーへの将来の拡張の機会を提供するようになりました。

![](images/entries/06b024c9294de21d36cc6efb702c342106a6242d.webp)

この機能は Rubicon Concierge Real Estate Services の資金提供で開発されました

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能: "壊れたレイヤーのみ表示"のレイヤーツリーフィルターの追加
チェックすると、ソースが壊れているレイヤーのみがツリーに表示されます。

これにより、ユーザーは大規模で複雑なプロジェクトで気づかれないかもしれない壊れたレイヤーを簡単に見つけることができるようになります！

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## プロセシング
### 機能: 履歴ダイアログでの詳細表示
プロセッシング履歴エントリを確認するための新しいツリー表示が提供されます。各エントリのルートアイテムはクリックするとアルゴリズムの完全なログを表示し、それぞれのPythonまたは qgis\_process コマンドが子アイテムとして表示されます。

これにより、すべての以前の情報を引き続き利用可能にしながら、履歴を閲覧するユーザーにより有用な情報が提供されます。

![](images/entries/34df4b46463545d3d9fc20168d386ffc04d9341d.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能: モデルデザイナーへの "選択したステップを実行" オプションの追加
新しいアクションにより、ユーザーはモデル内の選択したステップのみを実行でき、効果的にモデルのサブセットを実行できるようになります。

初期状態はデザイナーを通じたモデルの以前の実行から取得されるため、モデルの以前のステップの結果が選択されたステップで利用可能になります。

これにより、ユーザーはテストのために常にモデル全体を実行することなく、大きなモデルの一部を修正することが可能になります。 特に<br />モデルの初期ステップが時間のかかる場合に役立ちます！

この機能は City of Canning によって資金提供されました

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Add "View Output Layers" option for model child algorithms
When editing a model through the designer, a new right-click context option has been added for "View Output Layers" on any child step in the model<br />that has been run. Selecting this option will add the output layers from that step as new layers in the current QGIS project.

This action is available for all child algorithms in the model, even if the model is not configured to use the outputs from those children as model outputs. This action is also always available after running the model, even if the model itself fails (e.g. because of a misconfigured step later in the model).

This is designed as a helpful debugging action. If a user's model fails (or gives unexpected results), they will now be able to trace through the model and view the outputs for suspected problematic steps, avoiding the need to add temporary outputs to a model and re-run for testing purposes.

An additional "View Log" action has also been provided so that users can see the log for each child after the algorithm dialog has been closed down.

![](images/entries/f4357f5df60617753cb9fc215f4cce96f34139b2.webp)

この機能は City of Canning によって資金提供されました

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Endpoint distance threshold for network analysis
An optional end-point distance threshold parameter has been added to the network analysis tools.

The previous (and current default) behavior is that endpoints will ALWAYS be snapped to the nearest point in the network layer, regardless of how far away from the network they are, resulting in errors where points are snapped to an edge an arbitrary distance away.

The behavior of the threshold depends on the algorithm:
- For the “Service area (from layer)” tool an optional new output was added for “non-routable features”. This output will contain any features that were deemed too far from the network. All other features that are within tolerance distance to the network will be stored in the standard output from the tool.
- For the “Service area (from point)” tool an error will be raised if the point is too far from the network
- For the “Shortest path (point to point)” tool an error will be raised if either the source or destination points are too far from the network.
- For the “Shortest path (layer to point)” and “Shortest path (point to layer)” tools:
- An error will be raised if the **point** is too far from the network.
- A new optional output was added for “non-routable features”. This output will contain any features that were deemed too far from the network. All other features that are within tolerance distance to the network will be stored in the standard output from the tool.

この機能は City of Canning によって資金提供されました

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Add support for pure date and time decorators
QGIS Processing previously provided support for generating and processing datetime values as an explicit datetime type, but this release will support the definition of datetime, time, and date objects as discrete data types.

この機能は Ifremer によって資金提供されました

This feature was developed by [Jean Felder](https://github.com/ptitjano)
## アプリケーションとプロジェクトのオプション
### Feature: Add vertical crs option for projects
In line with [QEP \#267](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/267), a new vertical CRS option has been added to projects.

If the project CRS is a compound CRS, then the vertical CRS for the project will be the vertical component of the main project CRS. Otherwise, it will be the value explicitly set by the user.

Users can specify the vertical CRS through the Elevation Tab of the Project Properties.

If a compound CRS is defined as the active CRS for a project, the Vertical Reference System will infer the Vertical CRS definition. If the current project CRS is a 2D/ Horizontal CRS, then users will be able to define their own explicitly selected Vertical CRS.

This functionality does not impact rendering or feature handling and is currently a metadata property only.

The API for project objects has also been extended to support this functionality, and now includes methods for:
- crs(): The existing project method for the defined project CRS
- verticalCrs(): A new project method for fetching the Vertical Reference System
- [crs3D()](https://github.com/qgis/QGIS/pull/57107): An explicit getter for retrieving a compound reference system (combination of crs and verticalCrs)

![](images/entries/83cc370834aa045a61e3021da640753f406f4a23.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Add elevation range to project properties
This setting allows users to specify the upper and lower elevation limits associated with the project in line with [QEP 201](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/201), providing an equivalent user experience for filtering elevation range as users may already be familiar with for configuring the temporal range settings within projects.

This can be specified through the Elevation tab (renamed from "Terrain") in the Project Properties and extends the API of the QgsProjectElevationProperties class.

![](images/entries/c9f0765306562047cdba7a675587d484d5a7ce51.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## センサ
### Feature: Support feature expansion
This change allows SensorThings entities to be expanded to contain their related child feature attributes, exposing the relational SensorThings model as a traditional "flat" GIS-friendly table structure.

For example, when selecting Location entities, users can now opt to expand to "Things &gt; Datastreams &gt; Observations". This would result in multiple "stacked" point location features, one corresponding to each observation, with the attributes for each point feature containing the location, thing, datastream, and observation attributes.

This functionality is best used when combined with some extent, feature limit, or custom filter option, as this can otherwise result in very heavy requests to the backend service!

An option to limit the number of child features returned when expanding is provided. By default, a conservative amount of features will be returned to reduce the load on services and require users to explicitly "opt-in" to fetch large amounts of features.

![](images/entries/457f84d686c8c91d0fc894920ab462511226c0d2.webp)

This feature was funded by [BRGM](https://www.brgm.fr/en) and [Water4All Partnership](https://www.water4all-partnership.eu)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Add support for SensorThings Multidatastreams
This adds support for the Multidatastream entity type, as implemented in the SensorThings version 1.1 "MultiDatastream extension".

While the specification mandates that MultiDatastreams have an optional polygon geometry, many servers expose different geometry types for this entity or return errors when attempting to read the geometries from MultiDatastreams. Accordingly, QGIS now exposes an option to load MultiDatastreams as geometryless layers alongside the default option to load them as polygon layers, allowing users to handle a wider range of connections.

This feature was funded by [BRGM](https://www.brgm.fr/en) and [Water4All Partnership](https://www.water4all-partnership.eu)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Serial port sensor's data frame delimiter
A new data frame delimiter option has been added to the serial port sensor configuration.

In cases where multiple data frames are found in the last chunk of data pushed by the serial port, this implementation will return all data frames. Users can then use an expression to further split the returned last data value from the sensor into individual frames (e.g. using string\_to\_array).

![](images/entries/6cc5c72f2a9ff329f8a507e63e28d3771b26c0d3.webp)

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### Feature: Add an optional feature limit setting
Allows setting a maximum number of features to request from the service, avoiding overloading services with too many requests

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Implement subset string support for SensorThings
This allows setting custom filters on the layer, using the SensorThings filter syntax.

A custom layer filter GUI is provided for SensorThings layer filters, making it easier for users to craft valid filters using the SensorThings filter language.

This feature was funded by [BRGM](https://www.brgm.fr/en) and [Water4All Partnership](https://www.water4all-partnership.eu)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Profile Plots
### Feature: Add tolerance for lines and polygons
The elevation profile tool has been improved by adding tolerance support for lines and polygons (2D/ 3D), as illustrated using drillhole representations (from the [OpenLog plugin](https://plugins.qgis.org/plugins/openlog/)).

Without support for tolerances, any line or polygon feature is displayed in its entirety within the elevation profile plot as soon as it intersects the profile curve. By adding support for user-defined tolerances, only intersecting slices of the feature that fall within the defined region are rendered on the plot.

![](images/entries/25b1f63397246b4195891a08956b38239e78df07.gif)

This feature was funded by CEA/DAM François Renard

This feature was developed by [Benoit D.-M. - oslandia](https://github.com/benoitdm-oslandia)
## データプロバイダ
### Feature: Add extent based filtering for SensorThings layers
Allows users to set an extent limit for the layer so that features are only ever loaded within this extent.

The extent can be set using the data source manager before initially adding the layer, or modified within the source tab if the layer properties.

This feature was funded by [BRGM](https://www.brgm.fr/en) and [Water4All Partnership](https://www.water4all-partnership.eu)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Web proxy prefix support for ArcGIS URLs
A new prefix field is provided in ArcGIS settings dialogs that allows users to define the URL prefix of a web proxy used to access ArcGIS Services which will be prepended to all requests.

![](images/entries/671e0f4b015b4a575c6bb1255317f0af56a6c056.webp)

This feature was developed by [Vytax](https://github.com/Vytax)
### Feature: Add support for fast extent estimation on SAP HANA connections
Stored extent metadata can be utilized with the new "use estimated metadata" connection, which allows for precomputed extent estimation and much faster connectivity on large tables.

Although costly aggregation functions are avoided whenever the extent is recomputed, the extent information for HANA tables is only available after a delta merge. By default, this option will leverage a fallback to the standard behavior of using aggregation functions to compute extents in cases where the data is unavailable(or has not yet been computed).

![](images/entries/cf6ffc5f71ca8d57e9f3f717bf3e960c5afb51e4.webp)

This feature was developed by [Johannes Quast](https://github.com/jatsqi)
## QGISサーバー
### Feature: Default limit for GetFeatureInfo results
A new setting allows users to set a default FEATURE\_COUNT value individually for each WMS connection, with a predefined default value of 10.

This default also works when adding WMS layers from the browser and it can be overridden for each layer when added from the datasource manager.

The default user experience has not changed when adding layers from the data source manager, so the default of 10 still applies unless it is explicitly set from the connection settings.

![](images/entries/aa3907488d32cf1e90bb04115dfacffb5cdfee21.webp)

This feature was funded by [QGIS user group Germany (QGIS Anwendergruppe Deutschland e.V.)](https://qgis.de/)

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
### Feature: Add crs information in WMS GetFeatureInfo output when it differs from WGS84
GeoJSON explicitly requires the use of OGC:CRS84, but when a GetFeatureInfo request that explicitly requests a CRS that is not WGS84 is sent to a QGIS Server WMS, the output will now include the CRS definition in a manner compatible with the older [GeoJSON specification format](http://wiki.geojson.org/GeoJSON_draft_version_6#Specification) that included support for multiple Coordinate Reference Systems.

This feature was funded by Eurométropole de Strasbourg

This feature was developed by [Julien Cabieces](https://github.com/troopa81)
## プログラマビリティ
### Feature: Add replace/ replace all functionality to QgsCodeEditorWidget
The new replace functionality allows replacing matching text. If the regex find option is enabled, then captured groups from the regular expression pattern are available for use in the replacement string using the numeric identifier of the group (e.g. via `\1`).

In addition, the processing script editor has been ported to leverage the `QgsCodeEditorWidget` class and functionalities.

![](images/entries/286b7da77b39735f963327f8c0c373a4530023fc.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Register custom elevation profile sources
We've added a new `QgsProfileSourceRegistry` class to allow both core and plugin developers to register profile sources other than map layers (e.g., based on profile web services).

These custom profile sources can generate elevation profiles that are displayed in the main Elevation Profile dock widget and as layout items.

To do so, plugins should subclass `QgsAbstractPluginSource` and pass it to the registry via `registerProfileSource()`. Likewise, plugins should unregister (most likely on their `unload()` method) their registered sources via `unregisterProfileSource()`.

Like other QGIS registries, the profile source registry is available from the `QgsApplication` object: `QgsApplication.profileSourceRegistry()`.

![Custom profile source example](images/entries/custom_profile_source.webp)

この機能は [the QGIS user group Switzerland](https://www.qgis.ch/) の資金提供で開発されました

This feature was developed by [Germán Carrillo](https://github.com/gacarrillor)
## 注目すべき修正
### Feature: Bug fixes by Even Rouault (Spatialys)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.34 backport commit (GitHub) |
| --- | --- | --- | --- |
| QGIS cannot load feature classes from a .gdb with a 64bit ObjectID | [#57471](https://github.com/qgis/QGIS/issues/57471) | Probably no longer a bug with GDAL 3.9 |  |
| QGIS crashes while Export Data from a WFS-Service as DXF-File | [#57139](https://github.com/qgis/QGIS/issues/57139) | 再現できません |  |
| WFS connection problems after QGIS Update from LTR 3.28.2 to LTR 3.34.4 | [#56931](https://github.com/qgis/QGIS/issues/56931) | Not a QGIS bug |  |
| [GML] asGml3() creates invalid GML for CurvePolygon | [#57355](https://github.com/qgis/QGIS/issues/57355) | [PR #57476](https://github.com/qgis/QGIS/pull/57476) | [PR #57485](https://github.com/qgis/QGIS/pull/57485) |
| GDAL processing provider: "FutureWarning: Neither ogr.UseExceptions() nor ogr.DontUseExceptions() has been explicitly called" warning | [#57344](https://github.com/qgis/QGIS/issues/57344) | [PR #57477](https://github.com/qgis/QGIS/pull/57477) | Not appropriate |
| QGIS can't create conformant geopackage files with UTC "Z" timestamps | [#57262](https://github.com/qgis/QGIS/issues/57262) | [PR #57483](https://github.com/qgis/QGIS/pull/57483) | [PR #57548](https://github.com/qgis/QGIS/pull/57548) |
| QGIS cannot load feature classes from a .gdb with a 64bit ObjectID | [#57471](https://github.com/qgis/QGIS/issues/57471) | [GDAL PR 9980](https://github.com/OSGeo/gdal/pull/9980) | N/A |
| [OAPIF] Server defined fields are not fetched when creating a new feature | [#57486](https://github.com/qgis/QGIS/issues/57486) | [PR #57547](https://github.com/qgis/QGIS/pull/57547) | [PR #57549](https://github.com/qgis/QGIS/pull/57549) |
| QGIS3.28.15:Polygon Features from ArcGIS GDB Turn into TABLE after Editing in QGIS | [#57536](https://github.com/qgis/QGIS/issues/57536) | [GDAL PR 10008](https://github.com/OSGeo/gdal/pull/10008) | N/A |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Even Rouault (Spatialys)](https://www.spatialys.com/)
### Feature: Bug fixes by Alessandro Pasotti (itOpen / qcooperative)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.34 backport commit (GitHub) |
| --- | --- | --- | --- |
| QGIS Server GetFeatureInfo issue on WMTS layer | [#57441](https://github.com/qgis/QGIS/issues/57441) | [PR #57491](https://github.com/qgis/QGIS/pull/57491) | queued |
| Cannot connect to SQL Server on QGis 3.34.3 | [#56136](https://github.com/qgis/QGIS/issues/56136) | 再現できません |  |
| Balloon annotations fails to adopt text formatting | [#57423](https://github.com/qgis/QGIS/issues/57423) | 再現できません |  |
| Generate XYZ tiles' does not render labels from ArcGIS Vector Tile Service layers | [#57443](https://github.com/qgis/QGIS/issues/57443) | [PR #57517](https://github.com/qgis/QGIS/pull/57517) | queued |
| Empty space after host name in SQL server, cause inconsistent error | [#57358](https://github.com/qgis/QGIS/issues/57358) | [PR #57518](https://github.com/qgis/QGIS/pull/57518) | queued |
| GDAL/OGR processing algorithms may silently output incorrect result if an input is a vector "memory" layer with a "fid" column | [#57343](https://github.com/qgis/QGIS/issues/57343) | [PR #57522](https://github.com/qgis/QGIS/pull/57522) | queued |
| attribute table row sorting doesn't work | [#57338](https://github.com/qgis/QGIS/issues/57338) | [PR #57624](https://github.com/qgis/QGIS/pull/57624) | queued |
| Unable to edit elements in the print layout after locking an element | [#57331](https://github.com/qgis/QGIS/issues/57331) | [PR #57543](https://github.com/qgis/QGIS/pull/57543) | queued |
| QGIS 3.34 LTR not loading REST services with referers | [#57288](https://github.com/qgis/QGIS/issues/57288) | Cannot reproduce (on master) |  |
| New Postgis/Postgres connection NOT saving username/password when requested | [#57284](https://github.com/qgis/QGIS/issues/57284) | [PR #57544](https://github.com/qgis/QGIS/pull/57544) |  |
| setting labeling font size to less than 0.3 freezes qgis with meters units | [#57336](https://github.com/qgis/QGIS/issues/57336) | [PR #57560](https://github.com/qgis/QGIS/pull/57560) |  |
| Server: OAPIF/WFS3 service collection id missmatch | [#57556](https://github.com/qgis/QGIS/issues/57556) | [PR #57561](https://github.com/qgis/QGIS/pull/57561) | queued |
| [Layout manager] The wordwrap expression function fails if the legend item is set to hidden | [#57589](https://github.com/qgis/QGIS/issues/57589) | Cannot reproduce (on master) - closed by OP |  |
| [ux][layouts] Fix legend item style mutex | 未報告 | [PR #57605](https://github.com/qgis/QGIS/pull/57605) | N/A |
| Expression output won't show until you open the attribute table (PostGIS layers) | [#57578](https://github.com/qgis/QGIS/issues/57578) | Cannot reproduce (on master and 3.36) |  |
| QGIS Server wrongly positions the map objects in the output when there's more than one map | [#57631](https://github.com/qgis/QGIS/issues/57631) | バグではない |  |
| Current selected feature still marked as "dirty" after save in attribute table's form view | [#57644](https://github.com/qgis/QGIS/issues/57644) | [PR #57674](https://github.com/qgis/QGIS/pull/57674) |  |
| JSON-String not read from GPKG | [#57673](https://github.com/qgis/QGIS/issues/57673) | [PR #57707](https://github.com/qgis/QGIS/pull/57707) | N/A |
| value maps ignore field length | [#57634](https://github.com/qgis/QGIS/issues/57634) | [PR #57690](https://github.com/qgis/QGIS/pull/57690) |  |
| Identify Results for raster data value does not use correct decimal separator | [#57765](https://github.com/qgis/QGIS/issues/57765) | [PR #57769](https://github.com/qgis/QGIS/pull/57769) | queued |
| Value relation dropdown issue -Dropdown list selection reverts to default value upon selecting subtype option | [#57808](https://github.com/qgis/QGIS/issues/57808) | Cannot reproduce (awaiting feedback) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Alessandro Pasotti (itOpen / qcooperative)](https://www.qcooperative.net/)
### Feature: Bug fixes by David Signer (OPENGIS)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.34 backport commit (GitHub) |
| --- | --- | --- | --- |
| Wrongly displayed action widget | [#33464](https://github.com/qgis/QGIS/issues/33464), [#57398](https://github.com/qgis/QGIS/issues/57398), [#56966](https://github.com/qgis/QGIS/issues/56966) | [PR #57475](https://github.com/qgis/QGIS/pull/57475) | Not appropriate |
| Custom properties variableNames and variableValues are cleared when more than one layer custom variable exist | [#57334](https://github.com/qgis/QGIS/issues/57334) | [PR #57490](https://github.com/qgis/QGIS/pull/57490) | Not appropriate |
| Default values depending on other fields are not correctly applied when field not part of form made by Drag and Drop Designer | [#57411](https://github.com/qgis/QGIS/issues/57411) | [PR #57527](https://github.com/qgis/QGIS/pull/57527) | Not appropriate |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [David Signer (OPENGIS)](https://www.opengis.ch/)
### Feature: Bug fixes by Sandro Santilli (strk)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.34 backport commit (GitHub) |
| --- | --- | --- | --- |
| Source-tree documentation improvements | 未報告 | [PR #57594](https://github.com/qgis/QGIS/pull/57594) |  |
| QGIS DB manager lowercase conversion is broken | [#52898](https://github.com/qgis/QGIS/issues/52898) | [PR #57645](https://github.com/qgis/QGIS/pull/57645) |  |
| "money" type (postgresql) interpreted as string | [#25529](https://github.com/qgis/QGIS/issues/25529) | [PR #57513](https://github.com/qgis/QGIS/pull/57513) |  |
| Fix podman run of container-based testing | [#57724](https://github.com/qgis/QGIS/issues/57724) | [PR #57688](https://github.com/qgis/QGIS/pull/57688) |  |
| QGIS 3.34 is not able to figure out PostgreSQL relations when there are build using compound keys | [#56420](https://github.com/qgis/QGIS/issues/56420) | [PR #57653](https://github.com/qgis/QGIS/pull/57653) | [PR #57817](https://github.com/qgis/QGIS/pull/57817) |
| Fix PostgreSQL compound key discovery | [#56420](https://github.com/qgis/QGIS/issues/56420) | [PR #57653](https://github.com/qgis/QGIS/pull/57653) | [PR #57817](https://github.com/qgis/QGIS/pull/57817) |
| Extent of data fetched from GEOGRAPHY PostGIS column can not be changed | [#30294](https://github.com/qgis/QGIS/issues/30294) | [PR #57514](https://github.com/qgis/QGIS/pull/57514) |  |
| test_core_project test fail if TMPDIR is set to anything but /tmp | [#57610](https://github.com/qgis/QGIS/issues/57610) | [PR #57606](https://github.com/qgis/QGIS/pull/57606) |  |
| Tests create directories under ~/.local/share | [#50587](https://github.com/qgis/QGIS/issues/50587) |  |  |
| Directory /tmp full of QGIS temporary files after ctest run | [#48884](https://github.com/qgis/QGIS/issues/48884) |  |  |
| test_provider_postgresprovider TestPyQgsPostgresProvider.testExtent doesn't test extent | [#57818](https://github.com/qgis/QGIS/issues/57818) | [PR #57829](https://github.com/qgis/QGIS/pull/57829) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Sandro Santilli (strk)](https://strk.kbt.io/)
### Feature: Bug fixes by Julien Cabieces (Oslandia)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.34 backport commit (GitHub) |
| --- | --- | --- | --- |
| Avoid crash on summary when error list is empty | 未報告 | [PR #57658](https://github.com/qgis/QGIS/pull/57658) | [PR #57661](https://github.com/qgis/QGIS/pull/57661) |
| Masking symbol of current layer not listed in style panel | [#57248](https://github.com/qgis/QGIS/issues/57248) | [PR #57679](https://github.com/qgis/QGIS/pull/57679) | [PR #57783](https://github.com/qgis/QGIS/pull/57783) |
| Marker Line masking not working for layout prints or PDF exports | [#57564](https://github.com/qgis/QGIS/issues/57564) | [PR #57694](https://github.com/qgis/QGIS/pull/57694) |  |
| Qgis crashes while digitising lines | [#57617](https://github.com/qgis/QGIS/issues/57617) | 再現できません |  |
| Crash when running Topology Checker to validate corrective edits. | [#53425](https://github.com/qgis/QGIS/issues/53425) | [PR #57695](https://github.com/qgis/QGIS/pull/57695) | [PR #57712](https://github.com/qgis/QGIS/pull/57712) |
| Topology Checker crashes | [#57627](https://github.com/qgis/QGIS/issues/57627) | [PR #57695](https://github.com/qgis/QGIS/pull/57695) | [PR #57712](https://github.com/qgis/QGIS/pull/57712) |
| Debian sid Qt6 compile fails on sip build, python bindings | [#57760](https://github.com/qgis/QGIS/issues/57760) | upstream issue, wait for PyQt/sip mailing list answer |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Julien Cabieces (Oslandia)](https://oslandia.com/)
### Feature: Bug fixes by Jacky Volpes (Oslandia)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.34 backport commit (GitHub) |
| --- | --- | --- | --- |
| copy/paste feature tool sets integer/decimal fields of destination feature to 0 if the source feature fields are NULL | [#57710](https://github.com/qgis/QGIS/issues/57710) | [PR #57851](https://github.com/qgis/QGIS/pull/57851) | [PR #57855](https://github.com/qgis/QGIS/pull/57855) |
| Postgres layer with multi geometry columns fails to export | [#57757](https://github.com/qgis/QGIS/issues/57757) | バグではない |  |
| Georeferencing tool: default name for export with an accent in french (_modifié) | [#55389](https://github.com/qgis/QGIS/issues/55389) | [Transifex](https://app.transifex.com/qgis/QGIS/translate/#fr/$/412589941?q=text%3A_modified) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Jacky Volpes (Oslandia)](https://oslandia.com/)
### Feature: Bug fixes by Jean Felder (Oslandia)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.34 backport commit (GitHub) |
| --- | --- | --- | --- |
| qgsabstractmaterialsettings: Handle selection in addParametersToEffect | 未報告 | [PR #57803](https://github.com/qgis/QGIS/pull/57803) | not backported |
| qgs3daxis: Fix cube face picking | 未報告 | [PR #57848](https://github.com/qgis/QGIS/pull/57848) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Jean Felder (Oslandia)](https://oslandia.com/)
### Feature: Bug fixes by Nyall Dawson (North Road)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.34 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fix bugs relating to selective masking vector exports | [#50734](https://github.com/qgis/QGIS/issues/50734) | [PR #57843](https://github.com/qgis/QGIS/pull/57843) | Too intrusive |
| Fix bugs relating to selective masking vector exports | [#54788](https://github.com/qgis/QGIS/issues/54788) | [PR #57703](https://github.com/qgis/QGIS/pull/57703) | Too intrusive |
| Fix bugs relating to selective masking vector exports | [PR #57623](https://github.com/qgis/QGIS/pull/57623) | Too intrusive |  |
| Fix bugs relating to selective masking vector exports | [PR #57498](https://github.com/qgis/QGIS/pull/57498) | Too intrusive |  |
| Pressing escape should clear current identify results | [#47984](https://github.com/qgis/QGIS/issues/47984) | [PR #57774](https://github.com/qgis/QGIS/pull/57774) | N/A |
| Fix some grass vectors incorrectly show as datasets | 未報告 | [PR #57780](https://github.com/qgis/QGIS/pull/57780) | [PR #57786](https://github.com/qgis/QGIS/pull/57786) |
| Don't try to load extent strings as layers | [#57758](https://github.com/qgis/QGIS/issues/57758) | [PR #57772](https://github.com/qgis/QGIS/pull/57772) | [PR #57787](https://github.com/qgis/QGIS/pull/57787) |
| Limit fixed interval classification to generate at most 999 classes | [PR #50290](https://github.com/qgis/QGIS/pull/50290) | [PR #57722](https://github.com/qgis/QGIS/pull/57722) | Not appropriate |
| Don't try to connect widget to null vector tile layers | 未報告 | [PR #57721](https://github.com/qgis/QGIS/pull/57721) | N/A |
| Don't show invalid "Style not found in database" warning when adding vector tile layers | 未報告 | [PR #57714](https://github.com/qgis/QGIS/pull/57714) | Not appropriate |
| Replace processing default extension setting with string based setting | [#57676](https://github.com/qgis/QGIS/issues/57676) | [PR #57702](https://github.com/qgis/QGIS/pull/57702) | Not appropriate |
| Fix incorrect attempts to load outputs from models to projects | [#57698](https://github.com/qgis/QGIS/issues/57698) | [PR #57701](https://github.com/qgis/QGIS/pull/57701) | [PR #57715](https://github.com/qgis/QGIS/pull/57715) |
| Fix add feature dialog does not restore position when shown modally | 未報告 | [PR #57686](https://github.com/qgis/QGIS/pull/57686) | [PR #57700](https://github.com/qgis/QGIS/pull/57700) |
| Fix python script editor "open in external editor" action | 未報告 | [PR #57682](https://github.com/qgis/QGIS/pull/57682) | Not appropriate |
| Fix broken prefetch capabilities for raster layers | 未報告 | [PR #57663](https://github.com/qgis/QGIS/pull/57663) | [PR #57667](https://github.com/qgis/QGIS/pull/57667) |
| Fix missing field type information in eg the horizontal header tooltips in attribute table | 未報告 | [PR #57621](https://github.com/qgis/QGIS/pull/57621) | Not appropriate |
| Don't try to paint to indexed image | 未報告 | [PR #57601](https://github.com/qgis/QGIS/pull/57601) |  |
| Clamp values for set_color_part function to avoid qt warnings when out of range values are specified | 未報告 | [PR #57600](https://github.com/qgis/QGIS/pull/57600) |  |
| Add some tests for rendering text with RTL markers | [PR #57586](https://github.com/qgis/QGIS/pull/57586) |  |  |
| Fix rotation based orientation when html labeling enabled | 未報告 | [PR #57582](https://github.com/qgis/QGIS/pull/57582) | Too intrusive |
| Fix data defined font size is ignored when HTML labeling is active | 未報告 | [PR #57582](https://github.com/qgis/QGIS/pull/57582) | Too intrusive |
| Don't set @value to line height when evaluating multi line alignment | 未報告 | [PR #57582](https://github.com/qgis/QGIS/pull/57582) | Too intrusive |
| Don't try to load CRS strings as map layers | [#57494](https://github.com/qgis/QGIS/issues/57494) | [PR #57508](https://github.com/qgis/QGIS/pull/57508) | [PR #57541](https://github.com/qgis/QGIS/pull/57541) |
| Don't try to load CRS strings as map layers | [#57494](https://github.com/qgis/QGIS/issues/57494) | [PR #57576](https://github.com/qgis/QGIS/pull/57576) | [PR #57579](https://github.com/qgis/QGIS/pull/57579) |
| Fix line extension tool when layer crs != map crs | [#49267](https://github.com/qgis/QGIS/issues/49267) | [PR #57575](https://github.com/qgis/QGIS/pull/57575) |  |
| Fix incorrect buffers drawn for html label item | 未報告 | [PR #57551](https://github.com/qgis/QGIS/pull/57551) | [PR #57571](https://github.com/qgis/QGIS/pull/57571) |
| Fix label mask sizes get reset to 0 | 未報告 | [PR #57555](https://github.com/qgis/QGIS/pull/57555) | [PR #57569](https://github.com/qgis/QGIS/pull/57569) |
| Fix tab stops in legend text | [#56981](https://github.com/qgis/QGIS/issues/56981) | [PR #57554](https://github.com/qgis/QGIS/pull/57554) | N/A |
| Fix colors for new diagram categories are not randomly picked | [#56862](https://github.com/qgis/QGIS/issues/56862) | [PR #57532](https://github.com/qgis/QGIS/pull/57532) | [PR #57539](https://github.com/qgis/QGIS/pull/57539) |
| Make brush and stroke style combo box icons visible on dark themes | 未報告 | [PR #57506](https://github.com/qgis/QGIS/pull/57506) | [PR #57510](https://github.com/qgis/QGIS/pull/57510) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)

{{<content-end >}}
