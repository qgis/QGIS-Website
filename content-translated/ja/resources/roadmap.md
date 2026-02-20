---
HasBanner: false
draft: false
sidebar: true
title: ロードマップ
type: page

---
{{<content-start >}}
# ロードマップ
{{<roadmap >}}

{{<button class="is-primary1 is-rounded" link="https://qgis.org/schedule.ics" text="Subscribe to the roadmap iCalendar" >}}

QGISのリリースと開発は時系列式のスケジュール（ロードマップ）に従って行われます。
- 偶数のバージョン番号 (2.18、 3.2 等々) は、リリースバージョンです。
- 奇数のバージョン番号（2.99, 3.1等々）は開発バージョンです。

新規リリースは４ヶ月ごとに予定されています。最初の３ヶ月で新規開発が行われます。リリース前にあたる４ヶ月目は機能凍結の呼びかけとテスト、バグの修正、翻訳、リリースの準備に当てます。リリース時のブランチ番号は偶数とし、先行するマスターブランチは奇数があてられます。リリース後、次回のパッケージの応募が呼びかけられます。

3回目のリリース（2.8から開始）は、次回の長期リリース（LTR）が公開されるまでサポートされます。
## 開発段階
開発者は、開発段階において次期リリースに向けた新機能の開発に取り組みます。アーリーアダプターは主要なプラットフォームをナイトリービルドで使うことができます。ここでは進捗状況の確認、予備試験、バグレポートの報告、開発の手助けするためのアイディアを提供などが可能です。
## 機能凍結
In the feature freeze phase, new features are not allowed in anymore and the focus of everyone moves from enhancing QGIS to stabilizing it. This also turns the nightly builds effectively into [prereleases](#qgis-prereleases).

**Users** should start extensive testing of these prereleases in their environment to verify that there are no issues, they wouldn’t want to see in the upcoming release. All such issues should be reported (see [Bugs, Features and Issues]({{< ref "resources/support/bug-reporting" >}})). Everything that goes unnoticed, will also end up in the next release. Only in case of serious problems backports to a latest release will occur. Therefore testing of the prereleases and reporting issues is very important.

機能凍結においては **開発者** はバグトラッカーを監視して報告された問題の修正作業を開始し、追加した機能で **ビジュアル変更履歴** を更新します。

翻訳者が作業を開始できるよう、機能凍結後翻訳ファイルが更新されます。ただしこれは暫定的なものであり、バグの修正が翻訳ファイルに追加される可能性があることに注意してください。

リリースの2週間前にハード凍結が開始され、その後は機能凍結の後に導入された深刻な問題と回帰のみが修正されます。

リリースマネージャはこれを機能凍結時に発表します。
## リリース
On major and minor release dates, the release branch is created and the release is tagged and tar balls are prepared. Point releases are just tagged and tar balls are created.

パッケージ作成者はパッケージ作成を開始できることを通知されます。

いくつかのパッケージが利用可能になると、リリースが発表され、それに応じてWebサイトが更新されます。
## リリースのスケジュール
2月下旬にLTRがLTRレポに入るため、月4回のリリースを考えると、毎年ほぼ同じ日程になるようにスケジュールが組まれています。

Beginning after 2.12 the development phase is always 12 weeks and the freeze phase is at least 5 weeks. Remainders are used to extend the freeze phase of LTR releases.

Point releases will happen every month on the latest release branch, if there are backports. Beginning with the 3.28 release, point releases are only done with new latest releases.

In the first four months after its release, a new LTR is also the current LR. In this phase, the new LTR doesn’t replace the previous LTR in the LTR repositories. This happens as soon as a new LR is released.

This schedule is also available as [“iCalendar”](https://qgis.org/schedule.ics).
### スケジュール
{{<csv-table file="csv/schedule.csv" >}}
### イベントの凡例
| Abbreviation | 説明 |
| --- | --- |
| LTR | 長期リリース、新規開発フェーズの開始 |
| LR | 定期リリース、新規開発フェーズの開始 |
| FF | 機能凍結、開発フェーズの終了 |
| PR | 最新版のリリースとLTRブランチのポイントリリース |
| EPR | 追加のポイントリリース |
| <span class="rm-current"> current </span> | <span class="rm-current"> currently supported releases: {{< param "ltrrelease" >}} and {{< param "release" >}} </span> |
| <span class="rm-next"> next </span> | <span class="rm-next"> next releases </span> |

## プレリリースの場所/ナイトリービルド{#qgis-prereleases }
| プラットフォーム | 位置 |
| --- | --- |
| Windows | [OSGeo4W]({{< ref "resources/installation-guide#online-osgeo4w-installer" >}}) |
| Linux | [Debian/Ubuntu]({{< ref "resources/installation-guide#repositories" >}}) |

{{<content-end >}}
