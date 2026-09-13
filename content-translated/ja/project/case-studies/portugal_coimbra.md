---
HasBanner: false
archived: true
date: 2014-07-01
draft: false
featured: false
section: project
sidebar: true
thumbnail: images/portugal_coimbra1.png
title: 景観の特徴付けのためにオープンソースツールを使用する。LecosSプラグイン
type: case-study

---
{{<content-start >}}
# 景観の特徴付けのためにオープンソースツールを使用する。LecosSプラグイン
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>July 01, 2014</span>
</p>

This case study results from the final draft of the Graduate Geographic Information Systems taught by GeoPoint. We proposed to study a landscape using Landscape Ecology plugin (LecoS) in QGIS 2.01 Dufour. The study was conduted in a region of central Portugal, Municipality of Coimbra, with an total area of 31940ha and it has geographic coordinates 40°12\'11.84\" North, 8°24\'37.15\" West. Because the new administrative reorganization this municipality are divided into 18 parishes, which are mostly urban areas (Figure 1).

<figure>
<img src="../images/portugal_coimbra1.png" class="align-left" alt="portugal_coimbra1.png" />
<figcaption>Geographic location of the municipality of Coimbra.</figcaption>
</figure>

風景の特徴付けは、景観評価指標によって設計された定量的な指標を用いて行われます。これらの指標は、その後、変更及びいくつかの種または種の群（ターナーら2001年；オルセンら、2007年；フィダルゴら、 2009年）、の発生との関係を文書化するため、風景の構造的特徴を記述するために使用される。指標の数が非常に多く、景観レベル、クラス及び染色（ターナーら、2001年；フィダルゴら、2009年）で計算できます。メトリックはCORINE土地被覆、土地利用（COS 90とCOS2006）または当社によって生成された土地被覆の地図から計算できます。マーティンジョン（2012年）によれば、風景エコロジーStistics（Lecos）はQGISのモジュールは、ラスターレイヤーにランドスケープ・メトリックを計算するために使用されます。結果はCSV形式で利用できるようにすることができます。
## メソッド
Landscape metrics was calculated using the Corine Land Cover (CLC) of the years 1990 and 2006. For this purpose it was necessary to transform the coverages in raster format with cell size 50x50 meters. We use r.to.raster tool the Grass Gis module that were present in processing toolbox and the CLC classification level used it´s the first. After transform coverages we calculate the metrics in Landscape Ecology plugin (LecoS) using the graphical modeler (Figure 2).

<figure>
<img src="../images/portugal_coimbra3.png" class="align-left" alt="portugal_coimbra3.png" />
<figcaption>Landscape metrics calculated for diferent years (1990 and 2006).</figcaption>
</figure>

私たちは、土地被覆面積、風景割合、エッジ密度、パッチの数、最大パッチ面積、最小パッチ面積、平均パッチ距離および実効メッシュサイズを計算します（表1）。景観の多様性の測度は、シャノン指数、均一性とシンプソン指数を算出しました。
## 結果
From analysis of the landscape metrics calculated it was found that there was an increase in the degree of human disturbance and therefore a greater fragmentation of uses between 1990 and 2006. The number of patches of "Forest Semi Natural areas" and "Agricultural areas" decreased between 1990 and 2006 (Table 1). This metric can give us some indication of ecological processes increasing or decreasing relationships between populations and habitats (Viana and Aranha, 2008). Also of note is the average distance between spots, one measure that allows us to understand the degree of landscape fragmentation, the decline of "Forest and Semi Natural areas" 1990 to 2006 at the expense of increased "Artificial areas" (Table 1).

<figure>
<img src="../images/portugal_coimbra2.png" class="align-left" alt="portugal_coimbra2.png" />
<figcaption>Model to calculate landscape metrics in 1990.</figcaption>
</figure>

From 1990 to 2006 diversity increased, however it is known that this result is directly related to the transfer between land cover, in particular loss of "Agricultural areas" and "Forest and Semi Natural areas". The same happened with uniformity.
## 結論
調査地域は、人為的撹乱の高度に断片化の問題を提起することは注目にLecoSプラグインを使用して景観評価指標を決定することが可能でした。QGISは、任意の制約が存在しない場合に景観評価指標の計算には非常に直感的で非常に実用的であることが判明しました。それは確かに独自のソフトウェア・ソリューションに比べ、堅牢かつ実行可能です。将来的には、風景の中に自分の行動を研究するために外来種の問題を持っている分野には、この方法を適用する予定。
## リファレンス
- Fidalgo, B., R. Salas, et al. (2009). \"Estimation of plant diversity in a forested mosaic landscape: the role of landscape, habitat and patch features.\" Revista Latinoamericana de Recursos Naturales 5 (2): 65-73.
- Viana, Hélder; Aranha, José (2008) - Estudo da alteração da cobertura do solo no Parque Nacional da Peneda Gerês (1995 e 2007). Análise temporal dos padrões espaciais e avaliação quantitativa da estrutura da paisagem. X Encontro de Utilizadores de Sistemas de Informação Geográfica, 14 a 16 de Maio de 2008 -- Oeiras.
- Martin Jung (2012) LecoS - A QGIS plugin to conduct landscape ecology statistics, <http://plugins.qgis.org/plugins/LecoS>.
- Olsen, L., V. Dale, et al. (2007). \"Landscape patterns as indicators of ecological change at Fort Benning, Georgia, USA.\" Landscape and urban planning 79: 137-149.
- Turner、MG、R. Gardner、et al。（2001）。理論と実践における景観生態学：パターンとプロセス。ニューヨーク。

## 著者
<figure>
<img src="../images/portugal_coimbra4.png" class="align-left" alt="portugal_coimbra4.png" />
<figcaption>André Duarte</figcaption>
</figure>

この記事は、アンドレ・ドゥアルテによって2014年7月に寄稿されました。氏は、エンジニアリング森林資源の学位およびコインブラ高等農業学校から森林資源の修士を持っています。Geopointによって地理情報システムで大学院。現在、グルポPortucel Soporcelとの共同研究。

{{<content-end >}}
