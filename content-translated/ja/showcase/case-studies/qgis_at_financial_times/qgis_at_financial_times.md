---
draft: 'true'

---
# フィナンシャルタイムズ・グラフィックチームでQGISの使用
## スティーブン・バーナード（インタラクティブデザインエディタ）インタビュー
Steven is an Interactive Design Editor at Financial Times. You can find him on [Twitter](https://twitter.com/sdbernard). He also publishes useful [HOWTO Videos on Youtube](https://t.co/6aTE6G8h0T) for certain cartographic tasks in QGIS.

**QGIS** ：スティーブン、あなたがFTで働いているチームの名前は何ですか？FTであなたのチームが何をしているかについて背景を少し提供してもらえますか？

**スティーブ**：私たちのチームは現時点では移行期間中でして、新しいデータ・ビジュアライゼーション・エディタのアラン・スミスOBE（以前はONSの）が就任し、グラフィックチームを一本化することになりました。従来は、Webグラフィックチームと印刷グラフィックチームがありました。印刷チームは、すべての新聞のグラフィックスを担当するだけでなく、それらのWebフレンドリーなバージョンも作成していました。私のチームは、Webだけのコンテンツを担当し、インタラクティブ・グラフィックスの設計ではインタラクティブ・プロデューサー／開発者と緊密に協力していました。

新たに形成されたチームでは、異なるメディア間のスキルのクロスオーバーがより可能になるでしょう。

アランは、d3を使ってより大きなグラフィック・ボキャブラリーを作成したり、ビジュアルを作成するのにかかる時間を短縮するなど、私たちのチームに単一のデジタルワークフローを導入しました。

![](./images/ft_europe_migration_balkan-route.png){.align-left width="100.0%"}

*例：移民の流れ。西バルカン半島ルート*

**QGIS** ：あなたのチームには何人くらい同僚がいますか？

**スティーブン**：デザイナー、開発者、プロデューサーと統計学者をすべて含めて24人のチームです

**QGIS**: What\'s your specific role within the team?

**Steven**: We are a multi-disciplinary department so I don't have a specific role as such. My role includes producing responsive designs for interactive graphics as well as doing the front-end development on the less complicated interactives (e.g. [Inside Isis Inc: The journey of a barrel of oil](http://ig.ft.com/sites/2015/isis-oil/)). I also produce the standard news related charts and maps on a daily basis. Over the past two years I have been concentrating on developing our cartographic offerings at the FT. QGIS has been instrumental in changing how we produce maps, and in conjunction with other tools such Blender have helped me to be more creative with how we approach maps.

![](./images/ft_nigeria-migration_animation.gif){.align-left width="100.0%"}

*Example: Animation of Dora\'s journey from Nigeria to Sicily - one of thousands by trafficked women each year.*

**QGIS**: Can you tell us a bit about yourself? What\'s your educational background? What did you do before joining the data visualization team at FT?

![](./images/ft_gotthard-tunnel.png){.align-left width="60.0%"}

*例：スイスアルプスのゴッタルド鉄道と道路トンネル*

**Steven**: I am traditionally trained as scientific illustrator. What's that I hear you ask? It involves producing illustrations for medical journals, natural history publications anything where you are trying to convey information visually where a photograph can't. Think of diagrams showing the human circulatory system, or showing a procedure to fix a broken bone. Sadly there wasn't much call for that kind of work when I left university and I basically fell into the job at the FT. I have always been good at maths, which I think is important when working with data visualisations, it has certainly helped me with my coding as well.

**QGIS** ：どのようにQGISを発見しましたか？

**Steven**: I came across QGIS in 2013 when we were working on a [project mapping the ethnicity of the Middle East](http://ig.ft.com/features/2013-07-19_middleeast_religion_map/dist/index.html)

We used it to georeference maps that were created by a professor at Columbia University. At first I found it really tricky using the add feature drawing tool, probably because it was unlike anything I'd used in Adobe Illustrator for 17 years prior! I also found it frustrating that you had to save things twice, once when done editing the shapefile, then again to save the project. However, this was just down to inexperience with the program and in the end it did exactly what we needed, which was to produce shapefiles that we could add to a Mapbox base map.

**QGIS**: What\'s the role of QGIS within your usual workflows?

**Steven**: QGIS is now an integral part of our mapping workflow. I don't use any other GIS tool to create our maps. Although a few members of our team also use Map Publisher as they feel more comfortable staying within Adobe Illustrator. I would say 80% of our maps are now produced in QGIS.

![](./images/ft_blm-federal-land-map.png){.align-left width="100.0%"}

*例：米国の公用地。*

**QGIS** ：あなたはQGIS以外の他のどのようなツールを使っていて、これらをどのように組み合わせるのですか？

**スティーブン**：簡単な位置図であれば、仕事の95％はQGISで行い、最終的な推敲はAdobe Illustratorで行います。

起伏地図をやっている場合、プロセスはたくさんより複雑です。私にはNASAの地球エクスプローラからDEMファイルを取得し、サイズにトリミングするQGISにそれらをもたらすでしょう。私はその後、レンダリング、3Dを作成するためにブレンダーにトリミングされたDEMがかかります。私はhillshading上の衛星オーバーレイを使用していた場合、私にはNASAからBlueMarble画像をダウンロードし、同様にブレンダーにこれを取ります。エクスポートされたブレンダーからレンダリング背景レイヤーとして使用するQGISに戻されます。必要であれば、私は事前にPhotoshopでそれを微調整することがあります。

For responsive maps like those in the [Isis oil story](http://ig.ft.com/sites/2015/isis-oil/), I used all of the above tools but the final step is to use an open source Adobe Illustrator script developed by the New York Times' Archie Tse. This allows me to create responsive versions of my maps that work on all devices.

もうひとつの便利なツールはGoogleマイマップで、世界中の記者が地図上に位置をマークし、それをkmzファイルとしてダウンロードし、そのままQGISにインポートすることができます。

最後のツールはAdobe After Effectsで、最近、ユーザーを旅に誘うために地図をアニメーション化することにハマっています。最近ランドラッシュシリーズで使ったようにね：
- [Land Rush Ethiopia](https://ig.ft.com/sites/land-rush-investment/ethiopia/)
- [Land Rush Myanmar](https://ig.ft.com/sites/land-rush-investment/myanmar/)
- [Land Rush Indonesia](https://ig.ft.com/sites/land-rush-investment/indonesia/)

**QGIS** ：QGIS以外の空間ツールやGISを使用していますか、そうであれば、どれですか？

**スティーブン**：私はQGIS一筋ですが、前述のように同僚の何人かはMap Publisherも使っています。

![](./images/ft_isis-air-strikes_febupdate.png){.align-left width="100.0%"}

*例：2016年2月のシリア攻撃*

**QGIS** ：あなたがしなければならないタスクについて、QGISの長所と短所を説明することはできますか？

**Steven**: When I first used QGIS I saw it as a specialist tool, fit for only dealing with specific tasks. I really didn't see it a production tool. In late 2014 two of my colleagues went on a QGIS course held by Alasdair Rae at Sheffield University. They both enthused about how good QGIS was, so I took it upon myself to evaluate it as a tool that could be used to produce all our maps.

約2週間以内に私はそれが実行可能になると確信していました。主なセールスポイントは、ストリートレベルのマップのズームレベルのスタイリングなど、すべてのためのスタイルガイドを設定する機能でした。

私は、名前、緯度、経度、マーカーアイコン、フォントウェイト、フォントサイズ、マーカーを表示するかしないかのカラムを持ったGoogleシートのセットを持った、システムセットアップを持っています。

マーカーアイコンは、そのマーカーについてのすべての詳細を記入VLOOKUPテーブルに接続されたドロップダウンです。

だから私がする必要があることすべては、CSVファイルをダウンロードQGISにインポートし、スタイルを適用することだけで、それで95％の準備ができている地図になっています。

To be perfectly honest I can't think of any weaknesses, there are a couple of things that I would like to see or be able to do but, I don't see that as a weakness, just a missing feature.

![](./images/ft_chinaMigration.png){.align-left width="100.0%"}

*例：中国の都市誘致と移住*

**QGIS** ：QGISで最も好きな概念や機能は何ですか？

**スティーブン**：私が人生の時間を節約するものとして分類するであろう多数の機能があります！しかし、主にクイックOSMとGeoreferencerにより私は多くの時間を節約してきて、これは期限が厳しいとき絶対に不可欠です。これは、報道機関のために働いているとき、通常90％の時間です。

![](./images/ft_china_henanGuangdong.png){.align-left width="100.0%"}

*例：中国の都市誘致と移住。詳細ビュー。*

**QGIS** ：QGISでどのような機能や機能性を最も不足を感じますか？実装されていれば、あなたに大いに役立つでしょう不足している機能のリストをお持ちですか？

**Steven**: A couple of things I would like to see in future versions are\...

Bezier curve support, this would be particularly useful in conjunction with Georeferencer. I know there is a spline plugin but it doesn't give you the full control a bezier curve would.

大きなファイルサイズの画像として保存できること。現在、これはBlenderに取りこむDEMファイルの地理参照された切り抜きを作ることができる唯一の方法です。しかしそれは画面のサイズに制限されます。例えばQGISにロードされた8,000ピクセルDEMファイルを持っていた場合は、HDビデオで使用するために画面よりも大きなサイズで切り抜きを書き出せるようにしたいと思います。

**QGIS** ：あなたを助けるQGISで特定の機能がない場合、あなたは自分自身でQGISを改良（QGISコアやPythonプラグインでのコーディングで）することを考えますか？または不足している機能を実装するためにQGIS開発者を雇うことを検討しますか？それとも、代わりにそのギャップを埋めるために他のツールを探すのでしょうか？

**Steven**: I certainly don't have the necessary skills to do the coding myself, I'm fairly proficient in Javascript but would struggle with Python. I would love to hire a developer to get features implemented but unfortunately I'm not in control of any budgets, so I use other tools to get around this.

![](./images/ft_us_broadband_internet_subscription.png){.align-left width="100.0%"}

*例：米国におけるブロードバンドインターネット加入世帯の割合*。

**QGIS**: Let\'s talk about user experience - the QGIS team is aware that there are various places in the UI (dialogs, panels, etc) that could be improved a lot. Can you tell us a little bit where in the UI you see the biggest potential for a UI overhaul?

**Steven**: I think the main tools are fine as they are, once you are familiar with them they're pretty obvious. However, one thing I do find a little frustrating is trying to hunt down a plugin once it's been installed. They either create their own menu (MMQGIS), live under one of the menus (Georeferencer) or create their own icon (threejs). It would be handy to have a plugin window that has all installed plugins in it. Again this isn't a deal breaker but would make it easier than hunting in several different locations.

**QGIS** ：お時間をいただき、またQGISでワークフローを促進し文書化するためにされた仕事について感謝します！

![](./images/ft_potrait_steve_bernard.jpg){.align-left width="50.0%"}

*スティーブ・バーナードの肖像。 ファイナンシャル・タイムスのインタラクティブデザインエディタ*

**Steven**: A pleasure, I'm almost evangelical about QGIS! Hence the [31 video tutorials](https://t.co/6aTE6G8h0T) and always happy to spread the word.

A.ノイマンとT.サットンによるインタビューの質問。2016年4月。
