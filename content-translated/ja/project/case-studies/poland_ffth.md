---
HasBanner: false
archived: true
date: 2016-10-30
draft: false
featured: false
section: project
sidebar: true
thumbnail: images/poland_ffth/toolbox.png
title: 欧州デジタルアジェンダ実施によるFTTH / GPONネットワーク計画のためにQGISを使用する
type: case-study

---
{{<content-start >}}
# 欧州デジタルアジェンダ実施によるFTTH / GPONネットワーク計画のためにQGISを使用する
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>October 30, 2016</span>
</p>

## 問題の定義
ここ数年、多くのEU諸国は、2010年に欧州委員会が策定した欧州デジタルアジェンダ（EAC）を実施するための運用プログラムを開始しています。2020年までのガイドラインによれば、すべてのEU​​市民は30Mbpsのインターネット帯域幅にアクセスでき、それらの半数以上が100 Mbps以上の帯域幅にアクセスできるべきです。

ポーランドは、アジェンダが実施されている国の一つです。欧州連合（EU）の資金のおかげで、多くの地方通信事業者は、高速ブロードバンドサービスに関して大手電気通信事業者と競争することができます。残念なことに、資金を申請するには、計画されたFTTH（Fiber To The Home）ネットワークの概念図の開発など、適切な文書を作成するために必要な多くの作業が必要です。

さらに、現時点では、潜在的な受益者を支援するためのGISベースのITツールは存在しません。問題の複雑さは、そのようなソフトウェアが特定のプログラムガイドライン（教育機関を結ぶ義務など）に従った文書の作成を可能にするという事実によってさらに複雑になります。

私たちは電気通信業界で豊富な経験を有しており、EUの資金を申請している企業はFTTHネットワークコンセプトマップの開発をサポートするソフトウェアの作成を依頼しました。開発されたソフトウェアによって生成された製品は、アプリケーション準備プロセスを大幅に高速化することでした。
## ソリューションの説明
高い人気、幅広いアベイラビリティ、ソフトウェアのオープン性、および非常に機能的な能力のために、私たちのソリューションの基礎となるプラットフォームとしてQGISを選択するのは自然なことでした。

FTTH Council Europeのガイドラインによれば、実際のアドレスポイントデータに基づいて、技術的側面（ケーブル、スプライス閉鎖、スプリッタの配置）と経済的側面（需要）の両方を考慮した計画を最初に準備することが重要です。建物の構造と建物の密度は、GPON（Gigabit Passive Optical Network）ネットワーク設計の技術を決定します。ネットワークトポロジを効率的に計画する能力を持たせるためには、特に以下が必要です。
- GISデータへのアクセス、
- GISデータ処理の自動化、
- ネットワーク最適化アルゴリズムの適用、
- GPONネットワークエンジニアリングルールの適用

これらの項目はすべてQGISプラットフォームで接続されていました。以下に、プロジェクトをどのように実現したのか、どのような機能項目を組み込んで一つの解決策を作り上げたのかを簡単に説明します。

私たちの目標を達成するためには、標準的なGISプラットフォーム以外の機能コンポーネントはほとんど必要ありませんでした。
- GRASS  - ベクターアルゴリズムとネットワークアルゴリズムのコレクション、
- QGISプラグイン -  OpenLayer、QuickOSM、Scipy Point Clustering、WorkContextTracer（私たちのプラグイン）、
- QGIS modeler -- tool for graphical flow modelling,
- SpatiaLite - 入出力データを格納するためのローカルデータベース。

The entire solution was based on the concept of so called wizards which realize the process of preparing the FTTx network technical concept step by step. Using \'geoprocessing\' modeller, we created models requiring only the necessary input data from operator. Algorithmic complexity was encapsulated within models in the form of designed flow, which use existing QGIS algorithms and calls dedicated scripts.

![](../images/poland_ffth/toolbox.png)

後続の分析結果が混同するのを防ぐために、WorkContextTracerというプラグインを用意しました。このプラグインは、私たちの作業をいわゆるワークコンテキストでグループ化しています。

![](../images/poland_ffth/workorder.png)

GRASSで利用可能なグラフ関数に基づくネットワークアルゴリズムは、電気通信スクリプトを追加することで充実しました。デマンドポイントを集約するためにK平均と階層的方法の両方を使用できるデマンドクラスタリングの概念を導入しました。

