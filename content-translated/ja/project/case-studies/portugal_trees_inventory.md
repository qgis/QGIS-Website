---
HasBanner: false
archived: false
date: '2025-06-08'
draft: false
featured: true
section: project
sidebar: true
thumbnail: images/portugal_trees_inventory3.webp
title: ポルトガルにおける都市樹木目録の作成にQGISとMergin Mapsを活用
type: case-study

---
{{<content-start >}}
# ポルトガルにおける都市樹木目録の作成にQGISとMergin Mapsを活用
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>2025年6月08日</span>
</p>

NaturalGIS \[<https://www.naturalgis.pt>\] は、地理情報システム(GIS)を専門とするポルトガルの企業であり、特にQGISとPostGIS技術に注力しています。同社の主力事業には、技術サポートの提供、トレーニング、WebGISプラットフォームやQGISプラグインを含むカスタムGISソリューションの開発があります。

Mergin Maps \[<https://merginmaps.com>\]は、QGISを用いた野外データの収集と同期を可能にする地理空間データプラットフォームです。同社の主力事業は、オフラインでのモバイルマッピングや共同GISワークフローのためのツールを提供することです。このサービスは、環境モニタリング、通信、農業、資産管理などの分野で広く利用されています。

2021年、ポルトガル政府は都市部の樹木管理を規定する法律を可決し、自治体に対し、都市部の公有地にある全ての樹木の台帳を公表することを義務付けました。NaturalGISは、QGISとMergin Mapsを活用して、ポルトガルの複数の自治体（マソン、パルメラ、ロウリニャ、ソウレなど）において、都市樹木台帳を作成するための調査を実施しています。QGISとMergin Mapsを組み合わせることで、規制の要件に合わせたカスタムデータ構造を構築できるだけでなく、技術系でないユーザーでも正確な調査データを収集できる簡素化されたモバイルインターフェイスを提供できます。

<figure>
  <img src="../images/portugal_trees_inventory1.webp" class="align-right" alt="Simple user interface makes Mergin Maps easy to use for non-technical users" />
  <figcaption>シンプルなユーザーインターフェイスにより、Mergin Mapsは技術系でないユーザーでも簡単に使えます</figcaption>
</figure>

## QGISを用いた規制に準拠した樹木調査の設計
この規制は、自治体が所有する土地にある各樹木について、以下の情報を収集することを義務付けています:
- 樹種またはその他の特別分類
- 寸法（全高、直径など）
- 推定樹齢
- 健康状態
- 地理的位置
- 保護指定の理由（該当する場合）

樹木の正しい同定を確認するため、幹、枝、葉、および果実や球果の写真も撮影されます。さらに、樹木が植えられている土壌の種類、灌漑システム、樹冠の大きさ、病気・ストレス・欠陥の兆候、その他の情報などの詳細も収集されます。

このプロジェクトはQGISを使用して設計され、データはGNU AGPL-3ライセンスの下で公開されているMergin MapsのひとつのバージョンであるMergin Maps Community Edition (CE) を導入した独自のサーバー上でホストされました。

プロジェクトの設定では、条件付き表示ウィジェットや写真添付ウィジェットが使用されました。プロジェクトで収集する必要のある写真数が膨大であったため、Mergin Mapsの機能である「デバイスごとの写真ダウンロード制限」が活用されました。さらにデバイスのストレージ容量を節約するため、Mergin Maps CLI（コマンドラインインターフェース）ツールを使用してスクリプトを毎日実行し、プロジェクトから写真を削除してWebサーバーに保存しました。そして、その写真へのリンクが調査レイヤーにある専用のフィールドに保存され、アプリ内で写真をプレビューできます。

<figure>
  <img src="../images/portugal_trees_inventory2.webp" class="align-right" alt="Mobile forms were set up in QGIS project and transferred to Mergin Maps" />
  <figcaption>QGISプロジェクトでモバイルフォームを設定し、Mergin Mapsに転送しました</figcaption>
</figure>

## モバイル利用向けに最適化されたデータ収集
データは、各自治体で2～4名の調査員からなるチームによって収集されました。通常、1日あたり平均約150本のデータを収集することができました。Mergin Mapsのモバイル向けに最適化されたインターフェイスにより、技術系でないユーザーでもデータ収集方法を素早く習得することが容易になりました。

チームによる初期の調査データ収集が完了すると、引き継ぎプロセスを実施し、現地の自治体チームに対して、QGISでのプロジェクト管理方法や、必要に応じてアプリ内のデータを更新する方法についてトレーニングを行いました。このプロジェクトでQGISとMergin Mapsを採用したことで、樹木台帳を正確かつタイムリーにまとめることが可能になりました。

<figure>
  <img src="../images/portugal_trees_inventory3.webp" class="align-right" alt="The QGIS project used for the inventory" />
  <figcaption>調査に使用されたQGISプロジェクト</figcaption>
</figure>

## 著者
Giovanni Manghi B.Sc. in Biology, is co-owner and CTO at NaturalGIS located in Évora, Portugal.

{{<content-end >}}
