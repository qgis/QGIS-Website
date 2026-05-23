---
HasBanner: false
draft: false
releaseDate: '2025-06-20'
section: project
sidebar: true
title: QGIS 3.44の変更履歴
type: visual-changelog

---
{{<content-start >}}
# QGIS 3.44の変更履歴{#changelog344 }
<img src="images/projects/3807b5d1851cc87bda040f637e1f4024bc11c58a.png" class="img-responsive img-rounded center-block" />

Release date: 2025-06-20

 QGISプロジェクトは、QGIS 3シリーズの集大成となる記念すべきリリース、QGIS 3.44を誇りを持って発表します。このリリースは、世界中のユーザーを支える活気あふれる拡大し続けるフリー＆オープンソースの地理空間ツール、ライブラリ、コミュニティサポートのエコシステムの中で登場します。過去のリリースの堅固な基盤の上に構築されたQGIS 3.44は、2025年10月に予定されている [QGIS 4.0](https://blog.qgis.org/2025/04/17/qgis-is-moving-to-qt6-and-launching-qgis-4-0/) のリリースに向けてプロジェクトが最新のQt6フレームワークへ移行する中、すべてのユーザーに安定した洗練された体験を提供します。

QGIS 3.xブランチの最後の機能リリースとして、このバージョンは既存のワークフローに信頼性の高い環境を提供します。QGIS 4.0では互換性対応の労力を最小化しエコシステムがコアアプリケーションとともに発展できるよう非推奨APIが維持されるため、プラグイン開発者はリリース間のスムーズな移行を期待できます。

安定性と洗練に重点を置きながらも、このリリースにはワークフローを改善し地理空間作業におけるユーザーの能力を高める注目すべき機能強化が多数含まれています。データベース管理と接続性の改善、データプロバイダーの柔軟性の向上、新しいプロジェクト設定などがその例として挙げられます。プロセッシングツールボックスやQGIS式などの長年親しまれてきた機能も充実した改善が加えられており、新しいラベリングとレイアウトの更新によりカートグラフィー機能も強化されています。

 導入されたすべての新機能を手早く確認するには、 [highlight reel video on YouTube](https://www.youtube.com/watch?v=5a02yaDKAiE) をご覧ください。

[![](https://img.youtube.com/vi/5a02yaDKAiE/0.jpg)](https://www.youtube.com/watch?v=5a02yaDKAiE)

QGISはコミュニティによる取り組みです。このリリースを実現するために時間と労力をボランティアで提供してくださった（または資金援助をしてくださった）開発者・ドキュメント作成者・テスター・その他多くの方々に心より感謝申し上げます。QGISコミュニティより、このリリースをお楽しみいただければ幸いです！QGISをさらに素晴らしいものにするために、時間・資金・その他の形でご貢献いただける方は、ぜひ [QGIS.ORG](https://qgis.org) をご覧いただき、お力をお貸しください！

QGIS is supported by donors and sustaining members. A current list of donors who have made financial contributions large or small to the project can be seen on our [list of donors](https://qgis.org/en/site/about/sustaining_members.html#list-of-donors). If you would like to become an official project sustaining member, please visit our [sustaining member page](https://qgis.org/en/site/about/sustaining_members.html) for more details. Sponsoring QGIS helps us to fund our regular developer meetings, maintain project infrastructure, and fund bug-fixing efforts. A complete list of current sponsors is provided below - our very big thank you to all of our sponsors!

QGIS はフリーのソフトウェアです。利用する上で金銭を支払う義務はありません。実際、私たちは利用者の財政状況や社会的地位にかかわらず、より多くの人に QGIS を利用して欲しいと思っています。私たちは地理空間的な意思決定ツールによって人々が力を持つことが、全人類の社会をより良くすると信じています。
## 時系列
### 機能: WMS-Tグループノードでの時間ディメンションの公開を可能に
WMS-Tレイヤーに、レイヤーツリーグループノードで時間ディメンションを公開できるようにする新しいオプションが追加されました。

WMSグループプロパティのチェックボックスにより、この時間ディメンションの計算をオン/オフできます。有効にすると、子レイヤーの時間ディメンションに基づいて時間ディメンションが再帰的に生成されます。

時間ディメンションの計算が無効になっているグループは、子レイヤーの時間ディメンションを親に伝播しません。

OGC WMSおよびISO8601標準に準拠した時間ディメンションの日付範囲も追加されました。

<img src="images/entries/4916ef1bc94c95cbcb5b66d83e4c4093fe411693" class="img-responsive img-rounded" />

この機能は Ifremer によって資金提供されました

This feature was developed by [Julien Cabieces](https://github.com/troopa81)
### 機能: ラスター時間モードへの固定日付/時刻の追加
ラスターレイヤーの時間プロパティで固定日付/時刻を選択できるようになり、単一の入力値から時間範囲の開始と終了を推定できるようになりました。

<img src="images/entries/d61699232fef2797a38e3fcbe18c65d889896308" class="img-responsive img-rounded" />

この機能は Ifremer によって資金提供されました

This feature was developed by [Julien Cabieces](https://github.com/troopa81)
## ユーザーインタフェース
### 機能:メッセージログパネルで特定のタブを開く
QGISのメッセージログパネルで特定のタブにメッセージを開けるようになりました。

これにより、例えば特定のプロバイダーやプラグイン向けのタブを直接開くことができます。

これは `openMessageLog` メソッドをタブ名をパラメーターとして受け付けるよう拡張することで実現されています。指定されたタブ名が見つからない場合、パネルは既存の状態で表示されます。

この変更にはifaceメソッド `iface.openMessageLog( tab_name )` の拡張も含まれています。

この機能は [City of Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html) の資金提供で開発されました

This feature was developed by [Germán Carrillo](https://github.com/gacarrillor)
## シンボロジ
### 機能: カテゴリ分類シンボルレンダラーウィジェットへの未使用カテゴリの削除オプションの追加
カテゴリ分類シンボルウィジェットに、ユーザーが未使用のカテゴリを一括削除できる新しいオプションが追加されました。

このオプションを使用すると、レイヤーのカテゴリ分類に使用している属性フィールドまたは式に一致しないカテゴリが自動的に特定・削除されます。

これは多数のカテゴリスタイルを引き継いだデータのクリップされたサブセットを使用する場合に特に役立ちます。

<img src="images/entries/85eb6c595a8e44e2fd6deb1586215bc523861dfd.png" class="img-responsive img-rounded" />

This feature was developed by [Ben Wirf](https://github.com/benwirf)
## ラベリング
### 機能: ラベル周囲の余白制御と重複ラベル防止の設定の追加
ベクターレイヤーのラベルに2つの新しい設定が導入されました:
- ラベル周囲の余白:レイヤーのラベル周囲に余白を設定できます。これにより、他のすべてのラベルがこの余白距離より近くに配置されることを防ぎます。
- 重複ラベルの防止:大文字と小文字を区別したマッチングを使用して、すべてのレイヤーにわたる最小距離内の重複するラベルを削除します。

これは、道路ネットワークデータなどの複雑な地理的状況のレンダリングでラベルの見栄えを向上させるために使用できます。片側2車線道路、側道、その他の要素により、同一のラベル要素が近接して多数表示されることがあります。

<img src="images/entries/efc5a69fe9fa346ba7b2d6b9c3ec2b6d57b731d0.png" class="img-responsive img-rounded" />

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## 三次元機能
### 機能: 断面図ツール
3Dシーンで断面図を作成する新しいツールが追加されました。ユーザーは2Dマップキャンバスで3点（始点、終点、断面図の厚さ）をクリックして対象領域を選択でき、3Dビューでは領域外のすべてが非表示になります。3DビューのカメラもROI（対象領域）を横から見る位置に移動します。

3Dビューの範囲設定と比較して、断面図ツールは動作が速く（断面図の有効/無効切り替え時にシーン全体の再読み込みが不要）、また回転した矩形領域にも対応しています。

<img src="images/entries/8034dbe7d55e297f052ef4d310beab10a56ddbb5.png" class="img-responsive img-rounded" />

この機能は Septima, Klimadatastyrelsen からの資金提供で開発されました

This feature was developed by [Matej Bagar](https://github.com/Withalion)
### 機能: 地球儀ビュー
投影座標系ベースの従来の3Dビューに加えて、3Dシーンに新しいモード　- 地球儀ビュー- が追加されました。

あらゆる種類のマップレイヤーを地球儀の2Dテクスチャとして使用でき、タイル化シーンレイヤーとポイントクラウドレイヤーの3Dレンダラーもサポートされています。

地球儀ビューはプロジェクトの楕円体を使用して地球儀メッシュを生成します。プロジェクトのCRSを適切に設定することで、火星や月などの他の天体も表示することができます。

詳細情報:
- [QEP \#301 - Large scenes and globe in QGIS 3D](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/301)
- [Cesium blog post](https://cesium.com/blog/2025/06/20/3d-globe-view-now-available-in-qgis/)

<img src="images/entries/b0ebe685540c3191ad07235d63e45176e9694551.png" class="img-responsive img-rounded" />

この機能は Cesium Ecosystem Grant の資金提供で開発されました

本機能は Lutra Consulting & North Road によって開発されました
### 機能: 大規模3Dシーンのサポート
 以前のバージョンのQGISでは、数値精度の問題により、50〜100キロメートルを超えるシーンで3Dマップビューが正しく動作しませんでした。カメラが不規則に動いたり（使用不能になるほど）、ズームイン時に地物がちらついたりしていました。 [QEP 301](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/301) に概説されているように、ローカルシーンと地球儀シーンの両方でこの問題が修正されました。

この機能は Cesium Ecosystem Grant の資金提供で開発されました

本機能は Lutra Consulting & North Road によって開発されました
## 点群
### 機能: pdal_wrenchをv1.2に更新
これにより以下が提供されます:
- プロセッシングアルゴリズムにおける仮想ポイントクラウド（VPC）サポートの改善
- さまざまな形式からCloud Optimized Point Cloud（COPC）への直接出力が可能に

その他の改善点の詳細については [pdal_wrench changelog](https://github.com/PDAL/wrench/releases/tag/v1.2) を参照してください。

この機能は Landesamt für Vermessung und Geoinformation Vorarlberg によって資金提供されました

This feature was developed by [Jan Caha](https://github.com/JanCaha)
### 機能: PDALアルゴリズムでのCOPC出力を可能に
アップグレードされたpdal_wrench依存関係を活用することで、PDALアルゴリズムの出力をCloud Optimized Point Cloudとして生成できるようになりました。

この機能は Landesamt für Vermessung und Geoinformation Vorarlberg によって資金提供されました

This feature was developed by [Jan Caha](https://github.com/JanCaha)
### 機能: プロセッシングツールでのCOPCインデックスファイルの自動活用
COPCファイルにインデックスが利用可能な場合、QGISはプロセッシング操作時にデフォルトで自動的にそれを活用するようになりました。これにより一部の操作（クリップなど）が高速化されます。

この機能は Landesamt für Vermessung und Geoinformation Vorarlberg によって資金提供されました

This feature was developed by [Jan Caha](https://github.com/JanCaha)
### 機能: ポイントクラウドの編集機能
3Dマップビューでポイントクラウドレイヤーを編集できるようになりました。ユーザーは変更する属性とターゲット値を選択し、変更するポイントをインタラクティブに選択できます。

編集するポイントを選択するためのマップツールが複数あります:
- ポリゴンによる選択
- ブラシによる選択
- 上方/下方 ラインによる選択

ユーザーはQGIS式を使用して編集ポイントのフィルタリングを設定できるため、一部のポイントのみ属性値を変更することができます。

<div class="col-lg-8 col-md-offset-1">

<div class="iframe">

<div id="player">

</div>

<div class="player-unavailable">

# An error has occurred.{#changelog344 }
<div class="submessage">

<a href="https://www.youtube.com/watch?v=TRxW-g0HYjU" target="_blank"> video on www.youtube.com を参照して下さい</a> あなたのブラウザーで利用できない場合は　JavaScriptを有効にしてください。

</div>

</div>

</div>

</div>

この機能は Septima, Klimadatastyrelsen からの資金提供で開発されました

この機能は Lutra Consulting によって開発されました
## 印刷レイアウト
### 機能: レイアウト凡例への自動折り返し設定の追加
自動折り返し設定により、凡例テキストを固定の行の長さ（ミリメートル単位で設定）で自動的に折り返すことができます。

これにより、自動生成された凡例が過度に横長になることを防ぐことができます。

<img src="images/entries/ec81517776eea3e38142ca38436789fbdb9e7f9a.png" class="img-responsive img-rounded" />

この機能は North Road, thanks to SLYR によって資金提供されました

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## 計算式
### 機能: 文字列用のrepeat関数とreverseバリアントの追加
新しい式には以下が含まれます:
- 新しい  'repeat'  関数で文字列を指定した回数繰り返すことができます
-  'reverse' 文字列バリアントで文字列を逆順にできます

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能: 文字列定義からCRSを作成し、CRSからauthidを取得するための式関数
座標参照系の管理をサポートする新しい式関数が追加されました:
- **crs_from_text**: 文字列定義から座標参照系を作成します。文字列定義は `auth:id` 形式のCRSコード、WKT定義、またはCRSのPROJ文字列定義で表すことができます。
- **crs_to_authid**: 座標参照系の識別子文字列を `authority:id` 形式（例：EPSG:4326）で返します。

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
## デジタイズ
### 機能: マージポリシーの追加
既存の分割および複製の "ポリシー" と同様に、QGISで地物の結合ダイアログの初期値を決定するように設定できるマージポリシーがサポートされるようになりました。

ポリシーはレイヤープロパティダイアログの属性フォームで、フィールド設定の "ポリシー" セクションにてフィールドごとに設定できます。

ポリシーメソッドには以下のものがあります:
- 合計を使う: (数値フィールドのみ) 値の合計
- ジオメトリ加重平均を使う: (数値フィールドのみ) ジオメトリの加重平均を使う
- デフォルト値を使う:  QGISで設定されているデフォルト値を使う
- 値を削除: フィールドをクリアし、データプロバイダーのデフォルト値（存在する場合）を使用します。値が指定されていない場合は、最初の地物の値が使用されます（現在のデフォルト）
- 最大地物の価を使う: 最大のジオメトリを持つ地物（ラインタイプは長さ、ポリゴンタイプは面積、マルチポイントタイプはパーツ数で判定）の値を使用します。
- 最小値を使う: (数値フィールドのみ) 最小値
- 最大値を使う: (数値フィールドのみ) 最大値
- NULLに設定: 地物のフィールド値をNULLに設定します。

<img src="images/entries/544229ddb1a9eb37b3deacd955241731f8aa4c59.png" class="img-responsive img-rounded" />

This feature was funded by the National Land Survey of Finland.

This feature was developed by [Juho Ervasti](https://github.com/JuhoErvasti)
## データ管理
### 機能: RPCが利用可能な場合のHEIGHT_AVERAGEの使用
QGISが衛星画像（特にDIMAP / Pleiades NEO製品）をより正確に位置合わせできるようになりました。

この改善により、追加の標高データがない場合でも、これらの種類の衛星画像がより高い精度で正確な地理的位置に表示されるようになります。

<img src="images/entries/6dac68ebcbe251181b8b878ca25e96bee1bf2b33" class="img-responsive img-rounded" />

This feature was developed by [Even Rouault](https://github.com/rouault)
### 機能: DBテーブルのインポート時のフィールドカスタマイズを可能に
データベーステーブルのインポートダイアログに新しいフィールドマッピングセクションが追加され、作成されるテーブルのフィールドをユーザーが制御できるようになりました。

ユーザーは各出力フィールドの名前変更、正確な出力先フィールドタイプの設定、およびソース式の調整が可能です。

フィールドをインポートから除外したり、ソーステーブルに存在しない新しいフィールドを作成したりすることもできます。

<img src="images/entries/100dca954811ba2396b0fa2fa7edbbaec32dadb0" class="img-responsive img-rounded" />

この機能は City of Canning によって資金提供されました

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能: データベースへのテーブルインポート時のオプションの範囲・式ベースのフィルターの追加
ブラウザーからデータベースにテーブルをインポートする際、コピーされるレコードを範囲または式でフィルタリングするオプションが追加されました。

<img src="images/entries/ac84f4eff2203d0b08b4577eeafa37cff09a6db1" class="img-responsive img-rounded" />

この機能は City of Canning によって資金提供されました

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能: SQL実行ウィンドウへのストアドクエリサポートの追加
 "Execute SQL" ダイアログがストアドクエリをサポートするようになりました。新しいブラウザーツールでDBマネージャーと同等の機能が利用できます。

新しいツールバーアクションから、ストアドクエリを現在のクエリに挿入したり、新しいストアドクエリを保存したり、クエリを削除したりできます。

クエリは現在のプロジェクトまたはローカルのユーザープロファイルに保存できます。

<img src="images/entries/b4d094f69e11aee5f1e2de7ad1ea40d3118b32fb.png" class="img-responsive img-rounded" />

この機能は City of Canning によって資金提供されました

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能: SQLの実行/SQL更新ダイアログからのSQLクエリの保存と読み込み
SQLの実行ダイアログと　SQLの更新ダイアログに、SQLクエリを.sqlテキストファイルに保存したり読み込んだりする機能が追加されました。これにより、DBマネージャーで利用可能な機能がコアのブラウザーベースのデータベース接続機能でも使えるようになりました。

UXはQGISの他の標準機能（プロセッシングスクリプトエディターなど）と同様の操作性になるよう設計されており、保存/読み込みのツールバーアクションに加え、コピー、貼り付け、元に戻す、やり直しなどの標準操作の新しいアクションも追加されています。

<img src="images/entries/6f5e0b09c033f427fb7f9162d1b2be5a763d674c" class="img-responsive img-rounded" />

この機能は City of Canning によって資金提供されました

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能: ヘッダーへの OAuth2トークンの追加を可能にする
OAuth2の詳細設定オプションで、OAuth2トークンエンドポイントから送信された追加トークンをHTTP(S)リクエストヘッダーとして付加できるようになりました。これにより、特定のプロバイダーがトークン応答にOpenIDトークンを追加する場合など、OAuth設定をより柔軟に処理できるようになります。

この変更は認証情報管理に統合されており、すべてのOAuth2サービスで利用できます。

<img src="images/entries/2a9dadb3cfbf35b2efea8c7cd9dd4fe49ffbc292" class="img-responsive img-rounded" />

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### 機能: ベクターレイヤーのインポート時のフィールド名の大文字/小文字変換
ベクターレイヤーをデータソースに移行するためのベクターインポートダイアログで、すべてのフィールド名を自動的に小文字または大文字に変換するオプションがサポートされるようになりました。

<img src="images/entries/dc2c1e575d451c7bd98fb6c3b0a7cebe2800fe04" class="img-responsive img-rounded" />

この機能開発には Ocean Winds の資金提供を受けました

This feature was developed by [Jan Caha](https://github.com/JanCaha)
### 機能: 選択した地物のみをデータベーステーブルにインポートします
レイヤーの地物をデータベーステーブルにインポートする際、選択した地物のみにインポートをフィルタリングする新しいダイアログオプションが追加されました。このオプションはインポートするレイヤーに現在の選択がある場合にのみ利用できます。

<img src="images/entries/4a0b7ca2843d5acb9b2c3b3b2a237d6f7e55a308" class="img-responsive img-rounded" />

この機能開発には Ocean Winds の資金提供を受けました

This feature was developed by [Jan Caha](https://github.com/JanCaha)
## フォームとウィジェット
### 機能: フォームでのフィールド名とフィールドエイリアスの切り替え
[QEP 401](https://github.com/qgis/QGIS-Enhancement-Proposals/blob/master/qep-401-overview-widget-types.md) にしたがって、ベクターレイヤープロパティがモデルベースのツリービューに切り替えられました。

これにより、利用可能なウィジェットパネルとフォームレイアウトパネルの両方でフィールド名とフィールドエイリアスを切り替えられる機能など、新しい機能が有効になりました。

Additional enhancements include:
- リレーションが壊れた場合のUXを模倣して、フォームレイアウトで孤立したフィールドがハイライト表示されます
- 壊れたリレーションの改善:リレーションマネージャーでリレーションがまだ利用可能な場合はリレーション名を保持します。

<img src="images/entries/5501d969ec51c06d6ecf49c691c484bec4d08b33.gif" class="img-responsive img-rounded" />

This feature was funded by [the QGIS user group Switzerland](https://qgis.ch/)

This feature was developed by [Germán Carrillo](https://github.com/gacarrillor)
### 機能: 属性フォームデザイナーへの検索ボックスの追加
[QEP#401](https://github.com/qgis/QGIS-Enhancement-Proposals/blob/master/qep-401-overview-widget-types.md) に従って、ドラッグ＆ドロップフォームデザイナーに名前またはエイリアスでアイテムをフィルタリングする検索ボックスが追加されました。これにより、属性フィールドが多数あるテーブルやデータセットでの作業が格段に容易になります。

このフィルターは 利用可能なウィジェットパネルとフォームレイアウトパネルの両方で機能します。

<img src="images/entries/3fefddf7d32b70bf849e390847eca7904ca85ea0.png" class="img-responsive img-rounded" />

This feature was funded by [the QGIS user group Switzerland](https://qgis.ch)

This feature was developed by [Germán Carrillo](https://github.com/gacarrillor)
## 分析ツール
### 機能: モデラーのツールボックスへの入力パラメーターの追加
グラフィカルモデラーに単一の　"ツールボックス" パネルが追加されました。これにより入力パネルとアルゴリズムパネルのオブジェクトが1つのパネルに統合されます。これによりグラフィカルモデラーのUXが簡素化され、モデラーツールの個別タブを管理するのではなく検索フィルターを使用できるようになります。

<img src="images/entries/2372c98c1724436a5d872bab22bd356ab6bae5d8.png" class="img-responsive img-rounded" />

この機能開発には [Hauts-de-France](https://www.hautsdefrance.fr/) の資金提供を受けました

この機能は  [Valentin Buira](https://github.com/ValentinBuira) によって開発されました
## プロセシング
### 機能: SAGAの "Fill Sinks Wang & Liu" のネイティブツールへの移植
このニーズの高いツールは、SAGAプロセッシングプラグイン経由で実行すると不安定でエラーが発生しやすい状況でした。

安定していて効果的な、最適化されたすぐに使えるツールとして新しいネイティブツールが提供されました

なお、この実装はSAGA実装のクローンであるため、ソースに存在するバグは新しいネイティブツールにも存在します。

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能: ラスター計算機への作成オプションUIの追加
ラスター計算機のUIで、ネイティブダイアログとプロセッシングアルゴリズムダイアログの両方にラスター作成オプションが公開されるようになりました。

<img src="images/entries/f95b1f5cf9163bbb300ce45564d4e1a7a0877271.png" class="img-responsive img-rounded" />

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
### 機能: バッチ処理の一時出力
バッチ処理ユーティリティで一時出力レイヤーがサポートされるようになりました。これにより中間データソースの生成や実験をより効率的に行う能力が向上します。

<img src="images/entries/6c4eab5ac90474f0d924f460586ff36b9c8df288.png" class="img-responsive img-rounded" />

この機能開発には Ocean Winds の資金提供を受けました

This feature was developed by [Jan Caha](https://github.com/JanCaha)
### 機能: モデルデザイナーにおける基本的なドラッグアンドドロップ機能の追加
QGISグラフィカルモデラーがモデルノードに接続された独立したソケットをサポートするようになり、ドラッグ＆ドロップでインタラクティブに接続できるようになりました。

これにより、各ノードの入力を個別に設定することなく、あるノードの出力を別のノードの特定の入力に素早く簡単に接続できるようになります。

<img src="images/entries/00050aa06ae1565769944d24e26b9d938da2df6c.png" class="img-responsive img-rounded" />

この機能は  [Valentin Buira](https://github.com/ValentinBuira) によって開発されました
### 機能: プロセッシングラスターランクアルゴリズム
新しい "Raster rank" アルゴリズムは、ラスターのコレクションを入力として受け取り、入力ラスターコレクションから取得したセル値リストのランク順に一致するセル値を持つ出力を作成します。

例えば、あるセルの入力値リストが  \[10,20,30,40\]  でランクが2の場合、出力値は20になります。

このアルゴリズムでは負のインデックスランクも使用できます。同じ入力値リスト  \[10,20,30,40\] でランク値-2を使用した場合、出力値は30になります。

さらに、このアルゴリズムはnodataの処理動作を提供します。デフォルトでは、nodata値はリストから除外され、ランクが値リストのサイズより大きい場合にのみ出力セルがnodataに設定されます。ユーザーは代替動作を選択することもでき、入力レイヤーの特定のセルに1つ以上のnodata値がある場合、その出力セルはnodata値になります。

<img src="images/entries/8fe5df608b4c445246e6e0f4379304e062e20b88" class="img-responsive img-rounded" />

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
## アプリケーションとプロジェクトのオプション
### 機能: 新しい "scale at equator" メソッドを含む、スケール計算のプロジェクト設定の追加
スケール計算方法のプロジェクトレベル設定が追加されました。選択肢は以下の通りです：
- 地図の上部分の縮尺
- 地図の下部分の縮尺
- 地図の中央の縮尺
- 上中下の縮尺の平均
- 常に赤道上の縮尺

スケール方法の変更は以下を含む多数のシステム動作に影響します:
- 新しいレイアウトスケールバーはプロジェクトのスケール計算方法をデフォルトとして使用します。
- スケール計算が調整され、以下を含むプロジェクトの側面に影響します:
  - ステータスバーウィジェットのマップレンダリング
  - `@map_scale` およびその他のスケール関連APIメソッド
  - レイヤーとシンボルのスケールベースの表示
- マップをレンダリングするプロセッシングアルゴリズムはプロジェクトのスケール計算方法に従います。
- スケール方法はQGISサーバーのマップレンダリングに影響します。

 マップ単位で決定されるシンボロジーのサイズはこの設定の影響を受けないことに注意してください。

新しい "常に赤道上の縮尺" 計算方法は、実際の表示マップ範囲に関わらず、常に赤道でのスケールを計算します。これにより、地図に実際に表示されている緯度に関わらず、地理座標系のマップに一貫した静的なスケールを提供するために使用できます。なお、この方法は度数ベースの参照系でスケールを計算する場合にのみ適用可能です。

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能: Nominatimジオコーダーロケーターへの複数の国コードフィルターの追加
Nominatimジオコーダーロケーターの新しいオプション設定値により、結果を制限したい  [2文字の国コード](https://wiki.openstreetmap.org/wiki/Nominatim/Country_Codes) をカンマ区切りの文字列で指定することで、1つまたは複数の国に結果をフィルタリングできるようになりました。

<img src="images/entries/ad98e211c26bc952c65e8c84b0323c866cc293f0" class="img-responsive img-rounded" />

この機能は [level2](https://level2.si/) の資金提供で開発されました

この機能は [Uroš Preložnik](https://github.com/uprel) によって開発されました
## Profile Plots
### 機能: サブセクションインジケーターのサポートの追加
プロファイルプロットがサブセクションインジケーターの表示をサポートするようになりました。インジケーターはプロファイルツールで垂直線としてレンダリングされます。これは [QEP#260](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/260) の成果に基づいており、カスタムインジケーターシンボロジーをサポートするとともに、標高プロファイルビューと印刷レイアウト要素の両方でサブセクションインジケーターを提供します。

<img src="images/entries/4eb01abb7bde11412b39323f0dc89ac13958e050.png" class="img-responsive img-rounded" />

この機能は BRGM の資金提供によって開発されました

This feature was developed by [Jean Felder](https://github.com/ptitjano)
## ブラウザ
### 機能: SQLクエリ履歴のブラウザーへの移植
 [QEP#332](https://github.com/qgis/QGIS-Enhancement-Proposals/blob/master/qep-332-sql-query-history.md) に沿って、データベースクエリ履歴パネルがブラウザーのSQLの実行ダイアログに表示されるようになりました。

クエリ履歴ウィンドウを開くための新しいトップレベルアクションが追加されます。

<img src="images/entries/0790aa10b23a8a21663586201234bb438b88bb21.png" class="img-responsive img-rounded" />

この機能は QGIS grant program 2025 の資金提供によって開発されました

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能: PostgreSQL保存プロジェクトのプロジェクト管理の改善
QGISのブラウザーに、PostGISデータベースに保存されたQGISプロジェクトを操作するオプションが追加されました。新しい機能には以下が含まれます:
- プロジェクト名を変更
- プロジェクトの削除
- プロジェクトを複製
- プロジェクトのスキーマへの移動

<img src="images/entries/2ab1e23aae557053f6271e23db145fc791f425ee" class="img-responsive img-rounded" />

この機能開発には Ocean Winds の資金提供を受けました

This feature was developed by [Jan Caha](https://github.com/JanCaha)
### 機能: ブラウザーからテーブルをインポートする際のダイアログ表示とインポート制御オプションの提供
QGISブラウザーでレイヤーをデータソースにドラッグする際、DBマネージャープラグインのデータインポート機能を模倣した、より包括的なインポート設定を促す新しいダイアログが表示されるようになりました。

なお、これは単一のレイヤーが選択されている場合にのみ機能し、複数選択の場合は引き続き即時インポートが実行されます。

現在のプロジェクトレイヤーから対象スキーマに直接インポートできる新しい "Import Vector Table.." コンテキストメニュー項目も追加されました。

ダイアログのオプションには以下が含まれます:
- インポート先テーブルの名前変更
- インポート先の置き換え
- 主キーの設定
- ジオメトリ列の設定
- インポート先CRSの設定
- 出力テーブルのコメントの設定

この作業では、QGISブラウザーとデータプロバイダーの実装に関する多くの内部アーキテクチャ要素のリファクタリングが必要でした。これは部分的に、DBマネージャーのPostgresインポート機能をQGISブラウザーに移植するための  [@JanCaha](https://github.com/JanCaha) による取り組みに基づいています。

なお、この機能はOracleデータプロバイダーが活用しているレガシー機能の制約により、現時点ではOracleデータベースをサポートしていません。

<img src="images/entries/eedf110211aebb2acf61d89108d15ada41b616c8" class="img-responsive img-rounded" />

この機能は City of Canning によって資金提供されました

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能: PostgreSQLプロバイダーでの別スキーマへのテーブルの移動
QGISブラウザーから直接、PostgreSQLテーブルを別のスキーマに移動できるようになりました。

この機能開発には Ocean Winds の資金提供を受けました

This feature was developed by [Jan Caha](https://github.com/JanCaha)
### 機能: PostgreSQLのフィールド名変更を有効化
QGISブラウザーインターフェースから直接、PostgreSQLテーブルのフィールド名を変更できるようになりました。

この機能開発には Ocean Winds の資金提供を受けました

This feature was developed by [Jan Caha](https://github.com/JanCaha)
## データプロバイダ
### 機能: featureModeのWFSパラメーターの追加
WFSプロバイダーのURIとUIが "featureMode" パラメーターをサポートするようになりました。以下のオプションをサポートします:
- デフォルト (サーバーのデフォルト設定を使用)
- 単純地物 (返された地物の単純化を有効にする)
- 複雑な地物 (返された地物の単純化を無効にする)

This feature was developed by [Even Rouault](https://github.com/rouault)
### 機能: PostgreSQLスキーマを制限する接続設定の追加
この機能により、Oracle プロバイダーの同等設定と同様に、Postgres接続を特定の1つのスキーマに制限するよう指定できます。

設定すると、一致するスキーマのテーブルのみが接続のブラウザーパネルとデータソース選択に含まれます。

これにより、大規模なデータベースストアを指す接続のテーブル取得に必要なデータベース処理を制限するために使用できます。

<img src="images/entries/14da725b2b420a05075ba1b09c83786bf5c839f3" class="img-responsive img-rounded" />

この機能開発には Regiodata からの資金提供を受けています

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能: WFS接続でのPOSTリクエストの使用オプションの追加
デフォルトでは、WFSサーバーへの接続はGETリクエストを使用しますが、特定のWFS接続をPOSTのHTTPメソッドを使用するように切り替えることができるようになり、Webサービスの設定においてより柔軟な対応が可能になります。

<img src="images/entries/4a70618846a5eac6a459a0262887e3474bb1c091" class="img-responsive img-rounded" />

この機能を開発には Dorset Council の資金提供を受けています

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能: SQL ServerからのSQLクエリをレイヤーソースとして使用可能に
QGISでブラウザーからSQL Serverのクエリをマップレイヤーとして読み込んだり、既存のクエリレイヤーのSQLを更新したりできるようになりました。

この機能は City of Canning によって資金提供されました

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## QGISサーバー
### 機能: サーバープロジェクトのキャッシュサイズの設定を可能に
新しい環境変数 `QGIS_SERVER_PROJECT_CACHE_SIZE` が追加されました。これにより、以前はハードコードされていたQCacheコストを設定できるようになります。

This feature was developed by [Sandro Mani](https://github.com/manisandro)
### 機能: レイヤーツリーグループへのサーバープロパティの追加
GetCapabilitiesリクエストで返されるレイヤーツリーグループの追加サーバープロパティを編集できるようになりました。利用可能なプロパティは、以前の短い名前、タイトル、概要に加えて以下まで拡張されました:
- キーワード
- データURL (フォーマット付き)
- 帰属タイトルとURL
- メタデータURL
- 凡例URLと形式（デフォルトでは自動生成されます）

<img src="images/entries/41632eca99d103daf60c2d90b21ce9a543dfc53f.png" class="img-responsive img-rounded" />

この機能は Ifremer によって資金提供されました

This feature was developed by [Julien Cabieces](https://github.com/troopa81)
## プログラム可能
### 機能: ShapelyジオメトリをQGISジオメトリに変換するメソッドの追加
 [QEP#227](This%20is%20part%20of%20https://github.com/qgis/QGIS-Enhancement-Proposals/issues/227) に沿って、ShapelyをオプションのI依存関係として維持しながらshapelyジオメトリライブラリとの統合を向上させるため、shapelyオブジェクトからQgsGeometryオブジェクトを生成する新しい QgsGeometry.from_shapely() メソッドが提供されました。

This feature was developed by [Till Frankenbach](https://github.com/merydian)
### 機能: QGIS GPSツールのPython APIとプラグインへの公開
GPSツールクラスが `QgisInterface::gpsTools()` を通じてアクセスできる新しい `QgsAppGpsTools` クラスとしてPyQGIS APIで利用可能になり、プラグインがQGIS GPSトラッキングセッションをより細かく制御できるようになりました。

 QGIS 3.44以降、プラグインは `iface.gpsTools().createFeatureFromGpsTrack()` メソッドを使用して現在のGPSトラックからベクターレイヤーの地物を作成できるようになりました。

また、QgsOptions の対応する設定を変更してGPSトラックラインシンボルを設定し、それに応じて最終的な現在のGPSトラックジオメトリを更新するなど、追加の機能も公開されています。例: `iface.gpsTools().setGpsTrackLineSymbol( line_symbol )`

この機能は [the Danish Nature Agency, Naturstyrelsen](https://naturstyrelsen.dk/) の資金提供で開発されました

This feature was developed by [Germán Carrillo](https://github.com/gacarrillor)
## 注目すべき修正
### Feature: Bug fixes by Even Rouault (Spatialys)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| CSV Import to Geopackage ( x/y data) ignores more than 5 Mio rows | [\#60966](https://github.com/qgis/QGIS/issues/60966) | 再現不可 |  |
| OGC API: Feature Creation Request Fails When Location Header is in Lowercase | [\#61729](https://github.com/qgis/QGIS/issues/61729) | [PR \#61814](https://github.com/qgis/QGIS/pull/61814) | [PR \#61835](https://github.com/qgis/QGIS/pull/61835) |
| \[Backport 3.40\] Pick missing commits | [mailing list](https://lists.osgeo.org/pipermail/qgis-developer/2025-May/067555.html) |  | [PR \#61843](https://github.com/qgis/QGIS/pull/61843) |
| Processing : unable to import non spatial table into PostGreSQL with OGR command with processing | [\#61655](https://github.com/qgis/QGIS/issues/61655) | [PR \#61868](https://github.com/qgis/QGIS/pull/61868) | [PR \#62023](https://github.com/qgis/QGIS/pull/62023) |
| Impossibility to save a Null value in a Interger64 field for geopackage files | [\#61787](https://github.com/qgis/QGIS/issues/61787) | 再現不可 |  |
| Error in GML handling in response to a GetFeature request in the WFS service | [\#60879](https://github.com/qgis/QGIS/issues/60879) | [PR \#61872](https://github.com/qgis/QGIS/pull/61872) | [PR \#61895](https://github.com/qgis/QGIS/pull/61895) |
| \[Tests\] Fix and unblock PyQgsLayerDefinition on QT6 |  | [PR \#61874](https://github.com/qgis/QGIS/pull/61874) | N/A |
| \[Tests\] Fix test_core_ogcutils on QT6 |  | [PR \#61876](https://github.com/qgis/QGIS/pull/61876) | N/A |
| \[Tests\] Fix PyQgsDelimitedTextProvider on QT6 |  | [PR \#61877](https://github.com/qgis/QGIS/pull/61877) | N/A |
| \[Tests\] Fix PyQgsSymbolLayerReadSld on QT6 |  | [PR \#61878](https://github.com/qgis/QGIS/pull/61878) | N/A |
| weird include paths including cmake keywords | [\#61887](https://github.com/qgis/QGIS/issues/61887) | [PR \#61894](https://github.com/qgis/QGIS/pull/61894) | N/A |
| QGIS Server GetProjectSettings doesn't output the EX_GeographicBoundingBox anymore for reverse axis projectsions | [\#61999](https://github.com/qgis/QGIS/issues/61999) | [PR \#62002](https://github.com/qgis/QGIS/pull/62002) | [PR \#62036](https://github.com/qgis/QGIS/pull/62036) |
| Spilhaus not displayed complete in QGIS 3.42.1 | [\#61318](https://github.com/qgis/QGIS/issues/61318) | [PR \#62002](https://github.com/qgis/QGIS/pull/62002) | [PR \#62036](https://github.com/qgis/QGIS/pull/62036) |
| QT6 tests: fix PyQgsServerAccessControlWFSTransactional |  | [PR \#62034](https://github.com/qgis/QGIS/pull/62034) | N/A |
| OAPIF: CQL layer filter expression is not used in request | [\#60092](https://github.com/qgis/QGIS/issues/60092) | [PR \#62156](https://github.com/qgis/QGIS/pull/62156) | [PR \#62186](https://github.com/qgis/QGIS/pull/62186) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Even Rouault (Spatialys)](https://www.spatialys.com/)
### Feature: Bug fixes by Alessandro Pasotti (QCooperative)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| Qgis server - Labels background get transparent based on layer transparency | [\#61801](https://github.com/qgis/QGIS/issues/61801) | Won't fix (not a bug) |  |
| Inconsistent contents in ogcapi openapi spec | [\#61848](https://github.com/qgis/QGIS/issues/61848) | [PR \#61903](https://github.com/qgis/QGIS/pull/61903) | [PR \#61922](https://github.com/qgis/QGIS/pull/61922) |
| QGIS Server does not list one layer in WMS GetCapabilities if datum transformation is used | [\#61293](https://github.com/qgis/QGIS/issues/61293) | フィードバック |  |
| QGIS server 3.40.4 - Invalid cache strategy | [\#60947](https://github.com/qgis/QGIS/issues/60947) | [PR \#61907](https://github.com/qgis/QGIS/pull/61907) | N/A |
| Server LTR: OAPIF/WFS3 describe collections malfunction - empty pg layer with UTM zone SRID | [\#60686](https://github.com/qgis/QGIS/issues/60686) | 再現不可 |  |
| Wrong rendering for HIGHLIGHT_LABEL_ROTATION above 89° | [\#54598](https://github.com/qgis/QGIS/issues/54598) | Old issue: asked the OP and put on feedback |  |
| CGIDIR default for UNIX is wrong (bin, should be libexec/cgi-bin or at least not bin) | [\#54424](https://github.com/qgis/QGIS/issues/54424) | Old issue: asked for feedback |  |
| Performance issue on editing large PostGIS layers. | [\#61879](https://github.com/qgis/QGIS/issues/61879) | Not enough info: put on feedback and recommended to hire a consultant |  |
| New HTTP (WMS & friends) connection dialog too tall | [\#61867](https://github.com/qgis/QGIS/issues/61867) | [PR \#61912](https://github.com/qgis/QGIS/pull/61912) | Not critical |
| Problems with \<NULL\> value in Value map | [\#61865](https://github.com/qgis/QGIS/issues/61865) | [PR \#61915](https://github.com/qgis/QGIS/pull/61915) | [PR \#61939](https://github.com/qgis/QGIS/pull/61939) |
| Expression constraint requires case-sensitive field names while form is open | [\#61740](https://github.com/qgis/QGIS/issues/61740) | [PR \#61928](https://github.com/qgis/QGIS/pull/61928) | [PR \#61949](https://github.com/qgis/QGIS/pull/61949) |
| JSON array attribute fields are not supported | [\#61728](https://github.com/qgis/QGIS/issues/61728) | [PR \#61938](https://github.com/qgis/QGIS/pull/61938) | Risky |
| WMS: The parser incorrectly assumes that PositionType contains only a single space (but multiple spaces may exist) | [\#61399](https://github.com/qgis/QGIS/issues/61399) | [PR \#61963](https://github.com/qgis/QGIS/pull/61963) | [PR \#61986](https://github.com/qgis/QGIS/pull/61986) |
| Graduated classification offers date/datetime fields but does not support them | [\#61767](https://github.com/qgis/QGIS/issues/61767) | [PR \#61964](https://github.com/qgis/QGIS/pull/61964) | [PR \#61987](https://github.com/qgis/QGIS/pull/61987) |
| Advanced Digitizing: Floater not working correctly | [\#61587](https://github.com/qgis/QGIS/issues/61587) | [PR \#61979](https://github.com/qgis/QGIS/pull/61979) | [PR \#62114](https://github.com/qgis/QGIS/pull/62114) |
| QGis Server quotes html maptip | [\#61380](https://github.com/qgis/QGIS/issues/61380) | won't fix (not a bug) |  |
| Hidden coverage layer option remains active after disabling atlas generation in layout | [\#61946](https://github.com/qgis/QGIS/issues/61946) | [PR \#61993](https://github.com/qgis/QGIS/pull/61993) | [PR \#62066](https://github.com/qgis/QGIS/pull/62066) |
| Distance/area user selected unit unwanted reset in processing tools | [\#61470](https://github.com/qgis/QGIS/issues/61470) | [PR \#61997](https://github.com/qgis/QGIS/pull/61997) | [PR \#62021](https://github.com/qgis/QGIS/pull/62021) |
| PG: Can't add/update feature when numeric field with numeric default is set to default | [\#61529](https://github.com/qgis/QGIS/issues/61529) | [PR \#62010](https://github.com/qgis/QGIS/pull/62010) | Risky |
| In Refactor Fields algorithm, field for "Source Expression" are loaded from the wrong layer when "selected features only" option is checked | [\#62019](https://github.com/qgis/QGIS/issues/62019) | [PR \#62124](https://github.com/qgis/QGIS/pull/62124) | [PR \#62235](https://github.com/qgis/QGIS/pull/62235) |
| Wrong timezone from default value when adding child feature | [\#62121](https://github.com/qgis/QGIS/issues/62121) | won't fix (not a bug) |  |
| Ellipsoidal measurement not working when the project is using a custom CRS | [\#61299](https://github.com/qgis/QGIS/issues/61299) | [PR \#62212](https://github.com/qgis/QGIS/pull/62212) | [PR \#62252](https://github.com/qgis/QGIS/pull/62252) |
| \[Processing\] "Select by Expression" doesn't works with some expressions | [\#62231](https://github.com/qgis/QGIS/issues/62231) | [PR \#62233](https://github.com/qgis/QGIS/pull/62233) | N/A |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Alessandro Pasotti (QCooperative)](https://www.qcooperative.net/)
### Feature: Bug fixes by Jacky Volpes (Oslandia)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| QgsOptions: Locale value is saved only if it is not empty | [\#52359](https://github.com/qgis/QGIS/issues/52359) | [PR \#62137](https://github.com/qgis/QGIS/pull/62137) | [PR \#62171](https://github.com/qgis/QGIS/pull/62171) |
| Extent not updated after digitizing features in a memory layer | [\#60830](https://github.com/qgis/QGIS/issues/60830) | [PR \#62159](https://github.com/qgis/QGIS/pull/62159) | [PR \#62189](https://github.com/qgis/QGIS/pull/62189) |
| Issue with the geometry combine and mergeLines | [\#61136](https://github.com/qgis/QGIS/issues/61136) | [PR \#62184](https://github.com/qgis/QGIS/pull/62184) |  |
| Atlas activation crash | [\#59610](https://github.com/qgis/QGIS/issues/59610) | [PR \#62260](https://github.com/qgis/QGIS/pull/62260) | [PR \#62288](https://github.com/qgis/QGIS/pull/62288) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Jacky Volpes (Oslandia)](https://oslandia.com/en/)
### Feature: Bug fixes by Jean Felder (Oslandia)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| QgsOptions: Locale value is saved only if it is not empty | [\#52359](https://github.com/qgis/QGIS/issues/52359) | [PR \#62137](https://github.com/qgis/QGIS/pull/62137) | [PR \#62171](https://github.com/qgis/QGIS/pull/62171) |
| Extent not updated after digitizing features in a memory layer | [\#60830](https://github.com/qgis/QGIS/issues/60830) | [PR \#62159](https://github.com/qgis/QGIS/pull/62159) | [PR \#62189](https://github.com/qgis/QGIS/pull/62189) |
| Issue with the geometry combine and mergeLines | [\#61136](https://github.com/qgis/QGIS/issues/61136) | [PR \#62184](https://github.com/qgis/QGIS/pull/62184) |  |
| Atlas activation crash | [\#59610](https://github.com/qgis/QGIS/issues/59610) | [PR \#62260](https://github.com/qgis/QGIS/pull/62260) | [PR \#62288](https://github.com/qgis/QGIS/pull/62288) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Jean Felder (Oslandia)](https://oslandia.com/en/)
### Feature: Bug fixes by Alexander Bruy (QCooperative)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| Better support for SQL and virtual layers as inputs in Processing | [\#39138](https://github.com/qgis/QGIS/issues/39138) | [PR \#61880](https://github.com/qgis/QGIS/pull/61880) | [PR \#61902](https://github.com/qgis/QGIS/pull/61902) |
| Using virtual layer gives error in GDAL processing algorithms | [\#59364](https://github.com/qgis/QGIS/issues/59364) | [PR \#61880](https://github.com/qgis/QGIS/pull/61880) | [PR \#61902](https://github.com/qgis/QGIS/pull/61902) |
| enable GdalAlgorithmsVectorTest on QT6 |  | [PR \#61882](https://github.com/qgis/QGIS/pull/61882) | N/A |
| fix PyQgsFloatingWidget test on Qt6 |  | [PR \#61885](https://github.com/qgis/QGIS/pull/61885) | N/A |
| fix PyQgsNetworkAccessManager test on Qt6 |  | [PR \#61886](https://github.com/qgis/QGIS/pull/61886) | N/A |
| enable QGIS algorithms tests (part 2) on Qt6 |  | [PR \#61888](https://github.com/qgis/QGIS/pull/61888) | N/A |
| Geopackage vocabulary harmonization | [\#60990](https://github.com/qgis/QGIS/issues/60990) | [PR \#61893](https://github.com/qgis/QGIS/pull/61893) | N/A |
| unbalanced QSettings.beginReadArray/endArray calls | [\#61373](https://github.com/qgis/QGIS/issues/61373) | [PR \#61904](https://github.com/qgis/QGIS/pull/61904) | [PR \#61923](https://github.com/qgis/QGIS/pull/61923) |
| Mesh styling, precision seems too small? | [\#50950](https://github.com/qgis/QGIS/issues/50950) | [PR \#61905](https://github.com/qgis/QGIS/pull/61905) | [PR \#61926](https://github.com/qgis/QGIS/pull/61926) |
| Inconsistency in PostgreSQL / PostGIS connection / layer dialog windows | [\#59886](https://github.com/qgis/QGIS/issues/59886) | [PR \#61908](https://github.com/qgis/QGIS/pull/61908) | N/A |
| Translate geometry does not create a 3D vector from 2D if deltaZ is an expression | [\#56495](https://github.com/qgis/QGIS/issues/56495) | [PR \#61906](https://github.com/qgis/QGIS/pull/61906) | [PR \#61933](https://github.com/qgis/QGIS/pull/61933) |
| After deleting the newly added XYZ layer...still exists | [\#53933](https://github.com/qgis/QGIS/issues/53933) | 再現不可 |  |
| TypeError: EnumType.**call**()... | [\#58312](https://github.com/qgis/QGIS/issues/58312) | 再現不可 |  |
| projects/anonymize\_\*\_projects doesn't affect projectMetadata.author | [\#42413](https://github.com/qgis/QGIS/issues/42413) | [PR \#61945](https://github.com/qgis/QGIS/pull/61945) | [PR \#61959](https://github.com/qgis/QGIS/pull/61959) |
| Inconsistencies in providers connection dialogs | [\#43951](https://github.com/qgis/QGIS/issues/43951) | [PR \#61948](https://github.com/qgis/QGIS/pull/61948) | N/A |
| Source manager and WMS configuration dialog too tall | [\#60477](https://github.com/qgis/QGIS/issues/60477) | [PR \#61948](https://github.com/qgis/QGIS/pull/61948) | N/A |
| New HTTP (WMS & friends) connection dialog too tall | [\#61867](https://github.com/qgis/QGIS/issues/61867) | [PR \#61948](https://github.com/qgis/QGIS/pull/61948) | N/A |
| duplicated objectName in the oracle dialog | 未報告 | [PR \#61944](https://github.com/qgis/QGIS/pull/61944) | N/A |
| "Save as" does not work... | [\#30130](https://github.com/qgis/QGIS/issues/30130) | [PR \#61960](https://github.com/qgis/QGIS/pull/61960) | N/A |
| Modifying project CRS...does not update coordinate CRS display | [\#61684](https://github.com/qgis/QGIS/issues/61684) | [PR \#61995](https://github.com/qgis/QGIS/pull/61995) | N/A |
| CRS selection widget not updated when project CRS changes | [\#56454](https://github.com/qgis/QGIS/issues/56454) | [PR \#61989](https://github.com/qgis/QGIS/pull/61989) | [PR \#62022](https://github.com/qgis/QGIS/pull/62022) |
| Choice for default/project styles missing... | [\#58653](https://github.com/qgis/QGIS/issues/58653) | [PR \#62012](https://github.com/qgis/QGIS/pull/62012) | N/A |
| Changing a new project's CRS does not change the annotation CRS | [\#48046](https://github.com/qgis/QGIS/issues/48046) | can't reproduce, already fixed |  |
| "editable" property misleading in JSON view | [\#47755](https://github.com/qgis/QGIS/issues/47755) | [PR \#62064](https://github.com/qgis/QGIS/pull/62064) | N/A |
| ‘Current CRS’ icon shows previous CRS | [\#53768](https://github.com/qgis/QGIS/issues/53768) | [PR \#62209](https://github.com/qgis/QGIS/pull/62209) | [PR \#62236](https://github.com/qgis/QGIS/pull/62236) |
| Crash when clicking on relation table node | [\#56481](https://github.com/qgis/QGIS/issues/56481) | 再現不可 |  |
| Documentation file grass7.txt is not up-to-date | [\#29140](https://github.com/qgis/QGIS/issues/29140) | [PR \#62210](https://github.com/qgis/QGIS/pull/62210) | N/A |
| AttributeError: 'NoneType' object has no attribute 'fields' | [\#62224](https://github.com/qgis/QGIS/issues/62224) | [PR \#62253](https://github.com/qgis/QGIS/pull/62253) | [PR \#62291](https://github.com/qgis/QGIS/pull/62291) |
| Selected field not cleared when changing layer in processing | [\#39351](https://github.com/qgis/QGIS/issues/39351) | [PR \#62241](https://github.com/qgis/QGIS/pull/62241) | [PR \#62305](https://github.com/qgis/QGIS/pull/62305) |
| pyqgis: QgsGraph | [\#56172](https://github.com/qgis/QGIS/issues/56172) | [PR \#62316](https://github.com/qgis/QGIS/pull/62316) | N/A |
| qgsidentifyresultsdialog.cpp: ‘best approach’ vs. ‘old fragile approach’ | [\#61499](https://github.com/qgis/QGIS/issues/61499) | 再現不可 |  |
| exporting to .dxf sets units to imperial inch | [\#50579](https://github.com/qgis/QGIS/issues/50579) | works for me, fixed upstream |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Alexander Bruy (QCooperative)](https://www.qcooperative.net/)
### Feature: Bug fixes by Stefanos Natsis (LutraConsulting)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| STAC client connection failing | [\#62232](https://github.com/qgis/QGIS/issues/62232) | [PR \#62258](https://github.com/qgis/QGIS/pull/62258) | N/A |
| \[browser\] Inappropriate menus in Postgres connection context menu | [\#62183](https://github.com/qgis/QGIS/issues/62183) | [PR \#62270](https://github.com/qgis/QGIS/pull/62270#discussion_r2149355232) | N/A |
| QGIS master crashes when trying to use reshape features tool | [\#55859](https://github.com/qgis/QGIS/issues/55859) | [PR \#62295](https://github.com/qgis/QGIS/pull/62295) | [PR \#62326](https://github.com/qgis/QGIS/pull/62326) |
| Reshape Features can't handle resulting exclaves | [\#24884](https://github.com/qgis/QGIS/issues/24884) | [PR \#62312](https://github.com/qgis/QGIS/pull/62312) |  |
| Reshape tool doesn't obey 'Avoid Overlaps' when a feature is selected. | [\#61720](https://github.com/qgis/QGIS/issues/61720) | [PR \#62312](https://github.com/qgis/QGIS/pull/62312) |  |
| Fix reshaping when snapping to segment | 未報告 | [PR \#62315](https://github.com/qgis/QGIS/pull/62315) |  |
| Unhandled GEOS exception when reshaping | 未報告 | [PR \#62322](https://github.com/qgis/QGIS/pull/62322) |  |
| Reshape returns Success instead of NothingHappened | 未報告 | [PR \#62323](https://github.com/qgis/QGIS/pull/62323) | [PR \#62336](https://github.com/qgis/QGIS/pull/62336) |
| Reshape tool tries to run with a single digitized point | 未報告 | [PR \#62324](https://github.com/qgis/QGIS/pull/62324) |  |
| Fix crash when undoing first digitized point in shape map tools | 未報告 | [PR \#62335](https://github.com/qgis/QGIS/pull/62335) |  |
| Fix crashing shape tools when not enough points digitized | 未報告 | [PR \#62338](https://github.com/qgis/QGIS/pull/62338) |  |
| Crash any time I try to modify a polygon with "Enable tracing" activated. | [\#60856](https://github.com/qgis/QGIS/issues/60856) | [PR \#62345](https://github.com/qgis/QGIS/pull/62345) |  |
| trace function on snap toolset causes QGIS to shutdown when initiated | [\#60978](https://github.com/qgis/QGIS/issues/60978) | [PR \#62345](https://github.com/qgis/QGIS/pull/62345) |  |
| Crash on vector digitizing with trace tool | [\#62163](https://github.com/qgis/QGIS/issues/62163) | [PR \#62345](https://github.com/qgis/QGIS/pull/62345) |  |
| QGIS 3.40.7 Bratislava crashes every time I try to use the tracing tool to create polygons | [\#62342](https://github.com/qgis/QGIS/issues/62342) | [PR \#62345](https://github.com/qgis/QGIS/pull/62345) |  |
| Misbehavior of advanced topology settings on independant layers | バグではない |  |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Stefanos Natsis (LutraConsulting)](https://www.lutraconsulting.co.uk/)
### Feature: Bug Fixes by Germán Carrillo (OPENGIS)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| Old relations in form (after exporting layer to new file and applied old style) can't be deleted | [\#44683](https://github.com/qgis/QGIS/issues/44683) | Can't reproduce |  |
| \[Processing toolbox\] Search box (result) not updated when list of providers change | [\#26435](https://github.com/qgis/QGIS/issues/26435) | [PR \#62162](https://github.com/qgis/QGIS/pull/62162) | No |
| 曖昧なJSONエラー | [\#42832](https://github.com/qgis/QGIS/issues/42832) | [PR \#62247](https://github.com/qgis/QGIS/pull/62247) | [PR \#62262](https://github.com/qgis/QGIS/pull/62262) |
| Disallow point layer as input to Oriented Minimum Bounding Box | [\#62126](https://github.com/qgis/QGIS/issues/62126) | [PR \#62300](https://github.com/qgis/QGIS/pull/62300) | [PR \#62330](https://github.com/qgis/QGIS/pull/62330) |
| When saving SLD to DB, make sure errors are reported to callers (like Package layers algorithm) | 未報告 | [PR \#62332](https://github.com/qgis/QGIS/pull/62332) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Germán Carrillo (OPENGIS)](https://opengis.ch/)
### Feature: Bug fixes by Mathieu Pellerin (OPENGIS)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| QGIS fails to import sprites from OpenStreetMap vector tile styles | 未報告 | [PR \#62175](https://github.com/qgis/QGIS/pull/62175) |  |
| Menu bar not respecting set font size on qt6 build | [\#62007](https://github.com/qgis/QGIS/issues/62007) | [PR \#62086](https://github.com/qgis/QGIS/pull/62086) |  |
| QGIS Qt6 the gui to select the Profile is not well visible | [\#61557](https://github.com/qgis/QGIS/issues/61557) | [PR \#62083](https://github.com/qgis/QGIS/pull/62083) |  |
| Clip by extent prints error on console | [\#61365](https://github.com/qgis/QGIS/issues/61365) | [PR \#62075](https://github.com/qgis/QGIS/pull/62075) | [PR \#62094](https://github.com/qgis/QGIS/pull/62094) |
| QGIS freeze/is not responding, big CPU usage when setting horizontal and vertical spacing units in "point pattern fill" to "meters at scale" | [\#53550](https://github.com/qgis/QGIS/issues/53550) | [PR \#62074](https://github.com/qgis/QGIS/pull/62074) | [PR \#62106](https://github.com/qgis/QGIS/pull/62106) |
| Project translation only happening for .qgs, not .qgz | [\#61485](https://github.com/qgis/QGIS/issues/61485) | [PR \#62070](https://github.com/qgis/QGIS/pull/62070) | [PR \#62101](https://github.com/qgis/QGIS/pull/62101) |
| Stuck in pan mode when using both middle mouse and space pan in model or layout | [\#61528](https://github.com/qgis/QGIS/issues/61528) | [PR \#62069](https://github.com/qgis/QGIS/pull/62069) | [PR \#62093](https://github.com/qgis/QGIS/pull/62093) |
| Unchecking "Include Z-dimension" still includes Z when Geometry Type is Automatic | [\#61554](https://github.com/qgis/QGIS/issues/61554) | [PR \#62068](https://github.com/qgis/QGIS/pull/62068) | [PR \#62092](https://github.com/qgis/QGIS/pull/62092) |
| Label font style reverts to Regular in non_english UI (LTR, Qt5) | [\#61660](https://github.com/qgis/QGIS/issues/61660) | [PR \#62067](https://github.com/qgis/QGIS/pull/62067) | [PR \#62080](https://github.com/qgis/QGIS/pull/62080) |
| Custom shortcuts are not replacing default ones when imported from XML | [\#61717](https://github.com/qgis/QGIS/issues/61717) | [PR \#62063](https://github.com/qgis/QGIS/pull/62063) |  |
| QGIS fails to handle of source containing a relative path to the root of the server hosting the style json | 未報告 | [PR \#62062](https://github.com/qgis/QGIS/pull/62062) | [PR \#62084](https://github.com/qgis/QGIS/pull/62084) |
| Can't save layers as gpkg.zip | [\#61773](https://github.com/qgis/QGIS/issues/61773) | [PR \#62049](https://github.com/qgis/QGIS/pull/62049) | [PR \#62185](https://github.com/qgis/QGIS/pull/62185) |
| appearance input attributes box do not appear checked | [\#61994](https://github.com/qgis/QGIS/issues/61994) | [PR \#62047](https://github.com/qgis/QGIS/pull/62047) | [PR \#62056](https://github.com/qgis/QGIS/pull/62056) |
| QGIS-Locator, Behavior changed between 3.22 and 3.4x | [\#62013](https://github.com/qgis/QGIS/issues/62013) | [PR \#62043](https://github.com/qgis/QGIS/pull/62043) | [PR \#62058](https://github.com/qgis/QGIS/pull/62058) |
| Various new connection dialog spacing and size issues | 未報告 | [PR \#62041](https://github.com/qgis/QGIS/pull/62041) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Mathieu Pellerin (OPENGIS)](https://opengis.ch/)
### Feature: Bug fixes by Julien Cabieces (Oslandia)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| Colours in PDF outputs appear washed out and don't render properly | [\#61674](https://github.com/qgis/QGIS/issues/61674) | [PR \#62091](https://github.com/qgis/QGIS/pull/62091) | [PR \#62107](https://github.com/qgis/QGIS/pull/62107) |
| \[Oracle\] Fix PyQgsProviderRegistry test | qt6 test failing | [PR \#62109](https://github.com/qgis/QGIS/pull/62109) | No |
| Model Designer - Python Converter not generating unique keys | [\#54150](https://github.com/qgis/QGIS/issues/54150) | [PR \#62261](https://github.com/qgis/QGIS/pull/62261) | [PR \#62329](https://github.com/qgis/QGIS/pull/62329) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Julien Cabieces (Oslandia)](https://oslandia.com/en/)
### Feature: Bug fixes by Nyall Dawson (North Road)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fix walk mode key handling | 未報告 | [PR \#62331](https://github.com/qgis/QGIS/pull/62331) | N/A |
| Increase QImageReader allocation limit for qt6 builds | 未報告 | [PR \#62320](https://github.com/qgis/QGIS/pull/62320) | N/A |
| Don't try to pass unset attributes to ArcGIS REST backends | [\#61673](https://github.com/qgis/QGIS/issues/61673) | [PR \#62061](https://github.com/qgis/QGIS/pull/62061) | [PR \#62249](https://github.com/qgis/QGIS/pull/62249) |
| Fix serious regression in boolean handling in expressions | [\#61072](https://github.com/qgis/QGIS/issues/61072) | [PR \#62217](https://github.com/qgis/QGIS/pull/62217) | [PR \#62248](https://github.com/qgis/QGIS/pull/62248) |
| Don't render effects which require rasterisation when forcing vector | [\#58230](https://github.com/qgis/QGIS/issues/58230) | [PR \#62218](https://github.com/qgis/QGIS/pull/62218) | N/A |
| Fix categorized symbol renderer feature counts for null values | [\#52690](https://github.com/qgis/QGIS/issues/52690) | [PR \#62174](https://github.com/qgis/QGIS/pull/62174) | [PR \#62203](https://github.com/qgis/QGIS/pull/62203) |
| Try to extract only polygons from Voronoi results | [\#62158](https://github.com/qgis/QGIS/issues/62158) | [PR \#62173](https://github.com/qgis/QGIS/pull/62173) | [PR \#62194](https://github.com/qgis/QGIS/pull/62194) |
| \[processing\] Fix show feature count option, output layer ordering | [\#61146](https://github.com/qgis/QGIS/issues/61146) | [PR \#62143](https://github.com/qgis/QGIS/pull/62143) | [PR \#62172](https://github.com/qgis/QGIS/pull/62172) |
| Don't finalize string stats after every value addition | [\#62122](https://github.com/qgis/QGIS/issues/62122) | [PR \#62170](https://github.com/qgis/QGIS/pull/62170) | [PR \#62192](https://github.com/qgis/QGIS/pull/62192) |
| Fix build with SIP \>= 6.11 | [\#61951](https://github.com/qgis/QGIS/issues/61951) | [PR \#62113](https://github.com/qgis/QGIS/pull/62113) | [PR \#62142](https://github.com/qgis/QGIS/pull/62142) |
| Use protected, not private virtual methods for map tool classes | 未報告 | [PR \#62097](https://github.com/qgis/QGIS/pull/62097) | [PR \#62112](https://github.com/qgis/QGIS/pull/62112) |
| Avoid corrupted overlapping docks when first changing from dialog to dock | 未報告 | [PR \#62102](https://github.com/qgis/QGIS/pull/62102) | N/A |
| Fix jumpy scroll area when using mouse wheel on qt6 builds | 未報告 | [PR \#62099](https://github.com/qgis/QGIS/pull/62099) | N/A |
| Fix comparators | [\#62045](https://github.com/qgis/QGIS/issues/62045) | [PR \#62081](https://github.com/qgis/QGIS/pull/62081) | [PR \#62118](https://github.com/qgis/QGIS/pull/62118) |
| \[processing\] Fix execution of nested models | [\#60883](https://github.com/qgis/QGIS/issues/60883) | [PR \#62079](https://github.com/qgis/QGIS/pull/62079) | [PR \#62100](https://github.com/qgis/QGIS/pull/62100) |
| Fix calculation of cost for speed strategy with null/negative values | [\#61667](https://github.com/qgis/QGIS/issues/61667) | [PR \#62044](https://github.com/qgis/QGIS/pull/62044) | [PR \#62059](https://github.com/qgis/QGIS/pull/62059) |
| Fix variables available for grid annotations missing for grid symbol | 未報告 | [PR \#61943](https://github.com/qgis/QGIS/pull/61943) | [PR \#61957](https://github.com/qgis/QGIS/pull/61957) |
| Add new enum for rasterised rendering policy | [\#58230](https://github.com/qgis/QGIS/issues/58230) | [PR \#61942](https://github.com/qgis/QGIS/pull/61942) | N/A |
| Fix blend modes ignored when label masking is enabled | [\#43141](https://github.com/qgis/QGIS/issues/43141) | [PR \#61901](https://github.com/qgis/QGIS/pull/61901) | N/A |
| Delimited text test can be run on qt6 now | 未報告 | [PR \#61900](https://github.com/qgis/QGIS/pull/61900) | N/A |
| Fix mesh layer labeling tests not actually run | 未報告 | [PR \#61899](https://github.com/qgis/QGIS/pull/61899) | [PR \#61909](https://github.com/qgis/QGIS/pull/61909) |
| \[ogr\] Handle auto addition of vsizip prefix for vsicurl archives | [\#61561](https://github.com/qgis/QGIS/issues/61561) | [PR \#61854](https://github.com/qgis/QGIS/pull/61854) | [PR \#61896](https://github.com/qgis/QGIS/pull/61896) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)

{{<content-end >}}
