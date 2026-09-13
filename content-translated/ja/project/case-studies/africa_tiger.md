---
HasBanner: false
archived: true
date: 2012-06-30
draft: false
featured: false
section: project
sidebar: true
thumbnail: images/africa_tiger1.jpg
title: 水の観察と情報システム：アフリカにおける統合水資源管理のために地球観測データの使用を可能にする
type: case-study

---
{{<content-start >}}
# 水の観察と情報システム：アフリカにおける統合水資源管理のために地球観測データの使用を可能にする
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>June 30, 2012</span>
</p>

The Water Observation and Information System (WOIS) is an open source software tool for monitoring, assessing and inventorying water resources in a cost-effective manner using Earth Observation (EO) data. The WOIS has been developed under the TIGER-NET project, which is a major component of the TIGER initiative of the European Space Agency (ESA) and whose main goal is to support the African Earth observation capacity for water resource monitoring. TIGER-NET aims to support the satellite-based assessment and monitoring of water resources from watershed to cross-border basin levels through the provision of a free and powerful software package, with associated capacity building, to African authorities.
## システム説明
The WOIS can be seen as a multipurpose system consisting of a spatial database, facilities for extracting and processing EO data, and integrative tools and models aimed at decision support e.g. hydrological modelling and GIS-embedded visualization and analysis tools. The WOIS is designed around QGIS, which acts as the front-end Graphical-User-Interface (GUI). QGIS was chosen as the central integrating platform, due to its clear and accessible GUI, strong development community, ease of implementing additional functionalities through Python plugins and its high level of interoperability with major GIS data formats through the use of the Geospatial Data Abstraction Library (GDAL/OGR) library.

Moreover, the integrated Processing Toolbox, formerly known as SEXTANTE, brings the ability to easily incorporate geoprocessing algorithms from various applications into QGIS. It acts as a joint repository for a wide range of algorithms, some native to QGIS and others imported from external applications, such as GRASS GIS or the Orfeo Toolbox. Support for algorithms from ESA's BEAM, NEST and Sentinel-1 Toolbox software and for setting up and executing SWAT based hydrological models was added to the Processing Toolbox during the WOIS development. The toolbox also allows for easy incorporation of custom R and Python scripts. The inputs and outputs of the Processing Toolbox algorithms can be evaluated with the QGIS capabilities of data I/O, rendering or map creation.

処理ツールボックスの重要な利点は、シームレスにデータ処理および分析のための別のアルゴリズムプロバイダからの機能を使用する能力です。これは、自動処理のモデルを作成し、TIGER-NETプロジェクトで開発されたQGISプラグインを通じて、順次ウィザードベースの処理チェーンに異なるプロバイダからアルゴリズムを組み合わせるために使用することができます。この機能は、水資源管理の中EOデータ分析に関連する共通だが複雑なタスクを実行するための（説明書付き）標準化されたワークフローのライブラリーを作成するために使用されました。

<figure>
<img src="../images/africa_tiger1.jpg" class="align-center" style="width:100.0%" alt="africa_tiger1.jpg" />
<figcaption>The WOIS graphical user interface, including the embedded workflow library (center) and wizard-based processing workflow (right)</figcaption>
</figure>

アフリカにおける統合的水資源管理をサポートするためのWOISの運用や実用は、テーマと情報製品の広い範囲をカバーし、ユーザー固有のデモンストレーション例シリーズを経て実証されています。これらの中にあるのは：湖沼水質；洪水の監視； 土地の劣化と土地被覆特性評価；水域マッピングおよび水文モデリング。デモの例は、いくつかの段階があります。まず、カスタマイズされたエンドツーエンドの処理のワークフローは、要求された製品やアプリケーション用に開発されています。これらのワークフローは、その後、ユーザーの要求に応じて重要な領域と時間の期間にわたって、製品の導出のために使用されています。最終工程において、ワークフロー（すなわち、それらの安定性/性能と使いやすさ）、ならびに製品の成果は、ユーザーとの緊密な対話で評価されています。

