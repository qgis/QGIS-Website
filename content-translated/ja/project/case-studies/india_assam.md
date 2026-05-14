---
HasBanner: false
archived: true
date: 2013-03-01
draft: false
featured: false
section: project
sidebar: true
thumbnail: images/india_assam1.png
title: (NAMERIトラ保護区、アッサム、インドSonitpur地区におけるカメラトラップを使用して）トラを監視するためのQGIS
type: case-study

---
{{<content-start >}}
# (NAMERIトラ保護区、アッサム、インドSonitpur地区におけるカメラトラップを使用して）トラを監視するためのQGIS
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>March 01, 2013</span>
</p>

Nameri Tiger Reserve (NTR) is one of the 3 tiger reserves of Assam and it is situated in the northern part of Sonitpur District of Assam along the foothills of Eastern Himalayas. Spread over an area of 344 sq km, NTR boasts rich diversity of flora and fauna. The core area of the reserve which constitutes the "Nameri National Park" is bound by River Jia-Bhoreli on the west and River Bor-Dikorai in the east. To the north of the Nameri lies the Pakke Tiger Reserve of Arunachal Pradesh.

![](../images/india_assam1.png)

この風景の中で、環境保全の重要性の主要な種はロイヤルベンガルトラ、アジアゾウ、インドのバイソン、共通のヒョウ、ウンピョウ、ワイルドドッグ、サンバー鹿、吠え鹿、豚、鹿、イノシシや他のいくつかの種です。NTRの鳥の多様性にも非常に印象的で、370以上の鳥種はこれまでに同定されています。準備金は、アッサムのアッサム森林局、政府によって管理されています。
## カメラトラップ調査を設計するためのQGISの応用
2011年から開始し、インドのナショナル・トラ保護庁（NTCA）は、必須の国のすべてのトラ保護区がカメラトラップを使用してトラを監視するために作られました。この新しいプロトコルの下では、カメラの25ペアは、トラ保護区の100平方キロのためにインストールされ、サンプリング周期は40〜60日です。この新しいトラの監視プロトコルは、GISに大きく依存しています。

<figure>
<img src="../images/india_assam2.png" class="align-right" alt="india_assam2.png" />
<figcaption>Picture of a male tiger that was captured in one of the camera traps</figcaption>
</figure>

2012～13年の間に、当社はQGISを使ってNTRでこの新しいトラの監視プロトコルを実装しました。まず、私たちはQGISでNTR境界をデジタル化し、ポリゴンとしてそれを保存しました。この境界ポリゴンは現地調査の際に、ナビゲーションの目的のためにGPSに書き出しされました。私たちは、トラの存在などpugmarks、スクラッチマークや糞の証拠のためのNTRで豊富な看板調査を実施しました。トラの兆候並びにカメラトラップに適した場所のGPS座標を記録しました。調査の完了後、データは、さらなる処理のために、カメラトラップの位置を確定するためのGPSツールを使用してQGISに移しました。トラの兆候と考えられるカメラトラップの位置を含むシェープファイルを作成しました。

<figure>
<img src="../images/india_assam3.png" alt="india_assam3.png" />
<figcaption>Block wise distribution of camera trap locations and assigning camera traps to different forest camps by using voronoi polygons &amp; hub distance.</figcaption>
</figure>

Next we prepared 4 sq km grid layer using mmqgis plugin. The shape file containing results of sign survey was overlaid on the 4 sq grid to visualise the distribution of camera traps in NTR. Distance matrix option under vector analysis tools was quite handy for determining the inter camera distance. Camera locations having less than 1.8 km inter distance were removed to comply with the monitoring protocol. Due to lack of sufficient cameras to monitor the entire reserve area in one go, we decided to divide the reserve area into 2 blocks of 100 sq km each. Boundaries of these blocks were digitised and saved as separate shape files for both the blocks. Using RGB composition plugin, a false color composite of the reserve was created and the sign survey shape file overlaid to assess the habitat types used by the tiger. During the study period, the camera traps have to be monitored intensively by the field staff. To ensure smooth functioning of monitoring process, we used Voronoi polygon feature of Geometry tools and hub distance of mmqgis plugin for planning logistic requirements. The geographic coordinates of camera traps are required for estimating the tiger density and occupancy modelling of other species. These coordinate details were easily generated from camera trap shape files by using the "Export/ add geometry columns" feature of vector Geometry tools.

<figure>
<img src="../images/india_assam4.png" class="align-right" alt="india_assam4.png" />
<figcaption>Survey grids with tiger presence</figcaption>
</figure>

## 結論
For the first time in the history of this small tiger reserve of North East India, it was possible to monitor tigers by using camera traps mainly because of QGIS. Results of this monitoring exercise indicate the presence of 8-15 tigers in this landscape. In addition to the tigers, several elusive species have also been photographically documented. Apart from tiger monitoring, we are also using QGIS for activities such as planning habitat management works, revising patrolling schedules, and designing maps for visitors. The user-friendly interface, rich features, in-depth documentation, on-line support and the free/open source philosophy are the few qualities of QGIS that made us to select it over other proprietary software. We believe that QGIS has great potential for empowering individuals/institutions/ involved in conserving endangered wildlife in the developing world by offering GIS technology at little or no cost.
## 著者
<figure>
<img src="../images/india_assamaut.png" class="align-left" height="200" alt="india_assamaut.png" />
<figcaption>Rajendra Garawad</figcaption>
</figure>

この記事は2013年3月にラジェンドラ・G. Garawadによって寄稿されました。氏はNAMERIトラ保護区、アッサム、インドのフィールドディレクターです。森林科学と保全＆土地管理のマスターの学位を保持しています。

{{<content-end >}}
