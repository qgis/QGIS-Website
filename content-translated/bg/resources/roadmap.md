---
HasBanner: false
draft: false
sidebar: true
title: Пътна карта
type: page

---
{{<content-start >}}
# Пътна карта
{{<roadmap >}}

{{<button class="is-primary1 is-rounded" link="https://qgis.org/schedule.ics" text="Абонирайте се за пътната карта iCalendar" >}}

Изданията и разработването на QGIS следват график, базиран на време (пътна карта).
- Дори номерата на версиите (2.18, 3.2 и т.н.) са версии за пускане на пазара.
- Нечетните номера на версиите (2.99, 3.1 и т.н.) са версии за разработка.

A new release will happen every four months. In the first three months, new development is taking place. In the last month before a release, a feature freeze is invoked and the final month is used for testing, bugfixing, translation and release preparations. When the release happens, a branch with an even release number is created and the master branch advances to the next odd version. After the release a call for packaging is issued.

Every third release (starting with 2.8) is a long-term-release (LTR) that is maintained until the next long-term-release occurs.
## Фаза на развитие
In the development phase, developers work on adding new features for the next release. Early adopters can use the nightly builds we have for all major platforms to see the development progress, do preliminary testing and provide bug reports and their thoughts to help with development.
## Замразяване на функциите
In the feature freeze phase, new features are not allowed in anymore and the focus of everyone moves from enhancing QGIS to stabilizing it. This also turns the nightly builds effectively into [prereleases](#qgis-prereleases).

**Users** should start extensive testing of these prereleases in their environment to verify that there are no issues, they wouldn’t want to see in the upcoming release. All such issues should be reported (see [Bugs, Features and Issues]({{< ref "resources/support/bug-reporting" >}})). Everything that goes unnoticed, will also end up in the next release. Only in case of serious problems backports to a latest release will occur. Therefore testing of the prereleases and reporting issues is very important.

In the feature freeze, **developers** monitor the bugtracker and start working on fixing the reported issues and update the **visual changelog** with the features they added.

With the start of the feature freeze, the translation files will be updated so that **translators** can start their work. Note that this might be an incremental process as although the features are frozen, bug fixes might still introduce translation string changes.

Two weeks before the release, a hard freeze is initiated after which only fixes to severe problems and regressions introduced after the feature freeze are allowed in.

Мениджърът на изданията обявява това при замразяване на функции.
## Обновяване
On major and minor release dates, the release branch is created and the release is tagged and tar balls are prepared. Point releases are just tagged and tar balls are created.

Опаковачите са уведомени, че опаковането може да започне.

Once some packages are available the release can be announced and the website is updated accordingly.
## График за издаване
The schedule is aligned to produce roughly the same dates for each year given our four monthly releases with LTRs entering the LTR repo in late february.

Beginning after 2.12 the development phase is always 12 weeks and the freeze phase is at least 5 weeks. Remainders are used to extend the freeze phase of LTR releases.

Point releases will happen every month on the latest release branch, if there are backports. Beginning with the 3.28 release, point releases are only done with new latest releases.

In the first four months after its release, a new LTR is also the current LR. In this phase, the new LTR doesn’t replace the previous LTR in the LTR repositories. This happens as soon as a new LR is released.

Този график е наличен и като [“iCalendar”](https://qgis.org/schedule.ics).
### График
{{< csv-table file="csv/schedule.csv" />}}
### Легенда на събитието
| Абривиатура | Описание |
| --- | --- |
| LTR | Дългосрочно издание, начало на нова фаза на разработка |
| LR | Редовно издание, начало на нова фаза на разработка |
| FF | Замразяване на функции, край на фазата на разработка |
| PR | Точково издание на най-новата версия и LTR клон |
| EPR | Освобождаване на Extra Point |
| <span class="rm-current"> текущ </span> | <span class="rm-current"> currently supported releases: {{< param "ltrrelease" >}} and {{< param "release" >}} </span> |
| <span class="rm-next"> следващ </span> | <span class="rm-next"> следващи издания </span> |

## Местоположение на предварителните издания / нощните компилации{#qgis-prereleases }
| Платформа | Път |
| --- | --- |
| Windows | [OSGeo4W]({{< ref "resources/installation-guide#online-osgeo4w-installer" >}}) |
| Linux | [Debian/Ubuntu]({{< ref "resources/installation-guide#repositories" >}}) |

{{<content-end >}}
