---
HasBanner: false
draft: false
sidebar: true
title: Ütemterv
type: page

---
{{<content-start >}}
# Ütemterv
{{<roadmap >}}

{{<button class="is-primary1 is-rounded" link="https://qgis.org/schedule.ics" text="Subscribe to the roadmap iCalendar" >}}

Releases and development of QGIS follow a timebased schedule (roadmap).
- A páros verziószámok (2.18, 3.2 stb.) a kiadott verziók.
- A páratlan verziószámok (2.99, 3.1, stb.) a fejlesztői verziók.

Minden negyedik hónapban történik egy kiadás. Az első három hónapban új fejlesztések zajlanak. A kiadás előtti utolsó hónapban a funkcióbővítést befagyasztjuk, az utolsó hónap pedig a tesztelésre, a hibajavításra, a fordításra és a kiadás előkészítésére szolgál. Amikor a kiadás megtörténik, egy páros kiadási számmal rendelkező ág jön létre, és a fő ág továbblép a következő páratlan verzióra. A kiadás után felhívást adunk ki a csomagkészítésre.

Minden harmadik kiadás (a 2.8 verziótól kezdve) egy hosszútávú kiadás (LTR), melyet a következő hosszútávú kiadás megjelenéséig karbantartunk.
## Fejlesztési fázis
A fejlesztési szakaszban a fejlesztők új funkciókat adnak a következő kiadáshoz. A korai alkalmazók a napi összeállításokat (nightly build) – melyet minden fontos platformra elkészítünk – használhatják a fejlesztési folyamat követésére, előzetes tesztelésre illetve hibajelentést küldhetnek, valamint megoszthatják gondolataikat, hogy segítsék a fejlesztést.
## Funkcióbővítés befagyasztása
In the feature freeze phase, new features are not allowed in anymore and the focus of everyone moves from enhancing QGIS to stabilizing it. This also turns the nightly builds effectively into [prereleases](#qgis-prereleases).

**Users** should start extensive testing of these prereleases in their environment to verify that there are no issues, they wouldn’t want to see in the upcoming release. All such issues should be reported (see [Bugs, Features and Issues]({{< ref "resources/support/bug-reporting" >}})). Everything that goes unnoticed, will also end up in the next release. Only in case of serious problems backports to a latest release will occur. Therefore testing of the prereleases and reporting issues is very important.

A befagyasztott funkcióbővítés alatt a **fejlesztők** figyelemmel követik a hibajegyeket és elkezdenek dolgozni a bejelentett problémák megoldásán, valamint frissítik a **vizuális változásnaplót** az általuk hozzáadott fejlesztésekkel.

A funkció bővítés befagyasztás kezdetekor a fordítási fájlokat aktualizálják, hogy a **fordítók** elkezdhessenek dolgozni. Vegye figyelembe, hogy ez egy többlépéses folyamat lehet, bár a funkció bővítést befagyasztották, a hibajavítás során változhatnak a lefordítandó szövegek is.

Két héttel a kiadás előtt elkezdődik a teljes befagyasztás, ami alatt csak a súlyos problémák és a funkcióbővítés kezdete óta bekerült regressziók javítását engedélyezik.

Ezt a kiadásfelelős jelenti be a funkcióbővítés befagyasztásakor.
## Kiadás
On major and minor release dates, the release branch is created and the release is tagged and tar balls are prepared. Point releases are just tagged and tar balls are created.

Értesítik a csomagkészítőket és megkezdődik a csomagkészítés.

Amint néhány csomag elérhetővé válik, a kiadást be lehet jelenteni, és ennek megfelelően frissül a webhely.
## Kiadási ütemterv
The schedule is aligned to produce roughly the same dates for each year given our four monthly releases with LTRs entering the LTR repo in late february.

Beginning after 2.12 the development phase is always 12 weeks and the freeze phase is at least 5 weeks. Remainders are used to extend the freeze phase of LTR releases.

Point releases will happen every month on the latest release branch, if there are backports. Beginning with the 3.28 release, point releases are only done with new latest releases.

In the first four months after its release, a new LTR is also the current LR. In this phase, the new LTR doesn’t replace the previous LTR in the LTR repositories. This happens as soon as a new LR is released.

This schedule is also available as [“iCalendar”](https://qgis.org/schedule.ics).
### Ütemterv
{{< csv-table file="csv/schedule.csv" />}}
### Az események magyarázata
{{< csv-table >}} "LTR","Long term release, begin of new development phase" "LR","Regular release, begin of new development phase" "FF","Feature freeze, end of development phase" "PR","Point release of latest release and LTR branch" "EPR","Extra Point release" ":rm-current:current",":rm-current:currently supported releases: {{< param "ltrrelease" >}} and {{< param "release" >}}" ":rm-next:next",":rm-next:next releases" {{< /csv-table >}}
## Előzetes kiadások / napi kiadások helye{#qgis-prereleases }
| Platform | Hely |
| --- | --- |
| Windows | [OSGeo4W]({{< ref "resources/installation-guide#online-osgeo4w-installer" >}}) |
| Linux | [Debian/Ubuntu]({{< ref "resources/installation-guide#repositories" >}}) |

<!-- |MacOS|[Mac OS]({{< ref "resources/installation-guide#qgis-nightly-release" >}})| -->

{{<content-end >}}
