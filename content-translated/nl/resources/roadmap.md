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

{{<button class="is-primary1 is-rounded" link="https://qgis.org/schedule.ics" text="Abonneren op het routeplan iCalendar" >}}

Uitgaven en ontwikkeling van QGIS volgen een op tijd gebaseerd schema (roadmap).
- Even versienummers (2.18, 3.2 etc) zijn  uitgaveversies.
- Oneven versienummers (2.99, 3.1 etc) zijn ontwikkelingsversies.

Elke vier maanden zal er een nieuwe uitgave zijn.  In de eerste drie maanden vindt nieuwe ontwikkeling plaats.  Dan, de laatste maand voor een uitgave, wordt een bevriezing van de mogelijkheden ingevoerd en de laatste maand wordt gebruikt voor het testen, oplossen van problemen, vertalen en voorbereidingen voor de uitgave.  Bij de uitgave wordt een tak met een even uitgavenummer gemaakt en de hoofdtak promoveert naar de volgende oneven versie.  Na de uitgave wordt een oproep uitgegeven voor het maken van de pakketten.

Elke derde uitgave (beginnend met 2.8) is een lange-termijn-uitgave (LTR) die wordt onderhouden totdat de volgende lange-termijn-uitgave verschijnt.
## Ontwikkelingsfase
In de ontwikkelingsfase werken ontwikkelaars aan het toevoegen van nieuwe mogelijkheden voor de volgende uitgave. Vroege deelnemers kunnen de nachtelijke builds, die we voor alle belangrijke platformen hebben, gebruiken om de voortgang van de ontwikkeling te bekijken, vroege testen te doen en rapporten voor problemen indienen en hun gedachten delen om met de ontwikkeling te helpen.
## Bevriezing
In de fase bevriezing worden nieuwe mogelijkheden niet meer toegestaan en de focus van iedereen verplaatst zich van het verbeteren van QGIS naar het stabiliseren ervan.  Dit wijzigt ook effectief de nachtelijke builds naar [voor-uitgaven](#qgis-prereleases).

**Gebruikers** zouden moeten beginnen met uitgebreid testen van deze voor-uitgaven in hun omgeving om te verifiëren dat er geen problemen zijn, die ze in de komende uitgave niet terug zouden willen zien.  Dergelijke problemen zouden allemaal moeten worden gerapporteerd (zie [Bugs, mogelijkheden en problemen]({{< ref "resources/support/bug-reporting" >}})). Alles wat niet wordt opgemerkt zal ook in de volgende uitgave zitten. Alleen in geval van serieuze problemen zal een backport naar de laatste uitgave plaatsvinden. Daarom is het testen van de voor-uitgaven en het rapporteren van problemen bijzonder belangrijk.

In de fase Bevriezing monitoren  **ontwikkelaars** het systeem voor problemen en beginnen met het herstellen van de gerapporteerde problemen en werken het **visuele log met wijzigingen** bij met de mogelijkheden die door hen werden toegevoegd.

Aan het begin van de bevriezing zullen de te vertalen bestanden worden bijgewerkt, zodat **vertalers** hun werk kunnen beginnen. Onthoud dat dit een voortdurend proces kan zijn, omdat, hoewel de mogelijkheden zijn bevroren, oplossingen van problemen nog steeds wijzigingen zouden kunnen opleveren in te vertalen tekenreeksen.

Twee weken voor de uitgave wordt een harde bevriezing uitgevoerd, waarna alleen reparaties aan ernstige problemen en regressies, geïntroduceerd na de bevriezing, zijn toegestaan om in te voegen.

De uitgavemanager kondigt dit aan bij het bevriezen van mogelijkheden.
## Uitgave
Op uitgavedatums van belangrijke en kleinere versies wordt de uitgavetak gemaakt en de uitgave wordt getagd en tarballs worden voorbereid. Puntuitgaven worden slechts getagd en worden tarballs gemaakt.

De inpakkers wordt bericht dat zij kunnen beginnen met inpakken.

Als enkele paketten beschikbaar zijn kan de uitgave worden aangekondigd en wordt de website overeenkomstig bijgewerkt.
## Uitgaveschema
Het schema is dusdanig ontworpen dat ruwweg op dezelfde datums in elk jaar onze viermaandelijkse uitgaven met LTR's worden geproduceerd waarbij eind februari de opslagplaats voor LTR wordt ingevoerd.

Beginnend na 2.12 is de ontwikkelfase altijd 12 weken en de vriesfase 5 weken. Herinneringen worden gebruikt om de vriesfase voor LTR-uitgaven te verlengen.

Puntuitgaven zullen elke maand worden uitgevoerd voor de laatste uitgavetak, als er terugkoppelingen zijn. Beginnend met de puntuitgave 3.28 worden uitgaven alleen nog uitgevoerd met de laatste nieuwe uitgaven.

In de eerste vier maanden na zijn uitgave is een nieuwe LTR ook de huidige LR. In deze fase vervangt de nieuwe LTR niet de voorgaande LTR in de opslagplaatsen van de LTR. Dat gebeurt zodra een nieuwe LR wordt uitgegeven.

Dit schema is ook beschikbaar als [“iCalendar”](https://qgis.org/schedule.ics).
### Schema
{{<csv-table file="csv/schedule.csv" >}}
### Legenda gebeurtenissen
| Afkorting | Beschrijving |
| --- | --- |
| LTR | Lange termijn uitgave, begin van nieuwe ontwikkelingsfase |
| LR | Reguliere uitgave, begin van nieuwe ontwikkelingsfase |
| FF | Vriesfase voor mogelijkheden, einde van de ontwikkelingsfase |
| PR | Puntuitgave van takken van laatste uitgave en van LTR |
| EPR | Extra puntuitgave |
| <span class="rm-current"> current </span> | <span class="rm-current"> currently supported releases: {{< param "ltrrelease" >}} and {{< param "release" >}} </span> |
| <span class="rm-next"> next </span> | <span class="rm-next"> next releases </span> |

## Locatie van pre-uitgaven / nachtelijke builds{#qgis-prereleases }
| Platform | Locatie |
| --- | --- |
| Windows | [OSGeo4W]({{< ref "resources/installation-guide#online-osgeo4w-installer" >}}) |
| Linux | [Debian/Ubuntu]({{< ref "resources/installation-guide#repositories" >}}) |

{{<content-end >}}
