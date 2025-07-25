---
HasBanner: false
draft: false
sidebar: true
title: 藍圖
type: page

---
{{<content-start >}}
# 藍圖
{{<roadmap >}}

{{<button class="is-primary1 is-rounded" link="https://qgis.org/schedule.ics" text="Subscribe to the roadmap iCalendar" >}}

Releases and development of QGIS follow a timebased schedule (roadmap).
- 偶數版本號(2.18、3.2等)是發行版。
- 奇數版本號(2.99、3.1等)是開發版。

每四個月會發行新版本，在最初的三個月間新的開發會不斷進行，發布前的最後一個月會凍結調整功能，並進行測試、修復錯誤、翻譯與準備發行。當版本發行後，會建立一個具有偶數版本號的分支，並且將主分支推進至奇數版本號。版本釋出後則需要封裝

自2.8版本起每三版為一個長期發行版，會維持至下一長期發行板釋出。
## 開發階段
在開發階段，開發者致力於新版本中添加新功能。先期使用者可以使用我們為所有主要平台提供的夜間建構版來查詢開發進度，進行初步測試、提供錯誤報告與想法供開發使用。
## 功能凍結
In the feature freeze phase, new features are not allowed in anymore and the focus of everyone moves from enhancing QGIS to stabilizing it. This also turns the nightly builds effectively into [prereleases](#qgis-prereleases).

**Users** should start extensive testing of these prereleases in their environment to verify that there are no issues, they wouldn’t want to see in the upcoming release. All such issues should be reported (see [Bugs, Features and Issues]({{< ref "resources/support/bug-reporting" >}})). Everything that goes unnoticed, will also end up in the next release. Only in case of serious problems backports to a latest release will occur. Therefore testing of the prereleases and reporting issues is very important.

In the feature freeze, **developers** monitor the bugtracker and start working on fixing the reported issues and update the **visual changelog** with the features they added.

With the start of the feature freeze, the translation files will be updated so that **translators** can start their work. Note that this might be an incremental process as although the features are frozen, bug fixes might still introduce translation string changes.

Two weeks before the release, a hard freeze is initiated after which only fixes to severe problems and regressions introduced after the feature freeze are allowed in.

發布管理員於功能凍結時宣布此事
## 釋出
On major and minor release dates, the release branch is created and the release is tagged and tar balls are prepared. Point releases are just tagged and tar balls are created.

The packagers are notified that packaging can begin.

Once some packages are available the release can be announced and the website is updated accordingly.
## 發布日程表
The schedule is aligned to produce roughly the same dates for each year given our four monthly releases with LTRs entering the LTR repo in late february.

Beginning after 2.12 the development phase is always 12 weeks and the freeze phase is at least 5 weeks. Remainders are used to extend the freeze phase of LTR releases.

Point releases will happen every month on the latest release branch, if there are backports. Beginning with the 3.28 release, point releases are only done with new latest releases.

In the first four months after its release, a new LTR is also the current LR. In this phase, the new LTR doesn’t replace the previous LTR in the LTR repositories. This happens as soon as a new LR is released.

This schedule is also available as [“iCalendar”](https://qgis.org/schedule.ics).
### 日程表
{{<csv-table file="csv/schedule.csv" >}}
### 事件說明
| Abbreviation | 說明 |
| --- | --- |
| LTR | 長期發行版，開始進入新的開發階段 |
| LR | 定期發行版，開始進入新的開發階段 |
| FF | 功能凍結，開發階段結束 |
| PR | 最新版與長期發行版的小數點版本 |
| EPR | 特別小數點版 |
| :rm-current:current | :rm-current:currently supported releases: {{< param "ltrrelease" >}} and {{< param "release" >}} |
| :rm-next:next | :rm-next:next releases |

## 預備發行版/每夜建構版安裝檔位置{#qgis-prereleases }
| 平台 | 位置 |
| --- | --- |
| 視窗 | [OSGeo4W]({{< ref "resources/installation-guide#online-osgeo4w-installer" >}}) |
| Linux | [Debian/Ubuntu]({{< ref "resources/installation-guide#repositories" >}}) |

{{<content-end >}}
