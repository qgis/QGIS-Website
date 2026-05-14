---
HasBanner: false
draft: false
releaseDate: '2021-10-22'
section: project
sidebar: true
title: QGIS 3.22の変更履歴
type: visual-changelog

---
{{<content-start >}}
# QGIS 3.22の変更履歴{#changelog322 }
![image1](images/projects/badbeb89221e014ed31e7ea07919c9e734df39b2.png)

リリース日: 2021-10-22

QGIS 3.22 Białowieża is aimed at celebrating the 100-year anniversary of [Białowieża National Park](https://en.wikipedia.org/wiki/Bia%C5%82owie%C5%BCa_National_Park), Poland, which was established in 1921. [Białowieża Forest](https://en.wikipedia.org/wiki/Bia%C5%82owie%C5%BCa_Forest) is one of the world's last primary woodlands, located on the border between Poland and Belarus. It is one of the few natural old-growth forests in temperate lowland Europe and has been protected for over 600 years. The outstanding value of Białowieża Forest has been acknowledged by its recognition as a [UNESCO Natural World Heritage Site](https://whc.unesco.org/en/list/33).

Białowieża Forest is named after the village Białowieża, which is located right in the middle of this woodland. It is one of the oldest settlements in the area, nowadays hosting numerous research and tourism activities. Today, there are three research institutions in the village: [Białowieża Geobotanical Station, University of Warsaw](https://bsg.bialowieza.pl/en/), [The Mammal Research Institute, Polish Academy of Sciences](https://ibs.bialowieza.pl/en/), and the [Forest Research Institute, Department of Natural Forests](https://www.ibles.pl/en/web/guest/home). Additionally, a large number of scientists from Poland and abroad travel to Białowieża in order to carry out their studies, and as such, there are also other users of QGIS in the area, as well as additional projects which contribute to the Open Data and Open Source Software ecosystems, such as the [Open Forest Data](https://openforestdata.pl/) project.

You can learn more about the project and this release of QGIS at the dedicated project website, <https://qgisbialowieza.pl>.

This feature-packed release includes a vast number of user experience enhancements and controls added to various advanced functionalities. In addition to a host of additional mesh functionality and operational improvements, QGIS Desktop now includes annotation tools and support for annotation layers, amongst much, much more. For a whirlwind tour of all the new functionalities introduced, you can view the highlight reel video at <https://youtu.be/U-RHBt6WZi8>

We would also like to extend a big thank you to the developers, documenters, testers, and all the many folks out there who volunteer their time and effort (or fund people to do so) to make these releases possible. From the QGIS community, we hope you enjoy this release! If you wish to donate time, money, or otherwise get involved in making QGIS more awesome, please wander along to [QGIS.ORG](https://www.qgis.org/) and lend a hand!

QGIS is supported by donors and sustaining members. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list]({{< ref "/funding/donate/donors.md" >}}). If you would like to become an official project sustaining member, please visit our [sustaining member page]({{< ref "/funding/membership.md" >}}) for details. Sponsoring QGIS helps us to fund our regular developer meetings, maintain project infrastructure, and fund bug fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

{{<fund type="active" >}}

QGIS はフリーのソフトウェアです。利用する上で金銭を支払う義務はありません。実際、私たちは利用者の財政状況や社会的地位にかかわらず、より多くの人に QGIS を利用して欲しいと思っています。私たちは地理空間的な意思決定ツールによって人々が力を持つことが、全人類の社会をより良くすると信じています。

{{<table-of-contents >}}
## 注記
### 機能：注記レイヤの性質と効果
注記レイヤの追加プロパティには、以下が含まれるようになります:
- 注記レイヤのプロパティウィンドウには、レイヤに関する基本情報や、レイヤのスケール範囲、不透明度、ブレンドモード、および描画効果の設定オプションが含まれています
- An option to view the main annotation layer\'s properties via the annotation toolbar (the main annotation layer is the hidden layer which is always present above all other map layers, so it\'s impossible to open it\'s property window via the layer tree)
- Options to set an annotation layer\'s opacity/blend mode/paint effect in the layer styling dock for interactive changes

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 地物: 注記アイテムのノードを編集する
注記の編集ツールは、既存のノードをクリックして移動することで、注記アイテム内のノードを編集するために使用できます。ユーザーの操作は、以下のように標準のQGISのパターンに従います：
- 左クリックで移動を開始します
- ２度目の左クリックで変更を適用します
- 右クリックで取り消します
- ノードを選択しデリートを押すとそのノードを取り除きます
- セグメントをダブルクリックするとノードを追加します

![image2](images/entries/4510afc65b63bab4ab46e0408a6c4c4207aff40f.gif)

この機能は Swiss QGIS user group によって資金提供されました。

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能: 選択した注記をカーソルキーで移動します
注記アイテムを選択すると、カーソルキーを押してそれを移動することができます。

この機能には、レイアウトアイテムと同じ相互作用のパターンでキーボードショートカットを使用する機能が含まれています:
- `shift + cursor`: Big movement
- `alt + cursor`: 1px movement

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能: ライン/ポリゴンの注記アイテムツールを作成する
注記ツールに新しいラインとポリゴンの注記アイテムを作成するための機能が追加されました。

これらは、ベクタ地物の描画と同じインタラクションをサポートしており、スナップ、トレース、CADドック、頂点を削除するバックスペース、曲線およびストリームのデジタイズモードなどがあります。

この機能は QGISスイスユーザーグループによって資金提供されました

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能: 新しいポイントテキストツール
マップツールにフレームワークが作られ、新しい注記アイテムを作成することができます。新しいポイントテキスト注記アイテムを作成する機能も備わっています。

![image3](images/entries/4822b0a64c8a57a049ae15acb8c77a27709172d5.gif)

この機能はスイスQGISユーザーグループによって資金提供されました

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能：注記ツールバー
新しい注記ツールバーが追加され、以下のアクションを提供します:
- 現在のプロジェクトに新しい空の注記レイヤを作ります。
- The \"Modify Annotations\" tool, which provides an interface for editing existing annotations.

注記を修正機能が対応する操作は次のようなものです:
- 既存の注記をクリックして選択すると、レイヤスタイルドックにそのプロパティが表示されます。これには、シンボル、参照スケール、Zインデックスなどが含まれます
- 選択した注記アイテムを移動するには、左クリックしてください。移動を取り消すには、右クリックまたはエスケープキーを押します。2回目の左クリックで移動を確定します。
- 注記が選択されている間に削除キーを押すと、その注記が削除されます

この機能はスイスQGISユーザーグループによって資金提供されました

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## ツール
### Feature: Add a \"measure bearing\" map tool
This tool behaves similarly to the existing \"measure angle\" map tool, but requires the user only to click two points on the map and displays the bearing between these points.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## ユーザーインタフェース
### 機能: 複数選択されたレイヤの編集モードの切り替え
The *toggle editing* action has been modified to support activation on all selected layers, making it easy to start and stop editing sessions across multiple layers simultaneously. Although the editing session status for all selected layers may not be the same, all selected layers will be toggled to an active or inactive state as the inverse of the current state of the currently active layer. This functionality is applied to the menu item *Layer \> Toggle Editing*, the *Toggle Editing* button on the digitizing toolbar, and the *Toggle Editing* entry in the layers context menu.

This feature was developed by [Stefanos Natsis](https://github.com/uclaros)
### 機能: レイヤグループと選択された全てのレイヤの情報を表示する
Whilst the identify features tool supported multiple selection modes, the \"current layer\" mode has been extended to support the selection of layer groups, and will identify features from all selected layers. Only features from visible layers within a layer group will be identified.

This feature was developed by [Stefanos Natsis](https://github.com/uclaros)
### Feature: Add a \'Show in Files\' action for all file items in browser
ファイルエクスプローラウィンドウを開いてそのファイルを直接選択します

Also fixes the existing \"File Properties\" action so that it shows regardless of the file type, and doesn\'t show incorrectly in some circumstances.

![image4](images/entries/f80090adb3c2f85fa81b5689741afd936f8d5439.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## シンボロジ
### 機能: ジオメトリジェネレータシンボルレイヤのカスタム単位
ジオメトリジェネレータは、ジオメトリを返す際に使用する単位を、レイヤのCRSで定義された単位のみをサポートするのではなく、選択できるオプションを公開しています。これは、レイアウトアイテムで使用される場合など、シンボルがレイヤに関連付けられていない場合に特に便利です。

このアップデートは、以下の単位の選択肢を提供します:
- 地図の単位（デフォルト、以前の動作）
- ミリメートル
- ピクセル
- インチ（Inches）
- ポイント（Points）

When millimeters, pixels, inches or points are selected, then the \@map_geometry variable will be available for use within the expression, containing the feature geometry in the specified units (relative to the map frame), whilst the \$geometry variable remains available within the expression in the layer CRS map units.

![image5](images/entries/d1c6b0c69cf9dd8247d1dc0e370d0182b550f48a.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能: ベクタレイヤのシンボロジ参照スケール
ベクタレイヤの地物シンボロジの参照スケールの設定ができるオプションが公開されました。

実際には、これにより、設定されたシンボロジとラベルのサイズが、ミリメートルやポイントなどの紙ベースの単位で参照される、関連した地図の縮尺が定義されます。これらの単位サイズは、関連参照スケールと現在のマップビューの縮尺の比率に基づいて自動的にスケーリングされます。

例えば、ラインレイヤが1:2000の参照スケールで2mm幅の線を使用するように設定されている場合、地物は、1:1000の地図の縮尺では4mm幅の線で、1:4000の地図の縮尺では1mmでレンダリングされます。

この機能は North Road, thanks to SLYR によって資金提供されました

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能: ラスタレンダリングの色反転フィルタオプション
新しい色反転オプションを介してレンダリングされるラスタの色を反転することができるようになりました。これは様々な場面で便利です。たとえば、明るいラスタのベースマップを、新しいラスタデータセットを作成する必要なく、簡単に暗いベースマップに変換することができます。

![image6](images/entries/0fc6bce9e9240b7e354b84d7477439798fd64a59.gif)

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
## ラベリング
### 機能: データ定義されたラベルの回転の単位を指定
データ定義型のラベルの回転のための角度単位を指定

![image](images/entries/126294292-06c91bd5-83d2-4d6f-88a2-38fa2d303c86.webp)

![Peek 2021-08-29 14-38](images/entries/131250678-52360214-31a9-4cf9-ad84-b10a4f78c431.gif)

This feature was developed by [Damiano Lombardi](https://github.com/domi4484)
## メッシュ
### 機能: 新しいメッシュレイヤを作成
QGISは新しいメッシュレイヤの作成に対応するようになります。

メッシュの作成は、次の作成形式に対応しています:
- 新しい空のメッシュレイヤ
- プロジェクト内の既存のメッシュに基づいた新しいメッシュフレーム
- ファイルの既存メッシュに基づいた新しいメッシュフレーム

![image9](images/entries/8ba4033bf4f8eea7e3776db420b34d6c51358859.gif)

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### 機能: メッシュフレームの編集
QGISは、メッシュフレームの編集に対応するようになり、メッシュの一貫性を確保する機能と、編集操作の元に戻すおよびやり直す機能を提供しています。

This introduces the `QgsMeshEditor` class to the QGIS Python API, which allows for performing edit operations, and the QgsTopologicalMesh class which is not exposed to the Python API but is used for ensuring that edited mesh elements remain topologically correct and perform data modifications.

![image10](images/entries/71bed70b1ced3fef5e3b8190cc613f3cb60f0fac.gif)

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### 機能: メッシュフレームの編集ライフサイクル
This feature has been introduced in the scope of [QEP 228](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/228) which outlines the introduction of Mesh Editing tools, implements changes to the User Interface, and exposes new functionality to the API.

メッシュフレームの編集は、ベクタレイヤと同様に、開始、確定、ロールバック、キャンセルなどの編集ライフサイクル操作の完全な機能セットに対応するようになりました。

![image11](images/entries/9463f4559796ff4808fcd05d1ffbec3aa6d6bae4.gif)

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### 機能: メッシュマップの編集ツール
This feature has been introduced in the scope of [QEP 228](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/228) which outlines the introduction of Mesh Editing tools.

メッシュ編集マップツールは次の操作に対応するようになります:
- 頂点／ 面を追加
- 頂点／ 面を選択
- 頂点／ 面を削除
- 頂点のZ値を変更
- 頂点を移動
- 辺と相互作用
- 面を分割

![image12](images/entries/ce164b754aff6438bb6db52a4d5c2eb3e103af62.gif)

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### 機能: 高度なメッシュ編集の拡張
This feature has been introduced in the scope of [QEP 228](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/228) which outlines the introduction of Mesh Editing tools, implements changes to the User Interface, and exposes new functionality to the API.

QGISユーザーインタフェースは、メッシュレイヤから頂点及び/又は面が選択されたとき、マップのコンテキストメニューからアクセス可能なドロネー三角形分割と面の改良機能を提供します。これらのオプションは、さらなる機能が導入された後に、メッシュツールバーのボタンに移行する可能性があります。

![mapToolrefine](images/entries/125721486-055c4cc3-5309-4455-bc5c-e00d6f349bc4.gif)

QGIS APIは、新しいインタフェース抽象クラスQgsMeshAdvancedEditingによって導入された、メッシュの高度な編集をサポートするためにも拡張されました。このクラスの派生クラスは、メッシュに追加するための面の生成、多くの面や頂点に対する特定の操作など、メッシュ上でいくつかの高度な編集を実装することができます。高度な編集は、QgsMeshAdvancedEditingのインスタンスをQgsmeshEditorのインスタンスに渡すことで行われ、他の編集操作と同様に編集が適用されます。

この機能には、2つの高度な編集機能が実装されています:
- ドロネー三角分割
- 面の改良

![image14](images/entries/a914bfb8a85bf2ab2232e8bfad6c3af3cdd751cb.gif)

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### 機能: 編集可能なメッシュ要素をポリゴンで選択
メッシュ編集を行う際に、デジタイズした領域内のメッシュ要素を選択することができるようになりました。ポリゴンの各頂点は左クリックでデジタイズされ、右クリックでポリゴンを完成させ、正しいことを確認し、交差するメッシュ要素（面と頂点）が選択されます。バックスペースキーを使って最後の頂点を削除でき、エスケープキーを使うと、ユーザーは通常のデジタイズモードに戻ることができます。

この機能は、次のように異なる選択述語を持つ2つの動作モードをサポートしています:
- 接触している要素（デフォルト）、または部分的に含まれる/交差する要素が選択されます（緑のラバーバンド）。
- 含まれている、または完全に含まれている要素が選択されます（青いラバーバンド）。

![image15](images/entries/6a687b260a4d3a41c432360336393ee2746997c8.gif)

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### 機能: メッシュ要素を既存のジオメトリで選択
既存のベクタレイヤに存在するジオメトリからメッシュ要素を選択するための2つのアクションが追加されました。

ベクタレイヤのジオメトリを選択した後、これらのツールを使用して、接触しているまたは含んでいる述語を使用してメッシュ要素を選択することができます。

![image16](images/entries/4a918fc1feabd7e3c68282b1b6d052c8504d6013.gif)

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### 機能: メッシュ要素を式で選択
An interface has been created for selecting mesh elements by expression during mesh editing. In addition, a contextual expression function `$face_area` has been added that returns the area of a mesh face.

![image17](images/entries/141acf32014c3ce387ff61e39cabf3e04c6d3896.gif)

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### 機能: 単一の頂点を変換
新しいメッシュ変形ツールの編集モードでは、単一の選択された頂点の座標をインポートすることができます。

「メッシュの頂点を変型」ウィンドウの右上にあるツールボタンは、このモードを切り替え、単一の頂点が選択されるたびに、頂点座標を調整するために使用できるフィールドが自動的に表示されます。

![image18](images/entries/2148b3024a51a218bafafbbe26f74c30692222f6.gif)

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Feature: Reindex/ renumber mesh layer
Users are now able to reindex (or renumber) the vertices and faces of a mesh layer during editing. The renumbering is an optimization of the mesh with the Cuthill-McKee algorithm.

![image19](images/entries/5da7e6705568488c08fbf7faaf311b2eca46c9da.gif)

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Feature: Force mesh by polylines
When editing mesh features, users can now transform features by forcing them to conform to a surface defined by existing polylines, or break lines. Faces are forced to follow the break lines, that is, edges of encountered faces have to be on these lines. Users may select break line geometries and then use the dedicated button to transform intersecting mesh elements.

Options provided for the transform include:
- Adding new vertices when the lines cut the internal edges
- Interpolating the Z value of newly added vertices on the mesh or from the lines
- Tolerance setting for shifting existing vertices into place and preventing the creation of new vertices along line within the specified distance

![forceByBreakLine](images/entries/132239197-096d733b-b519-4aab-9384-79724fd84331.gif)

Whilst the term \"break lines\" is typically used to refer to polylines that constrain a surface or TIN to the defined positions, these break lines are often components of the mesh itself, and additional operations would continue to constrain the surface to these lines. This functionality specifically transforms the surface in a static manner, so that future operations are not constrained to the lines used to transform the mesh elements.

![image21](images/entries/704c731583ce48d963fe9878177bc40639ae3078.webp)

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### 機能: 式によるメッシュの変形
User can perform geometrical transformations on a mesh using an expression to change the vertices\' coordinates. All coordinates (X,Y,Z) of selected vertices can be calculated with an expression, allowing transformation of the mesh while the mesh is still valid.

With a valid expression, selecting the \"Preview transform\" option will calculate the new expression based mesh coordinates and identify whether the transform is valid and may be applied.

If the preview is green, the transformed mesh is valid and the user can apply the transformation. If the preview is red, the transformed mesh is invalid and user cannot apply the transformation.

Once applied, users have the option to undo or redo the operation.

![image22](images/entries/04937a2d9bba1e27712351f52e6b6f4d5fc0be4d.gif)

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
## レンダリング
### Feature: Allow using physical DPI for map canvas
A new setting has been made available for correctly using the physical screen DPI instead of logical DPI, allowing symbols to be rendered equally on different attached devices (hi dpi and low dpi), and in mobile applications such as QField.

This setting is disabled by default to ensure that symbols are not scaled differently than they were in previous versions of QGIS.

This feature was developed by [Matthias Kuhn](https://github.com/m-kuhn)
### Feature: Data defined raster layer opacity
A new control has been exposed which allows the opacity of a raster to be data defined. This allows for the varied representation of a raster layer, in various contexts, such as on different pages of an atlas, being dependent on the visibility of another layer, or adjusted by temporal variables etc.

Additionally, a \"redraw layer only\" temporal mode for raster layers has been added, which causes a raster layer to be redrawn on each new animation frame as in the equivalent functionality for vector layers. This may be useful in many contexts, such as when the layer uses time-based expression values like the data defined renderer opacity to fade in or out a raster layer from an animation.

![image23](images/entries/881acd52afafba75698f1d7668794b80b594baef.gif)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## 印刷レイアウト
### Feature: Predefined scale support for point-driven atlases
Layout map items gained support for the predefined scale mode when controlled by point-driven atlases. This ensures the correct behavior is observed when atlas features are multipoint geometries with varying envelope areas.

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
### Feature: Indentation of legend groups and subgroups
Two new entries have been added to the \"Spacing\" section of the Legend properties:
- グループアイテムのインデント
- サブグループのインデント

Items belonging to groups or subgroups will be shifted right by the specified amount. When legend patches are added to the left of entries they will be indented as well.

![image24](images/entries/3792e9ae5124b81f1b4289cab220fdbb237851a8.webp)

This feature was developed by [Jürnjakob Dugge](https://github.com/jdugge)
## 計算式
### Feature: Mesh expression functions for vertex_as_point and vertex_z
Expressions have been added for interacting with mesh layers, with the following functions returning value related to the current vertex:
- `$vertex_as_point`: returns the current vertex as a geometry point
- `$vertex_z`: returns the Z value of the current vertex.

These two functions are contextual and need to be added in a `QgsExpressionContext` with `QgsExpressionContextUtils::meshExpressionScope()` for the creation of a specific `QgsExpressionScope`.

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Feature: Expression function for \$z
The z value for the current feature in an expression context can now be retrieved using `$z`

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Feature: Affine transform expression
An affine_transform function has been added to QGIS Expressions.

This feature was developed by [Antoine Facchini](https://github.com/Koyaani)
### Feature: Straight distance2d expression
A straight_distance2d function is now available in QGIS expressions for retrieving the direct/ Euclidean distance between the first and last vertex of a curve geometry feature.

This feature was developed by [Antoine Facchini](https://github.com/Koyaani)
### Feature: Add sinuosity expression
A sinuosity function has been added to QGIS expressions.

This feature was developed by [Loïc Bartoletti](https://github.com/lbartoletti)
### Feature: New exif() and exif_geotag() functions
A new pair of functions was added to the QGIS expression engine to read exif tags from image files. The two functions are:
- exif(path, tag) : this function returns the value of a given tag string for the provided image file path; when the second optional parameter isn\'t provided, the function will return a map object containing *all* exif tags and their values.
- exif_geotag(path) : this function returns a point geometry from the exif geotags containing in the provided image file path.

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
## デジタイズ
### Feature: Geometry snapper algorithm optimization
The geometry snapper is now blazingly fast after benefiting from another round of optimization work. Small snapping distance values hanging QGIS forever is now a thing of the past.

This feature was funded by [SwissTierras Colombia](https://www.swisstierrascolombia.com/)

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
### Feature: Convert to curve with vertex tool
The ability to convert vertices to or from curved vertices is now supported with the Vertex tool, allowing users to convert vertices with the \"C\" and \"O\" keys.

Additionally, methods for `convertVertex()` have been introduced for the `QgsGeometry` and `QgsCompoundCurve` objects in the QGIS API.

![image25](images/entries/fcc006352c7b09e37d6d8511ecb7fe2ae6a8be50.gif)

This feature was funded by [Swiss QGIS user group](https://qgis.ch/)

This feature was developed by [Olivier Dalang](https://github.com/olivierdalang)
### Feature: Add Z/M support to Advanced Digitizing
The QGIS Advanced Digitizing tools now support the entering of user-defined Z and M values, greatly improving the available control for newly digitized features such as components of 3D networks.

![image26](images/entries/287d041be909700393995e3018fba76f41e09a67.gif)

This feature was funded by Métropole Européenne de Lille \@Jean-Roc

This feature was developed by [Loïc Bartoletti](https://github.com/lbartoletti)
## データ管理
### Feature: Drag and Drop support for external storage file widget
Users may now use Drag and Drop support on an external resource widget when an external storage has been defined and configured appropriately.

![image27](images/entries/038bb187a174a4c491f3f2db6ef03cec5b75e43d.gif)

This feature was funded by [Lille Metropole](https://www.lillemetropole.fr/)

This feature was developed by [Julien Cabieces](https://github.com/troopa81)
### Feature: File-based dataset size and last modified date in the layer properties dialog
The layer properties dialog\'s information panel now shows the size and last modified date of file-based datasets, removing the need to retrieve these details from a file manager. These additional details are also visible in the browser panel\'s information section. For datasets formed of more than a single file, the size will reflect the sum of all the auxiliary/ sidecar files forming the dataset.

![image28](images/entries/10c72ab958bb1e7a59f8f81afb81d33780ed0834.webp)

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
### Feature: Rename files in QGIS Browser
A rename action has been added to the manage submenu for files in the QGIS browser. If the renamed file corresponds to a spatial dataset with multiple auxiliary/ sidecar files, then these will be renamed accordingly.

Additionally, users are warned if the file is a layer which exists in the current project and are asked whether they want to automatically update all the layer paths accordingly.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Move GPS tools \"add gpx layer\" functionality to Data Source Manager
Functionality from the GPS tools plugin to add GPX layers has been moved to a new \"Add GPS Data\" page in the data source manager.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Load projects from GPKG using drag and drop
Historically, when using drag and drop functionality with the GPKG format, only feature layers were represented to load into QGIS.

QGIS will now show projects embedded in a GPKG when the GPKG file is added to the QGIS canvas using the drag and drop functionality.

![image29](images/entries/3672e8bb8d50bf1593252343da8fd8ff78a46535.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能: 外部ストレージのサポート
QGIS now includes an External Storage API, in line with the proposal outlined in [QEP 196](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/196).

The implementation includes the following features:
- 外部ストレージAPI
- Registry that contains all external storage backends
- SimpleCopy external storage that stores the selected external resource on a specific location on disk
- WebDAVのサポート

In addition, a widget has been added to allow for the configuration and visualization of external storage backends and components. The storage mode (File or Directory) widget is not currently visible when an external storage is selected, and relative path settings are hidden as relative paths are not relevant to external storage data.

![image30](images/entries/c16663cabec529b113bb73919141bf50bf142c9e.gif)

This feature was funded by [Lille Metropole](https://www.lillemetropole.fr/)

This feature was developed by [Julien Cabieces](https://github.com/troopa81)
## フォームとウィジェット
### Feature: Drag & Drop designer form actions
Layer actions are now available in forms using the drag and drop designer

![image31](images/entries/d8af279071ac38fdc63fbd3980077155db39bd0f.gif)

This feature was funded by [Kanton Solothurn, Amt für Geoinformation](https://geo.so.ch/)

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
## レイヤ凡例
### Feature: Use placeholder icon in legend for raster layers
A new feature has been added to allow the selection of a placeholder image which may be used in the legend item of a raster or vector layer. This is very useful in certain instances such as when using raster layers with QGIS server, preventing long lists of palleted values from GetLegendGraphic requests and instead returning a tailored result, among various other use cases.

![image32](images/entries/f06524b9f422ee1ced55d9d79b816cabc5ea212d.webp)

This feature was funded by [Canton of Glarus](https://www.gl.ch/verwaltung/bau-und-umwelt/hochbau/raumentwicklung-und-geoinformation/geoportal-kanton-glarus.html/808)

This feature was developed by [mhugent](https://github.com/mhugent)
## 分析ツール
### 機能: ラスタ計算機に if() 関数を追加
A long awaited feature has been for QGIS to support simple if() statements in the raster calculator.

Although conditional statements have been supported in the raster calculator for a while, the syntax and structure of the expressions was often verbose and complex.

The raster calculator will now support simple conditional statements with the common syntax of `if ( condition , option1 , option2 )` whereby if the condition evaluates to true, the first option will be used, otherwise the second option will be used.

![image33](images/entries/c5d6968380879133ddb31ab2d0f755d6d2048402.gif)

This feature was developed by [Francesco Bursi](https://github.com/Franc-Brs)
### 機能: ラスタ計算機で仮想ラスタをサポート
Virtual raster data provider support has been added to the QGIS raster calculator, which now allows users to perform raster calculator operations without specifying an output file or writing the resulting raster to disk.

This option is enabled via the UI by checking the \"Create on-the-fly raster instead of writing layer to disk\" checkbox in the raster calculator, and is also supported via the PyQgis API.

Resulting raster layers may be used in further analysis operations and allow for user specified raster names. Where a name is not provided for the resulting raster, it will be named according to the formula used to generate it.

![image34](images/entries/844b2b463a26d035fe25d43d7221a24a570ac615.gif)

This feature was developed by [Francesco Bursi](https://github.com/Franc-Brs)
## プロセシング
### 機能: プロセシング用の注記レイヤパラメータ型
An annotation layer parameter type has been added to the QGIS Processing Framework, which includes a new algorithm for converting main annotation layer items to secondary annotation layers. This is useful for moving items created in the main layer to a secondary layer, so that the item placement can be adjusted within the layer stack.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### 機能: FileDownloaderプロセシングアルゴリズムへPOSTオプションを追加
Add a choice between performing GET or POST requests when downloading a file using the FileDownloader processing tool.

If the POST parameter is specified, some DATA can be added in the query.

This is useful in many contexts, such as for sending longer requests to the Overpass API using POST to download OSM data.

![image35](images/entries/89bee20177cb03e453300ae291ae879649e963ab.webp)

This feature was funded by [3Liz](https://www.3liz.com)

This feature was developed by [Étienne Trimaille](https://github.com/Gustry)
### Feature: Add new \"Select within distance\" and \"Extract within distance\" algorithms
New algorithms have been provided which allow users to select or extract features from one layer which are within a certain distance of features from another reference layer.

The distance checking is heavily optimized, using spatial indices to restrict the number of features retrieved, and also automatically handling off the check to the database server for layers using the PostGIS provider.

Additionally, the distance parameter may be a data-defined. property

この機能は QTIBIA Engineering によって資金提供されました

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Point cloud parameter for Processing
A new point cloud parameter has been added to the QGIS Processing. Framework. this allows for the filtering of point cloud layers in the map layer and multiple layers parameters. This opens the door for native point cloud algorithms and improves point cloud support for 3rd party providers.

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
### Feature: Remove the GPS importer plugin
The last of the GPS tools functionality has been ported to three new processing algorithms, namely:
- GPSデータを変換
- GPSデータをデバイスへアップロード
- デバイスからGPSデータをダウンロード

As a result, the GPS importer plugin has been made redundant and has been completely removed from QGIS.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Convert GPX feature type processing algorithm
The Convert GPX feature type tool has been ported from the GPS tools to a new processing algorithm, which uses the GPSBabel tool to convert GPX features from one type to another (e.g. converting all waypoint features to a route feature).

It is designed as a drop-in replacement for workflows which previously used this functionality from the GPS tools plugin, but with all the benefits and improvements that come automatically from being a part of of the QGIS Processing Framework.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Add incremental field with modulo option
This algorithm allows the user to add a column with an integer that will be incremented from START to the limit, with the possibility of grouping to resume at the value of START following the group.

An option called \"modulo counter\" is included which will reset the counter to the starting value if the modulo value is reached. Using a value of 0 for the modulo option will disable it.

This feature was developed by [Loïc Bartoletti](https://github.com/lbartoletti)
### Feature: Duration parameter
A brand new duration parameter was added to the processing framework to facilitate the creation of temporal-related algorithms.

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
### Feature: Spatiotemporal ST-DBSCAN clustering algorithm
QGIS 3.22 ships with a brand new spatiotemporal ST-DBSCAN clustering algorithm which clusters point features based on a 2D implementation of spatiotemporal density-based clustering of applications with noise (ST-DBSCAN) algorithm.

For more details, please see the following papers:
- Ester, M., H. P. Kriegel, J. Sander, and X. Xu, \"A Density-Based Algorithm for Discovering Clusters in Large Spatial Databases with Noise\". In: Proceedings of the 2nd International Conference on Knowledge Discovery and Data Mining, Portland, OR, AAAI Press, pp. 226-231. 1996
- Birant, Derya, and Alp Kut. \"ST-DBSCAN: An algorithm for clustering spatial--temporal data.\" Data & Knowledge Engineering 60.1 (2007): 208-221.
- Peca, I., Fuchs, G., Vrotsou, K., Andrienko, N. V., & Andrienko, G. L. (2012). Scalable Cluster Analysis of Spatial Events. In EuroVA@ EuroVis.

![image36](images/entries/10136b7563df169c40e2c20a96fe75b6ed93e16f.webp)

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
### Feature: Move non-native processing providers into independent plugins
In line with the discussion in [QEP 226](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/226), the SAGA, GRASS, and OTB providers have been separated into independent plugins.

This should prevent issues with the loading of the Processing plugin in cases where any one of these providers is broken. It will also make it easier to convert them into third-party plugins in the future.

The SAGA and GRASS plugins are enabled by default, leaving the UX unchanged. The OTB provider can be enabled in the Plugin Manager if necessary, however, the enabling or disabling of any of these providers is now performed via the Plugin Manager as with any other plugin.

This is mostly an internal change, with the only visible change on the part of end-users being that the Plugin Manager is used to activate or deactivate the SAGA, GRASS, and OTB providers.

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
## アプリケーションとプロジェクトのオプション
### Feature: Export all keyboard shortcuts to XML or PDF
Historically, when exporting keyboard shortcuts to an XML file, QGIS would only export user-defined shortcuts. In instances where no customized shortcuts were found, an empty file would be created.

A new option has been provided to export all available keyboard shortcuts to the resulting XML file, or to generate a PDF output with a list of all defined QGIS shortcuts.

![image37](images/entries/1822a5ace82d1e8030ed3d563c07f6b9b6fc3901.webp)

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
### Feature: Move GPS Tools GPSbabel device configuration widget to global settings
The GPS babel configuration settings has been moved from a settings page in the deprecated GPS Tools plugin, to a new page in the main settings dialog.

![image38](images/entries/d61c12a455d85b290431d5ff461de15db0afb446.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Set default path structure for new projects
QGIS Desktop historically supported the definition of whether a particular project used an absolute or relative structure from the project properties, however, the default setting for this functionality was always configured to use relative paths.

A new setting has been exposed which allows users to set the default path structure to use either absolute or relative for new projects under the program options. In much the same way the default project format may be configured to use qgz or qgs, this is made available as a global property specific to each user profile.

This feature was developed by [mhugent](https://github.com/mhugent)
### Feature: Allow configuration of the max cache size from QGIS settings
In the `qgis_global_settings.ini` file, it\'s possible to set the max image cache size in bytes.

The cache is used for caching symbology and layout images, If high resolution images are used for printing layout, then this value should be increased accordingly.

Default value is 100mb.

This feature was funded by [3Liz](https://www.3liz.com/)

This feature was developed by [David Marteau](https://github.com/dmarteau)
## ブラウザ
### Feature: Improved delete action for browser files
The delete action used from the QGIS browser has been improved in various ways, including:
- The action is more consistent and applied to all file type items
- Multiple file deletion is now supported by selecting multiple file items in the browser which includes a confirmation prompt
- Before deleting files, the current project is scanned to see if it is using any of the files. If so, a prompt is shown asking users if they want to cancel the deletion, or delete and remove layers, or delete and retain layers.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Connections API result widget
As a part of the ongoing efforts to port the table management functionalities from the DB Manager to the QGIS Browser, as detailed in [QEP 205](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/205), a new SQL dialog is available from the browser panel which provides the ability to execute queries and SQL statements for the following elements:
- DB connections
- Schema items
- Table items

The implementation also supports the following advanced functionalities:
- A multi-threaded implementation for both API token fetching and row fetching results in non-blocking GUI operations
- Fully interruptible API
- Support for progressive loading of features in the results view (fetchMore API)

![image39](images/entries/a4d260146fe4267a34d9db97495df2b244f5d7ff.gif)

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
## データプロバイダ
### Feature: Transactions in MSSQL provider
Addition of transaction support to the MSSQL data provider.

There are no GUI-related changes, as users can enable transactional editing as with other providers. This is done by going to the Project Properties and checking \"Automatically create transaction groups where possible\" in the Data Sources tab.

By default, a running transaction in MSSQL will block other clients from accessing the same data. For example, if one client starts a transaction and adds or modifies a feature in a table, other clients will get blocked when trying to read any data from the table until the transaction is completed.

There is database-level configuration option, `READ_COMMITTED_SNAPSHOT`, which is `OFF` by default.

Activating this will change the behavior to function in a similar fashion as other RDBMS systems such as PostgreSQL, in that transactions do not cause blocking and enables the database to support multiple versions of data. This is a database-level property configured by the administrator and can not be automatically set by QGIS when connecting to the database, however it may be activated using the following query:
``` sql
ALTER DATABASE my_db SET READ_COMMITTED_SNAPSHOT ON
```
In most instances where transactions are desired, activating this option is likely recommended to prevent freezing in QGIS or other clients.

This feature was funded by [ms.GIS](http://www.msgis.com)

This feature was developed by [Lutra Consulting (Martin Dobias)](https://www.lutraconsulting.co.uk/)
### Feature: Show system and internal tables in sublayer selection
A check box has been added to the sublayer selection dialog to control whether system and internal tables should be shown. This will be turned off by default, but will be useful in instances where users have a particular need to load a system table into QGIS for viewing or manipulation purposes.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Automatically read and convert metadata from ESRI Personal Geodatabases
Previously this was supported for File Geodatabases and shp.xml metadata, but it is now also supported for ESRI personal geodatabases (.mdb files)

Requires GDAL 3.4+

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Create a generic data item provider for all file based datasources
This provider uses the QgsProviderRegistry::querySublayers API to automatically create appropriate browser data items for all file based sources, regardless of the underlying provider whether it may be mdal, gdal, ogr, pdal, or ept.

This allows the merging of sources which can be handled by multiple different providers into single container items in the browser, which may be expanded to display all related or nested elements. It is common for many file types, such as GeoPDF or KML/KMZ files to may contain raster and vector layers, or .nc files which may be accessed as a mesh or raster depending on the data provider.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## QGISサーバー
### Feature: Enable multiple MetadataUrls
QGIS Server historically only supported the provision of a single metadata URL, but will now allow multiple metadata endpoints to be specified in the service definition.

![image40](images/entries/8e644bb4823b8da291e1e2b2dd1ca472d3d57246.webp)

This feature was funded by [Ifremer](https://wwz.ifremer.fr/)

This feature was developed by [Étienne Trimaille](https://github.com/Gustry)
### Feature: Add version to QGIS Server CLI tools
It\'s quite a common practice to have arguments like `-v` and `--version` for tools accessed via command line interfaces (CLIs), so new `--version` and it\'s alias `-v` have been added to identify QGIS version information for the following tools:
- qgis_process
- qgis_mapserv.fcgi
- qgis_mapserver

This feature was funded by [3Liz](https://www.3liz.com/)

This feature was developed by [Étienne Trimaille](https://github.com/Gustry)
## プログラム可能
### Feature: Expose scriptable vector tile encoder
An additional `writeSingleTile` method in `QgsVectorTileWriter` has been exposed to enable the encoding of a single vector tile to a memory buffer. This may support workflows for PyQgis and QGIS Server which include support for vector tiles.

This feature was developed by [David Marteau](https://github.com/dmarteau)
### Feature: Encode and write vector tiles in different CRS than EPSG:3857
The QGIS API has been extended to support encoding and writing vector tiles in a different CRS than EPSG:3857.

Note that according to the Mapbox Vector Tile specification, a Vector Tile represents data based on a square extent within a projection. A Vector Tile should contain information about its bounds and projection. The file format assumes that the decoder knows the bounds and projection of a Vector Tile before decoding it.

この機能は Ifremer によって資金提供されました

This feature was developed by [rldhont](https://github.com/rldhont)
### Feature: DistanceWithin filter for QgsFeatureRequest
An option has been added to QgsFeatureRequest to request features within a certain distance of a reference geometry

This is made possible by the new enum Qgis::SpatialFilterType which has been added to reflect whether a request uses no spatial filter, a BoundingBox filter (via setFilterRect), or the new DistanceWithin filter.

For example, the following request will retrieve all features within 50 map units of the provided linestring:
``` python
QgsFeatureRequest().setDistanceWithin(QgsGeometry.fromWkt('LineString(0 0, 10 0, 12 1)'), 50)
```
Distance within filters are treated like bounding box filters, in that they are independent of any attribute/id filters (such as feature ids or expressions).

Provider feature iterators can potentially delegate the distance within search to the backend. So, for example, the PostgreSQL data provider could use an `ST_DWithin` query for optimal index use.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: API for preset combobox values
An API has been added to allow a string parameter to show as a combobox with preset choices in processing GUI tools.

In some circumstances, it is desirable to restrict the values available when a user is asked to enter a string parameter that should match a list of predetermined \"valid\" values, yet these values will vary installation by installation.

For example, a \"printer name\" parameter, where it may be desired that users may pick a name value from a list of printers installed on the system, but since the printer names will vary between installations, an enum parameter is not a suitable choice.

This is now supported by setting the \"value_hints\" option in the widget wrapper metadata, as demonstrated below.

Whilst this provides a mechanism for guiding users to select from valid string values when running a Processing algorithm through the GUI, it does not place any limits on the string values accepted via PyQGIS codes or when running the algorithm via other means that do not use the GUI. Algorithms should gracefully handle other values accordingly.
``` python
param = QgsProcessingParameterString( 'PRINTER_NAME', 'Printer name')
# show only printers which are available on the current system as options
# for the string input.
param.setMetadata( {'widget_wrapper': { 'value_hints': ['Inkjet printer', 'Laser printer'] } })
```
This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: QgsExifTools class support for fetching tag values
The QgsExifTools class can now retrieve individual exif tags from images using the readTag function.

E.g.: `QgsExifTools.readTag('/my/photo/0997.JPG'), 'Exif.Image.DateTime')`

Known exif tags representing time values are automatically converted to Q{Date,Time,DateTime} objects. This makes working with those tags much easier and integrates well with other parts of the QGIS API.

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
## 注目すべき修正
### Even Rouaultによるバグ修正
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.16 backport commit (GitHub) | Remark |
| --- | --- | --- | --- | --- |
| WFS / GML parse issue, but QGIS loads GML as file fine? | [#45017](https://github.com/qgis/QGIS/issues/45017) | バグではない |  |  |
| POST request to modify timestamp does not respect defined format | [#44990](https://github.com/qgis/QGIS/issues/44990) | Wontfix / not a bug |  |  |
| Warning message \'Cannot create temporary SpatiaLite cache\' when adding many WFS-layers | [#44971](https://github.com/qgis/QGIS/issues/44971) | 重複 |  |  |
| QGIS creates invalid filter for WFS GetFeature request | [#43957](https://github.com/qgis/QGIS/issues/43957) | [PR #45043](https://github.com/qgis/QGIS/pull/45043) | [PR #45053](https://github.com/qgis/QGIS/pull/45053) |  |
| WFS Layer is not rendered when requested CRS is not matching project CRS and \"Only request features overlapping the view extent\" option is set | [#44054](https://github.com/qgis/QGIS/issues/44054) | [PR #45044](https://github.com/qgis/QGIS/pull/45044) | [PR #45047](https://github.com/qgis/QGIS/pull/45047) |  |
| Adding a WFS layer with filter for non-existent attribute leads to broken layer | [#43950](https://github.com/qgis/QGIS/issues/43950) | [PR #45045](https://github.com/qgis/QGIS/pull/45045) | [PR #45052](https://github.com/qgis/QGIS/pull/45052) |  |
| New Shapefile layer silently overwrite existing files | [#44299](https://github.com/qgis/QGIS/issues/44299) | [PR #45207](https://github.com/qgis/QGIS/pull/45207) | [PR #45240](https://github.com/qgis/QGIS/pull/45240) |  |
| QGIS on linux crashes when opening many geopackages at once | [#43620](https://github.com/qgis/QGIS/issues/43620) | [PR #45211](https://github.com/qgis/QGIS/pull/45211) | No |  |
| Crash in QgsPointCloudLayerRenderer when closing while rendering still active | [#44144](https://github.com/qgis/QGIS/issues/44144) | [PR #45227](https://github.com/qgis/QGIS/pull/45227) | [PR #45241](https://github.com/qgis/QGIS/pull/45241) |  |
| Geoprocessing tools cause libgeos to throw SIGBUS | [#45226](https://github.com/qgis/QGIS/issues/45226) | [geos PR 481](https://github.com/libgeos/geos/pull/481) | N/A |  |
| QGIS crash after loading WMS layer via script and zooming in and out | [#44095](https://github.com/qgis/QGIS/issues/44095) | [PR #45254](https://github.com/qgis/QGIS/pull/45254) | No | Mostly a usage issue |
| Integer unexpectedly large in GeoPackage | [#45178](https://github.com/qgis/QGIS/issues/45178) | バグではない |  |  |
| Attributes - Update All button - Creates Corrupted Fields - GeoJSON file | [#45139](https://github.com/qgis/QGIS/issues/45139) | [GDAL PR 4552](https://github.com/OSGeo/gdal/pull/4552) | N/A |  |
| WFS connection manager: GetCapabilities document\'s URLs not being used consistently | [#45242](https://github.com/qgis/QGIS/issues/45242) | [PR #45267](https://github.com/qgis/QGIS/pull/45267) | [PR #45273](https://github.com/qgis/QGIS/pull/45273) |  |
| QGIS crashes if network connexion is lost and a raster layer is loaded | [#45293](https://github.com/qgis/QGIS/issues/45293) | [GDAL PR 4560](https://github.com/OSGeo/gdal/pull/4560) | N/A |  |

These bug fixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

Bugs fixed by [Even Rouault](https://www.spatialys.com/)
### Alessandro Pasotti によるバグ修正
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.16 backport commit (GitHub) | Remark |
| --- | --- | --- | --- | --- |
| Data Source Manager - ArcGIS REST Server - dialog/window closes when adding a layer | [#45050](https://github.com/qgis/QGIS/issues/45050) | [PR #45059](https://github.com/qgis/QGIS/pull/45059) | n/a |  |
| \"Display no data value as\" option is not available in raster layer properties | [#44949](https://github.com/qgis/QGIS/issues/44949) | [PR #45063](https://github.com/qgis/QGIS/pull/45063) | Not critical |  |
| Raster layer not rendering after data-source change when combined with certain layout element | [#44929](https://github.com/qgis/QGIS/issues/44929) | [PR #45074](https://github.com/qgis/QGIS/pull/45074) | [PR #45083](https://github.com/qgis/QGIS/pull/45083) |  |
| Update selected feature ids before emitting featuresDeleted | [#44921](https://github.com/qgis/QGIS/issues/44921) | [PR #45078](https://github.com/qgis/QGIS/pull/45078) | Not critical |  |
| sample() and identify() from QgsRasterDataProvider don\'t always provide the same value | [#44902](https://github.com/qgis/QGIS/issues/44902) | [PR #45086](https://github.com/qgis/QGIS/pull/45086) | [PR #45145](https://github.com/qgis/QGIS/pull/45145) |  |
| Copying objects containing multiline strings into another project does not work properly | [#44989](https://github.com/qgis/QGIS/issues/44989) | [PR #45129](https://github.com/qgis/QGIS/pull/45129) | Not critical |  |
| projecting label coordinates for multiPoint geometry crashes QGIS | [#45148](https://github.com/qgis/QGIS/issues/45148) | [PR #45150](https://github.com/qgis/QGIS/pull/45150) | No |  |
| Copy/paste style category \"Form\" is missing some settings | [#45146](https://github.com/qgis/QGIS/issues/45146) | Maybe won\'t fix, checking with m-kuhn and 3nids |  |  |
| Adding a new point onto a memory multipoint layer kills QGIS | [#45152](https://github.com/qgis/QGIS/issues/45152) | [PR #45157](https://github.com/qgis/QGIS/pull/45157) |  |  |
| Attributes - Update All button - Creates Corrupted Fields - GeoJSON file | [#45139](https://github.com/qgis/QGIS/issues/45139) | [PR #45174](https://github.com/qgis/QGIS/pull/45174) | No |  |
| WMS parent layer added via QGIS Browser doesn\'t use default style | [#45192](https://github.com/qgis/QGIS/issues/45192) | [PR #45209](https://github.com/qgis/QGIS/pull/45209) | No |  |
| \"Display nodata as\" color widget is not automatically updated in layer styling panel | [#45132](https://github.com/qgis/QGIS/issues/45132) | [PR #45264](https://github.com/qgis/QGIS/pull/45264) | n/a |  |
| PostGIS error while changing attributes (field value and geometry): prepared statement \"updatefeature\" already exists | [#45100](https://github.com/qgis/QGIS/issues/45100) | [PR #45266](https://github.com/qgis/QGIS/pull/45266) | queued |  |
| Attribute Table in Layout Manager Font Style Override Doesn\'t Show Fields | [#45098](https://github.com/qgis/QGIS/issues/45098) | [PR #45269](https://github.com/qgis/QGIS/pull/45269) | queued |  |
| WFS Layer from QGIS Server is not rendered because of an issue with coordinate axis order | [#45216](https://github.com/qgis/QGIS/issues/45216) | [PR #45270](https://github.com/qgis/QGIS/pull/45270) | Not critical |  |
| Not rendering with identity transform raster created with rasterio | [#45324](https://github.com/qgis/QGIS/issues/45324) | Checked out, probably not a bug |  |  |
| SQL query from DB Manager is executed twice | [#45318](https://github.com/qgis/QGIS/issues/45318) | [PR #45351](https://github.com/qgis/QGIS/pull/45351) | queued |  |
| can\'t use layers where name starts with number in virtual layer | [#45347](https://github.com/qgis/QGIS/issues/45347) | [PR #45354](https://github.com/qgis/QGIS/pull/45354) | queued |  |
| Show Feature Count counts null in zero category | [#45280](https://github.com/qgis/QGIS/issues/45280) | [PR #45361](https://github.com/qgis/QGIS/pull/45361) | queued |  |
| Copying table by Drag&Drop in Browser (2) doesn\'t copy the table structure correctly | [#45286](https://github.com/qgis/QGIS/issues/45286) | [PR #45375](https://github.com/qgis/QGIS/pull/45375) | No |  |
| Wrong histogram plot if raster data type is byte | [#45379](https://github.com/qgis/QGIS/issues/45379) | [PR #45400](https://github.com/qgis/QGIS/pull/45400) | queued |  |
| Inconsistency regarding pattern handling for QgsServerOgcApiHandler | [#45439](https://github.com/qgis/QGIS/issues/45439) | [PR #45450](https://github.com/qgis/QGIS/pull/45450) | queued |  |
| QGIS Server - WMS Request GetPrint fails with ATLAS_PK | [#30817](https://github.com/qgis/QGIS/issues/30817) | [PR #45521](https://github.com/qgis/QGIS/pull/45521) | queued |  |
| projectsInDatabase key is not stored to xml for PostGIS connections | [#45508](https://github.com/qgis/QGIS/issues/45508) | [PR #45523](https://github.com/qgis/QGIS/pull/45523) | queued |  |
| Changing values in Form mode of attribute table doesn\'t set active the Save button | [#45527](https://github.com/qgis/QGIS/issues/45527) | [PR #45532](https://github.com/qgis/QGIS/pull/45532) | queued |  |
| Create spatialite trigger with DBManager do not work | [#45420](https://github.com/qgis/QGIS/issues/45420) | [PR #45553](https://github.com/qgis/QGIS/pull/45553) | No |  |

These bug fixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

Bugs fixed by [Alessandro Pasotti](https://www.qcooperative.net/)
### Peter Petrik によるバグ修正
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.16 backport commit (GitHub) | Remark |
| --- | --- | --- | --- | --- |
| QGIS 3.20 on Mac crashes when certain Qt signals are emitted | [#44182](https://github.com/qgis/QGIS/issues/44182) | [QGIS-Mac-Packager Commit bf925f311](https://github.com/qgis/QGIS-Mac-Packager/commit/bf925f3118a5d51080dfed46dddcb7cba3bbbc00) | n/a |  |
| Unable to view LAS files written in WGS84 (EPSG:4326) coordinates | [#44755](https://github.com/qgis/QGIS/issues/44755) | duplicate of [#41765](https://github.com/qgis/QGIS/issues/41765) |  |  |
| macOS: Symbol not found: \_\_cg_jpeg_resync_to_restart when reprojecting raster layer with GDAL warp on macOS | [#40164](https://github.com/qgis/QGIS/issues/40164) | いいえ | いいえ | Not an issue with the nightly (qgis-deps-0.9) anymore |
| Data Source Manager incorrectly identifies PostGIS raster extent on macOS | [#43042](https://github.com/qgis/QGIS/issues/43042) | [PR #45322](https://github.com/qgis/QGIS/pull/45322) | queued |  |
| icons not visible in the Layer Notes | [#44425](https://github.com/qgis/QGIS/issues/44425) | [PR #45332](https://github.com/qgis/QGIS/pull/45332) | n/a |  |
| メッシュレイヤでascii FLO-2Dファイルが開けない | 未報告 | [PR #45349](https://github.com/qgis/QGIS/pull/45349) | n/a |  |
| macOSでGRASSプロセシングツールを使うときのエンコーディング問題 | [#41870](https://github.com/qgis/QGIS/issues/41870) | [PR #45399](https://github.com/qgis/QGIS/pull/45399) | Not critical - workaround exists |  |
| Matplotlib QT backend imports not working on MacOS | [#45398](https://github.com/qgis/QGIS/issues/45398) | investigation |  |  |

These bug fixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

Bugs fixed by [Lutra Consulting (Peter Petrik)](https://www.lutraconsulting.co.uk/)
### Sandro Santilliによるバグ修正
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.16 backport commit (GitHub) | Remark |
| --- | --- | --- | --- | --- |
| Make QgsGeos::prepareGeometry and QgsGeos::cacheGeos idempotent | 未報告 | [PR #45147](https://github.com/qgis/QGIS/pull/45147) |  |  |
| Add a distanceWithin method to the QgsGeometryEngine virtual class | 未報告 | [PR #45057](https://github.com/qgis/QGIS/pull/45057) |  |  |
| Allow calling testdata_pg.sh from any directory | 未報告 | [PR #45378](https://github.com/qgis/QGIS/pull/45378) |  |  |
| Make TestPyQgsPostgresProvider.testGeneratedColumns idempotent | 未報告 | [PR #45415](https://github.com/qgis/QGIS/pull/45415) |  |  |
| Improve PostgreSQL test DB setup documentation and script | 未報告 | [PR #45413](https://github.com/qgis/QGIS/pull/45413) |  |  |
| Add GEOS DistanceWithin API | [GEOS Ticket #1124](https://trac.osgeo.org/geos/ticket/1124) | [GEOS commit #ba10ba4508a](https://trac.osgeo.org/geos/changeset/ba10ba4508af887a1a78bbc632ab45d89ce3242c/git) | [GEOS Issue #472](https://github.com/libgeos/geos/issues/472) |  |
| Make Postgres provider test idempotent | [#45417](https://github.com/qgis/QGIS/issues/45417) | [PR #45418](https://github.com/qgis/QGIS/pull/45418) |  |  |
| Use GEOSDistanceWithin when available | 未報告 | [PR #45340](https://github.com/qgis/QGIS/pull/45340) |  |  |
| Reduce GEOS conversions and preparations of geometries | 未報告 | [PR #45195](https://github.com/qgis/QGIS/pull/45195) |  |  |
| More heuristics to determine whether to iterate over target source | 未報告 | [PR #45339](https://github.com/qgis/QGIS/pull/45339) |  |  |

These bug fixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

Bugs fixed by [Sandro Santilli](https://strk.kbt.io/)
### Loïc Bartoletti によるバグ修正
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.16 backport commit (GitHub) | Remark |
| --- | --- | --- | --- | --- |
| More const in geometry | Not reported / performance | [PR #45217](https://github.com/qgis/QGIS/pull/45217) |  |  |
| QgsFeature::setId improve documentation with a warning | [#44898](https://github.com/qgis/QGIS/issues/44898) | [PR #45189](https://github.com/qgis/QGIS/pull/45189) | [PR #45229](https://github.com/qgis/QGIS/pull/45229) |  |
| Geometry Checker: Enlarge FeatureID | [#44250](https://github.com/qgis/QGIS/issues/44250) | [PR #45191](https://github.com/qgis/QGIS/pull/45191) | [PR #45229](https://github.com/qgis/QGIS/pull/45229) |  |
| VertexTool. Fixes move vertex on Z layer if CRS are differents (with Vincent Cloarec) | 未報告 | [PR #45020](https://github.com/qgis/QGIS/pull/45020) | Not backported. Introduce new methods. |  |
| Fix Z/M dimension URI via DB Manager. | [#34894](https://github.com/qgis/QGIS/issues/34894) | [PR #45223](https://github.com/qgis/QGIS/pull/45223) | [PR #45304](https://github.com/qgis/QGIS/pull/45304) |  |
| \[FIX\] GeometryValidator init curve support | 未報告 | [PR #45272](https://github.com/qgis/QGIS/pull/45272) |  |  |
| Compile fails, \'None\' is not a member of \'QgsField::ConfigurationFlags\' | [#44681](https://github.com/qgis/QGIS/issues/44681) | Wontfix / not a bug |  |  |
| Union fails when using a point and a polygon layer | [#44801](https://github.com/qgis/QGIS/issues/44801) | Difference between GEOS 3.8 and 3.9 |  |  |
| Rings order in MultiPolygon WKT string may leave overlapping parts when deleting holes (native:deleteholes) | [#44424](https://github.com/qgis/QGIS/issues/44424) | Wontfix for now. We can use Geos to fix the issue, but will remove Z/M and segmentize arc. |  |  |

These bug fixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

Bugs fixed by [Loïc Bartoletti](https://www.oslandia.com/)
### Denis Rouzaud によるバグ修正
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.16 backport commit (GitHub) | Remark |
| --- | --- | --- | --- | --- |
| Regression: trying to run the multipart to singleparts algorithm throws a python error | [#45331](https://github.com/qgis/QGIS/issues/45331) | [PR #45348](https://github.com/qgis/QGIS/pull/45348) |  |  |

These bug fixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

Bugs fixed by [Denis Rouzaud](https://www.opengis.ch/)
### Julien Cabieces によるバグ修正
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.16 backport commit (GitHub) | Remark |
| --- | --- | --- | --- | --- |
| Styles in database not working for postgres provider and non-geometric layers | [#44749](https://github.com/qgis/QGIS/issues/44749) | [PR #45075](https://github.com/qgis/QGIS/pull/45075) | [PR #45102](https://github.com/qgis/QGIS/pull/45102) |  |
| \"Layer notes\" icon is not displayed when copy-pasting a style | [#44692](https://github.com/qgis/QGIS/issues/44692) | [PR #45302](https://github.com/qgis/QGIS/pull/45302) | 必要なし |  |
| 曖昧なJSONエラー | [#42832](https://github.com/qgis/QGIS/issues/42832) | 複製に失敗する |  |  |
| Attribute table: missing features when copying/pasting from scratch layer | [#42798](https://github.com/qgis/QGIS/issues/42798) | Can't reproduce (Closed) |  |  |
| Form view shows wrong image attachments when scrolling through features | [#42705](https://github.com/qgis/QGIS/issues/42705) | 修正済み |  |  |
| Build Virtual Raster tool creates an additional layer when selecting and reordering layers | [#44270](https://github.com/qgis/QGIS/issues/44270) | [PR #45092](https://github.com/qgis/QGIS/pull/45092) | [PR #45102](https://github.com/qgis/QGIS/pull/45102) |  |
| Attachment widget options are reset when you reopen the field widget properties | [#45089](https://github.com/qgis/QGIS/issues/45089) | 重複 |  |  |
| Cleared feature attributes not acting like they have been cleared, and preventing saving of layer | [#39146](https://github.com/qgis/QGIS/issues/39146) | [PR #45176](https://github.com/qgis/QGIS/pull/45176) | [PR #45292](https://github.com/qgis/QGIS/pull/45292) |  |
| \[Postgres\] default value displayed instead of NULL | [#45198](https://github.com/qgis/QGIS/issues/45198) | [PR #45199](https://github.com/qgis/QGIS/pull/45199) | [PR #45291](https://github.com/qgis/QGIS/pull/45291) |  |
| a feature copy/paste sets a NULL field to its \"default value\" in a geopackage | [#44544](https://github.com/qgis/QGIS/issues/44544) | Question: Do we evaluate default value on NULL field when copy-pasting feature ? |  |  |
| QGIS expression builder can not resolve PostgreSQL text arrays correctly | [#45290](https://github.com/qgis/QGIS/issues/45290) | [PR #45321](https://github.com/qgis/QGIS/pull/45321) |  |  |

These bug fixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

Bugs fixed by [Julien Cabieces](https://www.oslandia.com/)
### Nyall Dawsonによるバグ修正
| バグの表題 | URL issues.qgis.org （報告された場合） | URL Commit (Github) | 3.16 backport commit (GitHub) | Remark |
| --- | --- | --- | --- | --- |
| Don\'t reset mesh layer styling when changing data source for layer | [#45391](https://github.com/qgis/QGIS/issues/45391) | [PR #45392](https://github.com/qgis/QGIS/pull/45392) | N/A |  |
| Fix crash when rendering clipped features and clipped shape results | [#45190](https://github.com/qgis/QGIS/issues/45190) | [Commit 6a4cdb36](https://github.com/qgis/QGIS/commit/6a4cdb36c91085c5bb1544fb02da1f83467a29d7) | [PR #45422](https://github.com/qgis/QGIS/pull/45422) |  |
| Fix crash when using map label tools with projects containing vector tile layers | [#44486](https://github.com/qgis/QGIS/issues/44486) | [PR #45311](https://github.com/qgis/QGIS/pull/45311) | [PR #45390](https://github.com/qgis/QGIS/pull/45390) |  |
| Fix symbol sizes in Meters at Scale cannot be negative | [#45298](https://github.com/qgis/QGIS/issues/45298) | [Commit 360351a](https://github.com/qgis/QGIS/commit/360351a02704c370545fb8f92c0bdafbdfa35b2e) | Not suitable for backport |  |
| Fix overwriting default style of geopackage layers | [#42811](https://github.com/qgis/QGIS/issues/42811) | [Commit eef6939b96](https://github.com/qgis/QGIS/commit/eef6939b96407b3d050988be4a0eeb692ffc5b68) | [PR #45107](https://github.com/qgis/QGIS/pull/45107) |  |
| Fix hang when rendering lines with dash patterns with all 0 values | [#41994](https://github.com/qgis/QGIS/issues/41994) | [Commit f4e2e900](https://github.com/qgis/QGIS/commit/f4e2e900eed16633ef0198f7b9a9152f395e173a) | [PR #45107](https://github.com/qgis/QGIS/pull/45107) |  |
| Update default toolbar locations | 未報告 | [Commit 77be95feac](https://github.com/qgis/QGIS/commit/77be95feac7391e58f6bd487f30e09ed8ed63651) | N/A |  |
| Don\'t overwrite existing data defined property expressions when an interactive map tool is used to move/rotate/edit labels | [PR #45279](https://github.com/qgis/QGIS/pull/45279) | [Commit b30c17f0](https://github.com/qgis/QGIS/commit/b30c17f07d00850597d8bb1b2cfb1f454498b391) | N/A |  |
| Fix crash on exit with CAD dock open | 未報告 | [Commit 1fb21f69f](https://github.com/qgis/QGIS/commit/1fb21f69fede05cabb8f1d27a8ad24564ae16f3d) | N/A |  |
| Fix rule based symbology doesn\'t work for columns with \'-\' in name | [#44379](https://github.com/qgis/QGIS/issues/44379) | [Commit 51fa9840](https://github.com/qgis/QGIS/commit/51fa9840248135a7fe7ee181b7d645f3c591c9cc) | [Commit 797367dde](https://github.com/qgis/QGIS/commit/797367dde65d6ab06f39f5c4636c2127c67aa9d1) |  |
| Avoid hangs when drawing symbol icons using inappropriate sizes in map units | [#41149](https://github.com/qgis/QGIS/issues/41149) | [PR #45233](https://github.com/qgis/QGIS/pull/45233) | Not suitable for backport |  |
| Fix inappropriate display of z/m values in cad dock when non-z/m layer is selected | 未報告 | [Commit 55a76d1d](https://github.com/qgis/QGIS/commit/55a76d1d867c32f52ae4bd38ed671d44aa3ae92e) | N/A |  |
| Implement more responsive cancelation of map render for maps using complex effects | [#41149](https://github.com/qgis/QGIS/issues/41149) | [PR #45212](https://github.com/qgis/QGIS/pull/45212) | Not suitable for backport |  |
| Allow CAD dock to be used for geographic CRS, but only allow the x/y/z/m constraints to be set | 未報告 | [PR #45185](https://github.com/qgis/QGIS/pull/45185) | Not suitable for backport |  |
| Fix crash when opening symbology properties of a layer set to embedded renderer which is not compatible with embedded renderers | [#45159](https://github.com/qgis/QGIS/issues/45159) | [PR #45193](https://github.com/qgis/QGIS/pull/45193) | N/A |  |
| Fix QgsMapToolCapture coordinates when associated with a non-vector layer where the layer CRS != canvas CRS | 未報告 | [PR #45183](https://github.com/qgis/QGIS/pull/45183) | N/A |  |
| Fix geometry generator rendering outside of vector layers | [#39159](https://github.com/qgis/QGIS/issues/39159) | [PR #45165](https://github.com/qgis/QGIS/pull/45165) | Not suitable for backport |  |
| Fix color customisation is lost when configuring renderers using geometry generators | [#38377](https://github.com/qgis/QGIS/issues/38377) | [PR #45166](https://github.com/qgis/QGIS/pull/45166) | Not suitable for backport |  |
| Fix rendering of interpolated line symbol layer outside of vector layers | [#45028](https://github.com/qgis/QGIS/issues/45028) | [PR #45164](https://github.com/qgis/QGIS/pull/45164) | N/A |  |
| QgsGeometry.fromPolygonXY ドキュメントの修正 | [#45099](https://github.com/qgis/QGIS/issues/45099) | [Commit 3d599fe4](https://github.com/qgis/QGIS/commit/3d599fe4b5574e7c916133171e097163cae51e32) | N/A |  |
| Fix digitizing features using CAD dock when layer CRS != canvas CRS | 未報告 | [PR #45108](https://github.com/qgis/QGIS/pull/45108) | N/A |  |
| Fix offset background when drawing rotated text | [#44907](https://github.com/qgis/QGIS/issues/44907) | [PR #45425](https://github.com/qgis/QGIS/pull/45425) | pending |  |
| Correctly escape complex source strings in processing history log | [#45403](https://github.com/qgis/QGIS/issues/45403) | [PR #45426](https://github.com/qgis/QGIS/pull/45426) | pending |  |
| Fix handling of ADF files in browser | 未報告 | [PR #45393](https://github.com/qgis/QGIS/pull/45393) | Not suitable for backport |  |

These bug fixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

Bugs fixed by [Nyall Dawson](https://north-road.com/)

{{<content-end >}}
