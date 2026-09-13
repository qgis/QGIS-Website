---
HasBanner: false
archived: true
date: 2012-05-01
draft: false
featured: false
section: project
sidebar: true
thumbnail: images/italy_vicenza1.png
title: Montecchio Maggiore、ヴィチェンツァ、イタリア、自治体での都市計画にQGISを使用する
type: case-study

---
{{<content-start >}}
# Montecchio Maggiore、ヴィチェンツァ、イタリア、自治体での都市計画にQGISを使用する
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>May 01, 2012</span>
</p>

Montecchio Maggiore is a small town in the middle west of Vicenza (about 24.000 population). And as many other italian municipality it manages the town planning; in particular the urban planning and what we call "recovery plan" aka PDR —— Piani Di Recupero. This urbanistic tool is dedicated to the historical area in the center of the town and it requires a specific study: building state of conservation, intended use, particular historical notice via survey and restitution to produce planimetric and prospectus graphics. For this purpose it has used QGIS in addition to Postgresql/Postgis database, PHP code and Libreoffice suite, QCAD (LibreCAD).
## タスク
<figure>
<img src="../images/italy_vicenza1.png" class="align-right" alt="italy_vicenza1.png" />
<figcaption>Workflow Schema</figcaption>
</figure>

スキーマによってワークフローが明確になります。

すべての建物データは調査を通じて取得され、紙のスケジュールに書かれました。一度オフィスでデータは標準的なWebブラウザを使用してPHPのフォームからのPostgreSQL / PostGISのデータベースに入力inputedされました（Firefoxの、Iceweaselのも）。第二の瞬間には、すべての建物の形状は、QGISで描画されidキーフィールド（PostgreSQLの/ PostGISのビュー）を介して、調査表にリンクされました。

同時に、建物のファサードはQCAD（LibreCAD）を使用して設計されました。

PDR（piani di recupero復旧計画）は、特定のグラフィックスを必要とする厳密な規則に従わなければなりません。
- 現在の状態
- プロジェクトの状態
- 使用目的（現在）
- 意図された使用（プロジェクト）
- 介入のタイプ

すべてのグラフィック主題図の属性を使用して生成されたデータは、研究と設計FASE中に変更（現在の状態のための）調査とデータの間に取得します。

Thus a photo was linked to every building facilitating the design and analisys in the gis project (using the "action" feature). The SQL tools (pgquery, postgis manager, dbmanager et al.) allowed to obtain very sophisticated query immediately viewable in the map canvas such as: volume calculation split by building intended use, standards area calculation in percentage of the total planning area and other minor queries. All useful items for the design and planning study otherwise not possible without a very strength tool like gis (and QGIS in particular).

<figure>
<img src="../images/italy_vicenza2.png" class="align-right" alt="italy_vicenza2.png" />
<figcaption>QGIS project with building data viewing</figcaption>
</figure>

最後に、すべての建物のための統合報告書が、LibreOfficeのスイートを用いて製作されました。報告書は、現状のコンテストやデータに建物をローカライズ写真、地図作成エキスをまとめるスケジュールで構成されています。

<figure>
<img src="../images/italy_vicenza3.png" class="align-right" alt="italy_vicenza3.png" />
<figcaption>QGIS print composer for final graphic layout</figcaption>
</figure>

## 結論
The strength of QGIS is the very user friendly interface coupled with the several tools it offers. The connection with vary data formats (shape files, spatialite db, postgresql/postgis db,\...) facilitates and increases the interoperability between different worlds. And thus the freedom offered by the free software (QGIS, PHP, Libreoffice, QCAD) stimulates and open new horizons.

そして、言い残していましたが：私たちは、異なるプラットフォーム上（Windows 7の64ビット、Windows XPの32ビット、DebianのサーバとDebianのクライアント）で作業していましたが、乗り越えられない問題に遭遇したことはありません。
## 著者
<figure>
<img src="../images/italy_vicenzaaut.png" class="align-left" height="200" alt="italy_vicenzaaut.png" />
<figcaption>Flavio Rigolon</figcaption>
</figure>

This article was contributed May 2012 by Flavio Rigolon. He lives in Vicenza (Italy) and works in Montecchio Maggiore municipality as SIT manager. He has migrated almost all the gis data from proprietary to free platform (QGIS, Postgresql/Postgis, Spatialite). He is a member of GFOSS.it (Associazione Italiana per l\'Informazione Geografica Libera) since 2007 and was a member of the GFOSS.it board from 2010 to 2012.

{{<content-end >}}
