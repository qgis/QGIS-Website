---
draft: 'true'

---
# The Research Institute for Geo-hydrological Protection of Turin \-\-- Aerial photo archive management
トリノ（IRPI）の地質・水文防災研究所、イタリアの国立研究評議会（CNR）のメンバー、では1970年にその活動を開始しました。例えば地質学や地質の研究基盤の懸念様々以下の捜査部門ので、集められたスキルを、アルパイン・ポー川水系（イタリア北部）や自然災害の監視、予測および予防の機能を備えています。これらのタスクは、ハース科学、工学、geomaticを含む学際的なアプローチの雇用によって行われています。

徹底的な調査研究を行うため、現地調査、モデリングや歴史的な記録の分析に加えて、空中フォトグラムが使用されています。それらの使用は「単純な」視覚的分析から実体図化や画像分割などの複雑な処理まで様々です。

The institute, for the explained purposes, keeps in its archive about 170000, recent and historical, photograms \-\-- the oldest one dating back to 1920s (Figure 1) \-\-- covering, in different years, the Po basin or part of it. Some photograms cover other basins in northern Italy. In addition the archives keeps flight plans of the described photograms (Figure 1).

![1929 photogram (left) and 1954 flight plan (right).](./images/italy_turin1.jpg){.align-left}
## アーカイブ管理
大量のデータに対応するため、GISのアプローチが採用されました。最初に、フォトグラムのフットプリントを示す各飛行計画がスキャンされ、ジオリファレンスされ、シェープファイル形式でデジタイズされました。次にフォトグラムは600dpiでスキャンされ、マップシート、取得年度、ストリップ番号、フォトグラムのシリアル番号とプロパティのコード（IRPI者または外部）を含むコードに応じてファイルに名前が付けられました。

eVis プラグイン（ホーニングら、2009）を使用してシェープファイルをスキャンされたフォトグラムにリンクするため、そして検索と参照のためのユーザーフレンドリーなインターフェイスを可能にするため、デジタイズされた飛行計画の各フットプリントは前述のコードを属性に入れて提供されました（図2）。フォトグラムコードに関するデータは属性テーブルのフィールドに格納され、フィールド計算機を使ってフォトグラムファイルパスを格納する「リンク」フィールドが作成されました。

![Photogram display (eVis Plugin)](./images/italy_turin2.jpg){.align-left}

また、検索可能なデータ量が多いため、地理的な検索インターフェイスが開発されました。（プロセシング、旧SEXTANTE、プラグインにある）グラフィカルモデラー機能のおかげで、開発されたツールでは、様々な選択マスクと入力ボックスを用いて、ユーザーは3つのレイヤー（行政境界、マップシート、河川）から選択したり、テーブルに問い合せて地物を見つけたり、それを使ってデジタイズされた飛行計画に空間クエリを実行し、選択された地物と交差するフォトグラムフットプリントを選択したりすることができます（図3）。この手順により、選択されたフォトグラムを特定し、前述のツールで簡単に表示したり、ファイル名やパスに基づいてフォトグラムファイルを抽出し、さらなる処理を行うことができます。

![Graphic modeler scheme used in the selection tool (in background: purple polygons-map sheets; labeled orange polygons-photogram footprints; brown polygons-municipalities administrative borders)](./images/italy_turin3.jpg){.align-left}

フォトグラムのコレクションは、（例えばGodoneら、2014）とプロの環境（図4）研究の両方で非常に重要です。今説明した手順とツールのおかげで、コレクションは完全にアクセス可能で、2009年からフォトグラムは、研究所の内部と外部の両方のいくつかのプロジェクトで採用されました。QGISの機能とプラグインは、その管理の実装で、その搾取の両方でフォトグラムアーカイブを最適化するためのツールと手順を開発できました。

![Pie chart showing different area of interest employing photograms in year 2013](./images/italy_turin4.jpg){.align-left}
## リファレンス
- Godone D., Garbarino M., Sibona E., Garnero G., Godone F. (2014) "Progressive fragmentation of a traditional Mediterranean landscape by hazelnut plantations: The impact of CAP over time in the Langhe region (NW Italy)", Land use policy, ISSN: 0264-8377
- Horning N., Koy K., Ersts P. (2009) "eVis (v1.1.0) User\'s Guide. American Museum of Natural History, Center for Biodiversity and Conservation" Available from <http://biodiversityinformatics.amnh.org/>

## リンク
- 航空写真のアーカイブウェブサイト: <http://www.irpi.to.cnr.it/index_en.php?page=aerofototeca_en>

## 著者
![Danilo Godone](./images/italy_turinaut1.jpg){.align-left height="120px"}

Danilo Godone is a Postdoc grant holder, at Turin University, studying geomatic contribution in landslide, glacier and, more generally, natural disasters monitoring. He is a member of NATRISK \-\-- Research Centre on Natural Risks in Mountain and Hilly Environments, in the same University. He acts as a freelance consultant in the same topics, too.

![Franco Godone](./images/italy_turinaut2.jpg){.align-left width="120px"}

フランコ・ゴドーネは1972年以来、トリノ地質・水文防災研究所（IRPI-CNR）の専門技術者です。アルプス地方の地形学や航空写真測量の調査やデータ分析に携わります。
