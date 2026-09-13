---
HasBanner: false
archived: true
date: 2015-02-01
draft: false
featured: false
section: project
sidebar: true
thumbnail: images/europe_lynx1.png
title: 南カルパチアでのオオヤマネコの生息環境解析
type: case-study

---
{{<content-start >}}
# 南カルパチアでのオオヤマネコの生息環境解析
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>February 01, 2015</span>
</p>

オープンソースのデータに基づいて、学生のための野生生物の生息地のモデリングの基本的な理解を促進するためのケーススタディ。
## 前書き
Challenged with the task of GIS based modeling for the first time, a working group of undergraduate forestry students of the University for Sustainable Development Eberswalde (HNEE) conducted literature research for habitat suitability and behavior of the Eurasian Lynx (*Lynx lynx*). In the module 'Applied GIS in Natural Resource Management', under the guidance of Prof. Mund, the students quickly discovered the subject's complexity, especially within regard to the adaptability of species to changing environments. With limited research published in English about lynx habitat on the Romanian side, we continued the project based on only freely available data sets and open-source software, aiming to establish conceptual knowledge of habitat modeling, strengthening skills on widely applied QGIS tools and to create a **basic expert model** in the process.
## 方法論
すべての収集されたデータは、ETRS89 / ETRS-LAEAに投影してQGIS 2.6および2.8で処理され、EUの基準を満たすためにINSPIRE指令に従って保存されました。重みの全体 **離散指数** が定義され、すべての入力データに適用されました。

<figure>
<img src="../images/europe_lynx1.png" alt="europe_lynx1.png" />
<figcaption>Figure 1: Workflow - Lynx habitat expert model</figcaption>
</figure>

**ワークフローの説明**
- Area of Interest \[Step I -- II\]: Based on selected national park areas and adding a 10 kilometer buffer, a minimum bounding box \[α\] was created and clipped with the outline of the river Danube (derived from Corine Land Cover 2006). Further clipping tools \[β\] were applied to all additional data as an initial preparation step (Figure 2)
- Land Cover Suitability Model \[Step IX\]: \[γ\] Input III and IV were transformed into shape files using the inbuilt #Polygonize function. Corine Landcover (2006) data was reclassified using the field calculator to group land use classes and assign respective index values. Similar processing was applied to Hansen Forestcover data (2000), extracting only areas of cover equal or higher 75 %. Sub-model IX was produced by using the functions #Merge Shapes to combine III with IV and #Rasterize

*注：土地被覆クラスはオオヤマネコの発生の可能性と人間の活動によって分類しました。技術的には古い起源のものですが、森林値に関連する情報が、生息地の改善を示すために、空間データセットを結合するための一般的な例として、統合されました*
- Habitat Suitability Model \[Step X\]: \[δ\] An Elevation Suitability Index was derived from the AsterDEM 2.0 \[VI\] and together with a Population Density Index \[V\] was integrated into the final habitat suitability model (Figure 3) by using the #Raster calculator

```
    Cover Suitability Model * Population Density Index * Elevation Suitability Index
```
*Note:Defining forest (\>= 75 % cover) as best suitable and using the elevation data to reduce index values above assumed tree line is conceptually related to habitat of deer as the main prey*
- Potential Hunter Accessibility Model \[Step XI\]: Applying the #Terrain analysis tool \[ε\], a slope layer was extracted from the DEM data and combined \[η\] with a road distance layer, which was produced by processing rasterized OSM road data within the #Proximity function and index values assigned using #Reclassify grid values

```
                          Slopelayer
    Road distance * ( 1 + ----------- )
                             100
```
- Conservation Value Model \[Step XII\]: Is the result of the #Raster calculator function: (Figure 4)

```
    (Habitat Suitability Model * Hunter Accessibility Model)
    --------------------------------------------------------
                           2
```
*注意：狩猟者接近可能性モデルでは、さらに道路への距離があったり傾斜が増加することによって領域へ接近する狩猟者が減少する可能性を示さなければなりません*

<figure>
<img src="../images/europe_lynx2.png" alt="europe_lynx2.png" />
<figcaption>Figure 2, 3 and 4</figcaption>
</figure>

## 結論
最終的な出力（図3）を見ると、もっともらしい最初の潜在的な生息環境の分析は成功しているように見え、さらにより重要なのは、基本的なモデル作成自体が当初予想より難しくないことが判明しました。狩猟者接近可能性のためのサブモデルを追加するには私たちの選択は、私たちは、単に既存のシナリオの中に入れ子にし、例えば、インフラ開発の側面の下で保護必需品を決定するために使用することができる生息地のリスク評価、という点で別の次元を実装することができました。しかし、このような森林の構造（私たちの最高の生息環境適合性）など、いくつかの重要な生息地の情報は、利用可能なデータセットによって導出することができず、複雑な種の挙動との組み合わせで、結果はそのための基本と不完全なものとして理解されなければなりません。この段階では実装されていない追加の要因は、道路の死亡率、地形の凹凸や詳細な獲物が発生しています。

QGISソフトウェアは、そのオープンソースで無料でご利用いただける性格以外にも、近年の主要な開発の対象となっています。私たちも、経験の浅いユーザーのために、様々なGRASSとSAGAツールの使用が可能、ツールボックスの統合と非常に肯定的な経験をしました。互換性の問題は、データセットを直感的に作業する際の強力な利点することができ、異なるバージョンや行政規制の一般的な不在の間で頻繁に変化するにもかかわらず発生していません。私たちは、特に統合モデルビルダーに関しては、さらなる改善を見て楽しみにしています。
## リファレンス
- Kaczensky, P., Chapron, G.,von Avrx, M., Huber, D., Andrén, H. & Linnell, J. (December 2012): Status, management and distribution of large carnivores in Europe. Document European Commission.
- Schadt, S., Revilla, E., Wiegand, T., Knauer, F., Kaczensky, P., Breitenmoser, U., Bufka, L., Cerveny, J., Koubek, P., Huber, T., Stanisa, C. & Trepl, L. (2002): Assessing the suitability of central European landscapes for the reintroduction of Eurasian lynx. Article Journal of Applied Ecology.
- Salvatori, V. (2004): Conservation areas for large carnivores in the Carpathian Mountains. PhD Thesis.
- Podgórski, T., Schmidt, K., Kowalczyk, R. & Gulczyñska, A. (2008): Microhabitat selection by Eurasian lynx and its implications for species conservation. Acta Theriologica 53: 97--110.
- Boutros, D. (March 2002): Characterization and assessment of suitability of Eurasian lynx (Lynx lynx) den sites. KORA Report No. 12e, Diploma thesis.

### 著者
アンジェラDichte、ルカEhrminger、シルヴァーナ・ガルシアTravesiレイエス、トビアスホッペとデビッド・ウィンガーは、研究プログラム国際森林生態系管理の学士号、第四学期の学生であり、アンGnilkeとヘンリ・ヒルツナンはそれぞれドイツ林業大学と、フィンランドのミッケリ応用科学大学からの交換留学生です。Mund教授は、2010年以来、HNE EberswaldeでGISやリモートセンシングを講義し、プロジェクトに指導し、技術サポートを提供しています

Please contact Luca.Ehrminger(at)hnee.de, David.Winger(at)hnee.de, or Prof.Dr.Jan-Peter Mund: Jan-Peter.Mund(at)hnee.de for further information.

{{<content-end >}}
