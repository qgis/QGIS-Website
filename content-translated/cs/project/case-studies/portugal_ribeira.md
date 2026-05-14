---
HasBanner: false
archived: true
date: 2012-07-01
draft: false
featured: false
section: projekt
sidebar: true
thumbnail: images/portugal_ribeira1.png
title: QGIS a GRASS pro modelování ekologických koridorů pro vlky v severním Portugalsku
type: case-study

---
{{<content-start >}}
# QGIS a GRASS pro modelování ekologických koridorů pro vlky v severním Portugalsku
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>July 01, 2012</span>
</p>

The Iberian wolf is a sub-species of the gray wolf that exists only in north of Portugal and Spain, with small isolated groups in the south of Douro river. During the last century, it suffered a high regression, being a "vulnerable" species in Spain and "endangered" in Portugal. Nowadays, there are only around 300 wolves in Portugal, due to the high persecution, destruction and fragmentation of the habitat.

<figure>
<img src="../images/portugal_ribeira1.png" class="align-right" alt="portugal_ribeira1.png" />
<figcaption>Study area in Portugal</figcaption>
</figure>

Ribeira de Pena je obec v okrese Vila Real na severu Portugalska. Je to venkovská obec, pro kterou je charakteristické zemědělství, pastva hospodářských zvířat, lesy, hory, údolí a rozmanitá fauna spolu s nízkou hustotou osídlení, která poskytuje útočiště a potravu vlkům. Ribeira de Pena se nachází v přechodové zóně mezi drsným a hornatým Trás-os-Montes a zeleným Minho a je jednou z obcí, které mohou fungovat jako ekologický koridor mezi oblastmi s vyšší koncentrací vlků na severu a nižší koncentrací na jihu.

Software GIS jsem začal používat během studia biologie a častěji během psaní diplomové práce. V té době jsem používal především proprietární software. Po dokončení magisterského studia jsem k proprietárnímu softwaru ztratil přístup.

Mezitím jsem vstoupil do nového světa Linuxu. Poté jsem byl osloven, abych pomohl několika výzkumníkům modelovat ekologické koridory pro vlky v Ribeira de Pena pomocí GIS, protože s tímto druhem softwaru nikdy nepracovali. Protože jsem již používal Linux místo Windows, mým prvním problémem bylo, jaký software použít. Pak jsem se doslechl o QGIS a rozhodl jsem se ho vyzkoušet, i když se mi zdál velmi zjednodušený a neúplný ve srovnání s tím, co jsem již znal. Rychle jsem si uvědomil, jak jsem se mýlil, a opravdu mě nadchly analytické možnosti, které QGIS poskytoval, speciálně s integrací GRASS.

K modelování ekologických koridorů jsme použili QGIS spolu s pluginem GRASS. K modelování ekologických koridorů jsme použili několik geografických informací spolu s údaji o výskytu druhů. Zde jsou uvedeny některé z funkcí QGIS i GRASS, které byly v tomto případě použity, a to jen některé:
- zásuvný modul Interpolace v QGIS: vytvoření digitálního modelu reliéfu
- r.watershed v GRASS: vytvoření vodních toků z DEM
- r.grow.distance v GRASS: generuje rastrovou mapovou vrstvu vzdáleností k prvkům ve vstupní vrstvě.
- r.reclass v GRASS: reklasifikace mapových vrstev
- r.slope.aspect.slope v GRASS: výpočet sklonu z DEM
- r.mapcalculator v GRASSu: výpočet jednoduché mapové algebry
- r.cost.coord v GRASS: vytvoří rastrovou mapu zobrazující kumulativní náklady na pohyb mezi různými geografickými místy na vstupní rastrové mapě, jejíž hodnoty kategorií buněk představují náklady.
- r.drain in GRASS: Traces a flow through an elevation model on a raster map — the one used to create the corridors

Díky této práci jsme získali mapu s potenciálními ekologickými koridory pro vlka v obci Ribeira de Pena. Jedná se o oblasti, které by měli vzít v úvahu technici městské rady při plánování ochranných opatření pro tento druh. Tyto koridory mají mimořádný význam, protože mohou propojit křehké vlčí smečky ve Vila Realu na jihu s těmi na severu, které jsou kontinuální s těmi z Peneda-Gerês a Španělska mnohem stabilnější. Zvláštní význam mají ty koridory, které protínají lidská sídla, jako jsou malé vesnice, města a silnice. Tyto oblasti je třeba považovat za kritické pro ochranu vlka a uplatňovat opatření ke snížení vlivu člověka na tento druh.

<figure>
<img src="../images/portugal_ribeira2.png" class="align-right" style="width:100.0%" alt="portugal_ribeira2.png" />
<figcaption>Ecological corridors and critical conservation areas for wolves in northern Portugal.</figcaption>
</figure>

## Závěr
Both QGIS and plugin GRASS are very intuitive with user-friendly interface, with all essential functions to perform most analysis. For what I could see, QGIS and GRASS perform equally as well as the proprietary programs I was most familiar with from college days, with the big advantage of free open-source software, usable in every computer or notebook without licenses, constant upgrades and the ultimate advantage to contribute to it\'s improvement and/or tip the developers about some essential function.

Changing to Linux and then to QGIS and GRASS was one of my best calls, and although there can be some missing issues, easily resolved in the future with the developers, I don\'t regret my decision and advise everyone to use them.
## Autor
<figure>
<img src="../images/portugal_ribeiraaut.png" class="align-left" height="200" alt="portugal_ribeiraaut.png" />
<figcaption>Monica Almeida</figcaption>
</figure>

Do tohoto článku přispěla v červenci 2012 Monica Almeida. Je ochranářskou bioložkou, která pracuje v nevládní organizaci zabývající se ochranou vlka v Portugalsku.

{{<content-end >}}
