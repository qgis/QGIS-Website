---
draft: 'true'

---
# QGIS \-\-- an interesting instrument for forestry planning concepts at local and regional level
Almost 35% of Switzerland\'s surface is covered by forests. Changing demands upon the forest and the poor financial situation of forest enterprises in Switzerland led to the development of a new forestry planning concept about fifteen years ago. This concept introduced a clear distinction between planning at the level of the authorities and planning at the level of the owners1. As a new forestry planning office, guaraci works primarily in the region of Basel (Switzerland) on both mentioned planning levels. This case study discusses the use of QGIS at the forest owner level. On this level, a simple, dynamic and compatible geographic information system is required for the establishment of a forest management plan. This plan covers about 1000 ha of forests, will be valid for about 20 years and is implemented by the local forest manager. The area is situated in the region of Basel (see google maps).
## QGISの使用方法
全体の計画プロセスの中でQGISは、次の4つのタスクに使用されました：
- 既存データのインポート。データは、ポリゴン、ラインやポイントシェイプファイルと一緒にジオリファレンス背景地図（ \*.tif ）が含まれます。森林管理者にとっては、既存の主題別データ（例えば地上および飲水資源、自然保護区）の可視化は、毎日の仕事のために重要です。
- Digitizing. The forestry measurements planned by the forest manager had been digitized. The QGIS digitizing tools with the advanced snapping options are very useful and user friendly. The „delimited text" plugin enabled the import of additional data tables.
- 分析。異なる測定カテゴリの領域が計算されました。鉄道線路や道路などの特定のライン地物から始めて、対応する保護林が、バッファの助けを借りて決定されました。
- 印刷およびエクスポート。印刷コンポーザが地図レイアウトの作成をサポートしました。地図は、PDFや画像ファイルとしてエクスポートされました。

![Extract of the forestry measurements map](./images/suisse_basel1.jpg){.align-right}
## 結論
QGIS is an interesting tool for small planning offices, such as guaraci, as well as for the forest managers and owners. It can be used in a professional context and the presented output result was appreciated by all parties involved. For the mentioned tasks the present QGIS version 1.4 "Enceladus" offers all necessary GIS tools. The most important qualities of QGIS are the intuitive user interface and the compatibility with different file formats. It is an ideal tool for projects that are on one hand based on existing geographic data and on the other hand require the acquisition of new data. The user-manual is helpful and easy to understand. Both from the technical as well as the financial perspective QGIS is an interesting alternative to other GIS software.
## 展望
森林計画コンセプトの中核業務は挙げられた基本的なGISツールで作業できます。Guaraciは、森林所有者レベルでの森林計画にQGISを使用し続けるでしょう。提示したプロジェクトの経験に基づいて、QGISは地方自治体のレベルでの森林の概念のためにも推奨できます。詳細な分析要件を持つ大規模、かつ複雑なプロジェクトは、PostGISの空間データベース・サーバーとのQGISの組み合わせによって処理できます。新しいロギングゾーンだけでなく、森林reservatesと保護ゾーンを簡単にデジタル化できます。願わくば、森林所有者や管理者が年間計画およびそれらの森林活動の文書化のためにも、QGISの可能性をますます使用するようになっていけばと思います。
## 著者
![Raphael Häner](./images/suisse_baselaut.jpg){.align-left height="200px"}

This article was contributed in June 2010 by Raphael Häner. He is Dipl. Forst Ing. at ETH Zürich, Switzerland and founded his one-man company guaraci in 2009.
