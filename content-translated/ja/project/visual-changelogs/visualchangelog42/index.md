---
HasBanner: false
draft: false
releaseDate: '2026-07-03'
section: project
sidebar: true
title: QGIS 4.2 の変更履歴
type: visual-changelog

---
{{<content-start >}}
# QGIS 4.2 の変更履歴{#changelog42 }
<img src="images/projects/b7fa0af07e61fe7036f463d15cbba685c11baae2.png" class="img-responsive img-rounded center-block" />

リリース日: 2026-07-03

[QGIS](https://qgis.org) (<https://qgis.org>) は、世界で最も広く使われている（オープンソースの）デスクトップ地理情報システム（GIS）です。世界中の人々が空間データの閲覧・編集・分析・共有に活用しています。プロ品質の地図作成物を作成でき、数百種類の空間データ形式をサポートしています。QGISは、空間プラットフォームへのアクセスを民主化するOSGeo財団のメンバープロジェクトです (<https://osgeo.org>)。

QGISのコアを最新のQt6フレームワークへ移行したメジャーバージョン4.0アップデートの堅固な基盤の上に構築された新しいメジャーリリース、QGIS 4.2の発表を喜んでお知らせします。このリリースには、3D機能とプロセッシングツールの複数の機能強化を含む、多数のパフォーマンス最適化と新たに導入された機能も含まれています。

今回のリリースで導入されたすべての新機能を手早く確認するには、 [YouTubeのハイライト動画](https://www.youtube.com/watch?v=5X1JKx7CXZY) をご覧ください。

[![](https://img.youtube.com/vi/5X1JKx7CXZY/0.jpg)](https://www.youtube.com/watch?v=5X1JKx7CXZY)

QGISはコミュニティの共同作業によって成り立っています。このリリースを実現するために時間と労力をボランティアで提供してくださった（あるいは他の方々の活動を支援してくださった）開発者、ドキュメント作成者、テスター、そして多くの皆様に心より感謝申し上げます。QGISコミュニティを代表して、このリリースをお楽しみいただければ幸いです！

時間や資金の寄付、またはその他の形でQGISをさらにすばらしいものにする活動に貢献したい方は、ぜひ [QGIS.ORG](https://qgis.org/) にアクセスしてご協力ください！

QGISは寄付者およびサステイニングメンバーによって支えられています。プロジェクトに大小を問わず財政的な貢献をしてくださった寄付者の最新リストは [寄付者一覧](https://qgis.org/en/site/about/sustaining_members.html#list-of-donors) でご覧いただけます。公式のプロジェクトサステイニングメンバーになることをご希望の方は、詳細について [サステイニングメンバーページ](https://qgis.org/en/site/about/sustaining_members.html) をご覧ください。QGISへのスポンサーシップは、定期的な開発者ミーティングの開催、プロジェクトインフラの維持、およびバグ修正活動の資金として活用されます。現在のスポンサーの完全なリストを以下に掲載します。すべてのスポンサーの皆様に心より感謝申し上げます！

QGISはフリーソフトウェアであり、使用にあたって料金を支払う義務は一切ありません。むしろ、経済的・社会的な立場に関わらず、世界中の多くの方々に使っていただけるよう積極的に推進しています。空間的な意思決定ツールを人々に提供することが、全人類にとってより良い社会の実現につながると信じているからです。
## Breaking Changes
### 機能:QGIS4の設定保存場所の移動とQGIS3からの自動移行
同一システム上のQGIS3とQGIS4の両方でユーザー設定に加えられた変更による設定ファイルの破損を防ぐため、QGIS 4の設定は別のディレクトリに完全に分離されるようになりました。<br />**注意:  これは自動インストールスクリプト、プロファイル管理、およびエンタープライズデプロイメントに影響します。**<br /> 初回起動時にQGIS4は既存のQGIS3パスからユーザープロファイルデータのコピーを実行し、設定を新しいQGIS4パスに複製します。自動デプロイメントとプロファイル管理スクリプトはこの新しい場所を対象とするよう更新する必要があります。これは報告された問題[\#61636](https://github.com/qgis/QGIS/issues/61636) and [\#60088](https://github.com/qgis/QGIS/issues/60088)を解決します。<br />以下の点に注意してください:
- これは一度限りの移行です
- 移行は読み込まれたユーザープロファイルの既存の設定をロスレスで保持します。
- その後のプロファイルの変更はQGIS3とQGIS4の間で同期されません。

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## ユーザーインタフェース
### 機能:スタイルの読み込みと保存のレイヤーメニューの追加
 **Styles**  サブメニューのレイヤーメニューに  **Load Style...** と **Save Style...**  オプションを直接追加します。これにより、別のインターフェースやメニューを開かずにレイヤーのスタイルを素早く読み込み/保存する方法がユーザーに提供されます。

<img src="images/entries/3649f31a4a1358779fd933bddce5e20161257fd9.png" class="img-responsive img-rounded" />

この機能は [Jan Caha](https://github.com/JanCaha) によって開発されました
## シンボロジ
### 機能:3Dシンボルのカテゴリ分類レンダラーの追加
カテゴリ分類とルールベースのレンダリングがQGIS 3Dシンボロジーで利用可能になりました。<br />両方の実装は2Dスタイリング用の既存のベクターレンダラーと同様であるため、ユーザーは3Dシーンで使い慣れたコントロールを持ちながら、この強力な機能セットをサポートするための複数のAPI拡張が適用されています。
 
 
 

<img src="images/entries/c5fb95c208d6bc03a05ac923f019475a50310cb6.png" class="img-responsive img-rounded" />

この機能は Stadt Frankfurt am Main の資金提供で開発されました

This feature was developed by [Jean Felder](https://github.com/ptitjano)
### 機能:テクスチャサポート付き物理ベースマテリアルの追加
完全なテクスチャマップサポートを持つ物理ベースマテリアルを公開する新しい3Dマテリアルタイプが追加されました。<br />テクスチャは以下のように指定できます:
- ベースカラー
- メタルネス
- ラフネス
- アンビエントオクルージョ

<img src="images/entries/ee3d3005794174302de3f65232c8cace82357987.png" class="img-responsive img-rounded" />

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能:ハッシュ/マーカーラインシンボルレイヤーへの始点と終点のトリム距離の追加
これにより、単純な線に対して既に存在する機能が、ハッシュやマーカーの線シンボルレイヤーにも拡張されます。

<img src="images/entries/bb0088d635bc91e52e14fec777c191861410d687" class="img-responsive img-rounded" />

この機能は Stadt Frankfurt am Main と Oslandia の資金提供で開発されました

This feature was developed by [Julien Cabieces](https://github.com/troopa81)
### 機能:メタルラフベース、放射カラーのデータ定義制御の追加
メタルラフベースと放射カラーのデータ定義制御が追加され、従来のPhongマテリアルと物理ベースマテリアルの間に残っている数少ない機能的なギャップの一つが埋められました。

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能:Phong/メタルラフテクスチャのスケール、回転、オフセットのデータ定義制御
メタルラフまたはPhongテクスチャーマテリアルを使用する際の3Dポリゴンのテクスチャスケール、回転、オフセットを制御するためのデータ定義制御が追加されました。

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能:メタルラフマテリアルへのオプションのソリッド放射カラーの追加
メタルラフマテリアルに新しい非デフォルトのソリッド放射カラー設定が追加され、放射の強度を制御するスピンボックスも追加されました。実際には、これによりシーンライティングの影響を受けないマテリアルを作成できます。<br />添付の画像は、この機能の効果を示すために、放射なしの暗いシーンライティング、100%の黄色放射、1000%の黄色放射の比較を示しています。

<img src="images/entries/260c863c37dddb6f738615df50851b8eb06185bf.png" class="img-responsive img-rounded" />

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能:メタルラフマテリアルへの不透明度サポートの追加
物理ベースレンダリングマテリアルが不透明度をサポートするようになり、古いPhongマテリアルの機能に近づきました。

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能:スタイルデータベースへの3Dマテリアル設定の追加
QGISがスタイルデータベース（およびスタイルマネージャーダイアログ）で3Dマテリアル設定を管理するサポートを含むようになりました。<br />ユーザーは3Dマテリアルのプリセットを作成し、他のスタイルオブジェクトと一緒に管理できます（タグ付け、お気に入りなどのメタデータも可能）。

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能:3Dポイントモデルシンボルの上方向/前方向軸の選択を可能に
モデルファイルが常にZ軸上方向、Y軸前方向の慣例で作成されていると仮定する代わりに、ユーザーが手動で前方と上方の軸を設定できる設定を公開します。<br />これにより、インターネットからダウンロードしたランダムなOBJファイルをQGISの3Dポイントシンボルとして使用しやすくなります。以前の回避策ではシンボルを手動で回転させる必要がありましたが、これにより他の3Dポイントシンボルで使用される回転/スケール値やデータ定義式の再利用が妨げられていました。

<img src="images/entries/70b6d2509f1fb98c8a582a95c7abe3d58c22066a.png" class="img-responsive img-rounded" />

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能:テンプレートラインシンボルレイヤーへの追加アイテムの追加
マーカー/ハッシュラインシンボルレイヤー用の新しいマーカー/ハッシュを作成、移動、回転、削除するツールが提供されるようになりました。<br />これらの新しいマーカーは元のマーカーと同じスタイル、選択または表示状態を共有します。<br />これは [QEP \#406](https://github.com/qgis/QGIS-Enhancement-Proposals/pull/356) の実装です。 

<img src="images/entries/ab98e9fb9b4fd3111e4329ec44cf60c777761fd6" class="img-responsive img-rounded" />

この機能は Stadt Frankfurt am Main と Oslandia\*\* の資金提供で開発されました

This feature was developed by [Julien Cabieces](https://github.com/troopa81)
## 三次元機能
### 機能:スカイボックスからの環境ライティングの生成
キューブマップスカイボックスが配置されている場合に、物理ベースマテリアルに新しい環境ライティング効果が追加されました。環境ライトはスカイボックステクスチャーから動的に計算されます。<br />これらの効果は、事前計算されたアイレディアンステクスチャーの必要性を避けてユーザーエクスペリエンスを簡素化するために、アイレディアンスの球面調和近似を使用します。<br />これはスカイボックスが使用されている場合（固定グラジェントではない）にのみ有効であり、必要に応じて無効にできます。

<img src="images/entries/80ed241c2adbea51749cc1d0d5d892ef17f7f6d6.png" class="img-responsive img-rounded" />

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能:3Dモデルのインスタンシングのサポート
3Dシンボルにインスタンシングサポートが追加されました。<br />新しいライブラリtinyobjloader https://github.com/tinyobjloader/tinyobjloade が導入されました<br />qgsobj3dutils（qgsgltf3dutils に類似）が作成され、OBJデータをジオメトリに読み込み、存在する場合はテクスチャーマテリアルを読み取り・作成します。<br />その他の変更:
- PhongTexturedMaterial が PhongおよびGoochと同様に setInstancingEnabled() を実装することでインスタンシングをサポートするようになりました。
- HighlightMaterial がコンストラクター呼び出しからtechniqueを削除するようにリファクタリングされ、フラグで setInstancingEnabled() も実装しました。これはまた、以前2Dで選択されたときに3Dビューで3Dモデルがハイライトされなかったバグも修正します。

"深淵を長く見つめるならば、深淵もまたあなたを見つめ返す"。

<img src="images/entries/71e571c0902c1d2a576fe09198e69dc0cb7d479f.png" class="img-responsive img-rounded" />

この機能は [Dominik Cindric](https://github.com/ViperMiniQ)によって開発されました
### 機能:3Dマップカラーグレーディング効果の制御を可能にしました
3Dシーンのトーンマッピング、露出調整、ガンマの新しい設定が公開されました。.<br />3Dマップの ”エフェクト" タブに新しい "カラーグレーディング" セクションが追加され、ユーザーがこれらのオプションを制御できます。これにより、ユーザーはシーンをよりドラマチックな色彩と高いコントラストでレンダリングするよう変更したり、夜間シーンで非常に明るい放射光を露出オーバーの光として表示するブルーム効果を使用したりすることができます。

<img src="images/entries/460ceb890c6261ddc51ce3659dde777121d649e5.png" class="img-responsive img-rounded" />

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能:オプションのライトブルーム効果
新しい物理ベースのライトブルーム効果が追加されました。これにより3Dマップの明るい部分にリアリスティックなブルームが与えられます。これにより、これらの領域が明るい色を持つだけでなく、実際に光を放っているように見えるようになり、3Dシーンをよりドラマチックに見せることができます。

<img src="images/entries/0c981146a38a83d08ffff1f8c49193662e5cf725.png" class="img-responsive img-rounded" />

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能:マルチサンプルアンチエイリアシング（MSAA）の追加
3Dマップでのマルチサンプルアンチエイリアシングの使用をトグルする新しいグローバル3D設定が提供されます。

<img src="images/entries/ca69a2e049f207e2a0a57f5c5d57b3420207605c.png" class="img-responsive img-rounded" />

この機能は [Dominik Cindric](https://github.com/ViperMiniQ)によって開発されました
### 機能:3Dシーンへのグラジェント背景の追加
QGISが3Dマップビューの背景効果として設定可能なグラジェントをサポートするようになり、テクスチャーなしでユーザーに効果的なカスタムスカイボックス効果を提供します。

<img src="images/entries/139a726cacbde4fdffaee78e66c974efbef509c3.png" class="img-responsive img-rounded" />

この機能は [Dominik Cindric](https://github.com/ViperMiniQ)によって開発されました
### 機能:3D Tiles:インスタンシングサポートの追加
3D Tilesのインスタンス化されたメッシュのサポートが追加され、ユーザーは樹木や街灯などの繰り返される3Dオブジェクトをさまざまな位置、回転、スケールで効率的に表示できるようになりました。この実装は3D Tiles 1.0と1.1の複雑な構造的差異を抽象化して、シームレスなレンダリングを提供します。
- 2Dおよび3Dマップビューの両方でサポートされています。
- 3DビューではGPUによる高効率のインスタンスレンダリングが活用されます。
- i3dmフォーマットを使用した3D Tiles 1.0をサポートします。
- glTF GPUインスタンシングを介した3D Tiles 1.1をサポートします。
- 投影座標系のタイル回転を自動的に修正します。
- 量子化された位置とoct符号化された回転は引き続きサポートされていません。
- 地物IDはこの実装では読み取られません。

<img src="images/entries/adb08002b421eee278c571fd52325e7e93251b69.png" class="img-responsive img-rounded" />

This feature was funded by Natural Resources Canada

This feature was developed by [Martin Dobias](https://github.com/wonder-sk)
### 機能:3D Tilesへの暗黙的タイリングの追加
3D Tiles 1.1標準で指定された暗黙的タイルのサポートが追加されました。この機能は構造化された細分化スキームを活用して、大規模な3Dデータセットの読み込みと解析の効率を向上させます。ロジックは新しい QgsCesiumImplicitTiling コアクラスを介して実行され、クワッドツリー細分化スキームが現在サポートされています（オクツリーサポートは将来の更新で可能になります）。<br />ロジックは新しい `QgsCesiumImplicitTiling` コアクラスを介して実行され、クワッドツリー細分化スキームが現在サポートされています（オクツリーサポートは将来の更新で可能になります）。

<img src="images/entries/3031b5c8facbd4e11ddd450b7314d92f9684c083.png" class="img-responsive img-rounded" />

This feature was developed by [Martin Dobias](https://github.com/wonder-sk)
### 機能:マップ座標で3Dカメラを制御するカメラコントロールダイアログの追加
3DマップCRS座標でXYZを見るカメラを制御し、ピッチ角、ヘディング角、中心点からの距離を設定するための新しいダイアログが提供されます。<br />ダイアログにはレイヤースタイリングパネルの動作を模倣した リアルタイム更新 ボタンが追加されます。有効にすると、ユーザーが変更した設定が自動的に3Dマップに反映されます。<br />これは3Dマップからの値の更新には影響しません。ユーザーがカメラを移動すると、リアルタイム更新 チェックボックスに関わらず、値がリアルタイムで更新されます。

<img src="images/entries/1f896ef8c6f67e8a925e31712a4c543525d8987c.png" class="img-responsive img-rounded" />

この機能は [Dominik Cindric](https://github.com/ViperMiniQ)によって開発されました
### 機能:3D複合タイル（"cmpt"）のサポートの追加
QGISが複数のタイル（b3dmやi3dmなど）を1つのファイルに結合する3D Tiles 1.0仕様の [複合タイル](https://github.com/CesiumGS/3d-tiles/blob/main/specification/TileFormats/Composite/README.adoc#tileformats-composite-composite) のサポートを含むようになりました。このサポートは2Dおよび3Dレンダリングの両方に含まれています。

<img src="images/entries/7196a54d0d5835b1cefa9efd8b4143c67130d5ab.png" class="img-responsive img-rounded" />

This feature was developed by [Martin Dobias](https://github.com/wonder-sk)
### 機能：3Dマップビューの "垂直軸を反転" 設定の改善
3DビューのY軸反転設定がQFlagベースの設定にリファクタリングされ、各ナビゲーションシナリオ（ウォークモードのドラッグ、ウォークモードのマウスキャプチャ、テレインモード）に独立したビットが割り当てられました。
- 設定はチェックボックスベースのコンボボックスからグローバルに編集できます。
- 反転Y設定のC++インターフェースが更新されました。
- Pythonインターフェースはダックタイピングにより引き続き互換性が維持されます。

<img src="images/entries/9ae04d9318d5c9662a84821de7c113ed1f48eb66.png" class="img-responsive img-rounded" />

この機能は [David Koňařík](https://github.com/dvdkon) によって開発されました
### 機能:3d stlエクスポート
QGISが既存の `OBJ`  エクスポート機能に加えて、3Dシーンを [STL](https://en.wikipedia.org/wiki/STL_(file_format))  形式でエクスポートするサポートを持つようになりました。`STL` 形式は `OBJ`  よりもはるかにシンプルで、テクスチャーを処理しません。

<img src="images/entries/e0e80d41fe495959ba786ad4261a947b766ac321.png" class="img-responsive img-rounded" />

この機能は Stadt Frankfurt am Main の資金提供で開発されました

This feature was developed by [Jean Felder](https://github.com/ptitjano)
## 点群
### 機能:VPC構築アルゴリズムへのオーバービュー長さオプションパラメーターの追加
VPC構築アルゴリズムに新しい `--overview-length` オプションパラメーターが追加されました。

This feature was developed by [Stefanos Natsis](https://github.com/uclaros)
### 機能:マルチオーバービューVPCファイルの読み取りサポートの追加
オーバービューアセットを "overview" IDで解析する代わりに、"overview" ロールに基づいて解析されるようになりました。<br />VPCファイルには任意のIDを持つアセットごとに複数のオーバービューが含まれる場合があります。"overview" ロールを持つすべてのアセットがオーバービューとして扱われ、ズームアウト時に読み込まれてレンダリングされます。<br />`QgsPointCloudLayer` と`QgsVirtualPointCloudProvider` に、単一ではなくすべてのオーバービューのリストを返す overviews() メソッドが追加されました。

This feature was developed by [Stefanos Natsis](https://github.com/uclaros)
### 機能:vpc-in-zip（.vpz）仮想ポイントクラウドフォーマットのサポートの追加
仮想ポイントクラウド（VPC）ファイルはかなり大きくなる可能性があり、ASCIIベースのJSON形式はサイズを小さく保つのにあまり役立ちません。<br />QGISがリモートの `.vpc` ファイルを読み取るための新しいサポートを活用すると、より小さいファイルサイズの必要性がより明らかになり、圧縮された `.vpc`  から構築された `.vpz` 形式のサポートが追加されました（圧縮された `.qgs` を提供する `.qgz`  QGISプロジェクトファイルに類似）。

This feature was developed by [Stefanos Natsis](https://github.com/uclaros)
### 機能:レイヤーごとの標高シェーディングの追加
QGISがポイントクラウドレイヤーに特化したレイヤーごとの標高シェーディングをサポートするようになりました。この機能はより細かい視覚的制御を提供し、グローバルな標高シェーディングがマップシーン全体に適用された場合に発生する可能性のあるブレンドとレンダリングのアーティファクトを回避します。
- 2Dシンボロジーの拡張GUIから制御されます。
- グローバルな標高シェーディングアーティファクトを完全にバイパスします。
- 異なるマップ要素の意図しないブレンドを防止します。

<img src="images/entries/41a69a819d5d1446c2bcf2ddfcc4319bdb3b9f39.png" class="img-responsive img-rounded" />

この機能は [Dominik Cindric](https://github.com/ViperMiniQ)によって開発されました
### 機能:式でのカラーオブジェクトへの算術演算子のサポート
QGISがポイントクラウドデータのカラーオブジェクトを式内で基本的な算術演算を使用して直接変更することをサポートするようになりました。これにより、カラーを基本コンポーネントに自動的に分割して各チャネルに数学的操作を適用することでダイナミックなカラー操作が簡素化され、複雑なコンポーネント抽出式の必要性がなくなります。 
- 算術演算は基礎となるRGBAチャネルに直接適用されます。
- 乗算はどちら側にカラーがあっても機能します。
 
 
 
- その他の演算はカラーを左側に必要とします。
- この機能は複雑なカラーコンポーネント抽出式を避けます。
- 属性に基づくダイナミックシェーディングが大幅に簡素化されます。

例:

`@point_color * scale_linear( @NumberOfReturns, 0, 8, 0.5, 1 )`

<img src="images/entries/d215e96ce1bf086ec558dbf3587894a22cc75af1.png" class="img-responsive img-rounded" />

この機能は [Dominik Cindric](https://github.com/ViperMiniQ)によって開発されました
### 機能:式によるレンダラーカラーの変更
ポイントクラウドレンダラーに色を調整するための式を使用できるようにする追加のモディファイアーが追加されました。<br />ポイントクラウドのすべての属性とレンダラーのベースカラーを式で使用できます。ユーザーはベースカラー値を強度などのポイントの別の属性と組み合わせて、ポイント分類とスタイリングのより良い結果を生成できます。<br />例えば:<br />`@point_color * (@intensity / 65535)`

この機能は [Dominik Cindric](https://github.com/ViperMiniQ)によって開発されました
## 印刷レイアウト
### 機能:ソースベクターレイヤーレンダラーからプロットデータとスタイリングを導出する新しいレイアウトチャートアイテム機能の追加
レイアウトチャートアイテムに新しい設定が追加されました:
- プロットシリーズのX軸をソースベクターレイヤーのレンダラーのカテゴリに一致させる 'レイヤーシンボロジーからカテゴリを生成する' トグル
- レンダリングされたチャートがベクターレイヤーのレンダラーに添付されたシンボルの色を引き継ぐ 'レイヤーシンボロジーの色を適用する' トグル

ユーザーは空白のシリーズを使用して一致する地物の数を *カウント* するか、カスタムY式（シンプルなフィールドまたは完全な式）を使用してカスタマイズされた合計（ラインの長さや合計できる値を参照する属性など）を算出することができます。

<img src="images/entries/ba82a958973bddc5c128c2b24c7cd249a81d737c.png" class="img-responsive img-rounded" />

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### 機能:シェイプベースのアイテムで画像アイテムをクリップする新しいオプションの追加
QGISがレイアウト画像アイテムをシェイプタイプのアイテムでクリップする機能を提供するようになりました。<br />これにより、クールなシェイプをフレームし、画像（アトラス地物属性によって動的に駆動されるか静的な画像ソースかを問わず）でマップ要素をマスクする素晴らしい方法が提供されます。<br />クリッピングは画像アイテムのプロパティパネルの新しいセクションで有効にして設定できます。

<img src="images/entries/08cbd88117433df3beb02050b1e690886b7ee27b.png" class="img-responsive img-rounded" />

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### 機能:ジオスペシャルPDFレイヤー管理の強化
ジオスペシャルPDFエクスポートがQGISレイヤーツリー設定（グループ、順序、名前、表示設定、グループレイヤー）に従えるようにする新しいオプションが追加されました。これにより、ユーザーはジオスペシャルPDFにエクスポートする際にネストされたグループを含むレイヤー構造を保持できます。この機能は印刷レイアウトでサポートされていますが、標準のマップレンダリングタスクではサポートされていません。
- この機能はロックされたレイヤーのないマップを必要とします。
- 表示されているレイヤーと非表示のレイヤーの両方がエクスポートされます。
- PDFはカスタム順序をレンダリングしながら標準ツリー構造を維持します。
- 地物属性はすべてのレイヤーでエクスポートされるか、まったくエクスポートされません。
- グループレイヤーは単一のマップレイヤーとしてサポートされています。
- 一致するPDFグループはレイアウトアイテムの表示設定を直接処理します。
- 一致しないPDFグループはツリーの下部に表示されます。
- 相互排他グループは現在サポートされていません。

<img src="images/entries/c4c92f09dc1381fac13768b1b52a192c9ed64eb8.png" class="img-responsive img-rounded" />

この機能は city of Bern の資金提供で開発されました

This feature was developed by [Germap](https://github.com/gacarrillor)
## 計算式
### 機能:scale_cubic_bezier式関数の追加とMapBoxスタイル変換時のベジェ三次補間の処理
既存の scale_linear、scale_exponential 関数を補完し、新しいベジェ三次ベースの補間メソッドを追加します。これはその後、"cubic-bezier" 補間タイプを使用してMapBoxスタイルを変換する際に使用されます。

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能:concat_ws式関数の追加
最初の引数を除くすべての引数を区切り文字で連結します。最初のパラメーターは区切り文字として使用されます。<br />NULL引数は無視されます。

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## データ管理
### 機能:属性テーブルヘッダーへの「フィールド計算機」メニューアイテムの追加
ベクターレイヤーの属性テーブルの列ヘッダーのコンテキストメニューに新しい "フィールド計算機" メニューアイテムが提供されます。<br />フィールド計算機ウィンドウは "既存のフィールドを更新" チェックボックスが自動的にチェックされ、対応するフィールドがコンボボックスにすでに選択された状態で開きます。<br />このアクションは編集可能なフィールドでのみ有効になります。

<img src="images/entries/8ade61ae18cd9ec8014958f35d175ed4e5d0ed4f.png" class="img-responsive img-rounded" />

This feature was developed by [Patrice Pineault](https://github.com/TurboGraphxBeige)
## プロセシング
### 機能:モデルの進行に応じて子ステップの地物数を動的に表示します
デザイナーダイアログからモデルが実行されると、QGISはモデルのリンクを流れる地物の更新されたカウントを表示するようになりました。これを実現するために、矢印に添付される新しい柔軟な　"バッジ" アイテムが導入されました。<br />注意:
- 矢印のバッジに地物数以外の出力も表示されるようになりました。例えば、別のアルゴリズムに添付された数値出力の値が表示されます（UIの乱雑さを避けるため、文字列は切りつめられます）。
- バッジが関連する矢印ラインの中間点の色を引き継ぐようになりました。
- パフォーマンス上の理由から、地物数の更新は100地物ごとに制限されています。
- すべてのアルゴリズムがダイナミックな地物数の進捗を報告するわけではないため（例：サードパーティプラグインベースのものは、プラグイン作者がこのためのアップグレードされたAPIを利用するまで報告しません）、QGISはモデル全体の実行が終了したときに常に正確な最終カウントで地物数を更新します。これらのモデルでは、ユーザーは子が実行される際ではなく、モデルの終了時に一度に矢印のカウントが更新されるのを見ることになります。

<img src="images/entries/e78e514a83f210185705a81bc6e1a8311bc025c0.png" class="img-responsive img-rounded" />

この機能は City of Canning によって資金提供されました

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能:面積しきい値パラメーターの追加
穴チェックプロセッシングツールに、ユーザーが返された結果をフィルタリングできるしきい値サイズが追加されました。穴の面積が指定したしきい値より大きい場合、その穴はエラーとして見なされません。

This feature was developed by [Jacky Volpes](https://github.com/Djedouas)
### 機能:中心軸アルゴリズムでのSFCGALエッジへの拡張パラメーターのサポートの追加
SFCGAL 2.3では、近似中心軸アルゴリズムに新しい `extendToEdges`  パラメーターが追加されました。このパラメーターを有効にすると、中心軸の端点が入力ポリゴンの境界まで延長されます。添付のメディアは、このオプションをfalse（赤）とtrue（緑）に設定してそれぞれ中心軸アルゴリズムを実行した場合の違いを示しています。

<img src="images/entries/d1cf8c4c5dd1ef1d172745817db02a6e2628191e.png" class="img-responsive img-rounded" />

この機能は Stadt Frankfurt am Main の資金提供で開発されました

This feature was developed by [Jean Felder](https://github.com/ptitjano)
### 機能:ユーザー定義メニューまたはツールバーへのプロセッシングの追加
ユーザーがプロセッシングアルゴリズムのアクションをユーザー定義のメニューまたはツールバーに追加できるようになりました。トリガーされると、これらのアクションは関連するプロセッシングアルゴリズムをパラメータ化して実行するためのダイアログを開きます。

<img src="images/entries/5ae9ce29dd7d2e8a7b094e3f7c129171af8a6d8f" class="img-responsive img-rounded" />

この機能は Stadt Frankfurt am Main と Oslandia の資金提供で開発されました

This feature was developed by [Julien Cabieces](https://github.com/troopa81)
### 機能:ランダムサブセットアルゴリズムのC++への移植
プロセッシングアルゴリズムのサブセット内でのランダム抽出とサブセット内でのランダム選択がPythonからC++に移植され、パフォーマンスが向上しました。
 
 
 

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
## アプリケーションとプロジェクトのオプション
### 機能:トポセントリック投影
QGISにトポセントリックCRSサポートが追加されました。ユーザーがCRS選択メニューからトポセントリックCRSオプションを明示的に選択すると有効になる投影の原点を設定するための新しいウィジェットが提供されます。

<img src="images/entries/405bc086bd84189e5113544155ac4ef7d85ed836.png" class="img-responsive img-rounded" />

この機能は [Dominik Cindric](https://github.com/ViperMiniQ)によって開発されました
## センサ
### 機能:Sensing、Sampling、Relations拡張を含むSensorThings 2.0のサポートの追加
 
 
 
QGISが新しいSensing、Sampling、Relations拡張を含むSensorThings 2.0仕様を利用するレイヤーのサポートを含むようになりました。<br />これはまたSensorThings 2.0対応サービスのこれらの選択も公開します。サービスのバージョンと拡張はブラウザーまたはデータソースマネージャーを介してサービスに接続する際に動的に決定されます。 

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Profile Plots
### 機能:3Dでの標高プロファイル曲線の表示
QGISがプロファイルプロット設定メニューに "3Dビューでプロファイルを表示" オプションを提供するようになり、3Dでの標高プロファイル曲線の表示が有効になります。<br />曲線は標高プロファイルから取得され、Z値は曲線内に収まるデータの計算された最小値と最大値のZ値から設定されます。<br />ポリゴンとラインのラバーバンドはカーソルに従い、ユーザーが現在標高プロファイルのどの位置にホバーしているかを表示します。

<img src="images/entries/51b9332232c56ecf122b5d6205744c01a2371e42.png" class="img-responsive img-rounded" />

この機能は [Dominik Cindric](https://github.com/ViperMiniQ)によって開発されました
## ブラウザ
### 機能:ブラウザーでのESRI RESTサービスの公開方法の改善
 
 
 
ブラウザーでのESRI RESTサービスコンテンツの整理を助けるための変更が加えられました:
- mapserver（ラスター）とfeatureserver（ベクター）の両方として公開された同じサービスの重複アイテムが非表示になりました。代わりにfeatureserverアイテムのみを表示し、ラスターとして読み込む機能をアイテムの右クリックコンテキストメニューに移動しました。これはArcProがこれらのサービスを公開する方法を模倣していますが、唯一の違いはArcProがベクターとしての読み込みのみを許可することです。サービスがクエリ機能を公開している場合、ラスターとして読み込む機能はありません。
- mapserverアイテムの "全レイヤー" 擬似レイヤーを表示しなくなりました。代わりに、この機能はマップサービスアイテムの右クリックコンテキストメニューに移動されました。これにより、サービスの実際のコンテンツに対応しないまれにしか使用されないアイテムでブラウザーのサービスコンテンツが乱雑にならないようにします。

この機能は République et canton de Genève の資金提供で開発されました

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## データプロバイダ
### 機能:マップ表示用FeatureServerプロバイダーの大幅な高速化
QGISがFeatureServerプロバイダーを使用してデータを取得するための大幅に高性能なリファクタリングアプローチを持つようになり、指定されたマップ範囲内の地物のサブセットを取得するために必要なリクエスト数が削減されました。<br />実際にサービスからすべての地物を取得するための合計リクエスト数は変わらないことに注意してください。例えば、属性テーブルを開くと同じ合計リクエスト数になります。

<img src="images/entries/e3ea1f5568a403cb6c293d963c0b04351df8ea21.png" class="img-responsive img-rounded" />

この機能は République et canton de Genève の資金提供で開発されました

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能:AFSおよびAMSプロバイダーの並列プロバイダー読み込みの有効化と関連する修正
QGISがArcGIS FeatureServer/MapServerプロバイダーの並列プロバイダー読み込みを有効にし、プロジェクトに複数のFeatureServer/MapServerレイヤーが含まれる場合のプロジェクト読み込み時間が大幅に短縮されました。

この機能は République et canton de Genève の資金提供で開発されました

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能:他のクラウド最適化データタイプとblobストアからのSTACアセットのサポート
 
 
 
QGISがAzureやGoogleなどの他のクラウドオブジェクトストアプロバイダーからのSTACアセットのサポートを追加しました。<br />Tこれにより、適切な cloud-optimized ラベルのmimetypeまたはサポートされたアセットタイプ宣言で公開されている場合に限り、GeoTiff以外のJPEG2000、TileDB、ポイントクラウドなどの他のクラウド最適化データタイプへのサポートも拡張されます。

この機能は [Norman Barker](https://github.com/normanb) によって開発されました
## QGISサーバー
### 機能:WMSパラメーターのHIGHLIGHT_LABELFRAMEオプションのサポー
WMSサービスの新しいパラメーターにより、ラベルのフレームスタイルプロパティの設定が可能になりました。以下が含まれます:
- `HIGHLIGHT_LABELFRAMEBACKGROUNDCOLOR`
- `HIGHLIGHT_LABELFRAMEOUTLINECOLOR`
- `HIGHLIGHT_LABELFRAMEOUTLINEWIDTH`
- `HIGHLIGHT_LABELFRAMESIZE`

例:

`&MAP0:HIGHLIGHT_LABELFRAMEBACKGROUNDCOLOR=%23FF0000`<br />`&MAP0:HIGHLIGHT_LABELFRAMEOUTLINECOLOR=%230000FF`<br />`&MAP0:HIGHLIGHT_LABELFRAMESIZE=5`<br />`&MAP0:HIGHLIGHT_LABELFRAMEOUTLINEWIDTH=2`

<img src="images/entries/e2ce00c7b18b3fbb012ee8e08e0def43db4959c5.png" class="img-responsive img-rounded" />

This feature was developed by [Sandro Mani](https://github.com/manisandro)
### 機能:FlatGeobuf OAPIFエクスポートと各種修正
 FlatGeobufエクスポートフォーマットが [QEP 414](https://github.com/qgis/QGIS-Enhancement-Proposals/blob/master/qep-414-server-oapif-jsonfg-flatgeobuf.md) に沿って実装され、QGIS Server OAPIFサービスに追加されました。

この機能は [QGIS user group Germany (QGIS Anwendergruppe Deutschland e.V.)](https://www.qgis.de/) の資金提供で開発されました

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
## プログラマビリティ
### 機能：ポリゴンの凹包機能の公開
QGISがGEOSのポリゴンの凹包アルゴリズムをサポートするようになり、PyQGISに公開されました。
1. 地物によるConcave Hullアルゴリズムにポリゴン（およびライン）地物の入力を許可します。以前は、ユーザーはポイントから凹包を計算するためにまずポリゴンから頂点を抽出する必要がありましたが、そのアプローチはポリゴンの内部を無視していました。
2. 専用の "ポリゴン間のギャップを埋める" アルゴリズムを追加します:

標準のConcave Hullアルゴリズムとは異なり、ポリゴンのConcave Hullは（場合によっては）すべての入力ポリゴンを含む非凸ポリゴンです。計算されたhullはポリゴンの内部と交差することなく、ポリゴン間のギャップを埋めます。入力ポリゴンの外側の境界に厳密に従い、元の形状を歪めることなくポリゴン間のギャップを埋めることができます。建物の輪郭グループの汎化、ブロック周辺の '地区' ポリゴンの作成、ギャップの削除や分離したポリゴンセットの結合などのケースに特に役立ちます。<br />詳細については https://lin-ear-th-inking.blogspot.com/2022/05/concave-hulls-of-polygons.html?m=1 を参照してください 

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## 注目すべき修正
### Feature: Bug fixes by Even Rouault (Spatialys)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| .ASC missing from Raster Extraction | [\#66319](https://github.com/qgis/QGIS/issues/66319) | [PR \#66368](https://github.com/qgis/QGIS/pull/66368) | N/A |
| \[OAPIF\] Zooming triggers download of already loaded data | [\#66358](https://github.com/qgis/QGIS/issues/66358) | バグではない |  |
| Gdb format in QGIS will show also .gdbtable .gdbtablex not only as .gdb | [\#66279](https://github.com/qgis/QGIS/issues/66279) | Not a bug / not desirable |  |
| Expose AZURE_STORAGE_SAS_TOKEN configuration option in Browser Cloud Storage Connection | [\#66274](https://github.com/qgis/QGIS/issues/66274) | [PR \#14731](https://github.com/OSGeo/gdal/pull/14731) | N/A |
| Filtering WFS causes total failure to display layer | [PR \#66373](https://github.com/qgis/QGIS/pull/66373) | [PR \#66373](https://github.com/qgis/QGIS/pull/66373) | [PR \#66373](https://github.com/qgis/QGIS/pull/66373) |
| \[OAPIF\]\[server\] Paging not working with format FlatGeobuf from QGIS Server | [\#66365](https://github.com/qgis/QGIS/issues/66365) | [PR \#66399](https://github.com/qgis/QGIS/pull/66399) | N/A |
| Gml to Gml- Conversion succeeded, input and output are not the same in QGIS | [\#66413](https://github.com/qgis/QGIS/issues/66413) | バグではない |  |
| No timeout for vsicurl layers when loading a project | [\#66496](https://github.com/qgis/QGIS/issues/66496) | [PR \#66510](https://github.com/qgis/QGIS/pull/66510) | [PR \#66539](https://github.com/qgis/QGIS/pull/66539) |
| Raster attribute table: convert empty DateTime as string coming from GDAL to NULL value | [\#66544](https://github.com/qgis/QGIS/issues/66544) | [PR \#66547](https://github.com/qgis/QGIS/pull/66547) | N/A |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Even Rouault (Spatialys)](https://www.spatialys.com/en/home/)
### Feature: Bug fixes by Denis Rouzaud (OPENGIS.ch)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| QgsSettings + QGIS4.ini + XYZ Tile provider = crash | [\#66424](https://github.com/qgis/QGIS/issues/66424) | [PR \#66450](https://github.com/qgis/QGIS/pull/66450) | N/A |
| Cannot load VT layer from style only from the dialog (works in browser) | not reported | [PR \#66500](https://github.com/qgis/QGIS/pull/66500) | TODO |
| "fix" every entry in relation reference widget is shown in italic | not reported | [PR \#66649](https://github.com/qgis/QGIS/pull/66649) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Denis Rouzaud (OPENGIS.ch)](http://opengis.ch/)
### Feature: Bug fixes by Alessandro Pasotti (QCooperative)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| \[OAPIF\] QGIS Server OGC API is detected as WFS 1.1 | [\#66362](https://github.com/qgis/QGIS/issues/66362) | [PR \#66369](https://github.com/qgis/QGIS/pull/66369) | N/A |
| \[OAPIF\] Changing feature format has no effect | [\#66359](https://github.com/qgis/QGIS/issues/66359) | [PR \#66386](https://github.com/qgis/QGIS/pull/66386) | N/A |
| represent_value not working | [\#66339](https://github.com/qgis/QGIS/issues/66339) | [PR \#66392](https://github.com/qgis/QGIS/pull/66392) | [PR \#66436](https://github.com/qgis/QGIS/pull/66436) |
| Remove &key=pk from memory layers tests | [\#66350](https://github.com/qgis/QGIS/issues/66350) | [PR \#66397](https://github.com/qgis/QGIS/pull/66397) | N/A |
| \[server\] Fix network cache settings read from environment | [\#59613](https://github.com/qgis/QGIS/issues/59613) | [PR \#66425](https://github.com/qgis/QGIS/pull/66425) | N/A |
| \[postgres\] Fix json/b bytea add feature in transaction group | [\#65323](https://github.com/qgis/QGIS/issues/65323) | [PR \#66478](https://github.com/qgis/QGIS/pull/66478) | N/A |
| Unable to load style from datasource database for non geometry layers. | [\#66341](https://github.com/qgis/QGIS/issues/66341) | [PR \#66486](https://github.com/qgis/QGIS/pull/66486) | N/A |
| \[expressions\] Fix IN operator nodes() | [\#66313](https://github.com/qgis/QGIS/issues/66313) | [PR \#66485](https://github.com/qgis/QGIS/pull/66485) | [PR \#66499](https://github.com/qgis/QGIS/pull/66499) |
| No timeout for vsicurl layers when loading a project | [\#66496](https://github.com/qgis/QGIS/issues/66496) | 再現できません |  |
| Field calculator allowed string \* float operation and program crashed | [\#66507](https://github.com/qgis/QGIS/issues/66507) | [PR \#66508](https://github.com/qgis/QGIS/pull/66508) | N/A |
| Calculating integer field by "id"=@row_number crashed QGIS on save action | [\#66268](https://github.com/qgis/QGIS/issues/66268) | [PR \#66508](https://github.com/qgis/QGIS/pull/66508) | N/A |
| Crash when attempting to load OpenHistoricalMap vector tiles | [\#66466](https://github.com/qgis/QGIS/issues/66466) | [PR \#66533](https://github.com/qgis/QGIS/pull/66533) | N/A |
| Data-defined override expression on a field is not evaluated until any field in the form is edited | [\#66504](https://github.com/qgis/QGIS/issues/66504) | 再現できません |  |
| Export to PostgreSQL (Available Connection) drops source table | [\#66228](https://github.com/qgis/QGIS/issues/66228) | [PR \#66536](https://github.com/qgis/QGIS/pull/66536) | [PR \#66570](https://github.com/qgis/QGIS/pull/66570) |
| Spatialite data types are not recognized correctly when creating query layers with SQL | [\#66329](https://github.com/qgis/QGIS/issues/66329) | [PR \#66538](https://github.com/qgis/QGIS/pull/66538) | N/A |
| Edit layer properties of an invalid layer (broken source) is not working | [\#66324](https://github.com/qgis/QGIS/issues/66324) | [PR \#66607](https://github.com/qgis/QGIS/pull/66607) | Not recommended |
| Qgis have problem to render GeometryCollection for Gml, other viewer like mygeodata website render ok | [\#66225](https://github.com/qgis/QGIS/issues/66225) | 重複 |  |
| 3.44.7-Solothurn Crashes on New Shapefile | [\#66220](https://github.com/qgis/QGIS/issues/66220) | [PR \#66609](https://github.com/qgis/QGIS/pull/66609) | [PR \#66648](https://github.com/qgis/QGIS/pull/66648) |
| Add inja escape() function to HTML escape values | [GHSA-cr49-pm9v-m788](https://github.com/qgis/QGIS/security/advisories/GHSA-cr49-pm9v-m788) | [PR \#66616](https://github.com/qgis/QGIS/pull/66616) | [PR \#66670](https://github.com/qgis/QGIS/pull/66670) |
| Regression with decimal values and negative number in color gradient in the layer style panel | [\#65566](https://github.com/qgis/QGIS/issues/65566) | [PR \#66619](https://github.com/qgis/QGIS/pull/66619) | [PR \#66671](https://github.com/qgis/QGIS/pull/66671) |
| QGIS Server: GetProjectSettings returns the error message "Layer(s) not valid" with two WMS layers | [\#65872](https://github.com/qgis/QGIS/issues/65872) | 再現できません |  |
| raster histogram not working for raster with scale factor | [\#65920](https://github.com/qgis/QGIS/issues/65920) | [PR \#66640](https://github.com/qgis/QGIS/pull/66640) | TODO |
| Advanced Digitizing Floater is not wide enough to show whole value | [\#65171](https://github.com/qgis/QGIS/issues/65171) | [PR \#66663](https://github.com/qgis/QGIS/pull/66663) | TODO |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Alessandro Pasotti (QCooperative)](https://www.qcooperative.net/)
### Feature: Bug fixes by Julien Cabieces (Oslandia)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| Custom Toolbar Position Loss | [\#65862](https://github.com/qgis/QGIS/issues/65862) | [PR \#66483](https://github.com/qgis/QGIS/pull/66483) | N/A |
| Export to PDF from layout changes colors | [\#42935](https://github.com/qgis/QGIS/issues/42935) | Not a bug (Was an Adobe issue IMHO) |  |
| Layout bleeding to edge outside map window | [\#49638](https://github.com/qgis/QGIS/issues/49638) | 一定 |  |
| Fix flaky test_gui_fileuploader | 未報告 | [PR \#66543](https://github.com/qgis/QGIS/pull/66543) |  |
| Hidden actions from user defined toolbar are still visible. | 未報告 | [PR \#66620](https://github.com/qgis/QGIS/pull/66620) |  |
| QGIS should never poll a PostGIS/WMS/WFS/etc connections unless specifically asked to | [\#58303](https://github.com/qgis/QGIS/issues/58303) | [PR \#66621](https://github.com/qgis/QGIS/pull/66621) | TODO |
| Password is not removed when it's at the the end of uri | 未報告 | [PR \#66625](https://github.com/qgis/QGIS/pull/66625) | TODO |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Julien Cabieces (Oslandia)](https://oslandia.com/en/)
### Feature: Bug fixes by Germán Carrillo (OPENGIS.ch)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| Allow QGIS to access curves from OGC API provider | 未報告 | [PR \#66452](https://github.com/qgis/QGIS/pull/66452) | N/A |
| Elevation profile - changing layer symbology crashes QGIS / Wrong rendering order of Elevation profile items after changing the color of a profile item / Elevation profile stops respecting layer order on layer properties change | [\#64952](https://github.com/qgis/QGIS/issues/64952), [\#62677](https://github.com/qgis/QGIS/issues/62677), [\#64806](https://github.com/qgis/QGIS/issues/64806) | [PR \#66360](https://github.com/qgis/QGIS/pull/66360) | N/A |
| QGIS crashes on registering a Custom Profile Source with 'Sync Layers to Project' active | [\#65056](https://github.com/qgis/QGIS/issues/65056) | [PR \#66455](https://github.com/qgis/QGIS/pull/66455) | N/A |
| QGIS hangs when opening raster calculator (Meu Qgis está travando ao tentar abrir a calculadora raster) | [\#66327](https://github.com/qgis/QGIS/issues/66327) | 再現できません |  |
| Ensure consistency in MultiCurves: don't allow NurbsCurves | 未報告 | [PR \#66676](https://github.com/qgis/QGIS/pull/66676) | N/A |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Germán Carrillo (OPENGIS.ch)](https://opengis.ch/)
### Feature: Bug fixes by David Signer (OPENGIS.ch)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fix field displayString on primitive JSON values | 未報告 | [PR \#66575](https://github.com/qgis/QGIS/pull/66575) | N/A |
| Fix bad behavior on widget detection of JSON fields | [\#62377](https://github.com/qgis/QGIS/issues/62377) | [PR \#66494](https://github.com/qgis/QGIS/pull/66494) | N/A |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [David Signer (OPENGIS.ch)](https://opengis.ch/)
### Feature: Bug fixes by Stefanos Natsis (Lutra Consulting)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| Windows QGIS 4 installs plugin with ACL that do not include SYSTEM or Administrators | [\#66515](https://github.com/qgis/QGIS/issues/66515) | [PR \#66576](https://github.com/qgis/QGIS/pull/66576) | N/A |
| Crash when clicking on an unavailable layer in Layers panel | [\#65913](https://github.com/qgis/QGIS/issues/65913) | [PR \#66578](https://github.com/qgis/QGIS/pull/66578) | TODO |
| QGIS server OGC API: Limits and offset parameters ignored when plugin changing parameters | [\#65858](https://github.com/qgis/QGIS/issues/65858) | 一定 | [PR \#66480](https://github.com/qgis/QGIS/pull/66480) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Stefanos Natsis (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Feature: Bug fixes by Loïc Bartoletti (Oslandia)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| Unbreak QGIS with GDAL \>= 3.13 | [commit ffdb8e3](https://github.com/qgis/QGIS/commit/ffdb8e3b27035478c533f37087505e749cc15b9b) | [PR \#66615](https://github.com/qgis/QGIS/pull/66615) | N/A |
| concat() returns NULL when all arguments are NULL: it should return an empty string | [\#65808](https://github.com/qgis/QGIS/issues/65808) | [PR \#66618](https://github.com/qgis/QGIS/pull/66618) | TODO |
| Remove all the parts in a geometry creates an empty geometry instead of NULL | [\#65453](https://github.com/qgis/QGIS/issues/65453) | WIP | TODO / Not recommended ? |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Loïc Bartoletti (Oslandia)](https://oslandia.com/en/)
### Feature: Bug fixes by Alexander Bruy (QCooperative)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| Deleted last series still visible in chart | [\#63466](https://github.com/qgis/QGIS/issues/63466) | 再現できません |  |
| Grey out "Use only features intersecting atlas features" for layout chart item if no atlas is activated | [\#65612](https://github.com/qgis/QGIS/issues/65612) | [PR \#66283](https://github.com/qgis/QGIS/pull/66283) | N/A |
| DBマネージャ | [\#59470](https://github.com/qgis/QGIS/issues/59470) | 再現できません |  |
| "Generate elevation profile image" algorithm doesn't propose image formats for output file | [\#64915](https://github.com/qgis/QGIS/issues/64915) | [PR \#66286](https://github.com/qgis/QGIS/pull/66286) | [PR \#66445](https://github.com/qgis/QGIS/pull/66445) |
| Ubuntu 23.04: /usr/lib/qgis/plugins/libplugin_grass8.so lib not loadable | [\#55159](https://github.com/qgis/QGIS/issues/55159) | Not a bug/feedback |  |
| Returned result of layer_property (layer, 'type') is dependent of UI language | [\#65009](https://github.com/qgis/QGIS/issues/65009) | [PR \#66300](https://github.com/qgis/QGIS/pull/66300) | [PR \#66446](https://github.com/qgis/QGIS/pull/66446) |
| Advanced digitizing floater should not allow editing every fields | [\#65173](https://github.com/qgis/QGIS/issues/65173) | [PR \#66303](https://github.com/qgis/QGIS/pull/66303) | [PR \#66447](https://github.com/qgis/QGIS/pull/66447) |
| Join attributes by location (summary) count returns Null | [\#40108](https://github.com/qgis/QGIS/issues/40108) | [PR \#66322](https://github.com/qgis/QGIS/pull/66322) | [PR \#66448](https://github.com/qgis/QGIS/pull/66448) |
| Qt6 porting: use size_t for qHash() return | [\#44351](https://github.com/qgis/QGIS/issues/44351) | [PR \#66477](https://github.com/qgis/QGIS/pull/66477) | N/A |
| Image source file chooser does not start in the program symbol library folder (Windows) | [\#37308](https://github.com/qgis/QGIS/issues/37308) | [PR \#66342](https://github.com/qgis/QGIS/pull/66342) | [PR \#66449](https://github.com/qgis/QGIS/pull/66449) |
| TestQgsProcessingAlgsPt2::exportMeshOnGrid() | [\#48605](https://github.com/qgis/QGIS/issues/48605) | 再現できません |  |
| TestQgsProcessingAlgs::convertGpsData() fails | [\#45588](https://github.com/qgis/QGIS/issues/45588) | Cannot reproduce/Not a bug |  |
| gdal:merge parameter OPTIONS not shown with execAlgorithmDialog | [\#66396](https://github.com/qgis/QGIS/issues/66396) | バグではない |  |
| projects/anonymize_saved_projects doesn't seem to be available in the new settings tree | [\#65844](https://github.com/qgis/QGIS/issues/65844) | バグではない |  |
| bug for .Shp namefile | [\#62655](https://github.com/qgis/QGIS/issues/62655) | バグではない |  |
| Build virtual point cloud (VPC): dialog adds .las extension for output | [\#61934](https://github.com/qgis/QGIS/issues/61934) | 再現できません |  |
| QGIS claims to be able to open all .jpg file (on Lubuntu) | [\#60911](https://github.com/qgis/QGIS/issues/60911) | [PR \#66472](https://github.com/qgis/QGIS/pull/66472) |  |
| QGIS wants to open all .json files, including ones unrelated to any geodata | [\#61215](https://github.com/qgis/QGIS/issues/61215) | 再現できません |  |
| Matrix distance does not output right fields when using N x T matrix type | [\#29165](https://github.com/qgis/QGIS/issues/29165) | [PR \#66101](https://github.com/qgis/QGIS/pull/66101) |  |
| Distance Matrix returns wrong record/result when using Linear Distance Matrix with k=1 | [\#45493](https://github.com/qgis/QGIS/issues/45493) | [PR \#66101](https://github.com/qgis/QGIS/pull/66101) |  |
| QLR files not associated with QGIS | [\#56844](https://github.com/qgis/QGIS/issues/56844) | 再現できません |  |
| TestQgsDatumTransformDialog fails | [\#48883](https://github.com/qgis/QGIS/issues/48883) | 再現できません |  |
| TestProcessingGui::testDatabaseSchemaWrapper() Caught unhandled exception | [\#48885](https://github.com/qgis/QGIS/issues/48885) | 再現できません |  |
| Layout arrow item has start marker in wrong direction | [\#59078](https://github.com/qgis/QGIS/issues/59078) | [PR \#66558](https://github.com/qgis/QGIS/pull/66558) |  |
| User Defined CRS gets lost | [\#57806](https://github.com/qgis/QGIS/issues/57806) | [PR \#66572](https://github.com/qgis/QGIS/pull/66572) |  |
| Raster Tools - Generate XYZ Tiles (Directory) always creates 0 tiles | [\#60069](https://github.com/qgis/QGIS/issues/60069) | バグではない |  |
| Error in counting tiles in each levels in Generate XYZ tiles (Directory) | [\#62157](https://github.com/qgis/QGIS/issues/62157) | [PR \#66606](https://github.com/qgis/QGIS/pull/66606) | N/A |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Alexander Bruy (QCooperative)](https://www.qcooperative.net/)
### Feature: Bug fixes by Nyall Dawson (North Road)
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fix deadlock when rendering annotation layers | 未報告 | [PR \#66712](https://github.com/qgis/QGIS/pull/66712) | [PR \#66742](https://github.com/qgis/QGIS/pull/66742) |
| Fix crashes in QgsFeatureListComboBox if layer is unloaded | 未報告 | [PR \#66697](https://github.com/qgis/QGIS/pull/66697) | [PR \#66708](https://github.com/qgis/QGIS/pull/66708) |
| Every entry in relation reference widget is shown in italic | 未報告 | [PR \#66649](https://github.com/qgis/QGIS/pull/66649) | Not appropriate |
| Fix buggy processing relief colors widget | 未報告 | [PR \#66602](https://github.com/qgis/QGIS/pull/66602) | Not appropriate |
| Fix QgsImageCache lossy conversion of images | 未報告 | [PR \#66585](https://github.com/qgis/QGIS/pull/66585) | Not appropriate |
| Fix crash when setting 3d skybox to non-square textures | [\#66560](https://github.com/qgis/QGIS/issues/66560) | [PR \#66580](https://github.com/qgis/QGIS/pull/66580) | N/A |
| Fix intermittent failure of GRASS raster tests | 未報告 | [PR \#66546](https://github.com/qgis/QGIS/pull/66546) | N/A |
| Fix symbology sizing issues on hidpi displays | [\#55349](https://github.com/qgis/QGIS/issues/55349) | [PR \#66531](https://github.com/qgis/QGIS/pull/66531) | Not appropriate |
| Fix symbology sizing issues on hidpi displays | [\#55349](https://github.com/qgis/QGIS/issues/55349) | [PR \#66530](https://github.com/qgis/QGIS/pull/66530) | Not appropriate |
| Fix broken color wheel widget on devices with pixel ratios | [\#55349](https://github.com/qgis/QGIS/issues/55349) | [PR \#66529](https://github.com/qgis/QGIS/pull/66529) | Not appropriate |
| Use correct lossless method to store metal rough colors | 未報告 | [PR \#66521](https://github.com/qgis/QGIS/pull/66521) | N/A |
| Ensure color picker opens inline for 3d settings in style dock | 未報告 | [PR \#66520](https://github.com/qgis/QGIS/pull/66520) | Not appropriate |
| Fix misalignment of spin boxes in color dialog | 未報告 | [PR \#66498](https://github.com/qgis/QGIS/pull/66498) | Not appropriate |
| Use unlit material instead of phong material when more appropriate | 未報告 | [PR \#66490](https://github.com/qgis/QGIS/pull/66490) | Not appropriate |
| Loosen the maximum number of grid ticks to draw | [\#45113](https://github.com/qgis/QGIS/issues/45113) | [PR \#66403](https://github.com/qgis/QGIS/pull/66403) | Not appropriate |
| Fixes malformed HTML metadata for postgres layers | Reported on mailing list | [PR \#66402](https://github.com/qgis/QGIS/pull/66402) | N/A - qt 6 only |
| Fix slow count of features for filtered SQL server layers | [\#64894](https://github.com/qgis/QGIS/issues/64894) | [PR \#66401](https://github.com/qgis/QGIS/pull/66401) | Not appropriate |
| Partially fix slow expression builder widget construction times | 未報告 | [PR \#66385](https://github.com/qgis/QGIS/pull/66385) | Not appropriate |
| Use correct default font for legend text on symbol | Related to [\#63431](https://github.com/qgis/QGIS/issues/63431) | [PR \#66384](https://github.com/qgis/QGIS/pull/66384) | Not appropriate |
| Don't show missing font warnings for MS Shell Dlg font | [\#63431](https://github.com/qgis/QGIS/issues/63431) | [PR \#66383](https://github.com/qgis/QGIS/pull/66383) | Not appropriate |
| Add explicit bool operator for QgsLayerTreeNode | [\#65755](https://github.com/qgis/QGIS/issues/65755) | [PR \#66381](https://github.com/qgis/QGIS/pull/66381) | QGIS 4 only |
| WMS Ensure we store deduced CRS in provider/layer sources | 未報告 | [PR \#66379](https://github.com/qgis/QGIS/pull/66379) | Not appropriate |
| Fix maximum word wrap for legend title/group/subgroup text | [\#66281](https://github.com/qgis/QGIS/issues/66281) | [PR \#66338](https://github.com/qgis/QGIS/pull/66338) |  |
| Fix model is zoomed right out when opening model designer | 未報告 | [PR \#66335](https://github.com/qgis/QGIS/pull/66335) | QGIS 4 only |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)

{{<content-end >}}
