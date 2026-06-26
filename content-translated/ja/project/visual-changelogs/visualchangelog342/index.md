---
HasBanner: false
draft: false
releaseDate: '2025-02-21'
section: project
sidebar: true
title: QGIS 3.42 の変更履歴
type: visual-changelog

---
{{<content-start >}}
# QGIS 3.42 の変更履歴{#changelog342 }
![](images/projects/b5beabaeef257557086b43ccdceffed3c78d8676.png.webp)

リリース日: 2025-02-21

QGISプロジェクトは、フリー＆オープンソース地理空間情報システムの開発における重要な前進となる、QGIS 3.42のリリースを誇りを持って発表します。このリリースは過去のリリースの堅固な基盤の上に構築され、ワークフローを効率化し空間分析におけるユーザーの能力を高める新しい機能と機能強化をもたらします。

3Dマップビューの各種機能、プロットやプロファイル、複雑なデータセットのナビゲーションを向上させる新しい仮想ポイントクラウドオーバービューウィジェットなど、従来のマップフレームを超えた機能に顕著な機能強化が導入されました。CSSベースのラベルプロパティやPython APIの拡張など、カートグラフィー機能のより細かい制御が提供される一方、メッシュやポイントクラウドなどの高度なデータタイプにも充実した改善が加えられています。

プロセッシングツールボックスに新しいメタデータツールのセット（およびその他のさまざまな新機能と機能強化）が追加された一方、ユーザーがラスターデータのピクセルにラベルを付けられる新機能も追加されました。レイアウトツールも忘れられておらず、QGISのPythonコンソールにも開発者体験を向上させるプロジェクトドキュメントソースとの直接統合を備えた新しいインタラクティブヘルプ機能が追加されました。

