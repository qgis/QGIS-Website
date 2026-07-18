---
HasBanner: false
draft: false
sidebar: true
title: Plan razvoja
type: page

---
{{<content-start >}}
# Plan razvoja
{{<roadmap >}}

{{<button class="is-primary1 is-rounded" link="https://qgis.org/schedule.ics" text="Pretplatite se na iCalendar plana razvoja" >}}

Izdanja i razvoj QGIS-a prate vremenski zasnovan raspored (plan razvoja).
- Parni brojevi verzija (2.18, 3.2 itd.) su izdate verzije.
- Neparni brojevi verzija (2.99, 3.1 itd.) su razvojne verzije.

Novo izdanje izlazi svaka četiri meseca. Prva tri meseca odvija se novi razvoj. Poslednjeg meseca pre izdanja uvodi se zamrzavanje mogućnosti, a taj mesec se koristi za testiranje, ispravke grešaka, prevođenje i pripremu izdanja. Kada izdanje izađe, kreira se grana sa parnim brojem izdanja, a master grana prelazi na sledeću neparnu verziju. Nakon izdanja upućuje se poziv za pakovanje.

Svako treće izdanje (počev od 2.8) je dugoročno izdanje (LTR) koje se održava do sledećeg dugoročnog izdanja.
## Faza razvoja
U fazi razvoja programeri rade na dodavanju novih mogućnosti za sledeće izdanje. Rani korisnici mogu da koriste noćne verzije koje pravimo za sve glavne platforme kako bi pratili napredak razvoja, obavili preliminarno testiranje i poslali prijave grešaka i svoja zapažanja koja pomažu razvoju.
## Zamrzavanje mogućnosti
U fazi zamrzavanja mogućnosti nove mogućnosti se više ne prihvataju i fokus svih prelazi sa unapređivanja QGIS-a na njegovo stabilizovanje. Time noćne verzije faktički postaju [predizdanja](#qgis-prereleases).

**Korisnici** treba da započnu opsežno testiranje ovih predizdanja u svom okruženju kako bi proverili da nema problema koje ne bi želeli da vide u nadolazećem izdanju. Sve takve probleme treba prijaviti (pogledajte [Greške, mogućnosti i problemi]({{< ref "resources/support/bug-reporting" >}})). Sve što prođe nezapaženo završiće i u sledećem izdanju. Prenošenje ispravki u najnovije izdanje dešava se samo u slučaju ozbiljnih problema. Zato su testiranje predizdanja i prijavljivanje problema veoma važni.

Tokom zamrzavanja mogućnosti **programeri** prate bagtreker i počinju da rade na ispravljanju prijavljenih problema, a **vizuelni spisak izmena** dopunjuju mogućnostima koje su dodali.

Sa početkom zamrzavanja mogućnosti ažuriraju se datoteke za prevod, kako bi **prevodioci** mogli da započnu svoj rad. Imajte u vidu da ovo može biti postupan proces jer, iako su mogućnosti zamrznute, ispravke grešaka i dalje mogu doneti izmene u tekstovima za prevod.

Dve nedelje pre izdanja uvodi se potpuno zamrzavanje, nakon kojeg se prihvataju samo ispravke ozbiljnih problema i regresija nastalih posle zamrzavanja mogućnosti.

Menadžer izdanja to objavljuje pri zamrzavanju mogućnosti.
## Ослободи
Na datume glavnih i manjih izdanja kreira se grana izdanja, izdanje se označava (tag) i pripremaju se tarball arhive. Servisna izdanja se samo označavaju i za njih se prave tarball arhive.

Pakerima se šalje obaveštenje da pakovanje može da počne.

Kada neki paketi postanu dostupni, izdanje se može objaviti, a sajt se u skladu s tim ažurira.
## Raspored izdanja
Raspored je usklađen tako da svake godine daje približno iste datume, s obzirom na naša izdanja na svaka četiri meseca i LTR verzije koje ulaze u LTR repozitorijum krajem februara.

Počev od verzije 2.12 faza razvoja uvek traje 12 nedelja, a faza zamrzavanja najmanje 5 nedelja. Preostalo vreme koristi se za produženje faze zamrzavanja LTR izdanja.

Servisna izdanja izlaze svakog meseca na grani najnovijeg izdanja, ako ima prenetih ispravki. Počev od izdanja 3.28, servisna izdanja se prave samo uz nova najnovija izdanja.

Prva četiri meseca nakon izlaska, novi LTR je ujedno i trenutni LR. U toj fazi novi LTR ne zamenjuje prethodni LTR u LTR repozitorijumima. To se dešava čim izađe novi LR.

Ovaj raspored je dostupan i kao [„iCalendar“](https://qgis.org/schedule.ics).
### Raspored
{{< csv-table file="csv/schedule.csv" />}}
### Legenda događaja
| Skraćenica | Опис |
| --- | --- |
| LTR | Dugoročno izdanje, početak nove faze razvoja |
| LR | Redovno izdanje, početak nove faze razvoja |
| FF | Zamrzavanje mogućnosti, kraj faze razvoja |
| PR | Servisno izdanje najnovijeg izdanja i LTR grane |
| EPR | Vanredno servisno izdanje |
| <span class="rm-current"> trenutno </span> | <span class="rm-current"> trenutno podržana izdanja: {{< param "ltrrelease" >}} i {{< param "release" >}} </span> |
| <span class="rm-next"> sledeće </span> | <span class="rm-next"> sledeća izdanja </span> |

## Lokacija predizdanja / noćnih verzija{#qgis-prereleases }
| Platforma | Локација |
| --- | --- |
| Windows | [OSGeo4W]({{< ref "resources/installation-guide#online-osgeo4w-installer" >}}) |
| Linux | [Debian/Ubuntu]({{< ref "resources/installation-guide#repositories" >}}) |

{{<content-end >}}
