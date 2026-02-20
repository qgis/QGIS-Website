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

{{<button class="is-primary1 is-rounded" link="https://qgis.org/schedule.ics" text="Feliratkozás az iCalendar ütemtervre" >}}

A QGIS kiadása és fejlesztése időalapú ütemezés (ütemterv) szerint történik.
- A páros verziószámok (2.18, 3.2 stb.) a kiadott verziók.
- A páratlan verziószámok (2.99, 3.1, stb.) a fejlesztői verziók.

Minden negyedik hónapban készül egy új kiadás. Az első három hónapban új fejlesztések zajlanak. A kiadás előtti utolsó hónapban a funkcióbővítést befagyasztjuk, az utolsó hónap pedig a tesztelésre, a hibajavításra, a fordításra és a kiadás előkészítésére szolgál. Amikor a kiadás elkészül, egy páros kiadási számmal rendelkező ág jön létre, és a fő ág továbblép a következő páratlan verzióra. A kiadás után felhívást adunk ki a csomagkészítésre.

Minden harmadik kiadás (a 2.8 verziótól kezdve) egy hosszútávú kiadás (LTR), melyet a következő hosszútávú kiadás megjelenéséig karbantartunk.
## Fejlesztési fázis
A fejlesztési szakaszban a fejlesztők új funkciókat adnak a következő kiadáshoz. A korai alkalmazók a napi összeállításokat (nightly build) – melyet minden fontos platformra elkészítünk – használhatják a fejlesztési folyamat követésére, előzetes tesztelésre illetve hibajelentést küldhetnek, valamint megoszthatják gondolataikat, hogy segítsék a fejlesztést.
## Funkcióbővítés befagyasztása
A funkció bővítés befagyasztásának időszakban új funkcionalitás hozzáadása tilos, mert a hangsúly a QGIS bővítéséről a stabilizálásra helyeződik át. A napi kiadások [előzetes kiadássá](#qgis-prereleases) változnak.

A **felhasználóknak** el kell kezdeniük ezen előzetes kiadások alapos tesztelését a saját környezetükben, hogy megbizonyosodjanak arról, hogy nincsenek olyan problémák, amelyeket nem szeretnének látni a közelgő kiadásban. Minden ilyen problémát jelenteni kell (lásd [Hibák, funkciók és problémák ]({{< ref "resources/support/bug-reporting" >}})). Minden amit nem vesznek észre, benne marad következő kiadásban. A legutolsó kiadásba csak súlyos probléma esetén történik meg a hibajavítások visszaépítése, ezért az előzetes kiadások tesztelése és a problémák jelentése nagyon fontos.

A befagyasztott funkcióbővítés alatt a **fejlesztők** figyelemmel kísérik a hibajegyeket, és elkezdenek dolgozni a bejelentett problémák megoldásán, valamint frissítik a **vizuális változásnaplót** az általuk hozzáadott fejlesztésekkel.

A funkcióbővítés befagyasztása kezdetekor a fordítási fájlokat aktualizálják, hogy a **fordítók** elkezdhessenek dolgozni. Vegye figyelembe, hogy ez egy többlépéses folyamat lehet, bár a funkció bővítést befagyasztották, a hibajavítás során változhatnak a lefordítandó szövegek is.

Két héttel a kiadás előtt elkezdődik a teljes befagyasztás, ami alatt csak a súlyos problémák és a funkcióbővítés kezdete óta bekerült regressziók javítását engedélyezik.

Ezt a kiadásfelelős jelenti be a funkcióbővítés befagyasztásakor.
## Kiadás
A főverziók és alverziók megjelenése napján létrehoznak egy új fejlesztési ágat és megcímkézik a kiadást, valamint előkészítik a tar csomagokat. Hibajavító kiadás esetén nem jön létre új fejlesztési ág.

Értesítik a csomagkészítőket és megkezdődik a csomagkészítés.

Amint néhány csomag elérhetővé válik, a kiadást be lehet jelenteni, és ennek megfelelően frissül a webhely.
## Kiadási ütemterv
Az ütemtervet úgy alakítottuk ki, hogy a rendszeres, négy hónaponkénti kiadásokat követően az LTR-ek minden évben közel azonos időpontban, február végén kerüljenek LTR fázisba.

A 2.12-es verzió óta a fejlesztési fázisok mindig 12 hetesek és a befagyasztási fázisok legalább 5 hetesek. A fennmaradó időt az LTR kiadások befagyasztási idejének kiterjesztésére használjuk.

Hibajavító kiadások havonta készülnek a legfrissebb kiadási ágon, ha vannak visszaépítendő javítások. A 3.28-as kiadástól kezdve pontkiadások csak az új, legfrissebb kiadásokhoz készülnek.

A megjelenést követő első négy hónapban az új LTR (hosszútávú kiadás) egyben a jelenlegi LR (legutóbbi kiadás) is. Ebben a fázisban az új LTR még nem váltja fel a korábbi LTR-t az LTR-tárolókban. Ez csak a következő LR verzió megjelenésekor történik meg.

Ez az ütemezés [“iCalendar”](https://qgis.org/schedule.ics) formában is elérhető.
### Ütemterv
{{<csv-table file="csv/schedule.csv" >}}
### Az események magyarázata
| Rövidítés | Leírás |
| --- | --- |
| LTR | Hosszútávú kiadás (Long Term Release), egy új fejlesztési fázis kezdete |
| LR | Rendes kiadás (Latest Release), egy új fejlesztési fázis kezdete |
| FF | Funkcióbővítés befagyasztása (Feature Freeze), fejlesztési fázis vége |
| PR | Hibajavító kiadás (Point Release) a legutóbbi kiadásból és az LTR ágból |
| EPR | Extra hibajavító kiadás |
| <span class="rm-current"> current </span> | <span class="rm-current"> currently supported releases: {{< param "ltrrelease" >}} and {{< param "release" >}} </span> |
| <span class="rm-next"> next </span> | <span class="rm-next"> next releases </span> |

## Előzetes kiadások / napi kiadások helye{#qgis-prereleases }
| Platform | Hely |
| --- | --- |
| Windows | [OSGeo4W]({{< ref "resources/installation-guide#online-osgeo4w-installer" >}}) |
| Linux | [Debian/Ubuntu]({{< ref "resources/installation-guide#repositories" >}}) |

{{<content-end >}}
