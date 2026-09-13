---
HasBanner: false
archived: true
date: 2012-01-01
draft: false
featured: false
section: project
sidebar: true
thumbnail: images/portugal_lisbon1.jpg
title: QGISを使用して生物多様性と生態系サービス（HABEaS）のホットスポット地域を地図化する
type: case-study

---
{{<content-start >}}
# QGISを使用して生物多様性と生態系サービス（HABEaS）のホットスポット地域を地図化する
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>January 01, 2012</span>
</p>

HABEaS —— Hotspot Areas for Biodiversity and Ecosystem Services is an online geographic information system (WebGIS) that was created by the [Centre for Applied Ecology](http://www.isa.utl.pt/ceabn/content/2/123/homepage) ([Instituto Superior de Agronomia](http://www.isa.utl.pt/home/), Technical University of Lisbon), Worldwide Fund for Nature (WWF) and Faunalia.

このプラットフォームの主な目的は、地中海流域の生物多様性と生態系サービスに関するさまざまなデータに自由にアクセスできるようにすることです。現在、HABEaS WebGISはポルトガルの南部をカバーしていますが、2012年末/ 2013年初めにはポルトガルの北部とボスニア・ヘルツェゴビナのTuzla Cantonまで拡張されます。長期的には、このツールを地中海の流域全体に広げたいと考えています。

![](../images/portugal_lisbon1.jpg)

Since the main goal of this tool is to promote free and easy access to information on biodiversity and ecosystem services we decided to use only free and open source software, that any person or entity can use regardless of their location or financial constraints. The website where HABEaS WebGIS is hosted on a server that runs Debian Linux and was developed with Drupal CMS. PostgreSQL/PostGIS was used to store the data and QGIS was used to process and analyze the GIS that we obtained from several entities. We used both QGIS\'s native tools but also GRASS GIS and SAGA GIS tools through the GRASS plugin and SEXTANTE Toolbox.

![](../images/portugal_lisbon2.jpg)

HABEaS に含まれている地理情報は、ポルトガルの南部の高保護価値森林（HCVF）を識別するサポートを提供するためにWWFによって使用されてきました。これは所有する森林について森林管理協議会（FSC）認証を受け取りたい土地所有者には必須のステップです。

![](../images/portugal_lisbon3.jpg)

各プロパティでどの保存値が発生しているかを調べるために、SEXTANTE モデラーを使用して、すべてのHABEaSレイヤーとプロパティの境界線と交差させるスクリプトを作成しました。同じツールを使用して、現在各プロパティに格納されている炭素量を自動的に計算するスクリプトも作成できました。

![](../images/portugal_lisbon4.jpg)
## 結論
QGISは使いやすく、非常に強力なジオプロセシング機能を備えています。SEXTANTE ToolboxによるGRASS GISツールとSAGA GISツールの統合により、多数の複雑な空間解析を実行し、SEXTANTE Modelerを使用してそれらをパイプライン化することができました。また、新しいプリントコンポーザで高品質の地図を作成することも、強力なオープンソースのベクターグラフィックスエディタであるInkscapeでさらに編集するためにSVG形式でエクスポートすることも非常に簡単でした。

In general, our experience with QGIS has been very positive, the software runs smoothly and the community is very active and supportive. Reported bugs are usually resolved shortly after being reported by users and QGIS developers are always willing to listen to "end user\'s" needs and suggestions.
## 著者
<figure>
<img src="../images/portugal_lisbonaut.jpg" class="align-left" height="200" alt="portugal_lisbonaut.jpg" />
<figcaption>Filipe Dias</figcaption>
</figure>

Filipe Diasは、応用生態学センター（リスボンのテクニカル大学研究所）と自然界のための地中海プログラム（WWF）のコンサルタントである応用生態学センターの博士課程の学生です。

{{<content-end >}}
