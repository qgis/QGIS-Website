---
HasBanner: false
draft: false
sidebar: true
title: Färdplan
type: page

---
{{<content-start >}}
# Färdplan
{{<roadmap >}}

{{<button class="is-primary1 is-rounded" link="https://qgis.org/schedule.ics" text="Prenumerera på färdplanen iCalendar" >}}

Utgåvor och utveckling av QGIS följer ett tidsbaserat schema (roadmap).
- Även versionsnummer (2.18, 3.2 etc) är releaseversioner.
- Udda versionsnummer (2.99, 3.1 etc) är utvecklingsversioner.

En ny release kommer att ske var fjärde månad. Under de första tre månaderna sker nyutveckling. Under den sista månaden före en release fryses utvecklingen och den sista månaden används för testning, buggfixning, översättning och förberedelser inför releasen. När releasen sker skapas en gren med ett jämnt versionsnummer och mastergrenen går vidare till nästa udda version. Efter releasen skickas en uppmaning om paketering ut.

Var tredje release (från och med 2.8) är en långtidsrelease (LTR) som underhålls tills nästa långtidsrelease inträffar.
## Utvecklingsfas
I utvecklingsfasen arbetar utvecklarna med att lägga till nya funktioner för nästa release. Tidiga användare kan använda de nattliga builds som vi har för alla större plattformar för att se hur utvecklingen fortskrider, göra preliminära tester och skicka in felrapporter och tankar som kan hjälpa till med utvecklingen.
## Versionsfrysning
I fasen för funktionsfrysning tillåts inte nya funktioner längre och allas fokus flyttas från att förbättra QGIS till att stabilisera det. Detta förvandlar också de nattliga builds effektivt till [prereleases] (#qgis-prereleases).

**Användare** bör påbörja omfattande tester av dessa prereleaser i sin miljö för att verifiera att det inte finns några problem som de inte vill se i den kommande releasen. Alla sådana problem bör rapporteras (se [Buggar, funktioner och problem]({{< ref "resources/support/bug-reporting" >}})). Allt som går obemärkt förbi kommer också att hamna i nästa version. Endast i händelse av allvarliga problem kommer bakåtporter till en senaste version att ske. Därför är det mycket viktigt att testa prereleaser och rapportera problem.

Under funktionsfrysningen övervakar **utvecklarna** buggtrackern och börjar arbeta med att åtgärda de rapporterade problemen och uppdaterar den **visuella ändringsloggen** med de funktioner som de har lagt till.

När funktionsfrysningen inleds kommer översättningsfilerna att uppdateras så att **översättare** kan påbörja sitt arbete. Observera att detta kan vara en stegvis process eftersom buggfixar fortfarande kan medföra ändringar i översättningssträngarna, även om funktionerna är frysta.

Två veckor före lanseringen inleds en hård frysning, varefter endast korrigeringar av allvarliga problem och regressioner som införts efter funktionsfrysningen tillåts.

Release manager meddelar detta vid feature freeze.
## Version
På datum för större och mindre releaser skapas release-grenen och releasen taggas och tar balls förbereds. Point-releaser taggas bara och tar balls skapas.

Packarna meddelas att packningen kan påbörjas.

När vissa paket är tillgängliga kan lanseringen meddelas och webbplatsen uppdateras i enlighet med detta.
## Släppschema
Schemat är anpassat för att ge ungefär samma datum för varje år med tanke på våra fyra månatliga utgåvor med LTR som kommer in i LTR-repån i slutet av februari.

Från och med 2.12 är utvecklingsfasen alltid 12 veckor och frysningsfasen är minst 5 veckor. Remainders används för att förlänga frysningsfasen för LTR-utgåvor.

Punktutgåvor kommer att ske varje månad på den senaste utgåveförgreningen, om det finns backports. Från och med utgåva 3.28 görs punktutgåvor endast med nya senaste utgåvor.

Under de första fyra månaderna efter utgivningen är en ny LTR också den aktuella LR. Under denna fas ersätter den nya LTR inte den tidigare LTR i LTR-arkivet. Detta sker så snart en ny LR har släppts.

Detta schema finns även tillgängligt som ["iCalendar"] (https://qgis.org/schedule.ics).
### Schema
{{<csv-table file="csv/schedule.csv" >}}
### Händelseförklaring
| Förkortning | Beskrivning |
| --- | --- |
| LTR | Långsiktig utgåva, början på en ny utvecklingsfas |
| LR | Regelbunden lansering, början på ny utvecklingsfas |
| FF | Funktionsfrysning, slutet av utvecklingsfasen |
| PR | Punktutgåva för senaste utgåva och LTR-förgrening |
| EPR | Extra punktutgåva |
| <span class="rm-current"> current </span> | <span class="rm-current"> currently supported releases: {{< param "ltrrelease" >}} and {{< param "release" >}} </span> |
| <span class="rm-next"> next </span> | <span class="rm-next"> next releases </span> |

## Plats för förhandsversioner/nattliga byggen{#qgis-prereleases }
| Plattform | Plats |
| --- | --- |
| Windows | [OSGeo4W]({{< ref "resources/installation-guide#online-osgeo4w-installer" >}}) |
| Linux | [Debian/Ubuntu]({{< ref "resources/installation-guide#repositories" >}}) |

{{<content-end >}}
