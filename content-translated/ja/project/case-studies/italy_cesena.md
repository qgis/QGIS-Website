---
HasBanner: false
archived: true
date: 2015-10-30
draft: false
featured: false
section: project
sidebar: true
thumbnail: images/italy_cesena1.png
title: チェゼーナの壁を描くQGIS
type: case-study

---
{{<content-start >}}
# QGIS to describe the Cesena\'s Wall
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>October 30, 2015</span>
</p>

「eキャンパス大学」はオンライン大学として作成され、2006年1月30日の省令により、MIUR（イタリア文部科学省）によって認可されました。それは労働市場に貢献するため、若い人、専門家、起業家、経営幹部およびビジネスおよび文化関係者.に対してeラーニングプラットフォームを通じた大学へのアクセスを提供する目的で形成されました。本部は、ミラノ国際キャンパスとしても、またはノヴェドラーテキャンパスとして知られていますが、ノヴェドラーテ（コモ、イタリア）の元IBMのトレーニングセンターの中、静かな緑のブリアンツァ中のあるキャンパスに位置しています。

大学は5つの仮想学部を持っています：エンジニアリング、経済学、心理学、芸術、法律。古地図とQGISプロジェクト　城壁はチェゼーナの街を特徴づけます。そのサソリ形状が新しくゾーンからの歴史的な中心部を分割します。

歴史的地図製作の文書は、その進化とその破壊を記述する。QGISプログラムは、それが地理参照プラグインで、同じ基準システム内のすべての地図を転送することを可能にするので、私は、別の古地図を比較できます。参考としてオープンレイヤのグーグルサテライトとオープンレイヤのオープンストリートマップは、すべての歴史的な参照系EPSG:3857（ウェブメルカトルまたは疑似メルカトル）に地図を参照するために使用されています。

QGISは、基本的なツールは、分析し、手の込んだ、私は、道路、建物、公園や庭園、城壁、古代の要塞塔、古代都市の門などの地図のoftheすべての要素を、記憶しているベクターレイヤーまたはシェープファイルを介して、これらの地理参照地図を比較することでした。私はpuntual、線形および多角形のレイヤーを使用しました。私は分析、研究、ジオプロセシング、ジオメトリデータ管理ツールを使用してこれらのレイヤーを比較しました（図1）。

<figure>
<img src="../images/italy_cesena1.png" style="width:100.0%" alt="italy_cesena1.png" />
<figcaption>Fig. 1 Concept Map of the QGIS project</figcaption>
</figure>

このツールを使用して、私は以下の情報を得ました：
- The precision of the Leonardo Da Vinci\'s topographic survey, realized in 1502, such as how many points of this survey are correct (Fig. 2);
- The Cesena Wall\'s Development from the Roman Age to the 15th Century;
- The Cesena Wall\'s Demolitions from the 19th Century to the Early 20th Century;
- 城壁の形態変化、例えば古代の要塞塔とその古代の城門の解体。
- The Cesena\'s Urban Progress from the 16th Century to the Present;

<figure>
<img src="../images/italy_cesena2.png" style="width:100.0%" alt="italy_cesena2.png" />
<figcaption>Fig. 2: Openlayer Google Satellite overlapped by the informations recorded in different layers: the present City Wall in black, the Leonardo Da Vinci's topographic survey of the City Wall in orange, the Leonardo Da Vinci's points of survey in yellow and the present ancient City Gates in red.</figcaption>
</figure>

たくさんのQGISツールがあり、私はこれらを使って次のように作成しました。
- 現在の城壁の線状レイヤの各セクションを写真につなぐリンク。実際の保存状態を表します。
- 19世紀のチェゼーナの写本を印刷作家に渡したもの。
- qgis2threejsプラグインを使用したチェゼーナの3Dモデル（図3）

<figure>
<img src="../images/italy_cesena3.png" style="width:100.0%" alt="italy_cesena3.png" />
<figcaption>Fig. 3: The 3D model of the present City Wall and Cesena's buildings inside and outside the Wall. The ancient fortified towers and the ancient City Gates are indicated.</figcaption>
</figure>

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
Camilla Fabbri has a bachelor\'s degree in Civil and Environmental Engineering. She has developed her dissertation on historical cartography of the Cesena Wall using the QGIS program with the Supervisor Alessandra Borghi, who is the University Teacher of Topography and Theoretical Mechanics of the bachelor\'s degree in Civil and Environmental Engineering in the eCampus University.

{{<content-end >}}