For a whirlwind tour of all the new functionalities introduced, you can view the [highlight reel video on YouTube](https://www.youtube.com/watch?v=v6Ejov4u7xk).
 導入されたすべての新機能を手早く確認するには、　 [YouTubeのハイライト動画](https://www.youtube.com/watch?v=v6Ejov4u7xk) をご覧ください。

[![](https://img.youtube.com/vi/v6Ejov4u7xk/0.jpg)](https://www.youtube.com/watch?v=v6Ejov4u7xk)

QGISはコミュニティによる取り組みです。このリリースを実現するために時間と労力をボランティアで提供してくださった（または資金援助をしてくださった）開発者・ドキュメント作成者・テスター・その他多くの方々に心より感謝申し上げます。QGISコミュニティより、このリリースをお楽しみいただければ幸いです！QGISをさらに素晴らしいものにするために、時間・資金・その他の形でご貢献いただける方は、ぜひ [QGIS.ORG](https://qgis.org) をご覧いただき、お力をお貸しください！

QGISは寄付者およびサステイニングメンバーによって支えられています。プロジェクトに大小を問わず財政的な貢献をしてくださった寄付者の最新リストは  [寄付者一覧](https://qgis.org/en/site/about/sustaining_members.html#list-of-donors) でご覧いただけます。公式のプロジェクトサステイニングメンバーになることをご希望の方は、詳細について  [サステイニングメンバーページ](https://qgis.org/en/site/about/sustaining_members.html) をご覧ください。QGISへのスポンサーシップは、定期的な開発者ミーティングの開催、プロジェクトインフラの維持、およびバグ修正活動の資金として活用されます。現在のスポンサーの完全なリストを以下に掲載します。すべてのスポンサーの皆様に心より感謝申し上げます！

QGIS はフリーのソフトウェアです。利用する上で金銭を支払う義務はありません。実際、私たちは利用者の財政状況や社会的地位にかかわらず、より多くの人に QGIS を利用して欲しいと思っています。私たちは地理空間的な意思決定ツールによって人々が力を持つことが、全人類の社会をより良くすると信じています。
## シンボロジ
### 機能: シンボルへの設定可能な範囲バッファーの追加
以前のバージョンのQGISでは、特定の条件下でキャンバスの範囲内に位置する地物のみがレンダリングの対象として考慮されていました。

これにより、特に複雑なジオメトリジェネレーターを使用する場合に特定のシンボロジーで問題が発生していました。レンダリングされたシンボルはキャンバス内に表示されるものの、ソース地物がキャンバス内に存在しない地物がユーザーに見えないという問題でした。

例えば、 `buffer(@geometry, 7)`  のようなバッファーポリゴンを生成するためにポイント地物を使用している場合、ポイントがキャンバスの範囲内にないとバッファーがレンダリングされませんでした。

シンボルの新しい設定オプションにより、キャンバス範囲のバッファーを設定して、ユーザー定義の制約内でこれらの追加地物を包含し、複雑なデータ可視化の要件とパフォーマンスのバランスを取ることができるようになります。

![](images/entries/bf954ba6632135c099f5e5d7f8db594e19dc01a2.png.webp)

この機能はthe National Land Survey of Finland. の資金提供で開発されました

この機能は [Juho Ervasti](https://github.com/JuhoErvasti) によって開発されました
## ラベリング
### 機能: ラスターラベリング
QGISがラスターバンドから取得した値でラスターピクセルにラベルを付けられるようになりました。ラベルはラベリングエンジンに登録されるため、ラベルの競合解決と重なり回避に参加します。オプションには以下が含まれます:
- 値を取得するバンドの選択
- QgsNumericFormat を使用したラベルの数値フォーマットのカスタマイズ
- テキストレンダラーを使用するため、バッファー、シャドウなどをサポート
- ラベル優先度
- スケール依存の表示
- オプションのピクセルサイズ依存の表示（例：ピクセルが4mm以上のサイズの場合にのみ表示）
- Zインデックス制御、重なり回避モード
- 隣接ピクセルにリサンプリングされた値を表示するオプション

![](images/entries/0ac302054a6a0e64bc140f4e7ebd403f0894a634.png.webp)

この機能は Canton de Neuchâtel の資金提供で開発されました

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能: ラベルのカスタムタブ間隔
ラベルに単一の距離ではなく、カスタムタブストップ距離のリストを設定できます。これにより改行間で異なるしきい値を使用することが可能になります。

![](images/entries/fb24a7593018d5732f9e3b64a68912e38d431dd3.png.webp)

この機能は City of Freiburg im Breisgau によって資金提供されました

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能: ラベル/テキストレンダラーでのCSS背景プロパティのサポート
QGISがHTMLラベルで使用した際のCSSの background-color および background-image プロパティをサポートするようになりました。
-  バックグラウンドはブロックアイテム (e.g. `<div>`) またはインラインアイテム (e.g. `<span>`) でサポートされています。
- 画像の場合、CSSは background-image: url(xx) の形式で記述してください。ローカルファイルパス、HTTPリンク、またはbase64埋め込みコンテンツをサポートしています。
- バックグラウンドはカーブドテキストではサポートされていません
- HTMLのバックぐうラウンドは常にラベルの背景シェイプの上にレンダリングされ、ドロップシャドウ/バッファーの下にレンダリングされます。

この機能は City of Freiburg im Breisgau によって資金提供されました

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能: HTMLラベルのブロック要素でのCSSマージンのサポート
QGISがテキストレンダラーのブロック要素でCSSマージンプロパティのサポートを追加しました。具体的には:
- これはブロック型要素（例：DIV、P、H1〜H6）のみで利用可能です。
-  マージンはspanやその他の非ブロックコンテンツには使用できません（Qtの制限による）。
- マージンはptの単位でのみ指定できます。
- マージンは "margin-left: 5pt; margin-right: 10pt" などの形式か、"margin: 5pt 0pt 10pt 0pt" の形式で指定できます
- 負のマージンは下マージンのみサポートされています（Qtの制限による）。

この機能は City of Freiburg im Breisgau によって資金提供されました

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能: HTMLラベルでのCSS line-height のサポート
 QGISがHTMLフォーマットのラベルで line-height CSSプロパティのサポートを追加しました

ポイントまたはパーセントでの line-height をサポートしています。例："line-height: 40pt" または "line-height: 40%"

この機能は City of Freiburg im Breisgau によって資金提供されました

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## メッシュ
### 地物: メッシュレンダリング範囲設定
メッシュのレンダラー設定に、現在のキャンバス範囲に基づいてカラーランプレンダラーの最小値/最大値の限界を設定するオプションが追加されました。これはラスターレイヤーと同様のレンダリング動作を使用して、特定のキャンバスインスタンスにロックしたり、アクティブなキャンバスに基づいて変更したりすることができます。

![](images/entries/36f92b26c173dbaddf798eb572e795a1759b2b5e.webp)

この機能は [Jan Caha](https://github.com/JanCaha) によって開発されました
### 機能: メッシュ編集のドロネー細分化
メッシュ編集に新しいドロネー細分化オプションが追加されました。メッシュフェイスに頂点を追加する際、この機能により隣接する三角形フェイスを自動的に細分化できます。アルゴリズムは隣接フェイスのエッジがドロネー条件を満たすかどうかを確認し、満たさない場合はメッシュ品質を向上させるためにエッジを自動的に反転させます。

![](images/entries/80bfb4d962708d894f5ae8735a8cf19d5de14dad.gif)

この機能は [Jan Caha](https://github.com/JanCaha) によって開発されました
### 機能: メッシュレイヤーのデータセットグループコントロール
メッシュレイヤーでより柔軟なデータセットグループ管理が可能になりました。ユーザーは同じ名前（ただし異なるURIから）のデータセットグループをメッシュレイヤーに追加できます。混乱を避けるため、重複した名前には自動的に数字が付加されます（例："Original Name\_1"）。

また、メッシュレイヤーからデータセットグループを削除できるようになりましたが、削除できるのは追加されたデータセットグループ（元のメッシュソースファイルに関連付けられていないもの）のみです。これによりコアデータの誤削除を防止します。

![](images/entries/dc92e7714bf34361837b67c23cd3faf1ea5bb797.webp)

この機能は [Jan Caha](https://github.com/JanCaha) によって開発されました
### 機能: メッシュ選択アクション
メッシュレイヤーの頂点を選択するための2つの新しいアクションが追加されました:
- どのフェイスにも属さない孤立した頂点を選択
- メッシュレイヤーのすべての頂点を選択

これによりユーザーは特定の頂点の選択条件をより細かく制御できるようになります。

![](images/entries/537402aa2d62c6db821d0f6eea457785adfbfc86.webp)

この機能は [Jan Caha](https://github.com/JanCaha) によって開発されました
### 機能: 追加されたメッシュ頂点の標高割り当てモード
"メッシュ要素のデジタイズ"ツールに、新しく作成された頂点のZ値割り当てに使用する方法を選択するための追加メニューが追加されました。新しいオプションには以下が含まれます:
- メッシュを優先、次にZウィジェット（頂点がメッシュのフェイス内にある場合はメッシュからZ値を補間し、そうでない場合はZウィジェットの値を使用）
- メッシュを優先、次に地形（頂点がメッシュのフェイス内にある場合はメッシュからZ値を補間し、そうでない場合は地形の値を使用）
- プロジェクト地形（常にプロジェクト地形のZ値を使用）
- Zウィジェット（常にウィジェットからZ値を取得）

"メッシュ頂点の変換" パネルにも、プロジェクト地形設定に基づいた推定値から選択した頂点のZ値を設定できる新しいボタンが追加されました。

![](images/entries/134e4b88cb478ff8c1d72fc1eb35cf873e416ab4.png.webp)

この機能は [Jan Caha](https://github.com/JanCaha) によって開発されました
## 三次元機能
### 機能: 3D ビューのデバッグウィジェット
3Dマップビューの新しいデバッグサイドパネルにより、関連するすべてのデバッグ設定が1か所に集約されました。

![](images/entries/b676f80f03eeac81a44dd5d95c21a1dd1d968d42.webp)

この機能は [Matej Bagar](https://github.com/Withalion) によって開発されました
## 点群
### 機能: 2Dでの仮想ポイントクラウドの概観表示
VPCレンダリングのデフォルト動作が変更されました。概観が存在する場合はそれがレンダリングされ、ズームアウト時には代わりに範囲がレンダリングされます。スタイリングパネルからのレイヤー設定により、ユーザーが好む動作を詳細に制御でき、範囲のみのレンダリング、概観のみのレンダリング、または両者の組み合わせをシームレスに切り替えることができます。

![](images/entries/76df45b4beff919f1428f39e13370c5bd48facb1.png.webp)

この機能は Klimadatastyrelsen の資金提供で開発されました

この機能は [Matej Bagar](https://github.com/Withalion) によって開発されました
## 印刷レイアウト
### 機能: レイアウトラベルのマウスハンドルをダブルクリックするとテキストに合わせてサイズ変更できます
ハンドルをダブルクリックすると、含まれるテキストにぴったり収まるようにラベルが自動サイズ調整されます（必要に応じて拡大または縮小）。ラベルの反対側は固定されたまま維持されます。例えば、右下のハンドルをダブルクリックするとラベルの右下の角が移動します。

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能: レイアウトアイテムのダブルクリック時のアクション
QGIS APIが拡張され、印刷レイアウト要素のダブルクリックにイベントが追加されました。これにより、将来的により高度な機能（例：アイテムをダブルクリックして編集）を導入することが可能になります。

This feature was developed by [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
### 機能: レイアウトのノードアイテム作成の改善
レイアウトツールでシェイプをデジタイズする際の動作が、既存のデジタイズツールのユーザーエクスペリエンスとより整合するよう変更されました。これにより、ユーザーはシェイプで誤って取得した頂点を削除できるようになります。

![](images/entries/65a754c47bc5d678e9716fc168d3802a96b04a2e.gif)

This feature was developed by [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
### 機能: レイアウトのページサイズをすべてのページに適用します
複数ページのレイアウトのページプロパティパネルに新しい "すべてのページに適用" ボタンが追加され、ユーザーが複雑なレイアウトプロパティの変更をより効率的に行えるようになりました。

![](images/entries/17edee9a6187866ed824fe92134f088e32327056.webp)

This feature was developed by [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
### 機能: レイアウトJPGエクスポートの新しい品質パラメーター
印刷レイアウトのJPEG/JPG画像エクスポートオプションに新しい品質パラメーターが追加され、ユーザーがエクスポートオプションをより細かく制御できるようになりました。

![](images/entries/ddc1fa979771c938ec22dabcadefda2cd79aa96b.webp)

This feature was developed by [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
## デジタイズ
### 機能: トリム/延長の交差平面のハイライト表示
トリム/延長機能のスタイリングと動作が高度デジタイズツールのUXとより密接に整合するよう変更されました。これによりジオメトリの境界がユーザーにより明確に視覚的に表現されるようになります。

![](images/entries/afff864bb555fcfba93b700cf4f63c7e2eb65390.webp)

This feature was developed by [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
## データ管理
### 機能: ジオリファレンサーでのスナッピングの有効化
データセットを位置合わせする際の基準点をより細かく制御できるよう、ジオリファレンサーインターフェースに高度デジタイズパネルとスナッピングオプションが追加されました。

![](images/entries/5d2403406b6bf2644f6ba0d60a77364dc80b4c7b.png.webp)

This feature was developed by [Denis Rouzaud](https://github.com/3nids)
### 機能: データソースマネージャーのSTAC機能強化
 [QEP\#300](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/300) の一環としてQGIS 3.40で導入されたSTACクライアント機能を基に、QGISのSTACクライアントは以下を含む追加機能をサポートするようになりました:
- データソースマネージャー内でのSTACカタログ検索機能
- 返された結果の高度なフィルタリング
- マップキャンバスへの検索結果アイテムのフットプリントの表示/非表示
- 選択したアイテムのフットプリントのハイライト表示

![](images/entries/86d59b6e6bbcafcd505cc6301d26f55b295566db.webp)

This feature was developed by [Stefanos Natsis](https://github.com/uclaros)
## フォームとウィジェット
### 機能: 値リレーションウィジェットへの追加ソートオプション
値リレーションウィジェットに以下を含むいくつかの新しいソートオプションが追加されました:
- 逆順
- 特定のフィールド値による並び替え

![](images/entries/ea40b733da3f998b83590ce985986cf8438fe2d7.webp)

本機能は Consorzio della Bonifica Renana の資金提供で開発されました

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
### 機能: フォームのデザイン時のウィジェット設定のコピー＆ペースト
ベクターレイヤープロパティダイアログの  `利用可能なウィジェット`  パネルにコンテキストメニューが追加されました。これにより、同じレイヤーのフィールド間、QGISプロジェクト内の異なるレイヤーのフィールド間、または異なるQGISインスタンスのレイヤーのフィールド間でウィジェット設定をコピー＆ペーストできるようになります

![Copy and paste context menu](images/entries/copy_paste_widget_configuration.webp)

この機能は Ville de Pully (Switzerland) の資金提供で開発されました

This feature was developed by [Germán Carrillo](https://github.com/gacarrillor)
## プロセシング
### 機能: プロセッシングメタデータツール
レイヤーメタデータをより適切に処理するための新しいネイティブアルゴリズムがプロセッシングツールボックスに追加されました。
- 入力レイヤーから対象レイヤーにメタデータをコピーするレイヤーメタデータのコピー
- QMDファイルからレイヤーメタデータを設定するレイヤーメタデータの適用
- QMDファイルにレイヤーメタデータをエクスポートするレイヤーメタデータのエクスポート
- レイヤーに定義された既存のエントリに新しい履歴エントリを追加する履歴メタデータの追加
- 入力レイヤーの空でないメタデータフィールドを対象レイヤーにコピーし、入力の空フィールドは対象レイヤーで変更せずに維持するレイヤーメタデータの更新
- シンプルなメタデータフィールド（識別子、親識別子、タイトル、タイプ、エンコーディング、言語、CRS、概要、料金）を設定する　メタデータフィールドの設定

![](images/entries/a61da0150028588dafa6e2fb98c0f71d628bdd29.png.webp)

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
### 機能: 散布図でのホバーコンテンツの式ベース設定
ベクターレイヤー散布図プロセッシングアルゴリズムの新しいオプションにより、QGIS式を使用してホバー時に表示されるテキストをオプションで追加できるようになりました

![](images/entries/43b93ee8f5a7632654207f5d31345ea9a66ec538.webp)

この機能は [Florian Neukirchen](https://github.com/florianneukirchen) によって開発されました
### 機能: ベクターレイヤーのマージツールへの  'layer'  属性と 'path' 属性を含めるオプションの追加
ベクターレイヤーのマージプロセッシングツールに新しいチェックボックスオプションが追加されました。このオプションにより、個々の入力ベクターレイヤーのlayer属性とpath属性を結果のマージされたレイヤーに含めるかどうかをユーザーが選択できます。後方互換性を維持するため、このオプションはデフォルトで有効になっています。

この機能は [Nass](https://github.com/lanckmann) によって開発されました
### 機能: ジオメトリチェッカーのプロセッシングツールへの移動
すべてのジオメトリとトポロジーの検証/確認方法を統一することを目指す [QEP\#236](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/236) の目標に沿って、ジオメトリチェッカーがQGISプロセッシングツールボックスに統合されました。

これらのアルゴリズムは "ジオメトリのチェック" および "ジオメトリの修正" カテゴリにそれぞれ追加されており、各アルゴリズムは単一の入力レイヤーと2つの出力レイヤーを持つ一貫した操作性を維持しています。

チェックプロセッシングアルゴリズムの出力は以下の通りです:
- 誤ったジオメトリのみを含む入力レイヤーと同じタイプのレイヤー
- エラーの位置と情報（地物ID、パーツ、頂点番号など）を含むポイントレイヤー

修正プロセッシングアルゴリズムの出力は以下の通りです:
- 選択した方法に従って修正された地物を含む、入力レイヤーと同じタイプの修正済みレイヤー
- エラーの位置と修正に関するレポート（修正されたかどうか、および処理された地物についてのメッセージ）を含むポイントレイヤー

![](images/entries/f1b235d2feb5b4fe396603fc0f0bbc039f9321fd.png.webp)

この機能は QGIS (Grant OpenSource 2023) と Oslandia の資金提供で開発されました

This feature was developed by [Jacky Volpes](https://github.com/Djedouas)
### 機能: プロットへのタイトル、軸タイトル、対数軸の追加
プロセッシングツールの "プロット" セクションのプロッティングアルゴリズムに新しい機能が追加されました。

散布図、棒グラフ、箱ひげ図アルゴリズムで、プロットタイトルと軸タイトルをオプションパラメーターとして指定できるようになりました。軸タイトルが空の場合、デフォルトでフィールド名が軸タイトルとして使用されます。

半角スペースを1つ入力すると、軸タイトルは表示されません（現在の動作を復元）。

散布図でいずれかの軸に対数スケールを使用できるようになりました。

![](images/entries/5c84aa9c7e5fc0f4dcf6ba72b6f721a10380777a.webp)

この機能は [Florian Neukirchen](https://github.com/florianneukirchen) によって開発されました
### 機能: ラスターゾーン最小値/最大値アルゴリズム
ポリゴンゾーン内に含まれるピクセル値の最小値と最大値に対応するポイント地物を抽出する新しいアルゴリズムが追加されました。

出力はポリゴンレイヤーの各ゾーン地物に対して、ラスター値の最小値に対応する1つのポイント地物と最大値に対応する1つのポイント地物を含みます。

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能: ラスターから最小値/最大値ピクセルを抽出するアルゴリズム
入力ラスターレイヤーの指定したバンドから極値（最小値と最大値）を抽出する新しいアルゴリズムが追加されました。

出力は、関連するピクセルの中心に選択した極値のポイント地物を含むベクターレイヤーです。

ラスター内の複数のピクセルが最小値または最大値を共有する場合、そのうちの1つのピクセルのみが出力に含まれます。

このアルゴリズムはラスターイテレーターを使用して大規模ラスターでも効率的に動作し、ラスター全体をメモリに読み込む必要がありません。

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能: 標高プロファイル画像を生成する新しいアルゴリズム
ユーザーが標高プロファイル画像を生成できる新しいプロセッシングアルゴリズムが作成されました。これはモデル内で効果的に使用でき、複数の曲線の標高プロファイルを効率的に出力することができます。

![](images/entries/e1ed046394798d715f1f08a00bc0233668b860b9.webp)

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### 機能: 新しいメッシュ:サーフェスからポリゴンへのアルゴリズム
メッシュデータセットのサーフェスをマルチポリゴン出力にエクスポートする新しいプロセッシングアルゴリズムが追加されました。

![](images/entries/9c057e645861d7ac5f6e83128845095e60c9cf35.webp)

この機能は [Jan Caha](https://github.com/JanCaha) によって開発されました
## Profile Plots
### 機能: ベクターレイヤーへのカスタムトレランスの導入
 ユーザーはレイヤーの標高プロパティに  `カスタムトレランス`  プロパティを追加することでカスタムトレランスを定義できます。設定すると、標高プロファイルウィジェットで定義されたグローバルトレランスパラメーターよりも優先されます。

![](images/entries/235450d3d9a4e73de42c567c3fc7120b31b5185f.webp)

This feature was developed by [Jean Felder](https://github.com/ptitjano)
## データプロバイダ
### 機能: レイヤーコンテキストメニューからのSQLの実行
プロジェクトの目次からサポートされているレイヤーに対して直接SQLを実行できるようになりました。

![](images/entries/17dd1deefc986be713c4c6b007ed345dbde449d2.webp)

This feature was developed by [Jürgen Fischer](https://github.com/jef-n)
### 機能: Postgresラスタープロバイダー - ラスタースタイルのDB保存
このPRによりラスタースタイルをPostGISデータベースに保存できるようになります。

この機能開発は Ocean Winds. の資金提供を受けています

この機能は [Jan Caha](https://github.com/JanCaha) によって開発されました
### 機能: PostgreSQL/PostGISデータプロバイダー - ラスター概観の非表示
 ブラウザーからラスター概観テーブルを一覧表示しないオプションをPostGIS接続に追加します。ラスター概観テーブルの一覧はPostGISビューの raster_overviews から取得されます。

![](images/entries/401532722-4fab3810-07d9-453e-beb0-9efe1e397bfd.webp)

この機能開発は Ocean Winds. の資金提供を受けています

この機能は [Jan Caha](https://github.com/JanCaha) によって開発されました
## プラグイン
### DBマネージャーのテーブルコメントの複数行対応
DBマネージャーのテーブルコメントを複数行対応にします（元のQLineEditをQTextEditに変換）。また、"テーブルのプロパティ" ウィンドウを2回目に開いた際にコメントが正しく更新されない軽微なエラーも修正しています。

![](images/entries/395182951-bffa7117-bc19-41a6-952a-adc0ed6187ae.webp)

![](images/entries/395182959-9b082901-56a7-4465-ba46-d1c6c10b896a.webp)

この機能開発は Ocean Winds. の資金提供を受けています

この機能は [Jan Caha](https://github.com/JanCaha) によって開発されました
## プログラマビリティ
### 機能: QgsGeosクラスのPyQGISへの公開
基底の QgsGeometryEngine クラスでは公開されていないGEOS固有の機能に、新しい QgsGeos クラスを通じて直接アクセスできるようになりました。

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能: QgsGeometry.as_numpy() を通じたZおよびM値へのアクセスを可能に
以前のバージョンのQGISでは、QgsGeometry.as_numpy() メソッドはXY値のみの座標を返していました。

このリリースでは  `as_numpy` が変更され、Z値および/またはM値を持つジオメトリの座標がそれぞれxyz、xym、またはxyzmとして返されるようになりました。

この機能は [Till Frankenbach](https://github.com/merydian) によって開発されました
### 機能: Pythonコンソールのインタラクティブヘルプ
Pythonコンソール内でF1キーを押すと、QGISは対応するAPIページを自動的に開きます
- 選択テキストがある場合はそれを使用、なければ
- マウス位置の単語（設定で有効になっている場合、下記参照）、なければ
- テキストカーソル位置の単語

ドキュメントは、デバッグおよび開発ツールパネルに新しく追加されたドキュメントセクション内に表示されます。これにより開発者はアプリケーション内から現在のコードオブジェクトのAPIドキュメントに直接アクセスできるようになります。

開発者がワークフローに合わせてこの動作をより簡単に変更できるよう、追加のQGIS設定も追加されました。

![](images/entries/e5590d57719aa11a7cdefd0014fa56ea830c535c.png.webp)

This feature was developed by [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
## 注目すべき修正
### Feature: Bug fixes by Even Rouault (Spatialys)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.40バックポートコミット（GitHub） |
| --- | --- | --- | --- |
| Allow additional fields in Cloud Storage Connection credentials (or maybe gdal credentials more broadly) | [#60174](https://github.com/qgis/QGIS/issues/60174) | [GDAL PR 11699](https://github.com/OSGeo/gdal/pull/11699) | N/A |
| Add geometryColumnName() method for WFS and OAPIF providers | [#60055](https://github.com/qgis/QGIS/issues/60055) | [PR #60191](https://github.com/qgis/QGIS/pull/60191) | N/A |
| OAPIF: CQL layer filter expression is not used in request | [#60092](https://github.com/qgis/QGIS/issues/60092) | バグではない |  |
| Add support to export to/convert to .gpkg.zip files | [#59959](https://github.com/qgis/QGIS/issues/59959) | [PR #60202](https://github.com/qgis/QGIS/pull/60202) | N/A |
| WMS-T with Time Value YYYY | [#60264](https://github.com/qgis/QGIS/issues/60264) | [PR #60290](https://github.com/qgis/QGIS/pull/60290) | [PR #60307](https://github.com/qgis/QGIS/pull/60307) |
| GDAL Clip Raster by Layer Mask fails when given GeoPackage layer with diacritics (accents) in the name | [#59573](https://github.com/qgis/QGIS/issues/59573) | Superficial investigation |  |
| webconnections xml is invalid due to missing namespace prefix | [#60242](https://github.com/qgis/QGIS/issues/60242) | [PR #60293](https://github.com/qgis/QGIS/pull/60293) | [PR #60353](https://github.com/qgis/QGIS/pull/60353) |
| Unsupported Data Source' adding GDAL AWS S3 raster layers with credential options | [#60288](https://github.com/qgis/QGIS/issues/60288) | [GDAL Commit 4d2e65347ee0207328b14753ee2ea5628ced7d17](https://github.com/OSGeo/gdal/commit/4d2e65347ee0207328b14753ee2ea5628ced7d17) | N/A |
| Create shapefile layer: allow to create Bool fields | [#60324](https://github.com/qgis/QGIS/issues/60324) | [PR #60327](https://github.com/qgis/QGIS/pull/60327) | [PR #60332](https://github.com/qgis/QGIS/pull/60332) |
| [cleanup] Limit number of hardcoded strings for layer type by leveraging QgsMapLayerFactory::typeToString() | None | [PR #60360](https://github.com/qgis/QGIS/pull/60360) | N/A |
| Add Raster Layer: do not include credentials in layer name | [#60292](https://github.com/qgis/QGIS/issues/60292) | [PR #60380](https://github.com/qgis/QGIS/pull/60380) | [PR #60387](https://github.com/qgis/QGIS/pull/60387) |
| QgsMapLayer::publicSource(): make it redact/remove GDAL credentials | [#60292](https://github.com/qgis/QGIS/issues/60292) | [PR #60384](https://github.com/qgis/QGIS/pull/60384) | [PR #60400](https://github.com/qgis/QGIS/pull/60400) |
| QgsLayoutExporter: avoid to print the "ERROR 6: The PNG driver does not support update access to existing datasets." GDAL error message | [PR #60208](https://github.com/qgis/QGIS/pull/60208) | [GDAL PR 11708](https://github.com/OSGeo/gdal/pull/11708) | N/A |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Even Rouault (Spatialys)](https://www.spatialys.com/)
### Feature: Bug fixes by Alessandro Pasotti (QCooperative)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.40バックポートコミット（GitHub） |
| --- | --- | --- | --- |
| A semicolon after a custom SQL query makes QGIS generate a broken layer | [#56993](https://github.com/qgis/QGIS/issues/56993) | [PR #60209](https://github.com/qgis/QGIS/pull/60209) | [PR #60230](https://github.com/qgis/QGIS/pull/60230) |
| QGIS Server does not respect datum transformation | [#60216](https://github.com/qgis/QGIS/issues/60216) | [PR #60239](https://github.com/qgis/QGIS/pull/60239) | [PR #60302](https://github.com/qgis/QGIS/pull/60302) |
| [OGR] Fix transactional editing for GPKG/SQLite | [PR #60198](https://github.com/qgis/QGIS/pull/60198) | [PR #60198](https://github.com/qgis/QGIS/pull/60198) | No |
| QGIS Server: GetFeatureInfo default tolerance can be too small for line and point features | [#59818](https://github.com/qgis/QGIS/issues/59818) | [PR #60243](https://github.com/qgis/QGIS/pull/60243) | [PR #60259](https://github.com/qgis/QGIS/pull/60259) |
| Missing Update operation for WFS layers without geometry | [#60185](https://github.com/qgis/QGIS/issues/60185) | [PR #60266](https://github.com/qgis/QGIS/pull/60266) | [PR #60271](https://github.com/qgis/QGIS/pull/60271) |
| QGIS Server OGC: Ignoring "Use attribute form settings in GetFeatureInfo response" in GML output | [#59355](https://github.com/qgis/QGIS/issues/59355) | [PR #60281](https://github.com/qgis/QGIS/pull/60281) | No |
| First field in attribute table gets cleared on selection when Widget Type Date/Time is set | [#60223](https://github.com/qgis/QGIS/issues/60223) | 再現できません | No |
| Data Source Manager connects to all PostgreSQL connections on launch | [#60018](https://github.com/qgis/QGIS/issues/60018) | [PR #60319](https://github.com/qgis/QGIS/pull/60319) | [PR #60326](https://github.com/qgis/QGIS/pull/60326) |
| Virtual layer with JOIN on PostGIS layers not working anymore | [#60104](https://github.com/qgis/QGIS/issues/60104) | 再現できません | No |
| Enabling OpenCL acceleration generates erratic behavior in raster operations | [#60077](https://github.com/qgis/QGIS/issues/60077) | [PR #60339](https://github.com/qgis/QGIS/pull/60339) | [PR #60347](https://github.com/qgis/QGIS/pull/60347) |
| QGIS Server OGC: Display name is not provided in GetFeatureInfo json/gml response | [#59353](https://github.com/qgis/QGIS/issues/59353) | [PR #60343](https://github.com/qgis/QGIS/pull/60343) | No |
| Source Multipolygon-geometry reads as Polygon-geometry in MapInfo TAB format | [#60396](https://github.com/qgis/QGIS/issues/60396) | [PR #60410](https://github.com/qgis/QGIS/pull/60410) | No |
| Geometry checker accepts invalid polygon | [#60464](https://github.com/qgis/QGIS/issues/60464) | 再現できません | No |
| Labels with decimal values do not use Locale when decimal is used in a text expression | [#60440](https://github.com/qgis/QGIS/issues/60440) | Not sure this is a bug, open for discussion [PR #60479](https://github.com/qgis/QGIS/pull/60479) | No |
| New Connections to OGC Services Hang in Profiles with PostGIS Connections | [#60335](https://github.com/qgis/QGIS/issues/60335) | [PR #60495](https://github.com/qgis/QGIS/pull/60495) | TODO |
| [Regression] OGC-Features API requests do not send Authorization header in v3.40.3 | [#60473](https://github.com/qgis/QGIS/issues/60473) | [PR #60511](https://github.com/qgis/QGIS/pull/60511) | TODO |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Alessandro Pasotti (QCooperative)](https://www.qcooperative.net/)
### Feature: Bug fixes by Julien Cabieces (Oslandia)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.40バックポートコミット（GitHub） |
| --- | --- | --- | --- |
| Qt6: migration script forces Qt modules which are not covered by qgis.PyQt | [#59351](https://github.com/qgis/QGIS/issues/59351) | [PR #60280](https://github.com/qgis/QGIS/pull/60280) | [PR #60298](https://github.com/qgis/QGIS/pull/60298) |
| Unable to perform zip or export to PDF/image | [#59911](https://github.com/qgis/QGIS/issues/59911) | バグではない | N/A |
| QgisVectorLayerEditUtils addTopologicalPoints causes overlaps | [#58350](https://github.com/qgis/QGIS/issues/58350) | バグではない | N/A |
| QGIS should never poll a PostGIS/WMS/WFS/etc connections unless specifically asked to | [#58303](https://github.com/qgis/QGIS/issues/58303) | 再現できません | N/A |
| Masking labels doesn't work with rule-based labeling | [#46402](https://github.com/qgis/QGIS/issues/46402) | [PR #60325](https://github.com/qgis/QGIS/pull/60325) | [PR #60458](https://github.com/qgis/QGIS/pull/60458) |
| [Clang] Remove some deprecated warnings | 未報告 | [PR #60428](https://github.com/qgis/QGIS/pull/60428) | N/A |
| Label mask in Geopackage | [#59245](https://github.com/qgis/QGIS/issues/59245) | 再現できません | N/A |
| QMS plugin crashes in master | [#60286](https://github.com/qgis/QGIS/issues/60286) | [PR #60363](https://github.com/qgis/QGIS/pull/60363) | N/A |
| Sip deprecated annotation makes QGIS crash | Unreported SIP issue | [SIP PR #67](https://github.com/Python-SIP/sip/pull/67) | N/A |
| Masking labels doesn't work with rule-based labeling | [#46402](https://github.com/qgis/QGIS/issues/46402) | [PR #60490](https://github.com/qgis/QGIS/pull/60490) | [PR #60509](https://github.com/qgis/QGIS/pull/60509) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Julien Cabieces (Oslandia)](https://oslandia.com/en/)
### Feature: Bug fixes by Jacky Volpes (Oslandia)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.40バックポートコミット（GitHub） |
| --- | --- | --- | --- |
| Rule based symbology sorting with all fields in legend when only linked maps is ticked | [#60383](https://github.com/qgis/QGIS/issues/60383) | [PR #60536](https://github.com/qgis/QGIS/pull/60536) |  |
| Fix bad overlaps results with QgsRange objects and derivatives (int range, date range...) | 未報告 | [PR #60139](https://github.com/qgis/QGIS/pull/60139) | [PR #60532](https://github.com/qgis/QGIS/pull/60532) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

この機能は [Jacky Volpes (Oslandia)](https://oslandia.com/en/) によって開発されました
### Feature: Bug fixes by Nyall Dawson (North Road)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.40バックポートコミット（GitHub） |
| --- | --- | --- | --- |
| Fix leaks in layer definition loading code | 未報告 | [PR #60650](https://github.com/qgis/QGIS/pull/60650) | pending |
| Fix data-defined overrides ignored in legend text format | [#60628](https://github.com/qgis/QGIS/issues/60628) | [PR #60632](https://github.com/qgis/QGIS/pull/60632) | pending |
| Fix normalising constant in quartic kernel | [#60616](https://github.com/qgis/QGIS/issues/60616) | [PR #60631](https://github.com/qgis/QGIS/pull/60631) | [PR #60633](https://github.com/qgis/QGIS/pull/60633) |
| Fix incorrect compilation of "field IN (...) or field NOT IN (...)" | 未報告 | [PR #60630](https://github.com/qgis/QGIS/pull/60630) | N/A |
| Lots of memory leak fixes | 未報告 | [PR #60629](https://github.com/qgis/QGIS/pull/60629) | [PR #60651](https://github.com/qgis/QGIS/pull/60651) |
| [stac] Port more API to use unique_ptr | 未報告 | [PR #60627](https://github.com/qgis/QGIS/pull/60627) | N/A |
| Fix slow performance of raster image marker | [#51273](https://github.com/qgis/QGIS/issues/51273) | [PR #60604](https://github.com/qgis/QGIS/pull/60604) | too risky |
| Fix hang when project with large number of layers has joins to same layers | [#55026](https://github.com/qgis/QGIS/issues/55026) | [PR #60577](https://github.com/qgis/QGIS/pull/60577) | pending |
| Fix some app slowdown when many queries visible in network/db log panel | 未報告 | [PR #60576](https://github.com/qgis/QGIS/pull/60576) | [PR #60583](https://github.com/qgis/QGIS/pull/60583) |
| Fix render order of symbol layers for filled marker/filled line/arrow subsymbol | 未報告 | [PR #60575](https://github.com/qgis/QGIS/pull/60575) | [PR #60613](https://github.com/qgis/QGIS/pull/60613) |
| Diamond star marker shape is not closed | 未報告 | [PR #60574](https://github.com/qgis/QGIS/pull/60574) | [PR #60579](https://github.com/qgis/QGIS/pull/60579) |
| Fix artifacts when rendering filled line symbol | [#59689](https://github.com/qgis/QGIS/issues/59689) | [PR #60554](https://github.com/qgis/QGIS/pull/60554) | [PR #60578](https://github.com/qgis/QGIS/pull/60578) |
| Fix checkbox search widget wrapper for boolean field types | [#60152](https://github.com/qgis/QGIS/issues/60152) | [PR #60552](https://github.com/qgis/QGIS/pull/60552) | [PR #60558](https://github.com/qgis/QGIS/pull/60558) |
| [processing] Use matrix editor panel value if open | [#60442](https://github.com/qgis/QGIS/issues/60442) | [PR #60551](https://github.com/qgis/QGIS/pull/60551) | [PR #60556](https://github.com/qgis/QGIS/pull/60556) |
| [processing] Fix exception when algorithm has no output layers | 未報告 | [PR #60550](https://github.com/qgis/QGIS/pull/60550) | [PR #60560](https://github.com/qgis/QGIS/pull/60560) |
| Fix status bar coordinate display when project has no CRS | [#56954](https://github.com/qgis/QGIS/issues/56954) | [PR #60549](https://github.com/qgis/QGIS/pull/60549) | [PR #60561](https://github.com/qgis/QGIS/pull/60561) |
| Fixes for layers with a compound crs | [#55173](https://github.com/qgis/QGIS/issues/55173) | [PR #60548](https://github.com/qgis/QGIS/pull/60548) | [PR #60557](https://github.com/qgis/QGIS/pull/60557) |
| [oracle] Fix adding features with null attributes | 未報告 | [PR #60540](https://github.com/qgis/QGIS/pull/60540) | [PR #60566](https://github.com/qgis/QGIS/pull/60566) |
| [ams] Fix crash when layer ids are not sequential | [#60483](https://github.com/qgis/QGIS/issues/60483) | [PR #60520](https://github.com/qgis/QGIS/pull/60520) | [PR #60538](https://github.com/qgis/QGIS/pull/60538) |
| Fix pasting unsaved changes as temporary scratch layers | [#38913](https://github.com/qgis/QGIS/issues/38913) | [PR #60474](https://github.com/qgis/QGIS/pull/60474) | too risky |
| More descriptive expression parsing errors when a function is not found | 未報告 | [PR #60472](https://github.com/qgis/QGIS/pull/60472) | [PR #60475](https://github.com/qgis/QGIS/pull/60475) |
| Fix paint effects sometimes result in aliased rendering | 未報告 | [PR #60453](https://github.com/qgis/QGIS/pull/60453) | [PR #60468](https://github.com/qgis/QGIS/pull/60468) |
| More fixes for use of inline data for SVG content | [#60427](https://github.com/qgis/QGIS/issues/60427) | [PR #60448](https://github.com/qgis/QGIS/pull/60448) | [PR #60452](https://github.com/qgis/QGIS/pull/60452) |
| Fix potential crashes when layer tree insertion target group is deleted | 未報告 | [PR #60446](https://github.com/qgis/QGIS/pull/60446) | [PR #60449](https://github.com/qgis/QGIS/pull/60449) |
| When changing rect text annotation to fixed size mode, use current size | [#59189](https://github.com/qgis/QGIS/issues/59189) | [PR #60424](https://github.com/qgis/QGIS/pull/60424) | [PR #60451](https://github.com/qgis/QGIS/pull/60451) |
| Fix crash in text renderer when wrapping with one word + small rect | [#60256](https://github.com/qgis/QGIS/issues/60256) | [PR #60423](https://github.com/qgis/QGIS/pull/60423) | [PR #60450](https://github.com/qgis/QGIS/pull/60450) |
| [sensorthings] Offer MultiDatastreams as valid expansion targets | [#59531](https://github.com/qgis/QGIS/issues/59531) | [PR #60420](https://github.com/qgis/QGIS/pull/60420) | [PR #60426](https://github.com/qgis/QGIS/pull/60426) |
| [sensorthings] Fix provider does not work with oauth2 config method | [#60407](https://github.com/qgis/QGIS/issues/60407) | [PR #60419](https://github.com/qgis/QGIS/pull/60419) | [PR #60425](https://github.com/qgis/QGIS/pull/60425) |
| [sensorthings] only allow expansion removal from end of table | [#59532](https://github.com/qgis/QGIS/issues/59532) | [PR #60403](https://github.com/qgis/QGIS/pull/60403) | [PR #60405](https://github.com/qgis/QGIS/pull/60405) |
| [sensorthings] Remove option for basic authentication | [#59721](https://github.com/qgis/QGIS/issues/59721) | [PR #60376](https://github.com/qgis/QGIS/pull/60376) | [PR #60421](https://github.com/qgis/QGIS/pull/60421) |
| [sensorthings] Offer geometry for Datastream entities | [#59525](https://github.com/qgis/QGIS/issues/59525) | [PR #60375](https://github.com/qgis/QGIS/pull/60375) | too risky |
| [sensorthings] Hide proxy fields for interval fields in filter builder | [#59528](https://github.com/qgis/QGIS/issues/59528) | [PR #60374](https://github.com/qgis/QGIS/pull/60374) | [PR #60457](https://github.com/qgis/QGIS/pull/60457) |
| [sensorthings] Offer choices of non-polygon geometry types for multidatastreams | [#59719](https://github.com/qgis/QGIS/issues/59719) | [PR #60373](https://github.com/qgis/QGIS/pull/60373) | too risky |
| [sensorthings] Don't allow expansion back to base entity type | [#59722](https://github.com/qgis/QGIS/issues/59722) | [PR #60372](https://github.com/qgis/QGIS/pull/60372) | [PR #60398](https://github.com/qgis/QGIS/pull/60398) |
| When a layer changes from non-spatial to spatial, update canvas layers | [#59723](https://github.com/qgis/QGIS/issues/59723) | [PR #60371](https://github.com/qgis/QGIS/pull/60371) | too risky |
| Ensure that labeling solutions are deterministic | 未報告 | [PR #60369](https://github.com/qgis/QGIS/pull/60369) | [PR #60388](https://github.com/qgis/QGIS/pull/60388) |
| Remove an extraneous setting of layer scope for vectors | [#60112](https://github.com/qgis/QGIS/issues/60112) | [PR #60367](https://github.com/qgis/QGIS/pull/60367) | too risky |
| Use font button in annotation widgets instead of full text format widget | 未報告 | [PR #60354](https://github.com/qgis/QGIS/pull/60354) | [PR #60368](https://github.com/qgis/QGIS/pull/60368) |
| Fix incorrect annotation HTML shown when clicking between annotations | 未報告 | [PR #60333](https://github.com/qgis/QGIS/pull/60333) | [PR #60365](https://github.com/qgis/QGIS/pull/60365) |
| Delegate bounding box transformation to proj | [#59821](https://github.com/qgis/QGIS/issues/59821) | [PR #60331](https://github.com/qgis/QGIS/pull/60331) | [PR #60439](https://github.com/qgis/QGIS/pull/60439) |
| Fix logic in pdal indexing task relating to progress updates | 未報告 | [PR #60312](https://github.com/qgis/QGIS/pull/60312) | [PR #60315](https://github.com/qgis/QGIS/pull/60315) |
| Fix handling of multiple consecutive tabs with HTML text rendering | [#60098](https://github.com/qgis/QGIS/issues/60098) | [PR #60299](https://github.com/qgis/QGIS/pull/60299) | [PR #60422](https://github.com/qgis/QGIS/pull/60422) |
| Explicitly block initQgis, exitQgis from within application | [#60025](https://github.com/qgis/QGIS/issues/60025) | [PR #60297](https://github.com/qgis/QGIS/pull/60297) | too risky |
| Fix potential (unlikely) crash in concave hull algorithm | [#59778](https://github.com/qgis/QGIS/issues/59778) | [PR #60296](https://github.com/qgis/QGIS/pull/60296) |  |
| Catch transform errors in QgsWFSProvider::getCapabilities | [#60622](https://github.com/qgis/QGIS/issues/60622) | [PR #60653](https://github.com/qgis/QGIS/pull/60653) | pending |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: Bug fixes by Alexander Bruy (QCooperative)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.40バックポートコミット（GitHub） |
| --- | --- | --- | --- |
| Zonal histogram unusable results if input raster has many decimal places | [#30822](https://github.com/qgis/QGIS/issues/30822) | [PR#60212](https://github.com/qgis/QGIS/pull/60212) | [PR#60234](https://github.com/qgis/QGIS/pull/60234) |
| PyQGIS / Processing: QgsProcessingParameterMapLayer doesn't respect QgsProcessing.TypeVector | [#56344](https://github.com/qgis/QGIS/issues/56344) | [PR#60213](https://github.com/qgis/QGIS/pull/60213) | [PR#60305](https://github.com/qgis/QGIS/pull/60305) |
| "Layer name" is actually layer title | [#28857](https://github.com/qgis/QGIS/issues/28857) | [PR#60215](https://github.com/qgis/QGIS/pull/60215) | いいえ |
| WMS layers added with the browser panel ignore image format preferences and default to PNG | [#57666](https://github.com/qgis/QGIS/issues/57666) | [PR#60221](https://github.com/qgis/QGIS/pull/60221) | [PR#60309](https://github.com/qgis/QGIS/pull/60309) |
| There seems to be an issue with the way the algorithm for merging pointclouds works in the model builder | [#57550](https://github.com/qgis/QGIS/issues/57550) | [PR#60236](https://github.com/qgis/QGIS/pull/60236) | [PR#60304](https://github.com/qgis/QGIS/pull/60304) |
| TypeError: unsupported operand type(s) for +: 'Modifier' and 'Key' | [#60063](https://github.com/qgis/QGIS/issues/60063) | [PR#60289](https://github.com/qgis/QGIS/pull/60289) | [PR#60294](https://github.com/qgis/QGIS/pull/60294) |
| "TIN interpolation" and "IDW interpolation" algs always output an ASCII grid (AAIGrid) raster regardless of the output file extension | [#56653](https://github.com/qgis/QGIS/issues/56653) | [PR#60320](https://github.com/qgis/QGIS/pull/60320) | [PR#60351](https://github.com/qgis/QGIS/pull/60351) |
| When editing a Scene connection a new Scene connection is created instead | [#57570](https://github.com/qgis/QGIS/issues/57570) | [PR#60321](https://github.com/qgis/QGIS/pull/60321) | [PR#60329](https://github.com/qgis/QGIS/pull/60329) |
| Spatialite execute SQL issues | [#53904](https://github.com/qgis/QGIS/issues/53904) | [PR#60337](https://github.com/qgis/QGIS/pull/60337) | [PR#60348](https://github.com/qgis/QGIS/pull/60348) |
| Selected sub-item of Join doesn't count for editing | [#29709](https://github.com/qgis/QGIS/issues/29709) | [PR#60338](https://github.com/qgis/QGIS/pull/60338) | [PR#60356](https://github.com/qgis/QGIS/pull/60356) |
| Export Layer(s) Information processing tool suggests unsupported Annotations layer as input | [#49010](https://github.com/qgis/QGIS/issues/49010) | [PR#60341](https://github.com/qgis/QGIS/pull/60341) | [PR#60460](https://github.com/qgis/QGIS/pull/60460) |
| Add BIGTIFF writing option to the georeferencer | [#47362](https://github.com/qgis/QGIS/issues/47362) | [PR#60344](https://github.com/qgis/QGIS/pull/60344) | いいえ |
| Raster resampling settings are not applied when importing a style | [#56771](https://github.com/qgis/QGIS/issues/56771) | [PR#60358](https://github.com/qgis/QGIS/pull/60358) | [PR#60377](https://github.com/qgis/QGIS/pull/60377) |
| Switching back to Box style scale bar after having switched to Hollow does not reset the fill brush | [#37413](https://github.com/qgis/QGIS/issues/37413) | [PR#60430](https://github.com/qgis/QGIS/pull/60430) | [PR#60471](https://github.com/qgis/QGIS/pull/60471) |
| Failure when writing to vector file: Path to corresponding vector file is not shown | [#49567](https://github.com/qgis/QGIS/issues/49567) | [PR#60433](https://github.com/qgis/QGIS/pull/60433) | [PR#60444](https://github.com/qgis/QGIS/pull/60444) |
| WFS GetFeature request is not using project CRS despite it is offered by WFS | [#44325](https://github.com/qgis/QGIS/issues/44325) | [PR#60476](https://github.com/qgis/QGIS/pull/60476) | [PR#60505](https://github.com/qgis/QGIS/pull/60505) |
| Fix missed import and incorrect call to getThemeIcon() | 未報告 | [PR#60480](https://github.com/qgis/QGIS/pull/60480) | [PR#60484](https://github.com/qgis/QGIS/pull/60484) |
| "CRS" variable does not work in Processing/expression calculator when defining an output name in batch mode | [#58313](https://github.com/qgis/QGIS/issues/58313) | [PR#60485](https://github.com/qgis/QGIS/pull/60485) | いいえ |
| [WMS] Not possible to "Ignore reported layer extents" | [#60496](https://github.com/qgis/QGIS/issues/60496) | [PR#60513](https://github.com/qgis/QGIS/pull/60513) | [PR#60529](https://github.com/qgis/QGIS/pull/60529) |
| Alias not exported with algorithm Export to spreadsheet with Value Relation widget | [#59403](https://github.com/qgis/QGIS/issues/59403) | [PR#60542](https://github.com/qgis/QGIS/pull/60542) | [PR#60544](https://github.com/qgis/QGIS/pull/60544) |
| Create "Constant Raster" image size is different compared to "Rasterize" | [#43547](https://github.com/qgis/QGIS/issues/43547) | [PR#60587](https://github.com/qgis/QGIS/pull/60587) | [PR#60608](https://github.com/qgis/QGIS/pull/60608) |
| [browser] "edit" multiple connections at once? | [#31928](https://github.com/qgis/QGIS/issues/31928) | [PR#60639](https://github.com/qgis/QGIS/pull/60639) | [PR#60648](https://github.com/qgis/QGIS/pull/60648) |
| Remove ALL references to plugin | [#56808](https://github.com/qgis/QGIS/issues/56808) | バグではない |  |
| native:savefeatures unable to specify output layer | [#56517](https://github.com/qgis/QGIS/issues/56517) | 再現できません |  |
| Processing Raster Calculator not working in Processing Graphical Modeler | [#37831](https://github.com/qgis/QGIS/issues/37831) | Cannot reproduce, fixed in the native algorithm |  |
| [processing] Raster calculator in embedded model can't refer to embedded model input | [#42825](https://github.com/qgis/QGIS/issues/42825) | Cannot reproduce, fixed in the native algorithm |  |
| Raster calculator in graphical modeler reversing layer definitions every time the program is opened | [#33338](https://github.com/qgis/QGIS/issues/33338) | Cannot reproduce, fixed in the native algorithm |  |
| Modeler and Raster Calculator fail to calc | [#32753](https://github.com/qgis/QGIS/issues/32753) | Cannot reproduce, fixed in the native algorithm |  |
| Hillshade not created when Save File As is used | [#57247](https://github.com/qgis/QGIS/issues/57247) | バグではない |  |
| Customization: Tools selected with the widget catcher are kept selected even if the dialog is cancelled | [#23199](https://github.com/qgis/QGIS/issues/23199) | [PR#60643](https://github.com/qgis/QGIS/pull/60643) | [PR#60678](https://github.com/qgis/QGIS/pull/60678) |
| Disable default actions for non-spatial tables | [#57916](https://github.com/qgis/QGIS/issues/57916) | [PR#60657](https://github.com/qgis/QGIS/pull/60657) | [PR#60670](https://github.com/qgis/QGIS/pull/60670) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Alexander Bruy (QCooperative)](https://www.qcooperative.net/)
### Feature: Bug fixes by Mathieu Pellerin (OPENGIS)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.40バックポートコミット（GitHub） |
| --- | --- | --- | --- |
| Algorithm postprocessing regression failing to add all but one output to the project | 未報告 | [PR #60624](https://github.com/qgis/QGIS/pull/60624) | [PR #60626](https://github.com/qgis/QGIS/pull/60626) |
| Expression's `$id` value can overflow due to wrong int casting | 未報告 | [PR #60521](https://github.com/qgis/QGIS/pull/60521) | - |
| Symbol selector dialog not passing on its context to its widget | [#58985](https://github.com/qgis/QGIS/issues/58985) | [PR #60482](https://github.com/qgis/QGIS/pull/60482) | [PR #60667](https://github.com/qgis/QGIS/pull/60667) |
| Missing `cluster_size` variable in expression constructor dialog for cluster symbol | [#58985](https://github.com/qgis/QGIS/issues/58985) | [#58985](https://github.com/qgis/QGIS/issues/58985) | [Commit 068e27c](https://github.com/qgis/QGIS/commit/068e27c0d30babc6582e2db511cd848ec6f0095c) |
| Annotation fixed-size units not set correctly in UI | [#59188](https://github.com/qgis/QGIS/issues/59188) | [PR #60392](https://github.com/qgis/QGIS/pull/60392) | [PR #60397](https://github.com/qgis/QGIS/pull/60397) |
| MBtiles Won't Load Zooms Higher Than 14 | [#59309](https://github.com/qgis/QGIS/issues/59309) | [PR #60391](https://github.com/qgis/QGIS/pull/60391) | [PR #60395](https://github.com/qgis/QGIS/pull/60395) |
| Docked Georeferencer does not reopen if closed | [#60382](https://github.com/qgis/QGIS/issues/60382) | [PR #60390](https://github.com/qgis/QGIS/pull/60390) | [PR #60401](https://github.com/qgis/QGIS/pull/60401) |
| Unable to reorder subdiagrams in stacked diagrams dialog | [#59505](https://github.com/qgis/QGIS/issues/59505) | [PR #60278](https://github.com/qgis/QGIS/pull/60278) | [PR #60519](https://github.com/qgis/QGIS/pull/60519) |
| Unable to save after error in Geometry Validation | [#59688](https://github.com/qgis/QGIS/issues/59688) | [PR #60263](https://github.com/qgis/QGIS/pull/60263) | [PR #60303](https://github.com/qgis/QGIS/pull/60303) |
| Barely visible icon within Python editor in grey theme | [#59772](https://github.com/qgis/QGIS/issues/59772) | [PR #60261](https://github.com/qgis/QGIS/pull/60261) | [PR #60352](https://github.com/qgis/QGIS/pull/60352) |
| Help->About window displays not up-to-date active Python plugins list after activating/deactivating or installing/uninstalling plugins | [#59779](https://github.com/qgis/QGIS/issues/59779) | [PR #60257](https://github.com/qgis/QGIS/pull/60257) | [PR #60270](https://github.com/qgis/QGIS/pull/60270) |
| QGIS' handling of network requests' redirects is broken under Qt6 | [#60235](https://github.com/qgis/QGIS/issues/60235) | [PR #60238](https://github.com/qgis/QGIS/pull/60238) | [PR #60269](https://github.com/qgis/QGIS/pull/60269) |
| Data loss for new rows if a column added after row in attribute table | [#59783](https://github.com/qgis/QGIS/issues/59783) | [PR #60226](https://github.com/qgis/QGIS/pull/60226) | [PR #60310](https://github.com/qgis/QGIS/pull/60310) |
| Non-HTML-formatted annotations have their text deleted every time a setting changes | [#59804](https://github.com/qgis/QGIS/issues/59804) | [PR #60222](https://github.com/qgis/QGIS/pull/60222) | [PR #60334](https://github.com/qgis/QGIS/pull/60334) |
| `outputCrs` is an unknown keyword argument in QgsRasterCalculator | [#59890](https://github.com/qgis/QGIS/issues/59890) | [PR #60218](https://github.com/qgis/QGIS/pull/60218) | - |
| Invalid CRS after writing in QgsRasterCalculator | [#59898](https://github.com/qgis/QGIS/issues/59898) | [PR #60214](https://github.com/qgis/QGIS/pull/60214) | [PR #60253](https://github.com/qgis/QGIS/pull/60253) |
| Data-defined expression for labels "tab distance" doesn't seem to work | [#60004](https://github.com/qgis/QGIS/issues/60004) | [PR #60211](https://github.com/qgis/QGIS/pull/60211) | 必要なし |
| QGIS crashes due to erroneous extent / invalid CRS in XYZ creation algorithms | [#60069](https://github.com/qgis/QGIS/issues/60069) | [PR #60199](https://github.com/qgis/QGIS/pull/60199) | [PR #60220](https://github.com/qgis/QGIS/pull/60220) |
| The "Selected features only" checkbox is incorrectly disabled / enabled although the layer has / has not selected features | [#60108](https://github.com/qgis/QGIS/issues/60108) | [PR #60197](https://github.com/qgis/QGIS/pull/60197) | [PR #60306](https://github.com/qgis/QGIS/pull/60306) |
| Modeler - Feature iteration does not work | [#60131](https://github.com/qgis/QGIS/issues/60131) | [PR #60194](https://github.com/qgis/QGIS/pull/60194) | [PR #60300](https://github.com/qgis/QGIS/pull/60300) |
| Changes on form are not applied by default | [#60181](https://github.com/qgis/QGIS/issues/60181) | [PR #60192](https://github.com/qgis/QGIS/pull/60192) | [PR #60591](https://github.com/qgis/QGIS/pull/60591) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Mathieu Pellerin (OPENGIS)](https://opengis.ch/)
### Feature: Bug fixes by Stefanos Natsis (LutraConsulting)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.40バックポートコミット（GitHub） |
| --- | --- | --- | --- |
| PointCloud - Converting LAZ to COPC.LAZ: CRS information is lost in COPC.LAZ file | [#59662](https://github.com/qgis/QGIS/issues/59662) | [hobuinc/untwine PR #189](https://github.com/hobuinc/untwine/pull/189) | - |
| Losing the CRS in .copc.laz created from .laz using drag and drop | [#57983](https://github.com/qgis/QGIS/issues/57983) | [hobuinc/untwine PR #189](https://github.com/hobuinc/untwine/pull/189) | - |
| Untwine fails if path contains Swedish characters | [#57913](https://github.com/qgis/QGIS/issues/57913) | [hobuinc/untwine PR #191](https://github.com/hobuinc/untwine/pull/191) | - |
| After loading a Mesh in current master, the Layer styling panel is unusable | [#60083](https://github.com/qgis/QGIS/issues/60083) | 修正済み | - |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Stefanos Natsis (LutraConsulting)](https://www.lutraconsulting.co.uk/)
### Feature: Bug Fixes by Loïc Bartoletti (Oslandia)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.40バックポートコミット（GitHub） |
| --- | --- | --- | --- |
| Add a CMAKE option to completely disable Python | security@ | [PR #60463](https://github.com/qgis/QGIS/pull/60463) | - |
| Allow snapping point with different CRS | [#59792](https://github.com/qgis/QGIS/issues/59792) | [PR #60456](https://github.com/qgis/QGIS/pull/60456) | [PR #60478](https://github.com/qgis/QGIS/pull/60478) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Loïc Bartoletti (Oslandia)](https://oslandia.com/en/)
### Feature: Bug Fixes by Germán Carrillo (OPENGIS)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.40バックポートコミット（GitHub） |
| --- | --- | --- | --- |
| Drag and drop of symbology classes is buggy <br> Cannot move legend items when classifying <br> Drag and drop in Point cloud classification is confusing | [#50823](https://github.com/qgis/QGIS/issues/50823) <br> [#55267](https://github.com/qgis/QGIS/issues/55267) <br> [#60559](https://github.com/qgis/QGIS/issues/60559) | [PR #60546](https://github.com/qgis/QGIS/pull/60546) | [PR #60750](https://github.com/qgis/QGIS/pull/60750) |
| (Still) Unable to reorder subdiagrams in stacked diagrams dialog | [#60596](https://github.com/qgis/QGIS/issues/60596) | [PR #60600](https://github.com/qgis/QGIS/pull/60600) | [PR #61126](https://github.com/qgis/QGIS/pull/61126) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

この機能は [Germán Carrillo (OPENGIS)](https://opengis.ch/) によって開発されました

{{<content-end >}}
