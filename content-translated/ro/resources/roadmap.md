---
HasBanner: false
draft: false
sidebar: true
title: Planificare
type: page

---
{{<content-start >}}
# Planificare
{{<roadmap >}}

{{<button class="is-primary1 is-rounded" link="https://qgis.org/schedule.ics" text="Subscribe to the roadmap iCalendar" >}}

Dezvoltarea QGIS și lansarea versiunilor se desfășoară după un anumit program (calendar).
- Versiunile standard sunt cele cu numere pare (2.18, 3.2 etc).
- Versiunile de dezvoltare sunt cele cu numere impare (2.99, 3.1 etc).

Lansările au loc la fiecare patru luni. În primele trei luni se desfășoară dezvoltarea. Cu o lună înainte de lansare, este invocată o înghețare de funcționalități, iar ultima lună este folosită pentru testare, eliminarea erorilor, traducere și alte activități pregătitoare. Atunci când are loc lansarea, este creată o ramură cu un număr par, iar ramura master avansează la următoarea versiune impară. După lansare este emisă o cerere de împachetare.

Fiecare a treia versiune (începând cu 2.8) este o versiune cu suport pe termen (LTR), ea fiind întreținută până la apariția următoarei versiuni similare.
## Faza de dezvoltare
În faza de dezvoltare, dezvoltatorii lucrează la adăugarea de noi caracteristici pentru următoarea lansare. Utilizatorii se pot folosi de compilările nocturne existente pentru toate platformele majore, în scopul observării progresului dezvoltării, efectuării de teste preliminare, transmiterii de rapoarte despre probleme și comunicându-și impresiile, ajutând astfel dezvoltarea.
## Înghețarea funcțiunilor
In the feature freeze phase, new features are not allowed in anymore and the focus of everyone moves from enhancing QGIS to stabilizing it. This also turns the nightly builds effectively into [prereleases](#qgis-prereleases).

**Users** should start extensive testing of these prereleases in their environment to verify that there are no issues, they wouldn’t want to see in the upcoming release. All such issues should be reported (see [Bugs, Features and Issues]({{< ref "resources/support/bug-reporting" >}})). Everything that goes unnoticed, will also end up in the next release. Only in case of serious problems backports to a latest release will occur. Therefore testing of the prereleases and reporting issues is very important.

Pe perioada înghețării, **dezvoltatorii** monitorizează erorile, lucrează la rezolvarea problemelor raportate și introduc în **registrul schimbărilor** funcțiile nou adăugate.                               .

O dată cu începerea fazei de înghețare, fișierele de traducere vor fi actualizate în așa fel încât **traducătorii** să-și poată începe munca. Rețineți că acest proces poate fi incremental întrucât, deși funcționalitățile sunt înghețate, remedierea erorilor poate aduce modificări textelor de tradus.

Cu două săptămâni înainte de lansare, este inițiată o înghețare dură, în urma căreia sunt permise numai corecții la problemele grave și la regresiile introduse după înghețare.

Responsabilul lansărilor anunță intrarea în faza de înghețare.
## Lansarea
On major and minor release dates, the release branch is created and the release is tagged and tar balls are prepared. Point releases are just tagged and tar balls are created.

Constructorii noilor versiuni sunt informați că poate începe împachetarea.

O dată ce pachetele sunt disponibile, lansarea poate fi anunțată și site-ul web este actualizat în consecință.
## Planificarea versiunilor
Lansările au loc o dată la patru luni, aproximativ în aceleași date ale fiecărui an, o nouă versiune cu suport pe termen lung intrând în depozitul LTR la sfârșitul lunii februarie.

Beginning after 2.12 the development phase is always 12 weeks and the freeze phase is at least 5 weeks. Remainders are used to extend the freeze phase of LTR releases.

Point releases will happen every month on the latest release branch, if there are backports. Beginning with the 3.28 release, point releases are only done with new latest releases.

In the first four months after its release, a new LTR is also the current LR. In this phase, the new LTR doesn’t replace the previous LTR in the LTR repositories. This happens as soon as a new LR is released.

This schedule is also available as [“iCalendar”](https://qgis.org/schedule.ics).
### Programare
{{<csv-table file="csv/schedule.csv" >}}
### Legenda evenimentelor
| Abbreviation | Descriere |
| --- | --- |
| LTR | Versiune cu suport pe termen lung; începerea unei noi faze de dezvoltate |
| LR | Versiune obișnuită; începerea unei noi faze de dezvoltare |
| FF | Înghețare caracteristici; sfârșitul fazei de dezvoltare |
| PR | Versiune minoră a ultimei versiuni și a ramurii LTR |
| EPR | Versiune Minoră Suplimentară |
| :rm-current:current | :rm-current:currently supported releases: {{< param "ltrrelease" >}} and {{< param "release" >}} |
| :rm-next:next | :rm-next:next releases |

## Locația prelansărilor / compilațiilor nocturne{#qgis-prereleases }
| Platformă | Locație |
| --- | --- |
| Windows | [OSGeo4W]({{< ref "resources/installation-guide#online-osgeo4w-installer" >}}) |
| Linux | [Debian/Ubuntu]({{< ref "resources/installation-guide#repositories" >}}) |

{{<content-end >}}
