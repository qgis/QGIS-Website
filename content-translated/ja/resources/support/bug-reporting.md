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

For help and questions, please contact the [Mailing lists]({{< ref "community/organisation/mailinglists" >}}).
## QGISのアプリケーション上の問題を報告
QGIS applications (QGIS Desktop and QGIS Server) issues are available in [Github](https://github.com/qgis/QGIS/issues). In order to submit or comment a report, you need to register and login.
### 問題を報告する前に
Before filing an issue, verify that you are running the currently supported versions {{< param "ltrrelease" >}} or {{< param "release" >}} or the development version {{< param "devversion" >}} (see also [Release schedule]({{< ref "resources/roadmap#release-schedule" >}})) and review the currently open issues to make sure that you aren’t creating a duplicate. If you have additional information on an issue, you can add it to the existing ticket. Third party plugins might also cause problems. If you have installed any, you should also verify that the problem is still reproducible without them. Please don’t report multiple unrelated bugs in a single bug report.

When you’re logged in, a `New Issue` button is available. Select it and follow the instructions there.

Before sending the report, please check the formatting of your report by clicking on “Preview”. Please avoid editing existing reports, if not for typos. Better add further comments in any other case.
#### バックトレースを作成する
クラッシュする場合は、そのバグを別のマシン上で再現できないかもしれないので、バックトレースを含めることが有益であるかもしれません。

On Linux QGIS automatically tries to use `gdb` to connect to the crashing process to produce a backtrace. But some distributions disable the possiblity to connect debuggers to a running processes. In that case `gdb` only produces a rather useless message like:

QGIS died on signal 11Could not attach to process. If your uid matches the uid of the target process, check the setting of /proc/sys/kernel/yama/ptrace_scope, or try again as the root user. For more details, see /etc/sysctl.d/10-ptrace.conf ptrace: Operation not permitted. No thread selected No stack. gdb returned 0 Aborted (core dumped)

In that case you should reenable that option by setting `kernel.yama.ptrace_scope` to 0 in `/etc/sysctl.d/10-ptrace.conf` (or `/etc/sysctl.conf` or some other file in `/etc/sysctl.d/`) and run `sysctl -p` as root. When you reproduce the crash after that, a backtrace will be printed instead.

If you cannot reproduce the crash, there should still be a core dump in the current directory, that can be analysed after the process has already terminated. It’s called `core`, though the filename may include a dot followed by the process id on some systems.

On some distributions the creation of core dumps is also disabled. In the event that you just get `Aborted` instead of `Aborted (core dumped)` when the crash occurs. Then you need to run `ulimit -c unlimited` before starting QGIS. You can also include that in your `.profile`, so that it’s always enabled when you login.

To produce a backtrace from the core file, start `gdb /path/to/the/qgis/binary core`. The binary is usually `/usr/bin/qgis` or `/usr/bin/qgis.bin` on Debian with the GRASS plugin installed. In `gdb` you run `bt` which will produce the backtrace.
#### Windows上でのログ出力
The nightly build in [OSGeo4W](https://trac.osgeo.org/osgeo4w) (package qgis-dev) is built with debugging output, that you can view with [DebugView](https://docs.microsoft.com/en-us/sysinternals/downloads/debugview). If the problem is not easy to reproduce, the output might shed some light about where QGIS crashes.
## QGISウェブサイトやマニュアルの問題点を報告
QGIS project provides an active [web site](https://qgis.org) and a rich [documentation](https://qgis.org/en/docs/index.html). Despite our efforts, if you find an out of date information, a wrong or unclear statement or miss valuable information, please feel free to report it.

これらの文書の主なソースはGitHubのリポジトリでホストされ、管理されています。ですからバグを報告したり、パッチを提出するためには、GitHubのアカウントとログインが必要です。

To get started, first [Create a GitHub account](https://github.com/join).

その後、適切なリポジトリを選択します。
- https://github.com/qgis/QGIS-Documentation/issues QGISドキュメントのための
- https://github.com/qgis/QGIS-Website/issues ウェブサイトのための

Check if the issue you’d like to report is not already entered.

**新しい問題** をクリックして、問題についてタイトルおよび明確な説明を入力します。

When you’re finished, click **Submit new issue**.

Note

A `Fix me` link is provided at the bottom of any page of the web site to help you directly improve this page and submit pull request.

このオプションは、ドキュメントのフッターにも使用可能です。
## プラグインの問題を報告する
Most of the plugins in QGIS are published in the official [QGIS Plugins repository](https://plugins.qgis.org/plugins/). Bugs or feature requests relative to them **must** be opened in their respective bug tracking system:
- For any plugin available in QGIS repository, you’ll find in its metadata a link to its bug tracker. Otherwise, consult the plugin documentation to find the address of the relevant bug tracking system or a developer to contact.
  
  If no information is available, please report it to the [Developer mailing-list](https://lists.osgeo.org/mailman/listinfo/qgis-developer).
- For other plugins, we have no means to ensure such information is provided.

## QGISプロジェクトにパッチを提出する
In addition to issue report, you can help to fix issues. Fixing issues is done in GitHub through pull requests. You need to [fork the repository](https://help.github.com/articles/working-with-forks/) you want to contribute to and submit pull requests at:
- QGIS デスクトップまたはQGIS サーバーアプリケーションについて https://github.com/qgis/QGIS
- https://qgis.org でのウェブサイトについて https://github.com/qgis/QGIS-Website 
- https://github.com/qgis/QGIS-Documentation で入手可能なドキュメントの https://docs.qgis.org

You can find a few guidelines that will help you to easily get your patches and pull requests into QGIS projects at [Submitting Pull Requests](https://docs.qgis.org/testing/en/docs/developers_guide/git.html#submitting-pull-requests). And more widely, you may need to read the [Development Process](https://docs.qgis.org/testing/en/docs/developers_guide/git.html) chapter.

{{<content-end >}}
