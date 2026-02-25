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
În faza de înghețare, nu mai este permisă adăugarea de noi funcțiuni, centrul de greutate mutându-se spre sporirea stabilității QGIS. Acest lucru transformă efectiv compilările nocturne în [prelansări](#qgis-prereleases).

**Utilizatorii** ar trebui să înceapă testarea extensivă a acestor prelansări, în mediile proprii, pentru a verifica existența unor aspecte nedorite pentru viitoarea versiune. Toate acestea ar trebui să fie raportate (v. [Erori, Caracteristici și Probleme]({{< ref "resources/support/bug-reporting" >}})). Tot ceea ce trece neobservat, va fi înglobat, de asemenea, în următoarea versiune. Numai în cazul unor probleme grave se va efectua o retroportare. Prin urmare, testarea prelansărilor și raportarea problemelor este foarte importantă.

Pe perioada înghețării, **dezvoltatorii** monitorizează erorile, lucrează la rezolvarea problemelor raportate și introduc în **registrul schimbărilor** funcțiile nou adăugate.                               .

O dată cu începerea fazei de înghețare, fișierele de traducere vor fi actualizate în așa fel încât **traducătorii** să-și poată începe munca. Rețineți că acest proces poate fi incremental întrucât, deși funcționalitățile sunt înghețate, remedierea erorilor poate aduce modificări textelor de tradus.

Cu două săptămâni înainte de lansare, este inițiată o înghețare dură, în urma căreia sunt permise numai corecții la problemele grave și la regresiile introduse după înghețare.

Responsabilul lansărilor anunță intrarea în faza de înghețare.
## Lansarea
La momentul lansării unei versiuni majore se creează ramura de lansare, apoi se etichetează versiunea, după care se pregătesc arhivele TAR. Pentru versiunile minore au loc doar etichetarea și crearea arhivelor TAR.

Constructorii noilor versiuni sunt informați că poate începe împachetarea.

O dată ce pachetele sunt disponibile, lansarea poate fi anunțată și site-ul web este actualizat în consecință.
## Planificarea versiunilor
Lansările au loc o dată la patru luni, aproximativ în aceleași date ale fiecărui an, o nouă versiune cu suport pe termen lung intrând în depozitul LTR la sfârșitul lunii februarie.

Începând cu versiunea 2.12, faza de dezvoltare este de 12 săptămâni, iar faza de înghețare este de cel puțin 5 săptămâni. Pentru a extinde faza de înghețare a versiunilor LTR se folosesc notificări.

Versiunile minore au loc în fiecare lună, pe cea mai recentă ramură de dezvoltare, dacă există backport-uri. Începând cu versiunea 3.28, lansările au loc numai pentru ultima versiune majoră.

În primele patru luni după lansare, noul LTR are, de asemenea, calitatea de LR curent. În această fază, noul LTR nu înlocuiește LTR-ul anterior în depozitele LTR. Acest lucru se întâmplă imediat ce se lansează un nou LR.

Planificarea este disponibilă și sub formă de [“iCalendar”](https://qgis.org/schedule.ics).
### Programare
{{<csv-table file="csv/schedule.csv" >}}
### Legenda evenimentelor
| Abreviere | Descriere |
| --- | --- |
| LTR | Versiune cu suport pe termen lung; începerea unei noi faze de dezvoltate |
| LR | Versiune obișnuită; începerea unei noi faze de dezvoltare |
| FF | Înghețare caracteristici; sfârșitul fazei de dezvoltare |
| PR | Versiune minoră a ultimei versiuni și a ramurii LTR |
| EPR | Versiune Minoră Suplimentară |
| <span class="rm-current"> current </span> | <span class="rm-current"> currently supported releases: {{< param "ltrrelease" >}} and {{< param "release" >}} </span> |
| <span class="rm-next"> next </span> | <span class="rm-next"> next releases </span> |

## Locația prelansărilor / compilațiilor nocturne{#qgis-prereleases }
| Platformă | Locație |
| --- | --- |
| Windows | [OSGeo4W]({{< ref "resources/installation-guide#online-osgeo4w-installer" >}}) |
| Linux | [Debian/Ubuntu]({{< ref "resources/installation-guide#repositories" >}}) |

{{<content-end >}}
