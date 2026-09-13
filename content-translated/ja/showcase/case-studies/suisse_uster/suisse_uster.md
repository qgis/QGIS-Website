---
draft: 'true'

---
# ウスター市の地理データインフラにおけるQGISの使用
ウスター市では2007年以来QGISを使っています。ArcViewに対するデスクトップGISの代替としてQGISを使用するというゾロトゥルン州の決定に後押しされ、ウスターでもそれを試してみることにしました。市は新機能を提案しテストすることで、また開発を財政的に支援することで、QGISアプリケーションのさらなる発展のための努力に参加しました。その見返りにウスターは、世界中のユーザーと開発コミュニティに裏打ちされ、急速に発展し、プラットフォームに依存しないデスクトップGISや型WebGISソリューションを受け取ります。

![](./images/suisse_uster1.png){.align-right}

PostGIS / PostgreSQLは中央地理データウェアハウスとして使用されます。他のデータベースとデータ・ソースは、このようなOGRとFMEなどのツールを使用して、定期的な間隔でPostgreSQLに複製されています。初めにQGISは、主に、ビューアとして使用しました。最初のQGISのユーザーは、農業補助金を受けるために地元の農家で作られた宣言を監督する仕事を持っていた農夫でした。その後、QGISは、編集ツールやプリントコンポーザの改善に伴い、データエディタと地図出版プラットフォームとして導入されました。私たちは他のスイスのQGISのユーザー（ゾロトゥルン、トゥーンとCDEベルン（大学））と一緒に、記号化、自動化されたラベル、属性取扱いおよびフォームをデータ駆動型でいくつかの改善に伴い、これらのツールの改良点を調整し資金提供します。 

![](./images/suisse_uster2.png){.align-right}

市の管理者はまた、市販のGISソフトウェアを使用しています：Autodesk Topobaseは、土地と地下水のインフラストラクチャデータの取得と編集、ガス、水道、電気ネットワークの管理のためのGE Smallworldです。しかし、これらは特別に訓練されたスタッフが使用しているエキスパートシステムです。他のすべてのGISプロジェクトとすべてのデータの表示は、QGISによって処理されます。

In the second half of 2010, first tests with QGIS server were carried out. In 2011 we introduced a new WebGIS system based on the QGIS WMS server and GeoExt/OpenLayers as the web client. The main reasons for the decision to use QGIS server were the considerable time savings made possible by re-using the existing QGIS desktop project configurations, rather than having to manage parallel Web project configurations. Additional advantages are the rich set of symbolization and labeling options and the consistent map rendering between the Desktop GIS application and the Web-GIS. The QGIS webclient can be tested and used at <http://gis.uster.ch/>

![](./images/suisse_uster3.png){.align-right}

現在、QGISは以下のGISプロジェクトに使用されています。
- 廃水データの表示、追加データベースの統合、運河のビデオと検査プロトコルへの直接アクセス
- モニタリングのための表示と編集、廃水と水文システムの環境と都市計画（ドイツ語：GenerellerEntwässerungsplan）
- 地下の土地台帳データ（廃水、水道、ガス、電力網、その後は電気通信も）の閲覧（ドイツ語：Leitungskataster）
- 地籍および測量データの表示
- 保護された自然の敷地の共同目録の閲覧と編集
- 都市および地域計画データの表示および編集
- 道路インフラストラクチャデータの表示と編集
- 現在および過去の居住者のデータベースから直接生成された統計の表示
- エネルギー計画の計画と可視化（ガス供給地域、廃水からの熱利用、地表付近の地熱、ブロック加熱ステーションなど）

さらなるプロジェクトが現在開発中です。

![](./images/suisse_uster4.png){.align-right}

2007年には、どんなペースでQGISがさらに開発されるか、コミュニティと商用サポートの両方がどのように進化するかは、完全に明確ではありませんでした。今日では、QGISコミュニティによって為された開発と改善の速度は私たちの期待を超えたと述べることができます。企業Sourcepoleとマッドファットワイフからのコミュニティや商用サポートが優れています。製品管理や販売チームが離れて遮られることなく、開発者との直接通信があります。これら両社の開発者は、QGISプロジェクトの開発をリードし、コードベースの優れた知識を持っています。

バグは報告した後でしばしば数時間または数日内に修正されており、新規開発が短期間で実装されています。新機能は開発した直後にテストされ、品質がエンドユーザーにとって十分である時はいつでもユーザーに展開することができます。公式のソフトウェアリリースを待つ必要はありません。私たちは、ライセンス管理に対処しなくても、プロジェクトに影響を与え、好きなだけ多くのコンピュータにソフトウェアをインストールできる自由を享受します。私たちはQGISコミュニティとQGISプロジェクトの発展のために私達の商業的支援者との将来のコラボレーションを楽しみにしています。
## 著者
![Andreas Neumann](./images/suisse_usteraut.jpg){.align-left height="200px"}

この記事はアンドレアス・ノイマン博士が2011年4月に寄稿しました。氏はスイスのウスター市でGISコーディネーターを務めています。