<figure>
<img src="../images/africa_tiger2.jpg" class="align-center" style="width:100.0%" alt="africa_tiger2.jpg" />
<figcaption>Sentinel-1 flood monitoring of Caprivi flood plain, Namibia.</figcaption>
</figure>

## 結論
WOISの開発はユーザー主導と共同開発モデルの成功例を表します。そこでは水管理と統合水資源管理計画を高める上でのシステムの実際の影響を実証するために、機能がユーザー指定の場合を介して、設計、開発、評価されてきました。WOISはすでに主要なアフリカの河川流域当局やいくつかのアフリカの省庁だけでなく、研究や人道組織で実装されています。したがって、新機能や機能改善のための継続的なユーザー要件に対応し、一般的なソフトウェア、アルゴリズムとメソッドの機能拡張を原因に、開発を続けていきます。

焦点は特に、WOISにESAのSentinelツールボックスを統合し、専用の生産ワークフローを開発することによって、新しいセンチネル衛星システムの処理能力の支援と実施を確実にすることになるでしょう。WOISの次のリリース（2015年4月の後半に起因する）は、すでにセンチネル-1ツールボックス洪水の監視や水ボディマッピングなどのために、この新しいレーダーデータセットを利用したワークフローの数々が組み込まれてます。これはWOISを完全運用監視システムに変えるでしょう。このライセンスフリー、強力かつ拡張システムの提供を通じて、および継続的な能力開発や研修活動を通じて、プロジェクトは、アフリカの他の国と地域に及び越えて延長、すなわちロールアウトのための基盤を構築するために繁栄します。
## リファレンス
- Bauer-Gottwein, P., Jensen, I. H., Guzinski, R., Bredtoft, G. K. T., Hansen, S., & Michailovsky, C. I. (2015). Operational river discharge forecasting in poorly gauged basins: the Kavango River basin case study. Hydrology and Earth System Sciences, 19(3), 1469-1485.
- Guzinski, R.; Kass, S.; Huber, S.; Bauer-Gottwein, P.; Jensen, I.H.; Naeimi, V.; Doubkova, M.; Walli, A.; Tottrup, C. Enabling the Use of Earth Observation Data for Integrated Water Resource Management in Africa with the Water Observation and Information System. Remote Sens. 2014, 6, 7819-7839.
- Walli, A., Tottrup, C., Naeimi, V., Bauer-Gottwein, P., Bila, M., Mufeti, P., Tumbulto, J.W., Rajah, C., Moloele, L.S. & Koetz, B. "TIGER-NET---Enabling an earth observation capacity for integrated water resource management in Africa," presented at the ESA Living Planet Symp., Edinburgh, U.K., Sep. 11--13, 2013.

## リンク
- More information about the WOIS software and the TIGER-NET project can be found on the project's website: www.tiger-net.org
- More information about ESA's TIGER initiative can be found on the initiative's website: <http://www.tiger.esa.int/> WOIS is available for download (after registration) from the TIGER website (<http://www.tiger.esa.int/page_eoservices_wois.php>) with source code of the developed plugins, scripts, models and workflows available from the project's GitHub page (<https://github.com/TIGER-NET>)
- More information about the new Sentinel satellites can be found on ESA's website: <http://www.esa.int/Our_Activities/Observing_the_Earth/Copernicus/Overview4>

### 著者
This article was contributed by Radoslaw Guzinski (WOIS software developer) with contributions from the TIGER-NET technical teams at DHI-GRAS (www.dhi-gras.com), GeoVille (www.geoville.com), the technical universities in Vienna (<http://rs.geo.tuwien.ac.at/>) and Copenhagen (<http://www.env.dtu.dk/>) as well as the European Space Agency ( www.esa.int).

{{<content-end >}}
