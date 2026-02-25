---
HasBanner: false
draft: false
sidebar: true
title: Planung
type: page

---
{{<content-start >}}
# Planung
{{<roadmap >}}

{{<button class="is-primary1 is-rounded" link="https://qgis.org/schedule.ics" text="Subscribe to the roadmap iCalendar" >}}

Releases and development of QGIS follow a timebased schedule (roadmap).
- Gerade Versionsnummern (2.18, 3.2, usw) sind veröffentliche Ausgaben.
- Ungerade Versionnummern (3.1, 3.3 usw.) sind Entwicklungsversionen.

Alle vier Monate wird eine neue Version veröffentlicht. In den ersten drei Monaten findet neue Entwicklung statt. Danach wird eine Feature Freeze ausgelöst, in dem keine neuen Funktionen mehr hinzugefügt werden. Der letzte Monat für Tests, Fehlerbehebung, Übersetzung und Freigabevorbereitung verwendet. Wenn die Freigabe stattfindet wird eine Zweig mit einer geraden Zahl erstellt und der Master-Zweig erhält die nächste ungerade Zahl. Nach der Freigabe wird zur Erstellung von Paketen aufgerufen.

Jedes dritte Versionfreigabe (beginnend mit 2.8) ist ein langfristige Versionslinie (engl. Long Term Release; LTR) das bis zur nächsten langfristigen Versionslinie gepflegt wird.
## Entwicklungsphase
In der Entwicklungsphase arbeiten die Entwickler an neuen Funktionen für die nächste Version. Frühzeitige Anwender können sich mit den nächtlichen Kompilaten, die wir für die Hauptplattformen haben, einen Eindruck des Entwicklungsfortschritt machen, Vorabtests durchführen und Fehlermeldungen und Ihre Gedanken liefern um die Entwicklung zu unterstützen.
## Feature Freeze
In the feature freeze phase, new features are not allowed in anymore and the focus of everyone moves from enhancing QGIS to stabilizing it. This also turns the nightly builds effectively into [prereleases](#qgis-prereleases).

**Users** should start extensive testing of these prereleases in their environment to verify that there are no issues, they wouldn’t want to see in the upcoming release. All such issues should be reported (see [Bugs, Features and Issues]({{< ref "resources/support/bug-reporting" >}})). Everything that goes unnoticed, will also end up in the next release. Only in case of serious problems backports to a latest release will occur. Therefore testing of the prereleases and reporting issues is very important.

Im Feature Freeze beobachten **Entwickler** den Bugtracker und beginnen mit der Beseitigung der berichteten Fehler und aktualisieren das **Visuelle Änderungsprotokoll** um die hinzugefügten Funktionen.

Mit dem Beginn des Feature Freezes werden auch die Übersetzungsdateien aktualisiert, damit die **Übersetzer** mit ihrer Arbeit beginnen können. Beachten Sie, dass dies eine inkrementeller Prozess sein kann, obwohl die Funktionen feststehen. könnten Fehlerkorrekturen immer noch Änderungen an den Übersetzungstexten mit sich bringen.

Zwei Wochen vor dem Release setzt ein harter Freeze ein, nachdem nur noch Reparaturen an ernsthaften Problemen und Regressionen, die nach dem Feature Freeze herauskamen, erlaubt sind.

Der Release Manager verkündet dies beim Feature Freeze.
## Version
On major and minor release dates, the release branch is created and the release is tagged and tar balls are prepared. Point releases are just tagged and tar balls are created.

Die Paketersteller werden informiert, dass das Paketieren beginnen kann.

Sobald einige Pakete verfügbar sind kann das Release verkündet werden und die Webseite wird entsprechend aktualisiert.
## Freigabe-Zeitplan
The schedule is aligned to produce roughly the same dates for each year given our four monthly releases with LTRs entering the LTR repo in late february.

Beginning after 2.12 the development phase is always 12 weeks and the freeze phase is at least 5 weeks. Remainders are used to extend the freeze phase of LTR releases.

Point releases will happen every month on the latest release branch, if there are backports. Beginning with the 3.28 release, point releases are only done with new latest releases.

In the first four months after its release, a new LTR is also the current LR. In this phase, the new LTR doesn’t replace the previous LTR in the LTR repositories. This happens as soon as a new LR is released.

This schedule is also available as [“iCalendar”](https://qgis.org/schedule.ics).
### Schedule
{{<csv-table file="csv/schedule.csv" >}}
### Event legend
| Abbreviation | Beschreibung |
| --- | --- |
| LTR | Langfristige Version, Beginn der neuen Entwicklungsphase |
| LR | Reguläre Version, Beginn der neuen Entwicklungsphase |
| FF | Feature-Freeze, Ende der Entwicklungsphase |
| PR | Point-Release des aktuellen und des LTR-Zweigs |
| EPR | Zusätzliches Point-Release |
| <span class="rm-current"> current </span> | <span class="rm-current"> currently supported releases: {{< param "ltrrelease" >}} and {{< param "release" >}} </span> |
| <span class="rm-next"> next </span> | <span class="rm-next"> next releases </span> |

## Ort von Vorabversionen / nächtlichen Kompilaten{#qgis-prereleases }
| Plattform | Ort |
| --- | --- |
| Windows | [OSGeo4W]({{< ref "resources/installation-guide#online-osgeo4w-installer" >}}) |
| Linux | [Debian/Ubuntu]({{< ref "resources/installation-guide#repositories" >}}) |

{{<content-end >}}
