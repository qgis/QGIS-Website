---
draft: 'true'

---
# チェゼーナの壁を描くQGIS
「eキャンパス大学」はオンライン大学として創設され、MIUR（イタリア文部科学省）の2006年1月30日の省令により認可されました。それは労働市場に貢献するため、若者、専門家、起業家、経営幹部並びにビジネス及び文化関係者に対してeラーニングプラットフォームを通じた大学へのアクセスを提供する目的で作られました。ミラノ国際キャンパスとしても知られる本部、ノヴェドラーテキャンパスは、元ノヴェドラーテ（コモ、イタリア）IBM訓練センターの中の、静かな緑のブリアンツァにあるキャンパスに位置しています。

大学には、エンジニアリング、経済学、心理学、芸術、法律の5つの仮想学部があります。古地図とQGISプロジェクト　城壁はチェゼーナの街を特徴づけています。そのサソリ型の形状が新しいゾーンから歴史的な中心部を分けています。

歴史的地図製作の文書は、その進化とその破壊を記述しています。QGISプログラムは、ジオリファレンスプラグインを使って全ての地図を同じ参照系に映しかえることができるので、別々の古地図を比較することができます。参考ですが、全ての古地図を参照系 EPSG:3857（ウェブメルカトルまたは疑似メルカトル）に参照させるため、オープンレイヤのグーグルサテライトとオープンレイヤのオープンストリートマップが使用しました。

QGISは、これらのジオリファレンスした地図を推敲し、分析し、比較するためになくてはならないツールであり、道路、建物、公園や庭園、城壁、古代の要塞塔、古代の城門などの地図のすべての要素をベクターレイヤーまたはシェープファイルを使って記録しました。ポイント、ライン、ポリゴンレイヤーが使われ、分析、調査、ジオプロセシング、ジオメトリ、データ管理ツールを使用してこれらのレイヤーを比較しました（図1）。

![Fig. 1 Concept Map of the QGIS project](./images/italy_cesena1.png){width="100.0%"}

このツールを使用して、私は以下の情報を得ました：
- 1502年に実施したレオナルド・ダ・ヴィンチの地形調査の精度（いくつの調査地点が正しいかなど）（図2）
- ローマ時代から15世紀までのチェゼーナの壁の造成
- 19世紀から20世紀初頭までのチェゼーナの壁の破壊
- 城壁の形態変化、例えば古代の要塞塔とその古代の城門の解体。
- 16世紀から現在までのチェゼーナの都市化

![Fig. 2: Openlayer Google Satellite overlapped by the informations recorded in different layers: the present City Wall in black, the Leonardo Da Vinci\'s topographic survey of the City Wall in orange, the Leonardo Da Vinci\'s points of survey in yellow and the present ancient City Gates in red.](./images/italy_cesena2.png){width="100.0%"}

たくさんのQGISツールのうちのいくつかを使って次のものを作成しました:
- 現在の城壁のラインレイヤの各セクションを実際の保存状態を表す写真につなぐリンク；
- プリントコンポーザを使った19世紀のチェゼーナの地図
- qgis2threejsプラグインを使用したチェゼーナの3Dモデル（図3）

![Fig. 3: The 3D model of the present City Wall and Cesena\'s buildings inside and outside the Wall. The ancient fortified towers and the ancient City Gates are indicated.](./images/italy_cesena3.png){width="100.0%"}
## 結論
古地図は、その精度が実際の地図製作の文書の精度と比較できないとしても、重要な書類であり、地理的な表現の専門家ではない人にとっても非常に伝達力のある表現です。QGISは、古地図の数値的な内容を、効果的で意味のある表現に従って利用できる唯一の手段でした。
## 書誌索引
歴史的な地図は以下によって抽出されています：
- \"Costruzione, alterazione e recupero del centro storico di Cesena\", Ballardini, Cantori, Pezzi, Righetti, Tossani, Bruno Ghigi Editore, 1977
- \"La cinta muraria di Cesena\", Pino Montalti, Edizioni Panini, 1986

歴史的な情報は以下から抽出されています：
- \"La cartografia in Italia: nuovi metodi e nuovi strumenti dal Settecento ad Oggi\", Andrea Cantile, IGM Firenze, 2007
- \"Lineamenti di storia della cartografia italiana, volume secondo, dal Seicento al Novecento\" Andrea Cantile, Geoweb, 2013
- \"I rilievi cartografici di Leonardo per Cesena ed Urbino contenuti nel manoscritto \'L\' dell\'Istituto di Francia\", Nando De Toni, G. Barbéra Editore, 1965
- \"La città da guerra\", Amelio Fara, Einaudi, 1993
- \"La cartografia dall\'antichità fino al XVIII secolo\", Carlo Monti, Maggioli Editore, 2011

## 著者
カミラ・ファブリは土木環境工学の学士号の保持者です。彼女は監修者のアレッサンドラ・ボルギ（eCampus 大学土木環境工学学部の地形と理論力学の大学教師）と共に QGIS プログラムを使用してチェゼーナの壁の歴史地図作成についての彼女の論文を作成しました。
