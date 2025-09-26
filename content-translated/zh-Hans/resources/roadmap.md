---
HasBanner: false
draft: false
sidebar: true
title: 路线图
type: page

---
{{<content-start >}}
# 路线图
{{<roadmap >}}

{{<button class="is-primary1 is-rounded" link="https://qgis.org/schedule.ics" text="Subscribe to the roadmap iCalendar" >}}

Releases and development of QGIS follow a timebased schedule (roadmap).
- 偶数版本号 (2.18, 3.2 等) 是发行版。
- 奇数版本号 (2.99, 3.1 等) 是开发版。

每四个月将发布一个新版本。前三个月，进行新功能的开发。发布前的最后一个月，各项功能将冻结，用于测试、错误修复、翻译和发行准备。当正式发布时，会创建一个具有偶数版本号的分支，并且主分支会进行到下一个奇数版本继续开发。发布后，会发出打包要求。

每三个版本 (从 2.8 开始) 是一个长期发行版 (LTR)，将一直维护到下一个长期发行版产生。
## 开发阶段
在开发阶段，开发人员致力于为下一个版本添加新功能。尝鲜者可以使用我们为所有主要平台提供的夜间构建版来查看开发的进度，进行初步测试并提供错误报告，与开发人员交流想法来帮助开发工作。
## 功能冻结
In the feature freeze phase, new features are not allowed in anymore and the focus of everyone moves from enhancing QGIS to stabilizing it. This also turns the nightly builds effectively into [prereleases](#qgis-prereleases).

**Users** should start extensive testing of these prereleases in their environment to verify that there are no issues, they wouldn’t want to see in the upcoming release. All such issues should be reported (see [Bugs, Features and Issues]({{< ref "resources/support/bug-reporting" >}})). Everything that goes unnoticed, will also end up in the next release. Only in case of serious problems backports to a latest release will occur. Therefore testing of the prereleases and reporting issues is very important.

在功能冻结期间， **开发人员** 监控错误追踪系统和修复报告的问题，并使用他们添加的功能更新 **可视化更新日志** 。

随着功能冻结的启动，翻译文件将被更新，便于 **译者** 开始翻译工作。请注意，这可能是增量过程，尽管功能被冻结，但Bug修复或许会引入新的翻译字符串。

发布前两周，将启动硬冻结，这时只允许修复在功能冻结之后复原引入的严重问题。

发布管理人员在功能冻结时将宣布此事。
## 发行版
On major and minor release dates, the release branch is created and the release is tagged and tar balls are prepared. Point releases are just tagged and tar balls are created.

通知包装程序可以开始打包。

一旦某些软件包可用，就可以发布并相应更新网站。
## 版本发布计划表
鉴于我们四个月一发行，LTR版将于2月下旬进入LTR资源库，因此，该计划表每年的日期大致相同。

Beginning after 2.12 the development phase is always 12 weeks and the freeze phase is at least 5 weeks. Remainders are used to extend the freeze phase of LTR releases.

Point releases will happen every month on the latest release branch, if there are backports. Beginning with the 3.28 release, point releases are only done with new latest releases.

In the first four months after its release, a new LTR is also the current LR. In this phase, the new LTR doesn’t replace the previous LTR in the LTR repositories. This happens as soon as a new LR is released.

This schedule is also available as [“iCalendar”](https://qgis.org/schedule.ics).
### 计划表
{{<csv-table file="csv/schedule.csv" >}}
### 版本说明
| Abbreviation | 描述 |
| --- | --- |
| LTR | 长期发行版，开始进入新版本的开发阶段 |
| LR | 定期发行版，开始进入新版本的开发阶段 |
| FF | 功能冻结，开发阶段结束 |
| PR | 最新版和LTR分支的单点版 |
| EPR | 特别单点版 - Extra Point release |
| :rm-current:current | :rm-current:currently supported releases: {{< param "ltrrelease" >}} and {{< param "release" >}} |
| :rm-next:next | :rm-next:next releases |

## 预发布的位置 / 每日构建版{#qgis-prereleases }
| 平台 | 位置 |
| --- | --- |
| Windows | [OSGeo4W]({{< ref "resources/installation-guide#online-osgeo4w-installer" >}}) |
| Linux | [Debian/Ubuntu]({{< ref "resources/installation-guide#repositories" >}}) |

{{<content-end >}}
