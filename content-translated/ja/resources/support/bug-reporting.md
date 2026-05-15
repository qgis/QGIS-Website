---
draft: false
sidebar: true
subtitle: ''
title: バグレポート
type: page

---
{{<content-start >}}
# バグ、機能と既知問題
QGISは主にボランティアにより運営されるプロジェクトで、開発者は、文書作成、翻訳者や支持者の専門チームの仕事です。チームではバグのないQGISをリリースしようと努力しておりますが、それでもバグが残っているかもしれません。バグを見つけたり新しい機能を追加したい場合は、ぜひご報告ください！
## どこに報告？
QGISプロジェクトの各部分について、問題（機能要求やバグ）を報告、管理、および議論できる専用の場所があります。問題に遭遇した分野に応じて、以下の表はそれを報告するための正しいリポジトリを示しています：
| バグを見つけた場所、または次の機能を要求した場所 | 問題を報告する場所 |
| --- | --- |
| アプリケーション（QGISデスクトップ、QGISサーバー） | https://github.com/qgis/QGIS/issues |
| QGIS ウェブサイト(https://qgis.org) | https://github.com/qgis/QGIS-Website/issues |
| QGIS文書(https://docs.qgis.org) | https://github.com/qgis/QGIS-Documentation/issues |
| C++ API (https://qgis.org/api) | https://github.com/qgis/QGIS/issues |
| PyQGIS API (https://qgis.org/pyqgis) | https://github.com/qgis/QGIS/issues （内容について）および https://github.com/qgis/pyqgis/issues （形式について） |
| QGIS Plugins Website (https://plugins.qgis.org) | https://github.com/qgis/QGIS-Plugins-Website/issues |
| QGIS Hub Website (https://hub.qgis.org) | https://github.com/qgis/QGIS-Hub-Website/issues |
| QGIS Planet Website (https://planet.qgis.org) | https://github.com/qgis/QGIS-Planet-Website/issues |
| QGIS Changelog Website (https://changelog.qgis.org) | https://github.com/kartoza/prj.app/issues |
| QGIS Feed Website (https://feed.qgis.org) | https://github.com/qgis/qgis-feed/issues |
| 外部プラグイン | プラグインの説明で設定された著者リポジトリ |

ヘルプと質問については [メーリングリスト]({{< ref "community/organisation/mailinglists" >}}) に連絡して下さい。
## QGISのアプリケーション上の問題を報告
 QGISアプリケーション（QGIS DesktopおよびQGIS Server）の問題は  [Github](https://github.com/qgis/QGIS/issues) で管理されています。レポートを送信またはコメントするには、アカウント登録とログインが必要です。
### 問題を報告する前に
問題を報告する前に、現在サポートされているバージョン {{< param "ltrrelease" >}}  または  {{< param "release" >}} 、あるいは開発版 {{< param "devversion" >}} を使用していることを確認してください ([リリーススケジュール](({< ref "resources/roadmap#release-schedule" >})) も参照) 。また、重複した報告を避けるため、現在オープンになっている問題も確認してください。既存の問題に追加情報がある場合は、既存のチケットに追記できます。サードパーティプラグインが問題を引き起こす場合もあります。プラグインをインストールしている場合は、それらを無効にした状態でも問題が再現するか確認してください。無関係な複数のバグを1つのバグレポートにまとめて報告しないでください。

ログイン後、 `New Issue`  ボタンが表示されます。それをクリックし、画面の指示に従ってください。

レポートを送信する前に、 “Preview” をクリックして書式を確認してください。タイプミスの修正を除き、既存のレポートを編集することはお控えください。それ以外の場合は、コメントを追記する方が適切です。
#### バックトレースを作成する
クラッシュする場合は、そのバグを別のマシン上で再現できないかもしれないので、バックトレースを含めることが有益であるかもしれません。

 LinuxではQGISがクラッシュした際、自動的に `gdb` を使用してクラッシュしたプロセスに接続し、バックトレースを生成しようとします。しかし、一部のディストリビューションでは実行中のプロセスへのデバッガー接続が無効化されています。その場合、 `gdb` は次のような役に立たないメッセージのみを出力します:

QGIS died on signal 11Could not attach to process. If your uid matches the uid of the target process, check the setting of /proc/sys/kernel/yama/ptrace_scope, or try again as the root user. For more details, see /etc/sysctl.d/10-ptrace.conf ptrace: Operation not permitted. No thread selected No stack. gdb returned 0 Aborted (core dumped)

その場合は、`/etc/sysctl.d/10-ptrace.conf`（または `/etc/sysctl.conf`  や `/etc/sysctl.conf`  内の他のファイル）で `kernel.yama.ptrace_scope` を 0 に設定してオプションを再度有効にし、rootとして `sysctl -p` を実行してください。その後クラッシュを再現すると、バックトレースが出力されるようになります。

クラッシュを再現できない場合でも、プロセス終了後に解析できるコアダンプがカレントディレクトリに残っているはずです。ファイル名は `core` ですが、システムによってはドットに続いてプロセスIDが付加されたファイル名になる場合があります。

 一部のディストリビューションではコアダンプの生成も無効化されています。クラッシュ時に `Aborted (core dumped)`  ではなく `Aborted`   のみ表示される場合は、QGIS起動前に `ulimit -c unlimited` を実行する必要があります。ログイン時に常に有効になるよう、`.profile` に追記しておくこともできます。

To produce a backtrace from the core file, start `gdb /path/to/the/qgis/binary core`. The binary is usually `/usr/bin/qgis` or `/usr/bin/qgis.bin` on Debian with the GRASS plugin installed. In `gdb` you run `bt` which will produce the backtrace.
#### Windows上でのログ出力
The nightly build in [OSGeo4W](https://trac.osgeo.org/osgeo4w) (package qgis-dev) is built with debugging output, that you can view with [DebugView](https://docs.microsoft.com/en-us/sysinternals/downloads/debugview). If the problem is not easy to reproduce, the output might shed some light about where QGIS crashes.
## QGISウェブサイトやマニュアルの問題点を報告
QGISプロジェクトでは、 [活発なWebサイト](https://qgis.org) と [充実したドキュメント](https://qgis.org/en/docs/index.html) を提供しています。私たちの努力にもかかわらず、古い情報、誤った記述や不明瞭な記述、または不足している情報を見つけた場合は、遠慮なくご報告ください。

これらの文書の主なソースはGitHubのリポジトリでホストされ、管理されています。ですからバグを報告したり、パッチを提出するためには、GitHubのアカウントとログインが必要です。

最初に [GitHubアカウントの作成](https://github.com/join) を行って下さい。

その後、適切なリポジトリを選択します。
- https://github.com/qgis/QGIS-Documentation/issues QGISドキュメントのための
- https://github.com/qgis/QGIS-Website/issues ウェブサイトのための

報告しようとしている問題がすでに登録されていないか確認してください。

**New Issue** をクリックして、問題についてタイトルおよび明確な説明を入力します。

終了するときに **Submit new issue** をクリックして下さい。

Note

Webサイトの各ページ下部に `Fix me` リンクが設置されており、そのページを直接修正してプルリクエストを送信することができます。

このオプションは、ドキュメントのフッターにも使用可能です。
## プラグインの問題を報告する
 QGISのプラグインのほとんどは、公式の [QGISプラグインリポジトリ](https://plugins.qgis.org/plugins/) で公開されています。それらに関するバグ報告や機能リクエストは、**必ず** それぞれのバグトラッキングシステムで行ってください：
- QGISリポジトリで公開されているプラグインには、メタデータにバグトラッカーへのリンクが含まれています。見つからない場合は、プラグインのドキュメントで該当するバグトラッキングシステムのアドレスまたは連絡先となる開発者を確認してください。
  
  情報が見つからない場合は、 [開発者メーリングリスト](https://lists.osgeo.org/mailman/listinfo/qgis-developer) にご報告ください。
- その他のプラグインについては、そのような情報が提供されているかどうかを保証する手段がありません。

## QGISプロジェクトにパッチを提出する
問題の報告に加えて、問題の修正にも貢献することができます。問題の修正はGitHubのプルリクエストを通じて行います。貢献したい  [リポジトリをフォーク](https://help.github.com/articles/working-with-forks/) し、以下の場所にプルリクエストを送信してください:
- QGIS デスクトップまたはQGIS サーバーアプリケーションについて https://github.com/qgis/QGIS
- https://qgis.org でのウェブサイトについて https://github.com/qgis/QGIS-Website 
- https://github.com/qgis/QGIS-Documentation で入手可能なドキュメントの https://docs.qgis.org

パッチやプルリクエストをQGISプロジェクトにスムーズに取り込んでもらうためのガイドラインが [プルリクエストの送信方法](https://docs.qgis.org/testing/en/docs/developers_guide/git.html#submitting-pull-requests) に記載されています。 より詳しくは  [開発プロセス](https://docs.qgis.org/testing/en/docs/developers_guide/git.html)  の章もご参照ください。

{{<content-end >}}
