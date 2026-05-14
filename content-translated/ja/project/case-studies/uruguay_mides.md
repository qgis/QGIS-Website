---
HasBanner: false
archived: true
date: 2016-03-01
draft: false
featured: false
section: project
sidebar: true
thumbnail: images/uruguay_mides1.png
title: ウルグアイ社会開発省（MIDES）におけるQGISの利用
type: case-study

---
{{<content-start >}}
# ウルグアイ社会開発省（MIDES）におけるQGISの利用
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>March 01, 2016</span>
</p>

## 前書き
The Ministry of Social Development of Uruguay ([MIDES,](http://www.mides.gub.uy/innovaportal/v/4376/3/innova.front/mision) , for its acronym in Spanish) is responsible for the national social policies. MIDES is also accountable for the coordination -at both sectoral and territorial levels- articulation, monitoring, supervision and evaluation of plans, programs and projects, within the areas of its competence, aiming at the consolidation of a progressive redistributive social policy.

The National Division of Evaluation and Monitoring ([DINEM](http://dinem.mides.gub.uy/innovaportal/v/25948/11/innova.front/mision-y-cometidos) ) is a section of MIDES that oversees the monitoring and evaluation of plans, programs, actions, devices and social projects through the national territory. DINEM also produces and manages necessary information to improve their design and implementation.

The [Department of Geography of DINEM](http://dinem.mides.gub.uy/innovaportal/v/25507/11/innova.front/departamento-de-geografia) is responsible for the production, management and analysis of geographical information,
## DINEM地理局のQGIS
Ever since the consolidation of the Department of Geography in 2012, we have tried to incorporate open source software to fulfill our duties. In particular, the management of an extensive field work, consisting in the annual implementation of approximately 40,000 visits to socially vulnerable households throughout the country. The objective was to conform a thorough georeferenced database of target households, in order to improve social policies implementation. Particularly, data was collected to enhance the scope of monetary transfer programs ([\"Asignaciones Familiares -- Plan de Equidad\"](https://www.bps.gub.uy/3540/plan-de-equidad.html) and [\"Tarjeta Uruguay Social\"](http://www.mides.gub.uy/innovaportal/v/55480/3/innova.front/tarjeta-uruguay-social-tus)). The survey form applied contemplates social, housing, and environmental aspects.

このようなフィールドワークを可能にするロジスティクスは、統計パッケージを使用して生成されたデータベースを管理し、GISを大いに活用して実地見学やジオリファレンスのいらないデータを整理することなどです。

<figure>
<img src="../images/uruguay_mides1.png" class="align-center" alt="uruguay_mides1.png" />
<figcaption>QGIS at work: identifying houses on informal settlements to implement fieldwork</figcaption>
</figure>

作業プロセスが開始されたときには商用ソフトウェアが実装されましたが、タスク自体の発展が徐々にオープンソースソフトウェアに変換することを要求しました。全体としてのプロセスがより電子化され、ワー​​クフローエンジンとPostGIS地理空間データベースを組み込むにつれ、フリーおよびオープンソースソフトウェア（FOSS）オプションによって提供されるライセンス要件と利点が私たちに変更を促しました。このようにして、QGISプロジェクトが洗練（バグ減少や機能増加）されるにつれ、QGISを使用して私たちのニーズを満たせるようになりました。PostGISに関連するツールを使用することで、作業グループは、毎日の現地調査を効率化するために必要な業務を迅速に調整し、リリーフしてデジタル化した直後の同じデータフィールドワークに対する後続の分析業務を迅速に実行できました。

<figure>
<img src="../images/uruguay_mides2.png" class="align-center" alt="uruguay_mides2.png" />
<figcaption>QGIS at work: Montevideo, Uruguay’s capital and most populated city, overlayed with PostGIS layer showing to-do visits (mostly composed of socially vulnerable households, in the outskirts of the city)</figcaption>
</figure>

In addition to information management and field work implementation, we constantly use QGIS typical geospatial tools to produce tematic cartography, and in spatial analysis tasks. This last, as much about the data that the fieldwork generates, as with other ministry programs information, and frequently even to aid interinstitutional projects. With [\"qgis2web\"](https://plugins.qgis.org/plugins/qgis2web/) we were able to produce interactive maps, which have become the main way to communicate the results of such investigations. They allow human resources within other programs and agencies to easily and effectively manage higher amounts of information than with a collection of static maps, even when these resources are not used to reading spatial data.
## 結論
QGISは、DINEM地理局にとって基本的なソフトウェアとなっています。これは、重いファイルで作業し、PostGISやワークフローエンジンと対話するための優れたパフォーマンスを提供します。これにより、地理データの優れた管理が可能になり、ベースマップや主観品質の優れた地図作成が可能になります。

At the same time, extra features that are incorporated through plugins are of great value to us. For instance, the possibility of exporting \"leaflet\" map viewers, as well as incorporating high resolution satellite imagery directly into the GIS work area through "OpenLayers" to manually vectorize information, among others.

This variety of options is precisely what has allowed us to develop the specific and at the same time very different technical solutions that programs and agencies have been needing through past years.As mentioned in this article, we can state that QGIS meets the necessary requirements to be used in public administration as desktop GIS software. Also it has been a cornerstone in helping this institution to set up a web map, offering general population much information about social issues ([SIG MIDES](https://mapas.mides.gub.uy/), OpenLayers based WEB GIS developed by the IT division).
## 著者
Guillermo D\'Angelo - Head of the Geography Department (DINEM-MIDES, Uruguay). Degree in Geography.

Richard Detomasi - Adviser in Spatial Analysis Section of Geography Department (DINEM-MIDES, Uruguay). Ph.D. student in Social Sciences, Population Studies. Magister in Contemporary Studies of Latin America. Degree in Anthropological Sciences.

Martín Hahn - Adviser in Spatial Analysis Section of Geography Department (DINEM-MIDES, Uruguay). Bach. currently coursing Geography Degree.

この記事は上記3名で書かれたものではありますが、そこに記載されているプロセスには100人以上の人が関わっています。

Contact: <mapas@mides.gub.uy>

{{<content-end >}}
