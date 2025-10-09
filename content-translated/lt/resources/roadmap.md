---
HasBanner: false
draft: false
sidebar: true
title: Planas
type: page

---
{{<content-start >}}
# Planas
{{<roadmap >}}

{{<button class="is-primary1 is-rounded" link="https://qgis.org/schedule.ics" text="Subscribe to the roadmap iCalendar" >}}

QGIS laidos ir kūrimas vykdomi pagal laiku paremtą grafiką (planą).
- Lyginiai numeriai (2.18, 3.2 ir pan.) yra laidos versijos.
- Nelyginiai numeriai (2.99, 3.1 ir pan.) yra kūrimo versijos.

Nauja laida leidžiama kas keturis mėnesius. Pirmus tris mėnesius vyksta naujų funkcijų kūrimas. Paskutinį laidos mėnesį naujų savybių pridėjimas užšaldomas, galutinis mėnuo naudojamas testavimui, riktų taisymui, vertimui ir pasiruošimui laidai. Įvykus laidai padaroma šaka su lyginiu laidos numeriu, pagrindinė šaka persijungia į tolimesnę nelyginę versiją. Po laidos pradedamas pakavimas.

Kas trečia laida (pradedant nuo 2.8) yra ilgo laikotarpio laida (LTR), kuri palaikoma tol, kol išleidžiama kita LTR laida.
## Kūrimo fazė
Kūrimo fazėje programuotojai prideda naujas funkcijas į kitą laidą. Ankstyvieji bandytojai gali naudoti kasnaktines versijas, kurias ruošiame visoms pagrindinėms platformoms, kur galima pažiūrėti kūrimo progresą, vykdyti preliminarų testavimą ir teikti reiktų pranešimus ir kitas mintis, padedančias kūrimui.
## Funkcionalumo užšaldymas
In the feature freeze phase, new features are not allowed in anymore and the focus of everyone moves from enhancing QGIS to stabilizing it. This also turns the nightly builds effectively into [prereleases](#qgis-prereleases).

**Users** should start extensive testing of these prereleases in their environment to verify that there are no issues, they wouldn’t want to see in the upcoming release. All such issues should be reported (see [Bugs, Features and Issues]({{< ref "resources/support/bug-reporting" >}})). Everything that goes unnoticed, will also end up in the next release. Only in case of serious problems backports to a latest release will occur. Therefore testing of the prereleases and reporting issues is very important.

Funkcionalumo užšaldymo metu **kūrėjai** seka riktų registravimo sistemą ir taiso praneštas problemas bei atnaujina **vizualų pakeitimų sąrašą**, papildydami jį savo pridėtu funkcionalumu.

Užšaldžius funkcionalumą atnaujinami vertimų failai, kad **vertėjai** galėtų pradėti darbą. Pastebėtina, kad tai gali būti palaipsninis procesas, nors funkcionalumas ir užšaldytas, gali būti pridedami riktų pataisymai, kuriuose keičiamos vertimų eilutės.

Dvi savaites iki laidos įvykdomas pilnas užšaldymas, po kurio pridedami tik labai rimtų problemų pataisymai ir regresijos, atsiradusios po funkcionalumo užšaldymo.

Laidos valdytojas praneša apie funkcionalumo užšaldymą.
## Laida
On major and minor release dates, the release branch is created and the release is tagged and tar balls are prepared. Point releases are just tagged and tar balls are created.

Pakuotojams pranešama, kad galima pradėti pakavimą.

Kai paketai paruošiami, galima pranešti apie laidą, atitinkamai atnaujinama ir svetainė.
## Laidų planas
Planas derinamas taip, kad kiekvienais metais tuo pačiu metu būtų kuriamos mūsų keturios mėnesinės laidos, o vėlai vasarį - LTR - ilgalaikė laida.

Beginning after 2.12 the development phase is always 12 weeks and the freeze phase is at least 5 weeks. Remainders are used to extend the freeze phase of LTR releases.

Point releases will happen every month on the latest release branch, if there are backports. Beginning with the 3.28 release, point releases are only done with new latest releases.

In the first four months after its release, a new LTR is also the current LR. In this phase, the new LTR doesn’t replace the previous LTR in the LTR repositories. This happens as soon as a new LR is released.

This schedule is also available as [“iCalendar”](https://qgis.org/schedule.ics).
### Planas
{{<csv-table file="csv/schedule.csv" >}}
### Įvykių sutartiniai ženklai
| Abbreviation | Aprašymas |
| --- | --- |
| LTR | Ilgalaikė laida, naujos kūrimo fazės pradžia |
| LR | Paprasta laida, naujos kūrimo fazės pradžia |
| FF | Funkcionalumo užšaldymas, kūrimo fazės pabaiga |
| PR | Paskutinės laidos taškinė laida ir LTR šaka |
| EPR | Papildoma taškinė laida |
| :rm-current:current | :rm-current:currently supported releases: {{< param "ltrrelease" >}} and {{< param "release" >}} |
| :rm-next:next | :rm-next:next releases |

## Išankstinių laidų vieta / kasnaktinės versijos{#qgis-prereleases }
| Platforma | Vieta |
| --- | --- |
| Windows | [OSGeo4W]({{< ref "resources/installation-guide#online-osgeo4w-installer" >}}) |
| Linux | [Debian/Ubuntu]({{< ref "resources/installation-guide#repositories" >}}) |

{{<content-end >}}
