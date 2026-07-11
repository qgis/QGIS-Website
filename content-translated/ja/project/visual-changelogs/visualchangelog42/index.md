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

[QGIS](https://qgis.org) (<https://qgis.org>) は、世界で最も広く使われている（オープンソースの）デスクトップ地理情報システム（GIS）です。世界中の人々が空間データの閲覧・編集・分析・共有に活用しています。プロ品質の地図作成物を作成でき、数百種類の空間データ形式をサポートしています。QGISは、空間プラットフォームへのアクセスを民主化するオープンソース地理空間財団OSGeoのメンバープロジェクトです (<https://osgeo.org>)。

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
完全なテクスチャマップサポートを持つ物理ベースマテリアルを公開する新しい3Dマテリアルタイプが追加されました。<br />Tテクスチャは以下のように指定できます:
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
### Feature: Add reading support for multi-overview VPC files
Instead of parsing overview assets by their "overview" id, they are now parsed based on their "overview" role.<br />VPC files may contain multiple overviews per asset with arbitrary ids. All assets with the "overview" role are now considered as overviews, loaded and rendered when zoomed out.<br />`QgsPointCloudLayer` and `QgsVirtualPointCloudProvider` now have an `overviews()` method returning a list of all overviews, instead of a single one.

This feature was developed by [Stefanos Natsis](https://github.com/uclaros)
### Feature: Add support for a vpc-in-zip (.vpz) virtual point cloud format
Virtual Point Cloud (VPC) files can become quite large, and the ASCII-based JSON format does not really help in keeping the size down.<br />Leveraging the new support for QGIS to read remote `.vpc` files, the need for a smaller file size is more apparent, and support for the `.vpz` format constructed from a zipped `.vpc` has been added (similar to the `.qgz` QGIS project files providing a zipped `.qgs`).

This feature was developed by [Stefanos Natsis](https://github.com/uclaros)
### Feature: Add per layer elevation shading
QGIS now supports per-layer elevation shading specifically for point cloud layers. This feature provides finer visual control, avoiding the blending and rendering artifacts that can occur when global elevation shading is applied across the entire map scene.
- Controlled via extended GUI in 2D symbology.
- Bypasses global elevation shading artifacts entirely.
- Prevents unwanted blending of distinct map elements.

<img src="images/entries/41a69a819d5d1446c2bcf2ddfcc4319bdb3b9f39.png" class="img-responsive img-rounded" />

この機能は [Dominik Cindric](https://github.com/ViperMiniQ)によって開発されました
### Feature: Support arithmetic operators on color objects in expressions
QGIS now supports modifying color objects on Point Cloud data directly within expressions, using basic arithmetic operations. This simplifies dynamic color manipulation by automatically splitting the color into its base components and applying the mathematical operation to each channel, eliminating the need for complex component extraction formulas.
- Arithmetic operations apply directly to underlying RGBA channels.
- Multiplication works with the color on either side.
- Other operations require the color on the left.
- This feature avoids complex color component extraction formulas.
- Dynamic shading based on attributes is greatly simplified.

For Example:

`@point_color * scale_linear( @NumberOfReturns, 0, 8, 0.5, 1 )`

<img src="images/entries/d215e96ce1bf086ec558dbf3587894a22cc75af1.png" class="img-responsive img-rounded" />

この機能は [Dominik Cindric](https://github.com/ViperMiniQ)によって開発されました
### Feature: Modify renderer color by expression
An additional modifier has been added to the point cloud renderer that makes it possible to use expressions to for adjusting colors.<br />All point cloud attributes can be used in the expression, as well as the base color of the renderer. Users can combine the base color value with another attribute of the point, such as intensity, to produce a better result for point classification and styling.<br />For example:<br />`@point_color * (@intensity / 65535)`

この機能は [Dominik Cindric](https://github.com/ViperMiniQ)によって開発されました
## 印刷レイアウト
### Feature: Add new layout chart item functionality to derive plot data and styling from the source vector layer renderer
New settings have been added to the layout chart items:
- a 'generate categories from the layer symbology' toggle to have the plot series' X axis match categories from the source vector layer's renderer
- an 'apply layer symbology colors' toggle to have the rendered charts take on the colors of the symbol attached to the vector layer's renderer

The user can either rely on a blank series to *count* the number of matching features, or can rely on a custom Y expression (a simple field or a full-fledged expression) to come up with a customized sum (say length of lines, or an attribute referring to a value that can be summed, etc.)

<img src="images/entries/ba82a958973bddc5c128c2b24c7cd249a81d737c.png" class="img-responsive img-rounded" />

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### Feature: Add new option to clip a picture item by a shape-based item
QGIS now provides the ability to clip a layout picture item by a shape-typed item.<br />This provides a fantastic way to frame cool shapes and mask elements with images (whether dynamically driven by an atlas feature attribute or a static image source).<br />The clipping is enabled and configured inside a new section of the picture item properties panel.

<img src="images/entries/08cbd88117433df3beb02050b1e690886b7ee27b.png" class="img-responsive img-rounded" />

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### Feature: Geospatial PDF layer management enhancement
New options have been added to allow Geospatial PDF Exports to follow the QGIS layer tree configuration (groups, order, names, visibility, group layers). This allows users to preserve the layer structure, including nested groups, when exporting to a Geospatial PDF. This functionality is supported in print layouts, but not in standard map rendering tasks.
- The feature requires a map without locked layers.
- Both visible and invisible project layers are exported.
- PDFs render custom orders while keeping standard tree structures.
- Feature attributes are exported for all layers or none.
- Group layers are supported as single map layers.
- Matching PDF groups handle layout item visibility directly.
- Unmatched PDF groups appear at the tree bottom.
- Mutually exclusive groups are currently not supported.

<img src="images/entries/c4c92f09dc1381fac13768b1b52a192c9ed64eb8.png" class="img-responsive img-rounded" />

This feature was funded by the city of Bern

This feature was developed by [Germap](https://github.com/gacarrillor)
## 計算式
### Feature: Add scale_cubic_bezier expression function, handle bezier-cubic interpolation when converting MapBox styles
Complements the existing scale_linear, scale_exponential functions and adds a new bezier-cubic based interpolation method. This is then used when converting MapBox styles using the "cubic-bezier" interpolation type.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Add concat_ws expression function
Concatenate all but the first arguments with separators. The first parameter is used as a separator.<br />NULL arguments are ignored.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## データ管理
### Feature: Adding "Field Calculator" menu item to the attribute table header
A new "Field Calculator" menu item is provided in the context menu of column headers in a vector layer's attribute table.<br />The Field Calculator window will open with "Update existing field" checkbox automatically checked and the corresponding field already selected in the combo box.<br />The action is only enabled on editable fields.

<img src="images/entries/8ade61ae18cd9ec8014958f35d175ed4e5d0ed4f.png" class="img-responsive img-rounded" />

This feature was developed by [Patrice Pineault](https://github.com/TurboGraphxBeige)
## プロセシング
### Feature: Dynamically show child step feature counts as model progresses
As the model is run through the designer dialog, QGIS will now show an updated count of features flowing through the model links. To achieve this, a new flexible "badge" item that is attached to arrows was introduced.<br />Note:
- We now also show non-feature count outputs in the badges for arrows, so, e.g., the value of numeric outputs attached to another algorithm will be shown. (To avoid cluttered UI, strings are truncated.)
- Badges now inherit the midpoint color of their associated arrow lines.
- For performance reasons, the feature count updates are limited to only every 100 features.
- Since not all algorithms report dynamic feature count progress (e.g., third-party plugin-based ones won't, at least until the plugin author utilises the upgraded API for this), QGIS will always update the feature counts with their exact final counts when the whole model finishes executing. For those models, the user will see the arrow's count updated in one go at the end of the model, not as that child executes.

<img src="images/entries/e78e514a83f210185705a81bc6e1a8311bc025c0.png" class="img-responsive img-rounded" />

この機能は City of Canning によって資金提供されました

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Add an area threshold parameter
The check holes processing tool now includes a threshold size which allows users to filter the returned results. If the hole area is higher than the provided threshold, then the hole is not considered an error.

This feature was developed by [Jacky Volpes](https://github.com/Djedouas)
### Feature: Add support for the SFCGAL extend to edges parameter in medial axis algorithm
With SFCGAL 2.3, the approximate media axis algorithm has a new `extendToEdges` parameter. If this parameter is activated, the medial axis endpoints are extended to the input polygon boundary. The attached media illustrates the difference between running the medial axis algorithm with this option set to false (red) and true (green), respectively.

<img src="images/entries/d1cf8c4c5dd1ef1d172745817db02a6e2628191e.png" class="img-responsive img-rounded" />

この機能は Stadt Frankfurt am Main の資金提供で開発されました

This feature was developed by [Jean Felder](https://github.com/ptitjano)
### Feature: Add processing in user defined menu or toolbar
Users can now add a processing algorithm action to a user-defined menu or toolbar. When triggered, those actions will open a dialog to parametrize and execute the associated processing algorithm.

<img src="images/entries/5ae9ce29dd7d2e8a7b094e3f7c129171af8a6d8f" class="img-responsive img-rounded" />

この機能は Stadt Frankfurt am Main と Oslandia の資金提供で開発されました

This feature was developed by [Julien Cabieces](https://github.com/troopa81)
### Feature: Random subset algorithms ported to C++
The Processing algorithms Random extract within subsets and Random selection within subsets have been ported from Python to C++, providing enhanced performance.

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
## アプリケーションとプロジェクトのオプション
### Feature: Topocentric projection
Topocentric CRS support has been added to QGIS, with a new widget provided for setting the point of origin of the projection, which is enabled when users explicitly select a Topocentric CRS option from the CRS selection menu.

<img src="images/entries/405bc086bd84189e5113544155ac4ef7d85ed836.png" class="img-responsive img-rounded" />

この機能は [Dominik Cindric](https://github.com/ViperMiniQ)によって開発されました
## センサ
### Feature: Add support for SensorThings 2.0, including Sensing, Sampling and Relations extensions
QGIS now includes support for layers utilising SensorThings 2.0 specifications, including the new Sensing, Sampling and Relations extensions.<br />This also exposes these choices for SensorThings 2.0-enabled services. The service version and extensions are determined dynamically when connecting to a service via the browser or data source manager.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Profile Plots
### Feature: Display elevation profile curve in 3D
QGIS now provides a "Show Profile in 3D Views" option in the profile plot settings menu, which enables the display of the elevation profile curve in 3D.<br />The curve is retrieved from the elevation profile, and Z values are set from the calculated min and max Z values of the data that fit within the curve.<br />Polygon and line rubberbands follow the cursor to display over what position in the elevation profile the user is currently hovering over.

<img src="images/entries/51b9332232c56ecf122b5d6205744c01a2371e42.png" class="img-responsive img-rounded" />

この機能は [Dominik Cindric](https://github.com/ViperMiniQ)によって開発されました
## ブラウザ
### Feature: Rework how ESRI REST services are exposed in the browser
Changes have been made to help de-clutter ESRI REST service content in the browser:
- The duplicate items for the same service exposed as both mapserver (raster) and featureserver (vector) are now hidden. Instead, only show the feature server item, and move the ability to load as a raster to the right-click context menu on the item. This mimics how ArcPro exposes these services, with the exception that it ONLY allows loading them as vectors. There's no capability to load as a raster when the service exposes the query capability.
- We no longer show the "All layers" pseudo layer for mapserver items. Instead, this functionality was moved to the right-click context menu for the map service item. This avoids cluttering up the service contents in the browser with rarely used items that don't correspond to the actual contents of the service.

This feature was funded by République et canton de Genève

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## データプロバイダ
### Feature: Greatly speed up the FeatureServer provider for map viewing
QGIS has a significantly more performant refactored approach to fetching data using the FeatureServer Provider, which trims down the number of requests required to fetch a subset of the features within a given map extent.<br />Note that the actual TOTAL number of requests to get EVERY feature from the service doesn't change, so, for example, opening the attribute table would result in the same total number of requests.

<img src="images/entries/e3ea1f5568a403cb6c293d963c0b04351df8ea21.png" class="img-responsive img-rounded" />

This feature was funded by République et canton de Genève

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Enable parallel provider load for AFS, AMS providers, and some related fixes
QGIS has enabled parallel provider loading for the ArcGIS FeatureServer/MapServer providers, giving much faster project load times when a project contains multiple FeatureServer/MapServer layers.

This feature was funded by République et canton de Genève

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Support STAC assets from other cloud optimized data types and blob stores
QGIS has added support for STAC assets from other cloud object-store providers, including Azure and Google.<br />This additionally extends support to other cloud-optimized data types beyond GeoTiff, such as. JPEG2000, TileDB, Point Clouds, and others provided they are published with an appropriate `cloud-optimized` labelled mimetype or a supported asset type declaration.

This feature was developed by [Norman Barker](https://github.com/normanb)
## QGISサーバー
### Feature: Add support for HIGHLIGHT_LABELFRAME options WMS params
New parameters for WMS services allow for the configuration of frame style properties on labels, including:
- `HIGHLIGHT_LABELFRAMEBACKGROUNDCOLOR`
- `HIGHLIGHT_LABELFRAMEOUTLINECOLOR`
- `HIGHLIGHT_LABELFRAMEOUTLINEWIDTH`
- `HIGHLIGHT_LABELFRAMESIZE`

For Example:

`&MAP0:HIGHLIGHT_LABELFRAMEBACKGROUNDCOLOR=%23FF0000`<br />`&MAP0:HIGHLIGHT_LABELFRAMEOUTLINECOLOR=%230000FF`<br />`&MAP0:HIGHLIGHT_LABELFRAMESIZE=5`<br />`&MAP0:HIGHLIGHT_LABELFRAMEOUTLINEWIDTH=2`

<img src="images/entries/e2ce00c7b18b3fbb012ee8e08e0def43db4959c5.png" class="img-responsive img-rounded" />

This feature was developed by [Sandro Mani](https://github.com/manisandro)
### Feature: FlatGeobuf OAPIF export plus various fixes
The FlatGeobuf export format has been added to the QGIS Server OAPIF service, implemented in line with [QEP 414](https://github.com/qgis/QGIS-Enhancement-Proposals/blob/master/qep-414-server-oapif-jsonfg-flatgeobuf.md)

This feature was funded by [QGIS user group Germany (QGIS Anwendergruppe Deutschland e.V.)](https://www.qgis.de/)

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
## プログラマビリティ
### Feature: Expose concave hull of polygons functionality
QGIS now supports the Concave Hull of Polygons algorithm from GEOS, which has been exposed in PyQGIS.
1. Allows polygon (and line) feature input for the Concave Hull by Feature algorithm. Previously, a user would have to first extract vertices from the polygon to calculate the concave hull from the points, but that approach ignores the interior of the polygon.
2. Adds a dedicated "Fill gaps between polygons" algorithm:

Unlike the standard Concave Hull algorithm, a Concave Hull of Polygons is a (possibly) non-convex polygon containing all the input polygons. The computed hull fills the gaps between the polygons without intersecting their interiors. It strictly follows the outer boundaries of the input polygons, allowing you to fill gaps between them without distorting their original shapes. It is particularly useful for cases such as generalizing groups of building outlines, creating 'district' polygons around blocks, or removing gaps and joining disjoint sets of polygons.<br />See https://lin-ear-th-inking.blogspot.com/2022/05/concave-hulls-of-polygons.html?m=1 for more details

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

{{<content-end >}}
