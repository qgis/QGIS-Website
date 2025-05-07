---
HasBanner: false
draft: false
sidebar: true
title: Stappenplan
type: page

---
{{<content-start >}}
# Stappenplan
{{<roadmap >}}

{{<button class="is-primary1 is-rounded" link="https://qgis.org/schedule.ics" text="Subscribe to the roadmap iCalendar" >}}

Uitgaven en ontwikkeling van QGIS volgen een op tijd gebaseerd schema (roadmap).
- Even versienummers (2.18, 3.2 etc) zijn  uitgaveversies.
- Oneven versienummers (2.99, 3.1 etc) zijn ontwikkelingsversies.

Elke vier maanden zal er een nieuwe uitgave zijn.  In de eerste drie maanden vindt nieuwe ontwikkeling plaats.  Dan, de laatste maand voor een uitgave, wordt een bevriezing van de mogelijkheden ingevoerd en de laatste maand wordt gebruikt voor het testen, oplossen van problemen, vertalen en voorbereidingen voor de uitgave.  Bij de uitgave wordt een tak met een even uitgavenummer gemaakt en de hoofdtak promoveert naar de volgende oneven versie.  Na de uitgave wordt een oproep uitgegeven voor het maken van de pakketten.

Elke derde uitgave (beginnend met 2.8) is een lange-termijn-uitgave (LTR) die wordt onderhouden totdat de volgende lange-termijn-uitgave verschijnt.
## Ontwikkelingsfase
In de ontwikkelingsfase werken ontwikkelaars aan het toevoegen van nieuwe mogelijkheden voor de volgende uitgave. Vroege deelnemers kunnen de nachtelijke builds, die we voor alle belangrijke platformen hebben, gebruiken om de voortgang van de ontwikkeling te bekijken, vroege testen te doen en rapporten voor problemen indienen en hun gedachten delen om met de ontwikkeling te helpen.
## Bevriezing
In the feature freeze phase, new features are not allowed in anymore and the focus of everyone moves from enhancing QGIS to stabilizing it. This also turns the nightly builds effectively into [prereleases](#qgis-prereleases).

**Users** should start extensive testing of these prereleases in their environment to verify that there are no issues, they wouldn’t want to see in the upcoming release. All such issues should be reported (see [Bugs, Features and Issues]({{< ref "resources/support/bug-reporting" >}})). Everything that goes unnoticed, will also end up in the next release. Only in case of serious problems backports to a latest release will occur. Therefore testing of the prereleases and reporting issues is very important.

In de fase Bevriezing monitoren  **ontwikkelaars** het systeem voor problemen en beginnen met het herstellen van de gerapporteerde problemen en werken het **visuele log met wijzigingen** bij met de mogelijkheden die door hen werden toegevoegd.

Aan het begin van de bevriezing zullen de te vertalen bestanden worden bijgewerkt, zodat **vertalers** hun werk kunnen beginnen. Onthoud dat dit een voortdurend proces kan zijn, omdat, hoewel de mogelijkheden zijn bevroren, oplossingen van problemen nog steeds wijzigingen zouden kunnen opleveren in te vertalen tekenreeksen.

Twee weken voor de uitgave wordt een harde bevriezing uitgevoerd, waarna alleen reparaties aan ernstige problemen en regressies, geïntroduceerd na de bevriezing, zijn toegestaan om in te voegen.

De uitgavemanager kondigt dit aan bij het bevriezen van mogelijkheden.
## Uitgave
On major and minor release dates, the release branch is created and the release is tagged and tar balls are prepared. Point releases are just tagged and tar balls are created.

De inpakkers wordt bericht dat zij kunnen beginnen met inpakken.

Als enkele paketten beschikbaar zijn kan de uitgave worden aangekondigd en wordt de website overeenkomstig bijgewerkt.
## Uitgaveschema
Het schema is dusdanig ontworpen dat ruwweg op dezelfde datums in elk jaar onze viermaandelijkse uitgaven met LTR's worden geproduceerd waarbij eind februari de opslagplaats voor LTR wordt ingevoerd.

Beginning after 2.12 the development phase is always 12 weeks and the freeze phase is at least 5 weeks. Remainders are used to extend the freeze phase of LTR releases.

Point releases will happen every month on the latest release branch, if there are backports. Beginning with the 3.28 release, point releases are only done with new latest releases.

In the first four months after its release, a new LTR is also the current LR. In this phase, the new LTR doesn’t replace the previous LTR in the LTR repositories. This happens as soon as a new LR is released.

This schedule is also available as [“iCalendar”](https://qgis.org/schedule.ics).
### Schema
{{< csv-table file="csv/schedule.csv" />}}
### Legenda gebeurtenissen
{{< csv-table >}} "LTR","Long term release, begin of new development phase" "LR","Regular release, begin of new development phase" "FF","Feature freeze, end of development phase" "PR","Point release of latest release and LTR branch" "EPR","Extra Point release" ":rm-current:current",":rm-current:currently supported releases: {{< param "ltrrelease" >}} and {{< param "release" >}}" ":rm-next:next",":rm-next:next releases" {{< /csv-table >}}
## Locatie van pre-uitgaven / nachtelijke builds{#qgis-prereleases }
| Platform | Locatie |
| --- | --- |
| Windows | [OSGeo4W]({{< ref "resources/installation-guide#online-osgeo4w-installer" >}}) |
| Linux | [Debian/Ubuntu]({{< ref "resources/installation-guide#repositories" >}}) |

<!-- |MacOS|[Mac OS]({{< ref "resources/installation-guide#qgis-nightly-release" >}})| -->

{{<content-end >}}
