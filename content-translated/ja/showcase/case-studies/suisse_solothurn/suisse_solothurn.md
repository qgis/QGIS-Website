---
draft: 'true'

---
# スイスのゾロトゥルン州の政府FOSSGISスタックにおけるQGIS
![](./images/suisse_solothurn1.png){.align-left}

ゾロトゥルン州では25万人のゾロトゥルン市民へのサービスおよびインフラストラクチャを提供します。2001年に州議会は、WindowsからLinuxへ移行することを決めました。動機は自由企業を奨励し、ライセンスコストを削減するために、ある特定のベンダーから独立しているようにしました。その結果、SO！ゾロトゥルン州のGIS部門はFOSSGIS戦略超える3500人の従業員のGIS-要件を実現するために始めました。

私たちが取った第一の段階は、UMNのMapServerの導入およびすべての3500人の従業員のためのWebGISのクライアントを使用して簡単に提供していますSO!MAPクライアントの作成でした。第二の段階は、PostGISの空間データベースエンジンへのシェープファイルからのすべての私達の地理空間データの移行でした。導入は非常に成功しましたが、使いやすいデスクトップGISがありませんでした。

異なるデスクトップGISの評価の後、私たちは2006年にESRIのArcInfoおよびArcView3を置き換え、GRASSと一緒にQGISを使用することにしました。

この決定は以下の側面によって推進されました：
- Due to our use of desktop GIS in a Linux Terminal Server environment, Java wasn\'t an option.
- OSGeoプロジェクト - 組織
- ドイツ語で翻訳されたGUI
- ドイツ語で書かれた文書
- スイスのゾロトゥルン近くのアクティブな開発者（Marco Hugentobler）。
- 私たちは、デジタイザや地図作成などの不足している機能を実装するためにMarco Hugentoblerと契約することができました。
- Pythonによるアプリケーションとプラグインの開発
- ユーザーコミュニティの拡大
- 非常にアクティブな開発者コミュニティ
- 単一のオペレーティングシステムからの独立性

## どこでQGISを使うのですか？
UMN MapServerのがサービスを提供インタラクティブマップとは対照的に、デスクトップGISは、ゾロトゥルンの地理空間データの柔軟なビューを提供しています。QGISデスクトップGISは、日常業務のための50人の以上のユーザーによって使用されています。しかし、それらの多くは、GISの専門家ではありません。彼らは、視覚化および/または直感的なユーザーインターフェイスと地理空間データを取り込みたいです。

One of the most important Desktop GIS issues is the question: \"How do I get the information from the PostGIS geodata repository I need?\". Since our end users are unfamiliar with data models and the underlying structures of our spatial database, offering the users a raw connection to the PostGIS DB was not an option. We have a metadata database that stores the descriptions of all production data called \'SO!DATA\'.

SO！DATAは人間可読データモデルの在庫が含まれており、非GIS-エキスパートユーザーは彼らが必要とする情報を発見するためにこのデータベースを使用できます。

![\"SO!GIS Layer\" plugin developed at the Canton of Solothurn](./images/suisse_solothurn2.png){.align-right}

To remove the need for end users to interact directly with PostGIS connections and table selection dialogs, a plugin has been developed in python. The plugin is called \"SO!GIS Layer\" (see Figure 1). The plugin connects to the SO!GIS PostGIS repository, gets the information of all published geospatial data layers from SO!DATA and offers the user a GUI to find the data layers they need. With this infrastructure in place, our users are happy \-\-- they can prepare for geoprocessing, editing and map composing in an individual way.

![\"SO!GIS Suche\" plugin developed at the Canton of Solothurn](./images/suisse_solothurn3.png){.align-right}

Another required QGIS plugin we created is called \'SO!GIS Suche\'. This provides the possibility to search for locations like townships, addresses or cadastral parcels (see Figure 2). As a result the user is able to navigate very easily to an area of interest.

At the moment many other plugins are under development. These will support data manipulation, analysis or mapping for different projects. Our in-development plugins cover topics such as nature reserves, soil conservation, cadastral data verification, crisis management, abandoned sites and so on.
## 結論
Today we can say that using QGIS was the right decision for us. QGIS offers most of the features requested by our users. The Canton of Solothurn subcontracts the creation of features that QGIS lacks to commercial support providers. With PyQgis and PyQt there are excellent options for easy in-house application development based on QGIS. One huge benefit is the unlimited number of installations. Everyone who needs to use QGIS can use it without any limitations. To push the development of QGIS the Canton of Solothurn has invested approximately \$30,000 into QGIS every year since 2007. This is much more efficient and target-oriented than the payment of support into the black box of our former software provider. Apart from using FOSSGIS, the Canton of Solothurn also provides public geodata free of charge via the SO!ONLINE web portal.
## 著者
![Horst Düster](./images/suisse_solothurnaut.jpg){.align-left height="200px"}

この記事はホルストデュスター博士が2009年5月に寄稿しました。氏はスイスのゾロトゥルン州の地理情報部のGISコーディネーターです。
