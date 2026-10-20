---
HasBanner: false
Reviewed: 1 June 2024
Reviewer: Tim Sutton
draft: false
sidebar: true
title: Felhasználói csoportok
type: page

---
{{<content-start >}}
# Felhasználói csoportok
Local user groups bring QGIS users together in their own country and language. They run meetings, share know how and help shape QGIS. This page explains how a group works and how to start one.

{{<rich-box-start layoutClass="has-right rounded" >}}

{{<rich-content-start themeClass="coloring-1" >}}
## Find a group near you
Search the groups by name, country or continent. Switch between cards and a sortable table.

{{<button class="is-success" link="/community/groups/list/" text="Browse the list" >}}

{{<rich-content-end >}}

{{<rich-right-start >}}

{{<user-groups-stats "groups" "/community/groups/list/" >}}

{{<rich-right-end >}}

{{<rich-box-end >}}

{{<rich-box-start layoutClass="has-right rounded" >}}

{{<rich-content-start themeClass="coloring-1" >}}
## See the groups on a map
Every highlighted country has a local group. Select a logo to meet the group.

{{<button class="is-success" link="/community/groups/map/" text="Open the map" >}}

{{<rich-content-end >}}

{{<rich-right-start >}}

{{<user-groups-stats "countries" "/community/groups/map/" >}}

{{<rich-right-end >}}

{{<rich-box-end >}}
## A felhasználói csoportok céljai
* Felhasználói találkozók szervezése
* A fejlesztés összehangolása, különös tekintettel a regionális/nemzeti szabványokra és követelményekre
* A QGIS népszerűsítése: találkozók, cikkek GIS-szaklapokban, a QGIS-szel kapcsolatos információk a közösségi médiában, GIS-fórumok stb.
* Esettanulmányok gyűjteménye a QGIS helyi használatáról
* Szponzorálás: a helyi felhasználói csoportokat arra ösztönözzük, hogy (az országtól függően) ésszerű összegű éves tagsági díjat szedjenek be. A begyűjtött összegeket felhasználhatják a releváns funkciók fejlesztésének finanszírozására, a hibajavítások támogatására, vagy adományként a nemzetközi QGIS-projekt javára.
* Érdekcsoportok létrehozása, pl. földmérés, várostervezés, szerver/web kliens, stb.
* Alkalmazásmodulok elindítása és koordinálása, pl. felmérés, várostervezés, szerver/webes kliens stb.
* [QGIS szavazati joggal]({{< ref "/community/organisation#voting-members" >}}) rendelkező képviselő megválasztása

## Általános feltételezések és ajánlások
* a helyi felhasználói csoportoknak semlegesnek kell maradniuk a beszállítót/céget illetően
* demokratikus struktúrákat kell kialakítani a helyi irányító bizottság számára, szavazni és fontos döntéseket hozni
* átláthatónak kell maradni, különösen a tagsági díjakkal és azok elköltésével kapcsolatban
* időnként tájékoztassa a nemzetközi projektet a helyi tevékenységekről

## Szervezet
Az országtól függően létrehozható egy kisebb jogi személy, például egy egyesület vagy nonprofit szervezet. A helyi jogszabályoktól függően egy ilyen jogi személy létrehozása azt jelenti, hogy évente legalább egyszer össze kell ülni (közgyűlés), éves jelentést kell közzétenni, és a pénzügyi beszámolót a tagok rendelkezésére kell bocsátani. Ez általában az alapszabály megalkotását is magában foglalja.

A svájci QGIS felhasználói csoport alapszabálya mint példa:
* Német (eredeti): [https://www.qgis.ch/assets/pdf/StatutenderQGISAnwendergruppeSchweiz.pdf](https://www.qgis.ch/assets/pdf/StatutenderQGISAnwendergruppeSchweiz.pdf)
* Francia (fordítás): [https://www.qgis.ch/assets/pdf/StatutsdugroupedutilisateursQGISSuisse.pdf](https://www.qgis.ch/assets/pdf/StatutsdugroupedutilisateursQGISSuisse.pdf)

Tagsági jelentkezési űrlapok:
* Német: [https://www.qgis.ch/assets/pdf/QGIS%20Usergruppe%20Beitrittserklaerung.pdf](https://www.qgis.ch/assets/pdf/QGIS%20Usergruppe%20Beitrittserklaerung.pdf)
* Francia: [https://www.qgis.ch/assets/pdf/QGIS%20groupe%20d%20utilisateurs%20Suisse%20declaration%20d%20adhesion.pdf](https://www.qgis.ch/assets/pdf/QGIS%20groupe%20d%20utilisateurs%20Suisse%20declaration%20d%20adhesion.pdf)

Ezeket az alapszabályokat és a tagsági jelentkezési űrlapokat irányadóként használhatja, és a helyi viszonyokhoz igazodva szükség szerint módosíthatja őket.
## Helyi országos domain qgis.xx
User groups can register their local country domains, e.g. qgis.ch or qgis.uk. If the domain is already taken by another organization, company or person, please negotiate if you can transfer the owner to the local QGIS user group. The QGIS international project has registered [QGIS as a trademark](../organisation/guidelines), which should help you during your negotiations.
## Honlap
A helyi felhasználói csoport weboldalát a felhasználói csoporttal kapcsolatos információk és az irányításhoz kapcsolódó anyagok közzétételére kell használni. Példák: felhasználói találkozók, esettanulmányok, megosztott anyagok, fórumok stb. A nyilvános anyagokhoz nem szabad bejelentkezést követelni (pl. ne legyen feltétel, hogy az érdeklődőknek tagjainak kell lenniük egy közösségi hálózaton, mint a Facebook vagy a Google+). A közösségi hálózatok használatát javasoljuk, de ne ez legyen az egyetlen információs csatorna. A QGIS felhasználói csoport honlapján RSS hírcsatornát célszerű létrehozni.

Sok sikert az ön helyi felhasználói csoportjának szervezéséhez. Kérjük, értesítse a nemzetközi csoportot, regisztráljon a QGIS közösségi listán és számoljon be a haladásról. Ne habozzon kérdéseket feltenni a helyi felhasználói csoport létrehozásával és fenntartásával kapcsolatban.
## Kezdőcsomag
### QGIS.org aldomain-tárhely
User groups are encouraged to use the official QGIS.org branding and host the user group's website on a QGIS.org subdomain (e.g., `sweden.qgis.org`), you can utilize the provided template repository at [https://github.com/qgis/QGIS-User-Group-Website](https://github.com/qgis/QGIS-User-Group-Website). This option ensures consistency with the main QGIS website design. Please carefully read and follow the setup instructions provided in the repository.
### Hozzáférés a QGIS hírcsatornához
A helyi felhasználói csoportok hozzáférést kérhetnek a [QGIS hírcsatorna-rendszerhez](https://feed.qgis.org), amelyen keresztül híreket (például rendezvényeket, közösségi finanszírozási kampányokat, találkozókat vagy közleményeket) tehetnek közzé, amelyek a moderátorok jóváhagyását követően megjelennek a QGIS hírek részében. Ez kiváló lehetőség arra, hogy csoportjuk tevékenységét megosszák a globális QGIS-közösséggel.
### Sablon a helyi országkódú qgis.xx domainhez
If you do not wish to use the QGIS.org subdomain hosting you can design your website using the template provided at [https://github.com/qgis/qgis-template.github.io](https://github.com/qgis/qgis-template.github.io) or create your own from scratch.

{{<content-end >}}
