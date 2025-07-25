---
HasBanner: false
draft: false
sidebar: true
title: Framdriftsplan
type: page

---
{{<content-start >}}
# Framdriftsplan
{{<roadmap >}}

{{<button class="is-primary1 is-rounded" link="https://qgis.org/schedule.ics" text="Subscribe to the roadmap iCalendar" >}}

Releases and development of QGIS follow a timebased schedule (roadmap).
- Partallsversjoner (2.18, 3.2 osv.) utgis til vanlig bruk.
- Oddetallsversjoner (2.99, 3.1 osv.) er utviklingsversjoner.

Nye utgivelser skjer hver fjerde måned. Nyutvikling skjer de første tre månedene. Den siste måneden brukes til testing, feilretting, oversettinger og annen forbereding av utgivelsen. Deretter opprettes en forgreining med partallsnummerering, og hovedgreina fortsetter til neste oddetall. Det gjøres klart for pakking etter at utgivelsen er et faktum.

Hver tredje utgivelse (etter 2.8) er en langtidsstøttet utgivelse (LTR) som vedlikeholdes fram til neste tilsvarende utgivelse.
## Utviklingsfase
Under denne fasen jobber utviklerne med ny funksjonalitet for neste utgivelse. Betatestere kan laste ned og bruke nattbyggene for å se framdriften, teste og sende inn feilrapporter og hjelpsomme merknader. Nattbygg gjøres tilgjengelig for de største plattformene.
## Frysing av ny funksjonalitet
In the feature freeze phase, new features are not allowed in anymore and the focus of everyone moves from enhancing QGIS to stabilizing it. This also turns the nightly builds effectively into [prereleases](#qgis-prereleases).

**Users** should start extensive testing of these prereleases in their environment to verify that there are no issues, they wouldn’t want to see in the upcoming release. All such issues should be reported (see [Bugs, Features and Issues]({{< ref "resources/support/bug-reporting" >}})). Everything that goes unnoticed, will also end up in the next release. Only in case of serious problems backports to a latest release will occur. Therefore testing of the prereleases and reporting issues is very important.

I frysefasen vil **utviklerne** overvåke feilsporingssystemet og starte å jobbe med rapporterte problemer, og oppdatere den **visuelle endringsloggen** med funksjonalitet de har lagt til.

Etter frysing av ny funksjonalitet vil oversettingsfilene oppdateres slik at **oversetterne** kan sette i gang med arbeidet sitt. Denne prosessen er gradvis – selv om det ikke kommer ny funksjonalitet så kan feilrettinger medføre endringer av tekststrenger som skal oversettes.

To uker før utgivelse starter hardfrysing. Det vil si at man kun kan rette alvorlige feil og regresjoner fra perioden etter frys av ny funksjonalitet.

Utgivelsesansvarlig annonserer dette ved funksjonsfrys.
## Utgivelse
On major and minor release dates, the release branch is created and the release is tagged and tar balls are prepared. Point releases are just tagged and tar balls are created.

Pakkerne varsles om at pakking kan igangsettes.

Utgivelsen kan annonseres når pakker begynner å bli tilgjengelige, og nettsiden oppdateres.
## Release schedule
The schedule is aligned to produce roughly the same dates for each year given our four monthly releases with LTRs entering the LTR repo in late february.

Beginning after 2.12 the development phase is always 12 weeks and the freeze phase is at least 5 weeks. Remainders are used to extend the freeze phase of LTR releases.

Point releases will happen every month on the latest release branch, if there are backports. Beginning with the 3.28 release, point releases are only done with new latest releases.

In the first four months after its release, a new LTR is also the current LR. In this phase, the new LTR doesn’t replace the previous LTR in the LTR repositories. This happens as soon as a new LR is released.

This schedule is also available as [“iCalendar”](https://qgis.org/schedule.ics).
### Schedule
{{<csv-table file="csv/schedule.csv" >}}
### Event legend
| Abbreviation | Beskrivelse |
| --- | --- |
| LTR | Long term release, begin of new development phase |
| LR | Regular release, begin of new development phase |
| FF | Feature freeze, end of development phase |
| PR | Point release of latest release and LTR branch |
| EPR | Extra Point release |
| :rm-current:current | :rm-current:currently supported releases: {{< param "ltrrelease" >}} and {{< param "release" >}} |
| :rm-next:next | :rm-next:next releases |

## Location of prereleases / nightly builds{#qgis-prereleases }
| Platform | Plassering |
| --- | --- |
| Windows | [OSGeo4W]({{< ref "resources/installation-guide#online-osgeo4w-installer" >}}) |
| Linux | [Debian/Ubuntu]({{< ref "resources/installation-guide#repositories" >}}) |

{{<content-end >}}
