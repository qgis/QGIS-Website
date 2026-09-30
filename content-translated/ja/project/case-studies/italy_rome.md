---
HasBanner: false
archived: true
date: 2015-03-01
draft: false
featured: false
section: project
sidebar: true
thumbnail: images/italy_igag1.png
title: 第１レベルの地震マイクロゾーニングの分析を簡素化するQGISのジオプロセシングモデル
type: case-study

---
{{<content-start >}}
# 第１レベルの地震マイクロゾーニングの分析を簡素化するQGISのジオプロセシングモデル
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>2015年3月1日</span>
</p>

米国学術研究会議（CNR）の環境地質とジオエンジニアリング研究所（IGAG）は、ローマ市の「ローマ1」研究エリアに位置しています。それは、それぞれの専門分野で40年以上にわたり活動していた5つの元研究機関やセンターの再編によって2002年に設立されました。IGAGは地球科学の分野で科学的なトピックの広い範囲をカバーしており、主に次の研究に焦点を当てています：
- 汚染された土壌及び水の地球化学環境および修復;
- 廃水の処理を含む鉱床および鉱物処理、;
- 岩の発掘調査のジオエンジニアリングおよび安全性。
- 最近の地質学的進化。
- 自然災害の軽減;
- 地質学と考古学。
- 海洋地質学
- 空間情報科学、GIS解析と開発。

ピエトラモンテコルヴィーノ地域（南イタリアのプーリア、中南部アペニン山系に沿って位置する）のレベル1地震マイクロゾーニング研究はプロジェクトの一部で、プーリアの流域機関（プーリアADB）およびバーリ大学の地質・地球物理学部（DGG）との共同で、フォッジャの地域の63の自治体の地震マイクロゾーニングを目指しました。この活動は、イタリア市民保護局（DPC）が推進し、経済計画のための省庁間委員会（CIPE n.20/2004）によって融資されました。
## 第１レベルの地震マイクロゾーニングの研究のためQGIS]ジオプロセシングツール
地震マイクロゾーニングは、ローカルスケールでの地震ハザードを評価し、均質な地震の行動によって特徴づけられる領土の領域を特定することを提案します。地震マイクロゾーニングの第１レベルは、岩相の特性と地域のこれらの部分（マイクロ領域）を特徴付ける地質学的単位の幾何形状を定義するという目的を有します。

地震による被害を観察すると、多くの場合、地質構造だけでなく、建物の構造のさまざまな品質や種類を原因とする局地的なスケールでの多様性が見え、これが結果としてさまざまな地震災害になります。

地震マイクロゾーニングは均質な地震挙動で特徴付けられる領土の領域の同定を通じて、局地的な地震動を評価します。

地震マイクロゾーニングのためのガイドラインおよび基準2008（<http://www.protezionecivile.gov.it/jcms/it/view_pub.wp?contentId=PUB1137>）では、イタリアの領土の地震マイクロゾーニング研究のための基準を提供します。それらは深さを3レベル（1〜3）で区別します。

第１レベルの地震マイクロゾーニングは3つの主題図の作成で構成されています。
1. 地震マイクロゾーニング研究のための調査を含む調査マップ。
2. 調査に関連する既存の、岩相層序および地質データを統合詳細なスケール地質及び地形図から得られたジオ岩相図。
3. ローカル危険の三つのカテゴリーにマイクロ領域を識別レベル1地震マイクロゾーニングマップ（レベル1マイクロゾーニングの主生成物）。
   - 安定したゾーン。
   - 接地増幅しやすい安定したゾーン。
   - 不安定ゾーン。

この研究の範囲は、オープンソースツールを使用して、レベル1地震マイクロゾーニング地図の起草に向けた地形、地質学、地球物理学および地理技術データを処理するための方法論の創造に貢献することです。

QGISの最新バージョン（執筆時点では2.8.1）に統合グラフィカルモデラーツールは、単純なジオプロセシングモデルの作成に使用されてきました。このツールは、一般的にレベル1地震マイクロゾーニングマップの作成のために実行される分析のいずれかを自動化するために、特にポリゴン地物として不安定なゾーンを識別するために有用です。

モデルは、異種GFOSS（地理空間フリーおよびオープンソースソフトウェア）ツール（図1）のための簡略化と統一されたインタフェースとしてQGISの有用性を実証し、さまざまなオープンソースソフトウェアやライブラリ（GRASS、GDAL、QGIS）を利用します。

<figure>
<img src="../images/italy_igag1.png" class="align-right" alt="italy_igag1.png" />
<figcaption>(Fig. 1) Screenshot from the geoprocessing model.</figcaption>
</figure>

モデルが入力として取るものは（図2）：
- 標高値を持つフィールドを含む等高線のシェープ
- 標高値を含むフィールドの名前
- DEMと傾斜に対するメートル単位での望ましいラスタ解像度（デフォルトは10）
- 15度超の勾配を持つ領域に交差する地物を抽出するポリゴンシェープファイル
- 結果のポリゴンレイヤーの名前

<figure>
<img src="../images/italy_igag2.png" class="align-right" alt="italy_igag2.png" />
<figcaption>(図2) モデル入力フォーム（左）と実行ログ（右）。</figcaption>
</figure>