Geoprocessing scripts with usage of cable routing layer and Djikstra algorithm develops a cable route proposal with optical fiber nodes\' locations.

事業者は、作成されたネットワーク・ノードとアドレス・ポイントとの関連付けによって、各ネットワーク・ブランチの個別コストを見積もる必要もありました。この作業を完了するために、この操作を実行するスクリプトを作成して、ローカルのSpatiaLiteデータベースに結果を格納しました。データはスプレッドシートにエクスポート可能である必要があったため、この要件を満たすためにフリーソフトウェアライブラリを使用しました。
## ユーザーがツールを使用してFTTH / GPONネットワークプランを作成する方法
ユーザーは、新しい作業コンテキストを開き、解析されるアドレスポイントの入力レイヤーを指定することによって作業を開始しました。標準的なQGISインタフェースを使用して、ユーザーはアドレスポイント上に一連の要求を確立し、アルゴリズムのさらなるステップに必要なパラメータを最終的に提供することができます。

![](../images/poland_ffth/step1_inputlayer.png)

既存の市民インフラに関する情報がなくても、適切にフィルタリングされたOpenStreet道路ネットワークがルーティングレイヤーとして使用されました。入力パラメータを与えられたScipyアルゴリズムは、アドレスポイントを特定のクラスタへの割り当てを示す別の色でマークする需要集約に集約しました。

![](../images/poland_ffth/step1.png)

すべてのアドレスポイントがクラスタ化されているので、ユーザーは前の手順で準備したレイヤーとGPONネットワークの開始ポイントを持つレイヤーを提供する高水準ネットワーク計画のステップを開始しました。

![](../images/poland_ffth/step1-2_result.png)

Upon the completion of the algorithm, in QGIS there are geometry objects representing planned cables and splice closure locations. Basing on demand data and network topology, an additional information is stored in database such as the length of the cable, its profile, node's serving areas.

![](../images/poland_ffth/step4_results.png)

この段階で、ユーザーは既に高レベルのFTTxネットワーク技術コンセプトを開発するためのすべての情報を持っていました。最終的な部分は、いくつかの異なる視点からすべての計算データを示すデータレポートスプレッドシートを作成することでした。

![](../images/poland_ffth/report_generated.png)

![](../images/poland_ffth/report_generated_and_tranformed.png)
## 結論
QGISプラットフォームとその拡張機能のおかげで私たちは、電気通信事業者が欧州デジタルアジェンダを実装しているEUプログラムで共同融資申請書を提出するのに必要な書類を準備できる、フリーでオープンソースのソリューションを開発できました。

柔軟なベクターアルゴリズムと電気通信工学のスクリプトを組み合わせることにより、電気通信網計画に関する実際の問題を解決するための数学的アルゴリズムの実用化が可能になりました。ユーザーは、理解可能なデータ範囲（自治体、建物、道路）について操作しますが、この情報の数学モデルへの変換はユーザーからは隠れています。

ユーザーには多くの便利なメリットがあります。
- 公開されているデータおよびGPON技術工学規則に基づいた自動GPONネットワーク計画開発。
- 特定の国の特定のEUプログラムガイドラインを使用してツールをカスタマイズする機能
- 実際の寸法に対応する結果の高い正確さ。
- EU資金の申請に必要なデータの作成：ネットワークコンセプトマップ、サービスエリア割当を含むケーブルおよびスプライス閉鎖レポート。
- 各アドレスポイントを接続するコストを計算することで、ネットワークの各部分の建設コストと減価償却コストを正確に決定することができます。
- アドレスポイントを最も収益性の高いものから不採算のものへ優先順位付けする可能性。
- ROI、NPVなどの基本的な経済指標を評価する可能性。

## 役に立つリンクと文献
- <http://europa.eu/rapid/press-release_MEMO-10-200_en.htm> - information on European Digital Agenda
- <http://www.ftthcouncil.eu/> - FTTH Council Europe website
- <https://www.scipy.org/> - SciPy project website
- <https://ksavinetworkinventory.com/en/download-geospatial-network-inventory-free/>
  - tool download webpage.

## 著者
このソリューションは完全に無料のオープンソースツールです。QGISとFreeCADプラットフォームをベースとした大規模プロジェクトの一部で、電気通信業界で使用される予定です。

The author of this QGIS based solution is Softelnet (<https://www.softelnet.com>), a company manufacturing and integrating software for the telecommunications industry for over 15 years.

{{<content-end >}}
