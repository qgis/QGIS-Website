---
draft: 'true'

---
# QGISでナイジェリアにおけるアムルム森林保護区と鳥相の地図を作成
Amurumの森林保護区は、ヨス、高原状態、ナイジェリアの都市の近くに位置しています。それは自然の保全、教育や研究の目的のためにアップ・レベンティス鳥類研究所（APLORI）の開始と併せて設立されました。APLORIはヨスの大学の動物学の部門によってホストされています。毎年、すべてのナイジェリアにわたり保全生物学の訓練を得るから約8意欲的な学生のグループ、（R付き）と同様に2011 GISのなどの統計。2011年12月に2週間の間、私たちは、基本的なGISの概念を学び、さまざまな環境保全のためにQGISを有するものを適用します。この記事では、私たちが生息地とAmurum準備金のその決定要因とどのように基本的な生息地図が効率的に生物多様性などの鳥類相の空間分布を決定する目的のために地層を取得するために使用されたを地図化するためにQGISを使用する方法について説明します。

![Training Group](./images/nigeria_jos1.jpg){.align-right}
## 高度、山陰、斜面および生息地を地図化
1) Mapping elevation and groundtruthing: We downloaded (free) elevation data originating from the NASA Shuttle Radar Topographic Mission (SRTM) for the area in which Amurum is located. (Information about the global elevation data set can be found here: <http://www.cgiar-csi.org/data/elevation/item/45-srtm-90m-digital-elevation-database-v41>).
2) GdalToolsは、元のデータセットをマージして、ラスターデータセットが比較的小さいままであったように予備を含む小さな領域をクリップするために使用しました。GPSを用いて、私たちは準備中の様々な場所で標高を収集しました。
3) 全体として、SRTMデータセットの上昇は、GPS収集上昇によく対応していました。GdalToolsにおける地形モデルは、地域のために丘のハデスとスロープを計算するために使用しました。彼らは強く生息地のタイプに関連付けられているため、これらの変数は、エコロジーの観点からも重要です。

![QGIS screenshot](./images/nigeria_jos2.jpg){.align-right}
4) 私たちは格好良い地図を開発することを意図しているので、私たちはより高解像度の地図を取得する（クリッピング）標高地図を元に補間しました。私たちはGdalTools中のワープツールを使用しました。等高線ツールによって、私たちは滑らかな等高線を得ました。
5) 予備の境界の座標は、GPSで予約の境界に沿って歩くことによって得ました。GPSに格納されたウェイポイントとトラックが円滑にGPSツールを使用してインポートしました。輸入ウェイポイントとトラックは、ポリゴンシェープファイルを構築するために使用されました。保護区内のトラックは、同様の方法でマッピングしました。
6) 私たちは、迅速かつ正確に、私たちはOpenLayersをプラグインで、ワークスペースに入った、Googleの衛星画像を使用してAmurumの生息地図を構築できました。サバンナ、ギャラリー森とロッキー露頭：準備は明確な生息地の3種類があります。衛星画像に基づいて、私たちは3つの生息地を区画するポリゴンを描画するためのエディタを使用していました。スナップオプションを設定すると、正しく、非重複ポリゴンの構築を可能にしました。

## 鳥の分布と多様性のマッピング
生息地の地図はランダムな位置を生成するために使用されました。生息地の様々なタイプの面積は、各生息地のタイプ（層化）の表面に比例した位置の数を生成するために使用しました。

![Training Group](./images/nigeria_jos3.jpg){.align-right}

The random points in fTools were used for this purpose. All the locations were visited during two mornings by four groups of students (2 per group) giving a total of 38 random locations dispersed throughout the reserve. The observation data were entered in a spreadsheet and analyzed using R. In addition, the Shannon-Wiener diversity index was calculated using R. After merging the location file with the resulting observation data it was exported as a csv file which was loaded into QGIS using the "Add delimited text layer" tool. On the basis of the above mentioned layers a map was constructed presenting some of the most important landscape features and avian diversity of the Amurum reserve.
## 結論
全体として、このコースは大きな成功を収めました。 - GISの経験がなかった学生グループである私たちは  \-\-- QGISでの作業をとても楽しみました。わずか2週間で、保護区の非常に有用な地図を作成することができました。特に、さまざまな生息地の範囲が特定され、層別化が可能になったことで、さまざまな生物の個体数をより精度高く推定できるようになりました。基本的に、私たちはオープンソースプラットフォームとしてQGISを活用することで、より高度な生態学的研究ができるようになりました。

![QGIS map: Diversity of Amurum Forest Reserve](./images/nigeria_jos4.png){.align-right}
## 著者
アベンゴー・エイモン・チアディカビ、アデヤンジュ・テマディ・エスター、アキエネン・ネリオヤ、アルバート・マランガレ・タウエエ、アジ・アボク・ジョエル、エチュード・ダニエル、エルフ・フォルマー、ネオグ・チマ・ジョシア、オノア・ジョセフ・ダニエル、