起動すると、モデルは、次の操作を実行します。
- GRASSツールv.to.rast.attributeは、等高線シェープファイル、Zフィールドの名前およびラスター解像度を入力として取り、等高線をラスターに変換します；
- GRASSツールr.surf.contourは、前のステップからのラスター化された一時出力およびラスター解像度を入力として取り、標高モデルを作成します。
- GDALツール「gdaldem」は標高モデルから度で表される勾配を作成します。
- GRASSツールr.mapcalculator式を使用して、（この値はマイクロゾーニングガイドラインで符号化され、そしてそれは固定されている）を15度よりも大きい勾配を有する領域を識別する1ビットラスターを生成するために使用されます。

if(A\>15,1,null())

ここでAはgdaldemによって生成された一時的な勾配ラスタです。
- GDALツール「gdal_polygonize」は1ビットラスターをポリゴンに変換します;
- 15度以上の傾きを持つ領域と、選択された交差レイヤーをオーバーレイするため、QGISツール「交差」が使用されます。

結果は、地滑りポリゴンレイヤー（図3）または岩相地図といった主題図から自動的に抽出された、勾配値が15度よりも大きい不安定になりやすい領域を有するポリゴンレイヤーです。

<figure>
<img src="../images/italy_igag3.png" class="align-right" alt="italy_igag3.png" />
<figcaption>(Fig. 3) The model output (in red) shows highly unstable areas extracted from a landslides layer (orange).</figcaption>
</figure>

## 結論
この作品は、QGIS、GRASS、GDAL/OGR、のようなオープンソースGISツールが、初級レベルの地震マイクロゾーニングの研究を目的とした空間分析とデータ処理に正常に使用できることを明らかに実証しています。この例の作業では、QGISは異なる高品質GFOSSツールの簡易な統一インタフェースとして使用されてきました。グラフィカルモデラ－でジオプロセシングモデルを直感的に構築し、それを高価なソフトウェアのライセンスを必要としないポータブルでクロスプラットフォームなツールとして簡単に共有できます。そのツールは、QGISのモデリング機能を活用して異なるアルゴリズムを視覚的に連鎖させ、入力および出力パラメータを定義し、中間データ出力を管理するタスクはソフトウェアに残しています。GRASSアルゴリズムを使用するためにGRASSデータベースと地図セットを定義したり使用する必要はなく、モデルの設計を大幅に簡素化できます。今後の開発には、オープンソースのソフトウェアに基づいたツールとモデルのパッケージの作成が含まれ、それは地震マイクロゾーニングの研究のために必要な空間解析作業を簡素化し高速化するために使用できます。
## リファレンス
- G. Baldassarre; Gallicchio, S.; Giannandrea, P. & Tropeano, M.: \"Relazione Finale Geolitologica per la microzonazione sismica di livello 1dei Comuni della Provincia di Foggia Dipartimento di Geologia e Geofisica dell\'Università di Bari, 2011\"
- Cavinato,G.P.; Cavuoto, G.; Coltella, M.; Cosentino, G.; Paolucci, E.; Peronace, E. & Simionato, M.: \"Studio di fattibilità per il monitoraggio e la messa in sicurezza delle aree urbane a rischio di stabilità statica e vulnerabilità strutturale del Comune e della Provincia di Foggia -CIPE 20/2004 Consiglio Nazionale delle Ricerche - Istituto di Geologia Ambientale e Geoingegneria, 2013, 526\"
- Contributi per l\'aggiornamento degli \"Indirizzi e criteri per la microzonazione sismica \" 2008. Ingegneria sismica, Pàtron Editore Bologna, 2011 (<http://www.protezionecivile.gov.it/jcms/it/view_pub.wp?contentId=PUB28083>)
- Gruppo di lavoro MS, 2008. Indirizzi e criteri per la microzonazione sismica. Conferenza delle Regioni e delle Province autonome - Dipartimento della protezione civile, Roma, 3 vol. e Dvd, Presidenza del Consiglio dei Ministri, Dipartimento di Protezione Civile, 2008, 424. (<http://www.protezionecivile.gov.it/jcms/it/view_pub.wp?contentId=PUB1137>)

## 著者
この記事はジュゼッペ・コセンティーノとフランチェスコ・ペニカ（ www.igag.cnr.it ）によって2015年3月に寄稿されました。

<figure>
<img src="../images/guiseppe_cosentino.png" class="align-left" height="200" alt="guiseppe_cosentino.png" />
<figcaption>Giuseppe Cosentino</figcaption>
</figure>

Giuseppe Cosentino \<<g.cosentino@igag.cnr.it>\> is geologist and technologist specializied in Geographic Information Systems for the management of geological and engineering hazards. Currently working in the field of seismic microzonation and environmental characterization of the lands in contaminated sites. Areas of interest: geological and environmental hazards, cartography, structural geology, explorative drillings.

<figure>
<img src="../images/francesco_pennica.png" class="align-left" height="200" alt="francesco_pennica.png" />
<figcaption>Francesco Pennica</figcaption>
</figure>

Francesco Pennica provides GIS and WebGIS software development and data management: GeoServer, MapServer, ArcGIS Server, GeoNetwork OGC standard based webgis services, Java, HTML, CSS, Javascript, Python, PHP languages and frameworks, WebGIS front-end development with OpenLayers, ExtJS, GeoExt, JQuery, GWT, Ext-GWT, Google Maps API SQL, geodatabase management, PostgreSQL, PostGIS, GIS desktop software based analysis and scripting (ArcGIS, GRASS, GFOSS tools), Software configuration and management in Linux and Windows based servers and desktops.

{{<content-end >}}
